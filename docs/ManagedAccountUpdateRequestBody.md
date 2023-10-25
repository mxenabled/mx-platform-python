# ManagedAccountUpdateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**ManagedAccountUpdateRequest**](ManagedAccountUpdateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.managed_account_update_request_body import ManagedAccountUpdateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedAccountUpdateRequestBody from a JSON string
managed_account_update_request_body_instance = ManagedAccountUpdateRequestBody.from_json(json)
# print the JSON string representation of the object
print ManagedAccountUpdateRequestBody.to_json()

# convert the object into a dict
managed_account_update_request_body_dict = managed_account_update_request_body_instance.to_dict()
# create an instance of ManagedAccountUpdateRequestBody from a dict
managed_account_update_request_body_form_dict = managed_account_update_request_body.from_dict(managed_account_update_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


