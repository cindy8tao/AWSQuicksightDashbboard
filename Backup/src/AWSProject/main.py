import boto3
# import quicksight
# import cfnresponse
import cost
import backup
from datetime import datetime

#####################################################
# Create the required clients and resources         #
#####################################################
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
backup_client = boto3.client('backup')
cost_client = boto3.client('ce')
glue_client = boto3.client('glue')
quicksight_client = boto3.client('quicksight')


def list_all_tags(account_id):
    backupClass = backup.Backup(account_id, backup_client)
    backupClass.list_recovery_points_with_tags()


# def upload_to_S3(account_id, path, bucket_name, key, content_type):
#     s3Class = s3.S3(account_id, s3_client, s3_resource)
#     s3Class.upload_to_S3(path, bucket_name, key, content_type)


def get_tags(account_id):
    backupClass = backup.Backup(account_id, backup_client)
    return backupClass.get_tags()


def get_cost_by_tags(account_id, tags):
    costClass = cost.Cost(account_id, cost_client)
    costClass.get_cost_by_tags(tags)


# def create_table(account_id, table_name, database_name, column, location):
#     glueClass = glue.Glue(account_id, glue_client)
#     glueClass.create_table(table_name, database_name, column, location)


# def lambda_handler(event, context):
# def refresh_spice_data(account_id):
#     quicksightClass = quicksight.Quicksight(account_id, quicksight_client)
#     quicksightClass.refresh_spice_data()


# def refresh_cost_spice_data(account_id):
#     quicksightClass = quicksight.Quicksight(account_id, quicksight_client)
#     quicksightClass.refresh_cost_spice_data()


# def update_data_set(account_id):
#     quicksightClass = quicksight.Quicksight(account_id, quicksight_client)
#     quicksightClass.update_data_set()


# def cost_update_data_set(account_id):
#     quicksightClass = quicksight.Quicksight(account_id, quicksight_client)
#     quicksightClass.cost_update_data_set()


# def update_analysis(account_id):
#     quicksightClass = quicksight.Quicksight(account_id, quicksight_client)
#     quicksightClass.update_analysis()


# def update_dashboard(account_id):
#     quicksightClass = quicksight.Quicksight(account_id, quicksight_client)
#     quicksightClass.update_dashboard()


def main():

    print("Welcome to create your Quicksight Backup Dashboard ")
    # account_id = context.invoked_function_arn.split(":")[4]
    account_id = '263675971756'

    # refresh_spice_data(account_id)
    # refresh_cost_spice_data(account_id)
    # update_data_set(account_id)
    # cost_update_data_set(account_id)
    # update_analysis(account_id)
    # update_dashboard(account_id)
    # tags = get_tags(account_id)
    # get_cost_by_tags(account_id, tags)

    # bucket_name = "new-backup-report-based-arn-tags-"+account_id
    # cost_bucket_name = "cost-report-for-quicksight-"+account_id
    # csv_file_name = "csv_file_from_path.csv"
    # cost_csv_file_name = "cost_csv_file_from_path.csv"
    # csv_content_type = "text/csv"

    # #####################################################
    # # Create the backup/cost report                     #
    # #####################################################

    list_all_tags(account_id)

    # tags = get_tags(account_id)
    # get_cost_by_tags(account_id, tags)

    # path = "/tmp/csv_file.csv"
    # upload_to_S3(account_id, path, bucket_name,
    #              csv_file_name, csv_content_type)

    # path = "/tmp/cost.csv"
    # upload_to_S3(account_id, path, cost_bucket_name,
    #              cost_csv_file_name, csv_content_type)

    # #####################################################
    # # Glue                                              #
    # #####################################################

    # now = datetime.now()
    # date = now.strftime("/%m/%d/")

    # database_name = 'database_'
    # table_name = 'backup_report'
    # column = [
    #     {
    #         'Name': 'creationdate',
    #         'Type': 'date',
    #     },
    #     {
    #         'Name': 'completiondate',
    #         'Type': 'date',
    #     },
    #     {
    #         'Name': 'resourcearn',
    #         'Type': 'string',
    #     },
    #     {
    #         'Name': 'resourcetype',
    #         'Type': 'string',
    #     },
    #     {
    #         'Name': 'backupsize',
    #         'Type': 'decimal',
    #     },
    #     {
    #         'Name': 'tagkey',
    #         'Type': 'string',
    #     },
    #     {
    #         'Name': 'tagvalue',
    #         'Type': 'string',
    #     },
    # ]

    # location = 's3://new-backup-report-based-arn-tags-' + account_id + date

    # create_table(account_id, table_name, database_name, column, location)

    # database_name = 'cost_database_'
    # table_name = 'cost_report'
    # column = [
    #     {
    #         'Name': 'start',
    #         'Type': 'date',
    #     },
    #     {
    #         'Name': 'end',
    #         'Type': 'date',
    #     },
    #     {
    #         'Name': 'tags',
    #         'Type': 'string',
    #     },
    #     {
    #         'Name': 'unblendedcost',
    #         'Type': 'float',
    #     },
    # ]

    # location = 's3://cost-report-for-quicksight-' + account_id + date

    # create_table(account_id, table_name, database_name, column, location)

    # #####################################################
    # # Set Quicksight Template Permission                #
    # #####################################################

    # # set_template_permissions(account_id)


if __name__ == "__main__":
    main()
