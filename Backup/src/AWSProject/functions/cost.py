import csv


class Cost:

    def __init__(self, account_id, client):
        self.account_id = account_id
        self.client = client

    def get_cost_and_usage(self, tag):
        response = self.client.get_cost_and_usage(
            TimePeriod={
                'Start': '2022-07-01',
                'End': '2022-07-20'
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
        cost_data = []
        for tag in tags:
            response = self.get_cost_and_usage(tag)
            size = len(response['ResultsByTime'])

            for i in range(size):
                row = []
                tag_response = response['ResultsByTime'][i]['Groups'][0]['Keys'][0][:-1]
                unblendedcost = float(
                    response['ResultsByTime'][i]['Groups'][0]['Metrics']['UnblendedCost']['Amount'])
                start = response['ResultsByTime'][0]['TimePeriod']['End']
                end = response['ResultsByTime'][0]['TimePeriod']['Start']

                row = [start, end, tag_response, unblendedcost]
                cost_data.append(row)

        self.write_to_csv(cost_data)

    def write_to_csv(self, cost_data):

        csv_file = open(
            '/tmp/cost.csv', 'w+')
        csv_writer = csv.writer(csv_file)

        header = ["StartDate", "EndDate", "Tags", "UnblendedCost"]
        csv_writer.writerow(header)
        csv_writer.writerows(cost_data)

        csv_file.close()
