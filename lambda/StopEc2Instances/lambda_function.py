import logging
import boto3
logging.basicConfig(level='INFO')

# TODO: break this out into environment variables
REGIONS = ['us-west-2', 'us-east-1']
EXCEPTION_INSTANCES = [
    # 'i-0146...',
]


def stop_instances(region):
    '''
    Stop ALL instances in the given regions.
    '''
    ec2 = boto3.client('ec2', region_name=region)
    insts = ec2.describe_instances()
    insts_stop = []
    for i in insts['Reservations']:
        inst = i['Instances'][0]
        id_ = inst['InstanceId']
        state = inst['State']
        if state['Name'] == 'running' and id_ not in EXCEPTION_INSTANCES:
            insts_stop.append(id_)
    if insts_stop:
        logging.info('Stopping instances {}'.format(insts_stop))
        ec2.stop_instances(InstanceIds=insts_stop)


def lambda_handler(event, context):
    for region in REGIONS:
        stop_instances(region)


if __name__ == "__main__":
    lambda_handler(None, None)
