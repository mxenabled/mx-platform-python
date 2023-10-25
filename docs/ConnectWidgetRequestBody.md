# ConnectWidgetRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**ConnectWidgetRequest**](ConnectWidgetRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.connect_widget_request_body import ConnectWidgetRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectWidgetRequestBody from a JSON string
connect_widget_request_body_instance = ConnectWidgetRequestBody.from_json(json)
# print the JSON string representation of the object
print ConnectWidgetRequestBody.to_json()

# convert the object into a dict
connect_widget_request_body_dict = connect_widget_request_body_instance.to_dict()
# create an instance of ConnectWidgetRequestBody from a dict
connect_widget_request_body_form_dict = connect_widget_request_body.from_dict(connect_widget_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


