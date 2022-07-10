import boto3
import backup
import s3
import jsonfile
import quicksight
from datetime import datetime
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
quicksight_client = boto3.client('quicksight')

account_id = '774446988871'


def create_backup_plan():

    backup_plan_name = '12hrs'
    rule_name = 'RunEvery12Hours'
    start_window_minutes = 60
    completion_window_minutes = 120
    schedule_expression = 'cron(0 12 * * ? *)'
    target_backup_vault_name = 'Default'

    backupClass = backup.Backup(backup_client)
    backupClass.create_backup_plan(backup_plan_name, rule_name, start_window_minutes,
                                   completion_window_minutes, schedule_expression, target_backup_vault_name)


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


def create_datasource():
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.create_datasource()


def update_datasource():
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.update_datasource()


def create_dataset():
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.create_dataset()


def create_template():
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.create_template()


def create_analysis():
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.create_analysis()


def create_dashboard():
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.create_dashboard()


def delete_datasource(datasource):
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.delete_datasource(datasource)


def delete_dataset(dataset):
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.delete_dataset(dataset)


def delete_template(template):
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.delete_template(template)


def delete_analysis(analysis):
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.delete_analysis(analysis)


def delete_dashboard(dashboard):
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.delete_dashboard(dashboard)


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

    s3_resource.Bucket(bucket_name)

    try:
        create_s3_bucket(bucket_name)
        print("Created bucket")
    except:
        print("Bucket name already exist")
        pass

    list_all_tags()

    path = "/tmp/csv_file.csv"
    upload_to_S3(path, bucket_name, csv_file_name, csv_content_type)

    path = "/tmp/file.json"
    upload_to_S3(path, bucket_name, json_file_name, json_content_type)

    now = datetime.now()
    folder_name = now.strftime("%m/%d/%Y")

    uri = "s3://" + bucket_name + "/" + folder_name + "/" + csv_file_name
    uri_prefixes = "s3://" + bucket_name + "/" + folder_name + "/"

    create_json_manifest_file(uri, uri_prefixes, "CSV")
    path = "/tmp/manifest.json"
    upload_to_S3(path, bucket_name, "manifest.json", json_content_type)

    create_datasource()
    create_dataset()


if __name__ == "__main__":
    main()
