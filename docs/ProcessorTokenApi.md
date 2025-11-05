# mx_platform_python.ProcessorTokenApi

All URIs are relative to *https://int-api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_real_time_account_balance**](ProcessorTokenApi.md#check_real_time_account_balance) | **POST** /account/check_balance | Check Real Time Account Balance (Processors Only)
[**deprecated_request_payment_processor_authorization_code**](ProcessorTokenApi.md#deprecated_request_payment_processor_authorization_code) | **POST** /payment_processor_authorization_code | (Deprecated) Request an authorization code
[**get_account_owner_info**](ProcessorTokenApi.md#get_account_owner_info) | **GET** /account/transactions | Get account owner information (Processors Only)
[**list_tokens**](ProcessorTokenApi.md#list_tokens) | **GET** /tokens | View a List of Tokens
[**read_account_balance**](ProcessorTokenApi.md#read_account_balance) | **GET** /payment_account | Read the account balance (Processors Only)
[**request_account_number**](ProcessorTokenApi.md#request_account_number) | **GET** /account/account_numbers | Request an account number (Processors Only)
[**request_authorization_code**](ProcessorTokenApi.md#request_authorization_code) | **POST** /authorization_code | Request an authorization code


# **check_real_time_account_balance**
> MemberResponseBody check_real_time_account_balance()

Check Real Time Account Balance (Processors Only)

Check the real-time account balance using your access token.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.member_response_body import MemberResponseBody
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

# Configure Bearer authorization: bearerAuth
configuration = mx_platform_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_python.ProcessorTokenApi(api_client)

    try:
        # Check Real Time Account Balance (Processors Only)
        api_response = api_instance.check_real_time_account_balance()
        print("The response of ProcessorTokenApi->check_real_time_account_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessorTokenApi->check_real_time_account_balance: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**MemberResponseBody**](MemberResponseBody.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deprecated_request_payment_processor_authorization_code**
> PaymentProcessorAuthorizationCodeResponseBody deprecated_request_payment_processor_authorization_code(payment_processor_authorization_code_request_body)

(Deprecated) Request an authorization code

(This endpoint is deprecated. Clients should use `/authorization_code`.) Clients use this endpoint to request an authorization_code according to a user, member, and account specified in the request body. Clients then pass this code to processors. Processor access is scoped only to the user/member/account specified in this request. Before requesting an authorization_code, clients must have verified the specified member.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.payment_processor_authorization_code_request_body import PaymentProcessorAuthorizationCodeRequestBody
from mx_platform_python.models.payment_processor_authorization_code_response_body import PaymentProcessorAuthorizationCodeResponseBody
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
    api_instance = mx_platform_python.ProcessorTokenApi(api_client)
    payment_processor_authorization_code_request_body = mx_platform_python.PaymentProcessorAuthorizationCodeRequestBody() # PaymentProcessorAuthorizationCodeRequestBody | The scope for the authorization code.

    try:
        # (Deprecated) Request an authorization code
        api_response = api_instance.deprecated_request_payment_processor_authorization_code(payment_processor_authorization_code_request_body)
        print("The response of ProcessorTokenApi->deprecated_request_payment_processor_authorization_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessorTokenApi->deprecated_request_payment_processor_authorization_code: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_processor_authorization_code_request_body** | [**PaymentProcessorAuthorizationCodeRequestBody**](PaymentProcessorAuthorizationCodeRequestBody.md)| The scope for the authorization code. | 

### Return type

[**PaymentProcessorAuthorizationCodeResponseBody**](PaymentProcessorAuthorizationCodeResponseBody.md)

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

# **get_account_owner_info**
> ProcessorOwnerBody get_account_owner_info()

Get account owner information (Processors Only)

Get account owner information (Processors Only)

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.processor_owner_body import ProcessorOwnerBody
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

# Configure Bearer authorization: bearerAuth
configuration = mx_platform_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_python.ProcessorTokenApi(api_client)

    try:
        # Get account owner information (Processors Only)
        api_response = api_instance.get_account_owner_info()
        print("The response of ProcessorTokenApi->get_account_owner_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessorTokenApi->get_account_owner_info: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ProcessorOwnerBody**](ProcessorOwnerBody.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tokens**
> TokenResponseBody list_tokens(token_request_body=token_request_body)

View a List of Tokens

View a list of tokens that exist for a user, member, or account.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.token_request_body import TokenRequestBody
from mx_platform_python.models.token_response_body import TokenResponseBody
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
    api_instance = mx_platform_python.ProcessorTokenApi(api_client)
    token_request_body = mx_platform_python.TokenRequestBody() # TokenRequestBody |  (optional)

    try:
        # View a List of Tokens
        api_response = api_instance.list_tokens(token_request_body=token_request_body)
        print("The response of ProcessorTokenApi->list_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessorTokenApi->list_tokens: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_request_body** | [**TokenRequestBody**](TokenRequestBody.md)|  | [optional] 

### Return type

[**TokenResponseBody**](TokenResponseBody.md)

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

# **read_account_balance**
> PaymentAccountBody read_account_balance()

Read the account balance (Processors Only)

Read the account balance (Processors Only)

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.payment_account_body import PaymentAccountBody
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

# Configure Bearer authorization: bearerAuth
configuration = mx_platform_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_python.ProcessorTokenApi(api_client)

    try:
        # Read the account balance (Processors Only)
        api_response = api_instance.read_account_balance()
        print("The response of ProcessorTokenApi->read_account_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessorTokenApi->read_account_balance: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**PaymentAccountBody**](PaymentAccountBody.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_account_number**
> ProcessorAccountNumberBody request_account_number()

Request an account number (Processors Only)

Get account information such as routing number and account number, scoped to your access token.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.processor_account_number_body import ProcessorAccountNumberBody
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

# Configure Bearer authorization: bearerAuth
configuration = mx_platform_python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_python.ProcessorTokenApi(api_client)

    try:
        # Request an account number (Processors Only)
        api_response = api_instance.request_account_number()
        print("The response of ProcessorTokenApi->request_account_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessorTokenApi->request_account_number: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ProcessorAccountNumberBody**](ProcessorAccountNumberBody.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_authorization_code**
> AuthorizationCodeResponseBody request_authorization_code(authorization_code_request_body)

Request an authorization code

Clients use this endpoint to request an authorization code according to the parameters specified in the scope. Clients then pass this code to processors. Processor access is scoped only to the GUIDs and features specified in this request. Before requesting an authorization code which includes a member in the scope, clients must have verified that member.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.authorization_code_request_body import AuthorizationCodeRequestBody
from mx_platform_python.models.authorization_code_response_body import AuthorizationCodeResponseBody
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
    api_instance = mx_platform_python.ProcessorTokenApi(api_client)
    authorization_code_request_body = mx_platform_python.AuthorizationCodeRequestBody() # AuthorizationCodeRequestBody | The scope for the authorization code.

    try:
        # Request an authorization code
        api_response = api_instance.request_authorization_code(authorization_code_request_body)
        print("The response of ProcessorTokenApi->request_authorization_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProcessorTokenApi->request_authorization_code: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_code_request_body** | [**AuthorizationCodeRequestBody**](AuthorizationCodeRequestBody.md)| The scope for the authorization code. | 

### Return type

[**AuthorizationCodeResponseBody**](AuthorizationCodeResponseBody.md)

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

