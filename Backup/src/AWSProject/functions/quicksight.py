
import pprint
import boto3


class Quicksight:

    def __init__(self, account_id, client):
        self.account_id = account_id
        self.client = client

    def set_template_permissions(self):
        try:
            response = self.client.update_template_permissions(
                AwsAccountId='774446988871',
                TemplateId='sharable-template-for-backup-in-quicksight',
                GrantPermissions=[
                    {
                        'Principal': "arn:aws:iam::" + self.account_id + ":root",
                        'Actions': [
                            'quicksight:UpdateTemplatePermissions',
                            'quicksight:UpdateTemplate',
                            'quicksight:DescribeTemplatePermissions',
                            'quicksight:UpdateTemplateAlias',
                            'quicksight:DeleteTemplateAlias',
                            'quicksight:DescribeTemplateAlias',
                            'quicksight:ListTemplateVersions',
                            'quicksight:ListTemplateAliases',
                            'quicksight:DescribeTemplate',
                            'quicksight:CreateTemplateAlias',
                            'quicksight:DeleteTemplate',
                        ]
                    },
                ],
            )
            print("Successfully set template permission")
        except NameError:
            print("Error when setting template permission")

    def set_analysis_permission(self):
        try:
            response = self.client.update_analysis_permissions(
                AwsAccountId='774446988871',
                AnalysisId='sharable-analysis-for-backup-in-quicksight',
                GrantPermissions=[
                    {
                        'Principal': 'arn:aws:iam::' + self.account_id + ':root',
                        'Actions': [
                            'quicksight:RestoreAnalysis',
                            'quicksight:UpdateAnalysisPermissions',
                            'quicksight:DeleteAnalysis',
                            'quicksight:DescribeAnalysisPermissions',
                            'quicksight:QueryAnalysis',
                            'quicksight:DescribeAnalysis',
                            'quicksight:UpdateAnalysis',
                        ]
                    },
                ],
            )
            print("Successfully set analysis permission")
        except NameError:
            print("Error when setting analysis permission")


client = boto3.client('quicksight')
# response = client.update_template_permissions(
#     AwsAccountId='774446988871',
#     TemplateId='sharable-template-for-backup-in-quicksight',
#     GrantPermissions=[
#         {
#             'Principal': 'arn:aws:iam::261297506777:root',
#             'Actions': [
#                 'quicksight:UpdateTemplatePermissions',
#                 'quicksight:UpdateTemplate',
#                 'quicksight:DescribeTemplatePermissions',
#                 'quicksight:UpdateTemplateAlias',
#                 'quicksight:DeleteTemplateAlias',
#                 'quicksight:DescribeTemplateAlias',
#                 'quicksight:ListTemplateVersions',
#                 'quicksight:ListTemplateAliases',
#                 'quicksight:DescribeTemplate',
#                 'quicksight:CreateTemplateAlias',
#                 'quicksight:DeleteTemplate',
#             ]
#         },
#     ]
# )

# response = client.update_analysis_permissions(
#     AwsAccountId='774446988871',
#     AnalysisId='sharable-analysis-for-backup-in-quicksight',
#     GrantPermissions=[
#         {
#             'Principal': 'arn:aws:iam::261297506777:root',
#             'Actions': [
#                 'quicksight:RestoreAnalysis',
#                 'quicksight:UpdateAnalysisPermissions',
#                 'quicksight:DeleteAnalysis',
#                 'quicksight:DescribeAnalysisPermissions',
#                 'quicksight:QueryAnalysis',
#                 'quicksight:DescribeAnalysis',
#                 'quicksight:UpdateAnalysis',
#             ]
#         },
#     ],
# )

# response = client.update_analysis_permissions(
#     AwsAccountId='774446988871',
#     AnalysisId='sharable-analysis-for-backup-in-quicksight',
#     GrantPermissions=[
#         {
#             'Principal': 'arn:aws:iam::261297506777:root',
#             'Actions': [
#                 'quicksight:DescribeAnalysis',
#             ]
#         },
#     ]
# )

# response = client.describe_analysis_permissions(
#     AwsAccountId='774446988871',
#     AnalysisId='sharable-analysis-for-backup-in-quicksight'
# )

# response = client.describe_template_permissions(
#     AwsAccountId='774446988871',
#     TemplateId='sharable-template-for-backup-in-quicksight'
# )
# response = client.list_users(
#     AwsAccountId='774446988871',
#     Namespace='default'
# )
# response = client.describe_template(
#     AwsAccountId='774446988871',
#     TemplateId='sharable-template-for-backup-in-quicksight',
# )
response = client.list_dashboards(
    AwsAccountId='774446988871'
)

pprint.PrettyPrinter(indent=4).pprint(response)
