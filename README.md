# AWS Quicksight Dashbboard

AWS (Amazon Web Service) currently supports the creation of Backup Reports and Cost & Usage Reports, however, users cannot categorize the backups and costs based on tags. Customers who desired to get daily, aggregated, cross-account, multi-Region AWS1 Backup or Cost reports about different resources with user-defined tags had to manually generate them. In order to tackle this problem, the team developed a set of automation templates and a dashboard to help users collect and analyze daily, aggregated reports based on tags automatically.

The Backups/Cost in Quicksight automation that the team created allows users to extract backup and cost details, categorize them based on tags, and automatically generate the daily backup and cost reports. In addition, the team uses Quicksight to create a backup/cost dashboard at the very end for users to visualize the backup/cost details in order to help users better analyze the report and performance based on tags. 

The objective of this project is to assist users in minimizing the time and effort associated with the creation of daily, automated, and aggregated backup and cost reports based on tags, simplified observability of data protection activities to provide enriched daily data protection reporting to customers, and enable users to dive deeper into the usage patterns and cost trends as well as backup data protection activities.


Goal of Project:

* Create 2-10 EC2 instances, 2-10 RDS databases and 2-10 S3 buckets. 

* Populate the RDS database and S3 buckets with some content. 

* Tag each resource with one of three environment tags ("dev", "staging", "prod") and another department tag from ("sales", "marketing", "HR"). 

* Create backup plans with different backup schedules for each tag, e.g. "dev" backs up once every 6 hours, "staging" every 3 hours, "prod" every hour.

* Make a Quicksight dashboard that allows a user to categorize backups from different tag groups as well as resource type (e.g. S3, RDS or EC2)


Reference:
https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

Demonstration Video:
[![Watch the video](https://img.youtube.com/vi/d-c4Zk0G-mY/0.jpg)](https://youtu.be/d-c4Zk0G-mY)
