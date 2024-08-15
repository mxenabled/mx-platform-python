# SplitTransactionsResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[TransactionResponse]**](TransactionResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.split_transactions_response_body import SplitTransactionsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of SplitTransactionsResponseBody from a JSON string
split_transactions_response_body_instance = SplitTransactionsResponseBody.from_json(json)
# print the JSON string representation of the object
print SplitTransactionsResponseBody.to_json()

# convert the object into a dict
split_transactions_response_body_dict = split_transactions_response_body_instance.to_dict()
# create an instance of SplitTransactionsResponseBody from a dict
split_transactions_response_body_form_dict = split_transactions_response_body.from_dict(split_transactions_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


