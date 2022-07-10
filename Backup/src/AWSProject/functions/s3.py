import boto3
import json
from datetime import datetime


class S3:

    def __init__(self, account_id, client, resource):
        self.client = client
        self.resource = resource
        self.account_id = account_id

    def list_all_bucket(self):
        for bucket in self.resource.buckets.all():
            print("List of Bucket:")
            print(bucket.name)

    def create_bucket(self, bucket_name):
        acl = 'private'  # 'private'|'public-read'|'public-read-write'|'authenticated-read'

        try:
            response = self.client.create_bucket(
                ACL=acl,
                Bucket=bucket_name
            )
            print("Successfully created S3 bucket")
        except NameError:
            print("Error has occur during creation of S3 bucket: ")

    def bucket_version(self, bucket_name):

        bucket_versioning = self.resource.BucketVersioning(bucket_name)
        try:
            response = bucket_versioning.enable()
            print("Successfully enabled version")
        except NameError:
            print("Error when enabling version")

    # def put_bucket_policy(self, bucket_name):
    #     # Create a bucket policy
    #     bucket_policy = {
    #         "Version": "2012-10-17",
    #         "Statement": [
    #             {
    #                 "Effect": "Allow",
    #                 "Principal": {
    #                     "AWS": "arn:aws:iam::" + self.account_id + ":role/aws-service-role/reports.backup.amazonaws.com/AWSServiceRoleForBackupReports"
    #                 },
    #                 "Action": "s3:PutObject",
    #                 "Resource": [
    #                     "arn:aws:s3:::" + bucket_name + "/*"
    #                 ],
    #                 "Condition": {
    #                     "StringEquals": {
    #                         "s3:x-amz-acl": "bucket-owner-full-control"
    #                     }
    #                 }
    #             }
    #         ]
    #     }

    #     # Convert the policy from JSON dict to string
    #     bucket_policy = json.dumps(bucket_policy)

    #     # Set the new policy
    #     s3 = boto3.client('s3')
    #     try:
    #         s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
    #         print("Successfully added permision to S3 bucket ")
    #     except NameError:
    #         print("Error when adding permission to S3 bucket")

    def put_bucket_policy(self, bucket_name):
        # Create a bucket policy
        bucket_policy = {
            "Version": "2008-10-17",
            "Id": "Policy1335892530063",
            "Statement": [
                {
                    "Sid": "Stmt1335892150622",
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "billingreports.amazonaws.com"
                    },
                    "Action": [
                        "s3:GetBucketAcl",
                        "s3:GetBucketPolicy"
                    ],
                    "Resource": "arn:aws:s3:::cost-report-for-quicksight-774446988871",
                    "Condition": {
                        "StringEquals": {
                            "aws:SourceArn": "arn:aws:cur:us-east-1:774446988871:definition/*",
                            "aws:SourceAccount": "774446988871"
                        }
                    }
                },
                {
                    "Sid": "Stmt1335892526596",
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "billingreports.amazonaws.com"
                    },
                    "Action": "s3:PutObject",
                    "Resource": "arn:aws:s3:::cost-report-for-quicksight-774446988871/*",
                    "Condition": {
                        "StringEquals": {
                            "aws:SourceArn": "arn:aws:cur:us-east-1:774446988871:definition/*",
                            "aws:SourceAccount": "774446988871"
                        }
                    }
                }
            ]
        }

        # Convert the policy from JSON dict to string
        bucket_policy = json.dumps(bucket_policy)

        try:
            self.client.put_bucket_policy(
                Bucket=bucket_name, Policy=bucket_policy)
            print("Successfully added permision to S3 bucket ")
        except NameError:
            print("Error when adding permission to S3 bucket")

    def upload_to_S3(self, path, bucket_name, key, content_type):

        now = datetime.now()
        folder_name = now.strftime("%m/%d/%Y")

        try:
            self.resource.meta.client.upload_file(
                path, bucket_name, Key=(folder_name + '/' + key), ExtraArgs={'ContentType': content_type})
            print("Successfully upload the file")
        except NameError:
            print("Error uploading")

    def s3_object(self, bucket_name, csv_file, key):
        print(csv_file)
        try:
            response = self.client.put_object(
                Body=csv_file,
                Bucket=bucket_name,
                Key=key,
                ContentType="text/csv"
            )
            print("Successfully put object")
        except NameError:
            print("Error putting object")
