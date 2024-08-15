# GoalsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** | Unique identifier of the account for the goal. | [optional] 
**amount** | **float** | Amount of the goal. | [optional] 
**current_amount** | **float** | The current amount of the goal. | [optional] 
**guid** | **str** | The unique identifier for the goal. Defined by MX. | [optional] 
**goal_type_name** | **str** | The goal type. | [optional] 
**meta_type_name** | **str** | The category of the goal. | [optional] 
**name** | **str** | The name of the goal. | [optional] 
**completed_at** | **str** | Date and time the goal was completed. | [optional] 
**has_been_spent** | **bool** | Determines if the goal has been spent. | [optional] 
**is_complete** | **bool** | Determines if the goal is complete. | [optional] 
**metadata** | **str** | Additional information a partner can store on the goal. | [optional] 
**position** | **int** | The priority of the goal in relation to multiple goals. | [optional] 
**projected_to_complete_at** | **str** | The date on which the project was completed. | [optional] 
**targeted_to_complete_at** | **str** |  | [optional] 
**track_type_name** | **str** |  | [optional] 
**user_guid** | **str** | The unique identifier for the the user. Defined by MX. | [optional] 

## Example

```python
from mx_platform_python.models.goals_response import GoalsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GoalsResponse from a JSON string
goals_response_instance = GoalsResponse.from_json(json)
# print the JSON string representation of the object
print GoalsResponse.to_json()

# convert the object into a dict
goals_response_dict = goals_response_instance.to_dict()
# create an instance of GoalsResponse from a dict
goals_response_form_dict = goals_response.from_dict(goals_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


