# MemberCreateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_redirect_url** | **str** |  | [optional] 
**enable_app2app** | **bool** | This indicates whether OAuth app2app behavior is enabled for institutions that support it. Defaults to &#x60;true&#x60;. When set to &#x60;false&#x60;, any &#x60;oauth_window_uri&#x60; generated will **not** direct the end user to the institution&#39;s mobile application. This setting is not persistent. This setting currently only affects Chase institutions.  | [optional] 
**member** | [**MemberCreateRequest**](MemberCreateRequest.md) |  | [optional] 
**referral_source** | **str** |  | [optional] 
**ui_message_webview_url_scheme** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.member_create_request_body import MemberCreateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of MemberCreateRequestBody from a JSON string
member_create_request_body_instance = MemberCreateRequestBody.from_json(json)
# print the JSON string representation of the object
print MemberCreateRequestBody.to_json()

# convert the object into a dict
member_create_request_body_dict = member_create_request_body_instance.to_dict()
# create an instance of MemberCreateRequestBody from a dict
member_create_request_body_form_dict = member_create_request_body.from_dict(member_create_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


