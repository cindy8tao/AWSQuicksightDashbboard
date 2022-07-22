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
import time
import urllib3
import boto3
from botocore.exceptions import ClientError
logger = logging.getLogger()
logger.setLevel(logging.INFO)


######################################################################
#                        CLASS DEFINITION                            #
######################################################################


class CustomResourceManager:
    """
    CustomResourceManager Controller class. Handles all logic related to Customer CFN Resources.
    """

    # INIT
    def __init__(self, event, context):
        self.session_id = boto3.session.Session().client('sts').get_caller_identity()
        self.account_id = boto3.client('sts').get_caller_identity()['Account']
        self.deployment_region = boto3.session.Session().region_name
        self.function_arn = context.invoked_function_arn

        self.success = 'SUCCESS'
        self.failed = 'FAILED'
        self.physical_resource_id = 'AWSBackupObserver'

    def handle_custom_resource_create_request(self, event, context):
        """
        CustomResourceManager handler for create request
        """
        response_data = {}
        try:
            supported_job_types = ['backup_job', 'restore_job', 'copy_job']
            overwrite_backup_job_logs = event['ResourceProperties'].get(
                'OverwriteJobLogs')
            backup_manager_arn = event['ResourceProperties'].get(
                'BackupManagerArn')
            # Add S3 Notifications as required
            if 'S3Bucket' in event['ResourceProperties']:
                s3_bucket = event['ResourceProperties']['S3Bucket']
                s3_event_handler_lambda_arn = event['ResourceProperties'][
                    'S3EventHandlerLambdaArn']
                s3_prefix_list = event['ResourceProperties']['S3PrefixList'].split(
                    ',')
                logger.info(
                    f"s3Bucket : {s3_bucket}, lambdaARN : {s3_event_handler_lambda_arn}, " +
                    f"s3PrefixList : {s3_prefix_list}")
                self.setup_s3_event_notifications(
                    s3_event_handler_lambda_arn, s3_prefix_list, s3_bucket)
                logger.info("setupS3EventNotifications completed")

            if 'ReportRecipient' in event['ResourceProperties']:
                # Validate the Email Recepient
                report_recipient = event['ResourceProperties'].get(
                    'ReportRecipient')
                if report_recipient:
                    input_params = {
                        "ReportRecipient": report_recipient
                    }
                    boto3.client('lambda').invoke(
                        FunctionName=s3_event_handler_lambda_arn,
                        InvocationType='Event',
                        Payload=json.dumps(input_params)
                    )

            if 'RefreshGluePartitions' in event['ResourceProperties']:
                # Initialize the PartitionLoader Function with initial partition details
                input_params = {
                    "RefreshGluePartitions": "true"
                }
                boto3.client('lambda').invoke(
                    FunctionName=s3_event_handler_lambda_arn,
                    InvocationType='Event',
                    Payload=json.dumps(input_params)
                )

            if 'RefreshJobLogs' in event['ResourceProperties']:
                refresh_jobs = event['ResourceProperties']['RefreshJobLogs']
                backup_manager_arn = event['ResourceProperties']['BackupManagerArn']
                logger.info(f"BackupManagerArn : {backup_manager_arn} , " +
                            f"OverwriteJobLogs : {overwrite_backup_job_logs}, " +
                            f"RefreshJobLogs : {refresh_jobs}")

                if refresh_jobs == 'true':
                    if 'ProcessDelay' in event['ResourceProperties']:
                        process_delay = event['ResourceProperties']['ProcessDelay']
                        logger.info(
                            f"ProcessDelay for :{process_delay} requested")
                        time.sleep(int(process_delay))

                    input_params = {
                        "RefreshJobLogs": "true",
                        "OverWriteFilesInS3": "true",
                        "State": "REFRESH",
                        "EventType": "JOB_TYPE"
                    }

                    for supportedJobType in supported_job_types:
                        input_params['EventType'] = supportedJobType
                        input_params['OverWriteFilesInS3'] = overwrite_backup_job_logs
                        logger.info(
                            f"Processing supportedJobType : {supportedJobType} with inputParams {input_params}")
                        try:
                            boto3.client('lambda').invoke(
                                FunctionName=backup_manager_arn,
                                InvocationType='Event',
                                Payload=json.dumps(input_params)
                            )

                        except (ClientError, Exception):  # pylint: disable = W0703
                            var = traceback.format_exc()
                            logger.error(f"Error {var} processing invoke")

            if 'RefreshBackupAuditManagerReports' in event['ResourceProperties']:
                try:
                    input_params = {
                        "RefreshBackupAuditManagerReports": "true"
                    }

                    boto3.client('lambda').invoke(
                        FunctionName=backup_manager_arn,
                        InvocationType='Event',
                        Payload=json.dumps(input_params)
                    )

                except (ClientError, Exception):  # pylint: disable = W0703
                    var = traceback.format_exc()
                    logger.error(f"Error {var} processing invoke")
            # Check if config refresh is enabled
            if 'RefreshConfigItems' in event['ResourceProperties']:
                try:
                    input_params = {
                        "RefreshConfigItems": "true"
                    }

                    boto3.client('lambda').invoke(
                        FunctionName=backup_manager_arn,
                        InvocationType='Event',
                        Payload=json.dumps(input_params)
                    )

                except (ClientError, Exception):  # pylint: disable = W0703
                    var = traceback.format_exc()
                    logger.error(f"Error {var} processing invoke")

            response_data = {
                'ResourceProperties': event['ResourceProperties']
            }

            send(event, context, self.success,
                 response_data, self.physical_resource_id)

        except (ClientError, Exception):  # pylint: disable = W0703
            send(event, context, self.failed,
                 response_data, self.physical_resource_id)
            var = traceback.format_exc()
            logger.error(f"Error {var} processing Create")

    def handle_custom_resource_update_request(self, event, context):
        """
        CustomResourceManager handler for update request
        """
        logger.info(
            f'request received of type {event["RequestType"]}, There are NO custom resources to update')
        response_data = {
            'Status': 'There are NO custom resources to update'
        }

        send(event, context, self.success,
             response_data, self.physical_resource_id)

    def handle_custom_resource_delete_request(self, event, context):
        """
        CustomResourceManager handler for delete request
        """
        response_data = {}
        try:
            if 'S3Bucket' in event['ResourceProperties']:
                s3_bucket = event['ResourceProperties']['S3Bucket']
                s3_event_handler_lambda_arn = event['ResourceProperties'][
                    'S3EventHandlerLambdaArn']
                s3_prefix_list = event['ResourceProperties']['S3PrefixList'].split(
                    ',')
                try:
                    self.delete_bucket_notifications(s3_prefix_list, s3_bucket)
                except (ClientError, Exception):  # pylint: disable = W0703
                    var = traceback.format_exc()
                    logger.error(f"Error {var} processing invoke")

            if 'CleanupGluePartitions' in event['ResourceProperties']:
                try:
                    # Cleanup The GluePartitionAutoLoader
                    input_params = {
                        "CleanupGluePartitions": "true"
                    }
                    boto3.client('lambda').invoke(
                        FunctionName=s3_event_handler_lambda_arn,
                        InvocationType='Event',
                        Payload=json.dumps(input_params)
                    )

                except (ClientError, Exception):  # pylint: disable = W0703
                    var = traceback.format_exc()
                    logger.error(f"Error {var} processing invoke")

            if event.get('ResourceProperties') and 'S3BucketToCleanup' in event[
                    'ResourceProperties']:
                bucket_name = event['ResourceProperties']['S3BucketToCleanup']
                self.process_bucket_cleanup_request(bucket_name)

            send(event, context, self.success,
                 response_data, self.physical_resource_id)
        except (ClientError, Exception):  # pylint: disable = W0703
            send(event, context, self.failed,
                 response_data, self.physical_resource_id)
            var = traceback.format_exc()
            logger.error(f"Error {var} processing Delete")

    def process_bucket_cleanup_request(self, bucket_name):
        logger.info(
            f"process_bucket_cleanup_request starting for bucket_name : {bucket_name}")
        s3 = boto3.resource('s3')
        bucket_to_delete = s3.Bucket(bucket_name)
        response = bucket_to_delete.objects.all().delete()
        logger.info(
            f"process_bucket_cleanup_request all object delete done. Response : {response}")

    def delete_bucket_notifications(self, s3_prefix_list, bucket):
        """
        Helper function to delete notifications from the S3 bucket with the
        matching the configuration details provided.
        """
        bucket_notify_config = {'LambdaFunctionConfigurations': []}
        existing_config = self.get_bucket_notification_config(bucket)
        if 'LambdaFunctionConfigurations' in existing_config:
            bucket_notify_config['LambdaFunctionConfigurations'] = existing_config[
                'LambdaFunctionConfigurations']
        pop_list = []
        for lambda_config in bucket_notify_config['LambdaFunctionConfigurations']:
            for s3_prefix in s3_prefix_list:
                if lambda_config['Id'] == s3_prefix:
                    pop_list.append(lambda_config)
                    break
        for pop_item in pop_list:
            bucket_notify_config['LambdaFunctionConfigurations'].remove(
                pop_item)

        s3_client = boto3.client('s3')
        s3_client.put_bucket_notification_configuration(Bucket=bucket,
                                                        NotificationConfiguration=bucket_notify_config)

    def get_bucket_notification_config(self, bucket):
        """
        Helper function to extract notification configuration in the S3 bucket with
        the matching the configuration details provided.
        """
        s3_client = boto3.client('s3')
        bucket_notification = s3_client.get_bucket_notification_configuration(
            Bucket=bucket)
        logger.info(f"lambda_function_configurations : {bucket_notification}")
        return bucket_notification

    def setup_s3_event_notifications(self, lambda_arn, s3_prefix_list, bucket):
        """
        Helper function to setup notifications in the S3 bucket with the
        matching the configuration details provided.
        """
        bucket_notify_config = {'LambdaFunctionConfigurations': []}
        existing_config = self.get_bucket_notification_config(bucket)
        if 'LambdaFunctionConfigurations' in existing_config:
            bucket_notify_config['LambdaFunctionConfigurations'] = existing_config[
                'LambdaFunctionConfigurations']
        for s3_prefix in s3_prefix_list:
            bucket_notify_config['LambdaFunctionConfigurations'].append({
                "Id": s3_prefix,
                "LambdaFunctionArn": lambda_arn,
                "Events": [
                    "s3:ObjectCreated:Put"
                ],
                "Filter": {
                    "Key": {
                        "FilterRules": [
                            {
                                "Name": "Prefix",
                                "Value": s3_prefix
                            }
                        ]
                    }
                }
            })
        s3_client = boto3.client('s3')
        try:
            s3_client.put_bucket_notification_configuration(Bucket=bucket,
                                                            NotificationConfiguration=bucket_notify_config)
        except ClientError as e:
            logger.error(
                f'bucket_notify_config : {bucket_notify_config} failed to set. Error: {e}')
            raise


def send(event, context, response_status, response_data, physical_resource_id,
         no_echo=False):  # pylint: disable = R0913
    """
    Helper function for sending updates on the custom resource to CloudFormation during a
    'Create', 'Update', or 'Delete' event.
    """
    logger.info(f"Send started with response_data:{response_data}")
    http = urllib3.PoolManager()
    response_url = event['ResponseURL']

    json_response_body = json.dumps({
        'Status': response_status,
        'Reason': f'See the details in CloudWatch Log Stream: {context.log_stream_name}',
        'PhysicalResourceId': physical_resource_id,
        'StackId': event['StackId'],
        'RequestId': event['RequestId'],
        'LogicalResourceId': event['LogicalResourceId'],
        'NoEcho': no_echo,
        'Data': response_data
    }).encode('utf-8')

    headers = {
        'content-type': '',
        'content-length': str(len(json_response_body))
    }

    try:
        http.request('PUT', response_url,
                     body=json_response_body, headers=headers)
    except Exception as e:  # pylint: disable = W0703
        logger.error(e)
