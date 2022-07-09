import boto3
import backup
import s3
import jsonfile
import ec2
import rds
import glue
import pprint
import os

#####################################################
# Create the required clients and resources         #
#####################################################
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
backup_client = boto3.client('backup')
ec2_resource = boto3.resource('ec2')
rds_client = boto3.client('rds')
glue_client = boto3.client('glue')

# account_id = input("Please enter your AWS account_id: ")
account_id = '744878436330'


def list_all_tags():

    backupClass = backup.Backup(backup_client)
    backupClass.list_recovery_points_with_tags()


def s3_object(bucket_name, json_file, key):
    s3Class = s3.S3(account_id, s3_client, s3_resource)
    s3Class.s3_object(bucket_name, json_file, key)


def upload_to_S3(path, bucket_name, key, content_type):
    s3Class = s3.S3(account_id, s3_client, s3_resource)
    s3Class.upload_to_S3(path, bucket_name, key, content_type)


def create_s3_bucket(bucket_name):
    s3Class = s3.S3(account_id, s3_client, s3_resource)
    s3Class.create_bucket(bucket_name)
    s3Class.bucket_version(bucket_name)


def create_json_manifest_file(uri, uri_prefixes, format):
    jsonClass = jsonfile.JsonFile()
    jsonClass.create_json_manifest_file(uri, uri_prefixes, format)


def main():

    #####################################################
    # Ask user for inputs                               #
    #####################################################

    print("Welcome to create your Quicksight Backup Dashboard ")

    bucket_name = "new-backup-report-based-arn-tags"
    json_file_name = "json_file_from_path.json"
    json_content_type = "application/json"
    csv_file_name = "csv_file_from_path.csv"
    csv_content_type = "text/csv"

    bucket = s3_resource.Bucket(bucket_name)

    try:
        create_s3_bucket(bucket_name)
        print("Created bucket")
    except NameError:
        print("Bucket name already exist")
        pass

    list_all_tags()
    # s3_object("backupreportwithtags", csv_file, "tagcsvfile")
    path = "/Users/cindytao/Document/GitHub/AWSQuicksightDashbboard/Backup/src/AWSProject/csv_file.csv"
    upload_to_S3(path, bucket_name, csv_file_name, csv_content_type)

    path = "/Users/cindytao/Document/GitHub/AWSQuicksightDashbboard/Backup/src/AWSProject/file.json"
    upload_to_S3(path, bucket_name, json_file_name, json_content_type)

    uri = "s3://" + bucket_name + "/" + csv_file_name
    uri_prefixes = "s3://" + bucket_name + "/"

    manifest = create_json_manifest_file(uri, uri_prefixes, "CSV")
    # s3_object(bucket_name, manifest, "manifest_file")
    path = "/Users/cindytao/Document/GitHub/AWSQuicksightDashbboard/Backup/src/AWSProject/manifest.json"
    upload_to_S3(path, bucket_name, "manifest.json", json_content_type)

    # manifest = create_json_manifest_file(uri, uri_prefixes, "JSON")
    # # s3_object(bucket_name, manifest, "manifest_file")
    # path = "/Users/cindytao/Document/GitHub/AWSQuicksightDashbboard/Backup/src/AWSProject/manifest.json"
    # upload_to_S3(path, bucket_name, "manifest.json", json_content_type)


if __name__ == "__main__":
    main()
