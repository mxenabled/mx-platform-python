# WidgetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_redirect_url** | **str** |  | [optional] 
**color_scheme** | **str** |  | [optional] 
**current_institution_code** | **str** |  | [optional] 
**current_institution_guid** | **str** |  | [optional] 
**current_member_guid** | **str** |  | [optional] 
**disable_background_agg** | **bool** |  | [optional] 
**disable_institution_search** | **bool** |  | [optional] 
**include_identity** | **bool** |  | [optional] 
**include_transactions** | **bool** |  | [optional] 
**is_mobile_webview** | **bool** |  | [optional] 
**microwidget_instance_id** | **str** |  | [optional] 
**mode** | **str** |  | [optional] 
**oauth_referral_source** | **str** |  | [optional] 
**ui_message_version** | **int** |  | [optional] 
**ui_message_webview_url_scheme** | **str** |  | [optional] 
**update_credentials** | **bool** |  | [optional] 
**widget_type** | **str** |  | 

## Example

```python
from mx_platform_python.models.widget_request import WidgetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetRequest from a JSON string
widget_request_instance = WidgetRequest.from_json(json)
# print the JSON string representation of the object
print WidgetRequest.to_json()

# convert the object into a dict
widget_request_dict = widget_request_instance.to_dict()
# create an instance of WidgetRequest from a dict
widget_request_form_dict = widget_request.from_dict(widget_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


