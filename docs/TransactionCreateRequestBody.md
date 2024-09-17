# TransactionCreateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**TransactionCreateRequest**](TransactionCreateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.transaction_create_request_body import TransactionCreateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCreateRequestBody from a JSON string
transaction_create_request_body_instance = TransactionCreateRequestBody.from_json(json)
# print the JSON string representation of the object
print TransactionCreateRequestBody.to_json()

# convert the object into a dict
transaction_create_request_body_dict = transaction_create_request_body_instance.to_dict()
# create an instance of TransactionCreateRequestBody from a dict
transaction_create_request_body_form_dict = transaction_create_request_body.from_dict(transaction_create_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


