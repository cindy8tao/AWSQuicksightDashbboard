from csv import excel
import boto3
import json
import pprint
import csv


class Backup:

    def __init__(self, account_id, client):
        self.account_id = account_id
        self.client = client

    def assign_backup_resources(self, backupPlanId, environment, department):
        try:
            response = self.client.create_backup_selection(
                BackupPlanId=backupPlanId,
                BackupSelection={
                    'SelectionName': environment + 'backup',
                    'IamRoleArn': 'arn:aws:iam::'+self.account_id+':role/aws-service-role/backup.amazonaws.com/AWSServiceRoleForBackup',
                    'Resources': [
                        '*',
                    ],
                    'ListOfTags': [
                        {
                            'ConditionType': 'STRINGEQUALS',
                            'ConditionKey': 'Environment',
                            'ConditionValue': environment
                        },
                        {
                            'ConditionType': 'STRINGEQUALS',
                            'ConditionKey': 'Department',
                            'ConditionValue': department
                        },
                    ]
                },
            )
            print("Successfully assigned backup resources")
        except NameError:
            print("Error when assigning backup resources")

    def create_backup_plan(self, start_window_minutes, completion_window_minutes, target_backup_vault_name, hrs, environment, department):

        try:
            response = self.client.create_backup_plan(
                BackupPlan={
                    'BackupPlanName': str(hrs) + 'hours-'+self.account_id,
                    'Rules': [
                        {
                            'RuleName': 'every' + str(hrs) + 'hours',
                            'TargetBackupVaultName': target_backup_vault_name,
                            'ScheduleExpression': 'cron(0 '+str(hrs) + ' * * ? *)',
                            'StartWindowMinutes': start_window_minutes,
                            'CompletionWindowMinutes': completion_window_minutes,
                            'RecoveryPointTags': {
                                'Environment': environment,
                                'Department': department
                            }
                        }
                    ]
                },
                BackupPlanTags={
                    'Environment': environment,
                    'Department': department
                },
            )

            self.assign_backup_resources(
                response['BackupPlanId'], environment, department)
            print("Successfully created backup plan")
        except NameError:
            print("Error has occur during creation")

    def list_recovery_points_with_tags(self):

        try:
            response = self.client.list_recovery_points_by_backup_vault(
                BackupVaultName='Default',
            )

            size = len(response['RecoveryPoints'])
            data_file = []
            header_list = []

            for i in range(size):
                resource_arn = response['RecoveryPoints'][i]['RecoveryPointArn']
                tags = self.client.list_tags(
                    ResourceArn=resource_arn

                )
                row = []
                tag = tags['Tags']
                resource_type = response['RecoveryPoints'][i]['ResourceType']
                backup_size = response['RecoveryPoints'][i]['BackupSizeInBytes']

                row.append(resource_arn)
                row.append(resource_type)
                row.append(backup_size)

                if (len(tag.values()) == 0):
                    row.append(" ")
                    row.append(" ")
                else:
                    for type_of_tag in tag.values():
                        row.append(type_of_tag)

                data_file.append(row)
                if tags['Tags'] != {}:
                    for key in list(tags['Tags'].keys()):
                        if key not in header_list:
                            header_list.append(key)

            self.write_to_csv(data_file, header_list)
            print("Complete writing csv file")

        except NameError:
            print("Error listing recovery point with tags")

    def get_tags(self):

        response = self.client.list_recovery_points_by_backup_vault(
            BackupVaultName='Default',
        )

        size = len(response['RecoveryPoints'])
        data_file = {}
        tags_list = []

        for i in range(size):
            resource_arn = response['RecoveryPoints'][i]['RecoveryPointArn']
            tags = self.client.list_tags(
                ResourceArn=resource_arn

            )
            data_file[resource_arn] = [tags['Tags'],
                                       response['RecoveryPoints'][0]['ResourceType']]
            if tags['Tags'] != {}:
                for key in list(tags['Tags'].keys()):
                    if key not in tags_list:
                        tags_list.append(key)

        return tags_list

    def write_to_csv(self, data_file, header_list):
        csv_file = open('/tmp/csv_file.csv', 'w')
        csv_writer = csv.writer(csv_file)

        header = ["ResourceArn", "ResourceType", "BackupSize"]
        for h in header_list:
            header.append(h)
        csv_writer.writerow(header)
        csv_writer.writerows(data_file)

        csv_file.close()
