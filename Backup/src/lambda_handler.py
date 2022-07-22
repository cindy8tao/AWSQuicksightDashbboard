# pylint: disable = C0103, R0902, W1203, C0301
"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import os
import logging
import traceback
from urllib.parse import unquote_plus
from AWSBackupObserver import AWSBackupObserver
from GluePartitionManager import GluePartitionManager
from CustomResourceManager import CustomResourceManager


logger = logging.getLogger()
logger.setLevel(logging.INFO)

######################################################################


#                        FUNCTIONAL LOGIC                            #
######################################################################

def handler(event, context):
    """
    Entry point for the Lambda function.
    """
    logger.info(f'Event : {event}')
    backup_observer = AWSBackupObserver(event, context)
    glue_manager = GluePartitionManager(event, context)
    cfn_manager = CustomResourceManager(event, context)

    if event.get('source') == 'aws.backup':
        try:
            detail_type = event.get('detail-type')
            event_detail = event.get('detail')
            job_event_state = event_detail.get('state')
            if not job_event_state:
                # Hack
                job_event_state = event_detail.get('status')

            if job_event_state in ('ABORTED', 'COMPLETED', 'FAILED', 'EXPIRED'):
                if detail_type == 'Backup Job State Change':
                    job_event_type = 'backup_job'
                    job_id = event_detail.get('backupJobId')
                elif detail_type == 'Restore Job State Change':
                    job_event_type = 'restore_job'
                    job_id = event_detail.get('restoreJobId')
                elif detail_type == 'Copy Job State Change':
                    job_event_type = 'copy_job'
                    job_id = event_detail.get('copyJobId')
                else:
                    logger.error(
                        f"unknown detail type : {detail_type} for aws.backup")
                    return

                backup_observer.handle_aws_backup_event(job_event_type, job_id)

        except Exception:
            var = traceback.format_exc()
            logger.error(f"Error {var} in lambda_handler")

    elif event.get('source') == 'observer.command':
        try:
            backup_observer.handle_observer_command(event)
        except Exception:
            var = traceback.format_exc()
            logger.error(f"Error {var} handling observer.command")

    elif event.get('source') == 'observer.events':
        try:
            backup_observer.handle_observer_event(event)
        except Exception:
            var = traceback.format_exc()
            logger.error(f"Error {var} handling observer.events")

    elif event.get('source') == 'backupauditmanager.events':
        try:
            backup_observer.handle_backup_audit_manager_event(event)
        except Exception:
            var = traceback.format_exc()
            logger.error(f"Error {var} in lambda_handler")

    # Handle Schedule Event Invocation
    elif event.get('detail-type') == 'Scheduled Event':
        logger.info("Processing Scheduled Event")
        backup_observer.handle_scheduled_event(event, context)

    elif event.get('ReportRecipient'):
        report_recipient = event.get('ReportRecipient')
        backup_observer.verify_email_address(report_recipient)

    elif event.get('RefreshGluePartitions') == 'true':
        logger.info('RefreshGluePartitions request')
        glue_manager.refresh_existing_table_details_cache()
        glue_manager.refresh_initial_partitions_from_bucket()

    elif event.get('RefreshConfigItems') == 'true':
        logger.info('RefreshConfigItems request')
        backup_observer.extract_config_details()

    elif event.get('RefreshJobLogs'):
        backup_observer.handle_refresh_job_logs(event)

    # Create request from CloudFormation
    elif event.get('RequestType') == 'Create':
        logger.info(
            f'request received of type {event["RequestType"]}, proceeding to configure resources')
        cfn_manager.handle_custom_resource_create_request(event, context)

    # Update request from CloudFormation
    elif event.get('RequestType') == 'Update':
        logger.info(
            f'request received of type {event["RequestType"]}, There are NO custom resources to update')
        cfn_manager.handle_custom_resource_update_request(event, context)

    # Delete request from CloudFormation
    elif event.get('RequestType') == 'Delete':
        logger.info(
            f'request received of type {event["RequestType"]}, proceeding to delete resources')
        cfn_manager.handle_custom_resource_delete_request(event, context)

    elif event.get('CleanupGluePartitions') == 'true':
        # Clear the GlueCache to avoid stale data
        glue_manager.delete_glue_cache(
            glue_manager.glue_table_partition_cache_key)

    elif event.get('RefreshBackupAuditManagerReports') == 'true':
        backup_observer.handle_backup_audit_manager_report_refresh()

    elif event.get('Records'):
        # Notification that an S3 PUT event occurred , Check if the partition update is required.
        if ('eventSource' in event['Records'][0]) and \
                event['Records'][0]['eventSource'] == 'aws:s3':
            logger.info('S3 event notification received')
            try:
                s3_bucket_name = event['Records'][0]['s3']['bucket']['name']
                s3_key = unquote_plus(
                    event['Records'][0]['s3']['object']['key'])

                if glue_manager.glue_database_name:
                    glue_manager.update_glue_partition_for_s3_key(s3_key)
                else:
                    backup_observer.handle_backup_audit_manager_report(
                        s3_bucket_name, s3_key)
            except Exception as e:  # pylint: disable = W0703
                logger.error(e)
