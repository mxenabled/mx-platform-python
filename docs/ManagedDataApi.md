# mx_platform_python.ManagedDataApi

All URIs are relative to *https://int-api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_managed_account**](ManagedDataApi.md#create_managed_account) | **POST** /users/{user_guid}/managed_members/{member_guid}/accounts | Create managed account
[**create_managed_member**](ManagedDataApi.md#create_managed_member) | **POST** /users/{user_guid}/managed_members | Create managed member
[**create_managed_transaction**](ManagedDataApi.md#create_managed_transaction) | **POST** /users/{user_guid}/managed_members/{member_guid}/accounts/{account_guid}/transactions | Create managed transaction
[**delete_managed_account**](ManagedDataApi.md#delete_managed_account) | **DELETE** /users/{user_guid}/managed_members/{member_guid}/accounts/{account_guid} | Delete managed account
[**delete_managed_member**](ManagedDataApi.md#delete_managed_member) | **DELETE** /users/{user_guid}/managed_members/{member_guid} | Delete managed member
[**delete_managed_transaction**](ManagedDataApi.md#delete_managed_transaction) | **DELETE** /users/{user_guid}/managed_members/{member_guid}/accounts/{account_guid}/transactions/{transaction_guid} | Delete managed transaction
[**list_managed_accounts**](ManagedDataApi.md#list_managed_accounts) | **GET** /users/{user_guid}/managed_members/{member_guid}/accounts | List managed accounts
[**list_managed_institutions**](ManagedDataApi.md#list_managed_institutions) | **GET** /managed_institutions | List managed institutions
[**list_managed_members**](ManagedDataApi.md#list_managed_members) | **GET** /users/{user_guid}/managed_members | List managed members
[**list_managed_transactions**](ManagedDataApi.md#list_managed_transactions) | **GET** /users/{user_guid}/managed_members/{member_guid}/accounts/{account_guid}/transactions | List managed transactions
[**read_managed_account**](ManagedDataApi.md#read_managed_account) | **GET** /users/{user_guid}/managed_members/{member_guid}/accounts/{account_guid} | Read managed account
[**read_managed_member**](ManagedDataApi.md#read_managed_member) | **GET** /users/{user_guid}/managed_members/{member_guid} | Read managed member
[**read_managed_transaction**](ManagedDataApi.md#read_managed_transaction) | **GET** /users/{user_guid}/managed_members/{member_guid}/accounts/{account_guid}/transactions/{transaction_guid} | Read managed transaction
[**update_managed_account**](ManagedDataApi.md#update_managed_account) | **PUT** /users/{user_guid}/managed_members/{member_guid}/accounts/{account_guid} | Update managed account
[**update_managed_member**](ManagedDataApi.md#update_managed_member) | **PUT** /users/{user_guid}/managed_members/{member_guid} | Update managed member
[**update_managed_transaction**](ManagedDataApi.md#update_managed_transaction) | **PUT** /users/{user_guid}/managed_members/{member_guid}/accounts/{account_guid}/transactions/{transaction_guid} | Update managed transaction


# **create_managed_account**
> AccountResponseBody create_managed_account(member_guid, user_guid, managed_account_create_request_body)

Create managed account

Use this endpoint to create a partner-managed account.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.account_response_body import AccountResponseBody
from mx_platform_python.models.managed_account_create_request_body import ManagedAccountCreateRequestBody
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
    api_instance = mx_platform_python.ManagedDataApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    managed_account_create_request_body = mx_platform_python.ManagedAccountCreateRequestBody() # ManagedAccountCreateRequestBody | Managed account to be created.

    try:
        # Create managed account
        api_response = api_instance.create_managed_account(member_guid, user_guid, managed_account_create_request_body)
        print("The response of ManagedDataApi->create_managed_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDataApi->create_managed_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **managed_account_create_request_body** | [**ManagedAccountCreateRequestBody**](ManagedAccountCreateRequestBody.md)| Managed account to be created. | 

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

# **create_managed_member**
> MemberResponseBody create_managed_member(user_guid, managed_member_create_request_body)

Create managed member

Use this endpoint to create a new partner-managed `member`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.managed_member_create_request_body import ManagedMemberCreateRequestBody
from mx_platform_python.models.member_response_body import MemberResponseBody
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
    api_instance = mx_platform_python.ManagedDataApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    managed_member_create_request_body = mx_platform_python.ManagedMemberCreateRequestBody() # ManagedMemberCreateRequestBody | Managed member to be created.

    try:
        # Create managed member
        api_response = api_instance.create_managed_member(user_guid, managed_member_create_request_body)
        print("The response of ManagedDataApi->create_managed_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDataApi->create_managed_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **managed_member_create_request_body** | [**ManagedMemberCreateRequestBody**](ManagedMemberCreateRequestBody.md)| Managed member to be created. | 

### Return type

[**MemberResponseBody**](MemberResponseBody.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.mx.api.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_managed_transaction**
> TransactionResponseBody create_managed_transaction(account_guid, member_guid, user_guid, managed_transaction_create_request_body)

Create managed transaction

Use this endpoint to create a new partner-managed `transaction`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.managed_transaction_create_request_body import ManagedTransactionCreateRequestBody
from mx_platform_python.models.transaction_response_body import TransactionResponseBody
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
    api_instance = mx_platform_python.ManagedDataApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    managed_transaction_create_request_body = mx_platform_python.ManagedTransactionCreateRequestBody() # ManagedTransactionCreateRequestBody | Managed transaction to be created.

    try:
        # Create managed transaction
        api_response = api_instance.create_managed_transaction(account_guid, member_guid, user_guid, managed_transaction_create_request_body)
        print("The response of ManagedDataApi->create_managed_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDataApi->create_managed_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **managed_transaction_create_request_body** | [**ManagedTransactionCreateRequestBody**](ManagedTransactionCreateRequestBody.md)| Managed transaction to be created. | 

### Return type

[**TransactionResponseBody**](TransactionResponseBody.md)

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

# **delete_managed_account**
> delete_managed_account(account_guid, member_guid, user_guid)

Delete managed account

Use this endpoint to delete a partner-managed account according to its unique GUID. If successful, the API will respond with a status of `204 No Content`.

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
    api_instance = mx_platform_python.ManagedDataApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Delete managed account
        api_instance.delete_managed_account(account_guid, member_guid, user_guid)
    except Exception as e:
        print("Exception when calling ManagedDataApi->delete_managed_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
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

# **delete_managed_member**
> delete_managed_member(member_guid, accept, user_guid)

Delete managed member

Use this endpoint to delete the specified partner-managed `member`. The endpoint will respond with a status of `204 No Content` without a resource.

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
    api_instance = mx_platform_python.ManagedDataApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    accept = 'application/vnd.mx.api.v1+json' # str | Specifies the media type expected in the response.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Delete managed member
        api_instance.delete_managed_member(member_guid, accept, user_guid)
    except Exception as e:
        print("Exception when calling ManagedDataApi->delete_managed_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
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

# **delete_managed_transaction**
> delete_managed_transaction(account_guid, member_guid, transaction_guid, user_guid)

Delete managed transaction

Use this endpoint to delete the specified partner-managed `transaction`. The endpoint will respond with a status of `204 No Content` without a resource.

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
    api_instance = mx_platform_python.ManagedDataApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    transaction_guid = 'TRN-810828b0-5210-4878-9bd3-f4ce514f90c4' # str | The unique id for a `transaction`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Delete managed transaction
        api_instance.delete_managed_transaction(account_guid, member_guid, transaction_guid, user_guid)
    except Exception as e:
        print("Exception when calling ManagedDataApi->delete_managed_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **transaction_guid** | **str**| The unique id for a &#x60;transaction&#x60;. | 
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

# **list_managed_accounts**
> AccountsResponseBody list_managed_accounts(member_guid, user_guid, page=page, records_per_page=records_per_page)

List managed accounts

Use this endpoint to retrieve a list of all the partner-managed accounts associated with the given partner-managed member.

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
    api_instance = mx_platform_python.ManagedDataApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # List managed accounts
        api_response = api_instance.list_managed_accounts(member_guid, user_guid, page=page, records_per_page=records_per_page)
        print("The response of ManagedDataApi->list_managed_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDataApi->list_managed_accounts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
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

# **list_managed_institutions**
> InstitutionsResponseBody list_managed_institutions(page=page, records_per_page=records_per_page)

List managed institutions

This endpoint returns a list of institutions which can be used to create partner-managed members.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.institutions_response_body import InstitutionsResponseBody
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
    api_instance = mx_platform_python.ManagedDataApi(api_client)
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # List managed institutions
        api_response = api_instance.list_managed_institutions(page=page, records_per_page=records_per_page)
        print("The response of ManagedDataApi->list_managed_institutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDataApi->list_managed_institutions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

### Return type

[**InstitutionsResponseBody**](InstitutionsResponseBody.md)

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

# **list_managed_members**
> MembersResponseBody list_managed_members(user_guid, page=page, records_per_page=records_per_page)

List managed members

This endpoint returns a list of all the partner-managed members associated with the specified `user`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.members_response_body import MembersResponseBody
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
    api_instance = mx_platform_python.ManagedDataApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # List managed members
        api_response = api_instance.list_managed_members(user_guid, page=page, records_per_page=records_per_page)
        print("The response of ManagedDataApi->list_managed_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDataApi->list_managed_members: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

### Return type

[**MembersResponseBody**](MembersResponseBody.md)

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

# **list_managed_transactions**
> TransactionsResponseBody list_managed_transactions(account_guid, member_guid, user_guid, page=page, from_date=from_date, to_date=to_date, records_per_page=records_per_page)

List managed transactions

This endpoint returns a list of all the partner-managed transactions associated with the specified `account`, scoped through a `user` and a `member`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.transactions_response_body import TransactionsResponseBody
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
    api_instance = mx_platform_python.ManagedDataApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    from_date = '2024-01-01' # str | Filter transactions from this date. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 120 days ago if not provided. (optional)
    to_date = '2024-03-31' # str | Filter transactions to this date (at midnight). This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 5 days forward from the day the request is made to capture pending transactions. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # List managed transactions
        api_response = api_instance.list_managed_transactions(account_guid, member_guid, user_guid, page=page, from_date=from_date, to_date=to_date, records_per_page=records_per_page)
        print("The response of ManagedDataApi->list_managed_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDataApi->list_managed_transactions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **from_date** | **str**| Filter transactions from this date. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 120 days ago if not provided. | [optional] 
 **to_date** | **str**| Filter transactions to this date (at midnight). This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 5 days forward from the day the request is made to capture pending transactions. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

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

# **read_managed_account**
> AccountResponseBody read_managed_account(account_guid, member_guid, user_guid)

Read managed account

Use this endpoint to read the attributes of a partner-managed account according to its unique guid.

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
    api_instance = mx_platform_python.ManagedDataApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Read managed account
        api_response = api_instance.read_managed_account(account_guid, member_guid, user_guid)
        print("The response of ManagedDataApi->read_managed_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDataApi->read_managed_account: %s\n" % e)
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

# **read_managed_member**
> MemberResponseBody read_managed_member(member_guid, user_guid)

Read managed member

This endpoint returns the attributes of the specified partner-managed`member`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.member_response_body import MemberResponseBody
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
    api_instance = mx_platform_python.ManagedDataApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Read managed member
        api_response = api_instance.read_managed_member(member_guid, user_guid)
        print("The response of ManagedDataApi->read_managed_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDataApi->read_managed_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 

### Return type

[**MemberResponseBody**](MemberResponseBody.md)

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

# **read_managed_transaction**
> TransactionResponseBody read_managed_transaction(account_guid, member_guid, transaction_guid, user_guid)

Read managed transaction

Requests to this endpoint will return the attributes of the specified partner-managed `transaction`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.transaction_response_body import TransactionResponseBody
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
    api_instance = mx_platform_python.ManagedDataApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    transaction_guid = 'TRN-810828b0-5210-4878-9bd3-f4ce514f90c4' # str | The unique id for a `transaction`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Read managed transaction
        api_response = api_instance.read_managed_transaction(account_guid, member_guid, transaction_guid, user_guid)
        print("The response of ManagedDataApi->read_managed_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDataApi->read_managed_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **transaction_guid** | **str**| The unique id for a &#x60;transaction&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 

### Return type

[**TransactionResponseBody**](TransactionResponseBody.md)

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

# **update_managed_account**
> AccountResponseBody update_managed_account(account_guid, member_guid, user_guid, managed_account_update_request_body)

Update managed account

Use this endpoint to update the attributes of a partner-managed account according to its unique GUID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.account_response_body import AccountResponseBody
from mx_platform_python.models.managed_account_update_request_body import ManagedAccountUpdateRequestBody
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
    api_instance = mx_platform_python.ManagedDataApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    managed_account_update_request_body = mx_platform_python.ManagedAccountUpdateRequestBody() # ManagedAccountUpdateRequestBody | Managed account object to be updated (While no single parameter is required, the request body can't be empty)

    try:
        # Update managed account
        api_response = api_instance.update_managed_account(account_guid, member_guid, user_guid, managed_account_update_request_body)
        print("The response of ManagedDataApi->update_managed_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDataApi->update_managed_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **managed_account_update_request_body** | [**ManagedAccountUpdateRequestBody**](ManagedAccountUpdateRequestBody.md)| Managed account object to be updated (While no single parameter is required, the request body can&#39;t be empty) | 

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

# **update_managed_member**
> MemberResponseBody update_managed_member(member_guid, user_guid, managed_member_update_request_body)

Update managed member

Use this endpoint to update the attributes of the specified partner_managed `member`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.managed_member_update_request_body import ManagedMemberUpdateRequestBody
from mx_platform_python.models.member_response_body import MemberResponseBody
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
    api_instance = mx_platform_python.ManagedDataApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    managed_member_update_request_body = mx_platform_python.ManagedMemberUpdateRequestBody() # ManagedMemberUpdateRequestBody | Managed member object to be updated (While no single parameter is required, the request body can't be empty)

    try:
        # Update managed member
        api_response = api_instance.update_managed_member(member_guid, user_guid, managed_member_update_request_body)
        print("The response of ManagedDataApi->update_managed_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDataApi->update_managed_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **managed_member_update_request_body** | [**ManagedMemberUpdateRequestBody**](ManagedMemberUpdateRequestBody.md)| Managed member object to be updated (While no single parameter is required, the request body can&#39;t be empty) | 

### Return type

[**MemberResponseBody**](MemberResponseBody.md)

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

# **update_managed_transaction**
> TransactionResponseBody update_managed_transaction(account_guid, member_guid, transaction_guid, user_guid, managed_transaction_update_request_body)

Update managed transaction

Use this endpoint to update the attributes of the specified partner_managed `transaction`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.managed_transaction_update_request_body import ManagedTransactionUpdateRequestBody
from mx_platform_python.models.transaction_response_body import TransactionResponseBody
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
    api_instance = mx_platform_python.ManagedDataApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    transaction_guid = 'TRN-810828b0-5210-4878-9bd3-f4ce514f90c4' # str | The unique id for a `transaction`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    managed_transaction_update_request_body = mx_platform_python.ManagedTransactionUpdateRequestBody() # ManagedTransactionUpdateRequestBody | Managed transaction object to be updated (While no single parameter is required, the request body can't be empty)

    try:
        # Update managed transaction
        api_response = api_instance.update_managed_transaction(account_guid, member_guid, transaction_guid, user_guid, managed_transaction_update_request_body)
        print("The response of ManagedDataApi->update_managed_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagedDataApi->update_managed_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **transaction_guid** | **str**| The unique id for a &#x60;transaction&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **managed_transaction_update_request_body** | [**ManagedTransactionUpdateRequestBody**](ManagedTransactionUpdateRequestBody.md)| Managed transaction object to be updated (While no single parameter is required, the request body can&#39;t be empty) | 

### Return type

[**TransactionResponseBody**](TransactionResponseBody.md)

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

