# mx_platform_python.InvestmentHoldingsApi

All URIs are relative to *https://int-api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deactivate_user**](InvestmentHoldingsApi.md#deactivate_user) | **GET** /users/{user_guid}/investment_holdings_deactivate | Deactivate user from Investment Holdings
[**list_holdings**](InvestmentHoldingsApi.md#list_holdings) | **GET** /users/{user_guid}/investment_holdings | List holdings by user
[**list_holdings_by_account**](InvestmentHoldingsApi.md#list_holdings_by_account) | **GET** /users/{user_guid}/accounts/{account_guid}/investment_holdings | List holdings by account
[**list_holdings_by_member**](InvestmentHoldingsApi.md#list_holdings_by_member) | **GET** /users/{user_guid}/members/{member_guid}/investment_holdings | List holdings by member
[**read_holding**](InvestmentHoldingsApi.md#read_holding) | **GET** /users/{user_guid}/investment_holdings/{holding_guid} | Read holding


# **deactivate_user**
> InvestmentHoldingsDeactivation deactivate_user(user_guid)

Deactivate user from Investment Holdings

This endpoint deactivates the specific user from the `/investment_holdings` product. To reactivate a user, use any of the current `/investment_holding` endpoints.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.investment_holdings_deactivation import InvestmentHoldingsDeactivation
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
    api_instance = mx_platform_python.InvestmentHoldingsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Deactivate user from Investment Holdings
        api_response = api_instance.deactivate_user(user_guid)
        print("The response of InvestmentHoldingsApi->deactivate_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentHoldingsApi->deactivate_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 

### Return type

[**InvestmentHoldingsDeactivation**](InvestmentHoldingsDeactivation.md)

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

# **list_holdings**
> InvestmentHoldingsResponseBody list_holdings(user_guid, page=page, records_per_page=records_per_page)

List holdings by user

This endpoint lists all holdings associated with the user across all accounts.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.investment_holdings_response_body import InvestmentHoldingsResponseBody
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
    api_instance = mx_platform_python.InvestmentHoldingsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # List holdings by user
        api_response = api_instance.list_holdings(user_guid, page=page, records_per_page=records_per_page)
        print("The response of InvestmentHoldingsApi->list_holdings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentHoldingsApi->list_holdings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

### Return type

[**InvestmentHoldingsResponseBody**](InvestmentHoldingsResponseBody.md)

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

# **list_holdings_by_account**
> InvestmentHoldingsResponseBody list_holdings_by_account(account_guid, user_guid, page=page, records_per_page=records_per_page)

List holdings by account

This endpoint lists all holdings associated with the particular account defined.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.investment_holdings_response_body import InvestmentHoldingsResponseBody
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
    api_instance = mx_platform_python.InvestmentHoldingsApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # List holdings by account
        api_response = api_instance.list_holdings_by_account(account_guid, user_guid, page=page, records_per_page=records_per_page)
        print("The response of InvestmentHoldingsApi->list_holdings_by_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentHoldingsApi->list_holdings_by_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

### Return type

[**InvestmentHoldingsResponseBody**](InvestmentHoldingsResponseBody.md)

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

# **list_holdings_by_member**
> InvestmentHoldingsResponseBody list_holdings_by_member(member_guid, user_guid, page=page, records_per_page=records_per_page)

List holdings by member

This endpoint lists all holdings associated with the specified member.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.investment_holdings_response_body import InvestmentHoldingsResponseBody
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
    api_instance = mx_platform_python.InvestmentHoldingsApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # List holdings by member
        api_response = api_instance.list_holdings_by_member(member_guid, user_guid, page=page, records_per_page=records_per_page)
        print("The response of InvestmentHoldingsApi->list_holdings_by_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentHoldingsApi->list_holdings_by_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

### Return type

[**InvestmentHoldingsResponseBody**](InvestmentHoldingsResponseBody.md)

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

# **read_holding**
> InvestmentHoldingResponseBody read_holding(holding_guid, user_guid)

Read holding

Use this endpoint to read the attributes of a specific `holding`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.investment_holding_response_body import InvestmentHoldingResponseBody
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
    api_instance = mx_platform_python.InvestmentHoldingsApi(api_client)
    holding_guid = 'HOL-d65683e8-9eab-26bb-bcfd-ced159c9abe2' # str | The unique id for a `holding`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Read holding
        api_response = api_instance.read_holding(holding_guid, user_guid)
        print("The response of InvestmentHoldingsApi->read_holding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentHoldingsApi->read_holding: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **holding_guid** | **str**| The unique id for a &#x60;holding&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 

### Return type

[**InvestmentHoldingResponseBody**](InvestmentHoldingResponseBody.md)

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

