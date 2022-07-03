import datetime
from urllib.request import Request
import boto3
import json


class Backup:

    def __init__(self, client):
        self.client = client

    def create_backup_plan(self, backup_plan_name, rule_name, start_window_minutes, completion_window_minutes, schedule_expression, target_backup_vault_name):

        # BACKUP_PLAN_NAME = "12hrs"
        # RULE_NAME = "RunEvery12Hrs"
        # # Completion Window Minutes (must be 60 > Start Window)
        # COMPLETION_WINDOW_MINUTES = 120
        # START_WINDOW_MINUTES = 60  # Start Window Minutes (minimum value = 60)
        # # Schedule Expression (example: cron(0 12 * * ? *))
        # SCHEDULE_EXPRESSION = "cron(0 12 * * ? *)"
        # # Target Backup Vault Name (example: "Default")
        # TARGET_BACKUP_VAULT_NAME = "Default"

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

    def create_report_plan(self):

        REPORT_PLAN_NAME = 'backupreport'
        S3_BUCKET_NAME = 'backups3fromvs'
        FORMAT = {'JSON', 'CSV'}
        # RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT
        REPORT_TEMPLATE = 'BACKUP_JOB_REPORT'

        try:
            response = self.client.create_report_plan(
                ReportPlanName=REPORT_PLAN_NAME,
                # ReportPlanDescription='string',
                ReportDeliveryChannel={
                    'S3BucketName': S3_BUCKET_NAME,
                    # 'S3KeyPrefix': 'string',
                    'Formats': [
                        FORMAT,
                    ]
                },
                ReportSetting={
                    'ReportTemplate': REPORT_TEMPLATE,
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
            print(response)
        except NameError:
            print("Error has occur during creation of report plan")
