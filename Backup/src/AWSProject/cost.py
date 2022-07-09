from csv import excel
import boto3
import json
import pprint
import csv


# class Cost:

#     def __init__(self, client):
#         self.client = client

client = boto3.client('ce')

response = client.get_cost_and_usage(
    TimePeriod={
        'Start': '2022-06-01',
        'End': '2022-07-01'
    },
    Granularity='DAILY',  # 'DAILY' | 'MONTHLY' | 'HOURLY'
    # Filter={

    #     "Not": {
    #         "Dimensions": {
    #             "Key": "RECORD_TYPE",
    #             "Values": ["Refund", "Upfront", "Support"],
    #         }
    #     }
    # },
    Metrics=[
        # 'BLENDED_COST',
        'UNBLENDED_COST',
        # 'AMORTIZED_COST',
        # 'NET_AMORTIZED_COST',
        # 'NET_UNBLENDED_COST',
        # 'USAGE_QUANTITY',
        # 'NORMALIZED_USAGE_AMOUNT'
    ],
    # GroupBy=[
    #     {
    #         'Type': 'DIMENSION',
    #         'Key': 'SERVICE'
    #     },
    # ]
)

size = len(response['ResultsByTime'])

for i in range(size):
    print(response['ResultsByTime'][i]['Total']['UnblendedCost'])
