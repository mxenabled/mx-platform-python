# ManagedMemberUpdateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**ManagedMemberUpdateRequest**](ManagedMemberUpdateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.managed_member_update_request_body import ManagedMemberUpdateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedMemberUpdateRequestBody from a JSON string
managed_member_update_request_body_instance = ManagedMemberUpdateRequestBody.from_json(json)
# print the JSON string representation of the object
print ManagedMemberUpdateRequestBody.to_json()

# convert the object into a dict
managed_member_update_request_body_dict = managed_member_update_request_body_instance.to_dict()
# create an instance of ManagedMemberUpdateRequestBody from a dict
managed_member_update_request_body_form_dict = managed_member_update_request_body.from_dict(managed_member_update_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


