import boto3
import json


class Glue:

    def __init__(self, account_id, client):
        self.account_id = account_id
        self.client = client

    def create_crawler(self, crawler_name, role, database_name, path):

        try:
            response = self.client.create_crawler(
                Name=crawler_name,
                Role=role,
                DatabaseName=database_name,
                Targets={
                    'S3Targets': [
                        {
                            'Path': path
                        }
                    ],
                }
            )
            print("Successfully create a crawler ")
        except NameError:
            print("Error occurred when creating a crawler")

        try:
            response = self.client.start_crawler(
                Name='backup_crawler'
            )
            print("Successfully started the crawler")
        except:
            print("Error occurred when starting the crawler")
