# Automate snapshots for specific server volumes

import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Specify volumes, separated by commas
    result = ec2.describe_volumes( VolumeIds=[
        #'vol-#########',
        #'vol-#########',
        # etc.
        ]
    )
    
    for volume in result['Volumes']:
        print "Backing up %s in %s" % (volume['VolumeId'], volume['AvailabilityZone'])
        
        # Create snapshot
        result = ec2.create_snapshot(VolumeId=volume['VolumeId'],Description='Created by Lambda backup function ebs-backup')
        
        # Get snapshot resource
        # Don't forget to specify the region name 
        ec2resource = boto3.resource('ec2', region_name='us-east-1')
        snapshot = ec2resource.Snapshot(result['SnapshotId'])
        
        volumename = 'N/A'
        
        # Find name tag for volume if it exists
        if 'Tags' in volume:
            for tags in volume['Tags']:
                if tags["Key"] == 'Name':
                    volumename = tags["Value"]
        
        # Add volume name to snapshot for easier identification
        snapshot.create_tags(Tags=[{'Key': 'Name','Value': volumename}])

