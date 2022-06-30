var AWS = require('aws-sdk');
const { Console } = require('console');

// Set the Region 
AWS.config.update({ region: 'us-east-1' });


var quicksight = new AWS.QuickSight({ apiVersion: '2018-04-01' });

var params = {
    AwsAccountId: 'STRING_VALUE', /* required */
    DataSetId: 'STRING_VALUE', /* required */
    ImportMode: SPICE | DIRECT_QUERY, /* required */
    Name: 'STRING_VALUE', /* required */
    PhysicalTableMap: { /* required */
        '<PhysicalTableId>': {
            CustomSql: {
                DataSourceArn: 'STRING_VALUE', /* required */
                Name: 'STRING_VALUE', /* required */
                SqlQuery: 'STRING_VALUE', /* required */
                Columns: [
                    {
                        Name: 'STRING_VALUE', /* required */
                        Type: STRING | INTEGER | DECIMAL | DATETIME | BIT | BOOLEAN | JSON /* required */
                    },
                    /* more items */
                ]
            },
            RelationalTable: {
                DataSourceArn: 'STRING_VALUE', /* required */
                InputColumns: [ /* required */
                    {
                        Name: 'STRING_VALUE', /* required */
                        Type: STRING | INTEGER | DECIMAL | DATETIME | BIT | BOOLEAN | JSON /* required */
                    },
                    /* more items */
                ],
                Name: 'STRING_VALUE', /* required */
                Catalog: 'STRING_VALUE',
                Schema: 'STRING_VALUE'
            },
            S3Source: {
                DataSourceArn: 'STRING_VALUE', /* required */
                InputColumns: [ /* required */
                    {
                        Name: 'STRING_VALUE', /* required */
                        Type: STRING | INTEGER | DECIMAL | DATETIME | BIT | BOOLEAN | JSON /* required */
                    },
                    /* more items */
                ],
                UploadSettings: {
                    ContainsHeader: true || false,
                    Delimiter: 'STRING_VALUE',
                    Format: CSV | TSV | CLF | ELF | XLSX | JSON,
                    StartFromRow: 'NUMBER_VALUE',
                    TextQualifier: DOUBLE_QUOTE | SINGLE_QUOTE
                }
            }
        },
        /* '<PhysicalTableId>': ... */
    },
    ColumnGroups: [
        {
            GeoSpatialColumnGroup: {
                Columns: [ /* required */
                    'STRING_VALUE',
                    /* more items */
                ],
                CountryCode: US, /* required */
                Name: 'STRING_VALUE' /* required */
            }
        },
        /* more items */
    ],
    ColumnLevelPermissionRules: [
        {
            ColumnNames: [
                'STRING_VALUE',
                /* more items */
            ],
            Principals: [
                'STRING_VALUE',
                /* more items */
            ]
        },
        /* more items */
    ],
    DataSetUsageConfiguration: {
        DisableUseAsDirectQuerySource: true || false,
        DisableUseAsImportedSource: true || false
    },
    FieldFolders: {
        '<FieldFolderPath>': {
            columns: [
                'STRING_VALUE',
                /* more items */
            ],
            description: 'STRING_VALUE'
        },
        /* '<FieldFolderPath>': ... */
    },
    LogicalTableMap: {
        '<LogicalTableId>': {
            Alias: 'STRING_VALUE', /* required */
            Source: { /* required */
                DataSetArn: 'STRING_VALUE',
                JoinInstruction: {
                    LeftOperand: 'STRING_VALUE', /* required */
                    OnClause: 'STRING_VALUE', /* required */
                    RightOperand: 'STRING_VALUE', /* required */
                    Type: INNER | OUTER | LEFT | RIGHT, /* required */
                    LeftJoinKeyProperties: {
                        UniqueKey: true || false
                    },
                    RightJoinKeyProperties: {
                        UniqueKey: true || false
                    }
                },
                PhysicalTableId: 'STRING_VALUE'
            },
            DataTransforms: [
                {
                    CastColumnTypeOperation: {
                        ColumnName: 'STRING_VALUE', /* required */
                        NewColumnType: STRING | INTEGER | DECIMAL | DATETIME, /* required */
                        Format: 'STRING_VALUE'
                    },
                    CreateColumnsOperation: {
                        Columns: [ /* required */
                            {
                                ColumnId: 'STRING_VALUE', /* required */
                                ColumnName: 'STRING_VALUE', /* required */
                                Expression: 'STRING_VALUE' /* required */
                            },
                            /* more items */
                        ]
                    },
                    FilterOperation: {
                        ConditionExpression: 'STRING_VALUE' /* required */
                    },
                    ProjectOperation: {
                        ProjectedColumns: [ /* required */
                            'STRING_VALUE',
                            /* more items */
                        ]
                    },
                    RenameColumnOperation: {
                        ColumnName: 'STRING_VALUE', /* required */
                        NewColumnName: 'STRING_VALUE' /* required */
                    },
                    TagColumnOperation: {
                        ColumnName: 'STRING_VALUE', /* required */
                        Tags: [ /* required */
                            {
                                ColumnDescription: {
                                    Text: 'STRING_VALUE'
                                },
                                ColumnGeographicRole: COUNTRY | STATE | COUNTY | CITY | POSTCODE | LONGITUDE | LATITUDE
                            },
                            /* more items */
                        ]
                    },
                    UntagColumnOperation: {
                        ColumnName: 'STRING_VALUE', /* required */
                        TagNames: [ /* required */
                            COLUMN_GEOGRAPHIC_ROLE | COLUMN_DESCRIPTION,
                            /* more items */
                        ]
                    }
                },
                /* more items */
            ]
        },
        /* '<LogicalTableId>': ... */
    },
    Permissions: [
        {
            Actions: [ /* required */
                'STRING_VALUE',
                /* more items */
            ],
            Principal: 'STRING_VALUE' /* required */
        },
        /* more items */
    ],
    RowLevelPermissionDataSet: {
        Arn: 'STRING_VALUE', /* required */
        PermissionPolicy: GRANT_ACCESS | DENY_ACCESS, /* required */
        FormatVersion: VERSION_1 | VERSION_2,
        Namespace: 'STRING_VALUE',
        Status: ENABLED | DISABLED
    },
    RowLevelPermissionTagConfiguration: {
        TagRules: [ /* required */
            {
                ColumnName: 'STRING_VALUE', /* required */
                TagKey: 'STRING_VALUE', /* required */
                MatchAllValue: 'STRING_VALUE',
                TagMultiValueDelimiter: 'STRING_VALUE'
            },
            /* more items */
        ],
        Status: ENABLED | DISABLED
    },
    Tags: [
        {
            Key: 'STRING_VALUE', /* required */
            Value: 'STRING_VALUE' /* required */
        },
        /* more items */
    ]
};
quicksight.createDataSet(params, function (err, data) {
    if (err) console.log(err, err.stack); // an error occurred
    else console.log(data);           // successful response
});
