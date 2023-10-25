# EnhanceTransactionsResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[EnhanceTransactionResponse]**](EnhanceTransactionResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.enhance_transactions_response_body import EnhanceTransactionsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of EnhanceTransactionsResponseBody from a JSON string
enhance_transactions_response_body_instance = EnhanceTransactionsResponseBody.from_json(json)
# print the JSON string representation of the object
print EnhanceTransactionsResponseBody.to_json()

# convert the object into a dict
enhance_transactions_response_body_dict = enhance_transactions_response_body_instance.to_dict()
# create an instance of EnhanceTransactionsResponseBody from a dict
enhance_transactions_response_body_form_dict = enhance_transactions_response_body.from_dict(enhance_transactions_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


