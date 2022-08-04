
import pprint
import boto3


class Quicksight:

    def __init__(self, account_id, client):
        self.account_id = account_id
        self.client = client

    def refresh_spice_data(self):

        try:
            response = self.client.create_ingestion(
                DataSetId='unique-dataset-' + self.account_id,
                IngestionId='unique-ingestion-' + self.account_id,
                AwsAccountId=self.account_id,
                IngestionType='FULL_REFRESH'
            )
            print("Successfully refreshed SPICE data")
        except NameError:
            print("Error when refreshing SPICE data")

    def refresh_cost_spice_data(self):

        try:
            response = self.client.create_ingestion(
                DataSetId='cost-unique-dataset-' + self.account_id,
                IngestionId='unique-cost-ingestion-' + self.account_id,
                AwsAccountId=self.account_id,
                IngestionType='FULL_REFRESH'
            )
            print("Successfully refreshed SPICE data")
        except NameError:
            print("Error when refreshing SPICE data")

    def update_data_set(self):

        columns = []

        columns.append({
            'Name': 'CreationDate',
            'Type': 'DATETIME'
        },)

        columns.append({
            'Name': 'CompletionDate',
            'Type': 'DATETIME'
        },)

        columns.append({
            'Name': 'ResourceArn',
            'Type': 'STRING'
        },)

        columns.append({
            'Name': 'ResourceType',
            'Type': 'STRING'
        },)

        columns.append({
            'Name': 'BackupSize',
            'Type': 'DECIMAL'
        },)

        columns.append({
            'Name': 'TagKey',
            'Type': 'STRING'
        },)

        columns.append({
            'Name': 'TagValue',
            'Type': 'STRING'
        },)

        try:
            response = self.client.update_data_set(
                AwsAccountId=self.account_id,
                DataSetId='unique-dataset-' + self.account_id,
                Name='dataset-'+self.account_id,
                PhysicalTableMap={
                    'string': {
                        'CustomSql': {
                            'DataSourceArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':datasource/unique-datasource-'+self.account_id,
                            'Name': 'backup-report',
                            'SqlQuery': 'SELECT * FROM "database_'+self.account_id+'"."backup_report"',
                            'Columns': columns
                        }
                    }
                },
                ImportMode='SPICE',
            )
            print("Successfully updated cost dataset")
        except NameError:
            print("Error when updating cost dataset")

    def cost_update_data_set(self):

        columns = []

        columns.append({
            'Name': 'Start',
            'Type': 'DATETIME'
        },)

        columns.append({
            'Name': 'End',
            'Type': 'DATETIME'
        },)

        columns.append({
            'Name': 'Tags',
            'Type': 'STRING'
        },)

        columns.append({
            'Name': 'UnblendedCost',
            'Type': 'DECIMAL'
        },)

        try:
            response = self.client.update_data_set(
                AwsAccountId=self.account_id,
                DataSetId='cost-unique-dataset-'+self.account_id,
                Name='cost-dataset-'+self.account_id,
                PhysicalTableMap={
                    'string': {
                        'CustomSql': {
                            'DataSourceArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':datasource/cost-unique-datasource-'+self.account_id,
                            'Name': 'backup-report',
                            'SqlQuery': 'SELECT * FROM "cost_database_'+self.account_id+'"."cost_report"',
                            'Columns': columns
                        }
                    }
                },
                ImportMode='SPICE',
            )
            print("Successfully updated dataset")
        except NameError:
            print("Error when updating dataset")

    def update_analysis(self):
        try:
            response = self.client.update_analysis(
                AwsAccountId=self.account_id,
                AnalysisId='unique-analysis-'+self.account_id,
                Name='analysis-'+self.account_id,
                SourceEntity={
                    'SourceTemplate': {
                        'DataSetReferences': [
                            {
                                'DataSetPlaceholder': 'BackupData',
                                'DataSetArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':dataset/unique-dataset-'+self.account_id
                            },
                            {
                                'DataSetPlaceholder': 'CostData',
                                'DataSetArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':dataset/cost-unique-dataset-'+self.account_id
                            }
                        ],
                        'Arn': 'arn:aws:quicksight:us-east-1:263675971756:template/sharable-template-for-backup-in-quicksight'
                    }
                },
                ThemeArn='arn:aws:quicksight::aws:theme/MIDNIGHT'
            )
            print("Successfully updated analysis")
        except NameError:
            print("Error when updating analysis")

    def update_dashboard(self):
        try:
            response = self.client.update_dashboard(
                AwsAccountId=self.account_id,
                DashboardId='unique-dashboard-'+self.account_id,
                Name='dashboard-'+self.account_id,
                SourceEntity={
                    'SourceTemplate': {
                        'DataSetReferences': [
                            {
                                'DataSetPlaceholder': 'BackupData',
                                'DataSetArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':dataset/unique-dataset-'+self.account_id
                            },
                            {
                                'DataSetPlaceholder': 'CostData',
                                'DataSetArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':dataset/cost-unique-dataset-'+self.account_id
                            }
                        ],
                        'Arn': 'arn:aws:quicksight:us-east-1:263675971756:template/sharable-template-for-backup-in-quicksight'
                    }
                }
            )
            print("Successfully updated dashboard")
        except NameError:
            print("Error when updating dashboard")
