# TransactionUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 

## Example

```python
from mx_platform_python.models.transaction_update_request import TransactionUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionUpdateRequest from a JSON string
transaction_update_request_instance = TransactionUpdateRequest.from_json(json)
# print the JSON string representation of the object
print TransactionUpdateRequest.to_json()

# convert the object into a dict
transaction_update_request_dict = transaction_update_request_instance.to_dict()
# create an instance of TransactionUpdateRequest from a dict
transaction_update_request_form_dict = transaction_update_request.from_dict(transaction_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


