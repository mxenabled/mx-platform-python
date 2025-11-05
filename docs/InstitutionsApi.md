# mx_platform_python.InstitutionsApi

All URIs are relative to *https://int-api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_favorite_institutions**](InstitutionsApi.md#list_favorite_institutions) | **GET** /institutions/favorites | List favorite institutions
[**list_institution_credentials**](InstitutionsApi.md#list_institution_credentials) | **GET** /institutions/{institution_code}/credentials | List institution credentials
[**list_institutions**](InstitutionsApi.md#list_institutions) | **GET** /institutions | List institutions
[**read_institution**](InstitutionsApi.md#read_institution) | **GET** /institutions/{institution_code} | Read institution


# **list_favorite_institutions**
> InstitutionsResponseBody list_favorite_institutions(iso_country_code=iso_country_code, page=page, records_per_page=records_per_page)

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
    api_instance = mx_platform_python.InstitutionsApi(api_client)
    iso_country_code = ['[\"US\",\"CA\"]'] # List[str] | An array of strings that filters institutions in the widget by the specified country code. Acceptable codes include `US`, `CA`, and `MX` (Mexico). (optional)
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `100`. If the value exceeds `100`, the default value of `25` will be used instead. (optional)

    try:
        # List favorite institutions
        api_response = api_instance.list_favorite_institutions(iso_country_code=iso_country_code, page=page, records_per_page=records_per_page)
        print("The response of InstitutionsApi->list_favorite_institutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstitutionsApi->list_favorite_institutions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iso_country_code** | [**List[str]**](str.md)| An array of strings that filters institutions in the widget by the specified country code. Acceptable codes include &#x60;US&#x60;, &#x60;CA&#x60;, and &#x60;MX&#x60; (Mexico). | [optional] 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;100&#x60;. If the value exceeds &#x60;100&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

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

# **list_institution_credentials**
> CredentialsResponseBody list_institution_credentials(institution_code, page=page, records_per_page=records_per_page)

List institution credentials

Use this endpoint to see which credentials will be needed to create a member for a specific institution.  Passing an invalid `institution_code` returns a `404`. 

### Example

* Basic Authentication (basicAuth):
```python
import time
import os
import mx_platform_python
from mx_platform_python.models.credentials_response_body import CredentialsResponseBody
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
    api_instance = mx_platform_python.InstitutionsApi(api_client)
    institution_code = 'mxbank' # str | The institution_code of the institution.
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `1000`. If the value exceeds `1000`, the default value of `25` will be used instead. (optional)

    try:
        # List institution credentials
        api_response = api_instance.list_institution_credentials(institution_code, page=page, records_per_page=records_per_page)
        print("The response of InstitutionsApi->list_institution_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstitutionsApi->list_institution_credentials: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **institution_code** | **str**| The institution_code of the institution. | 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;1000&#x60;. If the value exceeds &#x60;1000&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 

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
> InstitutionsResponseBody list_institutions(name=name, iso_country_code=iso_country_code, page=page, records_per_page=records_per_page, supports_account_identification=supports_account_identification, supports_account_statement=supports_account_statement, supports_account_verification=supports_account_verification, supports_transaction_history=supports_transaction_history)

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
    api_instance = mx_platform_python.InstitutionsApi(api_client)
    name = 'mxbank' # str | This will list only institutions in which the appended string appears. (optional)
    iso_country_code = ['[\"US\",\"CA\"]'] # List[str] | An array of strings that filters institutions in the widget by the specified country code. Acceptable codes include `US`, `CA`, and `MX` (Mexico). (optional)
    page = 1 # int | Results are paginated. Specify current page. (optional)
    records_per_page = 10 # int | This specifies the number of records to be returned on each page. Defaults to `25`. The valid range is from `10` to `100`. If the value exceeds `100`, the default value of `25` will be used instead. (optional)
    supports_account_identification = true # bool | Filter only institutions which support account identification. (optional)
    supports_account_statement = true # bool | Filter only institutions which support account statements. (optional)
    supports_account_verification = true # bool | Filter only institutions which support account verification. (optional)
    supports_transaction_history = true # bool | Filter only institutions which support extended transaction history. (optional)

    try:
        # List institutions
        api_response = api_instance.list_institutions(name=name, iso_country_code=iso_country_code, page=page, records_per_page=records_per_page, supports_account_identification=supports_account_identification, supports_account_statement=supports_account_statement, supports_account_verification=supports_account_verification, supports_transaction_history=supports_transaction_history)
        print("The response of InstitutionsApi->list_institutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstitutionsApi->list_institutions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| This will list only institutions in which the appended string appears. | [optional] 
 **iso_country_code** | [**List[str]**](str.md)| An array of strings that filters institutions in the widget by the specified country code. Acceptable codes include &#x60;US&#x60;, &#x60;CA&#x60;, and &#x60;MX&#x60; (Mexico). | [optional] 
 **page** | **int**| Results are paginated. Specify current page. | [optional] 
 **records_per_page** | **int**| This specifies the number of records to be returned on each page. Defaults to &#x60;25&#x60;. The valid range is from &#x60;10&#x60; to &#x60;100&#x60;. If the value exceeds &#x60;100&#x60;, the default value of &#x60;25&#x60; will be used instead. | [optional] 
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
    api_instance = mx_platform_python.InstitutionsApi(api_client)
    institution_code = 'mxbank' # str | The institution_code of the institution.

    try:
        # Read institution
        api_response = api_instance.read_institution(institution_code)
        print("The response of InstitutionsApi->read_institution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstitutionsApi->read_institution: %s\n" % e)
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

