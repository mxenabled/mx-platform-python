# EnhanceTransactionsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**description** | **str** |  | 
**extended_transaction_type** | **str** |  | [optional] 
**id** | **str** |  | 
**memo** | **str** |  | [optional] 
**merchant_category_code** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.enhance_transactions_request import EnhanceTransactionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnhanceTransactionsRequest from a JSON string
enhance_transactions_request_instance = EnhanceTransactionsRequest.from_json(json)
# print the JSON string representation of the object
print EnhanceTransactionsRequest.to_json()

# convert the object into a dict
enhance_transactions_request_dict = enhance_transactions_request_instance.to_dict()
# create an instance of EnhanceTransactionsRequest from a dict
enhance_transactions_request_form_dict = enhance_transactions_request.from_dict(enhance_transactions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


