import datetime
from urllib.request import Request
import boto3
import json


class Quicksight:

    def __init__(self):
        pass

    def create_dataset():
        client = boto3.client('quicksight',
                              aws_access_key_id='AKIA3IUFDHZD65DZ2BQX',
                              aws_secret_access_key='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',)
        response = client.create_data_set(
            AwsAccountId='string',
            DataSetId='string',
            Name='string',
            PhysicalTableMap={
                'string': {
                    'RelationalTable': {
                        'DataSourceArn': 'string',
                        'Catalog': 'string',
                        'Schema': 'string',
                        'Name': 'string',
                        'InputColumns': [
                            {
                                'Name': 'string',
                                'Type': 'STRING' | 'INTEGER' | 'DECIMAL' | 'DATETIME' | 'BIT' | 'BOOLEAN' | 'JSON'
                            },
                        ]
                    },
                    'CustomSql': {
                        'DataSourceArn': 'string',
                        'Name': 'string',
                        'SqlQuery': 'string',
                        'Columns': [
                            {
                                'Name': 'string',
                                'Type': 'STRING' | 'INTEGER' | 'DECIMAL' | 'DATETIME' | 'BIT' | 'BOOLEAN' | 'JSON'
                            },
                        ]
                    },
                    'S3Source': {
                        'DataSourceArn': 'string',
                        'UploadSettings': {
                            'Format': 'CSV' | 'TSV' | 'CLF' | 'ELF' | 'XLSX' | 'JSON',
                            'StartFromRow': 123,
                            'ContainsHeader': True | False,
                            'TextQualifier': 'DOUBLE_QUOTE' | 'SINGLE_QUOTE',
                            'Delimiter': 'string'
                        },
                        'InputColumns': [
                            {
                                'Name': 'string',
                                'Type': 'STRING' | 'INTEGER' | 'DECIMAL' | 'DATETIME' | 'BIT' | 'BOOLEAN' | 'JSON'
                            },
                        ]
                    }
                }
            },
            LogicalTableMap={
                'string': {
                    'Alias': 'string',
                    'DataTransforms': [
                        {
                            'ProjectOperation': {
                                'ProjectedColumns': [
                                    'string',
                                ]
                            },
                            'FilterOperation': {
                                'ConditionExpression': 'string'
                            },
                            'CreateColumnsOperation': {
                                'Columns': [
                                    {
                                        'ColumnName': 'string',
                                        'ColumnId': 'string',
                                        'Expression': 'string'
                                    },
                                ]
                            },
                            'RenameColumnOperation': {
                                'ColumnName': 'string',
                                'NewColumnName': 'string'
                            },
                            'CastColumnTypeOperation': {
                                'ColumnName': 'string',
                                'NewColumnType': 'STRING' | 'INTEGER' | 'DECIMAL' | 'DATETIME',
                                'Format': 'string'
                            },
                            'TagColumnOperation': {
                                'ColumnName': 'string',
                                'Tags': [
                                    {
                                        'ColumnGeographicRole': 'COUNTRY' | 'STATE' | 'COUNTY' | 'CITY' | 'POSTCODE' | 'LONGITUDE' | 'LATITUDE',
                                        'ColumnDescription': {
                                            'Text': 'string'
                                        }
                                    },
                                ]
                            },
                            'UntagColumnOperation': {
                                'ColumnName': 'string',
                                'TagNames': [
                                    'COLUMN_GEOGRAPHIC_ROLE' | 'COLUMN_DESCRIPTION',
                                ]
                            }
                        },
                    ],
                    'Source': {
                        'JoinInstruction': {
                            'LeftOperand': 'string',
                            'RightOperand': 'string',
                            'LeftJoinKeyProperties': {
                                'UniqueKey': True | False
                            },
                            'RightJoinKeyProperties': {
                                'UniqueKey': True | False
                            },
                            'Type': 'INNER' | 'OUTER' | 'LEFT' | 'RIGHT',
                            'OnClause': 'string'
                        },
                        'PhysicalTableId': 'string',
                        'DataSetArn': 'string'
                    }
                }
            },
            ImportMode='SPICE' | 'DIRECT_QUERY',
            ColumnGroups=[
                {
                    'GeoSpatialColumnGroup': {
                        'Name': 'string',
                        'CountryCode': 'US',
                        'Columns': [
                            'string',
                        ]
                    }
                },
            ],
            FieldFolders={
                'string': {
                    'description': 'string',
                    'columns': [
                        'string',
                    ]
                }
            },
            Permissions=[
                {
                    'Principal': 'string',
                    'Actions': [
                        'string',
                    ]
                },
            ],
            RowLevelPermissionDataSet={
                'Namespace': 'string',
                'Arn': 'string',
                'PermissionPolicy': 'GRANT_ACCESS' | 'DENY_ACCESS',
                'FormatVersion': 'VERSION_1' | 'VERSION_2',
                'Status': 'ENABLED' | 'DISABLED'
            },
            RowLevelPermissionTagConfiguration={
                'Status': 'ENABLED' | 'DISABLED',
                'TagRules': [
                    {
                        'TagKey': 'string',
                        'ColumnName': 'string',
                        'TagMultiValueDelimiter': 'string',
                        'MatchAllValue': 'string'
                    },
                ]
            },
            ColumnLevelPermissionRules=[
                {
                    'Principals': [
                        'string',
                    ],
                    'ColumnNames': [
                        'string',
                    ]
                },
            ],
            Tags=[
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ],
            DataSetUsageConfiguration={
                'DisableUseAsDirectQuerySource': True | False,
                'DisableUseAsImportedSource': True | False
            }
        )
