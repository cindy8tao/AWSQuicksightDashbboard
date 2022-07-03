import boto3
import backup
import s3

#####################################################
# Create the required clients and resources         #
#####################################################
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
backup_client = boto3.client('backup')
# account_id = input("Please enter your AWS account_id: ")
account_id = '774446988871'


def create_s3_bucket():
    print("Creating a S3 bucket ... ")
    bucket_name = input("Name of bucket: ")
    s3Class = s3.S3(account_id, s3_client, s3_resource)
    s3Class.create_bucket(bucket_name)

    version_enabled = input("Version enabled? (Yes/No) ")

    if(version_enabled.lower() == 'yes'):
        s3Class.bucket_version(bucket_name)
        s3Class.put_bucket_policy(bucket_name)

    to_upload_file = input(
        "Would you like to upload a file? (Yes/No)")
    if(to_upload_file.lower() == "yes"):
        # path = '/Users/cindytao/Document/GitHub/AWSQuicksightDashbboard/Backup/src/text.txt'
        # key = 'hello.txt'
        path = input("File path: ")
        key = input("File Name: ")
        s3Class.upload_to_S3(path, bucket_name, key)


def create_backup_plan():

    print("Creating backup plan ...")
    print("Please enter the following: ")

    backup_plan_name = input("Backup Plan Name (example: 12hrs): ")
    rule_name = input("Rule Name (example: RunEvery12Hours): ")
    start_window_minutes = int(
        input("Start Window Minutes (minimum value = 60): "))
    completion_window_minutes = int(input(
        "Completion Window Minutes (must be 60 > Start Window): "))
    schedule_expression = input(
        "Schedule Expression (example: cron(0 12 * * ? *)): ")
    target_backup_vault_name = input(
        "Target Backup Vault Name (example: Default): ")

    backupClass = backup.Backup(backup_client)
    backupClass.create_backup_plan(backup_plan_name, rule_name, start_window_minutes,
                                   completion_window_minutes, schedule_expression, target_backup_vault_name)


def create_backup_report():

    print("Creating backup report ...")
    print("Please enter the following: ")

    to_create_a_new_bucket = input(
        "Would you like to create a new bucket to store the backup report? (Yes/No) ")

    if (to_create_a_new_bucket.lower() == "yes"):
        create_s3_bucket()

    bucket_name = input("Enter the name of bucket to store backup report: ")
    report_plan_name = input("Report plan name: ")
    format = input("Format (JSON/CSV or both): ")
    report_template = input(
        "Report Template (RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT): ")

    backupClass = backup.Backup(backup_client)
    backupClass.create_report_plan(
        bucket_name, report_plan_name, format, report_template)


def main():

    #####################################################
    # Ask user for inputs                               #
    #####################################################

    print("Welcome to create your Quicksight Backup Dashboard ")
    # ACCOUNT_ID = '774446988871'
    # account_id = input("Please enter your account_id: ")
    # account_id = '774446988871'

    to_create_AWS_resource = input(
        "Would you like to create a AWS resource? (Yes/No) ")

    while (to_create_AWS_resource.lower() == "yes"):
        resource = input(
            "Which resources would you like to create? (EC2, RDS, S3) ")

        if (resource.lower() == 'ec2'):
            pass
        elif (resource.lower() == 'rds'):
            pass
        elif (resource.lower() == 's3'):
            create_s3_bucket()
            to_create_another_bucket = input(
                "Would you like to create another bucket? (Yes/No) ")
            while(to_create_another_bucket.lower() == 'yes'):
                create_s3_bucket()
                to_create_another_bucket = input(
                    "Would you like to create another bucket? (Yes/No) ")

        to_create_AWS_resource = input(
            "Would you like to create a AWS resource? (Yes/No) ")

    create_backup_plan()
    to_create_another_backup_plan = input(
        "Would you like to create another backup plan? (Yes/No) ")
    while(to_create_another_backup_plan.lower() == 'yes'):
        create_backup_plan()
        to_create_another_backup_plan = input(
            "Would you like to create another backup plan? (Yes/No) ")

    create_backup_report()
    to_create_another_backup_report = input(
        "Would you like to create another backup report? (Yes/No) ")
    while(to_create_another_backup_report.lower() == "yes"):
        create_backup_report()
        to_create_another_backup_report = input(
            "Would you like to create another backup report? (Yes/No) ")


if __name__ == "__main__":
    main()
