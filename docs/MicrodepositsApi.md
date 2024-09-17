# mx_platform_python.MicrodepositsApi

All URIs are relative to *https://api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**micro_deposits_microdeposit_guid_verify_put**](MicrodepositsApi.md#micro_deposits_microdeposit_guid_verify_put) | **PUT** /micro_deposits/{microdeposit_guid}/verify | Verify a Microdeposit
[**users_user_guid_micro_deposits_get**](MicrodepositsApi.md#users_user_guid_micro_deposits_get) | **GET** /users/{user_guid}/micro_deposits | List all microdeposits for a user
[**users_user_guid_micro_deposits_micro_deposit_guid_delete**](MicrodepositsApi.md#users_user_guid_micro_deposits_micro_deposit_guid_delete) | **DELETE** /users/{user_guid}/micro_deposits/{micro_deposit_guid} | Delete a microdeposit
[**users_user_guid_micro_deposits_micro_deposit_guid_get**](MicrodepositsApi.md#users_user_guid_micro_deposits_micro_deposit_guid_get) | **GET** /users/{user_guid}/micro_deposits/{micro_deposit_guid} | Read a microdeposit for a user
[**users_user_guid_micro_deposits_post**](MicrodepositsApi.md#users_user_guid_micro_deposits_post) | **POST** /users/{user_guid}/micro_deposits | Create a microdeposit


# **micro_deposits_microdeposit_guid_verify_put**
> MicrodepositResponseBody micro_deposits_microdeposit_guid_verify_put(microdeposit_guid, microdeposit_verify_request_body=microdeposit_verify_request_body)

Verify a Microdeposit

Use this endpoint to verify the amounts deposited into the account during a microdeposit verification. The verification has not successfully completed until the `status` is `VERIFIED`. Poll the `/users/{user_guid}/micro_deposits/{micro_deposit_guid}` (read microdeposit) endpoint until you see this status or an error state.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.microdeposit_response_body import MicrodepositResponseBody
from mx_platform_python.models.microdeposit_verify_request_body import MicrodepositVerifyRequestBody
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
    api_instance = mx_platform_python.MicrodepositsApi(api_client)
    microdeposit_guid = 'microdeposit_guid_example' # str | The unique identifier for the microdeposit. Defined by MX.
    microdeposit_verify_request_body = mx_platform_python.MicrodepositVerifyRequestBody() # MicrodepositVerifyRequestBody |  (optional)

    try:
        # Verify a Microdeposit
        api_response = api_instance.micro_deposits_microdeposit_guid_verify_put(microdeposit_guid, microdeposit_verify_request_body=microdeposit_verify_request_body)
        print("The response of MicrodepositsApi->micro_deposits_microdeposit_guid_verify_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MicrodepositsApi->micro_deposits_microdeposit_guid_verify_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **microdeposit_guid** | **str**| The unique identifier for the microdeposit. Defined by MX. | 
 **microdeposit_verify_request_body** | [**MicrodepositVerifyRequestBody**](MicrodepositVerifyRequestBody.md)|  | [optional] 

### Return type

[**MicrodepositResponseBody**](MicrodepositResponseBody.md)

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

# **users_user_guid_micro_deposits_get**
> MicrodepositsResponseBody users_user_guid_micro_deposits_get(user_guid)

List all microdeposits for a user

Use this endpoint to read the attributes of a specific microdeposit according to its unique GUID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.microdeposits_response_body import MicrodepositsResponseBody
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
    api_instance = mx_platform_python.MicrodepositsApi(api_client)
    user_guid = 'user_guid_example' # str | The unique identifier for the user. Defined by MX.

    try:
        # List all microdeposits for a user
        api_response = api_instance.users_user_guid_micro_deposits_get(user_guid)
        print("The response of MicrodepositsApi->users_user_guid_micro_deposits_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MicrodepositsApi->users_user_guid_micro_deposits_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. Defined by MX. | 

### Return type

[**MicrodepositsResponseBody**](MicrodepositsResponseBody.md)

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

# **users_user_guid_micro_deposits_micro_deposit_guid_delete**
> users_user_guid_micro_deposits_micro_deposit_guid_delete(micro_deposit_guid, user_guid)

Delete a microdeposit

Use this endpoint to delete the specified microdeposit.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
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
    api_instance = mx_platform_python.MicrodepositsApi(api_client)
    micro_deposit_guid = 'MIC-09ba578e-8448-4f7f-89e1-b62ff2517edb' # str | The unique identifier for the microdeposit. Defined by MX.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Delete a microdeposit
        api_instance.users_user_guid_micro_deposits_micro_deposit_guid_delete(micro_deposit_guid, user_guid)
    except Exception as e:
        print("Exception when calling MicrodepositsApi->users_user_guid_micro_deposits_micro_deposit_guid_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **micro_deposit_guid** | **str**| The unique identifier for the microdeposit. Defined by MX. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_guid_micro_deposits_micro_deposit_guid_get**
> MicrodepositResponseBody users_user_guid_micro_deposits_micro_deposit_guid_get(user_guid, micro_deposit_guid)

Read a microdeposit for a user

Use this endpoint to read the attributes of a specific microdeposit according to its unique GUID. <br></br> Webhooks for microdeposit status changes are triggered when a status changes. The actual status of the microdeposit guid updates every minute. You may force a status update by calling the read microdeposit endpoint.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.microdeposit_response_body import MicrodepositResponseBody
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
    api_instance = mx_platform_python.MicrodepositsApi(api_client)
    user_guid = 'user_guid_example' # str | The unique identifier for the user. Defined by MX.
    micro_deposit_guid = 'micro_deposit_guid_example' # str | The unique identifier for the microdeposit. Defined by MX.

    try:
        # Read a microdeposit for a user
        api_response = api_instance.users_user_guid_micro_deposits_micro_deposit_guid_get(user_guid, micro_deposit_guid)
        print("The response of MicrodepositsApi->users_user_guid_micro_deposits_micro_deposit_guid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MicrodepositsApi->users_user_guid_micro_deposits_micro_deposit_guid_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. Defined by MX. | 
 **micro_deposit_guid** | **str**| The unique identifier for the microdeposit. Defined by MX. | 

### Return type

[**MicrodepositResponseBody**](MicrodepositResponseBody.md)

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

# **users_user_guid_micro_deposits_post**
> MicrodepositResponseBody users_user_guid_micro_deposits_post(user_guid, microdeposit_request_body)

Create a microdeposit

Use this endpoint to create a microdeposit. The response will include the new microdeposit record with a status of INITIATED.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.microdeposit_request_body import MicrodepositRequestBody
from mx_platform_python.models.microdeposit_response_body import MicrodepositResponseBody
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
    api_instance = mx_platform_python.MicrodepositsApi(api_client)
    user_guid = 'user_guid_example' # str | The unique identifier for the user. Defined by MX.
    microdeposit_request_body = mx_platform_python.MicrodepositRequestBody() # MicrodepositRequestBody | 

    try:
        # Create a microdeposit
        api_response = api_instance.users_user_guid_micro_deposits_post(user_guid, microdeposit_request_body)
        print("The response of MicrodepositsApi->users_user_guid_micro_deposits_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MicrodepositsApi->users_user_guid_micro_deposits_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. Defined by MX. | 
 **microdeposit_request_body** | [**MicrodepositRequestBody**](MicrodepositRequestBody.md)|  | 

### Return type

[**MicrodepositResponseBody**](MicrodepositResponseBody.md)

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

