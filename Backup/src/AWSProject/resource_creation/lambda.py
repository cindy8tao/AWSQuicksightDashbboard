import boto3
import csv
import datetime
import os

# Analyze payload from CloudWatch Event


def pipeline_execution(data):
    print(data)
    # Specify data fields to deliver to S3
    row = ['pipeline,time,state,execution,stage,action']

    if "stage" in data['detail'].keys():
        stage = data['detail']['execution']
    else:
        stage = 'NA'

    if "action" in data['detail'].keys():
        action = data['detail']['action']
    else:
        action = 'NA'
    row.append(data['detail']['pipeline']+','+data['time']+','+data['detail']
               ['state']+','+data['detail']['execution']+','+stage+','+action)
    values = '\n'.join(str(v) for v in row)
    return values

 # Upload CSV file to S3 bucket


def upload_data_to_s3(data):
    s3 = boto3.client('s3')
    runDate = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S:%f")
    csv_key = runDate+'.csv'
    response = s3.put_object(
        Body=data,
        Bucket='new-backup-report-based-arn-tags',
        Key=csv_key
    )


def lambda_handler(event, context):
    upload_data_to_s3(pipeline_execution(event))
