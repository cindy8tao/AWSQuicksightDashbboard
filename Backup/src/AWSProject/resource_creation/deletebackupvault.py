import datetime
from urllib.request import Request
import boto3
import json

client = boto3.client('backup')

response = client.list_recovery_points_by_backup_vault(
    BackupVaultName='Default'
)

i = 0
size = len(response['RecoveryPoints'])
listarn = []
while i < size:
    recovery_point_arn = response['RecoveryPoints'][i]['RecoveryPointArn']
    listarn.append(recovery_point_arn)
    i = i + 1

for l in listarn:
    response = client.delete_recovery_point(
        BackupVaultName='Default',
        RecoveryPointArn=l
    )
    print("Deleted " + l)
