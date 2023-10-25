# SpendingPlanIterationItemResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actual_amount** | **float** |  | [optional] 
**category_guid** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**item_type** | **str** |  | [optional] 
**planned_amount** | **float** |  | [optional] 
**scheduled_payment_guid** | **str** |  | [optional] 
**spending_plan_iteration_guid** | **str** |  | [optional] 
**top_level_category_guid** | **str** |  | [optional] 
**transaction_guids** | **List[str]** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.spending_plan_iteration_item_response import SpendingPlanIterationItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SpendingPlanIterationItemResponse from a JSON string
spending_plan_iteration_item_response_instance = SpendingPlanIterationItemResponse.from_json(json)
# print the JSON string representation of the object
print SpendingPlanIterationItemResponse.to_json()

# convert the object into a dict
spending_plan_iteration_item_response_dict = spending_plan_iteration_item_response_instance.to_dict()
# create an instance of SpendingPlanIterationItemResponse from a dict
spending_plan_iteration_item_response_form_dict = spending_plan_iteration_item_response.from_dict(spending_plan_iteration_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


