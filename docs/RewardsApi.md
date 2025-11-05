# mx_platform_python.RewardsApi

All URIs are relative to *https://int-api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credit_card**](RewardsApi.md#credit_card) | **GET** /credit_card_products/{credit_card_product_guid} | Read a Credit Card Product
[**fetch_rewards**](RewardsApi.md#fetch_rewards) | **POST** /users/{user_guid}/members/{member_guid}/fetch_rewards | Fetch Rewards
[**list_rewards**](RewardsApi.md#list_rewards) | **GET** /users/{user_guid}/members/{member_guid}/rewards | List Rewards
[**read_rewards**](RewardsApi.md#read_rewards) | **GET** /users/{user_guid}/members/{member_guid}/rewards/{reward_guid} | Read Reward


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
    api_instance = mx_platform_python.RewardsApi(api_client)
    credit_card_product_guid = 'credit_card_product_guid' # str | The required `credit_card_product_guid` can be found on the `account` object.

    try:
        # Read a Credit Card Product
        api_response = api_instance.credit_card(credit_card_product_guid)
        print("The response of RewardsApi->credit_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RewardsApi->credit_card: %s\n" % e)
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

# **fetch_rewards**
> MemberResponseBody fetch_rewards(user_guid, member_guid)

Fetch Rewards

Calling this endpoint initiates an aggregation-type event which will gather the member's rewards information, as well as account and transaction information. Rewards data is also gathered with daily background aggregations. Member and Rewards guids are defined by MX.

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
    api_instance = mx_platform_python.RewardsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.

    try:
        # Fetch Rewards
        api_response = api_instance.fetch_rewards(user_guid, member_guid)
        print("The response of RewardsApi->fetch_rewards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RewardsApi->fetch_rewards: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 

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

# **list_rewards**
> RewardsResponseBody list_rewards(user_guid, member_guid)

List Rewards

Use this endpoint to list all the `rewards` associated with a specified `member`. Member guids are defined by MX.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.rewards_response_body import RewardsResponseBody
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
    api_instance = mx_platform_python.RewardsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.

    try:
        # List Rewards
        api_response = api_instance.list_rewards(user_guid, member_guid)
        print("The response of RewardsApi->list_rewards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RewardsApi->list_rewards: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 

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

# **read_rewards**
> RewardResponseBody read_rewards(user_guid, member_guid, reward_guid)

Read Reward

Use this endpoint to read a specific `reward` based on its unique GUID. Member and Rewards guids are defined by MX.

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.reward_response_body import RewardResponseBody
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
    api_instance = mx_platform_python.RewardsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    reward_guid = 'RWD-fa7537f3-48aa-a683-a02a-b324322f54' # str | The unique identifier for the rewards. Defined by MX.

    try:
        # Read Reward
        api_response = api_instance.read_rewards(user_guid, member_guid, reward_guid)
        print("The response of RewardsApi->read_rewards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RewardsApi->read_rewards: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
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

