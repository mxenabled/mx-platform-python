# ManagedTransactionUpdateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**ManagedTransactionUpdateRequest**](ManagedTransactionUpdateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.managed_transaction_update_request_body import ManagedTransactionUpdateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedTransactionUpdateRequestBody from a JSON string
managed_transaction_update_request_body_instance = ManagedTransactionUpdateRequestBody.from_json(json)
# print the JSON string representation of the object
print ManagedTransactionUpdateRequestBody.to_json()

# convert the object into a dict
managed_transaction_update_request_body_dict = managed_transaction_update_request_body_instance.to_dict()
# create an instance of ManagedTransactionUpdateRequestBody from a dict
managed_transaction_update_request_body_form_dict = managed_transaction_update_request_body.from_dict(managed_transaction_update_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


