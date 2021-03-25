## ML Inference with AWS Lambda, API Gateway & Cognito

This tutorial aims to deploy AutoKeras Image Classification model on Lambda with an API endpoint, secured by `oauth2` using Cognito. 

### Deploying the Lambda function & API endpoint

Create a Python 3.7 Virtual environment - and clone the contents of this repository. Steps to package the Lambda function and deploy the function + API endpoint are outlined in the `tutorial.ipynb` notebook. 

### Securing the Endpoint with Congnito 

#### Step 1: Create AWS Cognito user pool and setup a OAuth application

- Login to AWS Management console and navigate to Cognito service
- Select `Manage your user pools` and click `Create a user pool`
- Enter a pool name and select `Review defaults`. Then select `Create pool`.
- Navigate to `General Settings > App clients` and select `Add an app client`
- Enter a `App client name` and select `Generate client secret` checkbox. Then `Create app client`. Note down the `App client ID` and `App client secret` values displayed in next page.
- Go to `Domain name` and enter your domain name. 
- Go to `Resource Servers` and `Add a resource server`. Enter `Name` and `Identifier`. Add the scopes.
- Go to `App client settings` and you should see the configuration page for new App client. For `Enabled Identity providers`, select `Cognito User pool` checkbox. Then select `Client credentials` checkbox for `Allowed OAuth flows`.
- Now, we have successfully setup a OAuth2 agent in Cognito. 

This CURL command should return an access token, make sure you replace your `App client ID` and your `App Secret ID` in the CURL command.

```
curl -X POST --user <app-client-id>:<app-secret-id> 'https://<your-domain-name>.auth.us-east-1.amazoncognito.com/oauth2/token?grant_type=client_credentials' -H 'Content-Type: application/x-www-form-urlencoded'
```

This should return a token that looks like this:
```
{`access_token`:`eyJraWQiOiJ5eERNZ2NNNERSZUdxUElKUFdoVWJUbk9sXC9yZmlDUlcrR2V3MVo4TU5hRT0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxNTZtbDhyOGZwNjhkbTJicjg4MWo3NjNsayIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoicHJlZGljdC1hcGlcL3ByZWRpY3QiLCJhdXRoX3RpbWUiOjE2MTY1MTc5OTIsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbVwvdXMtZWFzdC0xX1ZNTFFGMVo3cyIsImV4cCI6MTYxNjUyMTU5MiwiaWF0IjoxNjE2NTE3OTkyLCJ2ZXJzaW9uIjoyLCJqdGkiOiIwOGE1MGUyNC04YTBhLTRiMTQtYTUwOS1mNjJiN2IyY2ZkNGMiLCJjbGllbnRfaWQiOiIxNTZtbDhyOGZwNjhkbTJicjg4MWo3NjNsayJ9.KRD7PanfyReSp-OcSJKatBphvWbIVF9xVtGByMJu22tGhZRHYP_L9m33QO9UHoRaTbNWIc6_GQFNYKYNNvC4BmII39-6kl1u2WtAXDElFPrPtnMNKBexNeLBk_IlEwOnOvdFyJ4oGauPuIwNE59HsNWU7DcfvPL7XqmQmNpS7yVwu7nT85L3QzqOvMGnGRii_N0OAQgczOMT6riRd866dZgHV6nQD1InkXMlvsnVFkXjJ509KGcRPttH3lbBHBM6wfakdeotUIoRH2Sgii5XoC5TWG3g5k6dKsq6-Zkvc8G5LPlWtSxxW7vLm-cId78pzUhaBsbk-TkQ_wz4ocLclQ`,`expires_in`:3600,`token_type`:`Bearer`}
```

#### Step 2: Add Authentication to Deployed Function & API Endpoint 

- Open API Gateway and open the newly created API
- Navigate to `Resources` in API_Cognito configuration. You will see only one method `ANY` below the API which means it accepts all HTTP methods.
- Select `ANY` and then `Actions > Delete Method`
- Select the API and then `Actions > Create Method`. Select `POST` and click the tick mark to add it. In the Setup screen, select `Use Lambda Proxy Integration` checkbox and enter the name of Lambda Function. On clicking `Save`, it will show a prompt for permissions and click OK.
- Go to `Amazon API Gateway > Authorizers` and `Create new Authorizer`. Enter a Name and select user pool which was created in Step 1. Also, enter `Token Source` as `Authorization` header.
- Go to `Resources` and select `GET` method. Select `Method Request` configuration on right pane.
- Select the newly crreated authorizer in `Authorization` drop-down. That should automatically add a new field `OAuth Scopes`. Enter the scopes created earlier.
- Select `Actions > Deploy API` and select `Deployment stage` as `dev`. This should deploy the latest changes in these APIs.

#### Step3: Test

- Get access_token from Cognito

```
curl -X POST --user <app-client-id>:<app-secret-id> 'https://<your-domain-name>.auth.us-east-1.amazoncognito.com/oauth2/token?grant_type=client_credentials' -H 'Content-Type: application/x-www-form-urlencoded'
```

- Now we can invoke the Lambda function with the Authorization token and get the results 

```
!curl -X POST '<Your-API-Endpoint' -H 'Content-Type: image/png' --data-binary @'test_images/0.png' -H 'Authorization: <your-auth-token>'
```

### References & Citation

[Serverless ML Inferencing with TensorFlow Lite and AWS Lambda](https://dev.to/sandeepmistry/serverless-ml-inferencing-with-aws-lambda-and-tensorflow-lite-15el) <br/>
[Securing API Gateway with Cognito](https://awskarthik82.medium.com/part-1-securing-aws-api-gateway-using-aws-cognito-oauth2-scopes-410e7fb4a4c0)