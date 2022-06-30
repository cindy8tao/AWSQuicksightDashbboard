var AWS = require('aws-sdk');
const { Console } = require('console');

// Set the Region 
AWS.config.update({ region: 'us-east-1' });

var backup = new AWS.Backup({ apiVersion: '2018-11-15' });

// List Backup Plans
// backup.listBackupPlans(function(err, data) {
//     if(err) 
//     {
//         console.log("Error", err);
//     }
//     else
//     {
//         console.log("Success", data);
//     }
// });

const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

var backupPlanId;

readline.question('BackupPlanName: ', input1 => {
  readline.question('Rule Name: ', input2 => {
    readline.question('Completion Window Minutes (must be 60 > Start Window): ', input3 => {
      readline.question('Start Window Minutes (minimum value = 60): ', input4 => {
        readline.question('Schedule Expression (example: cron(0 12 * * ? *)): ', input5 => {
          readline.question('Target Backup Vault Name (example: "Default"): ', input6 => {

            var backupPlanName = input1;
            var ruleName = input2;
            var completionWindowMinutes = input3;
            var startWindowMinutes = input4;
            var scheduleExpression = input5;
            var targetBackupVaultName = input6;

            // Create Backup Plan
            // var backupPlanName = "12HrsPlan";
            // var ruleName = "RunEvery12Hrs";
            // var completionWindowMinutes = 120;
            // var startWindowMinutes = 60;
            // var scheduleExpression = "cron(0 12 * * ? *)";
            // var targetBackupVaultName = "Default"

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

            backup.createBackupPlan(params, function (err, data) {
              if (err) {
                console.log(err, err.stack);
              }
              else {
                console.log(data);
                backupPlanId = data.backupPlanId;
              }
            });

            readline.close();
          });
        });
      });
    });
  });
});


// var params = {
//   BackupPlanId: backupPlanId /* required */
// };
// backup.deleteBackupPlan(params, function (err, data) {
//   if (err) console.log(err, err.stack); // an error occurred
//   else console.log(data);           // successful response
// });