# mx_platform_python.AchReturnApi

All URIs are relative to *https://int-api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ach_return**](AchReturnApi.md#create_ach_return) | **POST** /ach_returns | Create ACH Return
[**list_ach_retruns**](AchReturnApi.md#list_ach_retruns) | **GET** /ach_returns | List ACH Returns
[**read_ach_retrun**](AchReturnApi.md#read_ach_retrun) | **GET** /ach_returns/{ach_return_guid} | Read ACH Return


# **create_ach_return**
> ACHReturnResponseBody create_ach_return(ach_return_create_request_body)

Create ACH Return

:::warning The features documented here are in a beta state, and this documentation is considered draft material subject to frequent change. :::  Use this endpoint to create an ACH return in our system. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.ach_return_create_request_body import ACHReturnCreateRequestBody
from mx_platform_python.models.ach_return_response_body import ACHReturnResponseBody
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
    api_instance = mx_platform_python.AchReturnApi(api_client)
    ach_return_create_request_body = mx_platform_python.ACHReturnCreateRequestBody() # ACHReturnCreateRequestBody | ACH return object to be created.

    try:
        # Create ACH Return
        api_response = api_instance.create_ach_return(ach_return_create_request_body)
        print("The response of AchReturnApi->create_ach_return:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AchReturnApi->create_ach_return: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ach_return_create_request_body** | [**ACHReturnCreateRequestBody**](ACHReturnCreateRequestBody.md)| ACH return object to be created. | 

### Return type

[**ACHReturnResponseBody**](ACHReturnResponseBody.md)

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

# **list_ach_retruns**
> ACHReturnsResponseBody list_ach_retruns(institution_guid=institution_guid, returned_at=returned_at, resolved_status_at=resolved_status_at, return_code=return_code, return_status=return_status, page=page, records_per_page=records_per_page)

List ACH Returns

:::warning The features documented here are in a beta state, and this documentation is considered draft material subject to frequent change. :::  Use this endpoint to get all ACH returns. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.ach_returns_response_body import ACHReturnsResponseBody
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
    api_instance = mx_platform_python.AchReturnApi(api_client)
    institution_guid = 'institution_guid_example' # str | The identifier for the institution associated with the ACH return. Defined by MX. (optional)
    returned_at = '2025-02-13T18:09:00+00:00' # str | The date and time when the return was reported by the Receiving Financial Depository Institution (RDFI) in ISO 8601 format without timestamp. (optional)
    resolved_status_at = '2025-02-13T18:09:00+00:00' # str | The date and time when the return was resolved by the Receiving Financial Depository Institution (RDFI) in ISO 8601 format without timestamp (optional)
    return_code = 'return_code_example' # str | The associated ACH return code and notice of change code. See [Return Codes](/api-reference/platform-api/reference/ach-return-fields#return-codes) for a complete list. (optional)
    return_status = 'SUBMITTED' # str | The status of the return. See [Return Statuses](/api-reference/platform-api/reference/ach-return-fields#return-status) for a complete list. (optional)
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `100`. If the value exceeds `100`, the default value of `25` will be used instead. (optional)

    try:
        # List ACH Returns
        api_response = api_instance.list_ach_retruns(institution_guid=institution_guid, returned_at=returned_at, resolved_status_at=resolved_status_at, return_code=return_code, return_status=return_status, page=page, records_per_page=records_per_page)
        print("The response of AchReturnApi->list_ach_retruns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AchReturnApi->list_ach_retruns: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_guid** | **str**| The identifier for the institution associated with the ACH return. Defined by MX. | [optional] 
 **returned_at** | **str**| The date and time when the return was reported by the Receiving Financial Depository Institution (RDFI) in ISO 8601 format without timestamp. | [optional] 
 **resolved_status_at** | **str**| The date and time when the return was resolved by the Receiving Financial Depository Institution (RDFI) in ISO 8601 format without timestamp | [optional] 
 **return_code** | **str**| The associated ACH return code and notice of change code. See [Return Codes](/api-reference/platform-api/reference/ach-return-fields#return-codes) for a complete list. | [optional] 
 **return_status** | **str**| The status of the return. See [Return Statuses](/api-reference/platform-api/reference/ach-return-fields#return-status) for a complete list. | [optional] 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;100&#x60;. If the value exceeds &#x60;100&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

### Return type

[**ACHReturnsResponseBody**](ACHReturnsResponseBody.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.mx.api.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ach_retrun**
> ACHReturnResponseBody read_ach_retrun(ach_return_guid)

Read ACH Return

:::warning The features documented here are in a beta state, and this documentation is considered draft material subject to frequent change. :::  Use this endpoint to get an ACH return by its `guid` or `id`. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.ach_return_response_body import ACHReturnResponseBody
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
    api_instance = mx_platform_python.AchReturnApi(api_client)
    ach_return_guid = 'ach_return_guid_example' # str | The unique identifier (`guid`) for the ACH return. Defined by MX.

    try:
        # Read ACH Return
        api_response = api_instance.read_ach_retrun(ach_return_guid)
        print("The response of AchReturnApi->read_ach_retrun:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AchReturnApi->read_ach_retrun: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ach_return_guid** | **str**| The unique identifier (&#x60;guid&#x60;) for the ACH return. Defined by MX. | 

### Return type

[**ACHReturnResponseBody**](ACHReturnResponseBody.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.mx.api.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

