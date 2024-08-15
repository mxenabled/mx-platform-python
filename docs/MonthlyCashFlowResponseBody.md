# MonthlyCashFlowResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monthly_cash_flow_profile** | [**MonthlyCashFlowResponse**](MonthlyCashFlowResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.monthly_cash_flow_response_body import MonthlyCashFlowResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of MonthlyCashFlowResponseBody from a JSON string
monthly_cash_flow_response_body_instance = MonthlyCashFlowResponseBody.from_json(json)
# print the JSON string representation of the object
print MonthlyCashFlowResponseBody.to_json()

# convert the object into a dict
monthly_cash_flow_response_body_dict = monthly_cash_flow_response_body_instance.to_dict()
# create an instance of MonthlyCashFlowResponseBody from a dict
monthly_cash_flow_response_body_form_dict = monthly_cash_flow_response_body.from_dict(monthly_cash_flow_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


