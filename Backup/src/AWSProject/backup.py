import datetime
from urllib.request import Request
import boto3
import json

# Let's use Amazon S3


class Backup:

    def __init__(self):
        pass

    def create_backup_plan():
        client = boto3.client('backup',
                              aws_access_key_id='AKIA3IUFDHZD65DZ2BQX',
                              aws_secret_access_key='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')

        BACKUP_PLAN_NAME = "12hrs"
        RULE_NAME = "RunEvery12Hrs"
        # Completion Window Minutes (must be 60 > Start Window)
        COMPLETION_WINDOW_MINUTES = 120
        START_WINDOW_MINUTES = 60  # Start Window Minutes (minimum value = 60)
        # Schedule Expression (example: cron(0 12 * * ? *))
        SCHEDULE_EXPRESSION = "cron(0 12 * * ? *)"
        # Target Backup Vault Name (example: "Default")
        TARGET_BACKUP_VAULT_NAME = "Default"

        try:
            response = client.create_backup_plan(
                BackupPlan={
                    'BackupPlanName': BACKUP_PLAN_NAME,
                    'Rules': [
                        {
                            'RuleName': RULE_NAME,
                            'TargetBackupVaultName': TARGET_BACKUP_VAULT_NAME,
                            'ScheduleExpression': SCHEDULE_EXPRESSION,
                            'StartWindowMinutes': START_WINDOW_MINUTES,
                            'CompletionWindowMinutes': COMPLETION_WINDOW_MINUTES,
                        }
                    ]
                }
            )
            BACKUP_PLAN_ID = response['BackupPlanId']
            print("Successfully created backup plan")
        except:
            print("Error has occur during creation")

        # Delete the backup plan just created
        # try:
        #     response = client.delete_backup_plan(
        #         BackupPlanId=BACKUP_PLAN_ID
        #     )
        #     print("Successfully deleted plan")
        # except:
        #     print("Error has occur during deletion")

    def create_report_plan():

        client = boto3.client('backup',
                              aws_access_key_id='AKIA3IUFDHZD65DZ2BQX',
                              aws_secret_access_key='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')

        REPORT_PLAN_NAME = 'backupreport'
        S3_BUCKET_NAME = 'backups3fromvs'
        FORMAT = 'JSON'
        # RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT
        REPORT_TEMPLATE = 'BACKUP_JOB_REPORT'

        try:
            response = client.create_report_plan(
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
        except:
            print("Error has occur during creation of report plan")
