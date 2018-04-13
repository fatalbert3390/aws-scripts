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
    result_one = ec2.describe_snapshots( Filters=[
        { 'Name': 'volume-id', 'Values': [
            'vol-062db5b7f9c9a2d6b', # Hebe C
            'vol-0f2857c60be51ad35', # Gaia C
            'vol-8c0b7bcf', # Gaia D
            'vol-0db623ad46a082e9d', # Zelus C
            'vol-0fd6a90020a728dd6', # Zelus D
                ]
            }
        ]
    )

# delete snapshots older than 1 day    
    for snapshot in result_one['Snapshots']:
        print "Checking snapshot %s which was created on %s" % (snapshot['SnapshotId'],snapshot['StartTime'])
    
        # Remove timezone info from snapshot in order for comparison to work below
        snapshot_time = snapshot['StartTime'].replace(tzinfo=None)
    
        # Subtract snapshot time from now returns a timedelta
        # Check if the timedelta is greater than retention days
        if (now - snapshot_time) > timedelta(retention_days_one):
            print "Snapshot is older than configured retention of %d days" % (retention_days_one)
            delete_snapshot(snapshot['SnapshotId'])
        else:
            print "Snapshot is newer than configured retention of %d days so we keep it" % (retention_days_one)
            
