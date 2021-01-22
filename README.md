# CSYE7245-Labs


## Requirements

- This requires an Amazon Web Services account to deploy and run. Signup for an AWS Account [here](https://portal.aws.amazon.com/billing/signup#/start).
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


## Repo Contents

#### s3_upload.py

Python script to generate some fake data using Faker and upload to your S3 Bucket 

#### s3_download.py

Download the file of your choice from S3 to your local machine 

#### comprehend_demo.py

Use AWS Compprehend to detect sentiment and extract PII features from your data. Additonal functions can be found here: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html


