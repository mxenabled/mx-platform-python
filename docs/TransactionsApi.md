# mx_platform_python.TransactionsApi

All URIs are relative to *https://int-api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_manual_transaction**](TransactionsApi.md#create_manual_transaction) | **POST** /users/{user_guid}/accounts/{account_guid}/transactions | Create manual transaction
[**create_split_transactions**](TransactionsApi.md#create_split_transactions) | **POST** /users/{user_guid}/transactions/{transaction_guid}/split | Create split transactions
[**delete_manual_transactions**](TransactionsApi.md#delete_manual_transactions) | **DELETE** /users/{user_guid}/transactions/{transaction_guid} | Delete manual transactions
[**delete_split_transactions**](TransactionsApi.md#delete_split_transactions) | **DELETE** /users/{user_guid}/transactions/{transaction_guid}/split | Delete split transactions
[**delete_transaction_rule**](TransactionsApi.md#delete_transaction_rule) | **DELETE** /users/{user_guid}/transaction_rules/{transaction_rule_guid} | Delete transaction rule
[**enhance_transactions**](TransactionsApi.md#enhance_transactions) | **POST** /transactions/enhance | Enhance transactions
[**extend_history**](TransactionsApi.md#extend_history) | **POST** /users/{user_guid}/members/{member_guid}/extend_history | Extend history
[**list_transactions**](TransactionsApi.md#list_transactions) | **GET** /users/{user_guid}/transactions | List transactions
[**list_transactions_by_account**](TransactionsApi.md#list_transactions_by_account) | **GET** /users/{user_guid}/accounts/{account_guid}/transactions | List transactions by account
[**list_transactions_by_member**](TransactionsApi.md#list_transactions_by_member) | **GET** /users/{user_guid}/members/{member_guid}/transactions | List transactions by member
[**list_transactions_by_tag**](TransactionsApi.md#list_transactions_by_tag) | **GET** /users/{user_guid}/tags/{tag_guid}/transactions | List transactions by tag
[**read_transaction**](TransactionsApi.md#read_transaction) | **GET** /users/{user_guid}/transactions/{transaction_guid} | Read transaction
[**repeating_transactions**](TransactionsApi.md#repeating_transactions) | **GET** /users/{user_guid}/repeating_transactions | List Repeating Transactions
[**specific_repeating_transaction**](TransactionsApi.md#specific_repeating_transaction) | **GET** /users/{user_guid}/repeating_transactions/{repeating_transaction_guid} | Get a Repeating Transaction
[**update_transaction**](TransactionsApi.md#update_transaction) | **PUT** /users/{user_guid}/transactions/{transaction_guid} | Update transaction
[**update_transaction_by_account**](TransactionsApi.md#update_transaction_by_account) | **PUT** /users/{user_guid}/members/{member_guid}/accounts/{account_guid}/transactions/{transaction_guid} | Update Transaction by Account


# **create_manual_transaction**
> TransactionCreateResponseBody create_manual_transaction(user_guid, account_guid, transaction_create_request_body)

Create manual transaction

This endpoint can only be used to create manual transactions that are under a manual account. This endpoint accepts the optional MX-Skip-Webhook header and skip_webhook parameter.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.transaction_create_request_body import TransactionCreateRequestBody
from mx_platform_python.models.transaction_create_response_body import TransactionCreateResponseBody
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
    api_instance = mx_platform_python.TransactionsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    transaction_create_request_body = mx_platform_python.TransactionCreateRequestBody() # TransactionCreateRequestBody | 

    try:
        # Create manual transaction
        api_response = api_instance.create_manual_transaction(user_guid, account_guid, transaction_create_request_body)
        print("The response of TransactionsApi->create_manual_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->create_manual_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **transaction_create_request_body** | [**TransactionCreateRequestBody**](TransactionCreateRequestBody.md)|  | 

### Return type

[**TransactionCreateResponseBody**](TransactionCreateResponseBody.md)

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

# **create_split_transactions**
> SplitTransactionsResponseBody create_split_transactions(transaction_guid, user_guid, split_transaction_request_body=split_transaction_request_body)

Create split transactions

This endpoint creates two or more child transactions that are branched from a previous transaction. This endpoint allows you to link multiple categories, descriptions, and amounts to a parent transaction.  When a split transaction is created, the parent transaction's `has_been_split` field will automatically be updated to true and the child transactions' `parent_guid` will have the transaction guid of the parent. The total amount of the child transactions must equal the amount of the parent transaction. Once a transaction has been split it can't be split again.    In order to re-split a transaction, it must first be un-split. This can be done by calling the Delete Split Transactions endpoint. Calling this endpoint will delete the existing child transactions and update the parent transaction's `has_been_split` field to false. You can then re-split the parent transaction by calling Create Split Transaction again. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.split_transaction_request_body import SplitTransactionRequestBody
from mx_platform_python.models.split_transactions_response_body import SplitTransactionsResponseBody
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
    api_instance = mx_platform_python.TransactionsApi(api_client)
    transaction_guid = 'TRN-810828b0-5210-4878-9bd3-f4ce514f90c4' # str | The unique id for a `transaction`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    split_transaction_request_body = mx_platform_python.SplitTransactionRequestBody() # SplitTransactionRequestBody |  (optional)

    try:
        # Create split transactions
        api_response = api_instance.create_split_transactions(transaction_guid, user_guid, split_transaction_request_body=split_transaction_request_body)
        print("The response of TransactionsApi->create_split_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->create_split_transactions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_guid** | **str**| The unique id for a &#x60;transaction&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **split_transaction_request_body** | [**SplitTransactionRequestBody**](SplitTransactionRequestBody.md)|  | [optional] 

### Return type

[**SplitTransactionsResponseBody**](SplitTransactionsResponseBody.md)

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

# **delete_manual_transactions**
> delete_manual_transactions(user_guid, transaction_guid)

Delete manual transactions

Delete a manual transaction. In the path, use the manual transaction guid as the `transaction_guid`, such as `MAN-810828b0-5210-4878-9bd3-f4ce514f90c4`.

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
    api_instance = mx_platform_python.TransactionsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    transaction_guid = 'TRN-810828b0-5210-4878-9bd3-f4ce514f90c4' # str | The unique id for a `transaction`.

    try:
        # Delete manual transactions
        api_instance.delete_manual_transactions(user_guid, transaction_guid)
    except Exception as e:
        print("Exception when calling TransactionsApi->delete_manual_transactions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **transaction_guid** | **str**| The unique id for a &#x60;transaction&#x60;. | 

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

# **delete_split_transactions**
> delete_split_transactions(transaction_guid, user_guid)

Delete split transactions

This endpoint deletes all split transactions linked to a parent transaction, but it leaves the parent transaction active. This request will also update the parent transaction's has_been_split field to false. This endpoint accepts the optional MX-Skip-Webhook header.

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
    api_instance = mx_platform_python.TransactionsApi(api_client)
    transaction_guid = 'TRN-810828b0-5210-4878-9bd3-f4ce514f90c4' # str | The unique id for a `transaction`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Delete split transactions
        api_instance.delete_split_transactions(transaction_guid, user_guid)
    except Exception as e:
        print("Exception when calling TransactionsApi->delete_split_transactions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**204** | No content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_transaction_rule**
> delete_transaction_rule(transaction_rule_guid, user_guid)

Delete transaction rule

Use this endpoint to permanently delete a transaction rule based on its unique GUID.

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
    api_instance = mx_platform_python.TransactionsApi(api_client)
    transaction_rule_guid = 'TXR-a080e0f9-a2d4-4d6f-9e03-672cc357a4d3' # str | The unique id for a `transaction_rule`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Delete transaction rule
        api_instance.delete_transaction_rule(transaction_rule_guid, user_guid)
    except Exception as e:
        print("Exception when calling TransactionsApi->delete_transaction_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_rule_guid** | **str**| The unique id for a &#x60;transaction_rule&#x60;. | 
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

# **enhance_transactions**
> EnhanceTransactionsResponseBody enhance_transactions(enhance_transactions_request_body)

Enhance transactions

Use this endpoint to categorize, cleanse, and classify transactions. These transactions are not persisted or stored on the MX platform. <br /><br />For more information on returned data, please see the [Enhanced Transactions fields guide](/api-reference/platform-api/reference/transactions-overview#enhanced-transactions).

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.enhance_transactions_request_body import EnhanceTransactionsRequestBody
from mx_platform_python.models.enhance_transactions_response_body import EnhanceTransactionsResponseBody
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
    api_instance = mx_platform_python.TransactionsApi(api_client)
    enhance_transactions_request_body = mx_platform_python.EnhanceTransactionsRequestBody() # EnhanceTransactionsRequestBody | Transaction object to be enhanced

    try:
        # Enhance transactions
        api_response = api_instance.enhance_transactions(enhance_transactions_request_body)
        print("The response of TransactionsApi->enhance_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->enhance_transactions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enhance_transactions_request_body** | [**EnhanceTransactionsRequestBody**](EnhanceTransactionsRequestBody.md)| Transaction object to be enhanced | 

### Return type

[**EnhanceTransactionsResponseBody**](EnhanceTransactionsResponseBody.md)

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

# **extend_history**
> MemberResponseBody extend_history(member_guid, user_guid)

Extend history

Some institutions allow developers to access an extended transaction history with up to 24 months of data associated with a particular member. The process for fetching and then reading this extended transaction history is much like standard aggregation, and it may trigger multi-factor authentication.

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
    api_instance = mx_platform_python.TransactionsApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # Extend history
        api_response = api_instance.extend_history(member_guid, user_guid)
        print("The response of TransactionsApi->extend_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->extend_history: %s\n" % e)
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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_transactions**
> TransactionsResponseBodyIncludes list_transactions(user_guid, page=page, records_per_page=records_per_page, from_date=from_date, to_date=to_date, from_created_at=from_created_at, to_created_at=to_created_at, from_updated_at=from_updated_at, to_updated_at=to_updated_at, category_guid=category_guid, category_guid2=category_guid2, top_level_category_guid=top_level_category_guid, top_level_category_guid2=top_level_category_guid2, use_case=use_case, includes=includes)

List transactions

Requests to this endpoint return a list of transactions associated with the specified `user`, across all members and accounts associated with that `user`. <br /><br />Enhanced transaction data may be requested using the `includes` parameter. To use this optional parameter, the value should include the optional metadata requested such as `repeating_transactions`, `merchants`, `classifications`, `geolocations`. For more information, see the [Optional Enhancement Query Parameter guide](/api-reference/platform-api/reference/transactions-overview#enhanced-transactions#optional-enhancement-query-parameter).

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.transactions_response_body_includes import TransactionsResponseBodyIncludes
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
    api_instance = mx_platform_python.TransactionsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)
    from_date = '2024-01-01' # str | Filter transactions from this date. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 120 days ago if not provided. (optional)
    to_date = '2024-03-31' # str | Filter transactions to this date (at midnight). This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 5 days forward from the day the request is made to capture pending transactions. (optional)
    from_created_at = '2024-01-01' # str | Filter transactions from the date the transaction was created. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. (optional)
    to_created_at = '2024-03-31' # str | Filter transaction to the date in which the transaction was created. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. (optional)
    from_updated_at = '2024-01-01' # str | Filter transactions from the date in which the transaction was updated. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. (optional)
    to_updated_at = '2024-03-31' # str | Filter transactions to the date in which the transaction was updated. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. (optional)
    category_guid = 'category_guid_example' # str | Filter transactions belonging to specified `category_guid`.  For example, `?category_guid=CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874`. (optional)
    category_guid2 = ['category_guid_example'] # List[str] | Filter transactions belonging to any specified `category_guid[]` in url.  For example, `?category_guid[]=CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874`. (optional)
    top_level_category_guid = 'top_level_category_guid_example' # str | Filter transactions belonging to specified `top_level_category_guid`. This must be top level category guid, use `category_guid` for subcategory guid.  For example, `?top_level_category_guid=CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874`. (optional)
    top_level_category_guid2 = ['top_level_category_guid_example'] # List[str] | Filter transactions belonging to any specified `top_level_category_guid[]` in url. This must be top level category guid(s), use `category_guid` for subcategory guid(s).  For example, `?top_level_category_guid[]=CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874`. (optional)
    use_case = 'MONEY_MOVEMENT' # str | The use case associated with the member. Valid values are `PFM` and `MONEY_MOVEMENT`. For example, you can append either `?use_case=PFM` or `?use_case=MONEY_MOVEMENT`. (optional)
    includes = 'repeating_transactions,merchants,classifications,geolocations' # str | Options for enhanced transactions. This query parameter is optional. Possible additional metadata: `repeating_transactions`, `merchants`, `classifications`, `geolocations`. The query value is format sensitive. To retrieve all available enhancements, append:  `?includes=repeating_transactions,merchants,classifications,geolocations`.    The query options may be combined to specific enhancements. For example, to request Repeating Transactions and Geolocation data, use:   `?includes=repeating_transactions,geolocations`.  - Repeating Transactions: Identifies transactions with predictable recurrence patterns (e.g., Bill, Income, Subscription). - Merchants: Enriches transactions with merchant name. - Classifications: Provides more insight into the type of money movement that is occurring on the transaction, whether it be retail or investments. - Geolocation: Provides geographic metadata.  (optional)

    try:
        # List transactions
        api_response = api_instance.list_transactions(user_guid, page=page, records_per_page=records_per_page, from_date=from_date, to_date=to_date, from_created_at=from_created_at, to_created_at=to_created_at, from_updated_at=from_updated_at, to_updated_at=to_updated_at, category_guid=category_guid, category_guid2=category_guid2, top_level_category_guid=top_level_category_guid, top_level_category_guid2=top_level_category_guid2, use_case=use_case, includes=includes)
        print("The response of TransactionsApi->list_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->list_transactions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 
 **from_date** | **str**| Filter transactions from this date. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 120 days ago if not provided. | [optional] 
 **to_date** | **str**| Filter transactions to this date (at midnight). This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 5 days forward from the day the request is made to capture pending transactions. | [optional] 
 **from_created_at** | **str**| Filter transactions from the date the transaction was created. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. | [optional] 
 **to_created_at** | **str**| Filter transaction to the date in which the transaction was created. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. | [optional] 
 **from_updated_at** | **str**| Filter transactions from the date in which the transaction was updated. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. | [optional] 
 **to_updated_at** | **str**| Filter transactions to the date in which the transaction was updated. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. | [optional] 
 **category_guid** | **str**| Filter transactions belonging to specified &#x60;category_guid&#x60;.  For example, &#x60;?category_guid&#x3D;CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874&#x60;. | [optional] 
 **category_guid2** | [**List[str]**](str.md)| Filter transactions belonging to any specified &#x60;category_guid[]&#x60; in url.  For example, &#x60;?category_guid[]&#x3D;CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874&#x60;. | [optional] 
 **top_level_category_guid** | **str**| Filter transactions belonging to specified &#x60;top_level_category_guid&#x60;. This must be top level category guid, use &#x60;category_guid&#x60; for subcategory guid.  For example, &#x60;?top_level_category_guid&#x3D;CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874&#x60;. | [optional] 
 **top_level_category_guid2** | [**List[str]**](str.md)| Filter transactions belonging to any specified &#x60;top_level_category_guid[]&#x60; in url. This must be top level category guid(s), use &#x60;category_guid&#x60; for subcategory guid(s).  For example, &#x60;?top_level_category_guid[]&#x3D;CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874&#x60;. | [optional] 
 **use_case** | **str**| The use case associated with the member. Valid values are &#x60;PFM&#x60; and &#x60;MONEY_MOVEMENT&#x60;. For example, you can append either &#x60;?use_case&#x3D;PFM&#x60; or &#x60;?use_case&#x3D;MONEY_MOVEMENT&#x60;. | [optional] 
 **includes** | **str**| Options for enhanced transactions. This query parameter is optional. Possible additional metadata: &#x60;repeating_transactions&#x60;, &#x60;merchants&#x60;, &#x60;classifications&#x60;, &#x60;geolocations&#x60;. The query value is format sensitive. To retrieve all available enhancements, append:  &#x60;?includes&#x3D;repeating_transactions,merchants,classifications,geolocations&#x60;.    The query options may be combined to specific enhancements. For example, to request Repeating Transactions and Geolocation data, use:   &#x60;?includes&#x3D;repeating_transactions,geolocations&#x60;.  - Repeating Transactions: Identifies transactions with predictable recurrence patterns (e.g., Bill, Income, Subscription). - Merchants: Enriches transactions with merchant name. - Classifications: Provides more insight into the type of money movement that is occurring on the transaction, whether it be retail or investments. - Geolocation: Provides geographic metadata.  | [optional] 

### Return type

[**TransactionsResponseBodyIncludes**](TransactionsResponseBodyIncludes.md)

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

# **list_transactions_by_account**
> TransactionsResponseBodyIncludes list_transactions_by_account(account_guid, user_guid, page=page, records_per_page=records_per_page, from_date=from_date, to_date=to_date, from_created_at=from_created_at, to_created_at=to_created_at, from_updated_at=from_updated_at, to_updated_at=to_updated_at, category_guid=category_guid, category_guid2=category_guid2, top_level_category_guid=top_level_category_guid, top_level_category_guid2=top_level_category_guid2, includes=includes)

List transactions by account

Requests to this endpoint return a list of transactions associated with the specified account. <br /><br /> Enhanced transaction data may be requested using the `includes` parameter. To use this optional parameter, the value should include the optional metadata requested such as `repeating_transactions`, `merchants`, `classifications`, `geolocations`. For more information, see the [Optional Enhancement Query Parameter guide](/api-reference/platform-api/reference/transactions-overview#enhanced-transactions#optional-enhancement-query-parameter).

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.transactions_response_body_includes import TransactionsResponseBodyIncludes
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
    api_instance = mx_platform_python.TransactionsApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)
    from_date = '2024-01-01' # str | Filter transactions from this date. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 120 days ago if not provided. (optional)
    to_date = '2024-03-31' # str | Filter transactions to this date (at midnight). This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 5 days forward from the day the request is made to capture pending transactions. (optional)
    from_created_at = '2024-01-01' # str | Filter transactions from the date the transaction was created. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. (optional)
    to_created_at = '2024-03-31' # str | Filter transaction to the date in which the transaction was created. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. (optional)
    from_updated_at = '2024-01-01' # str | Filter transactions from the date in which the transaction was updated. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. (optional)
    to_updated_at = '2024-03-31' # str | Filter transactions to the date in which the transaction was updated. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. (optional)
    category_guid = 'category_guid_example' # str | Filter transactions belonging to specified `category_guid`.  For example, `?category_guid=CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874`. (optional)
    category_guid2 = ['category_guid_example'] # List[str] | Filter transactions belonging to any specified `category_guid[]` in url.  For example, `?category_guid[]=CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874`. (optional)
    top_level_category_guid = 'top_level_category_guid_example' # str | Filter transactions belonging to specified `top_level_category_guid`. This must be top level category guid, use `category_guid` for subcategory guid.  For example, `?top_level_category_guid=CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874`. (optional)
    top_level_category_guid2 = ['top_level_category_guid_example'] # List[str] | Filter transactions belonging to any specified `top_level_category_guid[]` in url. This must be top level category guid(s), use `category_guid` for subcategory guid(s).  For example, `?top_level_category_guid[]=CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874`. (optional)
    includes = 'repeating_transactions,merchants,classifications,geolocations' # str | Options for enhanced transactions. This query parameter is optional. Possible additional metadata: `repeating_transactions`, `merchants`, `classifications`, `geolocations`. The query value is format sensitive. To retrieve all available enhancements, append:  `?includes=repeating_transactions,merchants,classifications,geolocations`.    The query options may be combined to specific enhancements. For example, to request Repeating Transactions and Geolocation data, use:   `?includes=repeating_transactions,geolocations`.  - Repeating Transactions: Identifies transactions with predictable recurrence patterns (e.g., Bill, Income, Subscription). - Merchants: Enriches transactions with merchant name. - Classifications: Provides more insight into the type of money movement that is occurring on the transaction, whether it be retail or investments. - Geolocation: Provides geographic metadata.  (optional)

    try:
        # List transactions by account
        api_response = api_instance.list_transactions_by_account(account_guid, user_guid, page=page, records_per_page=records_per_page, from_date=from_date, to_date=to_date, from_created_at=from_created_at, to_created_at=to_created_at, from_updated_at=from_updated_at, to_updated_at=to_updated_at, category_guid=category_guid, category_guid2=category_guid2, top_level_category_guid=top_level_category_guid, top_level_category_guid2=top_level_category_guid2, includes=includes)
        print("The response of TransactionsApi->list_transactions_by_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->list_transactions_by_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 
 **from_date** | **str**| Filter transactions from this date. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 120 days ago if not provided. | [optional] 
 **to_date** | **str**| Filter transactions to this date (at midnight). This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 5 days forward from the day the request is made to capture pending transactions. | [optional] 
 **from_created_at** | **str**| Filter transactions from the date the transaction was created. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. | [optional] 
 **to_created_at** | **str**| Filter transaction to the date in which the transaction was created. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. | [optional] 
 **from_updated_at** | **str**| Filter transactions from the date in which the transaction was updated. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. | [optional] 
 **to_updated_at** | **str**| Filter transactions to the date in which the transaction was updated. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. | [optional] 
 **category_guid** | **str**| Filter transactions belonging to specified &#x60;category_guid&#x60;.  For example, &#x60;?category_guid&#x3D;CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874&#x60;. | [optional] 
 **category_guid2** | [**List[str]**](str.md)| Filter transactions belonging to any specified &#x60;category_guid[]&#x60; in url.  For example, &#x60;?category_guid[]&#x3D;CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874&#x60;. | [optional] 
 **top_level_category_guid** | **str**| Filter transactions belonging to specified &#x60;top_level_category_guid&#x60;. This must be top level category guid, use &#x60;category_guid&#x60; for subcategory guid.  For example, &#x60;?top_level_category_guid&#x3D;CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874&#x60;. | [optional] 
 **top_level_category_guid2** | [**List[str]**](str.md)| Filter transactions belonging to any specified &#x60;top_level_category_guid[]&#x60; in url. This must be top level category guid(s), use &#x60;category_guid&#x60; for subcategory guid(s).  For example, &#x60;?top_level_category_guid[]&#x3D;CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874&#x60;. | [optional] 
 **includes** | **str**| Options for enhanced transactions. This query parameter is optional. Possible additional metadata: &#x60;repeating_transactions&#x60;, &#x60;merchants&#x60;, &#x60;classifications&#x60;, &#x60;geolocations&#x60;. The query value is format sensitive. To retrieve all available enhancements, append:  &#x60;?includes&#x3D;repeating_transactions,merchants,classifications,geolocations&#x60;.    The query options may be combined to specific enhancements. For example, to request Repeating Transactions and Geolocation data, use:   &#x60;?includes&#x3D;repeating_transactions,geolocations&#x60;.  - Repeating Transactions: Identifies transactions with predictable recurrence patterns (e.g., Bill, Income, Subscription). - Merchants: Enriches transactions with merchant name. - Classifications: Provides more insight into the type of money movement that is occurring on the transaction, whether it be retail or investments. - Geolocation: Provides geographic metadata.  | [optional] 

### Return type

[**TransactionsResponseBodyIncludes**](TransactionsResponseBodyIncludes.md)

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

# **list_transactions_by_member**
> TransactionsResponseBodyIncludes list_transactions_by_member(member_guid, user_guid, page=page, records_per_page=records_per_page, from_date=from_date, to_date=to_date, from_created_at=from_created_at, to_created_at=to_created_at, from_updated_at=from_updated_at, to_updated_at=to_updated_at, category_guid=category_guid, category_guid2=category_guid2, top_level_category_guid=top_level_category_guid, top_level_category_guid2=top_level_category_guid2, includes=includes)

List transactions by member

Requests to this endpoint return a list of transactions associated with the specified `member`, across all accounts associated with that `member`. <br /><br />Enhanced transaction data may be requested using the `includes` parameter. To use this optional parameter, the value should include the optional metadata requested such as `repeating_transactions`, `merchants`, `classifications`, `geolocations`. For more information, see the [Optional Enhancement Query Parameter guide](/api-reference/platform-api/reference/transactions-overview#enhanced-transactions#optional-enhancement-query-parameter).

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.transactions_response_body_includes import TransactionsResponseBodyIncludes
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
    api_instance = mx_platform_python.TransactionsApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)
    from_date = '2024-01-01' # str | Filter transactions from this date. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 120 days ago if not provided. (optional)
    to_date = '2024-03-31' # str | Filter transactions to this date (at midnight). This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 5 days forward from the day the request is made to capture pending transactions. (optional)
    from_created_at = '2024-01-01' # str | Filter transactions from the date the transaction was created. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. (optional)
    to_created_at = '2024-03-31' # str | Filter transaction to the date in which the transaction was created. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. (optional)
    from_updated_at = '2024-01-01' # str | Filter transactions from the date in which the transaction was updated. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. (optional)
    to_updated_at = '2024-03-31' # str | Filter transactions to the date in which the transaction was updated. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. (optional)
    category_guid = 'category_guid_example' # str | Filter transactions belonging to specified `category_guid`.  For example, `?category_guid=CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874`. (optional)
    category_guid2 = ['category_guid_example'] # List[str] | Filter transactions belonging to any specified `category_guid[]` in url.  For example, `?category_guid[]=CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874`. (optional)
    top_level_category_guid = 'top_level_category_guid_example' # str | Filter transactions belonging to specified `top_level_category_guid`. This must be top level category guid, use `category_guid` for subcategory guid.  For example, `?top_level_category_guid=CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874`. (optional)
    top_level_category_guid2 = ['top_level_category_guid_example'] # List[str] | Filter transactions belonging to any specified `top_level_category_guid[]` in url. This must be top level category guid(s), use `category_guid` for subcategory guid(s).  For example, `?top_level_category_guid[]=CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874`. (optional)
    includes = 'repeating_transactions,merchants,classifications,geolocations' # str | Options for enhanced transactions. This query parameter is optional. Possible additional metadata: `repeating_transactions`, `merchants`, `classifications`, `geolocations`. The query value is format sensitive. To retrieve all available enhancements, append:  `?includes=repeating_transactions,merchants,classifications,geolocations`.    The query options may be combined to specific enhancements. For example, to request Repeating Transactions and Geolocation data, use:   `?includes=repeating_transactions,geolocations`.  - Repeating Transactions: Identifies transactions with predictable recurrence patterns (e.g., Bill, Income, Subscription). - Merchants: Enriches transactions with merchant name. - Classifications: Provides more insight into the type of money movement that is occurring on the transaction, whether it be retail or investments. - Geolocation: Provides geographic metadata.  (optional)

    try:
        # List transactions by member
        api_response = api_instance.list_transactions_by_member(member_guid, user_guid, page=page, records_per_page=records_per_page, from_date=from_date, to_date=to_date, from_created_at=from_created_at, to_created_at=to_created_at, from_updated_at=from_updated_at, to_updated_at=to_updated_at, category_guid=category_guid, category_guid2=category_guid2, top_level_category_guid=top_level_category_guid, top_level_category_guid2=top_level_category_guid2, includes=includes)
        print("The response of TransactionsApi->list_transactions_by_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->list_transactions_by_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 
 **from_date** | **str**| Filter transactions from this date. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 120 days ago if not provided. | [optional] 
 **to_date** | **str**| Filter transactions to this date (at midnight). This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 5 days forward from the day the request is made to capture pending transactions. | [optional] 
 **from_created_at** | **str**| Filter transactions from the date the transaction was created. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. | [optional] 
 **to_created_at** | **str**| Filter transaction to the date in which the transaction was created. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. | [optional] 
 **from_updated_at** | **str**| Filter transactions from the date in which the transaction was updated. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. | [optional] 
 **to_updated_at** | **str**| Filter transactions to the date in which the transaction was updated. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. | [optional] 
 **category_guid** | **str**| Filter transactions belonging to specified &#x60;category_guid&#x60;.  For example, &#x60;?category_guid&#x3D;CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874&#x60;. | [optional] 
 **category_guid2** | [**List[str]**](str.md)| Filter transactions belonging to any specified &#x60;category_guid[]&#x60; in url.  For example, &#x60;?category_guid[]&#x3D;CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874&#x60;. | [optional] 
 **top_level_category_guid** | **str**| Filter transactions belonging to specified &#x60;top_level_category_guid&#x60;. This must be top level category guid, use &#x60;category_guid&#x60; for subcategory guid.  For example, &#x60;?top_level_category_guid&#x3D;CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874&#x60;. | [optional] 
 **top_level_category_guid2** | [**List[str]**](str.md)| Filter transactions belonging to any specified &#x60;top_level_category_guid[]&#x60; in url. This must be top level category guid(s), use &#x60;category_guid&#x60; for subcategory guid(s).  For example, &#x60;?top_level_category_guid[]&#x3D;CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874&#x60;. | [optional] 
 **includes** | **str**| Options for enhanced transactions. This query parameter is optional. Possible additional metadata: &#x60;repeating_transactions&#x60;, &#x60;merchants&#x60;, &#x60;classifications&#x60;, &#x60;geolocations&#x60;. The query value is format sensitive. To retrieve all available enhancements, append:  &#x60;?includes&#x3D;repeating_transactions,merchants,classifications,geolocations&#x60;.    The query options may be combined to specific enhancements. For example, to request Repeating Transactions and Geolocation data, use:   &#x60;?includes&#x3D;repeating_transactions,geolocations&#x60;.  - Repeating Transactions: Identifies transactions with predictable recurrence patterns (e.g., Bill, Income, Subscription). - Merchants: Enriches transactions with merchant name. - Classifications: Provides more insight into the type of money movement that is occurring on the transaction, whether it be retail or investments. - Geolocation: Provides geographic metadata.  | [optional] 

### Return type

[**TransactionsResponseBodyIncludes**](TransactionsResponseBodyIncludes.md)

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

# **list_transactions_by_tag**
> TransactionsResponseBodyIncludes list_transactions_by_tag(user_guid, tag_guid, page=page, records_per_page=records_per_page, from_date=from_date, to_date=to_date, from_created_at=from_created_at, to_created_at=to_created_at, from_updated_at=from_updated_at, to_updated_at=to_updated_at, category_guid=category_guid, category_guid2=category_guid2, top_level_category_guid=top_level_category_guid, top_level_category_guid2=top_level_category_guid2, use_case=use_case, includes=includes)

List transactions by tag

Use this endpoint to get a list of all transactions associated with a particular tag according to the tag's unique GUID. This lists all transactions that have been assigned to a particular tag using the create tagging endpoint. <br /><br />Enhanced transaction data may be requested using the `includes` parameter. To use this optional parameter, the value should include the optional metadata requested such as `repeating_transactions`, `merchants`, `classifications`, `geolocations`. For more information, see the [Optional Enhancement Query Parameter guide](/api-reference/platform-api/reference/transactions-overview#enhanced-transactions#optional-enhancement-query-parameter).

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.transactions_response_body_includes import TransactionsResponseBodyIncludes
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
    api_instance = mx_platform_python.TransactionsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    tag_guid = 'TAG-aef36e72-6294-4c38-844d-e573e80aed52' # str | The unique id for a `tag`.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)
    from_date = '2024-01-01' # str | Filter transactions from this date. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 120 days ago if not provided. (optional)
    to_date = '2024-03-31' # str | Filter transactions to this date (at midnight). This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 5 days forward from the day the request is made to capture pending transactions. (optional)
    from_created_at = '2024-01-01' # str | Filter transactions from the date the transaction was created. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. (optional)
    to_created_at = '2024-03-31' # str | Filter transaction to the date in which the transaction was created. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. (optional)
    from_updated_at = '2024-01-01' # str | Filter transactions from the date in which the transaction was updated. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. (optional)
    to_updated_at = '2024-03-31' # str | Filter transactions to the date in which the transaction was updated. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. (optional)
    category_guid = 'category_guid_example' # str | Filter transactions belonging to specified `category_guid`.  For example, `?category_guid=CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874`. (optional)
    category_guid2 = ['category_guid_example'] # List[str] | Filter transactions belonging to any specified `category_guid[]` in url.  For example, `?category_guid[]=CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874`. (optional)
    top_level_category_guid = 'top_level_category_guid_example' # str | Filter transactions belonging to specified `top_level_category_guid`. This must be top level category guid, use `category_guid` for subcategory guid.  For example, `?top_level_category_guid=CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874`. (optional)
    top_level_category_guid2 = ['top_level_category_guid_example'] # List[str] | Filter transactions belonging to any specified `top_level_category_guid[]` in url. This must be top level category guid(s), use `category_guid` for subcategory guid(s).  For example, `?top_level_category_guid[]=CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874`. (optional)
    use_case = 'MONEY_MOVEMENT' # str | The use case associated with the member. Valid values are `PFM` and `MONEY_MOVEMENT`. For example, you can append either `?use_case=PFM` or `?use_case=MONEY_MOVEMENT`. (optional)
    includes = 'repeating_transactions,merchants,classifications,geolocations' # str | Options for enhanced transactions. This query parameter is optional. Possible additional metadata: `repeating_transactions`, `merchants`, `classifications`, `geolocations`. The query value is format sensitive. To retrieve all available enhancements, append:  `?includes=repeating_transactions,merchants,classifications,geolocations`.    The query options may be combined to specific enhancements. For example, to request Repeating Transactions and Geolocation data, use:   `?includes=repeating_transactions,geolocations`.  - Repeating Transactions: Identifies transactions with predictable recurrence patterns (e.g., Bill, Income, Subscription). - Merchants: Enriches transactions with merchant name. - Classifications: Provides more insight into the type of money movement that is occurring on the transaction, whether it be retail or investments. - Geolocation: Provides geographic metadata.  (optional)

    try:
        # List transactions by tag
        api_response = api_instance.list_transactions_by_tag(user_guid, tag_guid, page=page, records_per_page=records_per_page, from_date=from_date, to_date=to_date, from_created_at=from_created_at, to_created_at=to_created_at, from_updated_at=from_updated_at, to_updated_at=to_updated_at, category_guid=category_guid, category_guid2=category_guid2, top_level_category_guid=top_level_category_guid, top_level_category_guid2=top_level_category_guid2, use_case=use_case, includes=includes)
        print("The response of TransactionsApi->list_transactions_by_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->list_transactions_by_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **tag_guid** | **str**| The unique id for a &#x60;tag&#x60;. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 
 **from_date** | **str**| Filter transactions from this date. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 120 days ago if not provided. | [optional] 
 **to_date** | **str**| Filter transactions to this date (at midnight). This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Defaults to 5 days forward from the day the request is made to capture pending transactions. | [optional] 
 **from_created_at** | **str**| Filter transactions from the date the transaction was created. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. | [optional] 
 **to_created_at** | **str**| Filter transaction to the date in which the transaction was created. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. | [optional] 
 **from_updated_at** | **str**| Filter transactions from the date in which the transaction was updated. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. | [optional] 
 **to_updated_at** | **str**| Filter transactions to the date in which the transaction was updated. This only supports ISO 8601 format without timestamp (YYYY-MM-DD). Maximum date range limit is 6 months. | [optional] 
 **category_guid** | **str**| Filter transactions belonging to specified &#x60;category_guid&#x60;.  For example, &#x60;?category_guid&#x3D;CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874&#x60;. | [optional] 
 **category_guid2** | [**List[str]**](str.md)| Filter transactions belonging to any specified &#x60;category_guid[]&#x60; in url.  For example, &#x60;?category_guid[]&#x3D;CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874&#x60;. | [optional] 
 **top_level_category_guid** | **str**| Filter transactions belonging to specified &#x60;top_level_category_guid&#x60;. This must be top level category guid, use &#x60;category_guid&#x60; for subcategory guid.  For example, &#x60;?top_level_category_guid&#x3D;CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874&#x60;. | [optional] 
 **top_level_category_guid2** | [**List[str]**](str.md)| Filter transactions belonging to any specified &#x60;top_level_category_guid[]&#x60; in url. This must be top level category guid(s), use &#x60;category_guid&#x60; for subcategory guid(s).  For example, &#x60;?top_level_category_guid[]&#x3D;CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874&#x60;. | [optional] 
 **use_case** | **str**| The use case associated with the member. Valid values are &#x60;PFM&#x60; and &#x60;MONEY_MOVEMENT&#x60;. For example, you can append either &#x60;?use_case&#x3D;PFM&#x60; or &#x60;?use_case&#x3D;MONEY_MOVEMENT&#x60;. | [optional] 
 **includes** | **str**| Options for enhanced transactions. This query parameter is optional. Possible additional metadata: &#x60;repeating_transactions&#x60;, &#x60;merchants&#x60;, &#x60;classifications&#x60;, &#x60;geolocations&#x60;. The query value is format sensitive. To retrieve all available enhancements, append:  &#x60;?includes&#x3D;repeating_transactions,merchants,classifications,geolocations&#x60;.    The query options may be combined to specific enhancements. For example, to request Repeating Transactions and Geolocation data, use:   &#x60;?includes&#x3D;repeating_transactions,geolocations&#x60;.  - Repeating Transactions: Identifies transactions with predictable recurrence patterns (e.g., Bill, Income, Subscription). - Merchants: Enriches transactions with merchant name. - Classifications: Provides more insight into the type of money movement that is occurring on the transaction, whether it be retail or investments. - Geolocation: Provides geographic metadata.  | [optional] 

### Return type

[**TransactionsResponseBodyIncludes**](TransactionsResponseBodyIncludes.md)

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

# **read_transaction**
> TransactionsResponseBodyIncludes read_transaction(user_guid, transaction_guid, includes=includes)

Read transaction

Requests to this endpoint will return the attributes of the specified `transaction`. To read a manual transaction, use the manual transaction guid in the path as the `transactionGuid`. <br /><br /> Enhanced transaction data may be requested using the `includes` parameter. To use this optional parameter, the value should include the optional metadata requested such as `repeating_transactions`, `merchants`, `classifications`, `geolocations`. For more information, see the [Optional Enhancement Query Parameter guide](/api-reference/platform-api/reference/transactions-overview#enhanced-transactions#optional-enhancement-query-parameter).

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.transactions_response_body_includes import TransactionsResponseBodyIncludes
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
    api_instance = mx_platform_python.TransactionsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    transaction_guid = 'TRN-810828b0-5210-4878-9bd3-f4ce514f90c4' # str | The unique id for a `transaction`.
    includes = 'repeating_transactions,merchants,classifications,geolocations' # str | Options for enhanced transactions. This query parameter is optional. Possible additional metadata: `repeating_transactions`, `merchants`, `classifications`, `geolocations`. The query value is format sensitive. To retrieve all available enhancements, append:  `?includes=repeating_transactions,merchants,classifications,geolocations`.    The query options may be combined to specific enhancements. For example, to request Repeating Transactions and Geolocation data, use:   `?includes=repeating_transactions,geolocations`.  - Repeating Transactions: Identifies transactions with predictable recurrence patterns (e.g., Bill, Income, Subscription). - Merchants: Enriches transactions with merchant name. - Classifications: Provides more insight into the type of money movement that is occurring on the transaction, whether it be retail or investments. - Geolocation: Provides geographic metadata.  (optional)

    try:
        # Read transaction
        api_response = api_instance.read_transaction(user_guid, transaction_guid, includes=includes)
        print("The response of TransactionsApi->read_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->read_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **transaction_guid** | **str**| The unique id for a &#x60;transaction&#x60;. | 
 **includes** | **str**| Options for enhanced transactions. This query parameter is optional. Possible additional metadata: &#x60;repeating_transactions&#x60;, &#x60;merchants&#x60;, &#x60;classifications&#x60;, &#x60;geolocations&#x60;. The query value is format sensitive. To retrieve all available enhancements, append:  &#x60;?includes&#x3D;repeating_transactions,merchants,classifications,geolocations&#x60;.    The query options may be combined to specific enhancements. For example, to request Repeating Transactions and Geolocation data, use:   &#x60;?includes&#x3D;repeating_transactions,geolocations&#x60;.  - Repeating Transactions: Identifies transactions with predictable recurrence patterns (e.g., Bill, Income, Subscription). - Merchants: Enriches transactions with merchant name. - Classifications: Provides more insight into the type of money movement that is occurring on the transaction, whether it be retail or investments. - Geolocation: Provides geographic metadata.  | [optional] 

### Return type

[**TransactionsResponseBodyIncludes**](TransactionsResponseBodyIncludes.md)

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

# **repeating_transactions**
> RepeatingTransactionsResponseBody repeating_transactions(user_guid)

List Repeating Transactions

Retrieve a list of all recurring transactions for a user. <br /><br />For more see the [Repeating Transactions guide](/api-reference/platform-api/v20111101/reference/transactions-overview#repeating-transactions).

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.repeating_transactions_response_body import RepeatingTransactionsResponseBody
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
    api_instance = mx_platform_python.TransactionsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.

    try:
        # List Repeating Transactions
        api_response = api_instance.repeating_transactions(user_guid)
        print("The response of TransactionsApi->repeating_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->repeating_transactions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 

### Return type

[**RepeatingTransactionsResponseBody**](RepeatingTransactionsResponseBody.md)

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

# **specific_repeating_transaction**
> RepeatingTransactionsResponseBody specific_repeating_transaction(user_guid, repeating_transaction_guid)

Get a Repeating Transaction

Get a Specific Repeating Transaction. <br /><br />List For more see the  [Repeating Transactions guide](/api-reference/platform-api/v20111101/reference/transactions-overview#repeating-transactions)

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.repeating_transactions_response_body import RepeatingTransactionsResponseBody
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
    api_instance = mx_platform_python.TransactionsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    repeating_transaction_guid = 'TRN-810828b0-5210-4878-9bd3-f4ce514f90c4' # str | The unique id for a recurring transaction.

    try:
        # Get a Repeating Transaction
        api_response = api_instance.specific_repeating_transaction(user_guid, repeating_transaction_guid)
        print("The response of TransactionsApi->specific_repeating_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->specific_repeating_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **repeating_transaction_guid** | **str**| The unique id for a recurring transaction. | 

### Return type

[**RepeatingTransactionsResponseBody**](RepeatingTransactionsResponseBody.md)

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

# **update_transaction**
> TransactionResponseBody update_transaction(user_guid, transaction_guid, transaction_update_request_body)

Update transaction

Use this endpoint to update a specific transaction according to its unique GUID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.transaction_response_body import TransactionResponseBody
from mx_platform_python.models.transaction_update_request_body import TransactionUpdateRequestBody
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
    api_instance = mx_platform_python.TransactionsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    transaction_guid = 'TRN-810828b0-5210-4878-9bd3-f4ce514f90c4' # str | The unique id for a `transaction`.
    transaction_update_request_body = mx_platform_python.TransactionUpdateRequestBody() # TransactionUpdateRequestBody | Transaction object with the fields to be updated.

    try:
        # Update transaction
        api_response = api_instance.update_transaction(user_guid, transaction_guid, transaction_update_request_body)
        print("The response of TransactionsApi->update_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->update_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **transaction_guid** | **str**| The unique id for a &#x60;transaction&#x60;. | 
 **transaction_update_request_body** | [**TransactionUpdateRequestBody**](TransactionUpdateRequestBody.md)| Transaction object with the fields to be updated. | 

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

# **update_transaction_by_account**
> TransactionResponseBody update_transaction_by_account(user_guid, member_guid, account_guid, transaction_guid, transaction_update_request_body)

Update Transaction by Account

Use this endpoint to update a specific transaction according to its unique GUID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.transaction_response_body import TransactionResponseBody
from mx_platform_python.models.transaction_update_request_body import TransactionUpdateRequestBody
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
    api_instance = mx_platform_python.TransactionsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    transaction_guid = 'TRN-810828b0-5210-4878-9bd3-f4ce514f90c4' # str | The unique id for a `transaction`.
    transaction_update_request_body = mx_platform_python.TransactionUpdateRequestBody() # TransactionUpdateRequestBody | Transaction object to be updated

    try:
        # Update Transaction by Account
        api_response = api_instance.update_transaction_by_account(user_guid, member_guid, account_guid, transaction_guid, transaction_update_request_body)
        print("The response of TransactionsApi->update_transaction_by_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->update_transaction_by_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **transaction_guid** | **str**| The unique id for a &#x60;transaction&#x60;. | 
 **transaction_update_request_body** | [**TransactionUpdateRequestBody**](TransactionUpdateRequestBody.md)| Transaction object to be updated | 

### Return type

[**TransactionResponseBody**](TransactionResponseBody.md)

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

