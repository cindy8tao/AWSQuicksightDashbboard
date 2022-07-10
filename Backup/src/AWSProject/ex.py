import resource
import boto3


s3 = boto3.resource('s3')
print("Hello")
for bucket in s3.buckets.all():
    print("List of Bucket:")
    print(bucket.name)

# client = boto3.client('s3')
# response = client.delete_bucket(
#     Bucket='string',
# )
