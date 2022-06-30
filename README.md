# AWS Quicksight Dashbboard

Goal of Project:

1). Create 2-10 EC2 instances, 2-10 RDS databases and 2-10 S3 buckets. 

2). Populate the RDS database and S3 buckets with some content. 

3). Tag each resource with one of three environment tags ("dev", "staging", "prod") and another department tag from ("sales", "marketing", "HR"). 

4). Create backup plans with different backup schedules for each tag, e.g. "dev" backs up once every 6 hours, "staging" every 3 hours, "prod" every hour.

5). Make a Quicksight dashboard that allows a user to categorize backups from different tag groups as well as resource type (e.g. S3, RDS or EC2)


Reference:
https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS.html
