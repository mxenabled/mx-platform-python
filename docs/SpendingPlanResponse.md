# SpendingPlanResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**current_iteration_number** | **int** |  | [optional] 
**guid** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.spending_plan_response import SpendingPlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SpendingPlanResponse from a JSON string
spending_plan_response_instance = SpendingPlanResponse.from_json(json)
# print the JSON string representation of the object
print SpendingPlanResponse.to_json()

# convert the object into a dict
spending_plan_response_dict = spending_plan_response_instance.to_dict()
# create an instance of SpendingPlanResponse from a dict
spending_plan_response_form_dict = spending_plan_response.from_dict(spending_plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


