# mx_platform_python.GoalsApi

All URIs are relative to *https://api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_user_guid_goals_get**](GoalsApi.md#users_user_guid_goals_get) | **GET** /users/{user_guid}/goals | List goals
[**users_user_guid_goals_goal_guid_delete**](GoalsApi.md#users_user_guid_goals_goal_guid_delete) | **DELETE** /users/{user_guid}/goals/{goal_guid} | Delete a goal
[**users_user_guid_goals_goal_guid_get**](GoalsApi.md#users_user_guid_goals_goal_guid_get) | **GET** /users/{user_guid}/goals/{goal_guid} | Read a goal
[**users_user_guid_goals_goal_guid_put**](GoalsApi.md#users_user_guid_goals_goal_guid_put) | **PUT** /users/{user_guid}/goals/{goal_guid} | Update a goal
[**users_user_guid_goals_post**](GoalsApi.md#users_user_guid_goals_post) | **POST** /users/{user_guid}/goals | Create a goal
[**users_user_guid_goals_reposition_put**](GoalsApi.md#users_user_guid_goals_reposition_put) | **PUT** /users/{user_guid}/goals/reposition | Reposition goals


# **users_user_guid_goals_get**
> GoalsResponseBody users_user_guid_goals_get(user_guid, page=page, records_per_age=records_per_age)

List goals

List all goals a user can set.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.goals_response_body import GoalsResponseBody
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
    api_instance = mx_platform_python.GoalsApi(api_client)
    user_guid = 'user_guid_example' # str | The unique identifier for the user.
    page = 'page_example' # str | Results are returned in paginated sets, this is the page of the results you would like to view. Defaults to page 1 if no page is specified. (optional)
    records_per_age = 'records_per_age_example' # str | The supported range is from 10 to 1000. If the records_per_page parameter is not specified or is outside this range, a default of 25 records per page will be used. (optional)

    try:
        # List goals
        api_response = api_instance.users_user_guid_goals_get(user_guid, page=page, records_per_age=records_per_age)
        print("The response of GoalsApi->users_user_guid_goals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->users_user_guid_goals_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. | 
 **page** | **str**| Results are returned in paginated sets, this is the page of the results you would like to view. Defaults to page 1 if no page is specified. | [optional] 
 **records_per_age** | **str**| The supported range is from 10 to 1000. If the records_per_page parameter is not specified or is outside this range, a default of 25 records per page will be used. | [optional] 

### Return type

[**GoalsResponseBody**](GoalsResponseBody.md)

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

# **users_user_guid_goals_goal_guid_delete**
> users_user_guid_goals_goal_guid_delete(goal_guid, user_guid)

Delete a goal

Delete a goal.

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
    api_instance = mx_platform_python.GoalsApi(api_client)
    goal_guid = 'goal_guid_example' # str | The unique identifier for a goal. Defined by MX.
    user_guid = 'user_guid_example' # str | The unique identifier for a user.

    try:
        # Delete a goal
        api_instance.users_user_guid_goals_goal_guid_delete(goal_guid, user_guid)
    except Exception as e:
        print("Exception when calling GoalsApi->users_user_guid_goals_goal_guid_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_guid** | **str**| The unique identifier for a goal. Defined by MX. | 
 **user_guid** | **str**| The unique identifier for a user. | 

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

# **users_user_guid_goals_goal_guid_get**
> GoalResponseBody users_user_guid_goals_goal_guid_get(goal_guid, user_guid)

Read a goal

Read a specific goal.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.goal_response_body import GoalResponseBody
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
    api_instance = mx_platform_python.GoalsApi(api_client)
    goal_guid = 'goal_guid_example' # str | The unique identifier for a goal. Defined by MX.
    user_guid = 'user_guid_example' # str | The unique identifier for a user.

    try:
        # Read a goal
        api_response = api_instance.users_user_guid_goals_goal_guid_get(goal_guid, user_guid)
        print("The response of GoalsApi->users_user_guid_goals_goal_guid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->users_user_guid_goals_goal_guid_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_guid** | **str**| The unique identifier for a goal. Defined by MX. | 
 **user_guid** | **str**| The unique identifier for a user. | 

### Return type

[**GoalResponseBody**](GoalResponseBody.md)

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

# **users_user_guid_goals_goal_guid_put**
> GoalResponseBody users_user_guid_goals_goal_guid_put(goal_guid, user_guid, update_goal_request_body)

Update a goal

This endpoint updates a specific goal.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.goal_response_body import GoalResponseBody
from mx_platform_python.models.update_goal_request_body import UpdateGoalRequestBody
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
    api_instance = mx_platform_python.GoalsApi(api_client)
    goal_guid = 'goal_guid_example' # str | The unique identifier for a goal. Defined by MX.
    user_guid = 'user_guid_example' # str | The unique identifier for a user.
    update_goal_request_body = mx_platform_python.UpdateGoalRequestBody() # UpdateGoalRequestBody | 

    try:
        # Update a goal
        api_response = api_instance.users_user_guid_goals_goal_guid_put(goal_guid, user_guid, update_goal_request_body)
        print("The response of GoalsApi->users_user_guid_goals_goal_guid_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->users_user_guid_goals_goal_guid_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **goal_guid** | **str**| The unique identifier for a goal. Defined by MX. | 
 **user_guid** | **str**| The unique identifier for a user. | 
 **update_goal_request_body** | [**UpdateGoalRequestBody**](UpdateGoalRequestBody.md)|  | 

### Return type

[**GoalResponseBody**](GoalResponseBody.md)

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

# **users_user_guid_goals_post**
> GoalResponseBody users_user_guid_goals_post(user_guid, goal_request_body)

Create a goal

Create a goal. This endpoint accepts the optional `MX-Skip-Webhook` header and `skip_webhook` parameter.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.goal_request_body import GoalRequestBody
from mx_platform_python.models.goal_response_body import GoalResponseBody
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
    api_instance = mx_platform_python.GoalsApi(api_client)
    user_guid = 'user_guid_example' # str | The unique identifier for the user.
    goal_request_body = mx_platform_python.GoalRequestBody() # GoalRequestBody | 

    try:
        # Create a goal
        api_response = api_instance.users_user_guid_goals_post(user_guid, goal_request_body)
        print("The response of GoalsApi->users_user_guid_goals_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->users_user_guid_goals_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. | 
 **goal_request_body** | [**GoalRequestBody**](GoalRequestBody.md)|  | 

### Return type

[**GoalResponseBody**](GoalResponseBody.md)

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

# **users_user_guid_goals_reposition_put**
> RepositionResponseBody users_user_guid_goals_reposition_put(user_guid, reposition_request_body)

Reposition goals

This endpoint repositions goal priority levels. If one goal is set to a lower priority, then any other goals need to be adjusted accordingly.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.reposition_request_body import RepositionRequestBody
from mx_platform_python.models.reposition_response_body import RepositionResponseBody
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
    api_instance = mx_platform_python.GoalsApi(api_client)
    user_guid = 'user_guid_example' # str | The unique identifier for the user.
    reposition_request_body = mx_platform_python.RepositionRequestBody() # RepositionRequestBody | 

    try:
        # Reposition goals
        api_response = api_instance.users_user_guid_goals_reposition_put(user_guid, reposition_request_body)
        print("The response of GoalsApi->users_user_guid_goals_reposition_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->users_user_guid_goals_reposition_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. | 
 **reposition_request_body** | [**RepositionRequestBody**](RepositionRequestBody.md)|  | 

### Return type

[**RepositionResponseBody**](RepositionResponseBody.md)

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

