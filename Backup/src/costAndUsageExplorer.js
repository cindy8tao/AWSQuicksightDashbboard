var AWS = require('aws-sdk');
AWS.config.update({ region: 'us-east-1' });





var costexplorer = new AWS.CostExplorer({ apiVersion: '2017-10-25' });

var params = {
    Metrics: [
        'UNBLENDED_COST',
    ],
    TimePeriod: {
        End: '2022-06-30', /* Fill the end date */
        Start: '2022-05-30' /* Fill the start date  */
    },
    Granularity: 'DAILY', /* MONTHLY or HOURLY */
    GroupBy: [
        {
            Key: 'LINKED_ACCOUNT',
            Type: 'DIMENSION'
        },
    ]
};
costexplorer.getCostAndUsage(params, function (err, data) {
    if (err) console.log(err, err.stack); // an error occurred
    else console.log(data);           // successful response
});