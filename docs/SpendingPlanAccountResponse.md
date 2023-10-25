# SpendingPlanAccountResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** |  | [optional] 
**client_guid** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**spending_plan_guid** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.spending_plan_account_response import SpendingPlanAccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SpendingPlanAccountResponse from a JSON string
spending_plan_account_response_instance = SpendingPlanAccountResponse.from_json(json)
# print the JSON string representation of the object
print SpendingPlanAccountResponse.to_json()

# convert the object into a dict
spending_plan_account_response_dict = spending_plan_account_response_instance.to_dict()
# create an instance of SpendingPlanAccountResponse from a dict
spending_plan_account_response_form_dict = spending_plan_account_response.from_dict(spending_plan_account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


