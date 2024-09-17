# mx_platform_python.TransactionsApi

All URIs are relative to *https://api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_user_guid_accounts_account_guid_transactions_post**](TransactionsApi.md#users_user_guid_accounts_account_guid_transactions_post) | **POST** /users/{user_guid}/accounts/{account_guid}/transactions | Create manual transaction


# **users_user_guid_accounts_account_guid_transactions_post**
> TransactionCreateResponseBody users_user_guid_accounts_account_guid_transactions_post(user_guid, account_guid, transaction_create_request_body)

Create manual transaction

This endpoint can only be used to create manual transactions that are under a manual account. This endpoint accepts the optional MX-Skip-Webhook header and skip_webhook parameter.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.transaction_create_request_body import TransactionCreateRequestBody
from mx_platform_python.models.transaction_create_response_body import TransactionCreateResponseBody
from mx_platform_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mx.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mx_platform_python.Configuration(
    host = "https://api.mx.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = mx_platform_python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_python.TransactionsApi(api_client)
    user_guid = 'user_guid_example' # str | The unique identifier for the user.
    account_guid = 'account_guid_example' # str | The unique identifier for the account.
    transaction_create_request_body = mx_platform_python.TransactionCreateRequestBody() # TransactionCreateRequestBody | 

    try:
        # Create manual transaction
        api_response = api_instance.users_user_guid_accounts_account_guid_transactions_post(user_guid, account_guid, transaction_create_request_body)
        print("The response of TransactionsApi->users_user_guid_accounts_account_guid_transactions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->users_user_guid_accounts_account_guid_transactions_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. | 
 **account_guid** | **str**| The unique identifier for the account. | 
 **transaction_create_request_body** | [**TransactionCreateRequestBody**](TransactionCreateRequestBody.md)|  | 

### Return type

[**TransactionCreateResponseBody**](TransactionCreateResponseBody.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.mx.api.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

