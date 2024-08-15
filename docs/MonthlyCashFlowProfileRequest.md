# MonthlyCashFlowProfileRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goals_contribution** | **float** | The monthly dollar amount allocated for goals. | [optional] 
**uses_estimated_goals_contribution** | **bool** | Determines if the user uses estimated goals contribution. | [optional] 

## Example

```python
from mx_platform_python.models.monthly_cash_flow_profile_request import MonthlyCashFlowProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MonthlyCashFlowProfileRequest from a JSON string
monthly_cash_flow_profile_request_instance = MonthlyCashFlowProfileRequest.from_json(json)
# print the JSON string representation of the object
print MonthlyCashFlowProfileRequest.to_json()

# convert the object into a dict
monthly_cash_flow_profile_request_dict = monthly_cash_flow_profile_request_instance.to_dict()
# create an instance of MonthlyCashFlowProfileRequest from a dict
monthly_cash_flow_profile_request_form_dict = monthly_cash_flow_profile_request.from_dict(monthly_cash_flow_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


