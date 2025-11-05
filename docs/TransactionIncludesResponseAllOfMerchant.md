# TransactionIncludesResponseAllOfMerchant


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.transaction_includes_response_all_of_merchant import TransactionIncludesResponseAllOfMerchant

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionIncludesResponseAllOfMerchant from a JSON string
transaction_includes_response_all_of_merchant_instance = TransactionIncludesResponseAllOfMerchant.from_json(json)
# print the JSON string representation of the object
print TransactionIncludesResponseAllOfMerchant.to_json()

# convert the object into a dict
transaction_includes_response_all_of_merchant_dict = transaction_includes_response_all_of_merchant_instance.to_dict()
# create an instance of TransactionIncludesResponseAllOfMerchant from a dict
transaction_includes_response_all_of_merchant_form_dict = transaction_includes_response_all_of_merchant.from_dict(transaction_includes_response_all_of_merchant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


