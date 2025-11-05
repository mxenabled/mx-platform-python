# InsightUpdateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**insight** | [**InsightUpdateRequest**](InsightUpdateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.insight_update_request_body import InsightUpdateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of InsightUpdateRequestBody from a JSON string
insight_update_request_body_instance = InsightUpdateRequestBody.from_json(json)
# print the JSON string representation of the object
print InsightUpdateRequestBody.to_json()

# convert the object into a dict
insight_update_request_body_dict = insight_update_request_body_instance.to_dict()
# create an instance of InsightUpdateRequestBody from a dict
insight_update_request_body_form_dict = insight_update_request_body.from_dict(insight_update_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


