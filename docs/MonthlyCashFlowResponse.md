# MonthlyCashFlowResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | Unique identifier for the monthly cash flow profile. Defined by MX. | [optional] 
**user_guid** | **str** | Unique identifier for the user the monthly cash flow profile is attached to. Defined by MX. | [optional] 
**budgeted_income** | **float** | The amount of the budgeted income for the user. | [optional] 
**budgeted_expenses** | **float** | The amount of the budgeted expenses for the user. | [optional] 
**goals_contribution** | **float** | The monthly dollar amount allocated for goals. | [optional] 
**estimated_goals_contribution** | **int** | The estimated monthly dollar amount allocated for goals calculated from income and budgets. | [optional] 
**uses_estimated_goals_contribution** | **bool** |  | [optional] 

## Example

```python
from mx_platform_python.models.monthly_cash_flow_response import MonthlyCashFlowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MonthlyCashFlowResponse from a JSON string
monthly_cash_flow_response_instance = MonthlyCashFlowResponse.from_json(json)
# print the JSON string representation of the object
print MonthlyCashFlowResponse.to_json()

# convert the object into a dict
monthly_cash_flow_response_dict = monthly_cash_flow_response_instance.to_dict()
# create an instance of MonthlyCashFlowResponse from a dict
monthly_cash_flow_response_form_dict = monthly_cash_flow_response.from_dict(monthly_cash_flow_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


