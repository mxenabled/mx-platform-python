# GoalsResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goals** | [**List[GoalsResponse]**](GoalsResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.goals_response_body import GoalsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of GoalsResponseBody from a JSON string
goals_response_body_instance = GoalsResponseBody.from_json(json)
# print the JSON string representation of the object
print GoalsResponseBody.to_json()

# convert the object into a dict
goals_response_body_dict = goals_response_body_instance.to_dict()
# create an instance of GoalsResponseBody from a dict
goals_response_body_form_dict = goals_response_body.from_dict(goals_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


