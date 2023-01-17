#capture userName attribute from the event payload
#get all records from pce-campaignDetails table where userName = userName

import boto3
import json
import logging
import decimal

def defaultencode(o):
    """
    Function to deserialize decimal data type of dynamoDB
    """
    if isinstance(o, decimal.Decimal):
        return int(float(o))
    raise o

def lambda_handler(event, context):
    header_data = event.get('headers')
    header_origin = {"Access-Control-Allow-Origin": header_data.get('Origin') if header_data.get('Origin') is not None else header_data.get('origin')}
    campaignId = json.loads(event.get("body", None)).get("campaignId")
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('pce-campaignDetails')
    response = table.scan(FilterExpression='campaignId = :val',
                          ExpressionAttributeValues={':val': campaignId})
    return {'statusCode': 200, "headers": header_origin, "multiValueHeaders": {}, "isBase64Encoded": False,
            'body': json.dumps(response['Items'], default=defaultencode)}

