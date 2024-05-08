# InsightResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**insight** | [**List[InsightResponse]**](InsightResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.insight_response_body import InsightResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of InsightResponseBody from a JSON string
insight_response_body_instance = InsightResponseBody.from_json(json)
# print the JSON string representation of the object
print InsightResponseBody.to_json()

# convert the object into a dict
insight_response_body_dict = insight_response_body_instance.to_dict()
# create an instance of InsightResponseBody from a dict
insight_response_body_form_dict = insight_response_body.from_dict(insight_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


