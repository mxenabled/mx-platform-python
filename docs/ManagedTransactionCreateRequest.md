# ManagedTransactionCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | 
**category** | **str** |  | [optional] 
**check_number_string** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**description** | **str** |  | 
**id** | **str** |  | [optional] 
**is_international** | **bool** |  | [optional] 
**latitude** | **float** |  | [optional] 
**localized_description** | **str** |  | [optional] 
**localized_memo** | **str** |  | [optional] 
**longitude** | **float** |  | [optional] 
**memo** | **str** |  | [optional] 
**merchant_category_code** | **int** |  | [optional] 
**merchant_guid** | **str** |  | [optional] 
**merchant_location_guid** | **str** |  | [optional] 
**metadata** | **str** |  | [optional] 
**posted_at** | **str** |  | [optional] 
**status** | **str** |  | 
**transacted_at** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from mx_platform_python.models.managed_transaction_create_request import ManagedTransactionCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedTransactionCreateRequest from a JSON string
managed_transaction_create_request_instance = ManagedTransactionCreateRequest.from_json(json)
# print the JSON string representation of the object
print ManagedTransactionCreateRequest.to_json()

# convert the object into a dict
managed_transaction_create_request_dict = managed_transaction_create_request_instance.to_dict()
# create an instance of ManagedTransactionCreateRequest from a dict
managed_transaction_create_request_form_dict = managed_transaction_create_request.from_dict(managed_transaction_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


