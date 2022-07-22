# pylint: disable = C0103, R0902, W1203, C0301
"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import json
import logging
import traceback
import os
import os.path
import datetime
from datetime import timezone, datetime
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)


######################################################################
#                        CLASS DEFINITION                            #
######################################################################

class GluePartitionManager:
    """
    GluePartitionManager Controller class. Handles all logic related to Glue Partitions.
    """

    # INIT
    def __init__(self, event, context):

        self.session_id = boto3.session.Session().client('sts').get_caller_identity()
        self.account_id = boto3.client('sts').get_caller_identity()['Account']
        self.deployment_region = os.environ.get('DeploymentRegion')
        if not self.deployment_region:
            self.deployment_region = boto3.session.Session().region_name

        # Parameter to configure AWS Glue partitions
        self.glue_database_name = os.environ.get('GlueDatabaseName')
        self.glue_table_name_list = []
        if os.environ.get('GlueTableNameList'):
            self.glue_table_name_list = os.environ.get(
                'GlueTableNameList').strip().split(',')

        self.glue_s3_path_exclusions = os.environ.get(
            'GlueS3PathPathExclusions')
        self.glue_table_partition_cache_key = os.environ.get(
            'GlueTablePartitionCacheKey')
        if not self.glue_table_partition_cache_key:
            self.glue_table_partition_cache_key = 'GlueCache'

        self.s3_glue_log_bucket = os.environ.get('GlueCacheBucket')
        self.lambda_temp_path = '/tmp'  # nosec

        self.s3_locations_list = []
        self.table_details_cache = []
        if self.glue_database_name:
            self.s3_location_details_cache_key = self.glue_table_partition_cache_key + \
                '/' + self.glue_database_name + '/s3_locations'

    def refresh_initial_partitions_from_bucket(self):
        """
        This method is responsible to refresh the Glue partition information based on the
        exist data in S3
        """
        if not self.s3_locations_list:
            self.__get_s3_locations_list()

        logger.info(
            f"refresh_initial_partitions_from_bucket with : {self.s3_locations_list}")

        try:
            for table_details in self.s3_locations_list:
                for table_name in table_details:
                    s3_folder = table_details[table_name]
                    self.refresh_initial_partitions_from_folder(s3_folder)
        except (Exception):
            var = traceback.format_exc()
            logger.error(
                f"Error {var} in refresh_initial_partitions_from_bucket processing : {table_details}")

        logger.info("Finished refresh_initial_partitions_from_bucket")

    def refresh_initial_partitions_from_folder(self, folder_name):
        """
        This method is responsible to refresh the Glue partition information based on the
        exist data in S3 folder (folder_name)
        """
        logger.info(
            f"refresh_initial_partitions_from_folder with : folder_name : {folder_name}")
        # Get the list of contents from the table
        s3_client = boto3.client('s3', region_name=self.deployment_region)
        response = s3_client.list_objects_v2(Bucket=self.s3_glue_log_bucket,
                                             Delimiter='/',
                                             Prefix=folder_name)
        if 'Contents' in response:
            for key_info in response['Contents']:
                s3_key = key_info['Key']
                self.update_glue_partition_for_s3_key(s3_key)
                # TODO : Hot Fix. Process a single file in the folder
                return
        elif 'CommonPrefixes' in response and len(response['CommonPrefixes']) > 0:
            for commonPrefix in response['CommonPrefixes']:
                self.refresh_initial_partitions_from_folder(
                    commonPrefix['Prefix'])
        else:
            logger.info(
                f'NO Report file exists in the location : {folder_name} on {self.s3_glue_log_bucket}')

        logger.info("Finished refresh_initial_partitions_from_folder")

    def refresh_existing_table_details_cache(self):
        """
        This method will create cache entries corresponding to the Glue database name including
        locations list
        """
        self.table_details_cache = []
        self.s3_locations_list = []
        glue_client = boto3.client('glue', region_name=self.deployment_region)
        get_tables_response = glue_client.get_tables(
            DatabaseName=self.glue_database_name)
        table_dict_list = get_tables_response['TableList']
        if len(self.glue_table_name_list) <= 0:
            self.glue_table_name_list = [
                table_dict['Name'] for table_dict in table_dict_list if 'Name' in table_dict]
        logger.info(f'Processing table list : {self.glue_table_name_list}')
        for table_dict in table_dict_list:
            self.refresh_table_details_cache_with_details(table_dict)

        self.__write_object_to_s3(self.s3_glue_log_bucket, self.s3_location_details_cache_key,
                                  {'s3_locations': self.s3_locations_list},
                                  self.glue_table_partition_cache_key)

    def refresh_table_details_cache_with_details(self, table_dict):
        table_name_in_dict = table_dict['Name']
        if table_name_in_dict in self.glue_table_name_list:
            logger.info(f'Adding : {table_name_in_dict} to the cache')
            # Persist the details to an S3 location
            table_details_cache_key = self.glue_table_partition_cache_key + \
                '/' + self.glue_database_name + '/' + table_name_in_dict
            self.__write_object_to_s3(self.s3_glue_log_bucket, table_details_cache_key, table_dict,
                                      self.glue_table_partition_cache_key)

            self.table_details_cache.append(
                {'Name': table_name_in_dict, 'Details': table_dict})
            if 'StorageDescriptor' in table_dict and 'Location' in table_dict['StorageDescriptor']:
                s3_location = table_dict['StorageDescriptor']['Location']
                s3_location = s3_location.replace(
                    f"s3://{self.s3_glue_log_bucket}/", "")
                self.s3_locations_list.append(
                    {table_name_in_dict: s3_location})
        else:
            logger.info(f'Skipping processing of table : {table_name_in_dict}')

    def refresh_table_details_cache(self, table_name):
        glue_client = boto3.client('glue', region_name=self.deployment_region)
        get_table_response = glue_client.get_table(
            DatabaseName=self.glue_database_name, Name=table_name)
        table_dict = get_table_response.get('Table')
        if table_dict:
            self.refresh_table_details_cache_with_details(table_dict)

    def __get_s3_locations_list(self):
        """
        This method will fetch the existing s3 locations list for all tables in the configuration
        from s3 cache
        """

        os.chdir(self.lambda_temp_path)
        try:
            s3_resource = boto3.resource('s3')
            s3_resource.Bucket(self.s3_glue_log_bucket).download_file(self.s3_location_details_cache_key,
                                                                      's3_locations')
            s3_locations = json.load(open('s3_locations', "r"))
            self.s3_locations_list = s3_locations['s3_locations']
        except ClientError as e:
            if e.response['Error']['Code'] == "404":
                logger.error(
                    "s3_locations cache doesn't exist. Refreshing data.")
                # Location Cache is missing. refresh it
                self.refresh_existing_table_details_cache()
            else:
                raise

    def __get_table_details_from_cache(self, table_name):
        """
        This method will fetch the existing table details from the s3 cache
        """
        try:
            table_details = None
            table_details_array = [
                x['Details'] for x in self.table_details_cache if x['Name'] == table_name]
            if table_details_array and len(table_details_array) > 0:
                table_details = table_details_array[0]

            if not table_details:
                table_details_cache_key = self.glue_table_partition_cache_key + \
                    '/' + self.glue_database_name + '/' + table_name
                os.chdir(self.lambda_temp_path)
                s3_resource = boto3.resource('s3')
                s3_resource.Bucket(self.s3_glue_log_bucket).download_file(
                    table_details_cache_key, table_name)
                table_details = json.load(open(table_name, "r"))
        except ClientError as e:
            if e.response['Error']['Code'] == "404":
                logger.error(
                    "table_name cache doesn't exist. Refreshing data.")
                # Location Cache is missing. refresh it
                self.refresh_table_details_cache(table_name)
            else:
                raise

        return table_details

    def __write_partition_keys_to_cache(self, table_name, partitions_to_create):
        """
        Helper function to write the partition information to the local cache
        """
        partition_cache_key = self.glue_table_partition_cache_key + '/' + table_name + '/' + '_'.join(
            partitions_to_create)
        key_creation_time = datetime.now(timezone.utc)
        logger.info(
            f"Bucket : {self.s3_glue_log_bucket} , Key : {partition_cache_key} ,Body : {json.dumps(key_creation_time, default=str, separators=(',', ':'))}")
        self.__write_object_to_s3(self.s3_glue_log_bucket, partition_cache_key, key_creation_time,
                                  self.glue_table_partition_cache_key)

    def __write_object_to_s3(self, s3_log_bucket, s3_log_location, json_content, write_source):
        """
        This method is responsible for writing the json_content to the s3 Bucket (s3_log_bucket)
        under (s3_log_location)
        """
        try:
            s3_client = boto3.client('s3', region_name=self.deployment_region)
            logger.info(f"Logging {s3_log_location} to {s3_log_bucket}")
            s3_client.put_object(Body=json.dumps(json_content,
                                                 default=str, separators=(',', ':')),
                                 Bucket=s3_log_bucket,
                                 Key=s3_log_location, ACL='bucket-owner-full-control',
                                 Tagging='Source=GluePartitionManager-' + write_source)
        except Exception:
            var = traceback.format_exc()
            logger.error(f"Error {var} processing __write_object_to_s3")
            raise

    def __check_partition_keys_in_cache(self, table_name, partitions_to_create):
        """
        Helper function to check if the partition_key exists in cache
        """
        partition_key_exists_in_cache = True
        # for the provided partition_key, check if there exists an entry in the cache storage in s3
        partition_cache_key = self.glue_table_partition_cache_key + '/' + table_name + '/' + \
            '_'.join(partitions_to_create)

        s3_client = boto3.client('s3', region_name=self.deployment_region)
        try:
            s3_client.head_object(
                Bucket=self.s3_glue_log_bucket, Key=partition_cache_key)
        except ClientError as e:
            partition_key_exists_in_cache = False
            if e.response['Error']['Code'] == "404":
                # The object does not exist.
                logger.info(
                    f"Object doesn't exist in GlueCache Bucket {self.s3_glue_log_bucket} at {partition_cache_key}")
            elif e.response['Error']['Code'] == "403":
                # Forbidden Error
                logger.info(
                    f"AccessDeniedException. Check permissions for the bucket : {self.s3_glue_log_bucket}")
            else:
                raise
        return partition_key_exists_in_cache

    def __get_partition_input_from_table_name(self, table_name, table_location, partitions_to_create):
        """
        Helper function to create the partition_input for table name (table_name)
        using cache contents
        """
        logger.info(
            f'__get_partition_input_from_table_name, partitions_to_create : {partitions_to_create}')
        table_details = self.__get_table_details_from_cache(table_name)
        logger.info(f'table_details : {table_details}')
        storage_descriptor = table_details.get('StorageDescriptor')
        storage_location_postfix = '/'.join(partitions_to_create) + '/'
        table_location = table_location + storage_location_postfix
        logger.info(f'Setting partition location as : {table_location}')
        partition_input = {
            "Values": partitions_to_create,
            "StorageDescriptor": {
                'Location': f's3://{self.s3_glue_log_bucket}/{table_location}',
                "InputFormat": storage_descriptor['InputFormat'],
                "OutputFormat": storage_descriptor['OutputFormat'],
                "SerdeInfo": storage_descriptor['SerdeInfo']
            }
        }
        return partition_input

    def get_table_details_from_key(self, s3_key):
        """
        Helper function to get table name from an S3 key
        s3_key example aws-backup-logs/backup_job/2021-07-29/A1144295-8F39-82C1-8BE0-668B41170A6A
        s3_location example s3://us-east-1-venkitas/aws-backup-logs/backup_job/
        """
        table_details_from_key = {}
        if not self.s3_locations_list:
            self.__get_s3_locations_list()

        for table_details in self.s3_locations_list:
            for table_name in table_details:
                if table_details[table_name] in s3_key:
                    table_details_from_key = {'Name': table_name,
                                              'Location': table_details[table_name]}
        return table_details_from_key

    def delete_glue_cache(self, s3_folder_prefix):
        """
        Helper function to clear GlueCache when Stack is deleted
        """
        partition_keys_list = []

        s3_client = boto3.client('s3', region_name=self.deployment_region)
        try:
            # Get the list of existing partition keys from the cache
            response = s3_client.list_objects_v2(Bucket=self.s3_glue_log_bucket,
                                                 Delimiter='/',
                                                 Prefix=s3_folder_prefix)

            if 'Contents' in response:
                for key_info in response['Contents']:
                    s3_key = key_info['Key']
                    partition_keys_list.append({'Key': s3_key})
            elif 'CommonPrefixes' in response and len(response['CommonPrefixes']) > 0:
                for commonPrefix in response['CommonPrefixes']:
                    self.delete_glue_cache(commonPrefix['Prefix'])
            else:
                logger.info(
                    f'NO Cache file exists in the location : {s3_folder_prefix} on {self.s3_glue_log_bucket}')

        except Exception as e:  # pylint: disable = W0703
            logger.error(f"Error : {e} processing list_objects_v2")

        try:
            if partition_keys_list:
                # Delete them in a single request
                s3_client.delete_objects(Bucket=self.s3_glue_log_bucket,
                                         Delete={
                                             'Objects': partition_keys_list,
                                             'Quiet': True
                                         })
        except Exception as e:  # pylint: disable = W0703
            logger.error(f"Error : {e} processing delete_objects")

        logger.info("Finished delete_glue_cache")

    def update_glue_partition_for_s3_key(self, s3_key):
        """
        This method is responsible for adding new partitions to the job logs Glue
        table, which is then used by Athena queries for easy analysis.
        """
        try:
            logger.info(f'update_glue_partition_for_s3_key : {s3_key}')
            s3_key = s3_key.lstrip('/')
            logger.info(f"s3_key : {s3_key}")
            table_details = self.get_table_details_from_key(s3_key)
            if not table_details:
                logger.error(
                    f"Unknown prefix in S3 Key. No Table mapping found under glue_table_name_list : {self.glue_table_name_list}. Skipping processing")
                return

            partitions_to_create = self.__get_partition_names_in_key(
                s3_key, table_details)
            if(partitions_to_create and len(partitions_to_create) > 0):
                self.__update_glue_table_partitions(
                    table_details['Name'], table_details['Location'], partitions_to_create)

        except (ClientError, Exception):
            var = traceback.format_exc()
            logger.error(f"Error {var} n update_glue_partition_for_s3_key")

    def __get_partition_names_in_key(self, s3_key, table_details):
        """
        Helper function to get partition names in the defined key
        """
        # for the provided s3 path get the list of partitions
        s3_key = s3_key.replace(table_details['Location'], '')
        slash_len = s3_key.count('/')
        keys_in_location = s3_key.rsplit('/', maxsplit=slash_len)
        partitions_in_key = keys_in_location[:slash_len]
        partitions_in_key = list(filter(None, partitions_in_key))
        if self.glue_s3_path_exclusions:
            for exclusion in self.glue_s3_path_exclusions.split(','):
                exclusion = exclusion.strip()
                if exclusion in partitions_in_key:
                    partitions_in_key.remove(exclusion)

        return partitions_in_key

    def __update_glue_table_partitions(self, table_name, table_location, partitions_to_create):
        """
        This method is responsible for adding new partitions to the Glue tables,
        which is then used by Athena queries for easy analysis.
        """
        glue_client = boto3.client('glue', region_name=self.deployment_region)
        logger.info(
            f"Update partitions for : {table_name}, Location : {table_location} with : {partitions_to_create}")
        try:
            if not self.__check_partition_keys_in_cache(table_name, partitions_to_create):
                logger.info(f"Creating Partitions : {partitions_to_create} " +
                            f" in Glue DB: {self.glue_database_name}, Glue Table: {table_name}")
                partition_input = self.__get_partition_input_from_table_name(
                    table_name, table_location, partitions_to_create)
                glue_client.create_partition(
                    DatabaseName=self.glue_database_name,
                    TableName=table_name,
                    PartitionInput=partition_input)
                # Successful Creation. Save the key to s3 cache
                self.__write_partition_keys_to_cache(
                    table_name, partitions_to_create)
            else:
                logger.info(
                    f'Partitions : {partitions_to_create} already exist for : {table_name}')
        except ClientError as e:
            logger.error(e)
            if e.response['Error']['Code'] == 'AlreadyExistsException':
                # Double confirm the cache existence
                self.__write_partition_keys_to_cache(
                    table_name, partitions_to_create)
