# InvestmentHoldingsResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**investment_holdings** | [**List[InvestmentHoldingResponse]**](InvestmentHoldingResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.investment_holdings_response_body import InvestmentHoldingsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of InvestmentHoldingsResponseBody from a JSON string
investment_holdings_response_body_instance = InvestmentHoldingsResponseBody.from_json(json)
# print the JSON string representation of the object
print InvestmentHoldingsResponseBody.to_json()

# convert the object into a dict
investment_holdings_response_body_dict = investment_holdings_response_body_instance.to_dict()
# create an instance of InvestmentHoldingsResponseBody from a dict
investment_holdings_response_body_form_dict = investment_holdings_response_body.from_dict(investment_holdings_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


