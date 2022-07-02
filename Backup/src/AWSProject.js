var AWS = require('aws-sdk');
const { Console } = require('console');

// Set the Region 
AWS.config.update({ region: 'us-east-1' });

var backup = new AWS.Backup({ apiVersion: '2018-11-15' });
var s3 = new AWS.S3({ apiVersion: '2006-03-01' });

// List Backup Plans
backup.listBackupPlans(function (err, data) {
    if (err) {
        console.log("Error", err);
    }
    else {
        console.log("Success", data);
    }
});

// // Create Backup Plan
// let BACKUP_PLAN_NAME = "12hrs";
// let RULE_NAME = "RunEvery12Hrs";
// let COMPLETION_WINDOW_MINUTES = 120; // Completion Window Minutes (must be 60 > Start Window)
// let START_WINDOW_MINUTES = 60; // Start Window Minutes (minimum value = 60)
// let SCHEDULE_EXPRESSION = "cron(0 12 * * ? *)"; // Schedule Expression (example: cron(0 12 * * ? *))
// let TARGET_BACKUP_VAULT_NAME = "Default" // Target Backup Vault Name (example: "Default")

// var params = {
//     BackupPlan: {
//         BackupPlanName: BACKUP_PLAN_NAME,
//         Rules: [
//             {
//                 RuleName: RULE_NAME,
//                 TargetBackupVaultName: TARGET_BACKUP_VAULT_NAME,
//                 CompletionWindowMinutes: COMPLETION_WINDOW_MINUTES,
//                 ScheduleExpression: SCHEDULE_EXPRESSION,
//                 StartWindowMinutes: START_WINDOW_MINUTES,
//             }
//         ]
//     }
// };

// backup.createBackupPlan(params, function (err, data) {
//     if (err) {
//         console.log(err, err.stack);
//     }
//     else {
//         console.log(data)
//     }
// })

// // Create a S3 bucket
// let BUCKET_NAME = 'backupreportfromnodejs' // Create a bucket with unique name

// var params = {
//     Bucket: BUCKET_NAME
// };
// s3.createBucket(params, function (err, data) {
//     if (err) {
//         console.log(err, err.stack);
//     }
//     else {
//         console.log(data);
//     }
// });


// // Create Backup Report

// let FORMAT = 'JSON' // 'JSON' OR 'CSV'
// let REPORT_PLAN_NAME = 'VSBackupReport'
// let REPORT_TEMPLATE = 'BACKUP_JOB_REPORT' // RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT

// var params = {
//     ReportDeliveryChannel: {
//         S3BucketName: BUCKET_NAME,
//         Formats: [
//             FORMAT,
//         ]
//     },
//     ReportPlanName: REPORT_PLAN_NAME,
//     ReportSetting: {
//         ReportTemplate: REPORT_TEMPLATE,
//         // FrameworkArns: [
//         //     'STRING_VALUE',
//         // ],
//         // NumberOfFrameworks: 'NUMBER_VALUE'
//     },
//     // IdempotencyToken: 'STRING_VALUE',
//     // ReportPlanDescription: 'STRING_VALUE',
//     // ReportPlanTags: {
//     //     '<string>': 'STRING_VALUE',
//     // }
// };
// backup.createReportPlan(params, function (err, data) {
//     if (err) {
//         console.log(err, err.stack);
//     }
//     else {
//         console.log(data);
//     }
// });