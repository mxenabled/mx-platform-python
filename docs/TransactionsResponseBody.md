# TransactionsResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[TransactionResponse]**](TransactionResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.transactions_response_body import TransactionsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionsResponseBody from a JSON string
transactions_response_body_instance = TransactionsResponseBody.from_json(json)
# print the JSON string representation of the object
print TransactionsResponseBody.to_json()

# convert the object into a dict
transactions_response_body_dict = transactions_response_body_instance.to_dict()
# create an instance of TransactionsResponseBody from a dict
transactions_response_body_form_dict = transactions_response_body.from_dict(transactions_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


