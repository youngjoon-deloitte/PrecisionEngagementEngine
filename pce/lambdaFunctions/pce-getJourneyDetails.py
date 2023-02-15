#get all records from a dynamoDB table pce-journeyDetails and pass as a response to the API call

import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('pce-journeyDetails')

def lambda_handler(event, context):
    response = table.scan()
    return {
        'statusCode': 200,
        'body': response['Items']
    }  