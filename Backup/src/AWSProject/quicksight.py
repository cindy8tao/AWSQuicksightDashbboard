import datetime
import time
import boto3
import json
import pprint
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pprint


class Quicksight:

    def __init__(self, account_id, client, user):
        self.account_id = account_id
        self.client = client
        self.user = user

    def create_new_datasource(self, data_source_id, name, bucket, key):

        response = self.client.create_data_source(
            AwsAccountId=self.account_id,
            DataSourceId=data_source_id,
            Name=name,
            Type='S3',
            DataSourceParameters={
                'S3Parameters': {
                    'ManifestFileLocation': {
                        'Bucket': bucket,
                        'Key': key
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

    def create_datasource(self, data_source_id, name, bucket, key):

        try:
            self.create_new_datasource(data_source_id, name, bucket, key)
            print("Created new datasource complete")
        except:
            self.update_datasource(data_source_id, name, bucket, key)

    def update_datasource(self, data_source_id, name, bucket, key):

        response = self.client.update_data_source(
            AwsAccountId=self.account_id,
            DataSourceId=data_source_id,
            Name=name,
            DataSourceParameters={
                'S3Parameters': {
                    'ManifestFileLocation': {
                        'Bucket': bucket,
                        'Key': key
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

    def update_dataset(self):

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
                        # 'Arn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':analysis/17e1db06-e7ac-47a5-9df0-62be93c9a33e',
                        'Arn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':analysis/unique-id-for-new-analysis774446988871',
                        'DataSetReferences': [
                            {
                                'DataSetPlaceholder': 'ds-123',
                                'DataSetArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':dataset/unique-id-for-new-dataset'+self.account_id
                            },
                            {
                                'DataSetPlaceholder': 'cost-ds-123',
                                'DataSetArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':dataset/unique-id-for-new-cost-dataset'+self.account_id
                            }
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
                        # 'Arn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':analysis/17e1db06-e7ac-47a5-9df0-62be93c9a33e',
                        'Arn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':analysis/unique-id-for-new-analysis774446988871',
                        'DataSetReferences': [
                            {
                                'DataSetPlaceholder': 'ds-123',
                                'DataSetArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':dataset/unique-id-for-new-dataset'+self.account_id
                            },
                            {
                                'DataSetPlaceholder': 'cost-ds-123',
                                'DataSetArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':dataset/unique-id-for-new-cost-dataset'+self.account_id
                            }
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
                            {
                                'DataSetPlaceholder': 'cost-ds-123',
                                'DataSetArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':dataset/unique-id-for-new-cost-dataset'+self.account_id
                            }
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
                            {
                                'DataSetPlaceholder': 'cost-ds-123',
                                'DataSetArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':dataset/unique-id-for-new-cost-dataset'+self.account_id
                            }
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
                            {
                                'DataSetPlaceholder': 'cost-ds-123',
                                'DataSetArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':dataset/unique-id-for-new-cost-dataset'+self.account_id
                            }
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
                            {
                                'DataSetPlaceholder': 'cost-ds-123',
                                'DataSetArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':dataset/unique-id-for-new-cost-dataset'+self.account_id
                            }
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

    def create_new_cost_dataset(self):
        response = self.client.create_data_set(
            AwsAccountId=self.account_id,
            DataSetId='unique-id-for-new-cost-dataset'+self.account_id,
            Name='cost_dataset'+self.account_id,
            PhysicalTableMap={
                'string': {
                    'S3Source': {
                        'DataSourceArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':datasource/'+'unique-cost-data-source-id-'+self.account_id,
                        'UploadSettings': {
                            'Format': 'CSV',
                            'StartFromRow': 1,
                            'ContainsHeader': True,
                            'TextQualifier': 'DOUBLE_QUOTE',
                            'Delimiter': ','
                        },
                        'InputColumns': [
                            {'Name': 'identity/LineItemId',
                             'Type': 'STRING'},
                            {'Name': 'identity/TimeInterval',
                                'Type': 'STRING'},
                            {'Name': 'bill/InvoiceId',
                                'Type': 'STRING'},
                            {'Name': 'bill/InvoicingEntity',
                                'Type': 'STRING'},
                            {'Name': 'bill/BillingEntity',
                                'Type': 'STRING'},
                            {'Name': 'bill/BillType',
                                'Type': 'STRING'},
                            {'Name': 'bill/PayerAccountId',
                                'Type': 'STRING'},
                            {'Name': 'bill/BillingPeriodStartDate',
                                'Type': 'STRING'},
                            {'Name': 'bill/BillingPeriodEndDate',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/UsageAccountId',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/LineItemType',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/UsageStartDate',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/UsageEndDate',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/ProductCode',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/UsageType',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/Operation',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/AvailabilityZone',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/ResourceId',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/UsageAmount',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/NormalizationFactor',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/NormalizedUsageAmount',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/CurrencyCode',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/UnblendedRate',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/UnblendedCost',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/BlendedRate',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/BlendedCost',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/LineItemDescription',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/TaxType',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/LegalEntity',
                                'Type': 'STRING'},
                            {'Name': 'product/ProductName',
                                'Type': 'STRING'},
                            {'Name': 'product/availability',
                                'Type': 'STRING'},
                            {'Name': 'product/availabilityZone',
                                'Type': 'STRING'},
                            {'Name': 'product/backupservice',
                                'Type': 'STRING'},
                            {'Name': 'product/capacitystatus',
                                'Type': 'STRING'},
                            {'Name': 'product/classicnetworkingsupport',
                                'Type': 'STRING'},
                            {'Name': 'product/clockSpeed',
                                'Type': 'STRING'},
                            {'Name': 'product/currentGeneration',
                                'Type': 'STRING'},
                            {'Name': 'product/databaseEngine',
                                'Type': 'STRING'},
                            {'Name': 'product/datatransferout',
                                'Type': 'STRING'},
                            {'Name': 'product/dedicatedEbsThroughput',
                                'Type': 'STRING'},
                            {'Name': 'product/deploymentOption',
                                'Type': 'STRING'},
                            {'Name': 'product/description',
                                'Type': 'STRING'},
                            {'Name': 'product/durability',
                                'Type': 'STRING'},
                            {'Name': 'product/ecu',
                                'Type': 'STRING'},
                            {'Name': 'product/edition',
                                'Type': 'STRING'},
                            {'Name': 'product/engineCode',
                                'Type': 'STRING'},
                            {'Name': 'product/enhancedNetworkingSupported',
                                'Type': 'STRING'},
                            {'Name': 'product/eventType',
                                'Type': 'STRING'},
                            {'Name': 'product/freeQueryTypes',
                                'Type': 'STRING'},
                            {'Name': 'product/fromLocation',
                                'Type': 'STRING'},
                            {'Name': 'product/fromLocationType',
                                'Type': 'STRING'},
                            {'Name': 'product/fromRegionCode',
                                'Type': 'STRING'},
                            {'Name': 'product/group',
                                'Type': 'STRING'},
                            {'Name': 'product/groupDescription',
                                'Type': 'STRING'},
                            {'Name': 'product/instanceFamily',
                                'Type': 'STRING'},
                            {'Name': 'product/instanceType',
                                'Type': 'STRING'},
                            {'Name': 'product/instanceTypeFamily',
                                'Type': 'STRING'},
                            {'Name': 'product/intelAvx2Available',
                                'Type': 'STRING'},
                            {'Name': 'product/intelAvxAvailable',
                                'Type': 'STRING'},
                            {'Name': 'product/intelTurboAvailable',
                                'Type': 'STRING'},
                            {'Name': 'product/licenseModel',
                                'Type': 'STRING'},
                            {'Name': 'product/location',
                                'Type': 'STRING'},
                            {'Name': 'product/locationType',
                                'Type': 'STRING'},
                            {'Name': 'product/logsDestination',
                                'Type': 'STRING'},
                            {'Name': 'product/marketoption',
                                'Type': 'STRING'},
                            {'Name': 'product/maxIopsBurstPerformance',
                                'Type': 'STRING'},
                            {'Name': 'product/maxIopsvolume',
                                'Type': 'STRING'},
                            {'Name': 'product/maxThroughputvolume',
                                'Type': 'STRING'},
                            {'Name': 'product/maxVolumeSize',
                                'Type': 'STRING'},
                            {'Name': 'product/memory',
                                'Type': 'STRING'},
                            {'Name': 'product/messageDeliveryFrequency',
                                'Type': 'STRING'},
                            {'Name': 'product/messageDeliveryOrder',
                                'Type': 'STRING'},
                            {'Name': 'product/minVolumeSize',
                                'Type': 'STRING'},
                            {'Name': 'product/networkPerformance',
                                'Type': 'STRING'},
                            {'Name': 'product/normalizationSizeFactor',
                                'Type': 'STRING'},
                            {'Name': 'product/operatingSystem',
                                'Type': 'STRING'},
                            {'Name': 'product/operation',
                                'Type': 'STRING'},
                            {'Name': 'product/physicalProcessor',
                                'Type': 'STRING'},
                            {'Name': 'product/platovolumetype',
                                'Type': 'STRING'},
                            {'Name': 'product/preInstalledSw',
                                'Type': 'STRING'},
                            {'Name': 'product/processorArchitecture',
                                'Type': 'STRING'},
                            {'Name': 'product/processorFeatures',
                                'Type': 'STRING'},
                            {'Name': 'product/productFamily',
                                'Type': 'STRING'},
                            {'Name': 'product/queueType',
                                'Type': 'STRING'},
                            {'Name': 'product/region',
                                'Type': 'STRING'},
                            {'Name': 'product/regionCode',
                                'Type': 'STRING'},
                            {'Name': 'product/requestType',
                                'Type': 'STRING'},
                            {'Name': 'product/servicecode',
                                'Type': 'STRING'},
                            {'Name': 'product/servicename',
                                'Type': 'STRING'},
                            {'Name': 'product/sku',
                                'Type': 'STRING'},
                            {'Name': 'product/storage',
                                'Type': 'STRING'},
                            {'Name': 'product/storageClass',
                                'Type': 'STRING'},
                            {'Name': 'product/storageMedia',
                                'Type': 'STRING'},
                            {'Name': 'product/storageType',
                                'Type': 'STRING'},
                            {'Name': 'product/subscriptionType',
                                'Type': 'STRING'},
                            {'Name': 'product/tenancy',
                                'Type': 'STRING'},
                            {'Name': 'product/toLocation',
                                'Type': 'STRING'},
                            {'Name': 'product/toLocationType',
                                'Type': 'STRING'},
                            {'Name': 'product/toRegionCode',
                                'Type': 'STRING'},
                            {'Name': 'product/transferType',
                                'Type': 'STRING'},
                            {'Name': 'product/usagetype',
                                'Type': 'STRING'},
                            {'Name': 'product/vcpu',
                                'Type': 'STRING'},
                            {'Name': 'product/version',
                                'Type': 'STRING'},
                            {'Name': 'product/volumeApiName',
                                'Type': 'STRING'},
                            {'Name': 'product/volumeType',
                                'Type': 'STRING'},
                            {'Name': 'product/vpcnetworkingsupport',
                                'Type': 'STRING'},
                            {'Name': 'product/withActiveUsers',
                                'Type': 'STRING'},
                            {'Name': 'pricing/RateCode',
                                'Type': 'STRING'},
                            {'Name': 'pricing/RateId',
                                'Type': 'STRING'},
                            {'Name': 'pricing/currency',
                                'Type': 'STRING'},
                            {'Name': 'pricing/publicOnDemandCost',
                                'Type': 'STRING'},
                            {'Name': 'pricing/publicOnDemandRate',
                                'Type': 'STRING'},
                            {'Name': 'pricing/term',
                                'Type': 'STRING'},
                            {'Name': 'pricing/unit',
                                'Type': 'STRING'},
                            {'Name': 'reservation/AmortizedUpfrontCostForUsage',
                                'Type': 'STRING'},
                            {'Name': 'reservation/AmortizedUpfrontFeeForBillingPeriod',
                                'Type': 'STRING'},
                            {'Name': 'reservation/EffectiveCost',
                                'Type': 'STRING'},
                            {'Name': 'reservation/EndTime',
                                'Type': 'STRING'},
                            {'Name': 'reservation/ModificationStatus',
                                'Type': 'STRING'},
                            {'Name': 'reservation/NormalizedUnitsPerReservation',
                                'Type': 'STRING'},
                            {'Name': 'reservation/NumberOfReservations',
                                'Type': 'STRING'},
                            {'Name': 'reservation/RecurringFeeForUsage',
                                'Type': 'STRING'},
                            {'Name': 'reservation/StartTime',
                                'Type': 'STRING'},
                            {'Name': 'reservation/SubscriptionId',
                                'Type': 'STRING'},
                            {'Name': 'reservation/TotalReservedNormalizedUnits',
                                'Type': 'STRING'},
                            {'Name': 'reservation/TotalReservedUnits',
                                'Type': 'STRING'},
                            {'Name': 'reservation/UnitsPerReservation',
                                'Type': 'STRING'},
                            {'Name': 'reservation/UnusedAmortizedUpfrontFeeForBillingPeriod',
                                'Type': 'STRING'},
                            {'Name': 'reservation/UnusedNormalizedUnitQuantity',
                                'Type': 'STRING'},
                            {'Name': 'reservation/UnusedQuantity',
                                'Type': 'STRING'},
                            {'Name': 'reservation/UnusedRecurringFee',
                                'Type': 'STRING'},
                            {'Name': 'reservation/UpfrontValue',
                                'Type': 'STRING'},
                            {'Name': 'savingsPlan/TotalCommitmentToDate',
                                'Type': 'STRING'},
                            {'Name': 'savingsPlan/SavingsPlanARN',
                                'Type': 'STRING'},
                            {'Name': 'savingsPlan/SavingsPlanRate',
                                'Type': 'STRING'},
                            {'Name': 'savingsPlan/UsedCommitment',
                                'Type': 'STRING'},
                            {'Name': 'savingsPlan/SavingsPlanEffectiveCost',
                                'Type': 'STRING'},
                            {'Name': 'savingsPlan/AmortizedUpfrontCommitmentForBillingPeriod',
                                'Type': 'STRING'},
                            {'Name': 'savingsPlan/RecurringCommitmentForBillingPeriod',
                                'Type': 'STRING'},
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
        print("Update cost dataset complete")

    def create_cost_dataset(self):

        try:
            self.create_new_cost_dataset()
            print("Created new cost dataset complete")
        except:
            self.delete_dataset(
                'unique-id-for-new-cost-dataset'+self.account_id)
            print("Wait 5 seconds for the dataset to delete ... ")
            time.sleep(5)
            self.create_new_cost_dataset()

    def update_cost_dataset(self):

        response = self.client.update_data_set(
            AwsAccountId=self.account_id,
            DataSetId='unique-id-for-new-cost-dataset'+self.account_id,
            Name='cost_dataset'+self.account_id,
            PhysicalTableMap={
                'string': {
                    'S3Source': {
                        'DataSourceArn': 'arn:aws:quicksight:us-east-1:'+self.account_id+':datasource/'+'unique-cost-data-source-id-'+self.account_id,
                        'UploadSettings': {
                            'Format': 'CSV',
                            'StartFromRow': 1,
                            'ContainsHeader': True,
                            'TextQualifier': 'DOUBLE_QUOTE',
                            'Delimiter': ','
                        },
                        'InputColumns': [
                            {'Name': 'identity/LineItemId',
                             'Type': 'STRING'},
                            {'Name': 'identity/TimeInterval',
                                'Type': 'STRING'},
                            {'Name': 'bill/InvoiceId',
                                'Type': 'STRING'},
                            {'Name': 'bill/InvoicingEntity',
                                'Type': 'STRING'},
                            {'Name': 'bill/BillingEntity',
                                'Type': 'STRING'},
                            {'Name': 'bill/BillType',
                                'Type': 'STRING'},
                            {'Name': 'bill/PayerAccountId',
                                'Type': 'STRING'},
                            {'Name': 'bill/BillingPeriodStartDate',
                                'Type': 'STRING'},
                            {'Name': 'bill/BillingPeriodEndDate',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/UsageAccountId',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/LineItemType',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/UsageStartDate',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/UsageEndDate',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/ProductCode',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/UsageType',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/Operation',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/AvailabilityZone',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/ResourceId',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/UsageAmount',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/NormalizationFactor',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/NormalizedUsageAmount',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/CurrencyCode',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/UnblendedRate',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/UnblendedCost',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/BlendedRate',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/BlendedCost',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/LineItemDescription',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/TaxType',
                                'Type': 'STRING'},
                            {'Name': 'lineItem/LegalEntity',
                                'Type': 'STRING'},
                            {'Name': 'product/ProductName',
                                'Type': 'STRING'},
                            {'Name': 'product/availability',
                                'Type': 'STRING'},
                            {'Name': 'product/availabilityZone',
                                'Type': 'STRING'},
                            {'Name': 'product/backupservice',
                                'Type': 'STRING'},
                            {'Name': 'product/capacitystatus',
                                'Type': 'STRING'},
                            {'Name': 'product/classicnetworkingsupport',
                                'Type': 'STRING'},
                            {'Name': 'product/clockSpeed',
                                'Type': 'STRING'},
                            {'Name': 'product/currentGeneration',
                                'Type': 'STRING'},
                            {'Name': 'product/databaseEngine',
                                'Type': 'STRING'},
                            {'Name': 'product/datatransferout',
                                'Type': 'STRING'},
                            {'Name': 'product/dedicatedEbsThroughput',
                                'Type': 'STRING'},
                            {'Name': 'product/deploymentOption',
                                'Type': 'STRING'},
                            {'Name': 'product/description',
                                'Type': 'STRING'},
                            {'Name': 'product/durability',
                                'Type': 'STRING'},
                            {'Name': 'product/ecu',
                                'Type': 'STRING'},
                            {'Name': 'product/edition',
                                'Type': 'STRING'},
                            {'Name': 'product/engineCode',
                                'Type': 'STRING'},
                            {'Name': 'product/enhancedNetworkingSupported',
                                'Type': 'STRING'},
                            {'Name': 'product/eventType',
                                'Type': 'STRING'},
                            {'Name': 'product/freeQueryTypes',
                                'Type': 'STRING'},
                            {'Name': 'product/fromLocation',
                                'Type': 'STRING'},
                            {'Name': 'product/fromLocationType',
                                'Type': 'STRING'},
                            {'Name': 'product/fromRegionCode',
                                'Type': 'STRING'},
                            {'Name': 'product/group',
                                'Type': 'STRING'},
                            {'Name': 'product/groupDescription',
                                'Type': 'STRING'},
                            {'Name': 'product/instanceFamily',
                                'Type': 'STRING'},
                            {'Name': 'product/instanceType',
                                'Type': 'STRING'},
                            {'Name': 'product/instanceTypeFamily',
                                'Type': 'STRING'},
                            {'Name': 'product/intelAvx2Available',
                                'Type': 'STRING'},
                            {'Name': 'product/intelAvxAvailable',
                                'Type': 'STRING'},
                            {'Name': 'product/intelTurboAvailable',
                                'Type': 'STRING'},
                            {'Name': 'product/licenseModel',
                                'Type': 'STRING'},
                            {'Name': 'product/location',
                                'Type': 'STRING'},
                            {'Name': 'product/locationType',
                                'Type': 'STRING'},
                            {'Name': 'product/logsDestination',
                                'Type': 'STRING'},
                            {'Name': 'product/marketoption',
                                'Type': 'STRING'},
                            {'Name': 'product/maxIopsBurstPerformance',
                                'Type': 'STRING'},
                            {'Name': 'product/maxIopsvolume',
                                'Type': 'STRING'},
                            {'Name': 'product/maxThroughputvolume',
                                'Type': 'STRING'},
                            {'Name': 'product/maxVolumeSize',
                                'Type': 'STRING'},
                            {'Name': 'product/memory',
                                'Type': 'STRING'},
                            {'Name': 'product/messageDeliveryFrequency',
                                'Type': 'STRING'},
                            {'Name': 'product/messageDeliveryOrder',
                                'Type': 'STRING'},
                            {'Name': 'product/minVolumeSize',
                                'Type': 'STRING'},
                            {'Name': 'product/networkPerformance',
                                'Type': 'STRING'},
                            {'Name': 'product/normalizationSizeFactor',
                                'Type': 'STRING'},
                            {'Name': 'product/operatingSystem',
                                'Type': 'STRING'},
                            {'Name': 'product/operation',
                                'Type': 'STRING'},
                            {'Name': 'product/physicalProcessor',
                                'Type': 'STRING'},
                            {'Name': 'product/platovolumetype',
                                'Type': 'STRING'},
                            {'Name': 'product/preInstalledSw',
                                'Type': 'STRING'},
                            {'Name': 'product/processorArchitecture',
                                'Type': 'STRING'},
                            {'Name': 'product/processorFeatures',
                                'Type': 'STRING'},
                            {'Name': 'product/productFamily',
                                'Type': 'STRING'},
                            {'Name': 'product/queueType',
                                'Type': 'STRING'},
                            {'Name': 'product/region',
                                'Type': 'STRING'},
                            {'Name': 'product/regionCode',
                                'Type': 'STRING'},
                            {'Name': 'product/requestType',
                                'Type': 'STRING'},
                            {'Name': 'product/servicecode',
                                'Type': 'STRING'},
                            {'Name': 'product/servicename',
                                'Type': 'STRING'},
                            {'Name': 'product/sku',
                                'Type': 'STRING'},
                            {'Name': 'product/storage',
                                'Type': 'STRING'},
                            {'Name': 'product/storageClass',
                                'Type': 'STRING'},
                            {'Name': 'product/storageMedia',
                                'Type': 'STRING'},
                            {'Name': 'product/storageType',
                                'Type': 'STRING'},
                            {'Name': 'product/subscriptionType',
                                'Type': 'STRING'},
                            {'Name': 'product/tenancy',
                                'Type': 'STRING'},
                            {'Name': 'product/toLocation',
                                'Type': 'STRING'},
                            {'Name': 'product/toLocationType',
                                'Type': 'STRING'},
                            {'Name': 'product/toRegionCode',
                                'Type': 'STRING'},
                            {'Name': 'product/transferType',
                                'Type': 'STRING'},
                            {'Name': 'product/usagetype',
                                'Type': 'STRING'},
                            {'Name': 'product/vcpu',
                                'Type': 'STRING'},
                            {'Name': 'product/version',
                                'Type': 'STRING'},
                            {'Name': 'product/volumeApiName',
                                'Type': 'STRING'},
                            {'Name': 'product/volumeType',
                                'Type': 'STRING'},
                            {'Name': 'product/vpcnetworkingsupport',
                                'Type': 'STRING'},
                            {'Name': 'product/withActiveUsers',
                                'Type': 'STRING'},
                            {'Name': 'pricing/RateCode',
                                'Type': 'STRING'},
                            {'Name': 'pricing/RateId',
                                'Type': 'STRING'},
                            {'Name': 'pricing/currency',
                                'Type': 'STRING'},
                            {'Name': 'pricing/publicOnDemandCost',
                                'Type': 'STRING'},
                            {'Name': 'pricing/publicOnDemandRate',
                                'Type': 'STRING'},
                            {'Name': 'pricing/term',
                                'Type': 'STRING'},
                            {'Name': 'pricing/unit',
                                'Type': 'STRING'},
                            {'Name': 'reservation/AmortizedUpfrontCostForUsage',
                                'Type': 'STRING'},
                            {'Name': 'reservation/AmortizedUpfrontFeeForBillingPeriod',
                                'Type': 'STRING'},
                            {'Name': 'reservation/EffectiveCost',
                                'Type': 'STRING'},
                            {'Name': 'reservation/EndTime',
                                'Type': 'STRING'},
                            {'Name': 'reservation/ModificationStatus',
                                'Type': 'STRING'},
                            {'Name': 'reservation/NormalizedUnitsPerReservation',
                                'Type': 'STRING'},
                            {'Name': 'reservation/NumberOfReservations',
                                'Type': 'STRING'},
                            {'Name': 'reservation/RecurringFeeForUsage',
                                'Type': 'STRING'},
                            {'Name': 'reservation/StartTime',
                                'Type': 'STRING'},
                            {'Name': 'reservation/SubscriptionId',
                                'Type': 'STRING'},
                            {'Name': 'reservation/TotalReservedNormalizedUnits',
                                'Type': 'STRING'},
                            {'Name': 'reservation/TotalReservedUnits',
                                'Type': 'STRING'},
                            {'Name': 'reservation/UnitsPerReservation',
                                'Type': 'STRING'},
                            {'Name': 'reservation/UnusedAmortizedUpfrontFeeForBillingPeriod',
                                'Type': 'STRING'},
                            {'Name': 'reservation/UnusedNormalizedUnitQuantity',
                                'Type': 'STRING'},
                            {'Name': 'reservation/UnusedQuantity',
                                'Type': 'STRING'},
                            {'Name': 'reservation/UnusedRecurringFee',
                                'Type': 'STRING'},
                            {'Name': 'reservation/UpfrontValue',
                                'Type': 'STRING'},
                            {'Name': 'savingsPlan/TotalCommitmentToDate',
                                'Type': 'STRING'},
                            {'Name': 'savingsPlan/SavingsPlanARN',
                                'Type': 'STRING'},
                            {'Name': 'savingsPlan/SavingsPlanRate',
                                'Type': 'STRING'},
                            {'Name': 'savingsPlan/UsedCommitment',
                                'Type': 'STRING'},
                            {'Name': 'savingsPlan/SavingsPlanEffectiveCost',
                                'Type': 'STRING'},
                            {'Name': 'savingsPlan/AmortizedUpfrontCommitmentForBillingPeriod',
                                'Type': 'STRING'},
                            {'Name': 'savingsPlan/RecurringCommitmentForBillingPeriod',
                                'Type': 'STRING'},
                        ]
                    }
                }
            },
            ImportMode='SPICE',
        )
        print("Updated cost dataset")


# client = boto3.client('quicksight')

# response = client.list_data_sets(
#     AwsAccountId='774446988871'
# )

# print(response)
