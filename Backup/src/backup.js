var AWS = require('aws-sdk');

// Set the Region 
AWS.config.update({region: 'us-east-1'});

var backup = new AWS.Backup({apiVersion: '2018-11-15'});

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
