# GoalRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** | Unique identifier of the account for the goal. | 
**amount** | **float** | Amount of the goal. | 
**goal_type_name** | **str** | The goal type. | 
**meta_type_name** | **str** | The category of the goal. | 
**name** | **str** | The name of the goal. | 
**completed_at** | **str** | Date and time the goal was completed. | [optional] 
**has_been_spent** | **bool** | Determines if the goal has been spent. | [optional] 
**is_complete** | **bool** | Determines if the goal is complete. | [optional] 
**metadata** | **str** | Additional information a partner can store on the goal. | [optional] 
**position** | **int** | The priority of the goal in relation to multiple goals. | [optional] 
**targeted_to_complete_at** | **str** | Date and time the goal is to complete. Intended for users to set their own goal completion dates. | [optional] 

## Example

```python
from mx_platform_python.models.goal_request import GoalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GoalRequest from a JSON string
goal_request_instance = GoalRequest.from_json(json)
# print the JSON string representation of the object
print GoalRequest.to_json()

# convert the object into a dict
goal_request_dict = goal_request_instance.to_dict()
# create an instance of GoalRequest from a dict
goal_request_form_dict = goal_request.from_dict(goal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


