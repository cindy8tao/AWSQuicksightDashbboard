class Backup:

    def __init__(self, account_id, client):
        self.account_id = account_id
        self.client = client

    def create_backup_plan(self, backup_plan_name, rule_name, start_window_minutes, completion_window_minutes, schedule_expression, target_backup_vault_name, number):
        try:
            response = self.client.create_backup_plan(
                BackupPlan={
                    'BackupPlanName': backup_plan_name + str(number),
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

            print("Successfully created backup plan")
        except NameError:
            print("Error has occur during creation")
