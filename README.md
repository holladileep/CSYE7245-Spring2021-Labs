# CSYE7245-Labs


## Requirements

- Most labs require an Amazon Web Services account to deploy and run. Signup for an AWS Account [here](https://portal.aws.amazon.com/billing/signup#/start).
- Python 3.7+


## Setup

### AWS Signup & Configuration 

Sign up for an AWS Account [here](https://portal.aws.amazon.com/billing/signup#/start). Additonally, the AWS Command Line Interface is required to interact with AWS Services. Download AWS CLI from [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)


### Configuring your AWS CLI 

Download your AWS Access and Secret access keys for your AWS Account. Steps to generate and download your keys can be found [here](https://docs.amazonaws.cn/en_us/IAM/latest/UserGuide/id_credentials_access-keys.html) 


> :warning: Never share your access and secret access keys or push them to GitHub<br />


Open command line tool of choice on your machine and run `aws configure`. Enter your access and secret access keys and leave the default region name and output format as null. 

```
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: 
Default output format [None]: json
```

### Billing Alerts

Set up billing alerts for your AWS Account [here](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html)


## Repo Contents

### Lab 1 - Getting Started with AWS

#### Requirements

```
pip3 install Faker
pip3 install boto3
```

#### Contents

- `s3_upload.py` - Python script to generate some fake data using Faker and upload to your S3 Bucket 
- `s3_download.py` - Download the file of your choice from S3 to your local environemnt 
- `comprehend_demo.py` - Use AWS Comprehend to detect sentiment and extract PII features from your data. Additonal APIs can be found [here](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html)
- Lambda Functions - Deploying Lambda functions using Python Lambda. Documentation and boilerplate code is available on [this repository](https://github.com/holladileep/lambda-serverless-py) 


### Lab 2 - FastAPI

#### What is FastAPI? 

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

#### Requirements

```
pip3 install fastapi
pip3 install uvicorn
pip3 install iexfinance
```

#### Getting Started

Basic usage is available in `main.py`. Run the server with `uvicorn main:app --reload`. Go to `http://127.0.0.1:8000/docs` and you should see the interactive API documentation. This is a simple example that demonstrates the created API that can: 

- Receives HTTP requests in the paths / and /items/{item_id}.
- Both paths take GET operations (also known as HTTP methods).
- The path /items/{item_id} has a path parameter item_id that should be an int.
- The path /items/{item_id} has an optional str query parameter q
- By Clicking on the "Execute" button on the API interface, the user interface will communicate with your API, send the parameters, get the results and show them on the screen

#### Level UP! :arrow_up:

Let's work with an API that would potentially be used by a brokerage to keep a track of investors buying and selling on the stock-market, using their website/app. In addition to serving `PUT` and `GET` requests, the endpoint stores all data on DynamoDB. Create a table on DynamoDB with `id` as the primary key before running the server.

- `stock_price.py` - A simple Python script to get the current stock price of a given company. This requires an API token to query IEX Cloud and fetch the current stock price. Create a free developer account [here](https://iexcloud.io/). Once you have the account, go to `Home > API Tokens` and copy the `SECRET` token, and use your token in the `stock_price.py` script. 

> :warning: Do not share your API token or push it to GitHub with your source code<br />


- `id_generator.py` - Python script to generate a unique 10 digit alpha-numeric ID

- `trades.py` - Script to deploy the FastAPI endpoint. Use the created DynamoDB table in this script. Contains three routes:


Fetch the price of a given stock:
```
# Get the current stock price
@app.get("/stock_price/{name}")
```

Place Trades - Required params: `customer_id, name, qty, position`

```
# Place trades
@app.put("/trade/{customer_id}")
```

Get all trades for a given customer ID - Required params: `customer_id`
```
@app.get("/get_trades/{customer_id}")
```

Run the server with `uvicorn trades:app --reload`. Go to `http://127.0.0.1:8000/docs` and you should see the interactive API documentation.

