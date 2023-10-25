# TransactionResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**TransactionResponse**](TransactionResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.transaction_response_body import TransactionResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionResponseBody from a JSON string
transaction_response_body_instance = TransactionResponseBody.from_json(json)
# print the JSON string representation of the object
print TransactionResponseBody.to_json()

# convert the object into a dict
transaction_response_body_dict = transaction_response_body_instance.to_dict()
# create an instance of TransactionResponseBody from a dict
transaction_response_body_form_dict = transaction_response_body.from_dict(transaction_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


