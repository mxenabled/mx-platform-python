# ManagedTransactionCreateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**ManagedTransactionCreateRequest**](ManagedTransactionCreateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.managed_transaction_create_request_body import ManagedTransactionCreateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedTransactionCreateRequestBody from a JSON string
managed_transaction_create_request_body_instance = ManagedTransactionCreateRequestBody.from_json(json)
# print the JSON string representation of the object
print ManagedTransactionCreateRequestBody.to_json()

# convert the object into a dict
managed_transaction_create_request_body_dict = managed_transaction_create_request_body_instance.to_dict()
# create an instance of ManagedTransactionCreateRequestBody from a dict
managed_transaction_create_request_body_form_dict = managed_transaction_create_request_body.from_dict(managed_transaction_create_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


