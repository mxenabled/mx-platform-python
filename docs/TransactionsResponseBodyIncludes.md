# TransactionsResponseBodyIncludes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[TransactionIncludesResponse]**](TransactionIncludesResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.transactions_response_body_includes import TransactionsResponseBodyIncludes

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionsResponseBodyIncludes from a JSON string
transactions_response_body_includes_instance = TransactionsResponseBodyIncludes.from_json(json)
# print the JSON string representation of the object
print TransactionsResponseBodyIncludes.to_json()

# convert the object into a dict
transactions_response_body_includes_dict = transactions_response_body_includes_instance.to_dict()
# create an instance of TransactionsResponseBodyIncludes from a dict
transactions_response_body_includes_form_dict = transactions_response_body_includes.from_dict(transactions_response_body_includes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


