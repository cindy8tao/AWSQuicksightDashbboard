from csv import excel
import datetime
from importlib.resources import Resource
from urllib.request import Request
import boto3
import json
import pprint
import csv
import pandas as pd


class Backup:

    def __init__(self, client):
        self.client = client

    # def list_recovery_points_with_tags(self):

    #     try:
    #         response = self.client.list_recovery_points_by_backup_vault(
    #             BackupVaultName='Default',
    #         )
    #         # size = len(response['RecoveryPoints'])
    #         size = 3

    #         json_file = {}
    #         for i in range(size):
    #             resource_arn = response['RecoveryPoints'][i]['RecoveryPointArn']
    #             tags = self.client.list_tags(
    #                 ResourceArn=resource_arn
    #             )

    #             json_file = json.dumps(tags)
    #             with open('file.json', 'a') as outfile:
    #                 outfile.write(json.dumps(tags))
    #                 outfile.write(",")
    #                 outfile.close()

    #         print("Complete writing json file")

    #         return json_file

    #     except NameError:
    #         print("Error listing recovery point with tags")

    def list_recovery_points_with_tags(self):

        try:
            response = self.client.list_recovery_points_by_backup_vault(
                BackupVaultName='Default',
            )
            # size = len(response['RecoveryPoints'])
            size = 10

            data_file = {}

            for i in range(size):
                resource_arn = response['RecoveryPoints'][i]['RecoveryPointArn']
                tags = self.client.list_tags(
                    ResourceArn=resource_arn

                )
                data_file[resource_arn] = tags['Tags']

            self.write_to_csv(data_file)
            print("Complete writing csv file")

            self.write_to_json(data_file)
            print("Complete writing json file")

        except NameError:
            print("Error listing recovery point with tags")

    def write_to_csv(self, data_file):
        csv_file = open('csv_file.csv', 'w')
        csv_writer = csv.writer(csv_file)
        count = 0

        for data in data_file:
            if count == 0:
                header = ["resource_arn"]
                for key in data_file[data].keys():
                    header.append(key)
                csv_writer.writerow(header)
                count += 1
            else:
                line = [data]
                for value in data_file[data].values():
                    line.append(value)
                csv_writer.writerow(line)
                count += 1

        csv_file.close()

    def write_to_json(self, data_file):

        with open('file.json', 'a') as outfile:
            outfile.write(json.dumps(data_file))
            outfile.close()
