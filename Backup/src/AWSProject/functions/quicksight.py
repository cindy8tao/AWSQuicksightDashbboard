
import pprint
import boto3


class Quicksight:

    def __init__(self, account_id, client):
        self.account_id = account_id
        self.client = client

    def set_template_permissions(self):
        try:
            response = self.client.update_template_permissions(
                AwsAccountId='263675971756',
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
