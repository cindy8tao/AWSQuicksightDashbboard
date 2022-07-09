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
#     DataSourceId='unique-data-source-id-123',
#     Name='newdatasource',
#     Type='S3',
#     DataSourceParameters={
#         'S3Parameters': {
#             'ManifestFileLocation': {
#                 'Bucket': 'new-backup-report-based-arn-tags',
#                 'Key': 'manifest.json'
#             }
#         }
#     },
#     Permissions=[
#         {
#             'Principal': 'arn:aws:quicksight:us-east-1:774446988871:user/default/774446988871',
#             'Actions': [
#                 'quicksight:DescribeDataSource',
#                 'quicksight:DescribeDataSourcePermissions',
#                 'quicksight:UpdateDataSource',
#                 'quicksight:UpdateDataSourcePermissions',
#                 'quicksight:DeleteDataSource',
#                 'quicksight:PassDataSource'
#             ]
#         },
#     ]
# )
# print("complete")

# response = client.create_data_set(
#     AwsAccountId='774446988871',
#     DataSetId='unique-id-for-new-dataset',
#     Name='new_dataset',
#     PhysicalTableMap={
#         'string': {
#             'S3Source': {
#                 'DataSourceArn': 'arn:aws:quicksight:us-east-1:774446988871:datasource/unique-data-source-id-123',
#                 'UploadSettings': {
#                     'Format': 'CSV',
#                     'StartFromRow': 1,
#                     'ContainsHeader': True,
#                     'TextQualifier': 'SINGLE_QUOTE',
#                     'Delimiter': ','
#                 },
#                 'InputColumns': [
#                     {
#                         'Name': 'ResourceArn',
#                         'Type': 'STRING'
#                     },
#                     {
#                         'Name': 'Environment',
#                         'Type': 'STRING'
#                     },
#                     {
#                         'Name': 'Department',
#                         'Type': 'STRING'
#                     },
#                     {
#                         'Name': 'ResourceType',
#                         'Type': 'STRING'
#                     },
#                 ]
#             }
#         }
#     },
#     ImportMode='SPICE',
#     Permissions=[
#         {
#             'Principal': 'arn:aws:quicksight:us-east-1:774446988871:user/default/774446988871',
#             'Actions': [
#                 'quicksight:PassDataSet',
#                 'quicksight:DescribeIngestion',
#                 'quicksight:CreateIngestion',
#                 'quicksight:UpdateDataSet',
#                 'quicksight:DeleteDataSet',
#                 'quicksight:DescribeDataSet',
#                 'quicksight:CancelIngestion',
#                 'quicksight:DescribeDataSetPermissions',
#                 'quicksight:ListIngestions',
#                 'quicksight:UpdateDataSetPermissions'
#             ]
#         },
#     ],
# )


# response = client.create_template(
#     AwsAccountId='774446988871',
#     TemplateId='unique-id-for-new-template',
#     Name='new_template',
#     Permissions=[
#         {
#             'Principal': 'arn:aws:quicksight:us-east-1:774446988871:user/default/774446988871',
#             'Actions': [
#                 'quicksight:UpdateTemplatePermissions',
#                 'quicksight:DescribeTemplatePermissions',
#                 'quicksight:UpdateTemplateAlias',
#                 'quicksight:DeleteTemplateAlias',
#                 'quicksight:DescribeTemplateAlias',
#                 'quicksight:ListTemplateAliases',
#                 'quicksight:ListTemplates',
#                 'quicksight:CreateTemplateAlias',
#                 'quicksight:DeleteTemplate',
#                 'quicksight:UpdateTemplate',
#                 'quicksight:ListTemplateVersions',
#                 'quicksight:DescribeTemplate',
#                 'quicksight:CreateTemplate'
#             ]
#         },
#     ],
#     SourceEntity={
#         'SourceAnalysis': {
#             'Arn': 'arn:aws:quicksight:us-east-1:774446988871:analysis/d1ca679c-4db5-41f8-b992-a6bd0353b6b3',
#             'DataSetReferences': [
#                 {
#                     'DataSetPlaceholder': 'ds-123',
#                     'DataSetArn': 'arn:aws:quicksight:us-east-1:774446988871:dataset/unique-id-for-new-dataset'
#                 },
#             ]
#         },
#         # 'SourceTemplate': {
#         #     'Arn': 'arn:aws:quicksight:us-east-1:774446988871:user/default/774446988871'
#         # }
#     }
# )


response = client.create_analysis(
    AwsAccountId='774446988871',
    AnalysisId='unique-id-for-new-analysis',
    Name='new_analysis',
    Permissions=[
        {
            'Principal': 'arn:aws:quicksight:us-east-1:774446988871:user/default/774446988871',
            'Actions': [
                'quicksight:RestoreAnalysis',
                'quicksight:UpdateAnalysisPermissions',
                'quicksight:DeleteAnalysis',
                'quicksight:DescribeAnalysisPermissions',
                'quicksight:QueryAnalysis',
                'quicksight:DescribeAnalysis',
                'quicksight:UpdateAnalysis'
            ]
        },
    ],
    SourceEntity={
        'SourceTemplate': {
            'DataSetReferences': [
                {
                    'DataSetPlaceholder': 'ds-123',
                    'DataSetArn': 'arn:aws:quicksight:us-east-1:774446988871:dataset/unique-id-for-new-dataset'
                },
            ],
            'Arn': 'arn:aws:quicksight:us-east-1:774446988871:template/unique-id-for-new-template'
        }
    },
    ThemeArn='string',
)


# response = client.create_dashboard(
#     AwsAccountId='774446988871',
#     DashboardId='unique-dashboard-id',
#     Name='new_dashboard',
#     Permissions=[
#         {
#             'Principal': 'arn:aws:quicksight:us-east-1:774446988871:user/default/774446988871',
#             'Actions': [
#                 'quicksight:DescribeDashboard',
#                 'quicksight:ListDashboardVersions',
#                 'quicksight:UpdateDashboardPermissions',
#                 'quicksight:QueryDashboard',
#                 'quicksight:UpdateDashboard',
#                 'quicksight:DeleteDashboard',
#                 'quicksight:DescribeDashboardPermissions',
#                 'quicksight:UpdateDashboardPublishedVersion'
#             ]
#         },
#     ],
#     SourceEntity={
#         'SourceTemplate': {
#             'DataSetReferences': [
#                 {
#                     'DataSetPlaceholder': 'ds-123',
#                     'DataSetArn': 'arn:aws:quicksight:us-east-1:774446988871:dataset/unique-id-for-new-dataset'
#                 },
#             ],
#             'Arn': 'arn:aws:quicksight:us-east-1:774446988871:template/unique-id-for-new-template'
#         }
#     },
#     #     Tags=[
#     #         {
#     #             'Key': 'string',
#     #             'Value': 'string'
#     #         },
#     #     ],
#     #     VersionDescription='string',
#     #     DashboardPublishOptions={
#     #         'AdHocFilteringOption': {
#     #             'AvailabilityStatus': 'ENABLED' | 'DISABLED'
#     #         },
#     #         'ExportToCSVOption': {
#     #             'AvailabilityStatus': 'ENABLED' | 'DISABLED'
#     #         },
#     #         'SheetControlsOption': {
#     #             'VisibilityState': 'EXPANDED' | 'COLLAPSED'
#     #         }
#     #     },
#     #     ThemeArn='string'
# )


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
#     DataSourceId='unique-data-source-id-123'
# )

# print(response)

# response = client.delete_data_set(
#     AwsAccountId='774446988871',
#     DataSetId='unique-id-for-new-dataset'
# )
# print(response)

# response = client.list_templates(
#     AwsAccountId='774446988871',
# )
# print(response)

# 'RelationalTable': {
#     'DataSourceArn': 'arn:aws:quicksight:us-east-1:774446988871:datasource/unique-data-source-id-123',
#     # 'Catalog': 'string',
#     # 'Schema': 'string',
#     'Name': 'new_table',
#     'InputColumns': [
#         {
#             'Name': 'resource_arn',
#             'Type': 'STRING'
#         },
#         {
#             'Name': 'Environment',
#             'Type': 'STRING'
#         },
#         {
#             'Name': 'Department',
#             'Type': 'STRING'
#         },
#     ]
# },

# response = client.describe_user(
#     UserName='774446988871',
#     AwsAccountId='774446988871',
#     Namespace='default'
# )

# print(response)


# response = client.describe_analysis(
#     AwsAccountId='774446988871',
#     AnalysisId='d1ca679c-4db5-41f8-b992-a6bd0353b6b3'
# )

# print(response)

# response = client.describe_template(
#     AwsAccountId='774446988871',
#     TemplateId='unique-id-for-new-template',
# )

# print(response)
