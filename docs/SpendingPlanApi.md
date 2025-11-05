# mx_platform_python.SpendingPlanApi

All URIs are relative to *https://int-api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_spending_plan**](SpendingPlanApi.md#create_spending_plan) | **POST** /users/{user_guid}/spending_plans | Create spending plan
[**create_spending_plan_iteration_item**](SpendingPlanApi.md#create_spending_plan_iteration_item) | **POST** /users/{user_guid}/spending_plans/{spending_plan_guid}/iterations/current/iteration_items | Create spending plan iteration item
[**delete_spending_plan**](SpendingPlanApi.md#delete_spending_plan) | **DELETE** /users/{user_guid}/spending_plans/{spending_plan_guid} | Delete spending plan
[**delete_spending_plan_account**](SpendingPlanApi.md#delete_spending_plan_account) | **DELETE** /users/{user_guid}/spending_plans/{spending_plan_guid}/spending_plan_accounts/{spending_plan_account_guid} | Delete spending plan account
[**delete_spending_plan_iteration_item**](SpendingPlanApi.md#delete_spending_plan_iteration_item) | **DELETE** /users/{user_guid}/spending_plans/{spending_plan_guid}/iterations/current/iteration_items/{iteration_item_guid} | Delete spending plan iteration item
[**list_spending_plan_accounts**](SpendingPlanApi.md#list_spending_plan_accounts) | **GET** /users/{user_guid}/spending_plans/{spending_plan_guid}/spending_plan_accounts | List spending plan accounts
[**list_spending_plan_iteration_items**](SpendingPlanApi.md#list_spending_plan_iteration_items) | **GET** /users/{user_guid}/spending_plans/{spending_plan_guid}/iterations/current/iteration_items | List spending plan iteration items
[**list_spending_plan_iterations**](SpendingPlanApi.md#list_spending_plan_iterations) | **GET** /users/{user_guid}/spending_plans/{spending_plan_guid}/iterations | List spending plan iterations
[**list_spending_plans**](SpendingPlanApi.md#list_spending_plans) | **GET** /users/{user_guid}/spending_plans | List spending plans
[**read_current_spending_plan_iteration**](SpendingPlanApi.md#read_current_spending_plan_iteration) | **GET** /users/{user_guid}/spending_plans/{spending_plan_guid}/iterations/current | Read current spending plan iteration
[**read_spending_plan_account**](SpendingPlanApi.md#read_spending_plan_account) | **GET** /users/{user_guid}/spending_plans/{spending_plan_guid}/spending_plan_accounts/{spending_plan_account_guid} | Read spending plan account
[**read_spending_plan_iteration**](SpendingPlanApi.md#read_spending_plan_iteration) | **GET** /users/{user_guid}/spending_plans/{spending_plan_guid}/iterations/{iteration_number} | Read a spending plan iteration
[**read_spending_plan_iteration_item**](SpendingPlanApi.md#read_spending_plan_iteration_item) | **GET** /users/{user_guid}/spending_plans/{spending_plan_guid}/iterations/current/iteration_items/{iteration_item_guid} | Read a spending plan iteration item
[**read_spending_plan_user**](SpendingPlanApi.md#read_spending_plan_user) | **GET** /users/{user_guid}/spending_plans/{spending_plan_guid} | Read a spending plan for a user
[**update_spending_plan_iteration_item**](SpendingPlanApi.md#update_spending_plan_iteration_item) | **PUT** /users/{user_guid}/spending_plans/{spending_plan_guid}/iterations/current/iteration_items/{iteration_item_guid} | Update a spending plan iteration item


# **create_spending_plan**
> SpendingPlanResponse create_spending_plan(user_guid)

Create spending plan

This endpoint creates a new `spending_plan` for the user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.spending_plan_response import SpendingPlanResponse
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
    api_instance = mx_platform_python.SpendingPlanApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Create spending plan
        api_response = api_instance.create_spending_plan(user_guid)
        print("The response of SpendingPlanApi->create_spending_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpendingPlanApi->create_spending_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 

### Return type

[**SpendingPlanResponse**](SpendingPlanResponse.md)

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

# **create_spending_plan_iteration_item**
> SpendingPlanIterationItemResponse create_spending_plan_iteration_item(spending_plan_guid, user_guid, spending_plan_iteration_item_create_request_body)

Create spending plan iteration item

This endpoint creates a new `spending_plan_iteration_item`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.spending_plan_iteration_item_create_request_body import SpendingPlanIterationItemCreateRequestBody
from mx_platform_python.models.spending_plan_iteration_item_response import SpendingPlanIterationItemResponse
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
    api_instance = mx_platform_python.SpendingPlanApi(api_client)
    spending_plan_guid = 'SPL-e5f9a5bd-c5b3-4901-bdc0-62119b9db262' # str | The unique ID for the `spending_plan`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    spending_plan_iteration_item_create_request_body = mx_platform_python.SpendingPlanIterationItemCreateRequestBody() # SpendingPlanIterationItemCreateRequestBody | Iteration item to be created with required parameter (planned_amount)

    try:
        # Create spending plan iteration item
        api_response = api_instance.create_spending_plan_iteration_item(spending_plan_guid, user_guid, spending_plan_iteration_item_create_request_body)
        print("The response of SpendingPlanApi->create_spending_plan_iteration_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpendingPlanApi->create_spending_plan_iteration_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spending_plan_guid** | **str**| The unique ID for the &#x60;spending_plan&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **spending_plan_iteration_item_create_request_body** | [**SpendingPlanIterationItemCreateRequestBody**](SpendingPlanIterationItemCreateRequestBody.md)| Iteration item to be created with required parameter (planned_amount) | 

### Return type

[**SpendingPlanIterationItemResponse**](SpendingPlanIterationItemResponse.md)

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

# **delete_spending_plan**
> delete_spending_plan(user_guid, spending_plan_guid)

Delete spending plan

Use this endpoint to delete a user's `spending_plan`.

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
    api_instance = mx_platform_python.SpendingPlanApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    spending_plan_guid = 'SPL-e5f9a5bd-c5b3-4901-bdc0-62119b9db262' # str | The unique ID for the `spending_plan`.

    try:
        # Delete spending plan
        api_instance.delete_spending_plan(user_guid, spending_plan_guid)
    except Exception as e:
        print("Exception when calling SpendingPlanApi->delete_spending_plan: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **spending_plan_guid** | **str**| The unique ID for the &#x60;spending_plan&#x60;. | 

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

# **delete_spending_plan_account**
> delete_spending_plan_account(user_guid, spending_plan_guid, spending_plan_account_guid)

Delete spending plan account

Use this endpoint to delete a `spending_plan_account`.

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
    api_instance = mx_platform_python.SpendingPlanApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    spending_plan_guid = 'SPL-e5f9a5bd-c5b3-4901-bdc0-62119b9db262' # str | The unique ID for the `spending_plan`.
    spending_plan_account_guid = 'ACT-e9f80fee-84da-7s7r-9a5e-0346g4279b4c' # str | The unique ID for the specified account.

    try:
        # Delete spending plan account
        api_instance.delete_spending_plan_account(user_guid, spending_plan_guid, spending_plan_account_guid)
    except Exception as e:
        print("Exception when calling SpendingPlanApi->delete_spending_plan_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **spending_plan_guid** | **str**| The unique ID for the &#x60;spending_plan&#x60;. | 
 **spending_plan_account_guid** | **str**| The unique ID for the specified account. | 

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

# **delete_spending_plan_iteration_item**
> delete_spending_plan_iteration_item(user_guid, spending_plan_guid, iteration_item_guid)

Delete spending plan iteration item

Use this endpoint to delete a spending plan `iteration_item`.

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
    api_instance = mx_platform_python.SpendingPlanApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    spending_plan_guid = 'SPL-e5f9a5bd-c5b3-4901-bdc0-62119b9db262' # str | The unique ID for the `spending_plan`.
    iteration_item_guid = 'SII-a4dc1549-da28-1245-9c9c-53eee4cdfbe3' # str | The unique ID for the `iteration_item`.

    try:
        # Delete spending plan iteration item
        api_instance.delete_spending_plan_iteration_item(user_guid, spending_plan_guid, iteration_item_guid)
    except Exception as e:
        print("Exception when calling SpendingPlanApi->delete_spending_plan_iteration_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **spending_plan_guid** | **str**| The unique ID for the &#x60;spending_plan&#x60;. | 
 **iteration_item_guid** | **str**| The unique ID for the &#x60;iteration_item&#x60;. | 

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

# **list_spending_plan_accounts**
> SpendingPlanAccountsResponse list_spending_plan_accounts(user_guid, spending_plan_guid, page=page, records_per_page=records_per_page)

List spending plan accounts

Use this endpoint to list all the spending plan accounts associated with the spending plan.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.spending_plan_accounts_response import SpendingPlanAccountsResponse
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
    api_instance = mx_platform_python.SpendingPlanApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    spending_plan_guid = 'SPL-e5f9a5bd-c5b3-4901-bdc0-62119b9db262' # str | The unique ID for the `spending_plan`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # List spending plan accounts
        api_response = api_instance.list_spending_plan_accounts(user_guid, spending_plan_guid, page=page, records_per_page=records_per_page)
        print("The response of SpendingPlanApi->list_spending_plan_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpendingPlanApi->list_spending_plan_accounts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **spending_plan_guid** | **str**| The unique ID for the &#x60;spending_plan&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

### Return type

[**SpendingPlanAccountsResponse**](SpendingPlanAccountsResponse.md)

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

# **list_spending_plan_iteration_items**
> SpendingPlanIterationItemsResponseBody list_spending_plan_iteration_items(user_guid, spending_plan_guid, page=page, records_per_page=records_per_page)

List spending plan iteration items

Use this endpoint to list all the spending plan `iteration_items` associated with the `iteration`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.spending_plan_iteration_items_response_body import SpendingPlanIterationItemsResponseBody
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
    api_instance = mx_platform_python.SpendingPlanApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    spending_plan_guid = 'SPL-e5f9a5bd-c5b3-4901-bdc0-62119b9db262' # str | The unique ID for the `spending_plan`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # List spending plan iteration items
        api_response = api_instance.list_spending_plan_iteration_items(user_guid, spending_plan_guid, page=page, records_per_page=records_per_page)
        print("The response of SpendingPlanApi->list_spending_plan_iteration_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpendingPlanApi->list_spending_plan_iteration_items: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **spending_plan_guid** | **str**| The unique ID for the &#x60;spending_plan&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

### Return type

[**SpendingPlanIterationItemsResponseBody**](SpendingPlanIterationItemsResponseBody.md)

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

# **list_spending_plan_iterations**
> SpendingPlanIterationsResponse list_spending_plan_iterations(user_guid, spending_plan_guid, page=page, records_per_page=records_per_page)

List spending plan iterations

Use this endpoint to list all the spending plan `iterations` associated with the `spending_plan`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.spending_plan_iterations_response import SpendingPlanIterationsResponse
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
    api_instance = mx_platform_python.SpendingPlanApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    spending_plan_guid = 'SPL-e5f9a5bd-c5b3-4901-bdc0-62119b9db262' # str | The unique ID for the `spending_plan`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # List spending plan iterations
        api_response = api_instance.list_spending_plan_iterations(user_guid, spending_plan_guid, page=page, records_per_page=records_per_page)
        print("The response of SpendingPlanApi->list_spending_plan_iterations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpendingPlanApi->list_spending_plan_iterations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **spending_plan_guid** | **str**| The unique ID for the &#x60;spending_plan&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

### Return type

[**SpendingPlanIterationsResponse**](SpendingPlanIterationsResponse.md)

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

# **list_spending_plans**
> SpendingPlansResponseBody list_spending_plans(user_guid, page=page, records_per_page=records_per_page)

List spending plans

Use this endpoint to list all the spending plans associated with the user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.spending_plans_response_body import SpendingPlansResponseBody
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
    api_instance = mx_platform_python.SpendingPlanApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # List spending plans
        api_response = api_instance.list_spending_plans(user_guid, page=page, records_per_page=records_per_page)
        print("The response of SpendingPlanApi->list_spending_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpendingPlanApi->list_spending_plans: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

### Return type

[**SpendingPlansResponseBody**](SpendingPlansResponseBody.md)

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

# **read_current_spending_plan_iteration**
> SpendingPlanIterationResponse read_current_spending_plan_iteration(user_guid, spending_plan_guid, page=page, records_per_page=records_per_page)

Read current spending plan iteration

Use this endpoint to read the attributes of the current spending plan `iteration`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.spending_plan_iteration_response import SpendingPlanIterationResponse
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
    api_instance = mx_platform_python.SpendingPlanApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    spending_plan_guid = 'SPL-e5f9a5bd-c5b3-4901-bdc0-62119b9db262' # str | The unique ID for the `spending_plan`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # Read current spending plan iteration
        api_response = api_instance.read_current_spending_plan_iteration(user_guid, spending_plan_guid, page=page, records_per_page=records_per_page)
        print("The response of SpendingPlanApi->read_current_spending_plan_iteration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpendingPlanApi->read_current_spending_plan_iteration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **spending_plan_guid** | **str**| The unique ID for the &#x60;spending_plan&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

### Return type

[**SpendingPlanIterationResponse**](SpendingPlanIterationResponse.md)

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

# **read_spending_plan_account**
> SpendingPlanAccountResponse read_spending_plan_account(user_guid, spending_plan_guid, spending_plan_account_guid, page=page, records_per_page=records_per_page)

Read spending plan account

Use this endpoint to read the attributes of a specific spending plan account according to its unique GUID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.spending_plan_account_response import SpendingPlanAccountResponse
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
    api_instance = mx_platform_python.SpendingPlanApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    spending_plan_guid = 'SPL-e5f9a5bd-c5b3-4901-bdc0-62119b9db262' # str | The unique ID for the `spending_plan`.
    spending_plan_account_guid = 'ACT-e9f80fee-84da-7s7r-9a5e-0346g4279b4c' # str | The unique ID for the specified account.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # Read spending plan account
        api_response = api_instance.read_spending_plan_account(user_guid, spending_plan_guid, spending_plan_account_guid, page=page, records_per_page=records_per_page)
        print("The response of SpendingPlanApi->read_spending_plan_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpendingPlanApi->read_spending_plan_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **spending_plan_guid** | **str**| The unique ID for the &#x60;spending_plan&#x60;. | 
 **spending_plan_account_guid** | **str**| The unique ID for the specified account. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

### Return type

[**SpendingPlanAccountResponse**](SpendingPlanAccountResponse.md)

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

# **read_spending_plan_iteration**
> SpendingPlanIterationResponse read_spending_plan_iteration(user_guid, spending_plan_guid, iteration_number, page=page, records_per_page=records_per_page)

Read a spending plan iteration

Use this endpoint to read the attributes of a specific spending plan `iteration` according to its `iteration_number`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.spending_plan_iteration_response import SpendingPlanIterationResponse
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
    api_instance = mx_platform_python.SpendingPlanApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    spending_plan_guid = 'SPL-e5f9a5bd-c5b3-4901-bdc0-62119b9db262' # str | The unique ID for the `spending_plan`.
    iteration_number = 1 # int | The current iteration number for the spending plan `iteration`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # Read a spending plan iteration
        api_response = api_instance.read_spending_plan_iteration(user_guid, spending_plan_guid, iteration_number, page=page, records_per_page=records_per_page)
        print("The response of SpendingPlanApi->read_spending_plan_iteration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpendingPlanApi->read_spending_plan_iteration: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **spending_plan_guid** | **str**| The unique ID for the &#x60;spending_plan&#x60;. | 
 **iteration_number** | **int**| The current iteration number for the spending plan &#x60;iteration&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

### Return type

[**SpendingPlanIterationResponse**](SpendingPlanIterationResponse.md)

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

# **read_spending_plan_iteration_item**
> SpendingPlanIterationItemResponse read_spending_plan_iteration_item(user_guid, spending_plan_guid, iteration_item_guid, page=page, records_per_page=records_per_page)

Read a spending plan iteration item

Use this endpoint to read the attributes of a specific spending plan `iteration_item` according to its unique GUID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.spending_plan_iteration_item_response import SpendingPlanIterationItemResponse
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
    api_instance = mx_platform_python.SpendingPlanApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    spending_plan_guid = 'SPL-e5f9a5bd-c5b3-4901-bdc0-62119b9db262' # str | The unique ID for the `spending_plan`.
    iteration_item_guid = 'SII-a4dc1549-da28-1245-9c9c-53eee4cdfbe3' # str | The unique ID for the `iteration_item`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # Read a spending plan iteration item
        api_response = api_instance.read_spending_plan_iteration_item(user_guid, spending_plan_guid, iteration_item_guid, page=page, records_per_page=records_per_page)
        print("The response of SpendingPlanApi->read_spending_plan_iteration_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpendingPlanApi->read_spending_plan_iteration_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **spending_plan_guid** | **str**| The unique ID for the &#x60;spending_plan&#x60;. | 
 **iteration_item_guid** | **str**| The unique ID for the &#x60;iteration_item&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

### Return type

[**SpendingPlanIterationItemResponse**](SpendingPlanIterationItemResponse.md)

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

# **read_spending_plan_user**
> SpendingPlanResponse read_spending_plan_user(user_guid, spending_plan_guid, page=page, records_per_page=records_per_page)

Read a spending plan for a user

Use this endpoint to read the attributes of a specific spending plan according to its unique GUID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.spending_plan_response import SpendingPlanResponse
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
    api_instance = mx_platform_python.SpendingPlanApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    spending_plan_guid = 'SPL-e5f9a5bd-c5b3-4901-bdc0-62119b9db262' # str | The unique ID for the `spending_plan`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # Read a spending plan for a user
        api_response = api_instance.read_spending_plan_user(user_guid, spending_plan_guid, page=page, records_per_page=records_per_page)
        print("The response of SpendingPlanApi->read_spending_plan_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpendingPlanApi->read_spending_plan_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **spending_plan_guid** | **str**| The unique ID for the &#x60;spending_plan&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

### Return type

[**SpendingPlanResponse**](SpendingPlanResponse.md)

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

# **update_spending_plan_iteration_item**
> SpendingPlanIterationItemResponse update_spending_plan_iteration_item(user_guid, spending_plan_guid, iteration_item_guid, spending_plan_iteration_item_create_request_body)

Update a spending plan iteration item

Use this endpoint to update an existing `spending_plan_iteration_item`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.spending_plan_iteration_item_create_request_body import SpendingPlanIterationItemCreateRequestBody
from mx_platform_python.models.spending_plan_iteration_item_response import SpendingPlanIterationItemResponse
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
    api_instance = mx_platform_python.SpendingPlanApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    spending_plan_guid = 'SPL-e5f9a5bd-c5b3-4901-bdc0-62119b9db262' # str | The unique ID for the `spending_plan`.
    iteration_item_guid = 'SII-a4dc1549-da28-1245-9c9c-53eee4cdfbe3' # str | The unique ID for the `iteration_item`.
    spending_plan_iteration_item_create_request_body = mx_platform_python.SpendingPlanIterationItemCreateRequestBody() # SpendingPlanIterationItemCreateRequestBody | Iteration item to be updated with required parameter (planned_amount)

    try:
        # Update a spending plan iteration item
        api_response = api_instance.update_spending_plan_iteration_item(user_guid, spending_plan_guid, iteration_item_guid, spending_plan_iteration_item_create_request_body)
        print("The response of SpendingPlanApi->update_spending_plan_iteration_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpendingPlanApi->update_spending_plan_iteration_item: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **spending_plan_guid** | **str**| The unique ID for the &#x60;spending_plan&#x60;. | 
 **iteration_item_guid** | **str**| The unique ID for the &#x60;iteration_item&#x60;. | 
 **spending_plan_iteration_item_create_request_body** | [**SpendingPlanIterationItemCreateRequestBody**](SpendingPlanIterationItemCreateRequestBody.md)| Iteration item to be updated with required parameter (planned_amount) | 

### Return type

[**SpendingPlanIterationItemResponse**](SpendingPlanIterationItemResponse.md)

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

