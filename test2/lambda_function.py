import json

def lambda_handler(event, context):
    print('code for aws lambda')
    print("value1 = " + event['key1'])
    print("value2 = " + event['key2'])
    # print("value3 = " + event['key3'])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }