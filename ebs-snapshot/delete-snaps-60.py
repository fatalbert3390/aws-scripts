# Delete snapshots older than retention period

import boto3
from botocore.exceptions import ClientError

from datetime import datetime,timedelta

def delete_snapshot(snapshot_id):
    print "Deleting snapshot %s " % (snapshot_id)
    try:  
        ec2resource = boto3.resource('ec2')
        snapshot = ec2resource.Snapshot(snapshot_id)
        snapshot.delete()
    except ClientError as e:
        print "Caught exception: %s" % e

    return
    
def lambda_handler(event, context):
    
    # Get current timestamp in UTC
    now = datetime.now()

    # AWS Account ID    
    account_id = '041619730184'
    
    # Define retention period in days
    retention_days_seven = 7
    retention_days_three = 3
    retention_days_one = 1
    retention_days_sixty = 60
    
    # Create EC2 client
    ec2 = boto3.client('ec2')

    # Filtering by snapshot timestamp comparison is not supported
    # grab all snapshots for specified instances:
    result_sixty = ec2.describe_snapshots( Filters=[
        { 'Name': 'volume-id', 'Values': [
            'vol-67661510', # Hebe D
                ]
            }
        ]
    )

# delete snapshots older than 60 days    
    for snapshot in result_sixty['Snapshots']:
        print "Checking snapshot %s which was created on %s" % (snapshot['SnapshotId'],snapshot['StartTime'])
    
        # Remove timezone info from snapshot in order for comparison to work below
        snapshot_time = snapshot['StartTime'].replace(tzinfo=None)
    
        # Subtract snapshot time from now returns a timedelta
        # Check if the timedelta is greater than retention days
        if (now - snapshot_time) > timedelta(retention_days_sixty):
            print "Snapshot is older than configured retention of %d days" % (retention_days_sixty)
            delete_snapshot(snapshot['SnapshotId'])
        else:
            print "Snapshot is newer than configured retention of %d days so we keep it" % (retention_days_sixty)




