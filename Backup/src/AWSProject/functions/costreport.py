import boto3
from datetime import datetime


class CostReport:

    def __init__(self, client):
        self.client = client

    def create_cost_report(self, bucket_name):

        now = datetime.now()
        folder_name = now.strftime("%m/%d/%Y")

        try:
            response = self.client.put_report_definition(
                ReportDefinition={
                    'ReportName': 'costreport',
                    'TimeUnit': 'HOURLY',
                    'Format': 'textORcsv',
                    'Compression': 'GZIP',
                    'AdditionalSchemaElements': [
                        'RESOURCES',
                    ],
                    'S3Bucket': bucket_name,
                    'S3Prefix': folder_name,
                    'S3Region': 'us-east-1',
                    'AdditionalArtifacts': [
                        'QUICKSIGHT',
                    ],
                    'RefreshClosedReports': True,
                    'ReportVersioning': 'CREATE_NEW_REPORT',
                }
            )
            print("Successfully created cost report")
        except NameError:
            print("Error creating cost report")
