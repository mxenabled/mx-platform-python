# WidgetRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**widget_url** | [**WidgetRequest**](WidgetRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.widget_request_body import WidgetRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetRequestBody from a JSON string
widget_request_body_instance = WidgetRequestBody.from_json(json)
# print the JSON string representation of the object
print WidgetRequestBody.to_json()

# convert the object into a dict
widget_request_body_dict = widget_request_body_instance.to_dict()
# create an instance of WidgetRequestBody from a dict
widget_request_body_form_dict = widget_request_body.from_dict(widget_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


