# BudgetResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget** | [**BudgetResponse**](BudgetResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.budget_response_body import BudgetResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetResponseBody from a JSON string
budget_response_body_instance = BudgetResponseBody.from_json(json)
# print the JSON string representation of the object
print BudgetResponseBody.to_json()

# convert the object into a dict
budget_response_body_dict = budget_response_body_instance.to_dict()
# create an instance of BudgetResponseBody from a dict
budget_response_body_form_dict = budget_response_body.from_dict(budget_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


