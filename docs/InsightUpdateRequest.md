# InsightUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_been_displayed** | **bool** |  | [optional] 
**is_dismissed** | **bool** |  | [optional] 

## Example

```python
from mx_platform_python.models.insight_update_request import InsightUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InsightUpdateRequest from a JSON string
insight_update_request_instance = InsightUpdateRequest.from_json(json)
# print the JSON string representation of the object
print InsightUpdateRequest.to_json()

# convert the object into a dict
insight_update_request_dict = insight_update_request_instance.to_dict()
# create an instance of InsightUpdateRequest from a dict
insight_update_request_form_dict = insight_update_request.from_dict(insight_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


