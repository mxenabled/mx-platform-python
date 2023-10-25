# ManagedMemberCreateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**ManagedMemberCreateRequest**](ManagedMemberCreateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.managed_member_create_request_body import ManagedMemberCreateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedMemberCreateRequestBody from a JSON string
managed_member_create_request_body_instance = ManagedMemberCreateRequestBody.from_json(json)
# print the JSON string representation of the object
print ManagedMemberCreateRequestBody.to_json()

# convert the object into a dict
managed_member_create_request_body_dict = managed_member_create_request_body_instance.to_dict()
# create an instance of ManagedMemberCreateRequestBody from a dict
managed_member_create_request_body_form_dict = managed_member_create_request_body.from_dict(managed_member_create_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


