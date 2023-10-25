# EnhanceTransactionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**categorized_by** | **int** |  | [optional] 
**category** | **str** |  | [optional] 
**category_guid** | **str** |  | [optional] 
**described_by** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**extended_transaction_type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_bill_pay** | **bool** |  | [optional] 
**is_direct_deposit** | **bool** |  | [optional] 
**is_expense** | **bool** |  | [optional] 
**is_fee** | **bool** |  | [optional] 
**is_income** | **bool** |  | [optional] 
**is_international** | **bool** |  | [optional] 
**is_overdraft_fee** | **bool** |  | [optional] 
**is_payroll_advance** | **bool** |  | [optional] 
**is_subscription** | **bool** |  | [optional] 
**memo** | **str** |  | [optional] 
**merchant_category_code** | **int** |  | [optional] 
**merchant_guid** | **str** |  | [optional] 
**merchant_location_guid** | **str** |  | [optional] 
**original_description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.enhance_transaction_response import EnhanceTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnhanceTransactionResponse from a JSON string
enhance_transaction_response_instance = EnhanceTransactionResponse.from_json(json)
# print the JSON string representation of the object
print EnhanceTransactionResponse.to_json()

# convert the object into a dict
enhance_transaction_response_dict = enhance_transaction_response_instance.to_dict()
# create an instance of EnhanceTransactionResponse from a dict
enhance_transaction_response_form_dict = enhance_transaction_response.from_dict(enhance_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


