# mx_platform_python.InsightsApi

All URIs are relative to *https://api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_accounts_insight**](InsightsApi.md#list_accounts_insight) | **GET** /users/{user_guid}/insights/{insight_guid}/accounts | List all accounts associated with an insight.
[**list_categories_insight**](InsightsApi.md#list_categories_insight) | **GET** /users/{user_guid}/insights/{insight_guid}/categories | List all categories associated with an insight.
[**list_insights_by_account**](InsightsApi.md#list_insights_by_account) | **GET** /users/{user_guid}/accounts/{account_guid}/insights | List insights by account
[**list_insights_user**](InsightsApi.md#list_insights_user) | **GET** /users/{user_guid}/insights | List all insights for a user.
[**list_merchants_insight**](InsightsApi.md#list_merchants_insight) | **GET** /users/{user_guid}/insights/{insight_guid}/merchants | List all merchants associated with an insight.
[**list_scheduled_payments_insight**](InsightsApi.md#list_scheduled_payments_insight) | **GET** /users/{user_guid}/insights/{insight_guid}/scheduled_payments | List all scheduled payments associated with an insight
[**list_transactions_insight**](InsightsApi.md#list_transactions_insight) | **GET** /users/{user_guid}/insights/{insight_guid}/transactions | List all transactions associated with an insight.
[**read_insights_user**](InsightsApi.md#read_insights_user) | **GET** /users/{user_guid}/insights{insight_guid} | Read a specific insight.
[**update_insight**](InsightsApi.md#update_insight) | **PUT** /users/{user_guid}/insights{insight_guid} | Update insight


# **list_accounts_insight**
> AccountsResponseBody list_accounts_insight(user_guid, insight_guid, page=page, records_per_page=records_per_page)

List all accounts associated with an insight.

Use this endpoint to list all the accounts associated with the insight.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.accounts_response_body import AccountsResponseBody
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
    api_instance = mx_platform_python.InsightsApi(api_client)
    user_guid = 'USR-1234-abcd' # str | The unique identifier for the user. Defined by MX.
    insight_guid = 'BET-1234-abcd' # str | The unique identifier for the insight. Defined by MX.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List all accounts associated with an insight.
        api_response = api_instance.list_accounts_insight(user_guid, insight_guid, page=page, records_per_page=records_per_page)
        print("The response of InsightsApi->list_accounts_insight:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsApi->list_accounts_insight: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. Defined by MX. | 
 **insight_guid** | **str**| The unique identifier for the insight. Defined by MX. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**AccountsResponseBody**](AccountsResponseBody.md)

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

# **list_categories_insight**
> CategoriesResponseBody list_categories_insight(user_guid, insight_guid, page=page, records_per_page=records_per_page)

List all categories associated with an insight.

Use this endpoint to list all the categories associated with the insight.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.categories_response_body import CategoriesResponseBody
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
    api_instance = mx_platform_python.InsightsApi(api_client)
    user_guid = 'USR-1234-abcd' # str | The unique identifier for the user. Defined by MX.
    insight_guid = 'BET-1234-abcd' # str | The unique identifier for the insight. Defined by MX.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List all categories associated with an insight.
        api_response = api_instance.list_categories_insight(user_guid, insight_guid, page=page, records_per_page=records_per_page)
        print("The response of InsightsApi->list_categories_insight:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsApi->list_categories_insight: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. Defined by MX. | 
 **insight_guid** | **str**| The unique identifier for the insight. Defined by MX. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**CategoriesResponseBody**](CategoriesResponseBody.md)

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

# **list_insights_by_account**
> InsightsResponseBody list_insights_by_account(account_guid, user_guid, page=page, records_per_page=records_per_page)

List insights by account

Use this endpoint to list all insights associated with a specified account GUID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.insights_response_body import InsightsResponseBody
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
    api_instance = mx_platform_python.InsightsApi(api_client)
    account_guid = 'ACT-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for the `account`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for the `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List insights by account
        api_response = api_instance.list_insights_by_account(account_guid, user_guid, page=page, records_per_page=records_per_page)
        print("The response of InsightsApi->list_insights_by_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsApi->list_insights_by_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for the &#x60;account&#x60;. | 
 **user_guid** | **str**| The unique id for the &#x60;user&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**InsightsResponseBody**](InsightsResponseBody.md)

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

# **list_insights_user**
> InsightsResponseBody list_insights_user(user_guid, page=page, records_per_page=records_per_page)

List all insights for a user.

Use this endpoint to list all the insights associated with the user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.insights_response_body import InsightsResponseBody
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
    api_instance = mx_platform_python.InsightsApi(api_client)
    user_guid = 'USR-1234-abcd' # str | The unique identifier for the user. Defined by MX.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List all insights for a user.
        api_response = api_instance.list_insights_user(user_guid, page=page, records_per_page=records_per_page)
        print("The response of InsightsApi->list_insights_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsApi->list_insights_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. Defined by MX. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**InsightsResponseBody**](InsightsResponseBody.md)

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

# **list_merchants_insight**
> MerchantsResponseBody list_merchants_insight(user_guid, insight_guid, page=page, records_per_page=records_per_page)

List all merchants associated with an insight.

Use this endpoint to list all the merchants associated with the insight.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.merchants_response_body import MerchantsResponseBody
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
    api_instance = mx_platform_python.InsightsApi(api_client)
    user_guid = 'USR-1234-abcd' # str | The unique identifier for the user. Defined by MX.
    insight_guid = 'BET-1234-abcd' # str | The unique identifier for the insight. Defined by MX.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List all merchants associated with an insight.
        api_response = api_instance.list_merchants_insight(user_guid, insight_guid, page=page, records_per_page=records_per_page)
        print("The response of InsightsApi->list_merchants_insight:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsApi->list_merchants_insight: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. Defined by MX. | 
 **insight_guid** | **str**| The unique identifier for the insight. Defined by MX. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**MerchantsResponseBody**](MerchantsResponseBody.md)

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

# **list_scheduled_payments_insight**
> ScheduledPaymentsResponseBody list_scheduled_payments_insight(user_guid, insight_guid, page=page, records_per_page=records_per_page)

List all scheduled payments associated with an insight

Use this endpoint to list all the scheduled payments associated with the insight.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.scheduled_payments_response_body import ScheduledPaymentsResponseBody
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
    api_instance = mx_platform_python.InsightsApi(api_client)
    user_guid = 'USR-1234-abcd' # str | The unique identifier for the user. Defined by MX.
    insight_guid = 'BET-1234-abcd' # str | The unique identifier for the insight. Defined by MX.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List all scheduled payments associated with an insight
        api_response = api_instance.list_scheduled_payments_insight(user_guid, insight_guid, page=page, records_per_page=records_per_page)
        print("The response of InsightsApi->list_scheduled_payments_insight:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsApi->list_scheduled_payments_insight: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. Defined by MX. | 
 **insight_guid** | **str**| The unique identifier for the insight. Defined by MX. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**ScheduledPaymentsResponseBody**](ScheduledPaymentsResponseBody.md)

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

# **list_transactions_insight**
> TransactionsResponseBody list_transactions_insight(user_guid, insight_guid, page=page, records_per_page=records_per_page)

List all transactions associated with an insight.

Use this endpoint to list all the transactions associated with the insight.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.transactions_response_body import TransactionsResponseBody
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
    api_instance = mx_platform_python.InsightsApi(api_client)
    user_guid = 'USR-1234-abcd' # str | The unique identifier for the user. Defined by MX.
    insight_guid = 'BET-1234-abcd' # str | The unique identifier for the insight. Defined by MX.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List all transactions associated with an insight.
        api_response = api_instance.list_transactions_insight(user_guid, insight_guid, page=page, records_per_page=records_per_page)
        print("The response of InsightsApi->list_transactions_insight:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsApi->list_transactions_insight: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. Defined by MX. | 
 **insight_guid** | **str**| The unique identifier for the insight. Defined by MX. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**TransactionsResponseBody**](TransactionsResponseBody.md)

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

# **read_insights_user**
> InsightResponseBody read_insights_user(user_guid, insight_guid)

Read a specific insight.

Use this endpoint to read the attributes of a specific insight according to its unique GUID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.insight_response_body import InsightResponseBody
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
    api_instance = mx_platform_python.InsightsApi(api_client)
    user_guid = 'USR-1234-abcd' # str | The unique identifier for the user. Defined by MX.
    insight_guid = 'BET-1234-abcd' # str | The unique identifier for the insight. Defined by MX.

    try:
        # Read a specific insight.
        api_response = api_instance.read_insights_user(user_guid, insight_guid)
        print("The response of InsightsApi->read_insights_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsApi->read_insights_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. Defined by MX. | 
 **insight_guid** | **str**| The unique identifier for the insight. Defined by MX. | 

### Return type

[**InsightResponseBody**](InsightResponseBody.md)

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

# **update_insight**
> InsightResponse update_insight(user_guid, insight_guid, insight_update_request)

Update insight

Use this endpoint to update the attributes of a particular insight according to its unique GUID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.insight_response import InsightResponse
from mx_platform_python.models.insight_update_request import InsightUpdateRequest
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
    api_instance = mx_platform_python.InsightsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for the user. Defined by MX.
    insight_guid = 'BET-1234-abcd' # str | The unique identifier for the insight. Defined by MX.
    insight_update_request = mx_platform_python.InsightUpdateRequest() # InsightUpdateRequest | The insight to be updated (None of these parameters are required, but the user object cannot be empty.)

    try:
        # Update insight
        api_response = api_instance.update_insight(user_guid, insight_guid, insight_update_request)
        print("The response of InsightsApi->update_insight:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsApi->update_insight: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. Defined by MX. | 
 **insight_guid** | **str**| The unique identifier for the insight. Defined by MX. | 
 **insight_update_request** | [**InsightUpdateRequest**](InsightUpdateRequest.md)| The insight to be updated (None of these parameters are required, but the user object cannot be empty.) | 

### Return type

[**InsightResponse**](InsightResponse.md)

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

