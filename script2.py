# In this script I am using boto3 package for listing all ec2 instances. 

import boto3

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
  print(instance.id)  # here I am printing instance ID.
  print(instance.tags[0].value)  # here I am printing the instance name. 
  
 

