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
