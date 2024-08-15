# UpdateGoalRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** | Unique identifier of the account for the goal. | [optional] 
**amount** | **float** | Amount of the goal. | [optional] 
**goal_type_name** | **str** | The goal type. | [optional] 
**meta_type_name** | **str** | The category of the goal. | [optional] 
**name** | **str** | The name of the goal. | [optional] 
**completed_at** | **str** | Date and time the goal was completed. | [optional] 
**has_been_spent** | **bool** | Determines if the goal has been spent. | [optional] 
**is_complete** | **bool** | Determines if the goal is complete. | [optional] 
**metadata** | **str** | Additional information a partner can store on the goal. | [optional] 
**position** | **int** | The priority of the goal in relation to multiple goals. | [optional] 
**targeted_to_complete_at** | **str** | Date and time the goal is to complete. Intended for users to set their own goal completion dates. | [optional] 

## Example

```python
from mx_platform_python.models.update_goal_request import UpdateGoalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGoalRequest from a JSON string
update_goal_request_instance = UpdateGoalRequest.from_json(json)
# print the JSON string representation of the object
print UpdateGoalRequest.to_json()

# convert the object into a dict
update_goal_request_dict = update_goal_request_instance.to_dict()
# create an instance of UpdateGoalRequest from a dict
update_goal_request_form_dict = update_goal_request.from_dict(update_goal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


