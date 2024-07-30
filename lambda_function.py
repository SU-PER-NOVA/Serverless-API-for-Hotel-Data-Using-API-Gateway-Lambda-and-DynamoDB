import json
import boto3
from urllib.parse import parse_qs

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ktable')

def lambda_handler(event, context):
    try:
        http_method = event['httpMethod']
        if http_method == 'GET':
            return serve_html('contactus.html')
        elif http_method == 'POST':
            form_data = parse_qs(event['body'])
            insert_record(form_data)
            return {
                'statusCode': 200,
                'headers': {
                    "Content-Type": "text/html",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
                    "Access-Control-Allow-Methods": "OPTIONS,POST"
                },
                'body': '<html><body><h2>Thank you for booking. You can verify the data in the DynamoDB table.</h2></body></html>'
            }
        else:
            return {
                'statusCode': 405,
                'headers': {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
                    "Access-Control-Allow-Methods": "OPTIONS,POST"
                },
                'body': json.dumps({'error': 'Method not allowed'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            'body': json.dumps({'error': str(e)})
        }

def serve_html(file_name):
    try:
        with open(file_name, 'r') as html_file:
            html_content = html_file.read()
        return {
            'statusCode': 200,
            'headers': {
                "Content-Type": "text/html",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            'body': html_content
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            'body': json.dumps({'error': str(e)})
        }

def insert_record(form_data):
    item = {
        'Name': form_data['name'][0],
        'aadhar': form_data['aadhar'][0],  # Ensure this matches the form field name 'aadhar'
        'Days': int(form_data['days'][0]),
        'RoomType': form_data['roomType'][0]
    }
    table.put_item(Item=item)
