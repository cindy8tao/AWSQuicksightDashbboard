import boto3
import backup
import s3


def main():

    s3_client = boto3.client('s3')
    s3_resource = boto3.resource('s3')

    print("Welcome to create your Quicksight Backup Dashboard ")
    # ACCOUNT_ID = '774446988871'
    account_id = input("Please enter your account_id: ")

    to_create_AWS_resource = input(
        "Would you like to create a AWS resource? (Yes/No) ")
    print(to_create_AWS_resource)

    if (to_create_AWS_resource.lower() == "yes"):
        resource = input(
            "Which resources would you like to create? (EC2, RDS, S3) ")

        if (resource.lower() == 'ec2'):
            pass
        elif (resource.lower() == 'rds'):
            pass
        elif (resource.lower() == 's3'):
            print("Creating a S3 bucket ... ")
            bucket_name = input("Name of bucket: ")
            s3Class = s3.S3(account_id, s3_client, s3_resource, bucket_name)
            s3Class.create_bucket()

            version_enabled = input("Version enabled? (Yes/No) ")

            if(version_enabled.lower() == 'yes'):
                s3Class.bucket_version()
                s3Class.put_bucket_policy()

                # backup.Backup.create_backup_plan()
                # backup.Backup.create_report_plan()


if __name__ == "__main__":
    main()
