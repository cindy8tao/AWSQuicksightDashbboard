from csv import excel
import boto3
import json
import pprint
import csv


class Backup:

    def __init__(self, client):
        self.client = client

    def list_recovery_points_with_tags(self):

        try:
            response = self.client.list_recovery_points_by_backup_vault(
                BackupVaultName='Default',
            )
            size = len(response['RecoveryPoints'])
            # size = 10

            data_file = {}

            for i in range(size):
                resource_arn = response['RecoveryPoints'][i]['RecoveryPointArn']
                tags = self.client.list_tags(
                    ResourceArn=resource_arn

                )
                data_file[resource_arn] = [tags['Tags'],
                                           response['RecoveryPoints'][0]['ResourceType']]

            self.write_to_csv(data_file)
            print("Complete writing csv file")

            self.write_to_json(data_file)
            print("Complete writing json file")

        except NameError:
            print("Error listing recovery point with tags")

    def write_to_csv(self, data_file):
        csv_file = open('/tmp/csv_file.csv', 'w+')
        csv_writer = csv.writer(csv_file)
        count = 1

        header = ["ResourceArn", "Department", "Environment", "ResourceType"]
        csv_writer.writerow(header)

        for key, value, in data_file.items():
            row = [key]
            if len(value[0]) == 0:
                row.append(" ")
                row.append(" ")
            else:
                for v in value[0].values():
                    row.append(v)
            row.append(value[1])

            csv_writer.writerow(row)
            count += 1

        csv_file.close()

    def write_to_json(self, data_file):

        with open('/tmp/file.json', 'w+') as outfile:
            outfile.write(json.dumps(data_file))
            outfile.close()
