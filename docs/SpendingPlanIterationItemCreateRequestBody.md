# SpendingPlanIterationItemCreateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_guid** | **str** |  | [optional] 
**item_type** | **float** |  | [optional] 
**planned_amount** | **float** |  | 
**scheduled_payment_guid** | **str** |  | [optional] 
**top_level_category_guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.spending_plan_iteration_item_create_request_body import SpendingPlanIterationItemCreateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of SpendingPlanIterationItemCreateRequestBody from a JSON string
spending_plan_iteration_item_create_request_body_instance = SpendingPlanIterationItemCreateRequestBody.from_json(json)
# print the JSON string representation of the object
print SpendingPlanIterationItemCreateRequestBody.to_json()

# convert the object into a dict
spending_plan_iteration_item_create_request_body_dict = spending_plan_iteration_item_create_request_body_instance.to_dict()
# create an instance of SpendingPlanIterationItemCreateRequestBody from a dict
spending_plan_iteration_item_create_request_body_form_dict = spending_plan_iteration_item_create_request_body.from_dict(spending_plan_iteration_item_create_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


