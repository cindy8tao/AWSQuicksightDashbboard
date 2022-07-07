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
account_id = '774446988871'


def list_all_tags():

    backupClass = backup.Backup(backup_client)
    backupClass.list_recovery_points_with_tags()


def s3_object(bucket_name, json_file, key):
    s3Class = s3.S3(account_id, s3_client, s3_resource)
    s3Class.s3_object(bucket_name, json_file, key)


def upload_to_S3(path, bucket_name, key):
    s3Class = s3.S3(account_id, s3_client, s3_resource)
    s3Class.upload_to_S3(path, bucket_name, key)


def create_s3_bucket(bucket_name):
    s3Class = s3.S3(account_id, s3_client, s3_resource)
    s3Class.create_bucket(bucket_name)


def create_json_manifest_file(uri, uri_prefixes):
    jsonClass = jsonfile.JsonFile()
    jsonClass.create_json_manifest_file(uri, uri_prefixes)


def main():

    #####################################################
    # Ask user for inputs                               #
    #####################################################

    print("Welcome to create your Quicksight Backup Dashboard ")

    bucket_name = "backupreportwithtags"
    json_file_name = "json_file_from_path"

    bucket = s3_resource.Bucket(bucket_name)
    if bucket.creation_date:
        print("Bucket already exist")
    else:
        create_s3_bucket(bucket_name)
        print("Created bucket")

    json_file = list_all_tags()
    # s3_object("backupreportwithtags", json_file, "tagjsonfile")
    path = "/Users/cindytao/Document/GitHub/AWSQuicksightDashbboard/Backup/src/AWSProject/file.json"
    upload_to_S3(path, bucket_name, json_file_name)

    uri = "s3://" + bucket_name + "/" + json_file_name
    uri_prefixes = "s3://" + bucket_name + "/"

    create_json_manifest_file(uri, uri_prefixes)
    # s3_object(bucket_name, manifest, "manifest_file")
    path = "/Users/cindytao/Document/GitHub/AWSQuicksightDashbboard/Backup/src/AWSProject/manifest.json"
    upload_to_S3(path, bucket_name, "manifest")


if __name__ == "__main__":
    main()
