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

    def create_backup_plan(self, backup_plan_name, rule_name, start_window_minutes, completion_window_minutes, schedule_expression, target_backup_vault_name):

        try:
            response = self.client.create_backup_plan(
                BackupPlan={
                    'BackupPlanName': backup_plan_name,
                    'Rules': [
                        {
                            'RuleName': rule_name,
                            'TargetBackupVaultName': target_backup_vault_name,
                            'ScheduleExpression': schedule_expression,
                            'StartWindowMinutes': start_window_minutes,
                            'CompletionWindowMinutes': completion_window_minutes,
                        }
                    ]
                }
            )
            BACKUP_PLAN_ID = response['BackupPlanId']
            print("Successfully created backup plan")
        except NameError:
            print("Error has occur during creation")

        # Delete the backup plan just created
        # try:
        #     response = client.delete_backup_plan(
        #         BackupPlanId=BACKUP_PLAN_ID
        #     )
        #     print("Successfully deleted plan")
        # except NameError:
        #     print("Error has occur during deletion")

    def create_report_plan(self, bucket_name, report_plan_name, format, report_template):

        try:
            response = self.client.create_report_plan(
                ReportPlanName=report_plan_name,
                # ReportPlanDescription='string',
                ReportDeliveryChannel={
                    'S3BucketName': bucket_name,
                    # 'S3KeyPrefix': 'string',
                    'Formats': [
                        format,
                    ]
                },
                ReportSetting={
                    'ReportTemplate': report_template,
                    # 'FrameworkArns': [
                    #     'string',
                    # ],
                    # 'NumberOfFrameworks': 123
                },
                # ReportPlanTags={
                #     'string': 'string'
                # },
                # IdempotencyToken='string'
            )
            print("Successfully created backup report")
        except NameError:
            print("Error has occur during creation of report plan")

    def list_recovery_points_with_tags(self):

        try:
            response = self.client.list_recovery_points_by_backup_vault(
                BackupVaultName='Default',
            )
            size = len(response['RecoveryPoints'])

            for i in range(size):
                resource_arn = response['RecoveryPoints'][i]['RecoveryPointArn']
                tags = self.client.list_tags(
                    ResourceArn=resource_arn
                )

                with open('file.json', 'a') as outfile:
                    outfile.write(json.dumps(tags))
                    outfile.write(",")
                    outfile.close()

            print("Complete writing json file")

        except NameError:
            print("Error listing recovery point with tags")
