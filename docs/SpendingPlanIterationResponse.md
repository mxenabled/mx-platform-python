# SpendingPlanIterationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**end_on** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**iteration_number** | **int** |  | [optional] 
**spending_plan_guid** | **str** |  | [optional] 
**start_on** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.spending_plan_iteration_response import SpendingPlanIterationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SpendingPlanIterationResponse from a JSON string
spending_plan_iteration_response_instance = SpendingPlanIterationResponse.from_json(json)
# print the JSON string representation of the object
print SpendingPlanIterationResponse.to_json()

# convert the object into a dict
spending_plan_iteration_response_dict = spending_plan_iteration_response_instance.to_dict()
# create an instance of SpendingPlanIterationResponse from a dict
spending_plan_iteration_response_form_dict = spending_plan_iteration_response.from_dict(spending_plan_iteration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


