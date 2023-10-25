# ConnectWidgetResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**ConnectWidgetResponse**](ConnectWidgetResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.connect_widget_response_body import ConnectWidgetResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectWidgetResponseBody from a JSON string
connect_widget_response_body_instance = ConnectWidgetResponseBody.from_json(json)
# print the JSON string representation of the object
print ConnectWidgetResponseBody.to_json()

# convert the object into a dict
connect_widget_response_body_dict = connect_widget_response_body_instance.to_dict()
# create an instance of ConnectWidgetResponseBody from a dict
connect_widget_response_body_form_dict = connect_widget_response_body.from_dict(connect_widget_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


