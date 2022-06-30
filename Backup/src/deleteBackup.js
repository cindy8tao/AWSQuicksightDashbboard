var AWS = require('aws-sdk');
const { Console } = require('console');

// Set the Region 
AWS.config.update({ region: 'us-east-1' });

var backup = new AWS.Backup({ apiVersion: '2018-11-15' });

let BACKUP_PLAN_ID = 'ee5ba818-8343-4523-941d-0eb5d2ad8427'

var params = {
    BackupPlanId: BACKUP_PLAN_ID
};


backup.deleteBackupPlan(params, function (err, data) {
    if (err) {
        console.log(err, err.stack)
    }
    else {
        console.log(data)
    }
})
