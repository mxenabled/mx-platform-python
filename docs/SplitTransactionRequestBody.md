# SplitTransactionRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**SplitTransactionRequest**](SplitTransactionRequest.md) |  | 

## Example

```python
from mx_platform_python.models.split_transaction_request_body import SplitTransactionRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of SplitTransactionRequestBody from a JSON string
split_transaction_request_body_instance = SplitTransactionRequestBody.from_json(json)
# print the JSON string representation of the object
print SplitTransactionRequestBody.to_json()

# convert the object into a dict
split_transaction_request_body_dict = split_transaction_request_body_instance.to_dict()
# create an instance of SplitTransactionRequestBody from a dict
split_transaction_request_body_form_dict = split_transaction_request_body.from_dict(split_transaction_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


