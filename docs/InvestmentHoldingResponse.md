# InvestmentHoldingResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** |  | [optional] 
**cost_basis** | **float** |  | [optional] 
**coupon_yield** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**current_price** | **float** |  | [optional] 
**daily_change** | **float** |  | [optional] 
**description** | **str** |  | [optional] 
**expiration** | **str** |  | [optional] 
**face_value** | **float** |  | [optional] 
**frequency** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**market_value** | **float** |  | [optional] 
**maturity_date** | **str** |  | [optional] 
**percentage_change** | **float** |  | [optional] 
**purchase_price** | **float** |  | [optional] 
**quantity** | **str** |  | [optional] 
**rate** | **float** |  | [optional] 
**strike_price** | **float** |  | [optional] 
**symbol** | **str** |  | [optional] 
**term** | **str** |  | [optional] 
**today_ugl_amount** | **float** |  | [optional] 
**today_ugl_percentage** | **float** |  | [optional] 
**total_ugl_amount** | **float** |  | [optional] 
**total_ugl_percentage** | **float** |  | [optional] 
**unvested_quantity** | **float** |  | [optional] 
**unvested_value** | **float** |  | [optional] 
**user_guid** | **str** |  | [optional] 
**vested_quantity** | **float** |  | [optional] 
**vested_value** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
**current_price_as_of** | **str** |  | [optional] 
**issue_date** | **str** |  | [optional] 
**vesting_start_date** | **str** |  | [optional] 
**vesting_end_date** | **str** |  | [optional] 
**put_or_call** | **str** |  | [optional] 
**holding_type** | **str** |  | [optional] 
**term_unit** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.investment_holding_response import InvestmentHoldingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvestmentHoldingResponse from a JSON string
investment_holding_response_instance = InvestmentHoldingResponse.from_json(json)
# print the JSON string representation of the object
print InvestmentHoldingResponse.to_json()

# convert the object into a dict
investment_holding_response_dict = investment_holding_response_instance.to_dict()
# create an instance of InvestmentHoldingResponse from a dict
investment_holding_response_form_dict = investment_holding_response.from_dict(investment_holding_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


