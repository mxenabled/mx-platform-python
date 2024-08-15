# GoalResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goal** | [**GoalResponse**](GoalResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.goal_response_body import GoalResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of GoalResponseBody from a JSON string
goal_response_body_instance = GoalResponseBody.from_json(json)
# print the JSON string representation of the object
print GoalResponseBody.to_json()

# convert the object into a dict
goal_response_body_dict = goal_response_body_instance.to_dict()
# create an instance of GoalResponseBody from a dict
goal_response_body_form_dict = goal_response_body.from_dict(goal_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


