# mx_platform_python.MonthlyCashFlowProfileApi

All URIs are relative to *https://int-api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**read_monthly_cash_flow_profile**](MonthlyCashFlowProfileApi.md#read_monthly_cash_flow_profile) | **GET** /users/{user_guid}/monthly_cash_flow_profile | Read monthly cash flow profile
[**update_monthly_cash_flow_profile**](MonthlyCashFlowProfileApi.md#update_monthly_cash_flow_profile) | **PUT** /users/{user_guid}/monthly_cash_flow_profile | Update monthly cash flow profile


# **read_monthly_cash_flow_profile**
> MonthlyCashFlowResponseBody read_monthly_cash_flow_profile(user_guid)

Read monthly cash flow profile

Read monthly cash flow profile.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.monthly_cash_flow_response_body import MonthlyCashFlowResponseBody
from mx_platform_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://int-api.mx.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mx_platform_python.Configuration(
    host = "https://int-api.mx.com"
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
    api_instance = mx_platform_python.MonthlyCashFlowProfileApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Read monthly cash flow profile
        api_response = api_instance.read_monthly_cash_flow_profile(user_guid)
        print("The response of MonthlyCashFlowProfileApi->read_monthly_cash_flow_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonthlyCashFlowProfileApi->read_monthly_cash_flow_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 

### Return type

[**MonthlyCashFlowResponseBody**](MonthlyCashFlowResponseBody.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_monthly_cash_flow_profile**
> MonthlyCashFlowResponseBody update_monthly_cash_flow_profile(user_guid, monthly_cash_flow_profile_request_body)

Update monthly cash flow profile

Use this endpoint to update the attributes of a `monthly_cash_flow_profile`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.monthly_cash_flow_profile_request_body import MonthlyCashFlowProfileRequestBody
from mx_platform_python.models.monthly_cash_flow_response_body import MonthlyCashFlowResponseBody
from mx_platform_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://int-api.mx.com
# See configuration.py for a list of all supported configuration parameters.
configuration = mx_platform_python.Configuration(
    host = "https://int-api.mx.com"
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
    api_instance = mx_platform_python.MonthlyCashFlowProfileApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    monthly_cash_flow_profile_request_body = mx_platform_python.MonthlyCashFlowProfileRequestBody() # MonthlyCashFlowProfileRequestBody | 

    try:
        # Update monthly cash flow profile
        api_response = api_instance.update_monthly_cash_flow_profile(user_guid, monthly_cash_flow_profile_request_body)
        print("The response of MonthlyCashFlowProfileApi->update_monthly_cash_flow_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonthlyCashFlowProfileApi->update_monthly_cash_flow_profile: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **monthly_cash_flow_profile_request_body** | [**MonthlyCashFlowProfileRequestBody**](MonthlyCashFlowProfileRequestBody.md)|  | 

### Return type

[**MonthlyCashFlowResponseBody**](MonthlyCashFlowResponseBody.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

