from csv import excel
import datetime
from importlib.resources import Resource
from urllib.request import Request
import boto3
import json
import pprint


class Backup:

    def __init__(self, client):
        self.client = client

    def list_recovery_points_with_tags(self):

        try:
            response = self.client.list_recovery_points_by_backup_vault(
                BackupVaultName='Default',
            )
            # size = len(response['RecoveryPoints'])
            size = 3

            json_file = {}
            for i in range(size):
                resource_arn = response['RecoveryPoints'][i]['RecoveryPointArn']
                tags = self.client.list_tags(
                    ResourceArn=resource_arn
                )

                json_file = json.dumps(tags)
                with open('file.json', 'a') as outfile:
                    outfile.write(json.dumps(tags))
                    outfile.write(",")
                    outfile.close()

            print("Complete writing json file")

            return json_file

        except NameError:
            print("Error listing recovery point with tags")
