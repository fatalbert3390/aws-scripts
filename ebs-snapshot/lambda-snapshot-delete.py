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

    # Define retention period in days
    retention_days = 7
    
    # Create EC2 client
    ec2 = boto3.client('ec2')
    
    # grab all snapshots for specified volumes:
    result = ec2.describe_snapshots( VolumeIds=[
	'vol-############', 
	]
    )
    
    for snapshot in result['Snapshots']:
        print "Checking snapshot %s which was created on %s" % (snapshot['SnapshotId'],snapshot['StartTime'])
    
        # Remove timezone info from snapshot in order for comparison to work below
        snapshot_time = snapshot['StartTime'].replace(tzinfo=None)
    
        # Subtract snapshot time from now returns a timedelta
        # Check if the timedelta is greater than retention days
        if (now - snapshot_time) > timedelta(retention_days):
            print "Snapshot is older than configured retention of %d days" % (retention_days)
            delete_snapshot(snapshot['SnapshotId'])
        else:
            print "Snapshot is newer than configured retention of %d days so we keep it" % (retention_days)
