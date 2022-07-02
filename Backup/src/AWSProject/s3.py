import datetime
from urllib.request import Request
import boto3
import json


class S3:

    def __init__(self):
        pass

    def list_all_bucket():
        s3 = boto3.resource('s3')

        for bucket in s3.buckets.all():
            print("Bucket:")
            print(bucket.name)

    def create_bucket():

        ACL = 'private'  # 'private'|'public-read'|'public-read-write'|'authenticated-read'
        BUCKET = 'backups3fromvs'

        client = boto3.client('s3')
        try:
            response = client.create_bucket(
                ACL=ACL,
                Bucket=BUCKET
            )
            print("Successfully created S3 bucket")
        except:
            print("Error has occur during creation of S3 bucket")

    def bucket_version():
        BUCKET = 'backups3fromvs'
        s3 = boto3.resource('s3')
        bucket_versioning = s3.BucketVersioning(BUCKET)

        try:
            response = bucket_versioning.enable()
            print("Successfully enabled version")
        except:
            print("Error when enabling version")

    def put_bucket_policy():
        BUCKET = 'backups3fromvs'
        ACCOUNT_ID = '774446988871'
        # Create a bucket policy
        bucket_name = BUCKET
        bucket_policy = {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "arn:aws:iam::" + ACCOUNT_ID + ":role/aws-service-role/reports.backup.amazonaws.com/AWSServiceRoleForBackupReports"
                    },
                    "Action": "s3:PutObject",
                    "Resource": [
                        "arn:aws:s3:::" + BUCKET + "/*"
                    ],
                    "Condition": {
                        "StringEquals": {
                            "s3:x-amz-acl": "bucket-owner-full-control"
                        }
                    }
                }
            ]
        }

        # Convert the policy from JSON dict to string
        bucket_policy = json.dumps(bucket_policy)

        # Set the new policy
        s3 = boto3.client('s3')
        try:
            s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
            print("Successfully added permision to S3 bucket ")
        except:
            print("Error when adding permission to S3 bucket")
