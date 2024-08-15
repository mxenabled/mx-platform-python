# UpdateGoalRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goal** | [**UpdateGoalRequest**](UpdateGoalRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.update_goal_request_body import UpdateGoalRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGoalRequestBody from a JSON string
update_goal_request_body_instance = UpdateGoalRequestBody.from_json(json)
# print the JSON string representation of the object
print UpdateGoalRequestBody.to_json()

# convert the object into a dict
update_goal_request_body_dict = update_goal_request_body_instance.to_dict()
# create an instance of UpdateGoalRequestBody from a dict
update_goal_request_body_form_dict = update_goal_request_body.from_dict(update_goal_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


