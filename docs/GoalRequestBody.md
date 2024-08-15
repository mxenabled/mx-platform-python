# GoalRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goal** | [**GoalRequest**](GoalRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.goal_request_body import GoalRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of GoalRequestBody from a JSON string
goal_request_body_instance = GoalRequestBody.from_json(json)
# print the JSON string representation of the object
print GoalRequestBody.to_json()

# convert the object into a dict
goal_request_body_dict = goal_request_body_instance.to_dict()
# create an instance of GoalRequestBody from a dict
goal_request_body_form_dict = goal_request_body.from_dict(goal_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


