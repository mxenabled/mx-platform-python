# BudgetUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Amount of the budget. | [optional] 
**metadata** | **str** | Additional information a partner can store on the budget. | [optional] 
**skip_webhook** | **bool** | When set to true, this parameter will prevent a webhook from being triggered by the request. | [optional] 

## Example

```python
from mx_platform_python.models.budget_update_request import BudgetUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetUpdateRequest from a JSON string
budget_update_request_instance = BudgetUpdateRequest.from_json(json)
# print the JSON string representation of the object
print BudgetUpdateRequest.to_json()

# convert the object into a dict
budget_update_request_dict = budget_update_request_instance.to_dict()
# create an instance of BudgetUpdateRequest from a dict
budget_update_request_form_dict = budget_update_request.from_dict(budget_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


