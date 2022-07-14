from csv import excel
import boto3
import json
import pprint
import csv


class Cost:

    def __init__(self, account_id, client):
        self.account_id = account_id
        self.client = client

    def get_cost_and_usage(self, tag):
        # try:
        response = self.client.get_cost_and_usage(
            TimePeriod={
                'Start': '2022-07-01',
                'End': '2022-07-13'
            },
            Granularity='DAILY',
            Metrics=[
                'UnblendedCost',
            ],
            GroupBy=[
                {
                    'Type': 'TAG',
                    'Key': tag
                },
            ],
        )

        return response

    def get_cost_by_tags(self, tags):
        cost_data = {}
        for tag in tags:
            response = self.get_cost_and_usage(tag)
            size = len(response['ResultsByTime'])

            for i in range(size):
                key = response['ResultsByTime'][i]['Groups'][0]['Keys'][0][:-1]
                value = float(response['ResultsByTime'][i]['Groups']
                              [0]['Metrics']['UnblendedCost']['Amount'])
                if key in cost_data.keys():
                    cost_data[key] += value
                else:
                    cost_data[key] = value

        self.write_to_csv(cost_data)

    def write_to_csv(self, cost_data):

        csv_file = open('/tmp/cost.csv', 'w+')
        csv_writer = csv.writer(csv_file)
        count = 1

        header = ["Tags", "UnblendedCost"]
        csv_writer.writerow(header)
        row = []

        for key, value, in cost_data.items():
            row = [key, value]

            csv_writer.writerow(row)
            count += 1

        csv_file.close()
