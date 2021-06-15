An AWS CloudFormation template to automate starting and stopping of EC2 instances, e.g. to allow them to run only during business hours.  Python code found in `lambda` directory.

Template expects code to be located in a zipped file at a specified S3 location.  To prepare the code for this, e.g.:

    cd lambda/StartEc2Instances
    zip aws_ec2_start_deploy.zip lambda_function.py
