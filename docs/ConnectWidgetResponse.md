# ConnectWidgetResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connect_widget_url** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.connect_widget_response import ConnectWidgetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectWidgetResponse from a JSON string
connect_widget_response_instance = ConnectWidgetResponse.from_json(json)
# print the JSON string representation of the object
print ConnectWidgetResponse.to_json()

# convert the object into a dict
connect_widget_response_dict = connect_widget_response_instance.to_dict()
# create an instance of ConnectWidgetResponse from a dict
connect_widget_response_form_dict = connect_widget_response.from_dict(connect_widget_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


