# InvestmentHoldingResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investment_holding** | [**InvestmentHoldingResponse**](InvestmentHoldingResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.investment_holding_response_body import InvestmentHoldingResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of InvestmentHoldingResponseBody from a JSON string
investment_holding_response_body_instance = InvestmentHoldingResponseBody.from_json(json)
# print the JSON string representation of the object
print InvestmentHoldingResponseBody.to_json()

# convert the object into a dict
investment_holding_response_body_dict = investment_holding_response_body_instance.to_dict()
# create an instance of InvestmentHoldingResponseBody from a dict
investment_holding_response_body_form_dict = investment_holding_response_body.from_dict(investment_holding_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


