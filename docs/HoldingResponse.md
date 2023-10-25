# HoldingResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** |  | [optional] 
**cost_basis** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**cusip** | **str** |  | [optional] 
**daily_change** | **float** |  | [optional] 
**description** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**holding_type** | **str** |  | [optional] 
**holding_type_id** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**market_value** | **float** |  | [optional] 
**member_guid** | **str** |  | [optional] 
**metadata** | **str** |  | [optional] 
**purchase_price** | **float** |  | [optional] 
**shares** | **float** |  | [optional] 
**symbol** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.holding_response import HoldingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HoldingResponse from a JSON string
holding_response_instance = HoldingResponse.from_json(json)
# print the JSON string representation of the object
print HoldingResponse.to_json()

# convert the object into a dict
holding_response_dict = holding_response_instance.to_dict()
# create an instance of HoldingResponse from a dict
holding_response_form_dict = holding_response.from_dict(holding_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


