# ManagedTransactionUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**check_number_string** | **str** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
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
**status** | **str** |  | [optional] 
**transacted_at** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.managed_transaction_update_request import ManagedTransactionUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedTransactionUpdateRequest from a JSON string
managed_transaction_update_request_instance = ManagedTransactionUpdateRequest.from_json(json)
# print the JSON string representation of the object
print ManagedTransactionUpdateRequest.to_json()

# convert the object into a dict
managed_transaction_update_request_dict = managed_transaction_update_request_instance.to_dict()
# create an instance of ManagedTransactionUpdateRequest from a dict
managed_transaction_update_request_form_dict = managed_transaction_update_request.from_dict(managed_transaction_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


