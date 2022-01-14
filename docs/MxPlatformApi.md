# mx_platform_python.MxPlatformApi

All URIs are relative to *https://api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate_member**](MxPlatformApi.md#aggregate_member) | **POST** /users/{user_guid}/members/{member_guid}/aggregate | Aggregate member
[**check_balances**](MxPlatformApi.md#check_balances) | **POST** /users/{user_guid}/members/{member_guid}/check_balance | Check balances
[**create_category**](MxPlatformApi.md#create_category) | **POST** /users/{user_guid}/categories | Create category
[**create_managed_account**](MxPlatformApi.md#create_managed_account) | **POST** /users/{user_guid}/managed_members/{member_guid}/accounts | Create managed account
[**create_managed_member**](MxPlatformApi.md#create_managed_member) | **POST** /users/{user_guid}/managed_members | Create managed member
[**create_managed_transaction**](MxPlatformApi.md#create_managed_transaction) | **POST** /users/{user_guid}/managed_members/{member_guid}/transactions | Create managed transaction
[**create_member**](MxPlatformApi.md#create_member) | **POST** /users/{user_guid}/members | Create member
[**create_tag**](MxPlatformApi.md#create_tag) | **POST** /users/{user_guid}/tags | Create tag
[**create_tagging**](MxPlatformApi.md#create_tagging) | **POST** /users/{user_guid}/taggings | Create tagging
[**create_transaction_rule**](MxPlatformApi.md#create_transaction_rule) | **POST** /users/{user_guid}/transaction_rules | Create transaction rule
[**create_user**](MxPlatformApi.md#create_user) | **POST** /users | Create user
[**delete_category**](MxPlatformApi.md#delete_category) | **DELETE** /users/{user_guid}/categories/{category_guid} | Delete category
[**delete_managed_account**](MxPlatformApi.md#delete_managed_account) | **DELETE** /users/{user_guid}/managed_members/{member_guid}/accounts/{account_guid} | Delete managed account
[**delete_managed_member**](MxPlatformApi.md#delete_managed_member) | **DELETE** /users/{user_guid}/managed_members/{member_guid} | Delete managed member
[**delete_managed_transaction**](MxPlatformApi.md#delete_managed_transaction) | **DELETE** /users/{user_guid}/managed_members/{member_guid}/transactions/{transaction_guid} | Delete managed transaction
[**delete_member**](MxPlatformApi.md#delete_member) | **DELETE** /users/{user_guid}/members/{member_guid} | Delete member
[**delete_tag**](MxPlatformApi.md#delete_tag) | **DELETE** /users/{user_guid}/tags/{tag_guid} | Delete tag
[**delete_tagging**](MxPlatformApi.md#delete_tagging) | **DELETE** /users/{user_guid}/taggings/{tagging_guid} | Delete tagging
[**delete_transaction_rule**](MxPlatformApi.md#delete_transaction_rule) | **DELETE** /users/{user_guid}/transaction_rules/{transaction_rule_guid} | Delete transaction rule
[**delete_user**](MxPlatformApi.md#delete_user) | **DELETE** /users/{user_guid} | Delete user
[**download_statement_pdf**](MxPlatformApi.md#download_statement_pdf) | **GET** /users/{user_guid}/members/{member_guid}/statements/{statement_guid}.pdf | Download statement pdf
[**enhance_transactions**](MxPlatformApi.md#enhance_transactions) | **POST** /transactions/enhance | Enhance transactions
[**extend_history**](MxPlatformApi.md#extend_history) | **POST** /users/{user_guid}/members/{member_guid}/extend_history | Extend history
[**fetch_statements**](MxPlatformApi.md#fetch_statements) | **POST** /users/{user_guid}/members/{member_guid}/fetch_statements | Fetch statements
[**identify_member**](MxPlatformApi.md#identify_member) | **POST** /users/{user_guid}/members/{member_guid}/identify | Identify member
[**list_account_numbers_by_account**](MxPlatformApi.md#list_account_numbers_by_account) | **GET** /users/{user_guid}/accounts/{account_guid}/account_numbers | List account numbers by account
[**list_account_numbers_by_member**](MxPlatformApi.md#list_account_numbers_by_member) | **GET** /users/{user_guid}/members/{member_guid}/account_numbers | List account numbers by member
[**list_account_owners_by_member**](MxPlatformApi.md#list_account_owners_by_member) | **GET** /users/{user_guid}/members/{member_guid}/account_owners | List account owners by member
[**list_categories**](MxPlatformApi.md#list_categories) | **GET** /users/{user_guid}/categories | List categories
[**list_default_categories**](MxPlatformApi.md#list_default_categories) | **GET** /categories/default | List default categories
[**list_default_categories_by_user**](MxPlatformApi.md#list_default_categories_by_user) | **GET** /users/{user_guid}/categories/default | List default categories by user
[**list_favorite_institutions**](MxPlatformApi.md#list_favorite_institutions) | **GET** /institutions/favorites | List favorite institutions
[**list_holdings**](MxPlatformApi.md#list_holdings) | **GET** /users/{user_guid}/holdings | List holdings
[**list_holdings_by_member**](MxPlatformApi.md#list_holdings_by_member) | **GET** /users/{user_guid}/members/{member_guid}/holdings | List holdings by member
[**list_institution_credentials**](MxPlatformApi.md#list_institution_credentials) | **GET** /institutions/{institution_code}/credentials | List institution credentials
[**list_institutions**](MxPlatformApi.md#list_institutions) | **GET** /institutions | List institutions
[**list_managed_accounts**](MxPlatformApi.md#list_managed_accounts) | **GET** /users/{user_guid}/managed_members/{member_guid}/accounts | List managed accounts
[**list_managed_institutions**](MxPlatformApi.md#list_managed_institutions) | **GET** /managed_institutions | List managed institutions
[**list_managed_members**](MxPlatformApi.md#list_managed_members) | **GET** /users/{user_guid}/managed_members | List managed members
[**list_managed_transactions**](MxPlatformApi.md#list_managed_transactions) | **GET** /users/{user_guid}/managed_members/{member_guid}/transactions | List managed transactions
[**list_member_challenges**](MxPlatformApi.md#list_member_challenges) | **GET** /users/{user_guid}/members/{member_guid}/challenges | List member challenges
[**list_member_credentials**](MxPlatformApi.md#list_member_credentials) | **GET** /users/{user_guid}/members/{member_guid}/credentials | List member credentials
[**list_members**](MxPlatformApi.md#list_members) | **GET** /users/{user_guid}/members | List members
[**list_merchants**](MxPlatformApi.md#list_merchants) | **GET** /merchants | List merchants
[**list_statements_by_member**](MxPlatformApi.md#list_statements_by_member) | **GET** /users/{user_guid}/members/{member_guid}/statements | List statements by member
[**list_taggings**](MxPlatformApi.md#list_taggings) | **GET** /users/{user_guid}/taggings | List taggings
[**list_tags**](MxPlatformApi.md#list_tags) | **GET** /users/{user_guid}/tags | List tags
[**list_transaction_rules**](MxPlatformApi.md#list_transaction_rules) | **GET** /users/{user_guid}/transaction_rules | List transaction rules
[**list_transactions**](MxPlatformApi.md#list_transactions) | **GET** /users/{user_guid}/transactions | List transactions
[**list_transactions_by_account**](MxPlatformApi.md#list_transactions_by_account) | **GET** /users/{user_guid}/accounts/{account_guid}/transactions | List transactions by account
[**list_transactions_by_member**](MxPlatformApi.md#list_transactions_by_member) | **GET** /users/{user_guid}/members/{member_guid}/transactions | List transactions by member
[**list_transactions_by_tag**](MxPlatformApi.md#list_transactions_by_tag) | **GET** /users/{user_guid}/tags/{tag_guid}/transactions | List transactions by tag
[**list_user_accounts**](MxPlatformApi.md#list_user_accounts) | **GET** /users/{user_guid}/accounts | List accounts
[**list_users**](MxPlatformApi.md#list_users) | **GET** /users | List users
[**read_account**](MxPlatformApi.md#read_account) | **GET** /users/{user_guid}/accounts/{account_guid} | Read account
[**read_category**](MxPlatformApi.md#read_category) | **GET** /users/{user_guid}/categories/{category_guid} | Read a custom category
[**read_default_category**](MxPlatformApi.md#read_default_category) | **GET** /categories/{category_guid} | Read a default category
[**read_holding**](MxPlatformApi.md#read_holding) | **GET** /users/{user_guid}/holdings/{holding_guid} | Read holding
[**read_institution**](MxPlatformApi.md#read_institution) | **GET** /institutions/{institution_code} | Read institution
[**read_managed_account**](MxPlatformApi.md#read_managed_account) | **GET** /users/{user_guid}/managed_members/{member_guid}/accounts/{account_guid} | Read managed account
[**read_managed_member**](MxPlatformApi.md#read_managed_member) | **GET** /users/{user_guid}/managed_members/{member_guid} | Read managed member
[**read_managed_transaction**](MxPlatformApi.md#read_managed_transaction) | **GET** /users/{user_guid}/managed_members/{member_guid}/transactions/{transaction_guid} | Read managed transaction
[**read_member**](MxPlatformApi.md#read_member) | **GET** /users/{user_guid}/members/{member_guid} | Read member
[**read_member_status**](MxPlatformApi.md#read_member_status) | **GET** /users/{user_guid}/members/{member_guid}/status | Read member status
[**read_merchant**](MxPlatformApi.md#read_merchant) | **GET** /merchants/{merchant_guid} | Read merchant
[**read_merchant_location**](MxPlatformApi.md#read_merchant_location) | **GET** /merchant_locations/{merchant_location_guid} | Read merchant location
[**read_statement_by_member**](MxPlatformApi.md#read_statement_by_member) | **GET** /users/{user_guid}/members/{member_guid}/statements/{statement_guid} | Read statement by member
[**read_tag**](MxPlatformApi.md#read_tag) | **GET** /users/{user_guid}/tags/{tag_guid} | Read tag
[**read_tagging**](MxPlatformApi.md#read_tagging) | **GET** /users/{user_guid}/taggings/{tagging_guid} | Read tagging
[**read_transaction**](MxPlatformApi.md#read_transaction) | **GET** /users/{user_guid}/transactions/{transaction_guid} | Read transaction
[**read_transaction_rule**](MxPlatformApi.md#read_transaction_rule) | **GET** /users/{user_guid}/transaction_rules/{transaction_rule_guid} | Read transaction rule
[**read_user**](MxPlatformApi.md#read_user) | **GET** /users/{user_guid} | Read user
[**request_connect_widget_url**](MxPlatformApi.md#request_connect_widget_url) | **POST** /users/{user_guid}/connect_widget_url | Request connect widget url
[**request_o_auth_window_uri**](MxPlatformApi.md#request_o_auth_window_uri) | **GET** /users/{user_guid}/members/{member_guid}/oauth_window_uri | Request oauth window uri
[**request_widget_url**](MxPlatformApi.md#request_widget_url) | **POST** /users/{user_guid}/widget_urls | Request widget url
[**resume_aggregation**](MxPlatformApi.md#resume_aggregation) | **PUT** /users/{user_guid}/members/{member_guid}/resume | Resume aggregation
[**update_account_by_member**](MxPlatformApi.md#update_account_by_member) | **PUT** /users/{user_guid}/members/{member_guid}/accounts/{account_guid} | Update account by member
[**update_category**](MxPlatformApi.md#update_category) | **PUT** /users/{user_guid}/categories/{category_guid} | Update category
[**update_managed_account**](MxPlatformApi.md#update_managed_account) | **PUT** /users/{user_guid}/managed_members/{member_guid}/accounts/{account_guid} | Update managed account
[**update_managed_member**](MxPlatformApi.md#update_managed_member) | **PUT** /users/{user_guid}/managed_members/{member_guid} | Update managed member
[**update_managed_transaction**](MxPlatformApi.md#update_managed_transaction) | **PUT** /users/{user_guid}/managed_members/{member_guid}/transactions/{transaction_guid} | Update managed transaction
[**update_member**](MxPlatformApi.md#update_member) | **PUT** /users/{user_guid}/members/{member_guid} | Update member
[**update_tag**](MxPlatformApi.md#update_tag) | **PUT** /users/{user_guid}/tags/{tag_guid} | Update tag
[**update_tagging**](MxPlatformApi.md#update_tagging) | **PUT** /users/{user_guid}/taggings/{tagging_guid} | Update tagging
[**update_transaction**](MxPlatformApi.md#update_transaction) | **PUT** /users/{user_guid}/transactions/{transaction_guid} | Update transaction
[**update_transaction_rule**](MxPlatformApi.md#update_transaction_rule) | **PUT** /users/{user_guid}/transaction_rules/{transaction_rule_guid} | Update transaction_rule
[**update_user**](MxPlatformApi.md#update_user) | **PUT** /users/{user_guid} | Update user
[**verify_member**](MxPlatformApi.md#verify_member) | **POST** /users/{user_guid}/members/{member_guid}/verify | Verify member


# **aggregate_member**
> MemberResponseBody aggregate_member(member_guid, user_guid)

Aggregate member

Calling this endpoint initiates an aggregation event for the member. This brings in the latest account and transaction data from the connected institution. If this data has recently been updated, MX may not initiate an aggregation event.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.member_response_body import MemberResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Aggregate member
        api_response = api_instance.aggregate_member(member_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->aggregate_member: %s\n" % e)
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

# **check_balances**
> MemberResponseBody check_balances(member_guid, user_guid)

Check balances

This endpoint operates much like the aggregate member endpoint except that it gathers only account balance information; it does not gather any transaction data.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.member_response_body import MemberResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Check balances
        api_response = api_instance.check_balances(member_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.category_create_request_body import CategoryCreateRequestBody
from mx_platform_python.model.category_response_body import CategoryResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    category_create_request_body = CategoryCreateRequestBody(
        category=CategoryCreateRequest(
            metadata="some metadata",
            name="Online Shopping",
            parent_guid="CAT-aad51b46-d6f7-3da5-fd6e-492328b3023f",
        ),
    ) # CategoryCreateRequestBody | Custom category object to be created

    # example passing only required values which don't have defaults set
    try:
        # Create category
        api_response = api_instance.create_category(user_guid, category_create_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> AccountResponseBody create_managed_account(user_guid, member_guid, managed_account_create_request_body)

Create managed account

Use this endpoint to create a partner-managed account.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.account_response_body import AccountResponseBody
from mx_platform_python.model.managed_account_create_request_body import ManagedAccountCreateRequestBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    managed_account_create_request_body = ManagedAccountCreateRequestBody(
        account=ManagedAccountCreateRequest(
            account_number="5366",
            apr=1.0,
            apy=1.0,
            available_balance=1000.0,
            available_credit=1000.0,
            balance=1000.0,
            cash_surrender_value=1000.0,
            credit_limit=100.0,
            currency_code="USD",
            day_payment_is_due=20,
            death_benefit=1000,
            id="1040434698",
            interest_rate=1.0,
            is_closed=False,
            is_hidden=False,
            last_payment=100.0,
            last_payment_at="2015-10-13T17:57:37.000Z",
            loan_amount=1000.0,
            matures_on="2015-10-13T17:57:37.000Z",
            metadata="some metadata",
            minimum_balance=100.0,
            minimum_payment=10.0,
            name="Test account 2",
            nickname="Swiss Account",
            original_balance=10.0,
            payment_due_at="2015-10-13T17:57:37.000Z",
            payoff_balance=10.0,
            routing_number="68899990000000",
            started_on="2015-10-13T17:57:37.000Z",
            subtype="NONE",
            type="SAVINGS",
        ),
    ) # ManagedAccountCreateRequestBody | Managed account to be created.

    # example passing only required values which don't have defaults set
    try:
        # Create managed account
        api_response = api_instance.create_managed_account(user_guid, member_guid, managed_account_create_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->create_managed_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. |
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. |
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.member_response_body import MemberResponseBody
from mx_platform_python.model.managed_member_create_request_body import ManagedMemberCreateRequestBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    managed_member_create_request_body = ManagedMemberCreateRequestBody(
        member=ManagedMemberCreateRequest(
            id="member123",
            institution_code="mxbank",
            metadata="some metadata",
            name="MX Bank",
        ),
    ) # ManagedMemberCreateRequestBody | Managed member to be created.

    # example passing only required values which don't have defaults set
    try:
        # Create managed member
        api_response = api_instance.create_managed_member(user_guid, managed_member_create_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> TransactionResponseBody create_managed_transaction(user_guid, member_guid, managed_transaction_create_request_body)

Create managed transaction

Use this endpoint to create a new partner-managed `transaction`.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.transaction_response_body import TransactionResponseBody
from mx_platform_python.model.managed_transaction_create_request_body import ManagedTransactionCreateRequestBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    managed_transaction_create_request_body = ManagedTransactionCreateRequestBody(
        transaction=ManagedTransactionCreateRequest(
            amount="61.11",
            category="Groceries",
            check_number_string="6812",
            currency_code="USD",
            description="Whole foods",
            id="transaction-265abee9-889b-af6a-c69b-25157db2bdd9",
            is_international=False,
            latitude=-43.2075,
            localized_description="This is a localized_description",
            localized_memo="This is a localized_memo",
            longitude=139.691706,
            memo="This is a memo",
            merchant_category_code=5411,
            merchant_guid="MCH-7ed79542-884d-2b1b-dd74-501c5cc9d25b",
            merchant_location_guid="MCL-00024e59-18b5-4d79-b879-2a7896726fea",
            metadata="some metadata",
            posted_at="2016-10-07T06:00:00.000Z",
            status="POSTED",
            transacted_at="2016-10-06T13:00:00.000Z",
            type="DEBIT",
        ),
    ) # ManagedTransactionCreateRequestBody | Managed transaction to be created.

    # example passing only required values which don't have defaults set
    try:
        # Create managed transaction
        api_response = api_instance.create_managed_transaction(user_guid, member_guid, managed_transaction_create_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->create_managed_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. |
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. |
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

# **create_member**
> MemberResponseBody create_member(user_guid, member_create_request_body)

Create member

This endpoint allows you to create a new member. Members are created with the required parameters credentials and institution_code, and the optional parameters id and metadata. When creating a member, youll need to include the correct type of credential required by the financial institution and provided by the user. You can find out which credential type is required with the `/institutions/{institution_code}/credentials` endpoint. If successful, the MX Platform API will respond with the newly-created member object. Once you successfully create a member, MX will immediately validate the provided credentials and attempt to aggregate data for accounts and transactions.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.member_create_request_body import MemberCreateRequestBody
from mx_platform_python.model.member_response_body import MemberResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    member_create_request_body = MemberCreateRequestBody(
        member=MemberCreateRequest(
            background_aggregation_is_disabled=False,
            credentials=[
                CredentialRequest(
                    guid="CRD-27d0edb8-1d50-5b90-bcbc-be270ca42b9f",
                    value="password",
                ),
            ],
            id="unique_id",
            institution_code="chase",
            is_oauth=False,
            metadata="\"credentials_last_refreshed_at\": \"2015-10-15\"",
            skip_aggregation=False,
        ),
        referral_source="APP",
        ui_message_webview_url_scheme="mx",
    ) # MemberCreateRequestBody | Member object to be created with optional parameters (id and metadata) and required parameters (credentials and institution_code)

    # example passing only required values which don't have defaults set
    try:
        # Create member
        api_response = api_instance.create_member(user_guid, member_create_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.tag_response_body import TagResponseBody
from mx_platform_python.model.tag_create_request_body import TagCreateRequestBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    tag_create_request_body = TagCreateRequestBody(
        tag=TagCreateRequest(
            name="MY TAG",
        ),
    ) # TagCreateRequestBody | Tag object to be created with required parameters (tag_guid)

    # example passing only required values which don't have defaults set
    try:
        # Create tag
        api_response = api_instance.create_tag(user_guid, tag_create_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.tagging_response_body import TaggingResponseBody
from mx_platform_python.model.tagging_create_request_body import TaggingCreateRequestBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    tagging_create_request_body = TaggingCreateRequestBody(
        tagging=TaggingCreateRequest(
            tag_guid="TAG-40faf068-abb4-405c-8f6a-e883ed541fff",
            transaction_guid="TRN-810828b0-5210-4878-9bd3-f4ce514f90c4",
        ),
    ) # TaggingCreateRequestBody | Tagging object to be created with required parameters (tag_guid and transaction_guid)

    # example passing only required values which don't have defaults set
    try:
        # Create tagging
        api_response = api_instance.create_tagging(user_guid, tagging_create_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.transaction_rule_create_request_body import TransactionRuleCreateRequestBody
from mx_platform_python.model.transaction_rule_response_body import TransactionRuleResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    transaction_rule_create_request_body = TransactionRuleCreateRequestBody(
        transaction_rule=TransactionRuleCreateRequest(
            category_guid="CAT-b1de2a04-db08-b6ed-f6fe-ca2f5b11c2d0",
            description="Wal-mart food storage",
            match_description="Wal-mart",
        ),
    ) # TransactionRuleCreateRequestBody | TransactionRule object to be created with optional parameters (description) and required parameters (category_guid and match_description)

    # example passing only required values which don't have defaults set
    try:
        # Create transaction rule
        api_response = api_instance.create_transaction_rule(user_guid, transaction_rule_create_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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

Call this endpoint to create a new user. The MX Platform API will respond with the newly-created user object if successful. This endpoint accepts several parameters - id, metadata, and is_disabled. Disabling a user means that accounts and transactions associated with it will not be updated in the background by MX. It will also restrict access to that users data until they are no longer disabled. Users who are disabled for the entirety of an MX Platform API billing period will not be factored into that months bill.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.user_response_body import UserResponseBody
from mx_platform_python.model.user_create_request_body import UserCreateRequestBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_create_request_body = UserCreateRequestBody(
        user=UserCreateRequest(
            email="email@provider.com",
            id="My-Unique-ID",
            is_disabled=False,
            metadata="{\"first_name\": \"Steven\", \"last_name\": \"Universe\"}",
        ),
    ) # UserCreateRequestBody | User object to be created. (None of these parameters are required, but the user object cannot be empty)

    # example passing only required values which don't have defaults set
    try:
        # Create user
        api_response = api_instance.create_user(user_create_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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

# **delete_category**
> delete_category(category_guid, user_guid)

Delete category

Use this endpoint to delete a specific custom category according to its unique GUID. The API will respond with an empty object and a status of `204 No Content`.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    category_guid = "CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874" # str | The unique id for a `category`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Delete category
        api_instance.delete_category(category_guid, user_guid)
    except mx_platform_python.ApiException as e:
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
> delete_managed_account(member_guid, user_guid, account_guid)

Delete managed account

Use this endpoint to delete a partner-managed account according to its unique GUID. If successful, the API will respond with a status of `204 No Content`.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    account_guid = "ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1" # str | The unique id for an `account`.

    # example passing only required values which don't have defaults set
    try:
        # Delete managed account
        api_instance.delete_managed_account(member_guid, user_guid, account_guid)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->delete_managed_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. |
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. |
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. |

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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Delete managed member
        api_instance.delete_managed_member(member_guid, user_guid)
    except mx_platform_python.ApiException as e:
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
> delete_managed_transaction(member_guid, user_guid, transaction_guid)

Delete managed transaction

Use this endpoint to delete the specified partner-managed `transaction`. The endpoint will respond with a status of `204 No Content` without a resource.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    transaction_guid = "TRN-810828b0-5210-4878-9bd3-f4ce514f90c4" # str | The unique id for a `transaction`.

    # example passing only required values which don't have defaults set
    try:
        # Delete managed transaction
        api_instance.delete_managed_transaction(member_guid, user_guid, transaction_guid)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->delete_managed_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. |
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. |
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_member**
> delete_member(member_guid, user_guid)

Delete member

Accessing this endpoint will permanently delete a member.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Delete member
        api_instance.delete_member(member_guid, user_guid)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    tag_guid = "TAG-aef36e72-6294-4c38-844d-e573e80aed52" # str | The unique id for a `tag`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Delete tag
        api_instance.delete_tag(tag_guid, user_guid)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    tagging_guid = "TGN-007f5486-17e1-45fc-8b87-8f03984430fe" # str | The unique id for a `tagging`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Delete tagging
        api_instance.delete_tagging(tagging_guid, user_guid)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    transaction_rule_guid = "TXR-a080e0f9-a2d4-4d6f-9e03-672cc357a4d3" # str | The unique id for a `transaction_rule`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Delete transaction rule
        api_instance.delete_transaction_rule(transaction_rule_guid, user_guid)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Delete user
        api_instance.delete_user(user_guid)
    except mx_platform_python.ApiException as e:
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

# **download_statement_pdf**
> file_type download_statement_pdf(member_guid, statement_guid, user_guid)

Download statement pdf

Use this endpoint to download a specified statement PDF.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    statement_guid = "STA-737a344b-caae-0f6e-1384-01f52e75dcb1" # str | The unique id for a `statement`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Download statement pdf
        api_response = api_instance.download_statement_pdf(member_guid, statement_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->download_statement_pdf: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. |
 **statement_guid** | **str**| The unique id for a &#x60;statement&#x60;. |
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. |

### Return type

**file_type**

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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.enhance_transactions_response_body import EnhanceTransactionsResponseBody
from mx_platform_python.model.enhance_transactions_request_body import EnhanceTransactionsRequestBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    enhance_transactions_request_body = EnhanceTransactionsRequestBody(
        transactions=[
            EnhanceTransactionsRequest(
                amount=21.33,
                description="ubr* pending.uber.com",
                extended_transaction_type="partner_transaction_type",
                id="ID-123",
                memo="Additional-information*on_transaction",
                merchant_category_code=4121,
                type="DEBIT",
            ),
        ],
    ) # EnhanceTransactionsRequestBody | Transaction object to be enhanced

    # example passing only required values which don't have defaults set
    try:
        # Enhance transactions
        api_response = api_instance.enhance_transactions(enhance_transactions_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.member_response_body import MemberResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique identifier for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique identifier for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Extend history
        api_response = api_instance.extend_history(member_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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

# **fetch_statements**
> MemberResponseBody fetch_statements(member_guid, user_guid)

Fetch statements

Use this endpoint to fetch the statements associated with a particular member.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.member_response_body import MemberResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Fetch statements
        api_response = api_instance.fetch_statements(member_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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

# **identify_member**
> MemberResponseBody identify_member(member_guid, user_guid)

Identify member

The identify endpoint begins an identification process for an already-existing member.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.member_response_body import MemberResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Identify member
        api_response = api_instance.identify_member(member_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> AccountNumbersResponseBody list_account_numbers_by_account(account_guid, user_guid)

List account numbers by account

This endpoint returns a list of account numbers associated with the specified `account`.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.account_numbers_response_body import AccountNumbersResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    account_guid = "ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1" # str | The unique id for an `account`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List account numbers by account
        api_response = api_instance.list_account_numbers_by_account(account_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_account_numbers_by_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List account numbers by account
        api_response = api_instance.list_account_numbers_by_account(account_guid, user_guid, page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> AccountNumbersResponseBody list_account_numbers_by_member(member_guid, user_guid)

List account numbers by member

This endpoint returns a list of account numbers associated with the specified `member`.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.account_numbers_response_body import AccountNumbersResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List account numbers by member
        api_response = api_instance.list_account_numbers_by_member(member_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_account_numbers_by_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List account numbers by member
        api_response = api_instance.list_account_numbers_by_member(member_guid, user_guid, page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> AccountOwnersResponseBody list_account_owners_by_member(member_guid, user_guid)

List account owners by member

This endpoint returns an array with information about every account associated with a particular member.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.account_owners_response_body import AccountOwnersResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List account owners by member
        api_response = api_instance.list_account_owners_by_member(member_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_account_owners_by_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List account owners by member
        api_response = api_instance.list_account_owners_by_member(member_guid, user_guid, page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> CategoriesResponseBody list_categories(user_guid)

List categories

Use this endpoint to list all categories associated with a `user`, including both default and custom categories.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.categories_response_body import CategoriesResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List categories
        api_response = api_instance.list_categories(user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_categories: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List categories
        api_response = api_instance.list_categories(user_guid, page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> CategoriesResponseBody list_default_categories()

List default categories

Use this endpoint to retrieve a list of all the default categories and subcategories offered within the MX Platform API. In other words, each item in the returned list will have its `is_default` field set to `true`. There are currently 119 default categories and subcategories. Both the _list default categories_ and _list default categories by user_ endpoints return the same results. The different routes are provided for convenience.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.categories_response_body import CategoriesResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List default categories
        api_response = api_instance.list_default_categories(page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> CategoriesResponseBody list_default_categories_by_user(user_guid)

List default categories by user

Use this endpoint to retrieve a list of all the default categories and subcategories, scoped by user, offered within the MX Platform API. In other words, each item in the returned list will have its `is_default` field set to `true`. There are currently 119 default categories and subcategories. Both the _list default categories_ and _list default categories by user_ endpoints return the same results. The different routes are provided for convenience.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.categories_response_body import CategoriesResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List default categories by user
        api_response = api_instance.list_default_categories_by_user(user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_default_categories_by_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List default categories by user
        api_response = api_instance.list_default_categories_by_user(user_guid, page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> InstitutionsResponseBody list_favorite_institutions()

List favorite institutions

This endpoint returns a paginated list containing institutions that have been set as the partner’s favorites, sorted by popularity. Please contact MX to set a list of favorites.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.institutions_response_body import InstitutionsResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List favorite institutions
        api_response = api_instance.list_favorite_institutions(page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> HoldingsResponseBody list_holdings(user_guid)

List holdings

This endpoint returns all holdings associated with the specified `user` across all accounts and members.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.holdings_response_body import HoldingsResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    from_date = "2015-09-20" # str | Filter holdings from this date. (optional)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)
    to_date = "2019-10-20" # str | Filter holdings to this date. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List holdings
        api_response = api_instance.list_holdings(user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_holdings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List holdings
        api_response = api_instance.list_holdings(user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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

# **list_holdings_by_member**
> HoldingsResponseBody list_holdings_by_member(member_guid, user_guid)

List holdings by member

This endpoint returns all holdings associated with the specified `member` across all accounts.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.holdings_response_body import HoldingsResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    from_date = "2015-09-20" # str | Filter holdings from this date. (optional)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)
    to_date = "2019-10-20" # str | Filter holdings to this date. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List holdings by member
        api_response = api_instance.list_holdings_by_member(member_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_holdings_by_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List holdings by member
        api_response = api_instance.list_holdings_by_member(member_guid, user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> CredentialsResponseBody list_institution_credentials(institution_code)

List institution credentials

Use this endpoint to see which credentials will be needed to create a member for a specific institution.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.credentials_response_body import CredentialsResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    institution_code = "chase" # str | The institution_code of the institution.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List institution credentials
        api_response = api_instance.list_institution_credentials(institution_code)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_institution_credentials: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List institution credentials
        api_response = api_instance.list_institution_credentials(institution_code, page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> InstitutionsResponseBody list_institutions()

List institutions

This endpoint returns a list of institutions based on the specified search term or parameter.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.institutions_response_body import InstitutionsResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    name = "chase" # str | This will list only institutions in which the appended string appears. (optional)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)
    supports_account_identification = True # bool | Filter only institutions which support account identification. (optional)
    supports_account_statement = True # bool | Filter only institutions which support account statements. (optional)
    supports_account_verification = True # bool | Filter only institutions which support account verification. (optional)
    supports_transaction_history = True # bool | Filter only institutions which support extended transaction history. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List institutions
        api_response = api_instance.list_institutions(name=name, page=page, records_per_page=records_per_page, supports_account_identification=supports_account_identification, supports_account_statement=supports_account_statement, supports_account_verification=supports_account_verification, supports_transaction_history=supports_transaction_history)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> AccountsResponseBody list_managed_accounts(user_guid, member_guid)

List managed accounts

Use this endpoint to retrieve a list of all the partner-managed accounts associated with the given partner-manage member.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.accounts_response_body import AccountsResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List managed accounts
        api_response = api_instance.list_managed_accounts(user_guid, member_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_managed_accounts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List managed accounts
        api_response = api_instance.list_managed_accounts(user_guid, member_guid, page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_managed_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. |
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. |
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
> InstitutionsResponseBody list_managed_institutions()

List managed institutions

This endpoint returns a list of institutions which can be used to create partner-managed members.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.institutions_response_body import InstitutionsResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List managed institutions
        api_response = api_instance.list_managed_institutions(page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> MembersResponseBody list_managed_members(user_guid)

List managed members

This endpoint returns a list of all the partner-managed members associated with the specified `user`.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.members_response_body import MembersResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List managed members
        api_response = api_instance.list_managed_members(user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_managed_members: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List managed members
        api_response = api_instance.list_managed_members(user_guid, page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> TransactionsResponseBody list_managed_transactions(user_guid, member_guid)

List managed transactions

This endpoint returns a list of all the partner-managed transactions associated with the specified `account`, scoped through a `user` and a `member`.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.transactions_response_body import TransactionsResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List managed transactions
        api_response = api_instance.list_managed_transactions(user_guid, member_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_managed_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List managed transactions
        api_response = api_instance.list_managed_transactions(user_guid, member_guid, page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_managed_transactions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. |
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. |
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

# **list_member_challenges**
> ChallengesResponseBody list_member_challenges(member_guid, user_guid)

List member challenges

Use this endpoint for information on what multi-factor authentication challenges need to be answered in order to aggregate a member. If the aggregation is not challenged, i.e., the member does not have a connection status of `CHALLENGED`, then code `204 No Content` will be returned. If the aggregation has been challenged, i.e., the member does have a connection status of `CHALLENGED`, then code `200 OK` will be returned - along with the corresponding credentials.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.challenges_response_body import ChallengesResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List member challenges
        api_response = api_instance.list_member_challenges(member_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_member_challenges: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List member challenges
        api_response = api_instance.list_member_challenges(member_guid, user_guid, page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> CredentialsResponseBody list_member_credentials(member_guid, user_guid)

List member credentials

This endpoint returns an array which contains information on every non-MFA credential associated with a specific member.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.credentials_response_body import CredentialsResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List member credentials
        api_response = api_instance.list_member_credentials(member_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_member_credentials: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List member credentials
        api_response = api_instance.list_member_credentials(member_guid, user_guid, page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> MembersResponseBody list_members(user_guid)

List members

This endpoint returns an array which contains information on every member associated with a specific user.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.members_response_body import MembersResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List members
        api_response = api_instance.list_members(user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_members: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List members
        api_response = api_instance.list_members(user_guid, page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> MerchantsResponseBody list_merchants()

List merchants

This endpoint returns a paginated list of all the merchants in the MX system.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.merchants_response_body import MerchantsResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List merchants
        api_response = api_instance.list_merchants(page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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

# **list_statements_by_member**
> StatementsResponseBody list_statements_by_member(member_guid, user_guid)

List statements by member

Use this endpoint to get an array of available statements.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.statements_response_body import StatementsResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List statements by member
        api_response = api_instance.list_statements_by_member(member_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_statements_by_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List statements by member
        api_response = api_instance.list_statements_by_member(member_guid, user_guid, page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> TaggingsResponseBody list_taggings(user_guid)

List taggings

Use this endpoint to retrieve a list of all the taggings associated with a specific user.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.taggings_response_body import TaggingsResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List taggings
        api_response = api_instance.list_taggings(user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_taggings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List taggings
        api_response = api_instance.list_taggings(user_guid, page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> TagsResponseBody list_tags(user_guid)

List tags

Use this endpoint to list all tags associated with the specified `user`. Each user includes the `Business` tag by default.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.tags_response_body import TagsResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List tags
        api_response = api_instance.list_tags(user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List tags
        api_response = api_instance.list_tags(user_guid, page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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

# **list_transaction_rules**
> TransactionRulesResponseBody list_transaction_rules(user_guid)

List transaction rules

Use this endpoint to read the attributes of all existing transaction rules belonging to the user.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.transaction_rules_response_body import TransactionRulesResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List transaction rules
        api_response = api_instance.list_transaction_rules(user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_transaction_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List transaction rules
        api_response = api_instance.list_transaction_rules(user_guid, page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> TransactionsResponseBody list_transactions(user_guid)

List transactions

Requests to this endpoint return a list of transactions associated with the specified `user`, accross all members and accounts associated with that `user`.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.transactions_response_body import TransactionsResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    from_date = "2015-09-20" # str | Filter transactions from this date. (optional)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)
    to_date = "2019-10-20" # str | Filter transactions to this date. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List transactions
        api_response = api_instance.list_transactions(user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_transactions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List transactions
        api_response = api_instance.list_transactions(user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> TransactionsResponseBody list_transactions_by_account(account_guid, user_guid)

List transactions by account

This endpoint returns a list of the last 90 days of transactions associated with the specified account.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.transactions_response_body import TransactionsResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    account_guid = "ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1" # str | The unique id for an `account`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    from_date = "2015-09-20" # str | Filter transactions from this date. (optional)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)
    to_date = "2019-10-20" # str | Filter transactions to this date. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List transactions by account
        api_response = api_instance.list_transactions_by_account(account_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_transactions_by_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List transactions by account
        api_response = api_instance.list_transactions_by_account(account_guid, user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> TransactionsResponseBody list_transactions_by_member(member_guid, user_guid)

List transactions by member

Requests to this endpoint return a list of transactions associated with the specified `member`, accross all accounts associated with that `member`.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.transactions_response_body import TransactionsResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    from_date = "2015-09-20" # str | Filter transactions from this date. (optional)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)
    to_date = "2019-10-20" # str | Filter transactions to this date. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List transactions by member
        api_response = api_instance.list_transactions_by_member(member_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_transactions_by_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List transactions by member
        api_response = api_instance.list_transactions_by_member(member_guid, user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> TransactionsResponseBody list_transactions_by_tag(tag_guid, user_guid)

List transactions by tag

Use this endpoint to get a list of all transactions associated with a particular tag according to the tag’s unique GUID. In other words, a list of all transactions that have been assigned to a particular tag using the create a tagging endpoint.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.transactions_response_body import TransactionsResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    tag_guid = "TAG-aef36e72-6294-4c38-844d-e573e80aed52" # str | The unique id for a `tag`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    from_date = "2015-09-20" # str | Filter transactions from this date. (optional)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)
    to_date = "2019-10-20" # str | Filter transactions to this date. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List transactions by tag
        api_response = api_instance.list_transactions_by_tag(tag_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_transactions_by_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List transactions by tag
        api_response = api_instance.list_transactions_by_tag(tag_guid, user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> AccountsResponseBody list_user_accounts(user_guid)

List accounts

This endpoint returns a list of all the accounts associated with the specified `user`.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.accounts_response_body import AccountsResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List accounts
        api_response = api_instance.list_user_accounts(user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_user_accounts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List accounts
        api_response = api_instance.list_user_accounts(user_guid, page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_user_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **list_users**
> UsersResponseBody list_users()

List users

Use this endpoint to list every user you've created in the MX Platform API.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.users_response_body import UsersResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    page = 1 # int | Specify current page. (optional)
    records_per_page = 10 # int | Specify records per page. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List users
        api_response = api_instance.list_users(page=page, records_per_page=records_per_page)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->list_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Specify current page. | [optional]
 **records_per_page** | **int**| Specify records per page. | [optional]

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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.account_response_body import AccountResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    account_guid = "ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1" # str | The unique id for an `account`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Read account
        api_response = api_instance.read_account(account_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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

# **read_category**
> CategoryResponseBody read_category(category_guid, user_guid)

Read a custom category

Use this endpoint to read the attributes of either a default category or a custom category.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.category_response_body import CategoryResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    category_guid = "CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874" # str | The unique id for a `category`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Read a custom category
        api_response = api_instance.read_category(category_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> CategoryResponseBody read_default_category(category_guid, user_guid)

Read a default category

Use this endpoint to read the attributes of a default category.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.category_response_body import CategoryResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    category_guid = "CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874" # str | The unique id for a `category`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Read a default category
        api_response = api_instance.read_default_category(category_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->read_default_category: %s\n" % e)
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

# **read_holding**
> HoldingResponseBody read_holding(holding_guid, user_guid)

Read holding

Use this endpoint to read the attributes of a specific `holding`.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.holding_response_body import HoldingResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    holding_guid = "HOL-d65683e8-9eab-26bb-bcfd-ced159c9abe2" # str | The unique id for a `holding`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Read holding
        api_response = api_instance.read_holding(holding_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.institution_response_body import InstitutionResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    institution_code = "chase" # str | The institution_code of the institution.

    # example passing only required values which don't have defaults set
    try:
        # Read institution
        api_response = api_instance.read_institution(institution_code)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> AccountResponseBody read_managed_account(member_guid, user_guid, account_guid)

Read managed account

Use this endpoint to read the attributes of a partner-managed account according to its unique guid.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.account_response_body import AccountResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    account_guid = "ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1" # str | The unique id for an `account`.

    # example passing only required values which don't have defaults set
    try:
        # Read managed account
        api_response = api_instance.read_managed_account(member_guid, user_guid, account_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->read_managed_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. |
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. |
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. |

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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.member_response_body import MemberResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Read managed member
        api_response = api_instance.read_managed_member(member_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> TransactionResponseBody read_managed_transaction(member_guid, user_guid, transaction_guid)

Read managed transaction

Requests to this endpoint will return the attributes of the specified partner-managed `transaction`.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.transaction_response_body import TransactionResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    transaction_guid = "TRN-810828b0-5210-4878-9bd3-f4ce514f90c4" # str | The unique id for a `transaction`.

    # example passing only required values which don't have defaults set
    try:
        # Read managed transaction
        api_response = api_instance.read_managed_transaction(member_guid, user_guid, transaction_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->read_managed_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. |
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. |
 **transaction_guid** | **str**| The unique id for a &#x60;transaction&#x60;. |

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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.member_response_body import MemberResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Read member
        api_response = api_instance.read_member(member_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.member_status_response_body import MemberStatusResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Read member status
        api_response = api_instance.read_member_status(member_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.merchant_response_body import MerchantResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    merchant_guid = "MCH-7ed79542-884d-2b1b-dd74-501c5cc9d25b" # str | The unique id for a `merchant`.

    # example passing only required values which don't have defaults set
    try:
        # Read merchant
        api_response = api_instance.read_merchant(merchant_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.merchant_location_response_body import MerchantLocationResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    merchant_location_guid = "MCH-09466f0a-fb58-9d1a-bae2-2af0afbea621" # str | The unique id for a `merchant_location`.

    # example passing only required values which don't have defaults set
    try:
        # Read merchant location
        api_response = api_instance.read_merchant_location(merchant_location_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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

# **read_statement_by_member**
> StatementResponseBody read_statement_by_member(member_guid, statement_guid, user_guid)

Read statement by member

Use this endpoint to read a JSON representation of the statement.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.statement_response_body import StatementResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    statement_guid = "STA-737a344b-caae-0f6e-1384-01f52e75dcb1" # str | The unique id for a `statement`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Read statement by member
        api_response = api_instance.read_statement_by_member(member_guid, statement_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.tag_response_body import TagResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    tag_guid = "TAG-aef36e72-6294-4c38-844d-e573e80aed52" # str | The unique id for a `tag`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Read tag
        api_response = api_instance.read_tag(tag_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.tagging_response_body import TaggingResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    tagging_guid = "TGN-007f5486-17e1-45fc-8b87-8f03984430fe" # str | The unique id for a `tagging`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Read tagging
        api_response = api_instance.read_tagging(tagging_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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

# **read_transaction**
> TransactionResponseBody read_transaction(transaction_guid, user_guid)

Read transaction

Requests to this endpoint will return the attributes of the specified `transaction`.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.transaction_response_body import TransactionResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    transaction_guid = "TRN-810828b0-5210-4878-9bd3-f4ce514f90c4" # str | The unique id for a `transaction`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Read transaction
        api_response = api_instance.read_transaction(transaction_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.transaction_rule_response_body import TransactionRuleResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    transaction_rule_guid = "TXR-a080e0f9-a2d4-4d6f-9e03-672cc357a4d3" # str | The unique id for a `transaction_rule`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Read transaction rule
        api_response = api_instance.read_transaction_rule(transaction_rule_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.user_response_body import UserResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Read user
        api_response = api_instance.read_user(user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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

# **request_connect_widget_url**
> ConnectWidgetResponseBody request_connect_widget_url(user_guid)

Request connect widget url

This endpoint will return a URL for an embeddable version of MX Connect.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.connect_widget_response_body import ConnectWidgetResponseBody
from mx_platform_python.model.connect_widget_request_body import ConnectWidgetRequestBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    connect_widget_request_body = ConnectWidgetRequestBody(
        config=ConnectWidgetRequest(
            color_scheme="light",
            current_institution_code="chase",
            current_member_guid="MBR-7c6f361b-e582-15b6-60c0-358f12466b4b",
            disable_institution_search=False,
            include_transactions=True,
            is_mobile_webview=True,
            mode="aggregation",
            ui_message_version=4,
            ui_message_webview_url_scheme="mx",
            update_credentials=False,
            wait_for_full_aggregation=False,
        ),
    ) # ConnectWidgetRequestBody | Optional config options for WebView (is_mobile_webview, current_institution_code, current_member_guid, update_credentials) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Request connect widget url
        api_response = api_instance.request_connect_widget_url(user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->request_connect_widget_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Request connect widget url
        api_response = api_instance.request_connect_widget_url(user_guid, connect_widget_request_body=connect_widget_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->request_connect_widget_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. |
 **connect_widget_request_body** | [**ConnectWidgetRequestBody**](ConnectWidgetRequestBody.md)| Optional config options for WebView (is_mobile_webview, current_institution_code, current_member_guid, update_credentials) | [optional]

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
> OAuthWindowResponseBody request_o_auth_window_uri(member_guid, user_guid)

Request oauth window uri

This endpoint will generate an `oauth_window_uri` for the specified `member`.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.o_auth_window_response_body import OAuthWindowResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    referral_source = "APP" # str | Must be either `BROWSER` or `APP` depending on the implementation. Defaults to `BROWSER`. (optional)
    ui_message_webview_url_scheme = "mx" # str | A scheme for routing the user back to the application state they were previously in. (optional)
    skip_aggregation = False # bool | Setting this parameter to `true` will prevent the member from automatically aggregating after being redirected from the authorization page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Request oauth window uri
        api_response = api_instance.request_o_auth_window_uri(member_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->request_o_auth_window_uri: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Request oauth window uri
        api_response = api_instance.request_o_auth_window_uri(member_guid, user_guid, referral_source=referral_source, ui_message_webview_url_scheme=ui_message_webview_url_scheme, skip_aggregation=skip_aggregation)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->request_o_auth_window_uri: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. |
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. |
 **referral_source** | **str**| Must be either &#x60;BROWSER&#x60; or &#x60;APP&#x60; depending on the implementation. Defaults to &#x60;BROWSER&#x60;. | [optional]
 **ui_message_webview_url_scheme** | **str**| A scheme for routing the user back to the application state they were previously in. | [optional]
 **skip_aggregation** | **bool**| Setting this parameter to &#x60;true&#x60; will prevent the member from automatically aggregating after being redirected from the authorization page. | [optional]

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
> WidgetResponseBody request_widget_url(user_guid, widget_request_body)

Request widget url

This endpoint allows partners to get a URL by passing the `widget_type` in the request body, as well as configuring it in several different ways. In the case of Connect, that means setting the `widget_type` to `connect_widget`. Partners may also pass an optional `Accept-Language` header as well as a number of configuration options. Note that this is a `POST` request.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.widget_request_body import WidgetRequestBody
from mx_platform_python.model.widget_response_body import WidgetResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    widget_request_body = WidgetRequestBody(
        widget_url=WidgetRequest(
            color_scheme="light",
            current_institution_code="chase",
            current_institution_guid="INS-f1a3285d-e855-b61f-6aa7-8ae575c0e0e9",
            current_member_guid="MBR-7c6f361b-e582-15b6-60c0-358f12466b4b",
            disable_institution_search=False,
            include_transactions=True,
            is_mobile_webview=True,
            mode="aggregation",
            ui_message_version=4,
            ui_message_webview_url_scheme="mx",
            update_credentials=False,
            wait_for_full_aggregation=False,
            widget_type="connect_widget",
        ),
    ) # WidgetRequestBody | The widget url configuration options.
    accept_language = "en-US" # str | The desired language of the widget. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Request widget url
        api_response = api_instance.request_widget_url(user_guid, widget_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->request_widget_url: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Request widget url
        api_response = api_instance.request_widget_url(user_guid, widget_request_body, accept_language=accept_language)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.member_response_body import MemberResponseBody
from mx_platform_python.model.member_resume_request_body import MemberResumeRequestBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    member_resume_request_body = MemberResumeRequestBody(
        member=MemberResumeRequest(
            challenges=[
                CredentialRequest(
                    guid="CRD-27d0edb8-1d50-5b90-bcbc-be270ca42b9f",
                    value="password",
                ),
            ],
        ),
    ) # MemberResumeRequestBody | Member object with MFA challenge answers

    # example passing only required values which don't have defaults set
    try:
        # Resume aggregation
        api_response = api_instance.resume_aggregation(member_guid, user_guid, member_resume_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> AccountResponseBody update_account_by_member(user_guid, member_guid, account_guid, account_update_request_body)

Update account by member

This endpoint allows you to update certain attributes of an `account` resource.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.account_response_body import AccountResponseBody
from mx_platform_python.model.account_update_request_body import AccountUpdateRequestBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    account_guid = "ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1" # str | The unique id for an `account`.
    account_update_request_body = AccountUpdateRequestBody(
        account=AccountUpdateRequest(
            is_hidden=False,
        ),
    ) # AccountUpdateRequestBody | Account object to be created with optional parameters (is_hidden)

    # example passing only required values which don't have defaults set
    try:
        # Update account by member
        api_response = api_instance.update_account_by_member(user_guid, member_guid, account_guid, account_update_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->update_account_by_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. |
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. |
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. |
 **account_update_request_body** | [**AccountUpdateRequestBody**](AccountUpdateRequestBody.md)| Account object to be created with optional parameters (is_hidden) |

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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.category_update_request_body import CategoryUpdateRequestBody
from mx_platform_python.model.category_response_body import CategoryResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    category_guid = "CAT-7829f71c-2e8c-afa5-2f55-fa3634b89874" # str | The unique id for a `category`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    category_update_request_body = CategoryUpdateRequestBody(
        category=CategoryUpdateRequest(
            metadata="some metadata",
            name="Web shopping",
        ),
    ) # CategoryUpdateRequestBody | Category object to be updated (While no single parameter is required, the `category` object cannot be empty)

    # example passing only required values which don't have defaults set
    try:
        # Update category
        api_response = api_instance.update_category(category_guid, user_guid, category_update_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> AccountResponseBody update_managed_account(member_guid, user_guid, account_guid, managed_account_update_request_body)

Update managed account

Use this endpoint to update the attributes of a partner-managed account according to its unique GUID.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.account_response_body import AccountResponseBody
from mx_platform_python.model.managed_account_update_request_body import ManagedAccountUpdateRequestBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    account_guid = "ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1" # str | The unique id for an `account`.
    managed_account_update_request_body = ManagedAccountUpdateRequestBody(
        account=ManagedAccountUpdateRequest(
            account_number="5366",
            apr=1.0,
            apy=1.0,
            available_balance=1000.0,
            available_credit=1000.0,
            balance=1000.0,
            cash_surrender_value=1000.0,
            credit_limit=100.0,
            currency_code="USD",
            day_payment_is_due=20,
            death_benefit=1000,
            id="1040434698",
            interest_rate=1.0,
            is_closed=False,
            is_hidden=False,
            last_payment=100.0,
            last_payment_at="2015-10-13T17:57:37.000Z",
            loan_amount=1000.0,
            matures_on="2015-10-13T17:57:37.000Z",
            metadata="some metadata",
            minimum_balance=100.0,
            minimum_payment=10.0,
            name="Test account 2",
            nickname="Swiss Account",
            original_balance=10.0,
            payment_due_at="2015-10-13T17:57:37.000Z",
            payoff_balance=10.0,
            routing_number="68899990000000",
            started_on="2015-10-13T17:57:37.000Z",
            subtype="NONE",
            type="SAVINGS",
        ),
    ) # ManagedAccountUpdateRequestBody | Managed account object to be updated (While no single parameter is required, the request body can't be empty)

    # example passing only required values which don't have defaults set
    try:
        # Update managed account
        api_response = api_instance.update_managed_account(member_guid, user_guid, account_guid, managed_account_update_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->update_managed_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. |
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. |
 **account_guid** | **str**| The unique id for an &#x60;account&#x60;. |
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.managed_member_update_request_body import ManagedMemberUpdateRequestBody
from mx_platform_python.model.member_response_body import MemberResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    managed_member_update_request_body = ManagedMemberUpdateRequestBody(
        member=ManagedMemberUpdateRequest(
            id="member123",
            metadata="some metadata",
            name="MX Bank",
        ),
    ) # ManagedMemberUpdateRequestBody | Managed member object to be updated (While no single parameter is required, the request body can't be empty)

    # example passing only required values which don't have defaults set
    try:
        # Update managed member
        api_response = api_instance.update_managed_member(member_guid, user_guid, managed_member_update_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
> TransactionResponseBody update_managed_transaction(member_guid, user_guid, transaction_guid, managed_transaction_update_request_body)

Update managed transaction

Use this endpoint to update the attributes of the specified partner_managed `transaction`.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.managed_transaction_update_request_body import ManagedTransactionUpdateRequestBody
from mx_platform_python.model.transaction_response_body import TransactionResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    transaction_guid = "TRN-810828b0-5210-4878-9bd3-f4ce514f90c4" # str | The unique id for a `transaction`.
    managed_transaction_update_request_body = ManagedTransactionUpdateRequestBody(
        transaction=ManagedTransactionUpdateRequest(
            amount="61.11",
            category="Groceries",
            check_number_string="6812",
            currency_code="USD",
            description="Whole foods",
            id="transaction-265abee9-889b-af6a-c69b-25157db2bdd9",
            is_international=False,
            latitude=-43.2075,
            localized_description="This is a localized_description",
            localized_memo="This is a localized_memo",
            longitude=139.691706,
            memo="This is a memo",
            merchant_category_code=5411,
            merchant_guid="MCH-7ed79542-884d-2b1b-dd74-501c5cc9d25b",
            merchant_location_guid="MCL-00024e59-18b5-4d79-b879-2a7896726fea",
            metadata="some metadata",
            posted_at="2016-10-07T06:00:00.000Z",
            status="POSTED",
            transacted_at="2016-10-06T13:00:00.000Z",
            type="DEBIT",
        ),
    ) # ManagedTransactionUpdateRequestBody | Managed transaction object to be updated (While no single parameter is required, the request body can't be empty)

    # example passing only required values which don't have defaults set
    try:
        # Update managed transaction
        api_response = api_instance.update_managed_transaction(member_guid, user_guid, transaction_guid, managed_transaction_update_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
        print("Exception when calling MxPlatformApi->update_managed_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. |
 **user_guid** | **str**| The unique id for a &#x60;user&#x60;. |
 **transaction_guid** | **str**| The unique id for a &#x60;transaction&#x60;. |
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.member_response_body import MemberResponseBody
from mx_platform_python.model.member_update_request_body import MemberUpdateRequestBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    member_update_request_body = MemberUpdateRequestBody(
        member=MemberUpdateRequest(
            background_aggregation_is_disabled=False,
            credentials=[
                CredentialRequest(
                    guid="CRD-27d0edb8-1d50-5b90-bcbc-be270ca42b9f",
                    value="password",
                ),
            ],
            id="unique_id",
            metadata="\"credentials_last_refreshed_at\": \"2015-10-15\"",
            skip_aggregation=False,
        ),
    ) # MemberUpdateRequestBody | Member object to be updated (While no single parameter is required, the request body can't be empty)

    # example passing only required values which don't have defaults set
    try:
        # Update member
        api_response = api_instance.update_member(member_guid, user_guid, member_update_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.tag_response_body import TagResponseBody
from mx_platform_python.model.tag_update_request_body import TagUpdateRequestBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    tag_guid = "TAG-aef36e72-6294-4c38-844d-e573e80aed52" # str | The unique id for a `tag`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    tag_update_request_body = TagUpdateRequestBody(
        tag=TagUpdateRequest(
            name="MY TAG",
        ),
    ) # TagUpdateRequestBody | Tag object to be updated with required parameter (tag_guid)

    # example passing only required values which don't have defaults set
    try:
        # Update tag
        api_response = api_instance.update_tag(tag_guid, user_guid, tag_update_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.tagging_response_body import TaggingResponseBody
from mx_platform_python.model.tagging_update_request_body import TaggingUpdateRequestBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    tagging_guid = "TGN-007f5486-17e1-45fc-8b87-8f03984430fe" # str | The unique id for a `tagging`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    tagging_update_request_body = TaggingUpdateRequestBody(
        tagging=TaggingUpdateRequest(
            tag_guid="TAG-40faf068-abb4-405c-8f6a-e883ed541fff",
        ),
    ) # TaggingUpdateRequestBody | Tagging object to be updated with required parameter (tag_guid)

    # example passing only required values which don't have defaults set
    try:
        # Update tagging
        api_response = api_instance.update_tagging(tagging_guid, user_guid, tagging_update_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.transaction_response_body import TransactionResponseBody
from mx_platform_python.model.transaction_update_request_body import TransactionUpdateRequestBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    transaction_guid = "TRN-810828b0-5210-4878-9bd3-f4ce514f90c4" # str | The unique id for a `transaction`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    transaction_update_request_body = TransactionUpdateRequestBody(
        transaction=TransactionUpdateRequest(
            description="new description",
        ),
    ) # TransactionUpdateRequestBody | Transaction object to be updated with a new description

    # example passing only required values which don't have defaults set
    try:
        # Update transaction
        api_response = api_instance.update_transaction(transaction_guid, user_guid, transaction_update_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.transaction_rule_response_body import TransactionRuleResponseBody
from mx_platform_python.model.transaction_rule_update_request_body import TransactionRuleUpdateRequestBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    transaction_rule_guid = "TXR-a080e0f9-a2d4-4d6f-9e03-672cc357a4d3" # str | The unique id for a `transaction_rule`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    transaction_rule_update_request_body = TransactionRuleUpdateRequestBody(
        transaction_rule=TransactionRuleUpdateRequest(
            category_guid="CAT-b1de2a04-db08-b6ed-f6fe-ca2f5b11c2d0",
            description="Wal-mart food storage",
            match_description="Wal-mart",
        ),
    ) # TransactionRuleUpdateRequestBody | TransactionRule object to be updated

    # example passing only required values which don't have defaults set
    try:
        # Update transaction_rule
        api_response = api_instance.update_transaction_rule(transaction_rule_guid, user_guid, transaction_rule_update_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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

Use this endpoint to update the attributes of a specific user. The MX Platform API will respond with the updated user object. Disabling a user means that accounts and transactions associated with it will not be updated in the background by MX. It will also restrict access to that users data until they are no longer disabled. Users who are disabled for the entirety of an MX Platform API billing period will not be factored into that months bill. To disable a user, update it and set the is_disabled parameter to true. Set it to false to re-enable the user.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.user_response_body import UserResponseBody
from mx_platform_python.model.user_update_request_body import UserUpdateRequestBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.
    user_update_request_body = UserUpdateRequestBody(
        user=UserUpdateRequest(
            email="email@provider.com",
            id="My-Unique-ID",
            is_disabled=False,
            metadata="{\"first_name\": \"Steven\", \"last_name\": \"Universe\"}",
        ),
    ) # UserUpdateRequestBody | User object to be updated (None of these parameters are required, but the user object cannot be empty.)

    # example passing only required values which don't have defaults set
    try:
        # Update user
        api_response = api_instance.update_user(user_guid, user_update_request_body)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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

# **verify_member**
> MemberResponseBody verify_member(member_guid, user_guid)

Verify member

The verify endpoint begins a verification process for a member.

### Example

* Basic Authentication (basicAuth):

```python
import time
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.model.member_response_body import MemberResponseBody
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
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with mx_platform_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mx_platform_api.MxPlatformApi(api_client)
    member_guid = "MBR-7c6f361b-e582-15b6-60c0-358f12466b4b" # str | The unique id for a `member`.
    user_guid = "USR-fa7537f3-48aa-a683-a02a-b18940482f54" # str | The unique id for a `user`.

    # example passing only required values which don't have defaults set
    try:
        # Verify member
        api_response = api_instance.verify_member(member_guid, user_guid)
        pprint(api_response)
    except mx_platform_python.ApiException as e:
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

