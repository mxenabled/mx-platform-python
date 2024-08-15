# mx_platform_python.BudgetsApi

All URIs are relative to *https://api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_user_guid_budgets_budget_guid_delete**](BudgetsApi.md#users_user_guid_budgets_budget_guid_delete) | **DELETE** /users/{user_guid}/budgets/{budget_guid} | Delete a budget
[**users_user_guid_budgets_budget_guid_get**](BudgetsApi.md#users_user_guid_budgets_budget_guid_get) | **GET** /users/{user_guid}/budgets/{budget_guid} | Read a specific budget
[**users_user_guid_budgets_budget_guid_put**](BudgetsApi.md#users_user_guid_budgets_budget_guid_put) | **PUT** /users/{user_guid}/budgets/{budget_guid} | Update a specific budget
[**users_user_guid_budgets_generate_post**](BudgetsApi.md#users_user_guid_budgets_generate_post) | **POST** /users/{user_guid}/budgets/generate | Auto-generate budgets
[**users_user_guid_budgets_get**](BudgetsApi.md#users_user_guid_budgets_get) | **GET** /users/{user_guid}/budgets | List all budgets
[**users_user_guid_budgets_post**](BudgetsApi.md#users_user_guid_budgets_post) | **POST** /users/{user_guid}/budgets | Create a budget


# **users_user_guid_budgets_budget_guid_delete**
> users_user_guid_budgets_budget_guid_delete(user_guid, budget_guid)

Delete a budget

Delete a budget.

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
    api_instance = mx_platform_python.BudgetsApi(api_client)
    user_guid = 'user_guid_example' # str | The unique identifier for the budget. Defined by MX.
    budget_guid = 'budget_guid_example' # str | The unique identifier for the budget. Defined by MX.

    try:
        # Delete a budget
        api_instance.users_user_guid_budgets_budget_guid_delete(user_guid, budget_guid)
    except Exception as e:
        print("Exception when calling BudgetsApi->users_user_guid_budgets_budget_guid_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the budget. Defined by MX. | 
 **budget_guid** | **str**| The unique identifier for the budget. Defined by MX. | 

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
**204** | No content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_user_guid_budgets_budget_guid_get**
> BudgetResponseBody users_user_guid_budgets_budget_guid_get(budget_guid, user_guid)

Read a specific budget

Read a specific budget.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.budget_response_body import BudgetResponseBody
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
    api_instance = mx_platform_python.BudgetsApi(api_client)
    budget_guid = 'budget_guid_example' # str | The unique identifier for the budget. Defined by MX.
    user_guid = 'user_guid_example' # str | The unique identifier for the budget. Defined by MX.

    try:
        # Read a specific budget
        api_response = api_instance.users_user_guid_budgets_budget_guid_get(budget_guid, user_guid)
        print("The response of BudgetsApi->users_user_guid_budgets_budget_guid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->users_user_guid_budgets_budget_guid_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **budget_guid** | **str**| The unique identifier for the budget. Defined by MX. | 
 **user_guid** | **str**| The unique identifier for the budget. Defined by MX. | 

### Return type

[**BudgetResponseBody**](BudgetResponseBody.md)

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

# **users_user_guid_budgets_budget_guid_put**
> BudgetResponseBody users_user_guid_budgets_budget_guid_put(user_guid, budget_guid, budget_update_request_body=budget_update_request_body)

Update a specific budget

Update a specific budget.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.budget_response_body import BudgetResponseBody
from mx_platform_python.models.budget_update_request_body import BudgetUpdateRequestBody
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
    api_instance = mx_platform_python.BudgetsApi(api_client)
    user_guid = 'user_guid_example' # str | The unique identifier for the budget. Defined by MX.
    budget_guid = 'budget_guid_example' # str | The unique identifier for the budget. Defined by MX.
    budget_update_request_body = mx_platform_python.BudgetUpdateRequestBody() # BudgetUpdateRequestBody |  (optional)

    try:
        # Update a specific budget
        api_response = api_instance.users_user_guid_budgets_budget_guid_put(user_guid, budget_guid, budget_update_request_body=budget_update_request_body)
        print("The response of BudgetsApi->users_user_guid_budgets_budget_guid_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->users_user_guid_budgets_budget_guid_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the budget. Defined by MX. | 
 **budget_guid** | **str**| The unique identifier for the budget. Defined by MX. | 
 **budget_update_request_body** | [**BudgetUpdateRequestBody**](BudgetUpdateRequestBody.md)|  | [optional] 

### Return type

[**BudgetResponseBody**](BudgetResponseBody.md)

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

# **users_user_guid_budgets_generate_post**
> BudgetResponseBody users_user_guid_budgets_generate_post(user_guid)

Auto-generate budgets

This endpoint will automatically create budgets for several categories based on existing transactions; these budgets are returned as an array. Specifically, budgets will only be generated if the `user` has at least one `transaction` in a given category during each of the two previous calendar months. For example, if the request is made on March 6, and there is at least one \"Bills & Utilities\" `transaction` in both January and February, a budget will be generated for \"Bills & Utilities.\" If there are two \"Bills & Utilities\" transactions in February but none in January, no budget will be generated for that category. If budgets already exist for particular categories, new budgets will be generated and returned based on the available transactions. If one or more budgets remain unchanged, they will nevertheless be returned in the response. If no transaction data for the `user` meet the above criteria, a `422 Unprocessable Entity` error will be returned with status code 4221 along with the message, `There aren't enough transactions to automatically create any budgets`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.budget_response_body import BudgetResponseBody
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
    api_instance = mx_platform_python.BudgetsApi(api_client)
    user_guid = 'user_guid_example' # str | The unique identifier for the user. Defined by MX.

    try:
        # Auto-generate budgets
        api_response = api_instance.users_user_guid_budgets_generate_post(user_guid)
        print("The response of BudgetsApi->users_user_guid_budgets_generate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->users_user_guid_budgets_generate_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. Defined by MX. | 

### Return type

[**BudgetResponseBody**](BudgetResponseBody.md)

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

# **users_user_guid_budgets_get**
> BudgetResponseBody users_user_guid_budgets_get(user_guid)

List all budgets

List all budgets

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.budget_response_body import BudgetResponseBody
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
    api_instance = mx_platform_python.BudgetsApi(api_client)
    user_guid = 'user_guid_example' # str | The unique identifier for the user. Defined by MX.

    try:
        # List all budgets
        api_response = api_instance.users_user_guid_budgets_get(user_guid)
        print("The response of BudgetsApi->users_user_guid_budgets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->users_user_guid_budgets_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. Defined by MX. | 

### Return type

[**BudgetResponseBody**](BudgetResponseBody.md)

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

# **users_user_guid_budgets_post**
> BudgetResponseBody users_user_guid_budgets_post(user_guid, budget_create_request_body)

Create a budget

Create a budget. This endpoint accepts the optional `MX-Skip-Webhook` header and `skip_webhook` parameter. You cannot create a duplicate budget. For example, if you attempt to create a budget for \"Gas\", but that budget already exist, the request will fail. You can retrieve a list of all existing categories by using the List Categories endpoint.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.budget_create_request_body import BudgetCreateRequestBody
from mx_platform_python.models.budget_response_body import BudgetResponseBody
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
    api_instance = mx_platform_python.BudgetsApi(api_client)
    user_guid = 'user_guid_example' # str | The unique identifier for the user. Defined by MX.
    budget_create_request_body = mx_platform_python.BudgetCreateRequestBody() # BudgetCreateRequestBody | 

    try:
        # Create a budget
        api_response = api_instance.users_user_guid_budgets_post(user_guid, budget_create_request_body)
        print("The response of BudgetsApi->users_user_guid_budgets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BudgetsApi->users_user_guid_budgets_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. Defined by MX. | 
 **budget_create_request_body** | [**BudgetCreateRequestBody**](BudgetCreateRequestBody.md)|  | 

### Return type

[**BudgetResponseBody**](BudgetResponseBody.md)

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

