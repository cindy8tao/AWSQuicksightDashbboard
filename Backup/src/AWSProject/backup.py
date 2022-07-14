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
            data_file = {}
            header_list = []

            for i in range(size):
                resource_arn = response['RecoveryPoints'][i]['RecoveryPointArn']
                tags = self.client.list_tags(
                    ResourceArn=resource_arn

                )

                tag = tags['Tags']
                resource_type = response['RecoveryPoints'][i]['ResourceType']
                # backup_size = int(
                #     response['RecoveryPoints'][i]['BackupSizeInBytes'])
                # backup_size = response['RecoveryPoints'][i]['BackupSizeInBytes']
                backup_size = 8392018
                data_file[resource_arn] = [tag, resource_type, backup_size]
                if tags['Tags'] != {}:
                    for key in list(tags['Tags'].keys()):
                        if key not in header_list:
                            header_list.append(key)

            self.write_to_csv(data_file, header_list)
            print("Complete writing csv file")

            self.write_to_json(data_file)
            print("Complete writing json file")

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
        csv_file = open('/tmp/csv_file.csv', 'w+')
        csv_writer = csv.writer(csv_file)
        count = 1

        header = ["ResourceArn", "ResourceType", "BackupSize"]
        for h in header_list:
            header.append(h)
        csv_writer.writerow(header)

        for key, value, in data_file.items():
            print(type(value[2]))
            row = [key, value[1], value[2]]
            if len(value[0]) == 0:
                row.append(" ")
                row.append(" ")
            else:
                for v in value[0].values():
                    row.append(v)
            csv_writer.writerow(row)
            count += 1

        csv_file.close()

    def write_to_json(self, data_file):

        with open('/tmp/file.json', 'w+') as outfile:
            outfile.write(json.dumps(data_file))
            outfile.close()


# client = boto3.client('backup')
