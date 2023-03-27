import boto3
import json
import time

#create a lambda function to take event from api gateway that has USER_ID, ITEM_ID, EVENT_TYPE, CAMPAIGN_NAME, LANGUAGE, CHANNEL, PURPOSE and send to personalize with tracking id 4508df20-32c7-4451-974d-3b7b18130dbf

personalize = boto3.client('personalize')

def lambda_handler(event, context):
    print(event)
    #store a variable for current timestamp
    event['SENT_AT'] = str(int(round(time.time() * 1000)))
    personalize.put_events(
        trackingId = '4508df20-32c7-4451-974d-3b7b18130dbf',
        userId = event['USER_ID'],
        sessionId = event['SESSION_ID'],
        eventList = [
            {
                'eventType': event['EVENT_TYPE'],
                #sentAt is current timestamp
                'sentAt': event['SENT_AT'],
                'properties': {
                    'campaignName': event['CAMPAIGN_NAME'],
                    'language': event['LANGUAGE'],
                    'channel': event['CHANNEL'],
                    'purpose': event['PURPOSE']
                }
            }
        ]
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }