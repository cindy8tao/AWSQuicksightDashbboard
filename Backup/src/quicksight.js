// var AWS = require('aws-sdk');
// const { Console } = require('console');

// // Set the Region 
// AWS.config.update({ region: 'us-east-1' });


// var quicksight = new AWS.QuickSight({ apiVersion: '2018-04-01' });

// var params = {
//     AwsAccountId: 'STRING_VALUE', 
//     DataSetId: 'STRING_VALUE', 
//     ImportMode: SPICE | DIRECT_QUERY, 
//     Name: 'STRING_VALUE', 
//     PhysicalTableMap: { 
//         '<PhysicalTableId>': {
//             CustomSql: {
//                 DataSourceArn: 'STRING_VALUE', 
//                 Name: 'STRING_VALUE', 
//                 SqlQuery: 'STRING_VALUE', 
//                 Columns: [
//                     {
//                         Name: 'STRING_VALUE', 
//                         Type: STRING | INTEGER | DECIMAL | DATETIME | BIT | BOOLEAN | JSON 
//                     },
//                     /* more items */
//                 ]
//             },
//             RelationalTable: {
//                 DataSourceArn: 'STRING_VALUE', 
//                 InputColumns: [ 
//                     {
//                         Name: 'STRING_VALUE', 
//                         Type: STRING | INTEGER | DECIMAL | DATETIME | BIT | BOOLEAN | JSON 
//                     },
//                     /* more items */
//                 ],
//                 Name: 'STRING_VALUE', 
//                 Catalog: 'STRING_VALUE',
//                 Schema: 'STRING_VALUE'
//             },
//             S3Source: {
//                 DataSourceArn: 'STRING_VALUE', 
//                 InputColumns: [ 
//                     {
//                         Name: 'STRING_VALUE', 
//                         Type: STRING | INTEGER | DECIMAL | DATETIME | BIT | BOOLEAN | JSON 
//                     },
//                     /* more items */
//                 ],
//                 UploadSettings: {
//                     ContainsHeader: true || false,
//                     Delimiter: 'STRING_VALUE',
//                     Format: CSV | TSV | CLF | ELF | XLSX | JSON,
//                     StartFromRow: 'NUMBER_VALUE',
//                     TextQualifier: DOUBLE_QUOTE | SINGLE_QUOTE
//                 }
//             }
//         },
//         /* '<PhysicalTableId>': ... */
//     },
//     ColumnGroups: [
//         {
//             GeoSpatialColumnGroup: {
//                 Columns: [ 
//                     'STRING_VALUE',
//                     /* more items */
//                 ],
//                 CountryCode: US, 
//                 Name: 'STRING_VALUE' 
//             }
//         },
//         /* more items */
//     ],
//     ColumnLevelPermissionRules: [
//         {
//             ColumnNames: [
//                 'STRING_VALUE',
//                 /* more items */
//             ],
//             Principals: [
//                 'STRING_VALUE',
//                 /* more items */
//             ]
//         },
//         /* more items */
//     ],
//     DataSetUsageConfiguration: {
//         DisableUseAsDirectQuerySource: true || false,
//         DisableUseAsImportedSource: true || false
//     },
//     FieldFolders: {
//         '<FieldFolderPath>': {
//             columns: [
//                 'STRING_VALUE',
//                 /* more items */
//             ],
//             description: 'STRING_VALUE'
//         },
//         /* '<FieldFolderPath>': ... */
//     },
//     LogicalTableMap: {
//         '<LogicalTableId>': {
//             Alias: 'STRING_VALUE', 
//             Source: { 
//                 DataSetArn: 'STRING_VALUE',
//                 JoinInstruction: {
//                     LeftOperand: 'STRING_VALUE', 
//                     OnClause: 'STRING_VALUE', 
//                     RightOperand: 'STRING_VALUE', 
//                     Type: INNER | OUTER | LEFT | RIGHT, 
//                     LeftJoinKeyProperties: {
//                         UniqueKey: true || false
//                     },
//                     RightJoinKeyProperties: {
//                         UniqueKey: true || false
//                     }
//                 },
//                 PhysicalTableId: 'STRING_VALUE'
//             },
//             DataTransforms: [
//                 {
//                     CastColumnTypeOperation: {
//                         ColumnName: 'STRING_VALUE', 
//                         NewColumnType: STRING | INTEGER | DECIMAL | DATETIME, 
//                         Format: 'STRING_VALUE'
//                     },
//                     CreateColumnsOperation: {
//                         Columns: [ 
//                             {
//                                 ColumnId: 'STRING_VALUE', 
//                                 ColumnName: 'STRING_VALUE', 
//                                 Expression: 'STRING_VALUE' 
//                             },
//                             /* more items */
//                         ]
//                     },
//                     FilterOperation: {
//                         ConditionExpression: 'STRING_VALUE' 
//                     },
//                     ProjectOperation: {
//                         ProjectedColumns: [ 
//                             'STRING_VALUE',
//                             /* more items */
//                         ]
//                     },
//                     RenameColumnOperation: {
//                         ColumnName: 'STRING_VALUE', 
//                         NewColumnName: 'STRING_VALUE' 
//                     },
//                     TagColumnOperation: {
//                         ColumnName: 'STRING_VALUE', 
//                         Tags: [ 
//                             {
//                                 ColumnDescription: {
//                                     Text: 'STRING_VALUE'
//                                 },
//                                 ColumnGeographicRole: COUNTRY | STATE | COUNTY | CITY | POSTCODE | LONGITUDE | LATITUDE
//                             },
//                             /* more items */
//                         ]
//                     },
//                     UntagColumnOperation: {
//                         ColumnName: 'STRING_VALUE', 
//                         TagNames: [ 
//                             COLUMN_GEOGRAPHIC_ROLE | COLUMN_DESCRIPTION,
//                             /* more items */
//                         ]
//                     }
//                 },
//                 /* more items */
//             ]
//         },
//         /* '<LogicalTableId>': ... */
//     },
//     Permissions: [
//         {
//             Actions: [ 
//                 'STRING_VALUE',
//                 /* more items */
//             ],
//             Principal: 'STRING_VALUE' 
//         },
//         /* more items */
//     ],
//     RowLevelPermissionDataSet: {
//         Arn: 'STRING_VALUE', 
//         PermissionPolicy: GRANT_ACCESS | DENY_ACCESS, 
//         FormatVersion: VERSION_1 | VERSION_2,
//         Namespace: 'STRING_VALUE',
//         Status: ENABLED | DISABLED
//     },
//     RowLevelPermissionTagConfiguration: {
//         TagRules: [ 
//             {
//                 ColumnName: 'STRING_VALUE', 
//                 TagKey: 'STRING_VALUE', 
//                 MatchAllValue: 'STRING_VALUE',
//                 TagMultiValueDelimiter: 'STRING_VALUE'
//             },
//             /* more items */
//         ],
//         Status: ENABLED | DISABLED
//     },
//     Tags: [
//         {
//             Key: 'STRING_VALUE', 
//             Value: 'STRING_VALUE' 
//         },
//         /* more items */
//     ]
// };
// quicksight.createDataSet(params, function (err, data) {
//     if (err) console.log(err, err.stack); // an error occurred
//     else console.log(data);           // successful response
// });


var AWS = require('aws-sdk');
const { Console } = require('console');

// Set the Region 
AWS.config.update({ region: 'us-east-1' });


var quicksight = new AWS.QuickSight({ apiVersion: '2018-04-01' });


// var params = {
//     AwsAccountId: '774446988871',
// };
// quicksight.listDataSets(params, function (err, data) {
//     if (err) console.log(err, err.stack);
//     else console.log(data);
// });


let AWS_ACCOUNT_ID = '774446988871'
let DATASET_NAME = 'BackupReport'
let DATA_SOURCE_ARN = 's3://sparcuser1costreport/Sparcuser1Cost/Sparcuser1CostReport/QuickSight/Sparcuser1CostReport-20220601-20220701-QuickSightManifest.json'
let IMPORT_MODE = 'SPICE' // SPICE | DIRECT_QUERY,
let COLUMN_NAME = 'Backup'
let COLUMN_TYPE = 'JSON' // STRING | INTEGER | DECIMAL | DATETIME | BIT | BOOLEAN | JSON

let CONTAINS_HEADER = true // TRUE || FALSE,
let DELIMITER = ''
let FORMAT = 'JSON' // CSV | TSV | CLF | ELF | XLSX | JSON,
let START_FROM_ROW = 0
let TEXT_QUALIFIER = "SINGLE_QUOTE" // DOUBLE_QUOTE | SINGLE_QUOTE


var params = {
    AwsAccountId: AWS_ACCOUNT_ID,
    DataSetId: 'STRING_VALUE',
    ImportMode: IMPORT_MODE,
    Name: DATASET_NAME,
    PhysicalTableMap: {
        '<PhysicalTableId>': {
            S3Source: {
                DataSourceArn: DATA_SOURCE_ARN,
                InputColumns: [
                    {
                        Name: COLUMN_NAME,
                        Type: COLUMN_TYPE
                    },
                ],
                UploadSettings: {
                    ContainsHeader: CONTAINS_HEADER,
                    Delimiter: DELIMITER,
                    Format: FORMAT,
                    StartFromRow: START_FROM_ROW,
                    TextQualifier: TEXT_QUALIFIER
                }
            }
        },
    },
};
quicksight.createDataSet(params, function (err, data) {
    if (err) console.log(err, err.stack); // an error occurred
    else console.log(data);           // successful response
});

