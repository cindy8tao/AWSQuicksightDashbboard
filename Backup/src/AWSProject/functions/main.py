import boto3
import backup
import s3
import jsonfile
import quicksight
import cost
from datetime import datetime
import costreport
from datetime import datetime
from dateutil.relativedelta import relativedelta

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
costreport_client = boto3.client('cur')
cost_client = boto3.client('ce')


def create_backup_plan(account_id, start_window_minutes, completion_window_minutes, target_backup_vault_name, hrs, environment, department):
    backupClass = backup.Backup(account_id, backup_client)
    backupClass.create_backup_plan(start_window_minutes, completion_window_minutes,
                                   target_backup_vault_name, hrs, environment, department)


def list_all_tags(account_id):
    backupClass = backup.Backup(account_id, backup_client)
    backupClass.list_recovery_points_with_tags()


def list_all_buckets(account_id):
    s3Class = s3.S3(account_id, s3_client, s3_resource)
    s3Class.list_all_bucket()


def s3_object(account_id, bucket_name, json_file, key):
    s3Class = s3.S3(account_id, s3_client, s3_resource)
    s3Class.s3_object(bucket_name, json_file, key)


def upload_to_S3(account_id, path, bucket_name, key, content_type):
    s3Class = s3.S3(account_id, s3_client, s3_resource)
    s3Class.upload_to_S3(path, bucket_name, key, content_type)


def create_s3_bucket(account_id, bucket_name):
    s3Class = s3.S3(account_id, s3_client, s3_resource)
    s3Class.create_bucket(bucket_name)
    s3Class.bucket_version(bucket_name)


def put_bucket_policy(account_id, bucket_name):
    s3Class = s3.S3(account_id, s3_client, s3_resource)
    s3Class.put_bucket_policy(bucket_name)


def create_json_manifest_file(uri, uri_prefixes, format):
    jsonClass = jsonfile.JsonFile()
    jsonClass.create_json_manifest_file(uri, uri_prefixes, format)


def create_datasource(account_id, data_source_id, name, bucket, key):
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.create_datasource(data_source_id, name, bucket, key)


def update_datasource(account_id, data_source_id, name, bucket, key):
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.update_datasource(data_source_id, name, bucket, key)


def create_dataset(account_id, tags):
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.create_dataset(tags)


def create_cost_dataset(account_id):
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.create_cost_dataset()


def create_template(account_id):
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.create_template()


def create_analysis(account_id):
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.create_analysis()


def create_dashboard(account_id):
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.create_dashboard()


def delete_datasource(account_id, datasource):
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.delete_datasource(datasource)


def delete_dataset(account_id, dataset):
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.delete_dataset(dataset)


def delete_template(account_id, template):
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.delete_template(template)


def delete_analysis(account_id, analysis):
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.delete_analysis(analysis)


def delete_dashboard(account_id, dashboard):
    quicksightClass = quicksight.Quicksight(
        account_id, quicksight_client, account_id)
    quicksightClass.delete_dashboard(dashboard)


def create_cost_report(bucket_name):
    costreportClass = costreport.CostReport(costreport_client)
    costreportClass.create_cost_report(bucket_name)


def get_tags(account_id):
    backupClass = backup.Backup(account_id, backup_client)
    return backupClass.get_tags()


def get_cost_by_tags(account_id, tags):
    costClass = cost.Cost(account_id, cost_client)
    costClass.get_cost_by_tags(tags)

# def lambda_handler(event, context):


def main():

    print("Welcome to create your Quicksight Backup Dashboard ")
    # account_id = context.invoked_function_arn.split(":")[4]
    account_id = '774446988871'

    bucket_name = "new-backup-report-based-arn-tags-"+account_id
    cost_bucket_name = "cost-report-for-quicksight-"+account_id
    json_file_name = "json_file_from_path.json"
    json_content_type = "application/json"
    csv_file_name = "csv_file_from_path.csv"
    cost_csv_file_name = "cost_csv_file_from_path.csv"
    csv_content_type = "text/csv"

    #####################################################
    # Create the backup/cost report                     #
    #####################################################

    list_all_tags(account_id)

    tags = get_tags(account_id)
    get_cost_by_tags(account_id, tags)

    path = "/tmp/csv_file.csv"
    upload_to_S3(account_id, path, bucket_name,
                 csv_file_name, csv_content_type)

    path = "/tmp/cost.csv"
    upload_to_S3(account_id, path, cost_bucket_name,
                 cost_csv_file_name, csv_content_type)

    ####################################################
    # Quicksight                                       #
    ####################################################

    # now = datetime.now()
    # folder_name = now.strftime("%m/%d/%Y")
    # data_source_id = 'unique-data-source-id-' + account_id
    # name = 'datasource' + account_id
    # bucket = 'new-backup-report-based-arn-tags-' + account_id
    # key = folder_name + '/manifest.json'

    # create_datasource(account_id, data_source_id, name, bucket, key)
    # create_dataset(account_id, tags)
    # create_template(account_id)
    # create_analysis(account_id)
    # create_dashboard(account_id)


if __name__ == "__main__":
    main()