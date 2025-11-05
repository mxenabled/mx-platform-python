# TransactionIncludesResponseAllOfRepeatingTransaction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repeating_transaction_type** | **str** |  | [optional] 
**recurrence_type** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.transaction_includes_response_all_of_repeating_transaction import TransactionIncludesResponseAllOfRepeatingTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionIncludesResponseAllOfRepeatingTransaction from a JSON string
transaction_includes_response_all_of_repeating_transaction_instance = TransactionIncludesResponseAllOfRepeatingTransaction.from_json(json)
# print the JSON string representation of the object
print TransactionIncludesResponseAllOfRepeatingTransaction.to_json()

# convert the object into a dict
transaction_includes_response_all_of_repeating_transaction_dict = transaction_includes_response_all_of_repeating_transaction_instance.to_dict()
# create an instance of TransactionIncludesResponseAllOfRepeatingTransaction from a dict
transaction_includes_response_all_of_repeating_transaction_form_dict = transaction_includes_response_all_of_repeating_transaction.from_dict(transaction_includes_response_all_of_repeating_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


