# SpendingPlanAccountsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spending_plan_accounts** | [**List[SpendingPlanAccountResponse]**](SpendingPlanAccountResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.spending_plan_accounts_response import SpendingPlanAccountsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SpendingPlanAccountsResponse from a JSON string
spending_plan_accounts_response_instance = SpendingPlanAccountsResponse.from_json(json)
# print the JSON string representation of the object
print SpendingPlanAccountsResponse.to_json()

# convert the object into a dict
spending_plan_accounts_response_dict = spending_plan_accounts_response_instance.to_dict()
# create an instance of SpendingPlanAccountsResponse from a dict
spending_plan_accounts_response_form_dict = spending_plan_accounts_response.from_dict(spending_plan_accounts_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


