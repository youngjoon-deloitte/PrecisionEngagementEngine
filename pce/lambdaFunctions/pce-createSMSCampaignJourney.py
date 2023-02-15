import json
import boto3
import logging
import os
import calendar
from datetime import datetime, timedelta

# Setting Logger Level to INFO
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Get Pinpoint and Personalize boto3 API's
pinpoint = boto3.client("pinpoint")

# Get Environment Variables
ApplicationName = os.environ["ApplicationName"]
ApplicationId = os.environ["ApplicationId"]


def create_journey(deliveryUri, data, eventType, journeyName):

    response = pinpoint.create_journey(
        ApplicationId=ApplicationId,
        WriteJourneyRequest={
            "Activities": {
                "Journey1": {
                    "CUSTOM": {
                        "DeliveryUri": DeliveryUri,
                        "EndpointTypes": [
                            "SMS",
                        ],
                        "MessageConfig": {"Data": Data},
                        "NextActivity": "MultiCondition1",
                        # 'TemplateName': 'string',
                        # 'TemplateVersion': 'string'
                    }
                },
                "MultiCondition1": {
                    "MultiCondition": {
                        "Branches": [
                            {
                                "Condition": {
                                    "SegmentCondition": {
                                        "SegmentId": CohortSegment1
                                    }
                                },
                                "NextActivity": "MultiCondition2",
                            },
                            {
                                "Condition": {
                                    "SegmentCondition": {
                                        "SegmentId": CohortSegment2
                                    }
                                },
                                "NextActivity": "MultiCondition3",
                            },
                            {
                                "Condition": {
                                    "SegmentCondition": {
                                        "SegmentId": CohortSegment3
                                    }
                                },
                                "NextActivity": "MultiCondition4",
                            },
                            {
                                "Condition": {
                                    "SegmentCondition": {
                                        "SegmentId": CohortSegment4A
                                    }
                                },
                                "NextActivity": "MultiCondition5",
                            },
                        ],
                        "DefaultActivity": "MultiCondition6",
                    }
                },
                "MultiCondition2": {
                    "MultiCondition": {
                        "Branches": [
                            {
                                "Condition": {
                                    "SegmentCondition": {
                                        "SegmentId": MonthSegment1
                                    }
                                },
                                "NextActivity": "Cohort1Month1",
                            },
                            {
                                "Condition": {
                                    "SegmentCondition": {
                                        "SegmentId": MonthSegment2
                                    }
                                },
                                "NextActivity": "Cohort1Month2",
                            },
                            {
                                "Condition": {
                                    "SegmentCondition": {
                                        "SegmentId": MonthSegment3
                                    }
                                },
                                "NextActivity": "Cohort1Month3",
                            },
                        ],
                    }
                },
                "MultiCondition3": {
                    "MultiCondition": {
                        "Branches": [
                            {
                                "Condition": {
                                    "SegmentCondition": {
                                        "SegmentId": MonthSegment1
                                    }
                                },
                                "NextActivity": "Cohort2Month1",
                            },
                            {
                                "Condition": {
                                    "SegmentCondition": {
                                        "SegmentId": MonthSegment2
                                    }
                                },
                                "NextActivity": "Cohort2Month2",
                            },
                            {
                                "Condition": {
                                    "SegmentCondition": {
                                        "SegmentId": MonthSegment3
                                    }
                                },
                                "NextActivity": "Cohort2Month3",
                            },
                        ],
                    }
                },
                "MultiCondition4": {
                    "MultiCondition": {
                        "Branches": [
                            {
                                "Condition": {
                                    "SegmentCondition": {
                                        "SegmentId": MonthSegment1
                                    }
                                },
                                "NextActivity": "Cohort3Month1",
                            },
                            {
                                "Condition": {
                                    "SegmentCondition": {
                                        "SegmentId": MonthSegment2
                                    }
                                },
                                "NextActivity": "Cohort3Month2",
                            },
                            {
                                "Condition": {
                                    "SegmentCondition": {
                                        "SegmentId": MonthSegment3
                                    }
                                },
                                "NextActivity": "Cohort3Month3",
                            },
                        ],
                    }
                },
                "MultiCondition5": {
                    "MultiCondition": {
                        "Branches": [
                            {
                                "Condition": {
                                    "SegmentCondition": {
                                        "SegmentId": MonthSegment1
                                    }
                                },
                                "NextActivity": "Cohort4AMonth1",
                            },
                            {
                                "Condition": {
                                    "SegmentCondition": {
                                        "SegmentId": MonthSegment2
                                    }
                                },
                                "NextActivity": "Cohort4AMonth2",
                            },
                            {
                                "Condition": {
                                    "SegmentCondition": {
                                        "SegmentId": MonthSegment3
                                    }
                                },
                                "NextActivity": "Cohort4AMonth3",
                            },
                        ],
                    }
                },
                "MultiCondition6": {
                    "MultiCondition": {
                        "Branches": [
                            {
                                "Condition": {
                                    "SegmentCondition": {
                                        "SegmentId": MonthSegment1
                                    }
                                },
                                "NextActivity": "Cohort4BMonth1",
                            },
                            {
                                "Condition": {
                                    "SegmentCondition": {
                                        "SegmentId": MonthSegment2
                                    }
                                },
                                "NextActivity": "Cohort4BMonth2",
                            },
                            {
                                "Condition": {
                                    "SegmentCondition": {
                                        "SegmentId": MonthSegment3
                                    }
                                },
                                "NextActivity": "Cohort4BMonth3",
                            },
                        ],
                    }
                },
                "Cohort1Month1": {
                    "CUSTOM": {
                        "DeliveryUri": "arn:aws:lambda:us-east-1:238731313807:function:LIER_Send_SMS",
                        "EndpointTypes": [
                            "SMS",
                        ],
                        "MessageConfig": {"Data": "C1_M1"}
                        #'NextActivity': 'GetResponse',
                    }
                },
                "Cohort1Month2": {
                    "CUSTOM": {
                        "DeliveryUri": "arn:aws:lambda:us-east-1:238731313807:function:LIER_Send_SMS",
                        "EndpointTypes": [
                            "SMS",
                        ],
                        "MessageConfig": {"Data": "C1_M2"}
                        #'NextActivity': 'GetResponse',
                    }
                },
                "Cohort1Month3": {
                    "CUSTOM": {
                        "DeliveryUri": "arn:aws:lambda:us-east-1:238731313807:function:LIER_Send_SMS",
                        "EndpointTypes": [
                            "SMS",
                        ],
                        "MessageConfig": {"Data": "C1_M3"}
                        #'NextActivity': 'GetResponse',
                    }
                },
                "Cohort2Month1": {
                    "CUSTOM": {
                        "DeliveryUri": "arn:aws:lambda:us-east-1:238731313807:function:LIER_Send_SMS",
                        "EndpointTypes": [
                            "SMS",
                        ],
                        "MessageConfig": {"Data": "C2_M1"}
                        #'NextActivity': 'GetResponse',
                    }
                },
                "Cohort2Month2": {
                    "CUSTOM": {
                        "DeliveryUri": "arn:aws:lambda:us-east-1:238731313807:function:LIER_Send_SMS",
                        "EndpointTypes": [
                            "SMS",
                        ],
                        "MessageConfig": {"Data": "C2_M2"}
                        #'NextActivity': 'GetResponse',
                    }
                },
                "Cohort2Month3": {
                    "CUSTOM": {
                        "DeliveryUri": "arn:aws:lambda:us-east-1:238731313807:function:LIER_Send_SMS",
                        "EndpointTypes": [
                            "SMS",
                        ],
                        "MessageConfig": {"Data": "C2_M3"}
                        #'NextActivity': 'GetResponse',
                    }
                },
                "Cohort3Month1": {
                    "CUSTOM": {
                        "DeliveryUri": "arn:aws:lambda:us-east-1:238731313807:function:LIER_Send_SMS",
                        "EndpointTypes": [
                            "SMS",
                        ],
                        "MessageConfig": {"Data": "C3_M1"}
                        #'NextActivity': 'GetResponse',
                    }
                },
                "Cohort3Month2": {
                    "CUSTOM": {
                        "DeliveryUri": "arn:aws:lambda:us-east-1:238731313807:function:LIER_Send_SMS",
                        "EndpointTypes": [
                            "SMS",
                        ],
                        "MessageConfig": {"Data": "C3_M2"}
                        #'NextActivity': 'GetResponse',
                    }
                },
                "Cohort3Month3": {
                    "CUSTOM": {
                        "DeliveryUri": "arn:aws:lambda:us-east-1:238731313807:function:LIER_Send_SMS",
                        "EndpointTypes": [
                            "SMS",
                        ],
                        "MessageConfig": {"Data": "C3_M3"}
                        #'NextActivity': 'GetResponse',
                    }
                },
                "Cohort4AMonth1": {
                    "CUSTOM": {
                        "DeliveryUri": "arn:aws:lambda:us-east-1:238731313807:function:LIER_Send_SMS",
                        "EndpointTypes": [
                            "SMS",
                        ],
                        "MessageConfig": {"Data": "C4A_M1"}
                        #'NextActivity': 'GetResponse',
                    }
                },
                "Cohort4AMonth2": {
                    "CUSTOM": {
                        "DeliveryUri": "arn:aws:lambda:us-east-1:238731313807:function:LIER_Send_SMS",
                        "EndpointTypes": [
                            "SMS",
                        ],
                        "MessageConfig": {"Data": "C4A_M2"}
                        #'NextActivity': 'GetResponse',
                    }
                },
                "Cohort4AMonth3": {
                    "CUSTOM": {
                        "DeliveryUri": "arn:aws:lambda:us-east-1:238731313807:function:LIER_Send_SMS",
                        "EndpointTypes": [
                            "SMS",
                        ],
                        "MessageConfig": {"Data": "C4A_M3"}
                        #'NextActivity': 'GetResponse',
                    }
                },
                "Cohort4BMonth1": {
                    "CUSTOM": {
                        "DeliveryUri": "arn:aws:lambda:us-east-1:238731313807:function:LIER_Send_SMS",
                        "EndpointTypes": [
                            "SMS",
                        ],
                        "MessageConfig": {"Data": "C4B_M1"}
                        #'NextActivity': 'GetResponse',
                    }
                },
                "Cohort4BMonth2": {
                    "CUSTOM": {
                        "DeliveryUri": "arn:aws:lambda:us-east-1:238731313807:function:LIER_Send_SMS",
                        "EndpointTypes": [
                            "SMS",
                        ],
                        "MessageConfig": {"Data": "C4B_M2"}
                        #'NextActivity': 'GetResponse',
                    }
                },
                "Cohort4BMonth3": {
                    "CUSTOM": {
                        "DeliveryUri": "arn:aws:lambda:us-east-1:238731313807:function:LIER_Send_SMS",
                        "EndpointTypes": [
                            "SMS",
                        ],
                        "MessageConfig": {"Data": "C4B_M3"}
                        #'NextActivity': 'GetResponse',
                    }
                },
            },
            "StartCondition": {
                "EventStartCondition": {
                    "EventFilter": {
                        "Dimensions": {
                            "EventType": {
                                "DimensionType": "INCLUSIVE",
                                "Values": [Values],
                            }
                        },
                        "FilterType": "ENDPOINT",
                    }
                }
            },
            "Name": Name,
            "Schedule": {
                "EndTime": datetime(2024,1,1),
                "StartTime": datetime.now() + timedelta(minutes = 5),
                "Timezone": 'UTC'
            },
            'State': 'ACTIVE',
            "StartActivity": "Journey1",
            #     'SegmentStartCondition': {
            #         'SegmentId': '89be914a73c24580aedcc8402f167d52'
            #   },
            "WaitForQuietTime": False,
        },
    )


def lambda_handler(event, context):

    # Create Journey
    create_journey(
        deliveryUri="arn:aws:lambda:us-east-1:238731313807:function:LIER_Send_SMS",
        data="Welcome_Message",
        eventType="User.Lier",
        journeyName="Lier_Journey_test",
    )

    return "Success"


# def create_journey(DeliveryUri,Data,Values,Name,):

#     Journey = pinpoint.create_journey(
#         ApplicationId = ApplicationId,
#         WriteJourneyRequest={
#             'Activities': {
#                 'Journey1': {
#                     'CUSTOM': {
#                         'DeliveryUri': DeliveryUri,
#                         'EndpointTypes': [
#                             'SMS',
#                         ],
#                         'MessageConfig': {
#                             'Data': Data
#                         },
#                         'NextActivity': 'MultiCondition'
#                         # 'TemplateName': 'string',
#                         # 'TemplateVersion': 'string'
#                         },
#                     'MultiCondition': {
#                         'Branches': [
#                          {
#                              'NextActivity': 'Cohort1_segment',
#                              #'Percentage': 25
#                          },
#                           {
#                              'NextActivity': 'Cohort2_segment',
#                              #'Percentage': 25
#                         },
#                         #   {
#                         #      'NextActivity': 'Cohort3_segment',
#                         #      #'Percentage': 25
#                         #  },
#                         #   {
#                         #      'NextActivity': 'Cohort4A_segment',
#                         #      #'Percentage': 25
#                         #  }
#                      ]
#                      } ,

#                     'Cohort1_segment': {
#                         'MultiCondition': {
#                             'Branches': [
#                              {
#                                  'SegmentCondition': {
#                                     'SegmentId': '19587b4b1b3b41ebb8753432d72cffb8'
#                                 },
#                                  #'Percentage': 25
#                              },
#                               {
#                                  'SegmentCondition': {
#                                     'SegmentId': 'b00c03c900cd45de9bcc1d340b9b7951'
#                                 }
#                             }

#                          ]
#                          }
#                         },

#                     'Cohort2_segment': {
#                          'MultiCondition': {
#                             'Branches': [
#                             {
#                                  'SegmentCondition': {
#                                     'SegmentId': '19587b4b1b3b41ebb8753432d72cffb8'
#                                 },
#                                  #'Percentage': 25
#                              },
#                               {
#                                  'SegmentCondition': {
#                                     'SegmentId': 'b00c03c900cd45de9bcc1d340b9b7951'
#                                 }
#                             }


#                          ]
#                          }
#                         },

#                     # 'Cohort3_segment': {
#                     #   'MultiCondition': {
#                     #         'Branches': [
#                     #          {
#                     #              'NextActivity': 'Month1_segment',
#                     #              #'Percentage': 25
#                     #          },
#                     #           {
#                     #              'NextActivity': 'Month2_segment',
#                     #              #'Percentage': 25
#                     #         },
#                     #           {
#                     #              'NextActivity': 'Month3_segment',
#                     #              #'Percentage': 25
#                     #          },

#                     #      ]
#                     #         }
#                     #     },

#                     # 'Cohort4A_segment': {
#                     #      'MultiCondition': {
#                     #         'Branches': [
#                     #          {
#                     #              'NextActivity': 'Month1_segment',
#                     #              #'Percentage': 25
#                     #          },
#                     #           {
#                     #              'NextActivity': 'Month2_segment',
#                     #              #'Percentage': 25
#                     #         },
#                     #           {
#                     #              'NextActivity': 'Month3_segment',
#                     #              #'Percentage': 25
#                     #          },

#                     #      ]
#                     #         }
#                     #     },
#             'StartCondition': {
#                      'EventStartCondition': {
#                          'EventFilter': {
#                              'Dimensions': {
#                                  'EventType': {
#                                      'DimensionType': 'INCLUSIVE',
#                                      'Values': [
#                                          Values
#                                 ]
#                             }
#                         },
#                         'FilterType': 'ENDPOINT'
#                     }
#                 }
#             }
#             }
#             },
#             'Name': Name,
#             'QuietTime': {
#                 'End': '08:00',
#                 'Start': '22:00'
#             },
#             'StartActivity': 'Journey1',
#             'State': 'DRAFT',
#             'WaitForQuietTime': False
#             }

#             )
