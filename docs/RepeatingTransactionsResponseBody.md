# RepeatingTransactionsResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repeating_transactions** | [**List[RepeatingTransactionResponse]**](RepeatingTransactionResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.repeating_transactions_response_body import RepeatingTransactionsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of RepeatingTransactionsResponseBody from a JSON string
repeating_transactions_response_body_instance = RepeatingTransactionsResponseBody.from_json(json)
# print the JSON string representation of the object
print RepeatingTransactionsResponseBody.to_json()

# convert the object into a dict
repeating_transactions_response_body_dict = repeating_transactions_response_body_instance.to_dict()
# create an instance of RepeatingTransactionsResponseBody from a dict
repeating_transactions_response_body_form_dict = repeating_transactions_response_body.from_dict(repeating_transactions_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


