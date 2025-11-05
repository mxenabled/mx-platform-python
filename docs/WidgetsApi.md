# mx_platform_python.WidgetsApi

All URIs are relative to *https://int-api.mx.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_connect_widget_url**](WidgetsApi.md#request_connect_widget_url) | **POST** /users/{user_guid}/connect_widget_url | (Deprecated) Request connect widget URL
[**request_o_auth_window_uri**](WidgetsApi.md#request_o_auth_window_uri) | **GET** /users/{user_guid}/members/{member_guid}/oauth_window_uri | Request oauth window uri
[**request_widget_url**](WidgetsApi.md#request_widget_url) | **POST** /users/{user_guid}/widget_urls | Request widget URL


# **request_connect_widget_url**
> ConnectWidgetResponseBody request_connect_widget_url(user_guid, connect_widget_request_body)

(Deprecated) Request connect widget URL

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
    api_instance = mx_platform_python.WidgetsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    connect_widget_request_body = mx_platform_python.ConnectWidgetRequestBody() # ConnectWidgetRequestBody | Optional config options for WebView (is_mobile_webview, current_institution_code, current_member_guid, update_credentials)

    try:
        # (Deprecated) Request connect widget URL
        api_response = api_instance.request_connect_widget_url(user_guid, connect_widget_request_body)
        print("The response of WidgetsApi->request_connect_widget_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetsApi->request_connect_widget_url: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
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
    api_instance = mx_platform_python.WidgetsApi(api_client)
    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b' # str | The unique id for a `member`.
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    client_redirect_url = 'https://{yoursite.com}' # str | A URL that MX will redirect to at the end of OAuth with additional query parameters. Only available with `referral_source=APP`. (optional)
    enable_app2app = 'false' # str | This indicates whether OAuth app2app behavior is enabled for institutions that support it. Defaults to `true`. When set to `false`, any `oauth_window_uri` generated will **not** direct the end user to the institution's mobile application. This setting is not persistent. This setting currently only affects Chase institutions. (optional)
    referral_source = 'APP' # str | Must be either `BROWSER` or `APP` depending on the implementation. Defaults to `BROWSER`. (optional)
    skip_aggregation = false # bool | Setting this parameter to `true` will prevent the member from automatically aggregating after being redirected from the authorization page. (optional)
    ui_message_webview_url_scheme = 'ui_message_webview_url_scheme_example' # str | A scheme for routing the user back to the application state they were previously in. Only available with `referral_source=APP`. (optional)

    try:
        # Request oauth window uri
        api_response = api_instance.request_o_auth_window_uri(member_guid, user_guid, client_redirect_url=client_redirect_url, enable_app2app=enable_app2app, referral_source=referral_source, skip_aggregation=skip_aggregation, ui_message_webview_url_scheme=ui_message_webview_url_scheme)
        print("The response of WidgetsApi->request_o_auth_window_uri:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetsApi->request_o_auth_window_uri: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_guid** | **str**| The unique id for a &#x60;member&#x60;. | 
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **client_redirect_url** | **str**| A URL that MX will redirect to at the end of OAuth with additional query parameters. Only available with &#x60;referral_source&#x3D;APP&#x60;. | [optional] 
 **enable_app2app** | **str**| This indicates whether OAuth app2app behavior is enabled for institutions that support it. Defaults to &#x60;true&#x60;. When set to &#x60;false&#x60;, any &#x60;oauth_window_uri&#x60; generated will **not** direct the end user to the institution&#39;s mobile application. This setting is not persistent. This setting currently only affects Chase institutions. | [optional] 
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
> WidgetResponseBody request_widget_url(user_guid, widget_request_body, accept_language=accept_language, x_callback_payload=x_callback_payload)

Request widget URL

Get an embeddable URL for integrating a widget into your website or app. The URL expires after ten minutes or upon first use, whichever occurs first. You'll need to obtain a new URL each time the page loads or reloads.  Include the `widget_type` in the request body to specify which widget you want to embed—the Connect Widget, a Personal Financial Management widget, or an Insights widget. Some request parameters are specific to certain widget types.  To embed the Connect Widget, set `widget_type` to `connect_widget`.  For a full list of available widget types, see [Widget Types](/api-reference/platform-api/reference/widgets#widget-types). 

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
    api_instance = mx_platform_python.WidgetsApi(api_client)
    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54' # str | The unique identifier for a `user`, beginning with the prefix `USR-`.
    widget_request_body = mx_platform_python.WidgetRequestBody() # WidgetRequestBody | The widget url configuration options.
    accept_language = 'en-US' # str | The desired language of the widget. (optional)
    x_callback_payload = '813e50bd-4a7e-4517-b6bb-9eef65a68cbd' # str | The base64 encoded string defined in this header will be returned in the [Member](/resources/webhooks/member/) and [Member Data Updated](/resources/webhooks/member#member-data-updated) webhooks. This allows you to trace user interactions and workflows initiated externally and internally in the MX Platform. Max 1024 characters. (optional)

    try:
        # Request widget URL
        api_response = api_instance.request_widget_url(user_guid, widget_request_body, accept_language=accept_language, x_callback_payload=x_callback_payload)
        print("The response of WidgetsApi->request_widget_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetsApi->request_widget_url: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_guid** | **str**| The unique identifier for a &#x60;user&#x60;, beginning with the prefix &#x60;USR-&#x60;. | 
 **widget_request_body** | [**WidgetRequestBody**](WidgetRequestBody.md)| The widget url configuration options. | 
 **accept_language** | **str**| The desired language of the widget. | [optional] 
 **x_callback_payload** | **str**| The base64 encoded string defined in this header will be returned in the [Member](/resources/webhooks/member/) and [Member Data Updated](/resources/webhooks/member#member-data-updated) webhooks. This allows you to trace user interactions and workflows initiated externally and internally in the MX Platform. Max 1024 characters. | [optional] 

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

