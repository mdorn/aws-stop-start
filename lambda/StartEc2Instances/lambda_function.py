import logging
import boto3
logging.basicConfig(level='INFO')

# TODO: break this out into environment variables
INSTANCES = {
    'us-west-2': [],
    'us-east-1': [
        # 'i-014...',
    ]
}


def start_instances(region, instances):
    '''
    Start specified EC2 instances in the given region
    '''
    ec2 = boto3.client('ec2', region_name=region)
    if instances:
        logging.info('Starting instances {}'.format(instances))
        try:
            ec2.start_instances(InstanceIds=instances)
        except Exception as exc:
            logging.error(exc)


def lambda_handler(event, context):
    for region in INSTANCES.keys():
        start_instances(region, INSTANCES[region])

if __name__ == "__main__":
    lambda_handler(None, None)
