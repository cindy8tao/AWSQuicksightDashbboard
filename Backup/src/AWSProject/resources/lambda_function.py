import boto3
from resources import backup
from resources import s3
from resources import ec2
from resources import rds
import pprint
import os

#####################################################
# Create the required clients and resources         #
#####################################################
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')
backup_client = boto3.client('backup')
ec2_resource = boto3.resource('ec2')
rds_client = boto3.client('rds')


def create_s3_bucket(account_id, number):
    print("Creating a S3 bucket ... ")
    bucket_name = "bucket-" + account_id + "-" + str(number)
    s3Class = s3.S3(account_id, s3_client, s3_resource)
    s3Class.create_bucket(bucket_name)
    s3Class.bucket_version(bucket_name)


def create_rds_instance(account_id, number):
    print("Creating a RDS instance ... ")

    DBInstanceClass = os.environ['DBInstanceClass']
    DBInstanceIdentifier = "database-instance-" + \
        account_id + "-" + str(number)
    Engine = os.environ['Engine']
    AllocatedStorage = int(os.environ['AllocatedStorage'])
    MasterUsername = os.environ['MasterUsername']
    MasterPassword = os.environ['MasterPassword']

    rdsClass = rds.RDS(account_id, rds_client)
    rdsClass.create_db_instance(DBInstanceClass, DBInstanceIdentifier,
                                Engine, AllocatedStorage, MasterUsername, MasterPassword)


def create_ec2_instance(account_id):
    print("Creating a EC2 instance ... ")
    AMIImageID = os.environ['AMIImageID']
    ec2Class = ec2.EC2(account_id, ec2_resource)
    ec2Class.create_instances(AMIImageID)


def create_backup_plan(account_id, number):

    print("Creating backup plan ...")
    print("Please enter the following: ")

    BackupPlanName = os.environ['BackupPlanName']
    RuleName = os.environ['RuleName']
    StartWindowMinutes = int(os.environ['StartWindowMinutes'])
    CompletionWindowMinutes = int(os.environ['CompletionWindowMinutes'])
    ScheduleExpression = os.environ['ScheduleExpression']
    TargetBackupVaultName = os.environ['TargetBackupVaultName']

    backupClass = backup.Backup(backup_client)
    backupClass.create_backup_plan(BackupPlanName, RuleName, StartWindowMinutes,
                                   CompletionWindowMinutes, ScheduleExpression, TargetBackupVaultName, number)


def lambda_handler(event, context):

    print("Welcome to create your Quicksight Backup Dashboard ")
    account_id = context.invoked_function_arn.split(":")[4]

    NumberOfEC2 = int(os.environ['NumberOfEC2'])
    for i in range(NumberOfEC2):
        create_ec2_instance(account_id)

    NumberOfRDS = int(os.environ['NumberOfRDS'])
    for i in range(NumberOfRDS):
        create_rds_instance(account_id, i)

    NumberOfS3 = int(os.environ['NumberOfS3'])
    for i in range(NumberOfS3):
        create_s3_bucket(account_id, i)

    NumberOfPlan = int(os.environ['NumberOfPlan'])
    for i in range(NumberOfPlan):
        create_backup_plan(account_id, i)

    print("Thank you for using this app")
