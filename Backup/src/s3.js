var AWS = require('aws-sdk');

// Set the Region 
AWS.config.update({ region: 'us-east-1' });

s3 = new AWS.S3({ apiVersion: '2006-03-01' });

s3.listBuckets(function (err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    console.log("Success", data.Buckets);
  }
});

// var params = {
//   Bucket: "backupobserve-solutionlocalcachebucket-rmcz0uozy0r8"
// };
// s3.deleteBucket(params, function (err, data) {
//   if (err) console.log(err, err.stack);
//   else console.log(data);
// });






