# MonthlyCashFlowProfileRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution** | [**MonthlyCashFlowProfileRequest**](MonthlyCashFlowProfileRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.monthly_cash_flow_profile_request_body import MonthlyCashFlowProfileRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of MonthlyCashFlowProfileRequestBody from a JSON string
monthly_cash_flow_profile_request_body_instance = MonthlyCashFlowProfileRequestBody.from_json(json)
# print the JSON string representation of the object
print MonthlyCashFlowProfileRequestBody.to_json()

# convert the object into a dict
monthly_cash_flow_profile_request_body_dict = monthly_cash_flow_profile_request_body_instance.to_dict()
# create an instance of MonthlyCashFlowProfileRequestBody from a dict
monthly_cash_flow_profile_request_body_form_dict = monthly_cash_flow_profile_request_body.from_dict(monthly_cash_flow_profile_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


