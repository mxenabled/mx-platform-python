# mx_platform_python.AccountsApi

All URIs are relative to *https://int-api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_manual_account**](AccountsApi.md#create_manual_account) | **POST** /users/{user_guid}/accounts | Create manual account
[**delete_manual_account**](AccountsApi.md#delete_manual_account) | **DELETE** /users/{user_guid}/accounts/{account_guid} | Delete manual account
[**list_account_numbers_by_account**](AccountsApi.md#list_account_numbers_by_account) | **GET** /users/{user_guid}/accounts/{account_guid}/account_numbers | List account numbers by account
[**list_account_numbers_by_member**](AccountsApi.md#list_account_numbers_by_member) | **GET** /users/{user_guid}/members/{member_guid}/account_numbers | List account numbers by member
[**list_account_owners_by_member**](AccountsApi.md#list_account_owners_by_member) | **GET** /users/{user_guid}/members/{member_guid}/account_owners | List account owners by member
[**list_member_accounts**](AccountsApi.md#list_member_accounts) | **GET** /users/{user_guid}/members/{member_guid}/accounts | List accounts by member
[**list_user_accounts**](AccountsApi.md#list_user_accounts) | **GET** /users/{user_guid}/accounts | List accounts
[**read_account**](AccountsApi.md#read_account) | **GET** /users/{user_guid}/accounts/{account_guid} | Read account
[**read_account_by_member**](AccountsApi.md#read_account_by_member) | **GET** /users/{user_guid}/members/{member_guid}/accounts/{account_guid} | Read account by member
[**update_account_by_member**](AccountsApi.md#update_account_by_member) | **PUT** /users/{user_guid}/members/{member_guid}/accounts/{account_guid} | Update account by member


# **create_manual_account**
> AccountResponseBody create_manual_account(user_guid, account_create_request_body)

Create manual account

This endpoint can only be used to create manual accounts. Creating a manual account will automatically create it under the Manual Institution member. Since a manual account has no credentials tied to the member, the account will never aggregate or include data from a data feed..

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.account_create_request_body import AccountCreateRequestBody
from mx_platform_python.models.account_response_body import AccountResponseBody
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
    api_instance = mx_platform_python.AccountsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    account_create_request_body = mx_platform_python.AccountCreateRequestBody() # AccountCreateRequestBody | Manual account object to be created.

    try:
        # Create manual account
        api_response = api_instance.create_manual_account(user_guid, account_create_request_body)
        print("The response of AccountsApi->create_manual_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->create_manual_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **account_create_request_body** | [**AccountCreateRequestBody**](AccountCreateRequestBody.md)| Manual account object to be created. | 

### Return type

[**AccountResponseBody**](AccountResponseBody.md)

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

# **delete_manual_account**
> delete_manual_account(account_guid, accept, user_guid)

Delete manual account

This endpoint deletes accounts that were manually created. The API will respond with an empty object and a status of `204 No Content`.

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
    api_instance = mx_platform_python.AccountsApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    accept = 'application/vnd.mx.api.v1+json' # str | Specifies the media type expected in the response.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Delete manual account
        api_instance.delete_manual_account(account_guid, accept, user_guid)
    except Exception as e:
        print("Exception when calling AccountsApi->delete_manual_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
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
**204** | No content. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_account_numbers_by_account**
> AccountNumbersResponseBody list_account_numbers_by_account(account_guid, user_guid, page=page, records_per_page=records_per_page)

List account numbers by account

This endpoint returns a list of account numbers associated with the specified `account`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.account_numbers_response_body import AccountNumbersResponseBody
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
    api_instance = mx_platform_python.AccountsApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # List account numbers by account
        api_response = api_instance.list_account_numbers_by_account(account_guid, user_guid, page=page, records_per_page=records_per_page)
        print("The response of AccountsApi->list_account_numbers_by_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->list_account_numbers_by_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

### Return type

[**AccountNumbersResponseBody**](AccountNumbersResponseBody.md)

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

# **list_account_numbers_by_member**
> AccountNumbersResponseBody list_account_numbers_by_member(member_guid, user_guid, page=page, records_per_page=records_per_page)

List account numbers by member

This endpoint returns a list of account numbers associated with the specified `member`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.account_numbers_response_body import AccountNumbersResponseBody
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
    api_instance = mx_platform_python.AccountsApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # List account numbers by member
        api_response = api_instance.list_account_numbers_by_member(member_guid, user_guid, page=page, records_per_page=records_per_page)
        print("The response of AccountsApi->list_account_numbers_by_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->list_account_numbers_by_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

### Return type

[**AccountNumbersResponseBody**](AccountNumbersResponseBody.md)

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

# **list_account_owners_by_member**
> AccountOwnersResponseBody list_account_owners_by_member(member_guid, user_guid, page=page, records_per_page=records_per_page)

List account owners by member

This endpoint returns an array with information about every account associated with a particular member.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.account_owners_response_body import AccountOwnersResponseBody
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
    api_instance = mx_platform_python.AccountsApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # List account owners by member
        api_response = api_instance.list_account_owners_by_member(member_guid, user_guid, page=page, records_per_page=records_per_page)
        print("The response of AccountsApi->list_account_owners_by_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->list_account_owners_by_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

### Return type

[**AccountOwnersResponseBody**](AccountOwnersResponseBody.md)

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

# **list_member_accounts**
> AccountsResponseBody list_member_accounts(user_guid, member_guid, member_is_managed_by_user=member_is_managed_by_user, page=page, records_per_page=records_per_page)

List accounts by member

This endpoint returns a list of all the accounts associated with the specified `member`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.accounts_response_body import AccountsResponseBody
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
    api_instance = mx_platform_python.AccountsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    member_is_managed_by_user = true # bool | List only accounts whose member is managed by the user. (optional)
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # List accounts by member
        api_response = api_instance.list_member_accounts(user_guid, member_guid, member_is_managed_by_user=member_is_managed_by_user, page=page, records_per_page=records_per_page)
        print("The response of AccountsApi->list_member_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->list_member_accounts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **member_is_managed_by_user** | **bool**| List only accounts whose member is managed by the user. | [optional] 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

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

# **list_user_accounts**
> AccountsResponseBody list_user_accounts(user_guid, page=page, member_is_managed_by_user=member_is_managed_by_user, is_manual=is_manual, records_per_page=records_per_page, use_case=use_case)

List accounts

This endpoint returns a list of all the accounts associated with the specified `user`.  :::warning This request will not return the full account number. It may return the last four digits of the account number if that information has been provided during aggregation. If you need the full account number, please refer to [List account numbers by member](/api-reference/platform-api/reference/list-account-numbers-by-member/) or [List account numbers by account](/api-reference/platform-api/reference/list-account-numbers-by-account/). ::: 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.accounts_response_body import AccountsResponseBody
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
    api_instance = mx_platform_python.AccountsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    member_is_managed_by_user = true # bool | List only accounts whose member is managed by the user. (optional)
    is_manual = true # bool | List only accounts that were manually created. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)
    use_case = 'MONEY_MOVEMENT' # str | The use case associated with the member. Valid values are `PFM` and `MONEY_MOVEMENT`. For example, you can append either `?use_case=PFM` or `?use_case=MONEY_MOVEMENT`. (optional)

    try:
        # List accounts
        api_response = api_instance.list_user_accounts(user_guid, page=page, member_is_managed_by_user=member_is_managed_by_user, is_manual=is_manual, records_per_page=records_per_page, use_case=use_case)
        print("The response of AccountsApi->list_user_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->list_user_accounts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **member_is_managed_by_user** | **bool**| List only accounts whose member is managed by the user. | [optional] 
 **is_manual** | **bool**| List only accounts that were manually created. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 
 **use_case** | **str**| The use case associated with the member. Valid values are &#x60;PFM&#x60; and &#x60;MONEY_MOVEMENT&#x60;. For example, you can append either &#x60;?use_case&#x3D;PFM&#x60; or &#x60;?use_case&#x3D;MONEY_MOVEMENT&#x60;. | [optional] 

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

# **read_account**
> AccountResponseBody read_account(account_guid, user_guid)

Read account

This endpoint returns the specified `account` resource.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.account_response_body import AccountResponseBody
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
    api_instance = mx_platform_python.AccountsApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Read account
        api_response = api_instance.read_account(account_guid, user_guid)
        print("The response of AccountsApi->read_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->read_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 

### Return type

[**AccountResponseBody**](AccountResponseBody.md)

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

# **read_account_by_member**
> AccountResponseBody read_account_by_member(account_guid, member_guid, user_guid)

Read account by member

This endpoint allows you to read the attributes of an `account` resource.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.account_response_body import AccountResponseBody
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
    api_instance = mx_platform_python.AccountsApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Read account by member
        api_response = api_instance.read_account_by_member(account_guid, member_guid, user_guid)
        print("The response of AccountsApi->read_account_by_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->read_account_by_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 

### Return type

[**AccountResponseBody**](AccountResponseBody.md)

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

# **update_account_by_member**
> AccountResponseBody update_account_by_member(account_guid, member_guid, user_guid, account_update_request_body)

Update account by member

This endpoint allows you to update certain attributes of an `account` resource, including manual accounts. For manual accounts, you can update every field listed. For aggregated accounts, you can only update `is_business`, `is_hidden` and `metadata`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.account_response_body import AccountResponseBody
from mx_platform_python.models.account_update_request_body import AccountUpdateRequestBody
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
    api_instance = mx_platform_python.AccountsApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    account_update_request_body = mx_platform_python.AccountUpdateRequestBody() # AccountUpdateRequestBody | 

    try:
        # Update account by member
        api_response = api_instance.update_account_by_member(account_guid, member_guid, user_guid, account_update_request_body)
        print("The response of AccountsApi->update_account_by_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->update_account_by_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **account_update_request_body** | [**AccountUpdateRequestBody**](AccountUpdateRequestBody.md)|  | 

### Return type

[**AccountResponseBody**](AccountResponseBody.md)

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

