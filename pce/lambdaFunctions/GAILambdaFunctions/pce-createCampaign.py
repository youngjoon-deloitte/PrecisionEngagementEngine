import boto3  
import json  
import psycopg2  
import os
 
def lambda_handler(event, context):  
    # Extract parameters from event  
    campaign_name = event['campaign_name']  
    description = event['description']  
    message = event['message']  
    message_type = event['message_type']  
    channel = event['channel']  
    start_date = event['start_date']  
    start_time = event['start_time']  
    end_date = event['end_date']  
    end_time = event['end_time']  
    quiet_time_start = event['quiet_time_start']  
    quiet_time_end = event['quiet_time_end']  
    time_zone = event['time_zone']  
      
    # Initialize Pinpoint client  
    pinpoint = boto3.client('pinpoint')  
      
    # Create campaign in Pinpoint  
    response = pinpoint.create_campaign(  
        ApplicationId=os.environ['PINPOINT_APP_ID'],  
        WriteCampaignRequest={  
            'Name': campaign_name,  
            'Description': description,  
            'SegmentId': os.environ['PINPOINT_SEGMENT_ID'],  
            'IsPaused': False,  
            'CampaignEmailMessage': {},  
            'CampaignSmsMessage': {},  
            'MessageConfiguration': {  
                'DefaultMessage': {  
                    'Body': message,  
                    'Substitutions': {}  
                }  
            },  
            'Schedule': {  
                'StartTime': f'{start_date}T{start_time}:00Z',  
                'EndTime': f'{end_date}T{end_time}:00Z',  
                'TimeZone': time_zone,  
                'QuietTime': {  
                    'Start': quiet_time_start,  
                    'End': quiet_time_end  
                }  
            },  
            'TreatmentDescription': '',  
            'TreatmentName': '',  
            'CampaignStatus': 'SCHEDULED',  
            'AdditionalTreatments': [],  
            'CustomDeliveryConfiguration': {},  
            'HoldoutPercent': 0,  
            'IsLocalTime': False,  
            'Limits': {},  
            'QuietTime': {},  
            'StartTime': '',  
            'EndTime': '',  
            'SegmentVersion': 1,  
            'TreatmentSchedule': {}  
        }  
    )  
      
    # Store campaign details in PostgreSQL database  
    conn = psycopg2.connect(  
        host=os.environ['DB_HOST'],  
        database=os.environ['DB_NAME'],  
        user=os.environ['DB_USER'],  
        password=os.environ['DB_PASSWORD']  
    )  
    cur = conn.cursor()  
      
    cur.execute(  
        'INSERT INTO campaigns (name, description, message, message_type, channel, start_date, start_time, end_date, end_time, quiet_time_start, quiet_time_end, time_zone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',  
        (campaign_name, description, message, message_type, channel, start_date, start_time, end_date, end_time, quiet_time_start, quiet_time_end, time_zone)  
    )  
      
    conn.commit()  
    cur.close()  
    conn.close()  
      
    # Return response  
    return {  
        'statusCode': 200,  
        'body': json.dumps(response)  
    }  