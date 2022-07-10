import datetime
import time
import boto3
import json
import pprint
from datetime import datetime


class Quicksight:

    def __init__(self, account_id, client, user):
        self.account_id = account_id
        self.client = client
        self.user = user

    def create_new_datasource(self):
        now = datetime.now()
        folder_name = now.strftime("%m/%d/%Y")

        # try:
        response = self.client.create_data_source(
            AwsAccountId=self.account_id,
            DataSourceId='unique-data-source-id-'+self.account_id,
            Name='datasource'+self.account_id,
            Type='S3',
            DataSourceParameters={
                'S3Parameters': {
                    'ManifestFileLocation': {
                        'Bucket': 'new-backup-report-based-arn-tags-'+self.account_id,
                        'Key': folder_name + '/manifest.json'
                    }
                }
            },
            Permissions=[
                {
                    'Principal': 'arn:aws:quicksight:us-east-1:'+self.account_id+':user/default/'+self.user,
                    'Actions': [
                        'quicksight:DescribeDataSource',
                        'quicksight:DescribeDataSourcePermissions',
                        'quicksight:UpdateDataSource',
                        'quicksight:UpdateDataSourcePermissions',
                        'quicksight:DeleteDataSource',
                        'quicksight:PassDataSource'
                    ]
                },
            ]
        )
        print("Create new source completed")

    def create_datasource(self):

        try:
            self.create_new_datasource()
            print("Created new datasource complete")
        except:
            self.update_datasource()

    def update_datasource(self):
        now = datetime.now()
        folder_name = now.strftime("%m/%d/%Y")

        response = self.client.update_data_source(
            AwsAccountId=self.account_id,
            DataSourceId='unique-data-source-id-'+self.account_id,
            Name='datasource'+self.account_id,
            DataSourceParameters={
                'S3Parameters': {
                    'ManifestFileLocation': {
                        'Bucket': 'new-backup-report-based-arn-tags-'+self.account_id,
                        'Key': folder_name + '/manifest.json'
                    }
                }
            }
        )
        print("Updated source")

    def create_new_dataset(self):
        response = self.client.create_data_set(
            AwsAccountId=self.account_id,
            DataSetId='unique-id-for-new-dataset'+self.account_id,
            Name='dataset'+self.account_id,
            PhysicalTableMap={
                'string': {
                    'S3Source': {
                        'DataSourceArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':datasource/'+'unique-data-source-id-'+self.account_id,
                        'UploadSettings': {
                            'Format': 'CSV',
                            'StartFromRow': 1,
                            'ContainsHeader': True,
                            'TextQualifier': 'SINGLE_QUOTE',
                            'Delimiter': ','
                        },
                        'InputColumns': [
                            {
                                'Name': 'ResourceArn',
                                'Type': 'STRING'
                            },
                            {
                                'Name': 'Environment',
                                'Type': 'STRING'
                            },
                            {
                                'Name': 'Department',
                                'Type': 'STRING'
                            },
                            {
                                'Name': 'ResourceType',
                                'Type': 'STRING'
                            },
                        ]
                    }
                }
            },
            ImportMode='SPICE',
            Permissions=[
                {
                    'Principal': 'arn:aws:quicksight:us-east-1:'+self.account_id+':user/default/'+self.user,
                    'Actions': [
                        'quicksight:PassDataSet',
                        'quicksight:DescribeIngestion',
                        'quicksight:CreateIngestion',
                        'quicksight:UpdateDataSet',
                        'quicksight:DeleteDataSet',
                        'quicksight:DescribeDataSet',
                        'quicksight:CancelIngestion',
                        'quicksight:DescribeDataSetPermissions',
                        'quicksight:ListIngestions',
                        'quicksight:UpdateDataSetPermissions'
                    ]
                },
            ],
        )
        print("Update dataset complete")

    def create_dataset(self):

        try:
            self.create_new_dataset()
            print("Created new dataset complete")
        except:
            self.delete_dataset('unique-id-for-new-dataset'+self.account_id)
            print("Wait 5 seconds for the dataset to delete ... ")
            time.sleep(5)
            self.create_new_dataset()

    def update_dateset(self):

        response = self.client.update_data_set(
            AwsAccountId=self.account_id,
            DataSetId='unique-id-for-new-dataset'+self.account_id,
            Name='dataset'+self.account_id,
            PhysicalTableMap={
                'string': {
                    'S3Source': {
                        'DataSourceArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':datasource/'+'unique-data-source-id-'+self.account_id,
                        'UploadSettings': {
                            'Format': 'CSV',
                            'StartFromRow': 1,
                            'ContainsHeader': True,
                            'TextQualifier': 'SINGLE_QUOTE',
                            'Delimiter': ','
                        },
                        'InputColumns': [
                            {
                                'Name': 'ResourceArn',
                                'Type': 'STRING'
                            },
                            {
                                'Name': 'Environment',
                                'Type': 'STRING'
                            },
                            {
                                'Name': 'Department',
                                'Type': 'STRING'
                            },
                            {
                                'Name': 'ResourceType',
                                'Type': 'STRING'
                            },
                        ]
                    }
                }
            },
            ImportMode='SPICE',
        )
        print("Updated dataset")

    def create_template(self):
        try:
            response = self.client.create_template(
                AwsAccountId=self.account_id,
                TemplateId='unique-id-for-new-template'+self.account_id,
                Name='template'+self.account_id,
                Permissions=[
                    {
                        'Principal': 'arn:aws:quicksight:us-east-1:'+self.account_id+':user/default/'+self.user,
                        'Actions': [
                            'quicksight:UpdateTemplatePermissions',
                            'quicksight:DescribeTemplatePermissions',
                            'quicksight:UpdateTemplateAlias',
                            'quicksight:DeleteTemplateAlias',
                            'quicksight:DescribeTemplateAlias',
                            'quicksight:ListTemplateAliases',
                            'quicksight:ListTemplates',
                            'quicksight:CreateTemplateAlias',
                            'quicksight:DeleteTemplate',
                            'quicksight:UpdateTemplate',
                            'quicksight:ListTemplateVersions',
                            'quicksight:DescribeTemplate',
                            'quicksight:CreateTemplate'
                        ]
                    },
                ],
                SourceEntity={
                    'SourceAnalysis': {
                        # 'Arn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':analysis/3f55df65-8c60-4a5c-bc24-926502089523',
                        'Arn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':analysis/unique-id-for-new-analysis774446988871',
                        # 'Arn': 'arn:aws:quicksight:us-east-1:744878436330:analysis/BoS-For-AWSBackup-Analysis-db697840',
                        'DataSetReferences': [
                            {
                                'DataSetPlaceholder': 'ds-123',
                                'DataSetArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':dataset/unique-id-for-new-dataset'+self.account_id
                            },
                        ]
                    }
                }
            )
            print("Wait 5 seconds for the template to finish creation ... ")
            time.sleep(5)
            print("Successfully created template")
        except:
            response = self.client.update_template(
                AwsAccountId=self.account_id,
                TemplateId='unique-id-for-new-template'+self.account_id,
                SourceEntity={
                    'SourceAnalysis': {
                        # 'Arn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':analysis/3f55df65-8c60-4a5c-bc24-926502089523',
                        'Arn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':analysis/unique-id-for-new-analysis774446988871',
                        # 'Arn': 'arn:aws:quicksight:us-east-1:744878436330:analysis/BoS-For-AWSBackup-Analysis-db697840',
                        'DataSetReferences': [
                            {
                                'DataSetPlaceholder': 'ds-123',
                                'DataSetArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':dataset/unique-id-for-new-dataset'+self.account_id
                            },
                        ]
                    }
                }
            )
            print("Wait 5 seconds for the template to updating ... ")
            time.sleep(5)
            print("Successfully updated template")

    def create_analysis(self):

        try:
            response = self.client.create_analysis(
                AwsAccountId=self.account_id,
                AnalysisId='unique-id-for-new-analysis'+self.account_id,
                Name='analysis'+self.account_id,
                Permissions=[
                    {
                        'Principal': 'arn:aws:quicksight:us-east-1:'+self.account_id+':user/default/'+self.user,
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
                                'DataSetArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':dataset/unique-id-for-new-dataset'+self.account_id
                            },
                        ],
                        'Arn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':template/unique-id-for-new-template'+self.account_id,
                    }
                }
            )
            print("Successfully created analysis")
        except:
            response = self.client.update_analysis(
                AwsAccountId=self.account_id,
                AnalysisId='unique-id-for-new-analysis'+self.account_id,
                Name='analysis'+self.account_id,
                SourceEntity={
                    'SourceTemplate': {
                        'DataSetReferences': [
                            {
                                'DataSetPlaceholder': 'ds-123',
                                'DataSetArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':dataset/unique-id-for-new-dataset'+self.account_id
                            },
                        ],
                        'Arn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':template/unique-id-for-new-template'+self.account_id,
                    }
                }
            )
            print("Successfully updated analysis")

    def create_dashboard(self):

        try:
            response = self.client.create_dashboard(
                AwsAccountId=self.account_id,
                DashboardId='unique-dashboard-id'+self.account_id,
                Name='dashboard'+self.account_id,
                Permissions=[
                    {
                        'Principal': 'arn:aws:quicksight:us-east-1:'+self.account_id+':user/default/'+self.user,
                        'Actions': [
                            'quicksight:DescribeDashboard',
                            'quicksight:ListDashboardVersions',
                            'quicksight:UpdateDashboardPermissions',
                            'quicksight:QueryDashboard',
                            'quicksight:UpdateDashboard',
                            'quicksight:DeleteDashboard',
                            'quicksight:DescribeDashboardPermissions',
                            'quicksight:UpdateDashboardPublishedVersion'
                        ]
                    },
                ],
                SourceEntity={
                    'SourceTemplate': {
                        'DataSetReferences': [
                            {
                                'DataSetPlaceholder': 'ds-123',
                                'DataSetArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':dataset/unique-id-for-new-dataset'+self.account_id
                            },
                        ],
                        'Arn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':template/unique-id-for-new-template'+self.account_id
                    }
                }
            )
            print("Successfully created dashboard")
        except:
            response = self.client.update_dashboard(
                AwsAccountId=self.account_id,
                DashboardId='unique-dashboard-id'+self.account_id,
                Name='dashboard'+self.account_id,
                SourceEntity={
                    'SourceTemplate': {
                        'DataSetReferences': [
                            {
                                'DataSetPlaceholder': 'ds-123',
                                'DataSetArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':dataset/unique-id-for-new-dataset'+self.account_id
                            },
                        ],
                        'Arn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':template/unique-id-for-new-template'+self.account_id
                    }
                },
            )
            print("Successfully updated dashboard")

    def delete_datasource(self, datasource):

        try:
            response = self.client.delete_data_source(
                AwsAccountId=self.account_id,
                DataSourceId=datasource
            )
            print("Successfully when deleting datasource ")
        except NameError:
            print("Error when deleting datasource")

    def delete_dataset(self, dataset):
        try:
            response = self.client.delete_data_set(
                AwsAccountId=self.account_id,
                DataSetId=dataset
            )
            print("Deleting dataset ... ")
        except NameError:
            print("Error when deleting dataset")

    def delete_template(self, template):
        try:
            response = self.client.delete_template(
                AwsAccountId=self.account_id,
                TemplateId=template
            )
            print("Successfully when deleting template")
        except NameError:
            print("Error when deleting template")

    def delete_analysis(self, analysis):
        try:
            response = self.client.delete_analysis(
                AwsAccountId=self.account_id,
                AnalysisId=analysis
            )
            print("Successfully when deleting analysis")
        except NameError:
            print("Error when deleting analysis")

    def delete_dashboard(self, dashboard):
        try:
            response = self.client.delete_dashboard(
                AwsAccountId=self.account_id,
                DashboardId=dashboard
            )
            print("Successfully when deleting dashboard")
        except NameError:
            print("Error when deleting dashboard")

    # pp = pprint.PrettyPrinter(depth=4)

    # response = client.list_data_sources(
    #     AwsAccountId='774446988871'
    # )
    # pp.pprint(response)

    # response = client.list_data_sets(
    #     AwsAccountId=self.account_id,
    # )
    # pp.pprint(response)

    # response = client.list_analyses(
    #     AwsAccountId=self.account_id,
    # )
    # pp.pprint(response)

    # response = client.delete_data_source(
    #     AwsAccountId=self.account_id,
    #     DataSourceId='unique-data-source-id-123'
    # )

    # print(response)

    # response = client.delete_data_set(
    #     AwsAccountId=self.account_id,
    #     DataSetId='unique-id-for-new-dataset'
    # )
    # print(response)

    # response = client.list_templates(
    #     AwsAccountId=self.account_id,
    # )
    # print(response)

    # response = client.describe_user(
    #     UserName='774446988871',
    #     AwsAccountId=self.account_id,
    #     Namespace='default'
    # )

    # print(response)

    # client = boto3.client('quicksight')
    # response = client.describe_analysis(
    #     AwsAccountId='774446988871',
    #     AnalysisId='3f55df65-8c60-4a5c-bc24-926502089523'
    # )

    # print(response)

    # response = client.describe_template(
    #     AwsAccountId=self.account_id,
    #     TemplateId='unique-id-for-new-template',
    # )

    # print(response)

    # client = boto3.client('quicksight')

    # response = client.delete_template(
    #     AwsAccountId='774446988871',
    #     TemplateId='unique-id-for-new-template774446988871'
    # )
    # print("Successfully when deleting template")

    # client = boto3.client('quicksight')
    # response = client.list_data_sources(
    #     AwsAccountId='774446988871'
    # )
    # print(response)

    # response = client.list_data_sets(
    #     AwsAccountId='774446988871',
    # )
    # print(response)

    # pp = pprint.PrettyPrinter(depth=4)
    # response = client.list_analyses(
    #     AwsAccountId='774446988871'
    # )
    # pp.pprint(response)
