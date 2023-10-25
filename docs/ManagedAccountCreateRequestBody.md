# ManagedAccountCreateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**ManagedAccountCreateRequest**](ManagedAccountCreateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.managed_account_create_request_body import ManagedAccountCreateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedAccountCreateRequestBody from a JSON string
managed_account_create_request_body_instance = ManagedAccountCreateRequestBody.from_json(json)
# print the JSON string representation of the object
print ManagedAccountCreateRequestBody.to_json()

# convert the object into a dict
managed_account_create_request_body_dict = managed_account_create_request_body_instance.to_dict()
# create an instance of ManagedAccountCreateRequestBody from a dict
managed_account_create_request_body_form_dict = managed_account_create_request_body.from_dict(managed_account_create_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


