import json
import boto3

#variable from the event with campaignID

def lambda_handler(event, context):
    campaignID = event['campaignID']
    #connect to dynamoDB
    dynamodb = boto3.resource('dynamodb')
    #select the table
    table = dynamodb.Table('pce-campaignDetails')
    #query the table for the campaignID
    response = table.get_item(
        Key={
            'campaignID': campaignID
        }
    )
    #return the item
    return response['Item']
    
