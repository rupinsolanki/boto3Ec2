import boto3

ec2 = boto3.client('ec2')
r = ec2.describe_instances(Filters=[{'Name':'vpc-id','Values':['VPC-ID']}])

for reservation in r['Reservations']:
  for instances in reservation['Instances']:
    if instances['State']['Name'] == 'stopped':
      instance = instances['InstanceId']
      print(instance , 'Instance is stopped')
    else:
      print(instances['InstanceId'], 'Instance is running'
