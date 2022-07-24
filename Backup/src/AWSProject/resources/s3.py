import boto3
import json
from datetime import datetime


class S3:

    def __init__(self, account_id, client, resource):
        self.client = client
        self.resource = resource
        self.account_id = account_id

    def create_bucket(self, bucket_name):
        acl = 'private'
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
