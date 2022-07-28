import pprint
import boto3

client = boto3.client('quicksight')

# response = client.create_data_source(
#     AwsAccountId='263675971756',
#     DataSourceId='unique-datasource-263675971756',
#     Name='datasource-263675971756',
#     Type='ATHENA',
#     DataSourceParameters={
#         'AthenaParameters': {
#             'WorkGroup': 'default'
#         },
#     },
#     Permissions=[
#         {
#             'Principal': 'arn:aws:quicksight:us-east-1:263675971756:user/default/263675971756',
#             'Actions': [
#                 'quicksight:DescribeDataSource',
#                 'quicksight:DescribeDataSourcePermissions',
#                 'quicksight:UpdateDataSource',
#                 'quicksight:UpdateDataSourcePermissions',
#                 'quicksight:DeleteDataSource',
#                 'quicksight:PassDataSource'
#             ]
#         }
#     ]
# )
# print("Create data source")

# response = client.create_data_source(
#     AwsAccountId='263675971756',
#     DataSourceId='cost-unique-datasource-263675971756',
#     Name='cost-datasource-263675971756',
#     Type='ATHENA',
#     DataSourceParameters={
#         'AthenaParameters': {
#             'WorkGroup': 'default'
#         },
#     },
#     Permissions=[
#         {
#             'Principal': 'arn:aws:quicksight:us-east-1:263675971756:user/default/263675971756',
#             'Actions': [
#                 'quicksight:DescribeDataSource',
#                 'quicksight:DescribeDataSourcePermissions',
#                 'quicksight:UpdateDataSource',
#                 'quicksight:UpdateDataSourcePermissions',
#                 'quicksight:DeleteDataSource',
#                 'quicksight:PassDataSource'
#             ]
#         }
#     ]
# )
# print("Create cost source")

# columns = []

# columns.append({
#     'Name': 'CreationDate',
#     'Type': 'DATETIME'
# },)

# columns.append({
#     'Name': 'CompletionDate',
#     'Type': 'DATETIME'
# },)

# columns.append({
#     'Name': 'ResourceArn',
#     'Type': 'STRING'
# },)

# columns.append({
#     'Name': 'ResourceType',
#     'Type': 'STRING'
# },)

# columns.append({
#     'Name': 'BackupSize',
#     'Type': 'DECIMAL'
# },)

# columns.append({
#     'Name': 'TagKey',
#     'Type': 'STRING'
# },)

# columns.append({
#     'Name': 'TagValue',
#     'Type': 'STRING'
# },)

# response = client.create_data_set(
#     AwsAccountId='263675971756',
#     DataSetId='unique-dataset-263675971756',
#     Name='dataset-263675971756',
#     PhysicalTableMap={
#         'string': {
#             'CustomSql': {
#                 'DataSourceArn': 'arn:aws:quicksight:us-east-1:263675971756:datasource/unique-datasource-263675971756',
#                 'Name': 'backup-report',
#                 'SqlQuery': 'SELECT * FROM "database_263675971756"."backup_report"',
#                 'Columns': columns
#             }
#         }
#     },
#     ImportMode='SPICE',
#     Permissions=[
#         {
#             'Principal': 'arn:aws:quicksight:us-east-1:263675971756:user/default/263675971756',
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
# print("Update dataset complete")

# columns = []

# columns.append({
#     'Name': 'Start',
#     'Type': 'DATETIME'
# },)

# columns.append({
#     'Name': 'End',
#     'Type': 'DATETIME'
# },)

# columns.append({
#     'Name': 'Tags',
#     'Type': 'STRING'
# },)

# columns.append({
#     'Name': 'UnblendedCost',
#     'Type': 'DECIMAL'
# },)


# response = client.create_data_set(
#     AwsAccountId='263675971756',
#     DataSetId='cost-unique-dataset-263675971756',
#     Name='cost-dataset-263675971756',
#     PhysicalTableMap={
#         'string': {
#             'CustomSql': {
#                 'DataSourceArn': 'arn:aws:quicksight:us-east-1:263675971756:datasource/cost-unique-datasource-263675971756',
#                 'Name': 'backup-report',
#                 'SqlQuery': 'SELECT * FROM "cost_database_263675971756"."cost_report"',
#                 'Columns': columns
#             }
#         }
#     },
#     ImportMode='SPICE',
#     Permissions=[
#         {
#             'Principal': 'arn:aws:quicksight:us-east-1:263675971756:user/default/263675971756',
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
# print("Update cost dataset complete")

# response = client.create_template(
#     AwsAccountId='263675971756',
#     TemplateId='sharable-template-for-backup-in-quicksight',
#     Name='sharable-template-for-backup-in-quicksight',
#     Permissions=[
#         {
#             'Principal': 'arn:aws:quicksight:us-east-1:263675971756:user/default/263675971756',
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
#             'Arn': 'arn:aws:quicksight:us-east-1:263675971756:analysis/f7df932c-941d-4216-9575-56d56eb92d0c',
#             # 'Arn': 'arn:aws:quicksight:us-east-1:'+263675971756+':analysis/unique-id-for-new-analysis263675971756',
#             'DataSetReferences': [
#                 {
#                     'DataSetPlaceholder': 'BackupData',
#                     'DataSetArn': 'arn:aws:quicksight:us-east-1:263675971756:dataset/unique-dataset-263675971756'
#                 },
#                 {
#                     'DataSetPlaceholder': 'CostData',
#                     'DataSetArn': 'arn:aws:quicksight:us-east-1:263675971756:dataset/cost-unique-dataset-263675971756'
#                 }
#             ]
#         }
#     }
# )

# response = client.update_template(
#     AwsAccountId='263675971756',
#     TemplateId='sharable-template-for-backup-in-quicksight',
#     SourceEntity={
#         'SourceAnalysis': {
#             'Arn': 'arn:aws:quicksight:us-east-1:263675971756:analysis/sharable-analysis-for-backup-in-quicksight',
#             'DataSetReferences': [
#                 {
#                     'DataSetPlaceholder': 'BackupData',
#                     'DataSetArn': 'arn:aws:quicksight:us-east-1:263675971756:dataset/unique-dataset-263675971756'
#                 },
#                 {
#                     'DataSetPlaceholder': 'CostData',
#                     'DataSetArn': 'arn:aws:quicksight:us-east-1:263675971756:dataset/cost-unique-dataset-263675971756'
#                 }
#             ]
#         }
#     }
# )

# response = client.update_analysis(
#     AwsAccountId='263675971756',
#     AnalysisId='sharable-analysis-for-backup-in-quicksight',
#     Name='sharable-analysis-for-backup-in-quicksight',
#     SourceEntity={
#         'SourceTemplate': {
#             'DataSetReferences': [
#                 {
#                     'DataSetPlaceholder': 'BackupData',
#                     'DataSetArn': 'arn:aws:quicksight:us-east-1:263675971756:dataset/unique-dataset-263675971756'
#                 },
#                 {
#                     'DataSetPlaceholder': 'CostData',
#                     'DataSetArn': 'arn:aws:quicksight:us-east-1:263675971756:dataset/cost-unique-dataset-263675971756'
#                 }
#             ],
#             'Arn': 'arn:aws:quicksight:us-east-1:'+'263675971756'+':template/sharable-template-for-backup-in-quicksight'
#         }
#     }
# )
# print("Successfully updated analysis")

# response = client.create_analysis(
#     AwsAccountId='263675971756',
#     AnalysisId='sharable-analysis-for-backup-in-quicksight',
#     Name='sharable-analysis-for-backup-in-quicksight',
#     Permissions=[
#         {
#             'Principal': 'arn:aws:quicksight:us-east-1:263675971756:user/default/263675971756',
#             'Actions': [
#                 'quicksight:RestoreAnalysis',
#                 'quicksight:UpdateAnalysisPermissions',
#                 'quicksight:DeleteAnalysis',
#                 'quicksight:DescribeAnalysisPermissions',
#                 'quicksight:QueryAnalysis',
#                 'quicksight:DescribeAnalysis',
#                 'quicksight:UpdateAnalysis'
#             ]
#         },
#     ],
#     SourceEntity={
#         'SourceTemplate': {
#             'DataSetReferences': [
#                 {
#                     'DataSetPlaceholder': 'BackupData',
#                     'DataSetArn': 'arn:aws:quicksight:us-east-1:263675971756:dataset/unique-dataset-263675971756'
#                 },
#                 {
#                     'DataSetPlaceholder': 'CostData',
#                     'DataSetArn': 'arn:aws:quicksight:us-east-1:263675971756:dataset/cost-unique-dataset-263675971756'
#                 }
#             ],
#             'Arn': 'arn:aws:quicksight:us-east-1:263675971756:template/sharable-template-for-backup-in-quicksight'
#         }
#     }
# )

response = client.update_analysis(
    AwsAccountId='263675971756',
    AnalysisId='unique-analysis-263675971756',
    Name='unique-analysis-263675971756',
    SourceEntity={
        'SourceTemplate': {
            'DataSetReferences': [
                {
                    'DataSetPlaceholder': 'BackupData',
                    'DataSetArn': 'arn:aws:quicksight:us-east-1:263675971756:dataset/unique-dataset-263675971756'
                },
                {
                    'DataSetPlaceholder': 'CostData',
                    'DataSetArn': 'arn:aws:quicksight:us-east-1:263675971756:dataset/cost-unique-dataset-263675971756'
                }
            ],
            'Arn': 'arn:aws:quicksight:us-east-1:263675971756:template/sharable-template-for-backup-in-quicksight'
        }
    },
    ThemeArn='arn:aws:quicksight::aws:theme/MIDNIGHT'
)

# response = client.create_dashboard(
#     AwsAccountId='263675971756',
#     DashboardId='unique-dashboard-263675971756',
#     Name='dashboard-263675971756',
#     Permissions=[
#         {
#             'Principal': 'arn:aws:quicksight:us-east-1:263675971756:user/default/263675971756',
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
#                     'DataSetPlaceholder': 'BackupData',
#                     'DataSetArn': 'arn:aws:quicksight:us-east-1:263675971756:dataset/unique-dataset-263675971756'
#                 },
#                 {
#                     'DataSetPlaceholder': 'CostData',
#                     'DataSetArn': 'arn:aws:quicksight:us-east-1:263675971756:dataset/cost-unique-dataset-263675971756'
#                 }
#             ],
#             'Arn': 'arn:aws:quicksight:us-east-1:263675971756:template/unique-template-263675971756'
#         }
#     }
# )
# print("Successfully created dashboard")


# response = client.list_templates(
#     AwsAccountId='263675971756',
# )

# response = client.describe_template_permissions(
#     AwsAccountId='263675971756',
#     TemplateId='sharable-template-for-backup-in-quicksight'
# )


# response = client.update_template_permissions(
#     AwsAccountId='263675971756',
#     TemplateId='sharable-template-for-backup-in-quicksight',
#     GrantPermissions=[
#         {
#             'Principal': 'arn:aws:iam::744878436330:root',
#             'Actions': [
#                 'quicksight:UpdateTemplate',
#                 'quicksight:UpdateTemplatePermissions',
#                 'quicksight:DescribeTemplatePermissions',
#                 'quicksight:UpdateTemplateAlias',
#                 'quicksight:DeleteTemplateAlias',
#                 'quicksight:DescribeTemplateAlias',
#                 'quicksight:ListTemplateVersions',
#                 'quicksight:DescribeTemplate',
#                 'quicksight:ListTemplateAliases',
#                 'quicksight:CreateTemplateAlias',
#                 'quicksight:DeleteTemplate'
#             ]
#         },
#     ]
# )


# response = client.list_themes(
#     AwsAccountId='263675971756',
# )

# pprint.PrettyPrinter(indent=4).pprint(response)
