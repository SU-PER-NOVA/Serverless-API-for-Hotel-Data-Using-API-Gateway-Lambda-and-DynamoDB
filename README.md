# Serverless-API-for-Hotel-Data-Using-API-Gateway-Lambda-and-DynamoDB

Components
DynamoDB: Backend database for storing hotel booking data.
Lambda: Acts as the web server to process requests.
API Gateway: Serves as the frontend to handle API requests and route them to Lambda.
Project Workflow
When a customer accesses the application, the request is sent to API Gateway. API Gateway then forwards the request to a Lambda function, which processes the information entered by the customer and stores it in the DynamoDB table.

Steps to Create the Project
1. Create IAM Role for Lambda Function
Create an IAM role that allows the Lambda function to write data to the DynamoDB table.
Attach the following policies to the IAM role:
AWSLambdaBasicExecutionRole: Provides permissions to write logs.
AmazonDynamoDBFullAccess: Allows full access to DynamoDB.

3. Create Lambda Function
Create a Lambda function named karanfn.
Attach the IAM role created in the previous step.
Upload the following files to the Lambda function:
lambda_function.py: Contains the Python code to handle POST requests, interact with DynamoDB, and generate HTML responses for GET requests.
contactus.html: Frontend HTML code for the hotel booking form.
success.html: HTML code for the success page displayed after a successful booking.

3. Create DynamoDB Table
Create a DynamoDB table named karantable.
Set aadhar as the primary key.
4. Configure API Gateway
Create a new REST API for complete control over request and response handling.
Add two methods:
GET for serving the HTML form.
POST for handling form submissions.
Configure both methods to use the Lambda function karanfn.
Enable CORS for both methods to handle cross-origin requests.
Deploy the API and obtain the invoke URL.
CORS Configuration
Enable CORS on the API Gateway methods:
In the API Gateway console, go to the Stages section and select your deployment stage.
For each method (GET and POST), configure CORS headers in the Method Response and Integration Response sections.
Deploy and Test
Deploy the API Gateway.
Test the GET request to ensure the HTML form is served correctly.
Test the POST request to ensure data is correctly written to the DynamoDB table.
Invoke URL
The deployed API can be accessed at:
https://giu9eobrzc.execute-api.ap-south-1.amazonaws.com/dev
