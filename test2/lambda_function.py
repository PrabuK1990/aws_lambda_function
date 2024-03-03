import json

def lambda_handler(event, context):
    print('aws started')
    print('hello')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }