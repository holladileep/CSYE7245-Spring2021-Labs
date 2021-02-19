# CSYE7245
## Big Data Systems & Intelligence Analytics Labs - Spring 2021

- [Course Details](https://wl11gp.neu.edu/udcprod8/bwckctlg.p_disp_course_detail?cat_term_in=201830&subj_code_in=CSYE&crse_numb_in=7245)
- Syllabus: Available on Canvas


### Requirements

- Most labs require an Amazon Web Services account to deploy and run. Signup for an AWS Account [here](https://portal.aws.amazon.com/billing/signup#/start).
- Python 3.7+


### Setup

#### AWS Signup & Configuration 

Sign up for an AWS Account [here](https://portal.aws.amazon.com/billing/signup#/start). Additonally, the AWS Command Line Interface is required to interact with AWS Services. Download AWS CLI from [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)


#### Configuring your AWS CLI 

Download your AWS Access and Secret access keys for your AWS Account. Steps to generate and download your keys can be found [here](https://docs.amazonaws.cn/en_us/IAM/latest/UserGuide/id_credentials_access-keys.html) 


:warning: Never share your access and secret access keys or push them to GitHub<br />


Open command line tool of choice on your machine and run `aws configure`. Enter your access and secret access keys and leave the default region name and output format as null. 

```
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: 
Default output format [None]: json
```

#### Billing Alerts

Set up billing alerts for your AWS Account [here](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html)


### Repo Contents

Refer `README.md` inside the respective directories for setup instructions.

- :white_check_mark: Getting Started with AWS: `aws-basics`
- :white_check_mark: Kafka: `kafka`
- :white_check_mark: Dask: `dask`
- :white_check_mark: Plotly Dash: `plotly-dash`
- :white_check_mark: SQLAlchemy: `sql-alchemy`
- :white_check_mark: FastAPI
- :white_check_mark: Airflow: `airflow_cnn_pipeline`


