# mx_platform_python.UsersApi

All URIs are relative to *https://int-api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /users | Create user
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{user_guid} | Delete user
[**list_users**](UsersApi.md#list_users) | **GET** /users | List users
[**read_user**](UsersApi.md#read_user) | **GET** /users/{user_guid} | Read user
[**update_user**](UsersApi.md#update_user) | **PUT** /users/{user_guid} | Update user


# **create_user**
> UserResponseBody create_user(user_create_request_body)

Create user

Use this endpoint to create a new user. The API will respond with the newly-created user object if successful, containing a `guid` that you'll set as the `user_guid` in other requests when required. Disabling a user means that accounts and transactions associated with it will not be updated in the background by MX. It will also restrict access to that user’s data until they are no longer disabled.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.user_create_request_body import UserCreateRequestBody
from mx_platform_python.models.user_response_body import UserResponseBody
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
    api_instance = mx_platform_python.UsersApi(api_client)
    user_create_request_body = mx_platform_python.UserCreateRequestBody() # UserCreateRequestBody | User object to be created. (None of these parameters are required, but the user object cannot be empty)

    try:
        # Create user
        api_response = api_instance.create_user(user_create_request_body)
        print("The response of UsersApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create_request_body** | [**UserCreateRequestBody**](UserCreateRequestBody.md)| User object to be created. (None of these parameters are required, but the user object cannot be empty) | 

### Return type

[**UserResponseBody**](UserResponseBody.md)

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

# **delete_user**
> delete_user(accept, user_guid)

Delete user

Use this endpoint to delete the specified `user`. The response will have a status of `204 No Content` without an object.  :::warning Deleting a user is permanent. Deleted users can never be restored. For more info, see [Deleting Objects](https://docs.mx.com/api-reference/platform-api/overview/deleting-objects). ::: 

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
    api_instance = mx_platform_python.UsersApi(api_client)
    accept = 'application/vnd.mx.api.v1+json' # str | Specifies the media type expected in the response.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Delete user
        api_instance.delete_user(accept, user_guid)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| Specifies the media type expected in the response. | 
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

# **list_users**
> UsersResponseBody list_users(page=page, records_per_page=records_per_page, id=id, email=email, is_disabled=is_disabled)

List users

Use this endpoint to list every user you've created in the MX Platform API.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.users_response_body import UsersResponseBody
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
    api_instance = mx_platform_python.UsersApi(api_client)
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)
    id = 'u-12324-abdc' # str | The user `id` to search for. (optional)
    email = 'example@example.com' # str | The user `email` to search for. (optional)
    is_disabled = true # bool | Search for users that are diabled. (optional)

    try:
        # List users
        api_response = api_instance.list_users(page=page, records_per_page=records_per_page, id=id, email=email, is_disabled=is_disabled)
        print("The response of UsersApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->list_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 
 **id** | **str**| The user &#x60;id&#x60; to search for. | [optional] 
 **email** | **str**| The user &#x60;email&#x60; to search for. | [optional] 
 **is_disabled** | **bool**| Search for users that are diabled. | [optional] 

### Return type

[**UsersResponseBody**](UsersResponseBody.md)

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

# **read_user**
> UserResponseBody read_user(user_guid)

Read user

Use this endpoint to read the attributes of a specific user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.user_response_body import UserResponseBody
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
    api_instance = mx_platform_python.UsersApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Read user
        api_response = api_instance.read_user(user_guid)
        print("The response of UsersApi->read_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->read_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 

### Return type

[**UserResponseBody**](UserResponseBody.md)

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

# **update_user**
> UserResponseBody update_user(user_guid, user_update_request_body)

Update user

Use this endpoint to update the attributes of the specified user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.user_response_body import UserResponseBody
from mx_platform_python.models.user_update_request_body import UserUpdateRequestBody
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
    api_instance = mx_platform_python.UsersApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    user_update_request_body = mx_platform_python.UserUpdateRequestBody() # UserUpdateRequestBody | User object to be updated (None of these parameters are required, but the user object cannot be empty.)

    try:
        # Update user
        api_response = api_instance.update_user(user_guid, user_update_request_body)
        print("The response of UsersApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **user_update_request_body** | [**UserUpdateRequestBody**](UserUpdateRequestBody.md)| User object to be updated (None of these parameters are required, but the user object cannot be empty.) | 

### Return type

[**UserResponseBody**](UserResponseBody.md)

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

