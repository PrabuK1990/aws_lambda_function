import json

def lambda_handler(event, context):
    print('aws started')
    print('hello')
    print('Prabu')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }