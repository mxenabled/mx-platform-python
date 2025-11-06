# mx_platform_python.MicrodepositsApi

All URIs are relative to *https://int-api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_microdeposit**](MicrodepositsApi.md#create_microdeposit) | **POST** /users/{user_guid}/micro_deposits | Create or pre-initiate a microdeposit
[**delete_microdeposit**](MicrodepositsApi.md#delete_microdeposit) | **DELETE** /users/{user_guid}/micro_deposits/{micro_deposit_guid} | Delete a microdeposit
[**list_user_microdeposits**](MicrodepositsApi.md#list_user_microdeposits) | **GET** /users/{user_guid}/micro_deposits | List all microdeposits for a user
[**list_user_verifications**](MicrodepositsApi.md#list_user_verifications) | **GET** /users/{user_guid}/account_verifications | List all verifications for a user
[**read_user_microdeposit**](MicrodepositsApi.md#read_user_microdeposit) | **GET** /users/{user_guid}/micro_deposits/{micro_deposit_guid} | Read a microdeposit for a user
[**verify_microdeposit**](MicrodepositsApi.md#verify_microdeposit) | **PUT** /micro_deposits/{micro_deposit_guid}/verify | Verify a Microdeposit


# **create_microdeposit**
> MicrodepositResponseBody create_microdeposit(user_guid, microdeposit_request_body)

Create or pre-initiate a microdeposit

Use this endpoint to create or pre-initiate a microdeposit. The response will include the new microdeposit record with a status of `INITIATED` or `PREINITIATED` respectively.  To pre-initiate a microdeposit, you only need to set `email` (string), `first_name` (string), and `last_name` (string) in the request body.   Pre-initiating a microdeposit allows you to pass the end user's first name, last name, and email if this data has already been collected. If the end user selects an institution which requires the microdeposit flow, the pre-initiated `micro_deposit` will be used and the Connect Widget step that normally requests this info from the end user will be skipped. However, if the end user selects an institution which supports IAV, the pre-initiated `micro_deposit` will be deleted and IAV will be used instead. When requesting a Connect Widget URL after pre-initiating, make sure to set the `current_microdeposit_guid` to the resulting microdeposit's `guid` and set the `mode` to `verification`. If you use this enhanced flow, a `micro_deposit` should be pre-initiated for all connect sessions in verification mode. After pre-initiating a microdeposit, pass the GUID to the config as `current_microdeposit_guid` and set the `mode` to `verification` when requesting a Connect URL.  Pre-initiating a microdeposit is optional. If you choose to implement this flow, it should be used for all Connect Widget sessions in verification mode. 

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
    api_instance = mx_platform_python.MicrodepositsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    microdeposit_request_body = mx_platform_python.MicrodepositRequestBody() # MicrodepositRequestBody | 

    try:
        # Create or pre-initiate a microdeposit
        api_response = api_instance.create_microdeposit(user_guid, microdeposit_request_body)
        print("The response of MicrodepositsApi->create_microdeposit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MicrodepositsApi->create_microdeposit: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
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

# **delete_microdeposit**
> delete_microdeposit(micro_deposit_guid, user_guid)

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
    api_instance = mx_platform_python.MicrodepositsApi(api_client)
    micro_deposit_guid = 'MIC-09ba578e-8448-4f7f-89e1-b62ff2517edb' # str | The unique identifier for the microdeposit. Defined by MX.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Delete a microdeposit
        api_instance.delete_microdeposit(micro_deposit_guid, user_guid)
    except Exception as e:
        print("Exception when calling MicrodepositsApi->delete_microdeposit: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **micro_deposit_guid** | **str**| The unique identifier for the microdeposit. Defined by MX. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 

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

# **list_user_microdeposits**
> MicrodepositsResponseBody list_user_microdeposits(user_guid)

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
    api_instance = mx_platform_python.MicrodepositsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # List all microdeposits for a user
        api_response = api_instance.list_user_microdeposits(user_guid)
        print("The response of MicrodepositsApi->list_user_microdeposits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MicrodepositsApi->list_user_microdeposits: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 

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

# **list_user_verifications**
> MicrodepositResponseBody list_user_verifications(user_guid)

List all verifications for a user

This endpoint returns a list of the account verifications associated with the user, as well as the status of those verifications. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.microdeposit_response_body import MicrodepositResponseBody
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
    api_instance = mx_platform_python.MicrodepositsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # List all verifications for a user
        api_response = api_instance.list_user_verifications(user_guid)
        print("The response of MicrodepositsApi->list_user_verifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MicrodepositsApi->list_user_verifications: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 

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

# **read_user_microdeposit**
> MicrodepositResponseBody read_user_microdeposit(micro_deposit_guid, user_guid)

Read a microdeposit for a user

Use this endpoint to read the attributes of a specific microdeposit according to its unique GUID. <br /><br /> Webhooks for microdeposit status changes are triggered when a status changes. The actual status of the microdeposit guid updates every minute. You may force a status update by calling the read microdeposit endpoint.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.microdeposit_response_body import MicrodepositResponseBody
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
    api_instance = mx_platform_python.MicrodepositsApi(api_client)
    micro_deposit_guid = 'MIC-09ba578e-8448-4f7f-89e1-b62ff2517edb' # str | The unique identifier for the microdeposit. Defined by MX.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Read a microdeposit for a user
        api_response = api_instance.read_user_microdeposit(micro_deposit_guid, user_guid)
        print("The response of MicrodepositsApi->read_user_microdeposit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MicrodepositsApi->read_user_microdeposit: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **micro_deposit_guid** | **str**| The unique identifier for the microdeposit. Defined by MX. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 

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

# **verify_microdeposit**
> MicrodepositResponseBody verify_microdeposit(micro_deposit_guid, microdeposit_verify_request_body=microdeposit_verify_request_body)

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
    api_instance = mx_platform_python.MicrodepositsApi(api_client)
    micro_deposit_guid = 'MIC-09ba578e-8448-4f7f-89e1-b62ff2517edb' # str | The unique identifier for the microdeposit. Defined by MX.
    microdeposit_verify_request_body = mx_platform_python.MicrodepositVerifyRequestBody() # MicrodepositVerifyRequestBody |  (optional)

    try:
        # Verify a Microdeposit
        api_response = api_instance.verify_microdeposit(micro_deposit_guid, microdeposit_verify_request_body=microdeposit_verify_request_body)
        print("The response of MicrodepositsApi->verify_microdeposit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MicrodepositsApi->verify_microdeposit: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **micro_deposit_guid** | **str**| The unique identifier for the microdeposit. Defined by MX. | 
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

