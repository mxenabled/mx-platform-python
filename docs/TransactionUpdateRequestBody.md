# TransactionUpdateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**TransactionUpdateRequest**](TransactionUpdateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.transaction_update_request_body import TransactionUpdateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionUpdateRequestBody from a JSON string
transaction_update_request_body_instance = TransactionUpdateRequestBody.from_json(json)
# print the JSON string representation of the object
print TransactionUpdateRequestBody.to_json()

# convert the object into a dict
transaction_update_request_body_dict = transaction_update_request_body_instance.to_dict()
# create an instance of TransactionUpdateRequestBody from a dict
transaction_update_request_body_form_dict = transaction_update_request_body.from_dict(transaction_update_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


