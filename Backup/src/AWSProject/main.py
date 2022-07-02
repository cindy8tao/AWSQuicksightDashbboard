import backup
import s3


def main():
    # backup.Backup.create_backup_plan()
    # s3.S3.create_bucket()
    s3.S3.bucket_version()
    # backup.Backup.create_report_plan()
    s3.S3.put_bucket_policy()


if __name__ == "__main__":
    main()
