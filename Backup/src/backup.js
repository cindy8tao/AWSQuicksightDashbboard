var AWS = require('aws-sdk');

// Set the Region 
AWS.config.update({region: 'us-east-1'});

var backup = new AWS.Backup({apiVersion: '2018-11-15'});

// List Backup Plans
backup.listBackupPlans(function(err, data) {
    if(err) 
    {
        console.log("Error", err);
    }
    else
    {
        console.log("Success", data);
    }
});


// Create Backup Plan
var backupPlanName = "12HrsPlan";
var ruleName = "RunEvery12Hrs";
var completionWindowMinutes = 120;
var startWindowMinutes = 60;
var scheduleExpression = "cron(0 12 * * ? *)";
var targetBackupVaultName = "Default"


var params = {
  BackupPlan: { /* required */
    BackupPlanName: backupPlanName, /* required */
    Rules: [ /* required */
      {
        RuleName: ruleName, /* required */
        TargetBackupVaultName: targetBackupVaultName, /* required */
        CompletionWindowMinutes: completionWindowMinutes,
          /* more items */
        ScheduleExpression: scheduleExpression,
        StartWindowMinutes: startWindowMinutes
      }
    ]
  }
};

backup.createBackupPlan(params, function(err, data) {
  if (err) console.log(err, err.stack); // an error occurred
  else     console.log(data);           // successful response
});