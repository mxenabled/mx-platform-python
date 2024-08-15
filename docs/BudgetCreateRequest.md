# BudgetCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_guid** | **str** | Unique identifier of the category. | 
**parent_guid** | **str** | Unique identifier of the parent budget. This is only required when creating a budget on a sub-category. | 
**amount** | **int** | Amount of the budget. | [optional] 
**metadata** | **str** | Additional information a partner can store on the budget. | [optional] 
**skip_webhook** | **bool** | When set to true, this parameter will prevent a webhook from being triggered by the request. | [optional] 

## Example

```python
from mx_platform_python.models.budget_create_request import BudgetCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetCreateRequest from a JSON string
budget_create_request_instance = BudgetCreateRequest.from_json(json)
# print the JSON string representation of the object
print BudgetCreateRequest.to_json()

# convert the object into a dict
budget_create_request_dict = budget_create_request_instance.to_dict()
# create an instance of BudgetCreateRequest from a dict
budget_create_request_form_dict = budget_create_request.from_dict(budget_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


