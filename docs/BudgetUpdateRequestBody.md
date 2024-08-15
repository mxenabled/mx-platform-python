# BudgetUpdateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget** | [**BudgetUpdateRequest**](BudgetUpdateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.budget_update_request_body import BudgetUpdateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetUpdateRequestBody from a JSON string
budget_update_request_body_instance = BudgetUpdateRequestBody.from_json(json)
# print the JSON string representation of the object
print BudgetUpdateRequestBody.to_json()

# convert the object into a dict
budget_update_request_body_dict = budget_update_request_body_instance.to_dict()
# create an instance of BudgetUpdateRequestBody from a dict
budget_update_request_body_form_dict = budget_update_request_body.from_dict(budget_update_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


