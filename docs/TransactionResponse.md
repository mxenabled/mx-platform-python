# TransactionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**category** | **str** |  | [optional] 
**category_guid** | **str** |  | [optional] 
**check_number_string** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**extended_transaction_type** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_bill_pay** | **bool** |  | [optional] 
**is_direct_deposit** | **bool** |  | [optional] 
**is_expense** | **bool** |  | [optional] 
**is_fee** | **bool** |  | [optional] 
**is_income** | **bool** |  | [optional] 
**is_international** | **bool** |  | [optional] 
**is_manual** | **bool** |  | [optional] 
**is_overdraft_fee** | **bool** |  | [optional] 
**is_payroll_advance** | **bool** |  | [optional] 
**is_recurring** | **bool** |  | [optional] 
**is_subscription** | **bool** |  | [optional] 
**latitude** | **float** |  | [optional] 
**localized_description** | **str** |  | [optional] 
**localized_memo** | **str** |  | [optional] 
**longitude** | **float** |  | [optional] 
**member_guid** | **str** |  | [optional] 
**member_is_managed_by_user** | **bool** |  | [optional] 
**memo** | **str** |  | [optional] 
**merchant_category_code** | **int** |  | [optional] 
**merchant_guid** | **str** |  | [optional] 
**merchant_location_guid** | **str** |  | [optional] 
**metadata** | **str** |  | [optional] 
**original_description** | **str** |  | [optional] 
**posted_at** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**top_level_category** | **str** |  | [optional] 
**transacted_at** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.transaction_response import TransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResponse from a JSON string
transaction_response_instance = TransactionResponse.from_json(json)
# print the JSON string representation of the object
print TransactionResponse.to_json()

# convert the object into a dict
transaction_response_dict = transaction_response_instance.to_dict()
# create an instance of TransactionResponse from a dict
transaction_response_form_dict = transaction_response.from_dict(transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


