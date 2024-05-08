# InsightsResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**insights** | [**List[InsightResponse]**](InsightResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.insights_response_body import InsightsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of InsightsResponseBody from a JSON string
insights_response_body_instance = InsightsResponseBody.from_json(json)
# print the JSON string representation of the object
print InsightsResponseBody.to_json()

# convert the object into a dict
insights_response_body_dict = insights_response_body_instance.to_dict()
# create an instance of InsightsResponseBody from a dict
insights_response_body_form_dict = insights_response_body.from_dict(insights_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


