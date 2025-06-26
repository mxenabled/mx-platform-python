# mx_platform_python.MxPlatformApi

All URIs are relative to *https://api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate_member**](MxPlatformApi.md#aggregate_member) | **POST** /users/{user_guid}/members/{member_guid}/aggregate | Aggregate member
[**check_balances**](MxPlatformApi.md#check_balances) | **POST** /users/{user_guid}/members/{member_guid}/check_balance | Check balances
[**create_category**](MxPlatformApi.md#create_category) | **POST** /users/{user_guid}/categories | Create category
[**create_managed_account**](MxPlatformApi.md#create_managed_account) | **POST** /users/{user_guid}/managed_members/{member_guid}/accounts | Create managed account
[**create_managed_member**](MxPlatformApi.md#create_managed_member) | **POST** /users/{user_guid}/managed_members | Create managed member
[**create_managed_transaction**](MxPlatformApi.md#create_managed_transaction) | **POST** /users/{user_guid}/managed_members/{member_guid}/accounts/{account_guid}/transactions | Create managed transaction
[**create_manual_account**](MxPlatformApi.md#create_manual_account) | **POST** /users/{user_guid}/accounts | Create manual account
[**create_member**](MxPlatformApi.md#create_member) | **POST** /users/{user_guid}/members | Create member
[**create_tag**](MxPlatformApi.md#create_tag) | **POST** /users/{user_guid}/tags | Create tag
[**create_tagging**](MxPlatformApi.md#create_tagging) | **POST** /users/{user_guid}/taggings | Create tagging
[**create_transaction_rule**](MxPlatformApi.md#create_transaction_rule) | **POST** /users/{user_guid}/transaction_rules | Create transaction rule
[**create_user**](MxPlatformApi.md#create_user) | **POST** /users | Create user
[**credit_card**](MxPlatformApi.md#credit_card) | **GET** /credit_card_products/{credit_card_product_guid} | Read a Credit Card Product
[**delete_category**](MxPlatformApi.md#delete_category) | **DELETE** /users/{user_guid}/categories/{category_guid} | Delete category
[**delete_managed_account**](MxPlatformApi.md#delete_managed_account) | **DELETE** /users/{user_guid}/managed_members/{member_guid}/accounts/{account_guid} | Delete managed account
[**delete_managed_member**](MxPlatformApi.md#delete_managed_member) | **DELETE** /users/{user_guid}/managed_members/{member_guid} | Delete managed member
[**delete_managed_transaction**](MxPlatformApi.md#delete_managed_transaction) | **DELETE** /users/{user_guid}/managed_members/{member_guid}/accounts/{account_guid}/transactions/{transaction_guid} | Delete managed transaction
[**delete_manual_account**](MxPlatformApi.md#delete_manual_account) | **DELETE** /users/{user_guid}/accounts/{account_guid} | Delete manual account
[**delete_member**](MxPlatformApi.md#delete_member) | **DELETE** /users/{user_guid}/members/{member_guid} | Delete member
[**delete_tag**](MxPlatformApi.md#delete_tag) | **DELETE** /users/{user_guid}/tags/{tag_guid} | Delete tag
[**delete_tagging**](MxPlatformApi.md#delete_tagging) | **DELETE** /users/{user_guid}/taggings/{tagging_guid} | Delete tagging
[**delete_transaction_rule**](MxPlatformApi.md#delete_transaction_rule) | **DELETE** /users/{user_guid}/transaction_rules/{transaction_rule_guid} | Delete transaction rule
[**delete_user**](MxPlatformApi.md#delete_user) | **DELETE** /users/{user_guid} | Delete user
[**deprecated_request_payment_processor_authorization_code**](MxPlatformApi.md#deprecated_request_payment_processor_authorization_code) | **POST** /payment_processor_authorization_code | (Deprecated) Request an authorization code.
[**download_statement_pdf**](MxPlatformApi.md#download_statement_pdf) | **GET** /users/{user_guid}/members/{member_guid}/statements/{statement_guid}.pdf | Download statement pdf
[**download_tax_document**](MxPlatformApi.md#download_tax_document) | **GET** /users/{user_guid}/members/{member_guid}/tax_documents/{tax_document_guid}.pdf | Download a Tax Document PDF
[**enhance_transactions**](MxPlatformApi.md#enhance_transactions) | **POST** /transactions/enhance | Enhance transactions
[**extend_history**](MxPlatformApi.md#extend_history) | **POST** /users/{user_guid}/members/{member_guid}/extend_history | Extend history
[**fetch_rewards**](MxPlatformApi.md#fetch_rewards) | **POST** /users/{user_guid}/members/{member_guid}/fetch_rewards | Fetch Rewards
[**fetch_statements**](MxPlatformApi.md#fetch_statements) | **POST** /users/{user_guid}/members/{member_guid}/fetch_statements | Fetch statements
[**fetch_tax_documents**](MxPlatformApi.md#fetch_tax_documents) | **POST** /users/{user_guid}/members/{member_guid}/fetch_tax_documents | Fetch Tax Documents
[**identify_member**](MxPlatformApi.md#identify_member) | **POST** /users/{user_guid}/members/{member_guid}/identify | Identify member
[**list_account_numbers_by_account**](MxPlatformApi.md#list_account_numbers_by_account) | **GET** /users/{user_guid}/accounts/{account_guid}/account_numbers | List account numbers by account
[**list_account_numbers_by_member**](MxPlatformApi.md#list_account_numbers_by_member) | **GET** /users/{user_guid}/members/{member_guid}/account_numbers | List account numbers by member
[**list_account_owners_by_member**](MxPlatformApi.md#list_account_owners_by_member) | **GET** /users/{user_guid}/members/{member_guid}/account_owners | List account owners by member
[**list_categories**](MxPlatformApi.md#list_categories) | **GET** /users/{user_guid}/categories | List categories
[**list_default_categories**](MxPlatformApi.md#list_default_categories) | **GET** /categories/default | List default categories
[**list_default_categories_by_user**](MxPlatformApi.md#list_default_categories_by_user) | **GET** /users/{user_guid}/categories/default | List default categories by user
[**list_favorite_institutions**](MxPlatformApi.md#list_favorite_institutions) | **GET** /institutions/favorites | List favorite institutions
[**list_holdings**](MxPlatformApi.md#list_holdings) | **GET** /users/{user_guid}/holdings | List holdings
[**list_holdings_by_account**](MxPlatformApi.md#list_holdings_by_account) | **GET** /users/{user_guid}/accounts/{account_guid}/holdings | List holdings by account
[**list_holdings_by_member**](MxPlatformApi.md#list_holdings_by_member) | **GET** /users/{user_guid}/members/{member_guid}/holdings | List holdings by member
[**list_institution_credentials**](MxPlatformApi.md#list_institution_credentials) | **GET** /institutions/{institution_code}/credentials | List institution credentials
[**list_institutions**](MxPlatformApi.md#list_institutions) | **GET** /institutions | List institutions
[**list_managed_accounts**](MxPlatformApi.md#list_managed_accounts) | **GET** /users/{user_guid}/managed_members/{member_guid}/accounts | List managed accounts
[**list_managed_institutions**](MxPlatformApi.md#list_managed_institutions) | **GET** /managed_institutions | List managed institutions
[**list_managed_members**](MxPlatformApi.md#list_managed_members) | **GET** /users/{user_guid}/managed_members | List managed members
[**list_managed_transactions**](MxPlatformApi.md#list_managed_transactions) | **GET** /users/{user_guid}/managed_members/{member_guid}/accounts/{account_guid}/transactions | List managed transactions
[**list_member_accounts**](MxPlatformApi.md#list_member_accounts) | **GET** /users/{user_guid}/members/{member_guid}/accounts | List accounts by member
[**list_member_challenges**](MxPlatformApi.md#list_member_challenges) | **GET** /users/{user_guid}/members/{member_guid}/challenges | List member challenges
[**list_member_credentials**](MxPlatformApi.md#list_member_credentials) | **GET** /users/{user_guid}/members/{member_guid}/credentials | List member credentials
[**list_members**](MxPlatformApi.md#list_members) | **GET** /users/{user_guid}/members | List members
[**list_merchants**](MxPlatformApi.md#list_merchants) | **GET** /merchants | List merchants
[**list_rewards**](MxPlatformApi.md#list_rewards) | **GET** /users/{user_guid}/members/{member_guid}/rewards | List Rewards
[**list_statements_by_member**](MxPlatformApi.md#list_statements_by_member) | **GET** /users/{user_guid}/members/{member_guid}/statements | List statements by member
[**list_taggings**](MxPlatformApi.md#list_taggings) | **GET** /users/{user_guid}/taggings | List taggings
[**list_tags**](MxPlatformApi.md#list_tags) | **GET** /users/{user_guid}/tags | List tags
[**list_tax_documents**](MxPlatformApi.md#list_tax_documents) | **GET** /users/{user_guid}/members/{member_guid}/tax_documents | List Tax Documents
[**list_transaction_rules**](MxPlatformApi.md#list_transaction_rules) | **GET** /users/{user_guid}/transaction_rules | List transaction rules
[**list_transactions**](MxPlatformApi.md#list_transactions) | **GET** /users/{user_guid}/transactions | List transactions
[**list_transactions_by_account**](MxPlatformApi.md#list_transactions_by_account) | **GET** /users/{user_guid}/accounts/{account_guid}/transactions | List transactions by account
[**list_transactions_by_member**](MxPlatformApi.md#list_transactions_by_member) | **GET** /users/{user_guid}/members/{member_guid}/transactions | List transactions by member
[**list_transactions_by_tag**](MxPlatformApi.md#list_transactions_by_tag) | **GET** /users/{user_guid}/tags/{tag_guid}/transactions | List transactions by tag
[**list_user_accounts**](MxPlatformApi.md#list_user_accounts) | **GET** /users/{user_guid}/accounts | List accounts
[**list_users**](MxPlatformApi.md#list_users) | **GET** /users | List users
[**read_account**](MxPlatformApi.md#read_account) | **GET** /users/{user_guid}/accounts/{account_guid} | Read account
[**read_account_by_member**](MxPlatformApi.md#read_account_by_member) | **GET** /users/{user_guid}/members/{member_guid}/accounts/{account_guid} | Read account by member
[**read_category**](MxPlatformApi.md#read_category) | **GET** /users/{user_guid}/categories/{category_guid} | Read a custom category
[**read_default_category**](MxPlatformApi.md#read_default_category) | **GET** /categories/{category_guid} | Read a default category
[**read_holding**](MxPlatformApi.md#read_holding) | **GET** /users/{user_guid}/holdings/{holding_guid} | Read holding
[**read_institution**](MxPlatformApi.md#read_institution) | **GET** /institutions/{institution_code} | Read institution
[**read_managed_account**](MxPlatformApi.md#read_managed_account) | **GET** /users/{user_guid}/managed_members/{member_guid}/accounts/{account_guid} | Read managed account
[**read_managed_member**](MxPlatformApi.md#read_managed_member) | **GET** /users/{user_guid}/managed_members/{member_guid} | Read managed member
[**read_managed_transaction**](MxPlatformApi.md#read_managed_transaction) | **GET** /users/{user_guid}/managed_members/{member_guid}/accounts/{account_guid}/transactions/{transaction_guid} | Read managed transaction
[**read_member**](MxPlatformApi.md#read_member) | **GET** /users/{user_guid}/members/{member_guid} | Read member
[**read_member_status**](MxPlatformApi.md#read_member_status) | **GET** /users/{user_guid}/members/{member_guid}/status | Read member status
[**read_merchant**](MxPlatformApi.md#read_merchant) | **GET** /merchants/{merchant_guid} | Read merchant
[**read_merchant_location**](MxPlatformApi.md#read_merchant_location) | **GET** /merchant_locations/{merchant_location_guid} | Read merchant location
[**read_rewards**](MxPlatformApi.md#read_rewards) | **GET** /users/{user_guid}/members/{member_guid}/rewards/{reward_guid} | Read Reward
[**read_statement_by_member**](MxPlatformApi.md#read_statement_by_member) | **GET** /users/{user_guid}/members/{member_guid}/statements/{statement_guid} | Read statement by member
[**read_tag**](MxPlatformApi.md#read_tag) | **GET** /users/{user_guid}/tags/{tag_guid} | Read tag
[**read_tagging**](MxPlatformApi.md#read_tagging) | **GET** /users/{user_guid}/taggings/{tagging_guid} | Read tagging
[**read_tax_document**](MxPlatformApi.md#read_tax_document) | **GET** /users/{user_guid}/members/{member_guid}/tax_documents/{tax_document_guid} | Read a Tax Document
[**read_transaction**](MxPlatformApi.md#read_transaction) | **GET** /users/{user_guid}/transactions/{transaction_guid} | Read transaction
[**read_transaction_rule**](MxPlatformApi.md#read_transaction_rule) | **GET** /users/{user_guid}/transaction_rules/{transaction_rule_guid} | Read transaction rule
[**read_user**](MxPlatformApi.md#read_user) | **GET** /users/{user_guid} | Read user
[**request_authorization_code**](MxPlatformApi.md#request_authorization_code) | **POST** /authorization_code | Request an authorization code.
[**request_connect_widget_url**](MxPlatformApi.md#request_connect_widget_url) | **POST** /users/{user_guid}/connect_widget_url | Request connect widget url
[**request_o_auth_window_uri**](MxPlatformApi.md#request_o_auth_window_uri) | **GET** /users/{user_guid}/members/{member_guid}/oauth_window_uri | Request oauth window uri
[**request_widget_url**](MxPlatformApi.md#request_widget_url) | **POST** /users/{user_guid}/widget_urls | Request widget url
[**resume_aggregation**](MxPlatformApi.md#resume_aggregation) | **PUT** /users/{user_guid}/members/{member_guid}/resume | Resume aggregation
[**update_account_by_member**](MxPlatformApi.md#update_account_by_member) | **PUT** /users/{user_guid}/members/{member_guid}/accounts/{account_guid} | Update account by member
[**update_category**](MxPlatformApi.md#update_category) | **PUT** /users/{user_guid}/categories/{category_guid} | Update category
[**update_managed_account**](MxPlatformApi.md#update_managed_account) | **PUT** /users/{user_guid}/managed_members/{member_guid}/accounts/{account_guid} | Update managed account
[**update_managed_member**](MxPlatformApi.md#update_managed_member) | **PUT** /users/{user_guid}/managed_members/{member_guid} | Update managed member
[**update_managed_transaction**](MxPlatformApi.md#update_managed_transaction) | **PUT** /users/{user_guid}/managed_members/{member_guid}/accounts/{account_guid}/transactions/{transaction_guid} | Update managed transaction
[**update_member**](MxPlatformApi.md#update_member) | **PUT** /users/{user_guid}/members/{member_guid} | Update member
[**update_tag**](MxPlatformApi.md#update_tag) | **PUT** /users/{user_guid}/tags/{tag_guid} | Update tag
[**update_tagging**](MxPlatformApi.md#update_tagging) | **PUT** /users/{user_guid}/taggings/{tagging_guid} | Update tagging
[**update_transaction**](MxPlatformApi.md#update_transaction) | **PUT** /users/{user_guid}/transactions/{transaction_guid} | Update transaction
[**update_transaction_rule**](MxPlatformApi.md#update_transaction_rule) | **PUT** /users/{user_guid}/transaction_rules/{transaction_rule_guid} | Update transaction_rule
[**update_user**](MxPlatformApi.md#update_user) | **PUT** /users/{user_guid} | Update user
[**users_user_guid_monthly_cash_flow_profile_get**](MxPlatformApi.md#users_user_guid_monthly_cash_flow_profile_get) | **GET** /users/{user_guid}/monthly_cash_flow_profile | Read monthly cash flow profile
[**users_user_guid_monthly_cash_flow_profile_put**](MxPlatformApi.md#users_user_guid_monthly_cash_flow_profile_put) | **PUT** /users/{user_guid}/monthly_cash_flow_profile | Update monthly cash flow profile
[**users_user_guid_transactions_transaction_guid_split_delete**](MxPlatformApi.md#users_user_guid_transactions_transaction_guid_split_delete) | **DELETE** /users/{user_guid}/transactions/{transaction_guid}/split | Delete split transactions
[**users_user_guid_transactions_transaction_guid_split_post**](MxPlatformApi.md#users_user_guid_transactions_transaction_guid_split_post) | **POST** /users/{user_guid}/transactions/{transaction_guid}/split | Create split transactions
[**verify_member**](MxPlatformApi.md#verify_member) | **POST** /users/{user_guid}/members/{member_guid}/verify | Verify member


# **aggregate_member**
> MemberResponseBody aggregate_member(member_guid, user_guid, include_holdings=include_holdings, include_transactions=include_transactions)

Aggregate member

Calling this endpoint initiates an aggregation event for the member. This brings in the latest account and transaction data from the connected institution. If this data has recently been updated, MX may not initiate an aggregation event.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.member_response_body import MemberResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    include_holdings = false # bool | When set to `false`, the aggregation will not gather holdings data. Defaults to `true`. (optional)
    include_transactions = false # bool | When set to `false`, the aggregation will not gather transactions data. Defaults to `true`. (optional)

    try:
        # Aggregate member
        api_response = api_instance.aggregate_member(member_guid, user_guid, include_holdings=include_holdings, include_transactions=include_transactions)
        print("The response of MxPlatformApi->aggregate_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->aggregate_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **include_holdings** | **bool**| When set to &#x60;false&#x60;, the aggregation will not gather holdings data. Defaults to &#x60;true&#x60;. | [optional] 
 **include_transactions** | **bool**| When set to &#x60;false&#x60;, the aggregation will not gather transactions data. Defaults to &#x60;true&#x60;. | [optional] 

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

# **check_balances**
> MemberResponseBody check_balances(member_guid, user_guid)

Check balances

This endpoint operates much like the aggregate member endpoint except that it gathers only account balance information; it does not gather any transaction data.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.member_response_body import MemberResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Check balances
        api_response = api_instance.check_balances(member_guid, user_guid)
        print("The response of MxPlatformApi->check_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->check_balances: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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

# **create_category**
> CategoryResponseBody create_category(user_guid, category_create_request_body)

Create category

Use this endpoint to create a new custom category for a specific `user`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.category_create_request_body import CategoryCreateRequestBody
from mx_platform_python.models.category_response_body import CategoryResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    category_create_request_body = mx_platform_python.CategoryCreateRequestBody() # CategoryCreateRequestBody | Custom category object to be created

    try:
        # Create category
        api_response = api_instance.create_category(user_guid, category_create_request_body)
        print("The response of MxPlatformApi->create_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->create_category: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **category_create_request_body** | [**CategoryCreateRequestBody**](CategoryCreateRequestBody.md)| Custom category object to be created | 

### Return type

[**CategoryResponseBody**](CategoryResponseBody.md)

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    managed_account_create_request_body = mx_platform_python.ManagedAccountCreateRequestBody() # ManagedAccountCreateRequestBody | Managed account to be created.

    try:
        # Create managed account
        api_response = api_instance.create_managed_account(member_guid, user_guid, managed_account_create_request_body)
        print("The response of MxPlatformApi->create_managed_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->create_managed_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
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
**202** | OK |  -  |

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    managed_member_create_request_body = mx_platform_python.ManagedMemberCreateRequestBody() # ManagedMemberCreateRequestBody | Managed member to be created.

    try:
        # Create managed member
        api_response = api_instance.create_managed_member(user_guid, managed_member_create_request_body)
        print("The response of MxPlatformApi->create_managed_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->create_managed_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    managed_transaction_create_request_body = mx_platform_python.ManagedTransactionCreateRequestBody() # ManagedTransactionCreateRequestBody | Managed transaction to be created.

    try:
        # Create managed transaction
        api_response = api_instance.create_managed_transaction(account_guid, member_guid, user_guid, managed_transaction_create_request_body)
        print("The response of MxPlatformApi->create_managed_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->create_managed_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
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
**202** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_manual_account**
> AccountResponseBody create_manual_account(user_guid, account_create_request_body)

Create manual account

This endpoint can only be used to create manual accounts. Creating a manual account will automatically create it under the Manual Institution member. Since a manual account has no credentials tied to the member, the account will never aggregate or include data from a data feed.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    account_create_request_body = mx_platform_python.AccountCreateRequestBody() # AccountCreateRequestBody | Manual account object to be created.

    try:
        # Create manual account
        api_response = api_instance.create_manual_account(user_guid, account_create_request_body)
        print("The response of MxPlatformApi->create_manual_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->create_manual_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
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

# **create_member**
> MemberResponseBody create_member(user_guid, member_create_request_body)

Create member

This endpoint allows you to create a new member. Members are created with the required parameters credentials and institution_code, and the optional parameters id and metadata. When creating a member, youll need to include the correct type of credential required by the financial institution and provided by the user. You can find out which credential type is required with the `/institutions/{institution_code}/credentials` endpoint. If successful, the MX Platform API will respond with the newly-created member object. Once you successfully create a member, MX will immediately validate the provided credentials and attempt to aggregate data for accounts and transactions.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.member_create_request_body import MemberCreateRequestBody
from mx_platform_python.models.member_response_body import MemberResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    member_create_request_body = mx_platform_python.MemberCreateRequestBody() # MemberCreateRequestBody | Member object to be created with optional parameters (id and metadata) and required parameters (credentials and institution_code)

    try:
        # Create member
        api_response = api_instance.create_member(user_guid, member_create_request_body)
        print("The response of MxPlatformApi->create_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->create_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **member_create_request_body** | [**MemberCreateRequestBody**](MemberCreateRequestBody.md)| Member object to be created with optional parameters (id and metadata) and required parameters (credentials and institution_code) | 

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tag**
> TagResponseBody create_tag(user_guid, tag_create_request_body)

Create tag

Use this endpoint to create a new custom tag.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.tag_create_request_body import TagCreateRequestBody
from mx_platform_python.models.tag_response_body import TagResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    tag_create_request_body = mx_platform_python.TagCreateRequestBody() # TagCreateRequestBody | Tag object to be created with required parameters (tag_guid)

    try:
        # Create tag
        api_response = api_instance.create_tag(user_guid, tag_create_request_body)
        print("The response of MxPlatformApi->create_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->create_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **tag_create_request_body** | [**TagCreateRequestBody**](TagCreateRequestBody.md)| Tag object to be created with required parameters (tag_guid) | 

### Return type

[**TagResponseBody**](TagResponseBody.md)

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

# **create_tagging**
> TaggingResponseBody create_tagging(user_guid, tagging_create_request_body)

Create tagging

Use this endpoint to create a new association between a tag and a particular transaction, according to their unique GUIDs.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.tagging_create_request_body import TaggingCreateRequestBody
from mx_platform_python.models.tagging_response_body import TaggingResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    tagging_create_request_body = mx_platform_python.TaggingCreateRequestBody() # TaggingCreateRequestBody | Tagging object to be created with required parameters (tag_guid and transaction_guid)

    try:
        # Create tagging
        api_response = api_instance.create_tagging(user_guid, tagging_create_request_body)
        print("The response of MxPlatformApi->create_tagging:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->create_tagging: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **tagging_create_request_body** | [**TaggingCreateRequestBody**](TaggingCreateRequestBody.md)| Tagging object to be created with required parameters (tag_guid and transaction_guid) | 

### Return type

[**TaggingResponseBody**](TaggingResponseBody.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.mx.api.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_transaction_rule**
> TransactionRuleResponseBody create_transaction_rule(user_guid, transaction_rule_create_request_body)

Create transaction rule

Use this endpoint to create a new transaction rule. The newly-created `transaction_rule` object will be returned if successful.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.transaction_rule_create_request_body import TransactionRuleCreateRequestBody
from mx_platform_python.models.transaction_rule_response_body import TransactionRuleResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    transaction_rule_create_request_body = mx_platform_python.TransactionRuleCreateRequestBody() # TransactionRuleCreateRequestBody | TransactionRule object to be created with optional parameters (description) and required parameters (category_guid and match_description)

    try:
        # Create transaction rule
        api_response = api_instance.create_transaction_rule(user_guid, transaction_rule_create_request_body)
        print("The response of MxPlatformApi->create_transaction_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->create_transaction_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **transaction_rule_create_request_body** | [**TransactionRuleCreateRequestBody**](TransactionRuleCreateRequestBody.md)| TransactionRule object to be created with optional parameters (description) and required parameters (category_guid and match_description) | 

### Return type

[**TransactionRuleResponseBody**](TransactionRuleResponseBody.md)

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

# **create_user**
> UserResponseBody create_user(user_create_request_body)

Create user

Use this endpoint to create a new user. The API will respond with the newly-created user object if successful. Disabling a user means that accounts and transactions associated with it will not be updated in the background by MX. It will also restrict access to that user’s data until they are no longer disabled.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_create_request_body = mx_platform_python.UserCreateRequestBody() # UserCreateRequestBody | User object to be created. (None of these parameters are required, but the user object cannot be empty)

    try:
        # Create user
        api_response = api_instance.create_user(user_create_request_body)
        print("The response of MxPlatformApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->create_user: %s\n" % e)
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

# **credit_card**
> CreditCardProductResponse credit_card(credit_card_product_guid)

Read a Credit Card Product

This endpoint returns the specified `credit_card_product` according to the unique GUID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.credit_card_product_response import CreditCardProductResponse
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    credit_card_product_guid = 'credit_card_product_guid' # str | The required `credit_card_product_guid` can be found on the `account` object.

    try:
        # Read a Credit Card Product
        api_response = api_instance.credit_card(credit_card_product_guid)
        print("The response of MxPlatformApi->credit_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->credit_card: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credit_card_product_guid** | **str**| The required &#x60;credit_card_product_guid&#x60; can be found on the &#x60;account&#x60; object. | 

### Return type

[**CreditCardProductResponse**](CreditCardProductResponse.md)

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

# **delete_category**
> delete_category(category_guid, user_guid)

Delete category

Use this endpoint to delete a specific custom category according to its unique GUID. The API will respond with an empty object and a status of `204 No Content`.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    category_guid = 'CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874' # str | The unique id for a `category`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Delete category
        api_instance.delete_category(category_guid, user_guid)
    except Exception as e:
        print("Exception when calling MxPlatformApi->delete_category: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_guid** | **str**| The unique id for a &#x60;category&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Delete managed account
        api_instance.delete_managed_account(account_guid, member_guid, user_guid)
    except Exception as e:
        print("Exception when calling MxPlatformApi->delete_managed_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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
> delete_managed_member(member_guid, user_guid)

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Delete managed member
        api_instance.delete_managed_member(member_guid, user_guid)
    except Exception as e:
        print("Exception when calling MxPlatformApi->delete_managed_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    transaction_guid = 'TRN-810828b0-5210-4878-9bd3-f4ce514f90c4' # str | The unique id for a `transaction`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Delete managed transaction
        api_instance.delete_managed_transaction(account_guid, member_guid, transaction_guid, user_guid)
    except Exception as e:
        print("Exception when calling MxPlatformApi->delete_managed_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **transaction_guid** | **str**| The unique id for a &#x60;transaction&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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

# **delete_manual_account**
> delete_manual_account(account_guid, user_guid)

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Delete manual account
        api_instance.delete_manual_account(account_guid, user_guid)
    except Exception as e:
        print("Exception when calling MxPlatformApi->delete_manual_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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

# **delete_member**
> delete_member(member_guid, user_guid)

Delete member

Accessing this endpoint will permanently delete a member.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Delete member
        api_instance.delete_member(member_guid, user_guid)
    except Exception as e:
        print("Exception when calling MxPlatformApi->delete_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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

# **delete_tag**
> delete_tag(tag_guid, user_guid)

Delete tag

Use this endpoint to permanently delete a specific tag based on its unique GUID. If successful, the API will respond with status of `204 No Content`.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    tag_guid = 'TAG-aef36e72-6294-4c38-844d-e573e80aed52' # str | The unique id for a `tag`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Delete tag
        api_instance.delete_tag(tag_guid, user_guid)
    except Exception as e:
        print("Exception when calling MxPlatformApi->delete_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_guid** | **str**| The unique id for a &#x60;tag&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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

# **delete_tagging**
> delete_tagging(tagging_guid, user_guid)

Delete tagging

Use this endpoint to delete a tagging according to its unique GUID. If successful, the API will respond with an empty body and a status of 204 NO Content.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    tagging_guid = 'TGN-007f5486-17e1-45fc-8b87-8f03984430fe' # str | The unique id for a `tagging`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Delete tagging
        api_instance.delete_tagging(tagging_guid, user_guid)
    except Exception as e:
        print("Exception when calling MxPlatformApi->delete_tagging: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tagging_guid** | **str**| The unique id for a &#x60;tagging&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    transaction_rule_guid = 'TXR-a080e0f9-a2d4-4d6f-9e03-672cc357a4d3' # str | The unique id for a `transaction_rule`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Delete transaction rule
        api_instance.delete_transaction_rule(transaction_rule_guid, user_guid)
    except Exception as e:
        print("Exception when calling MxPlatformApi->delete_transaction_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_rule_guid** | **str**| The unique id for a &#x60;transaction_rule&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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

# **delete_user**
> delete_user(user_guid)

Delete user

Use this endpoint to delete the specified `user`. The response will have a status of `204 No Content` without an object.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Delete user
        api_instance.delete_user(user_guid)
    except Exception as e:
        print("Exception when calling MxPlatformApi->delete_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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

# **deprecated_request_payment_processor_authorization_code**
> PaymentProcessorAuthorizationCodeResponseBody deprecated_request_payment_processor_authorization_code(payment_processor_authorization_code_request_body)

(Deprecated) Request an authorization code.

(This endpoint is deprecated. Clients should use `/authorization_code`.) Clients use this endpoint to request an authorization_code according to a user, member, and account specified in the request body. Clients then pass this code to processors. Processor access is scoped only to the user/member/account specified in this request. Before requesting an authorization_code, clients must have verified the specified member.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.payment_processor_authorization_code_request_body import PaymentProcessorAuthorizationCodeRequestBody
from mx_platform_python.models.payment_processor_authorization_code_response_body import PaymentProcessorAuthorizationCodeResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    payment_processor_authorization_code_request_body = mx_platform_python.PaymentProcessorAuthorizationCodeRequestBody() # PaymentProcessorAuthorizationCodeRequestBody | The scope for the authorization code.

    try:
        # (Deprecated) Request an authorization code.
        api_response = api_instance.deprecated_request_payment_processor_authorization_code(payment_processor_authorization_code_request_body)
        print("The response of MxPlatformApi->deprecated_request_payment_processor_authorization_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->deprecated_request_payment_processor_authorization_code: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_processor_authorization_code_request_body** | [**PaymentProcessorAuthorizationCodeRequestBody**](PaymentProcessorAuthorizationCodeRequestBody.md)| The scope for the authorization code. | 

### Return type

[**PaymentProcessorAuthorizationCodeResponseBody**](PaymentProcessorAuthorizationCodeResponseBody.md)

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

# **download_statement_pdf**
> bytearray download_statement_pdf(member_guid, statement_guid, user_guid)

Download statement pdf

Use this endpoint to download a specified statement PDF.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    statement_guid = 'STA-737a344b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for a `statement`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Download statement pdf
        api_response = api_instance.download_statement_pdf(member_guid, statement_guid, user_guid)
        print("The response of MxPlatformApi->download_statement_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->download_statement_pdf: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **statement_guid** | **str**| The unique id for a &#x60;statement&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

### Return type

**bytearray**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.mx.api.v1+pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_tax_document**
> bytearray download_tax_document(tax_document_guid, member_guid, user_guid)

Download a Tax Document PDF

Use this endpoint to download a PDF version of the specified tax document. The endpoint URL is the base URL appended with the uri of the tax_document.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    tax_document_guid = 'TAX-987dfds1b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `tax_document`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Download a Tax Document PDF
        api_response = api_instance.download_tax_document(tax_document_guid, member_guid, user_guid)
        print("The response of MxPlatformApi->download_tax_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->download_tax_document: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_document_guid** | **str**| The unique id for a &#x60;tax_document&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

### Return type

**bytearray**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.mx.api.v1+pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enhance_transactions**
> EnhanceTransactionsResponseBody enhance_transactions(enhance_transactions_request_body)

Enhance transactions

Use this endpoint to categorize, cleanse, and classify transactions. These transactions are not persisted or stored on the MX platform.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    enhance_transactions_request_body = mx_platform_python.EnhanceTransactionsRequestBody() # EnhanceTransactionsRequestBody | Transaction object to be enhanced

    try:
        # Enhance transactions
        api_response = api_instance.enhance_transactions(enhance_transactions_request_body)
        print("The response of MxPlatformApi->enhance_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->enhance_transactions: %s\n" % e)
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique identifier for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`.

    try:
        # Extend history
        api_response = api_instance.extend_history(member_guid, user_guid)
        print("The response of MxPlatformApi->extend_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->extend_history: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique identifier for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;. | 

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

# **fetch_rewards**
> MemberResponseBody fetch_rewards(user_guid, member_guid)

Fetch Rewards

Calling this endpoint initiates an aggregation-type event which will gather the member's rewards information, as well as account and transaction information. Rewards data is also gathered with daily background aggregations.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.member_response_body import MemberResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    member_guid = 'MBR-fa7537f3-48aa-a683-a02a-b18345562f54' # str | The unique identifier for the member. Defined by MX.

    try:
        # Fetch Rewards
        api_response = api_instance.fetch_rewards(user_guid, member_guid)
        print("The response of MxPlatformApi->fetch_rewards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->fetch_rewards: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **member_guid** | **str**| The unique identifier for the member. Defined by MX. | 

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

# **fetch_statements**
> MemberResponseBody fetch_statements(member_guid, user_guid)

Fetch statements

Use this endpoint to fetch the statements associated with a particular member.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.member_response_body import MemberResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Fetch statements
        api_response = api_instance.fetch_statements(member_guid, user_guid)
        print("The response of MxPlatformApi->fetch_statements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->fetch_statements: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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

# **fetch_tax_documents**
> MemberResponseBody fetch_tax_documents(member_guid, user_guid)

Fetch Tax Documents

Use this endpoint to fetch (aggregate) the tax documents associated with the specified member. This request **does not** return the latest tax documents. It just starts the document aggregation process and returns the initial state of the process. You must interact with the newly aggregated data using the other document endpoints in this reference. This request may also trigger multi-factor authentication which requires end-user input and a specific process for answering authentication challenges.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.member_response_body import MemberResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Fetch Tax Documents
        api_response = api_instance.fetch_tax_documents(member_guid, user_guid)
        print("The response of MxPlatformApi->fetch_tax_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->fetch_tax_documents: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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

# **identify_member**
> MemberResponseBody identify_member(member_guid, user_guid)

Identify member

The identify endpoint begins an identification process for an already-existing member.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.member_response_body import MemberResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Identify member
        api_response = api_instance.identify_member(member_guid, user_guid)
        print("The response of MxPlatformApi->identify_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->identify_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List account numbers by account
        api_response = api_instance.list_account_numbers_by_account(account_guid, user_guid, page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_account_numbers_by_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_account_numbers_by_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List account numbers by member
        api_response = api_instance.list_account_numbers_by_member(member_guid, user_guid, page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_account_numbers_by_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_account_numbers_by_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List account owners by member
        api_response = api_instance.list_account_owners_by_member(member_guid, user_guid, page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_account_owners_by_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_account_owners_by_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

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

# **list_categories**
> CategoriesResponseBody list_categories(user_guid, page=page, records_per_page=records_per_page)

List categories

Use this endpoint to list all categories associated with a `user`, including both default and custom categories.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List categories
        api_response = api_instance.list_categories(user_guid, page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_categories: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
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

# **list_default_categories**
> CategoriesResponseBody list_default_categories(page=page, records_per_page=records_per_page)

List default categories

Use this endpoint to retrieve a list of all the default categories and subcategories offered within the MX Platform API. In other words, each item in the returned list will have its `is_default` field set to `true`. There are currently 119 default categories and subcategories. Both the _list default categories_ and _list default categories by user_ endpoints return the same results. The different routes are provided for convenience.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List default categories
        api_response = api_instance.list_default_categories(page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_default_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_default_categories: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **list_default_categories_by_user**
> CategoriesResponseBody list_default_categories_by_user(user_guid, page=page, records_per_page=records_per_page)

List default categories by user

Use this endpoint to retrieve a list of all the default categories and subcategories, scoped by user, offered within the MX Platform API. In other words, each item in the returned list will have its `is_default` field set to `true`. There are currently 119 default categories and subcategories. Both the _list default categories_ and _list default categories by user_ endpoints return the same results. The different routes are provided for convenience.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List default categories by user
        api_response = api_instance.list_default_categories_by_user(user_guid, page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_default_categories_by_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_default_categories_by_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
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

# **list_favorite_institutions**
> InstitutionsResponseBody list_favorite_institutions(page=page, records_per_page=records_per_page)

List favorite institutions

This endpoint returns a paginated list containing institutions that have been set as the partner’s favorites, sorted by popularity. Please contact MX to set a list of favorites.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.institutions_response_body import InstitutionsResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List favorite institutions
        api_response = api_instance.list_favorite_institutions(page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_favorite_institutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_favorite_institutions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

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

# **list_holdings**
> HoldingsResponseBody list_holdings(user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)

List holdings

This endpoint returns all holdings associated with the specified `user` across all accounts and members.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.holdings_response_body import HoldingsResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    from_date = '2015-09-20' # str | Filter holdings from this date. (optional)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)
    to_date = '2019-10-20' # str | Filter holdings to this date. (optional)

    try:
        # List holdings
        api_response = api_instance.list_holdings(user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)
        print("The response of MxPlatformApi->list_holdings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_holdings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **from_date** | **str**| Filter holdings from this date. | [optional] 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 
 **to_date** | **str**| Filter holdings to this date. | [optional] 

### Return type

[**HoldingsResponseBody**](HoldingsResponseBody.md)

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
> HoldingsResponseBody list_holdings_by_account(account_guid, user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)

List holdings by account

This endpoint returns all holdings associated with the specified `account`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.holdings_response_body import HoldingsResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    account_guid = 'ACT-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for the `account`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for the `user`.
    from_date = '2015-09-20' # str | Filter holdings from this date. (optional)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)
    to_date = '2019-10-20' # str | Filter holdings to this date. (optional)

    try:
        # List holdings by account
        api_response = api_instance.list_holdings_by_account(account_guid, user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)
        print("The response of MxPlatformApi->list_holdings_by_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_holdings_by_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for the &#x60;account&#x60;. | 
 **user_guid** | **str**| The unique id for the &#x60;user&#x60;. | 
 **from_date** | **str**| Filter holdings from this date. | [optional] 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 
 **to_date** | **str**| Filter holdings to this date. | [optional] 

### Return type

[**HoldingsResponseBody**](HoldingsResponseBody.md)

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
> HoldingsResponseBody list_holdings_by_member(member_guid, user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)

List holdings by member

This endpoint returns all holdings associated with the specified `member` across all accounts.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.holdings_response_body import HoldingsResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    from_date = '2015-09-20' # str | Filter holdings from this date. (optional)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)
    to_date = '2019-10-20' # str | Filter holdings to this date. (optional)

    try:
        # List holdings by member
        api_response = api_instance.list_holdings_by_member(member_guid, user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)
        print("The response of MxPlatformApi->list_holdings_by_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_holdings_by_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **from_date** | **str**| Filter holdings from this date. | [optional] 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 
 **to_date** | **str**| Filter holdings to this date. | [optional] 

### Return type

[**HoldingsResponseBody**](HoldingsResponseBody.md)

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

# **list_institution_credentials**
> CredentialsResponseBody list_institution_credentials(institution_code, page=page, records_per_page=records_per_page)

List institution credentials

Use this endpoint to see which credentials will be needed to create a member for a specific institution.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.credentials_response_body import CredentialsResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    institution_code = 'chase' # str | The institution_code of the institution.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List institution credentials
        api_response = api_instance.list_institution_credentials(institution_code, page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_institution_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_institution_credentials: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_code** | **str**| The institution_code of the institution. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**CredentialsResponseBody**](CredentialsResponseBody.md)

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

# **list_institutions**
> InstitutionsResponseBody list_institutions(name=name, page=page, records_per_page=records_per_page, supports_account_identification=supports_account_identification, supports_account_statement=supports_account_statement, supports_account_verification=supports_account_verification, supports_transaction_history=supports_transaction_history)

List institutions

This endpoint returns a list of institutions based on the specified search term or parameter.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.institutions_response_body import InstitutionsResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    name = 'chase' # str | This will list only institutions in which the appended string appears. (optional)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)
    supports_account_identification = true # bool | Filter only institutions which support account identification. (optional)
    supports_account_statement = true # bool | Filter only institutions which support account statements. (optional)
    supports_account_verification = true # bool | Filter only institutions which support account verification. (optional)
    supports_transaction_history = true # bool | Filter only institutions which support extended transaction history. (optional)

    try:
        # List institutions
        api_response = api_instance.list_institutions(name=name, page=page, records_per_page=records_per_page, supports_account_identification=supports_account_identification, supports_account_statement=supports_account_statement, supports_account_verification=supports_account_verification, supports_transaction_history=supports_transaction_history)
        print("The response of MxPlatformApi->list_institutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_institutions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| This will list only institutions in which the appended string appears. | [optional] 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 
 **supports_account_identification** | **bool**| Filter only institutions which support account identification. | [optional] 
 **supports_account_statement** | **bool**| Filter only institutions which support account statements. | [optional] 
 **supports_account_verification** | **bool**| Filter only institutions which support account verification. | [optional] 
 **supports_transaction_history** | **bool**| Filter only institutions which support extended transaction history. | [optional] 

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

# **list_managed_accounts**
> AccountsResponseBody list_managed_accounts(member_guid, user_guid, page=page, records_per_page=records_per_page)

List managed accounts

Use this endpoint to retrieve a list of all the partner-managed accounts associated with the given partner-manage member.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List managed accounts
        api_response = api_instance.list_managed_accounts(member_guid, user_guid, page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_managed_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_managed_accounts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List managed institutions
        api_response = api_instance.list_managed_institutions(page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_managed_institutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_managed_institutions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List managed members
        api_response = api_instance.list_managed_members(user_guid, page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_managed_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_managed_members: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

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
> TransactionsResponseBody list_managed_transactions(account_guid, member_guid, user_guid, page=page, records_per_page=records_per_page)

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List managed transactions
        api_response = api_instance.list_managed_transactions(account_guid, member_guid, user_guid, page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_managed_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_managed_transactions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    member_is_managed_by_user = true # bool | List only accounts whose member is managed by the user. (optional)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List accounts by member
        api_response = api_instance.list_member_accounts(user_guid, member_guid, member_is_managed_by_user=member_is_managed_by_user, page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_member_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_member_accounts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **member_is_managed_by_user** | **bool**| List only accounts whose member is managed by the user. | [optional] 
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

# **list_member_challenges**
> ChallengesResponseBody list_member_challenges(member_guid, user_guid, page=page, records_per_page=records_per_page)

List member challenges

Use this endpoint for information on what multi-factor authentication challenges need to be answered in order to aggregate a member. If the aggregation is not challenged, i.e., the member does not have a connection status of `CHALLENGED`, then code `204 No Content` will be returned. If the aggregation has been challenged, i.e., the member does have a connection status of `CHALLENGED`, then code `200 OK` will be returned - along with the corresponding credentials.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.challenges_response_body import ChallengesResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List member challenges
        api_response = api_instance.list_member_challenges(member_guid, user_guid, page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_member_challenges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_member_challenges: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**ChallengesResponseBody**](ChallengesResponseBody.md)

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

# **list_member_credentials**
> CredentialsResponseBody list_member_credentials(member_guid, user_guid, page=page, records_per_page=records_per_page)

List member credentials

This endpoint returns an array which contains information on every non-MFA credential associated with a specific member.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.credentials_response_body import CredentialsResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List member credentials
        api_response = api_instance.list_member_credentials(member_guid, user_guid, page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_member_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_member_credentials: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**CredentialsResponseBody**](CredentialsResponseBody.md)

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

# **list_members**
> MembersResponseBody list_members(user_guid, page=page, records_per_page=records_per_page)

List members

This endpoint returns an array which contains information on every member associated with a specific user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.members_response_body import MembersResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List members
        api_response = api_instance.list_members(user_guid, page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_members: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

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

# **list_merchants**
> MerchantsResponseBody list_merchants(page=page, records_per_page=records_per_page)

List merchants

This endpoint returns a paginated list of all the merchants in the MX system.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List merchants
        api_response = api_instance.list_merchants(page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_merchants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_merchants: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **list_rewards**
> RewardsResponseBody list_rewards(user_guid, member_guid)

List Rewards

Use this endpoint to list all the `rewards` associated with a specified `member`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.rewards_response_body import RewardsResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    member_guid = 'MBR-fa7537f3-48aa-a683-a02a-b18345562f54' # str | The unique identifier for the member. Defined by MX.

    try:
        # List Rewards
        api_response = api_instance.list_rewards(user_guid, member_guid)
        print("The response of MxPlatformApi->list_rewards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_rewards: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **member_guid** | **str**| The unique identifier for the member. Defined by MX. | 

### Return type

[**RewardsResponseBody**](RewardsResponseBody.md)

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

# **list_statements_by_member**
> StatementsResponseBody list_statements_by_member(member_guid, user_guid, page=page, records_per_page=records_per_page)

List statements by member

Use this endpoint to get an array of available statements.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.statements_response_body import StatementsResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List statements by member
        api_response = api_instance.list_statements_by_member(member_guid, user_guid, page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_statements_by_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_statements_by_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**StatementsResponseBody**](StatementsResponseBody.md)

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

# **list_taggings**
> TaggingsResponseBody list_taggings(user_guid, page=page, records_per_page=records_per_page)

List taggings

Use this endpoint to retrieve a list of all the taggings associated with a specific user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.taggings_response_body import TaggingsResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List taggings
        api_response = api_instance.list_taggings(user_guid, page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_taggings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_taggings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**TaggingsResponseBody**](TaggingsResponseBody.md)

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

# **list_tags**
> TagsResponseBody list_tags(user_guid, page=page, records_per_page=records_per_page)

List tags

Use this endpoint to list all tags associated with the specified `user`. Each user includes the `Business` tag by default.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.tags_response_body import TagsResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List tags
        api_response = api_instance.list_tags(user_guid, page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_tags: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**TagsResponseBody**](TagsResponseBody.md)

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

# **list_tax_documents**
> TaxDocumentsResponseBody list_tax_documents(member_guid, user_guid, page=page, records_per_page=records_per_page)

List Tax Documents

Use this endpoint to get a paginated list of tax documents.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.tax_documents_response_body import TaxDocumentsResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List Tax Documents
        api_response = api_instance.list_tax_documents(member_guid, user_guid, page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_tax_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_tax_documents: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**TaxDocumentsResponseBody**](TaxDocumentsResponseBody.md)

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

# **list_transaction_rules**
> TransactionRulesResponseBody list_transaction_rules(user_guid, page=page, records_per_page=records_per_page)

List transaction rules

Use this endpoint to read the attributes of all existing transaction rules belonging to the user.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.transaction_rules_response_body import TransactionRulesResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List transaction rules
        api_response = api_instance.list_transaction_rules(user_guid, page=page, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_transaction_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_transaction_rules: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 

### Return type

[**TransactionRulesResponseBody**](TransactionRulesResponseBody.md)

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

# **list_transactions**
> TransactionsResponseBody list_transactions(user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)

List transactions

Requests to this endpoint return a list of transactions associated with the specified `user`, accross all members and accounts associated with that `user`.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    from_date = '2015-09-20' # str | Filter transactions from this date. (optional)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)
    to_date = '2019-10-20' # str | Filter transactions to this date. (optional)

    try:
        # List transactions
        api_response = api_instance.list_transactions(user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)
        print("The response of MxPlatformApi->list_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_transactions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **from_date** | **str**| Filter transactions from this date. | [optional] 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 
 **to_date** | **str**| Filter transactions to this date. | [optional] 

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

# **list_transactions_by_account**
> TransactionsResponseBody list_transactions_by_account(account_guid, user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)

List transactions by account

This endpoint returns a list of the last 90 days of transactions associated with the specified account.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    from_date = '2015-09-20' # str | Filter transactions from this date. (optional)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)
    to_date = '2019-10-20' # str | Filter transactions to this date. (optional)

    try:
        # List transactions by account
        api_response = api_instance.list_transactions_by_account(account_guid, user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)
        print("The response of MxPlatformApi->list_transactions_by_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_transactions_by_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **from_date** | **str**| Filter transactions from this date. | [optional] 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 
 **to_date** | **str**| Filter transactions to this date. | [optional] 

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

# **list_transactions_by_member**
> TransactionsResponseBody list_transactions_by_member(member_guid, user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)

List transactions by member

Requests to this endpoint return a list of transactions associated with the specified `member`, accross all accounts associated with that `member`.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    from_date = '2015-09-20' # str | Filter transactions from this date. (optional)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)
    to_date = '2019-10-20' # str | Filter transactions to this date. (optional)

    try:
        # List transactions by member
        api_response = api_instance.list_transactions_by_member(member_guid, user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)
        print("The response of MxPlatformApi->list_transactions_by_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_transactions_by_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **from_date** | **str**| Filter transactions from this date. | [optional] 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 
 **to_date** | **str**| Filter transactions to this date. | [optional] 

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

# **list_transactions_by_tag**
> TransactionsResponseBody list_transactions_by_tag(tag_guid, user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)

List transactions by tag

Use this endpoint to get a list of all transactions associated with a particular tag according to the tag’s unique GUID. In other words, a list of all transactions that have been assigned to a particular tag using the create a tagging endpoint.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    tag_guid = 'TAG-aef36e72-6294-4c38-844d-e573e80aed52' # str | The unique id for a `tag`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    from_date = '2015-09-20' # str | Filter transactions from this date. (optional)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)
    to_date = '2019-10-20' # str | Filter transactions to this date. (optional)

    try:
        # List transactions by tag
        api_response = api_instance.list_transactions_by_tag(tag_guid, user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)
        print("The response of MxPlatformApi->list_transactions_by_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_transactions_by_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_guid** | **str**| The unique id for a &#x60;tag&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **from_date** | **str**| Filter transactions from this date. | [optional] 
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 
 **to_date** | **str**| Filter transactions to this date. | [optional] 

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

# **list_user_accounts**
> AccountsResponseBody list_user_accounts(user_guid, member_is_managed_by_user=member_is_managed_by_user, page=page, is_manual=is_manual, records_per_page=records_per_page)

List accounts

This endpoint returns a list of all the accounts associated with the specified `user`.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    member_is_managed_by_user = true # bool | List only accounts whose member is managed by the user. (optional)
    page = 1 # int | Specify current page. (optional)
    is_manual = true # bool | List only accounts that were manually created. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    try:
        # List accounts
        api_response = api_instance.list_user_accounts(user_guid, member_is_managed_by_user=member_is_managed_by_user, page=page, is_manual=is_manual, records_per_page=records_per_page)
        print("The response of MxPlatformApi->list_user_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_user_accounts: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **member_is_managed_by_user** | **bool**| List only accounts whose member is managed by the user. | [optional] 
 **page** | **int**| Specify current page. | [optional] 
 **is_manual** | **bool**| List only accounts that were manually created. | [optional] 
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)
    id = 'u-12324-abdc' # str | The user `id` to search for. (optional)
    email = 'example@example.com' # str | The user `email` to search for. (optional)
    is_disabled = true # bool | Search for users that are diabled. (optional)

    try:
        # List users
        api_response = api_instance.list_users(page=page, records_per_page=records_per_page, id=id, email=email, is_disabled=is_disabled)
        print("The response of MxPlatformApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->list_users: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Specify current page. | [optional] 
 **records_per_page** | **int**| Specify records per page. | [optional] 
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Read account
        api_response = api_instance.read_account(account_guid, user_guid)
        print("The response of MxPlatformApi->read_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Read account by member
        api_response = api_instance.read_account_by_member(account_guid, member_guid, user_guid)
        print("The response of MxPlatformApi->read_account_by_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_account_by_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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

# **read_category**
> CategoryResponseBody read_category(category_guid, user_guid)

Read a custom category

Use this endpoint to read the attributes of either a default category or a custom category.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.category_response_body import CategoryResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    category_guid = 'CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874' # str | The unique id for a `category`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Read a custom category
        api_response = api_instance.read_category(category_guid, user_guid)
        print("The response of MxPlatformApi->read_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_category: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_guid** | **str**| The unique id for a &#x60;category&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

### Return type

[**CategoryResponseBody**](CategoryResponseBody.md)

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

# **read_default_category**
> CategoryResponseBody read_default_category(category_guid)

Read a default category

Use this endpoint to read the attributes of a default category.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.category_response_body import CategoryResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    category_guid = 'CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874' # str | The unique id for a `category`.

    try:
        # Read a default category
        api_response = api_instance.read_default_category(category_guid)
        print("The response of MxPlatformApi->read_default_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_default_category: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_guid** | **str**| The unique id for a &#x60;category&#x60;. | 

### Return type

[**CategoryResponseBody**](CategoryResponseBody.md)

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
> HoldingResponseBody read_holding(holding_guid, user_guid)

Read holding

Use this endpoint to read the attributes of a specific `holding`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.holding_response_body import HoldingResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    holding_guid = 'HOL-d65683e8-9eab-26bb-bcfd-ced159c9abe2' # str | The unique id for a `holding`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Read holding
        api_response = api_instance.read_holding(holding_guid, user_guid)
        print("The response of MxPlatformApi->read_holding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_holding: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **holding_guid** | **str**| The unique id for a &#x60;holding&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

### Return type

[**HoldingResponseBody**](HoldingResponseBody.md)

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

# **read_institution**
> InstitutionResponseBody read_institution(institution_code)

Read institution

This endpoint returns information about the institution specified by `institution_code`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.institution_response_body import InstitutionResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    institution_code = 'chase' # str | The institution_code of the institution.

    try:
        # Read institution
        api_response = api_instance.read_institution(institution_code)
        print("The response of MxPlatformApi->read_institution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_institution: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_code** | **str**| The institution_code of the institution. | 

### Return type

[**InstitutionResponseBody**](InstitutionResponseBody.md)

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Read managed account
        api_response = api_instance.read_managed_account(account_guid, member_guid, user_guid)
        print("The response of MxPlatformApi->read_managed_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_managed_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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

This endpoint returns the attributes of the specified partner-managed `member`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.member_response_body import MemberResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Read managed member
        api_response = api_instance.read_managed_member(member_guid, user_guid)
        print("The response of MxPlatformApi->read_managed_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_managed_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    transaction_guid = 'TRN-810828b0-5210-4878-9bd3-f4ce514f90c4' # str | The unique id for a `transaction`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Read managed transaction
        api_response = api_instance.read_managed_transaction(account_guid, member_guid, transaction_guid, user_guid)
        print("The response of MxPlatformApi->read_managed_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_managed_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **transaction_guid** | **str**| The unique id for a &#x60;transaction&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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

# **read_member**
> MemberResponseBody read_member(member_guid, user_guid)

Read member

Use this endpoint to read the attributes of a specific member.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.member_response_body import MemberResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Read member
        api_response = api_instance.read_member(member_guid, user_guid)
        print("The response of MxPlatformApi->read_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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

# **read_member_status**
> MemberStatusResponseBody read_member_status(member_guid, user_guid)

Read member status

This endpoint provides the status of the members most recent aggregation event. This is an important step in the aggregation process, and the results returned by this endpoint should determine what you do next in order to successfully aggregate a member. MX has introduced new, more detailed information on the current status of a members connection to a financial institution and the state of its aggregation - the connection_status field. These are intended to replace and expand upon the information provided in the status field, which will soon be deprecated; support for the status field remains for the time being.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.member_status_response_body import MemberStatusResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Read member status
        api_response = api_instance.read_member_status(member_guid, user_guid)
        print("The response of MxPlatformApi->read_member_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_member_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

### Return type

[**MemberStatusResponseBody**](MemberStatusResponseBody.md)

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

# **read_merchant**
> MerchantResponseBody read_merchant(merchant_guid)

Read merchant

Returns information about a particular merchant, such as a logo, name, and website.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.merchant_response_body import MerchantResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    merchant_guid = 'MCH-7ed79542-884d-2b1b-dd74-501c5cc9d25b' # str | The unique id for a `merchant`.

    try:
        # Read merchant
        api_response = api_instance.read_merchant(merchant_guid)
        print("The response of MxPlatformApi->read_merchant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_merchant: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_guid** | **str**| The unique id for a &#x60;merchant&#x60;. | 

### Return type

[**MerchantResponseBody**](MerchantResponseBody.md)

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

# **read_merchant_location**
> MerchantLocationResponseBody read_merchant_location(merchant_location_guid)

Read merchant location

This endpoint returns the specified merchant_location resource.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.merchant_location_response_body import MerchantLocationResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    merchant_location_guid = 'MCH-09466f0a-fb58-9d1a-bae2-2af0afbea621' # str | The unique id for a `merchant_location`.

    try:
        # Read merchant location
        api_response = api_instance.read_merchant_location(merchant_location_guid)
        print("The response of MxPlatformApi->read_merchant_location:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_merchant_location: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_location_guid** | **str**| The unique id for a &#x60;merchant_location&#x60;. | 

### Return type

[**MerchantLocationResponseBody**](MerchantLocationResponseBody.md)

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

# **read_rewards**
> RewardResponseBody read_rewards(user_guid, member_guid, reward_guid)

Read Reward

Use this endpoint to read a specific `reward` based on its unique GUID..

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.reward_response_body import RewardResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    member_guid = 'MBR-fa7537f3-48aa-a683-a02a-b18345562f54' # str | The unique identifier for the member. Defined by MX.
    reward_guid = 'RWD-fa7537f3-48aa-a683-a02a-b324322f54' # str | The unique identifier for the rewards. Defined by MX.

    try:
        # Read Reward
        api_response = api_instance.read_rewards(user_guid, member_guid, reward_guid)
        print("The response of MxPlatformApi->read_rewards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_rewards: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **member_guid** | **str**| The unique identifier for the member. Defined by MX. | 
 **reward_guid** | **str**| The unique identifier for the rewards. Defined by MX. | 

### Return type

[**RewardResponseBody**](RewardResponseBody.md)

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

# **read_statement_by_member**
> StatementResponseBody read_statement_by_member(member_guid, statement_guid, user_guid)

Read statement by member

Use this endpoint to read a JSON representation of the statement.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.statement_response_body import StatementResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    statement_guid = 'STA-737a344b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for a `statement`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Read statement by member
        api_response = api_instance.read_statement_by_member(member_guid, statement_guid, user_guid)
        print("The response of MxPlatformApi->read_statement_by_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_statement_by_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **statement_guid** | **str**| The unique id for a &#x60;statement&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

### Return type

[**StatementResponseBody**](StatementResponseBody.md)

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

# **read_tag**
> TagResponseBody read_tag(tag_guid, user_guid)

Read tag

Use this endpoint to read the attributes of a particular tag according to its unique GUID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.tag_response_body import TagResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    tag_guid = 'TAG-aef36e72-6294-4c38-844d-e573e80aed52' # str | The unique id for a `tag`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Read tag
        api_response = api_instance.read_tag(tag_guid, user_guid)
        print("The response of MxPlatformApi->read_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_guid** | **str**| The unique id for a &#x60;tag&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

### Return type

[**TagResponseBody**](TagResponseBody.md)

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

# **read_tagging**
> TaggingResponseBody read_tagging(tagging_guid, user_guid)

Read tagging

Use this endpoint to read the attributes of a `tagging` according to its unique GUID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.tagging_response_body import TaggingResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    tagging_guid = 'TGN-007f5486-17e1-45fc-8b87-8f03984430fe' # str | The unique id for a `tagging`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Read tagging
        api_response = api_instance.read_tagging(tagging_guid, user_guid)
        print("The response of MxPlatformApi->read_tagging:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_tagging: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tagging_guid** | **str**| The unique id for a &#x60;tagging&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

### Return type

[**TaggingResponseBody**](TaggingResponseBody.md)

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

# **read_tax_document**
> TaxDocumentResponseBody read_tax_document(tax_document_guid, member_guid, user_guid)

Read a Tax Document

Use this endpoint to read the attributes of the specified tax document.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.tax_document_response_body import TaxDocumentResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    tax_document_guid = 'TAX-987dfds1b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `tax_document`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Read a Tax Document
        api_response = api_instance.read_tax_document(tax_document_guid, member_guid, user_guid)
        print("The response of MxPlatformApi->read_tax_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_tax_document: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_document_guid** | **str**| The unique id for a &#x60;tax_document&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

### Return type

[**TaxDocumentResponseBody**](TaxDocumentResponseBody.md)

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
> TransactionResponseBody read_transaction(transaction_guid, user_guid)

Read transaction

Requests to this endpoint will return the attributes of the specified `transaction`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.transaction_response_body import TransactionResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    transaction_guid = 'TRN-810828b0-5210-4878-9bd3-f4ce514f90c4' # str | The unique id for a `transaction`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Read transaction
        api_response = api_instance.read_transaction(transaction_guid, user_guid)
        print("The response of MxPlatformApi->read_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_guid** | **str**| The unique id for a &#x60;transaction&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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

# **read_transaction_rule**
> TransactionRuleResponseBody read_transaction_rule(transaction_rule_guid, user_guid)

Read transaction rule

Use this endpoint to read the attributes of an existing transaction rule based on the rule’s unique GUID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.transaction_rule_response_body import TransactionRuleResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    transaction_rule_guid = 'TXR-a080e0f9-a2d4-4d6f-9e03-672cc357a4d3' # str | The unique id for a `transaction_rule`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Read transaction rule
        api_response = api_instance.read_transaction_rule(transaction_rule_guid, user_guid)
        print("The response of MxPlatformApi->read_transaction_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_transaction_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_rule_guid** | **str**| The unique id for a &#x60;transaction_rule&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

### Return type

[**TransactionRuleResponseBody**](TransactionRuleResponseBody.md)

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Read user
        api_response = api_instance.read_user(user_guid)
        print("The response of MxPlatformApi->read_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->read_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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

# **request_authorization_code**
> AuthorizationCodeResponseBody request_authorization_code(authorization_code_request_body)

Request an authorization code.

Clients use this endpoint to request an authorization code according to the parameters specified in the scope. Clients then pass this code to processors. Processor access is scoped only to the GUIDs and features specified in this request. Before requesting an authorization code which includes a member in the scope, clients must have verified that member.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.authorization_code_request_body import AuthorizationCodeRequestBody
from mx_platform_python.models.authorization_code_response_body import AuthorizationCodeResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    authorization_code_request_body = mx_platform_python.AuthorizationCodeRequestBody() # AuthorizationCodeRequestBody | The scope for the authorization code.

    try:
        # Request an authorization code.
        api_response = api_instance.request_authorization_code(authorization_code_request_body)
        print("The response of MxPlatformApi->request_authorization_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->request_authorization_code: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization_code_request_body** | [**AuthorizationCodeRequestBody**](AuthorizationCodeRequestBody.md)| The scope for the authorization code. | 

### Return type

[**AuthorizationCodeResponseBody**](AuthorizationCodeResponseBody.md)

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

# **request_connect_widget_url**
> ConnectWidgetResponseBody request_connect_widget_url(user_guid, connect_widget_request_body)

Request connect widget url

This endpoint will return a URL for an embeddable version of MX Connect.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.connect_widget_request_body import ConnectWidgetRequestBody
from mx_platform_python.models.connect_widget_response_body import ConnectWidgetResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    connect_widget_request_body = mx_platform_python.ConnectWidgetRequestBody() # ConnectWidgetRequestBody | Optional config options for WebView (is_mobile_webview, current_institution_code, current_member_guid, update_credentials)

    try:
        # Request connect widget url
        api_response = api_instance.request_connect_widget_url(user_guid, connect_widget_request_body)
        print("The response of MxPlatformApi->request_connect_widget_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->request_connect_widget_url: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **connect_widget_request_body** | [**ConnectWidgetRequestBody**](ConnectWidgetRequestBody.md)| Optional config options for WebView (is_mobile_webview, current_institution_code, current_member_guid, update_credentials) | 

### Return type

[**ConnectWidgetResponseBody**](ConnectWidgetResponseBody.md)

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

# **request_o_auth_window_uri**
> OAuthWindowResponseBody request_o_auth_window_uri(member_guid, user_guid, client_redirect_url=client_redirect_url, enable_app2app=enable_app2app, referral_source=referral_source, skip_aggregation=skip_aggregation, ui_message_webview_url_scheme=ui_message_webview_url_scheme)

Request oauth window uri

This endpoint will generate an `oauth_window_uri` for the specified `member`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.o_auth_window_response_body import OAuthWindowResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    client_redirect_url = 'https://mx.com' # str | A URL that MX will redirect to at the end of OAuth with additional query parameters. Only available with `referral_source=APP`. (optional)
    enable_app2app = 'false' # str | This indicates whether OAuth app2app behavior is enabled for institutions that support it. Defaults to `true`. This setting is not persistent. (optional)
    referral_source = 'APP' # str | Must be either `BROWSER` or `APP` depending on the implementation. Defaults to `BROWSER`. (optional)
    skip_aggregation = false # bool | Setting this parameter to `true` will prevent the member from automatically aggregating after being redirected from the authorization page. (optional)
    ui_message_webview_url_scheme = 'mx' # str | A scheme for routing the user back to the application state they were previously in. Only available with `referral_source=APP`. (optional)

    try:
        # Request oauth window uri
        api_response = api_instance.request_o_auth_window_uri(member_guid, user_guid, client_redirect_url=client_redirect_url, enable_app2app=enable_app2app, referral_source=referral_source, skip_aggregation=skip_aggregation, ui_message_webview_url_scheme=ui_message_webview_url_scheme)
        print("The response of MxPlatformApi->request_o_auth_window_uri:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->request_o_auth_window_uri: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **client_redirect_url** | **str**| A URL that MX will redirect to at the end of OAuth with additional query parameters. Only available with &#x60;referral_source&#x3D;APP&#x60;. | [optional] 
 **enable_app2app** | **str**| This indicates whether OAuth app2app behavior is enabled for institutions that support it. Defaults to &#x60;true&#x60;. This setting is not persistent. | [optional] 
 **referral_source** | **str**| Must be either &#x60;BROWSER&#x60; or &#x60;APP&#x60; depending on the implementation. Defaults to &#x60;BROWSER&#x60;. | [optional] 
 **skip_aggregation** | **bool**| Setting this parameter to &#x60;true&#x60; will prevent the member from automatically aggregating after being redirected from the authorization page. | [optional] 
 **ui_message_webview_url_scheme** | **str**| A scheme for routing the user back to the application state they were previously in. Only available with &#x60;referral_source&#x3D;APP&#x60;. | [optional] 

### Return type

[**OAuthWindowResponseBody**](OAuthWindowResponseBody.md)

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

# **request_widget_url**
> WidgetResponseBody request_widget_url(user_guid, widget_request_body, accept_language=accept_language)

Request widget url

This endpoint allows partners to get a URL by passing the `widget_type` in the request body, as well as configuring it in several different ways. In the case of Connect, that means setting the `widget_type` to `connect_widget`. Partners may also pass an optional `Accept-Language` header as well as a number of configuration options. Note that this is a `POST` request.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.widget_request_body import WidgetRequestBody
from mx_platform_python.models.widget_response_body import WidgetResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    widget_request_body = mx_platform_python.WidgetRequestBody() # WidgetRequestBody | The widget url configuration options.
    accept_language = 'en-US' # str | The desired language of the widget. (optional)

    try:
        # Request widget url
        api_response = api_instance.request_widget_url(user_guid, widget_request_body, accept_language=accept_language)
        print("The response of MxPlatformApi->request_widget_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->request_widget_url: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **widget_request_body** | [**WidgetRequestBody**](WidgetRequestBody.md)| The widget url configuration options. | 
 **accept_language** | **str**| The desired language of the widget. | [optional] 

### Return type

[**WidgetResponseBody**](WidgetResponseBody.md)

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

# **resume_aggregation**
> MemberResponseBody resume_aggregation(member_guid, user_guid, member_resume_request_body)

Resume aggregation

This endpoint answers the challenges needed when a member has been challenged by multi-factor authentication.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.member_response_body import MemberResponseBody
from mx_platform_python.models.member_resume_request_body import MemberResumeRequestBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    member_resume_request_body = mx_platform_python.MemberResumeRequestBody() # MemberResumeRequestBody | Member object with MFA challenge answers

    try:
        # Resume aggregation
        api_response = api_instance.resume_aggregation(member_guid, user_guid, member_resume_request_body)
        print("The response of MxPlatformApi->resume_aggregation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->resume_aggregation: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **member_resume_request_body** | [**MemberResumeRequestBody**](MemberResumeRequestBody.md)| Member object with MFA challenge answers | 

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
**202** | Accepted |  -  |

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    account_update_request_body = mx_platform_python.AccountUpdateRequestBody() # AccountUpdateRequestBody | 

    try:
        # Update account by member
        api_response = api_instance.update_account_by_member(account_guid, member_guid, user_guid, account_update_request_body)
        print("The response of MxPlatformApi->update_account_by_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->update_account_by_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
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

# **update_category**
> CategoryResponseBody update_category(category_guid, user_guid, category_update_request_body)

Update category

Use this endpoint to update the attributes of a custom category according to its unique GUID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.category_response_body import CategoryResponseBody
from mx_platform_python.models.category_update_request_body import CategoryUpdateRequestBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    category_guid = 'CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874' # str | The unique id for a `category`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    category_update_request_body = mx_platform_python.CategoryUpdateRequestBody() # CategoryUpdateRequestBody | Category object to be updated (While no single parameter is required, the `category` object cannot be empty)

    try:
        # Update category
        api_response = api_instance.update_category(category_guid, user_guid, category_update_request_body)
        print("The response of MxPlatformApi->update_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->update_category: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_guid** | **str**| The unique id for a &#x60;category&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **category_update_request_body** | [**CategoryUpdateRequestBody**](CategoryUpdateRequestBody.md)| Category object to be updated (While no single parameter is required, the &#x60;category&#x60; object cannot be empty) | 

### Return type

[**CategoryResponseBody**](CategoryResponseBody.md)

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    managed_account_update_request_body = mx_platform_python.ManagedAccountUpdateRequestBody() # ManagedAccountUpdateRequestBody | Managed account object to be updated (While no single parameter is required, the request body can't be empty)

    try:
        # Update managed account
        api_response = api_instance.update_managed_account(account_guid, member_guid, user_guid, managed_account_update_request_body)
        print("The response of MxPlatformApi->update_managed_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->update_managed_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    managed_member_update_request_body = mx_platform_python.ManagedMemberUpdateRequestBody() # ManagedMemberUpdateRequestBody | Managed member object to be updated (While no single parameter is required, the request body can't be empty)

    try:
        # Update managed member
        api_response = api_instance.update_managed_member(member_guid, user_guid, managed_member_update_request_body)
        print("The response of MxPlatformApi->update_managed_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->update_managed_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1' # str | The unique id for an `account`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    transaction_guid = 'TRN-810828b0-5210-4878-9bd3-f4ce514f90c4' # str | The unique id for a `transaction`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    managed_transaction_update_request_body = mx_platform_python.ManagedTransactionUpdateRequestBody() # ManagedTransactionUpdateRequestBody | Managed transaction object to be updated (While no single parameter is required, the request body can't be empty)

    try:
        # Update managed transaction
        api_response = api_instance.update_managed_transaction(account_guid, member_guid, transaction_guid, user_guid, managed_transaction_update_request_body)
        print("The response of MxPlatformApi->update_managed_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->update_managed_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **transaction_guid** | **str**| The unique id for a &#x60;transaction&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
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

# **update_member**
> MemberResponseBody update_member(member_guid, user_guid, member_update_request_body)

Update member

Use this endpoint to update a members attributes. Only the credentials, id, and metadata parameters can be updated. To get a list of the required credentials for the member, use the list member credentials endpoint.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.member_response_body import MemberResponseBody
from mx_platform_python.models.member_update_request_body import MemberUpdateRequestBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    member_update_request_body = mx_platform_python.MemberUpdateRequestBody() # MemberUpdateRequestBody | Member object to be updated (While no single parameter is required, the request body can't be empty)

    try:
        # Update member
        api_response = api_instance.update_member(member_guid, user_guid, member_update_request_body)
        print("The response of MxPlatformApi->update_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->update_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **member_update_request_body** | [**MemberUpdateRequestBody**](MemberUpdateRequestBody.md)| Member object to be updated (While no single parameter is required, the request body can&#39;t be empty) | 

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

# **update_tag**
> TagResponseBody update_tag(tag_guid, user_guid, tag_update_request_body)

Update tag

Use this endpoint to update the name of a specific tag according to its unique GUID.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.tag_response_body import TagResponseBody
from mx_platform_python.models.tag_update_request_body import TagUpdateRequestBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    tag_guid = 'TAG-aef36e72-6294-4c38-844d-e573e80aed52' # str | The unique id for a `tag`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    tag_update_request_body = mx_platform_python.TagUpdateRequestBody() # TagUpdateRequestBody | Tag object to be updated with required parameter (tag_guid)

    try:
        # Update tag
        api_response = api_instance.update_tag(tag_guid, user_guid, tag_update_request_body)
        print("The response of MxPlatformApi->update_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->update_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_guid** | **str**| The unique id for a &#x60;tag&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **tag_update_request_body** | [**TagUpdateRequestBody**](TagUpdateRequestBody.md)| Tag object to be updated with required parameter (tag_guid) | 

### Return type

[**TagResponseBody**](TagResponseBody.md)

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

# **update_tagging**
> TaggingResponseBody update_tagging(tagging_guid, user_guid, tagging_update_request_body)

Update tagging

Use this endpoint to update a tagging.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.tagging_response_body import TaggingResponseBody
from mx_platform_python.models.tagging_update_request_body import TaggingUpdateRequestBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    tagging_guid = 'TGN-007f5486-17e1-45fc-8b87-8f03984430fe' # str | The unique id for a `tagging`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    tagging_update_request_body = mx_platform_python.TaggingUpdateRequestBody() # TaggingUpdateRequestBody | Tagging object to be updated with required parameter (tag_guid)

    try:
        # Update tagging
        api_response = api_instance.update_tagging(tagging_guid, user_guid, tagging_update_request_body)
        print("The response of MxPlatformApi->update_tagging:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->update_tagging: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tagging_guid** | **str**| The unique id for a &#x60;tagging&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **tagging_update_request_body** | [**TaggingUpdateRequestBody**](TaggingUpdateRequestBody.md)| Tagging object to be updated with required parameter (tag_guid) | 

### Return type

[**TaggingResponseBody**](TaggingResponseBody.md)

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

# **update_transaction**
> TransactionResponseBody update_transaction(transaction_guid, user_guid, transaction_update_request_body)

Update transaction

Use this endpoint to update the `description` of a specific transaction according to its unique GUID.

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    transaction_guid = 'TRN-810828b0-5210-4878-9bd3-f4ce514f90c4' # str | The unique id for a `transaction`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    transaction_update_request_body = mx_platform_python.TransactionUpdateRequestBody() # TransactionUpdateRequestBody | Transaction object to be updated with a new description

    try:
        # Update transaction
        api_response = api_instance.update_transaction(transaction_guid, user_guid, transaction_update_request_body)
        print("The response of MxPlatformApi->update_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->update_transaction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_guid** | **str**| The unique id for a &#x60;transaction&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **transaction_update_request_body** | [**TransactionUpdateRequestBody**](TransactionUpdateRequestBody.md)| Transaction object to be updated with a new description | 

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

# **update_transaction_rule**
> TransactionRuleResponseBody update_transaction_rule(transaction_rule_guid, user_guid, transaction_rule_update_request_body)

Update transaction_rule

Use this endpoint to update the attributes of a specific transaction rule based on its unique GUID. The API will respond with the updated transaction_rule object. Any attributes not provided will be left unchanged.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.transaction_rule_response_body import TransactionRuleResponseBody
from mx_platform_python.models.transaction_rule_update_request_body import TransactionRuleUpdateRequestBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    transaction_rule_guid = 'TXR-a080e0f9-a2d4-4d6f-9e03-672cc357a4d3' # str | The unique id for a `transaction_rule`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    transaction_rule_update_request_body = mx_platform_python.TransactionRuleUpdateRequestBody() # TransactionRuleUpdateRequestBody | TransactionRule object to be updated

    try:
        # Update transaction_rule
        api_response = api_instance.update_transaction_rule(transaction_rule_guid, user_guid, transaction_rule_update_request_body)
        print("The response of MxPlatformApi->update_transaction_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->update_transaction_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_rule_guid** | **str**| The unique id for a &#x60;transaction_rule&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
 **transaction_rule_update_request_body** | [**TransactionRuleUpdateRequestBody**](TransactionRuleUpdateRequestBody.md)| TransactionRule object to be updated | 

### Return type

[**TransactionRuleResponseBody**](TransactionRuleResponseBody.md)

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.
    user_update_request_body = mx_platform_python.UserUpdateRequestBody() # UserUpdateRequestBody | User object to be updated (None of these parameters are required, but the user object cannot be empty.)

    try:
        # Update user
        api_response = api_instance.update_user(user_guid, user_update_request_body)
        print("The response of MxPlatformApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->update_user: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 
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

# **users_user_guid_monthly_cash_flow_profile_get**
> MonthlyCashFlowResponseBody users_user_guid_monthly_cash_flow_profile_get(user_guid)

Read monthly cash flow profile

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.monthly_cash_flow_response_body import MonthlyCashFlowResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'user_guid_example' # str | The unique identifier for the user.

    try:
        # Read monthly cash flow profile
        api_response = api_instance.users_user_guid_monthly_cash_flow_profile_get(user_guid)
        print("The response of MxPlatformApi->users_user_guid_monthly_cash_flow_profile_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->users_user_guid_monthly_cash_flow_profile_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. | 

### Return type

[**MonthlyCashFlowResponseBody**](MonthlyCashFlowResponseBody.md)

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

# **users_user_guid_monthly_cash_flow_profile_put**
> MonthlyCashFlowResponseBody users_user_guid_monthly_cash_flow_profile_put(user_guid, monthly_cash_flow_profile_request_body)

Update monthly cash flow profile

Use this endpoint to update the attributes of a `monthly_cash_flow_profile`.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.monthly_cash_flow_profile_request_body import MonthlyCashFlowProfileRequestBody
from mx_platform_python.models.monthly_cash_flow_response_body import MonthlyCashFlowResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'user_guid_example' # str | The unique identifier for the user.
    monthly_cash_flow_profile_request_body = mx_platform_python.MonthlyCashFlowProfileRequestBody() # MonthlyCashFlowProfileRequestBody | 

    try:
        # Update monthly cash flow profile
        api_response = api_instance.users_user_guid_monthly_cash_flow_profile_put(user_guid, monthly_cash_flow_profile_request_body)
        print("The response of MxPlatformApi->users_user_guid_monthly_cash_flow_profile_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->users_user_guid_monthly_cash_flow_profile_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. | 
 **monthly_cash_flow_profile_request_body** | [**MonthlyCashFlowProfileRequestBody**](MonthlyCashFlowProfileRequestBody.md)|  | 

### Return type

[**MonthlyCashFlowResponseBody**](MonthlyCashFlowResponseBody.md)

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

# **users_user_guid_transactions_transaction_guid_split_delete**
> users_user_guid_transactions_transaction_guid_split_delete(transaction_guid, user_guid)

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    transaction_guid = 'TRN-810828b0-5210-4878-9bd3-f4ce514f90c4' # str | The unique id for a `transaction`.
    user_guid = 'USR-85628b0-5210-4878-9bd3-f4ce154f90c4' # str | The unique id for a `user`.

    try:
        # Delete split transactions
        api_instance.users_user_guid_transactions_transaction_guid_split_delete(transaction_guid, user_guid)
    except Exception as e:
        print("Exception when calling MxPlatformApi->users_user_guid_transactions_transaction_guid_split_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_guid** | **str**| The unique id for a &#x60;transaction&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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

# **users_user_guid_transactions_transaction_guid_split_post**
> SplitTransactionsResponseBody users_user_guid_transactions_transaction_guid_split_post(user_guid, transaction_guid, split_transaction_request_body=split_transaction_request_body)

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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    user_guid = 'user_guid_example' # str | The unique identifier for the user. Defined by MX.
    transaction_guid = 'transaction_guid_example' # str | The unique identifier for the transaction. Defined by MX.
    split_transaction_request_body = mx_platform_python.SplitTransactionRequestBody() # SplitTransactionRequestBody |  (optional)

    try:
        # Create split transactions
        api_response = api_instance.users_user_guid_transactions_transaction_guid_split_post(user_guid, transaction_guid, split_transaction_request_body=split_transaction_request_body)
        print("The response of MxPlatformApi->users_user_guid_transactions_transaction_guid_split_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->users_user_guid_transactions_transaction_guid_split_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for the user. Defined by MX. | 
 **transaction_guid** | **str**| The unique identifier for the transaction. Defined by MX. | 
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

# **verify_member**
> MemberResponseBody verify_member(member_guid, user_guid)

Verify member

The verify endpoint begins a verification process for a member.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.member_response_body import MemberResponseBody
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
    api_instance = mx_platform_python.MxPlatformApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique id for a `user`.

    try:
        # Verify member
        api_response = api_instance.verify_member(member_guid, user_guid)
        print("The response of MxPlatformApi->verify_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MxPlatformApi->verify_member: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. | 

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

