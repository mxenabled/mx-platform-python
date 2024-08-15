# BudgetCreateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget** | [**BudgetCreateRequest**](BudgetCreateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.budget_create_request_body import BudgetCreateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetCreateRequestBody from a JSON string
budget_create_request_body_instance = BudgetCreateRequestBody.from_json(json)
# print the JSON string representation of the object
print BudgetCreateRequestBody.to_json()

# convert the object into a dict
budget_create_request_body_dict = budget_create_request_body_instance.to_dict()
# create an instance of BudgetCreateRequestBody from a dict
budget_create_request_body_form_dict = budget_create_request_body.from_dict(budget_create_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


