# mx_platform_python.VerifiableCredentialsApi

All URIs are relative to *https://int-api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounts_data**](VerifiableCredentialsApi.md#get_accounts_data) | **GET** /vc/users/{user_guid}/members/{member_guid}/accounts | Get Accounts Data
[**get_identity_data**](VerifiableCredentialsApi.md#get_identity_data) | **GET** /vc/users/{user_guid}/members/{member_guid}/customers | Get Identity Data
[**get_transactions_data**](VerifiableCredentialsApi.md#get_transactions_data) | **GET** /vc/users/{user_guid}/accounts/{account_guid}/transactions | Get Transactions Data


# **get_accounts_data**
> VCResponse get_accounts_data(user_guid, member_guid)

Get Accounts Data

Get an MX-issued verifiable credential of a user's accounts data.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.vc_response import VCResponse
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
    api_instance = mx_platform_python.VerifiableCredentialsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.

    try:
        # Get Accounts Data
        api_response = api_instance.get_accounts_data(user_guid, member_guid)
        print("The response of VerifiableCredentialsApi->get_accounts_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerifiableCredentialsApi->get_accounts_data: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 

### Return type

[**VCResponse**](VCResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.mx.api.v2beta+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_data**
> VCResponse get_identity_data(user_guid, member_guid)

Get Identity Data

Get an MX-issued verifiable credential of a user's identity data.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.vc_response import VCResponse
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
    api_instance = mx_platform_python.VerifiableCredentialsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.

    try:
        # Get Identity Data
        api_response = api_instance.get_identity_data(user_guid, member_guid)
        print("The response of VerifiableCredentialsApi->get_identity_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerifiableCredentialsApi->get_identity_data: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 

### Return type

[**VCResponse**](VCResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.mx.api.v2beta+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_data**
> VCResponse get_transactions_data(user_guid, account_guid, start_time=start_time, end_time=end_time)

Get Transactions Data

Get an MX-issued verifiable credential of a user's transaction data.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.vc_response import VCResponse
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
    api_instance = mx_platform_python.VerifiableCredentialsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    start_time = '2015-09-20' # str | Filter transactions from this date. Must be in the format YYYY-MM-DD. The range is limited to 1 year. (optional)
    end_time = '2015-09-20' # str | Filter transactions to this date. Must be in the format YYYY-MM-DD. The range is limited to 1 year. (optional)

    try:
        # Get Transactions Data
        api_response = api_instance.get_transactions_data(user_guid, account_guid, start_time=start_time, end_time=end_time)
        print("The response of VerifiableCredentialsApi->get_transactions_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VerifiableCredentialsApi->get_transactions_data: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **start_time** | **str**| Filter transactions from this date. Must be in the format YYYY-MM-DD. The range is limited to 1 year. | [optional] 
 **end_time** | **str**| Filter transactions to this date. Must be in the format YYYY-MM-DD. The range is limited to 1 year. | [optional] 

### Return type

[**VCResponse**](VCResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.mx.api.v2beta+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

