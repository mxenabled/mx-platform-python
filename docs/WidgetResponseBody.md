# WidgetResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**widget_url** | [**WidgetResponse**](WidgetResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.widget_response_body import WidgetResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetResponseBody from a JSON string
widget_response_body_instance = WidgetResponseBody.from_json(json)
# print the JSON string representation of the object
print WidgetResponseBody.to_json()

# convert the object into a dict
widget_response_body_dict = widget_response_body_instance.to_dict()
# create an instance of WidgetResponseBody from a dict
widget_response_body_form_dict = widget_response_body.from_dict(widget_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


