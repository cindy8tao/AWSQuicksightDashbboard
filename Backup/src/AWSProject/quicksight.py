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

# response = client.create_analysis(
#     AwsAccountId='774446988871',
#     AnalysisId='unique-id-for-new-analysis',
#     Name='new_analysis',
#     SourceEntity={
#         'SourceTemplate': {
#             'DataSetReferences': [
#                 {
#                     'DataSetPlaceholder': 'string',
#                     'DataSetArn': 'arn:aws:quicksight:us-east-1:774446988871:dataset/unique-id-for-new-dataset'
#                 },
#             ],
#             'Arn': 'arn:aws:quicksight:us-east-1:774446988871:datasource/unique-data-string-for-this-quicksight'
#         }
#     }
# )

pp = pprint.PrettyPrinter(depth=4)

response = client.list_data_sources(
    AwsAccountId='774446988871'
)
pp.pprint(response)

response = client.list_data_sets(
    AwsAccountId='774446988871',
)
pp.pprint(response)

response = client.list_analyses(
    AwsAccountId='774446988871',
)
pp.pprint(response)

# response = client.delete_data_source(
#     AwsAccountId='774446988871',
#     DataSourceId='unique-data-string-for-this-quicksight'
# )

# print(response)
