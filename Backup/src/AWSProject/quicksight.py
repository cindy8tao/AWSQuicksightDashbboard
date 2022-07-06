import datetime
from urllib.request import Request
import boto3
import json
import pprint


# class Quicksight:

#     def __init__(self):
#         pass

#     def create_dataset(self):


client = boto3.client('quicksight')

response = client.create_data_source(
    AwsAccountId='744878436330',
    DataSourceId='unique-data-source-id-123',
    Name='s3datasource',
    Type='S3',
    DataSourceParameters={
        'S3Parameters': {
            'ManifestFileLocation': {
                'Bucket': 's3://sparcuser-backupreport/aws-backup-logs/backup_job_report/json/744878436330/us-east-1/2022/07/06/bos_backupjobreport_e0875b80/',
                'Key': 'aws-backup-logs/backup_job_report/json/744878436330/us-east-1/2022/07/06/bos_backupjobreport_e0875b80/backup_job_report_bos_backupjobreport_e0875b80_2022-07-05t00:00:00z_2022-07-06t00:00:00z_1.json'
            }
        }
    },
    # Credentials={
    #     'CredentialPair': {
    #         'Username': 'sparcuser1',
    #         'Password': 'sparcuser1!',
    #         'AlternateDataSourceParameters': [
    #             {
    #                 'AmazonElasticsearchParameters': {
    #                     'Domain': 'string'
    #                 },
    #                 'AthenaParameters': {
    #                     'WorkGroup': 'string'
    #                 },
    #                 'AuroraParameters': {
    #                     'Host': 'string',
    #                     'Port': 123,
    #                     'Database': 'string'
    #                 },
    #                 'AuroraPostgreSqlParameters': {
    #                     'Host': 'string',
    #                     'Port': 123,
    #                     'Database': 'string'
    #                 },
    #                 'AwsIotAnalyticsParameters': {
    #                     'DataSetName': 'string'
    #                 },
    #                 'JiraParameters': {
    #                     'SiteBaseUrl': 'string'
    #                 },
    #                 'MariaDbParameters': {
    #                     'Host': 'string',
    #                     'Port': 123,
    #                     'Database': 'string'
    #                 },
    #                 'MySqlParameters': {
    #                     'Host': 'string',
    #                     'Port': 123,
    #                     'Database': 'string'
    #                 },
    #                 'OracleParameters': {
    #                     'Host': 'string',
    #                     'Port': 123,
    #                     'Database': 'string'
    #                 },
    #                 'PostgreSqlParameters': {
    #                     'Host': 'string',
    #                     'Port': 123,
    #                     'Database': 'string'
    #                 },
    #                 'PrestoParameters': {
    #                     'Host': 'string',
    #                     'Port': 123,
    #                     'Catalog': 'string'
    #                 },
    #                 'RdsParameters': {
    #                     'InstanceId': 'string',
    #                     'Database': 'string'
    #                 },
    #                 'RedshiftParameters': {
    #                     'Host': 'string',
    #                     'Port': 123,
    #                     'Database': 'string',
    #                     'ClusterId': 'string'
    #                 },
    #                 'S3Parameters': {
    #                     'ManifestFileLocation': {
    #                         'Bucket': 'string',
    #                         'Key': 'string'
    #                     }
    #                 },
    #                 'ServiceNowParameters': {
    #                     'SiteBaseUrl': 'string'
    #                 },
    #                 'SnowflakeParameters': {
    #                     'Host': 'string',
    #                     'Database': 'string',
    #                     'Warehouse': 'string'
    #                 },
    #                 'SparkParameters': {
    #                     'Host': 'string',
    #                     'Port': 123
    #                 },
    #                 'SqlServerParameters': {
    #                     'Host': 'string',
    #                     'Port': 123,
    #                     'Database': 'string'
    #                 },
    #                 'TeradataParameters': {
    #                     'Host': 'string',
    #                     'Port': 123,
    #                     'Database': 'string'
    #                 },
    #                 'TwitterParameters': {
    #                     'Query': 'string',
    #                     'MaxRows': 123
    #                 },
    #                 'AmazonOpenSearchParameters': {
    #                     'Domain': 'string'
    #                 },
    #                 'ExasolParameters': {
    #                     'Host': 'string',
    #                     'Port': 123
    #                 }
    #             },
    #         ]
    #     },
    #     'CopySourceArn': 'string'
    # },
    # Permissions=[
    #     {
    #         'Principal': 'string',
    #         'Actions': [
    #             'string',
    #         ]
    #     },
    # ],
    # VpcConnectionProperties={
    #     'VpcConnectionArn': 'string'
    # },
    # SslProperties={
    #     'DisableSsl': True | False
    # },
    # Tags=[
    #     {
    #         'Key': 'string',
    #         'Value': 'string'
    #     },
    # ]
)
print("complete")

# response = client.create_data_source(
#     AwsAccountId='774446988871',
#     DataSourceId='unique-data-string-for-this-quicksight',
#     Name='athena_datasource',
#     Type='ATHENA',
#     DataSourceParameters={
#         'AthenaParameters': {
#             'WorkGroup': 'primary'
#         }
#     },
# )

# response = client.create_data_set(
#     AwsAccountId='774446988871',
#     DataSetId='unique-id-for-new-dataset',
#     Name='new_dataset',
#     PhysicalTableMap={
#         'string': {
#             'RelationalTable': {
#                 'DataSourceArn': 'arn:aws:quicksight:us-east-1:774446988871:datasource/unique-data-string-for-this-quicksight',
#                 # 'Catalog': 'string',
#                 # 'Schema': 'string',
#                 'Name': 'new_table',
#                 'InputColumns': [
#                     {
#                         'Name': 'report time period start',
#                         'Type': 'STRING'
#                     },
#                 ]
#             },
#         }
#     },
#     ImportMode='SPICE',
# )

# # response = client.create_analysis(
# #     AwsAccountId='774446988871',
# #     AnalysisId='unique-id-for-new-analysis',
# #     Name='new_analysis',
# #     SourceEntity={
# #         'SourceTemplate': {
# #             'DataSetReferences': [
# #                 {
# #                     'DataSetPlaceholder': 'string',
# #                     'DataSetArn': 'arn:aws:quicksight:us-east-1:774446988871:dataset/unique-id-for-new-dataset'
# #                 },
# #             ],
# #             'Arn': 'arn:aws:quicksight:us-east-1:774446988871:datasource/unique-data-string-for-this-quicksight'
# #         }
# #     }
# # )

# pp = pprint.PrettyPrinter(depth=4)

# response = client.list_data_sources(
#     AwsAccountId='774446988871'
# )
# pp.pprint(response)

# response = client.list_data_sets(
#     AwsAccountId='774446988871',
# )
# pp.pprint(response)

# response = client.list_analyses(
#     AwsAccountId='774446988871',
# )
# pp.pprint(response)

# response = client.delete_data_source(
#     AwsAccountId='774446988871',
#     DataSourceId='unique-data-string-for-this-quicksight'
# )

# print(response)
