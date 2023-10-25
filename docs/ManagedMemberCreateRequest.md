# ManagedMemberCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**institution_code** | **str** |  | 
**metadata** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.managed_member_create_request import ManagedMemberCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedMemberCreateRequest from a JSON string
managed_member_create_request_instance = ManagedMemberCreateRequest.from_json(json)
# print the JSON string representation of the object
print ManagedMemberCreateRequest.to_json()

# convert the object into a dict
managed_member_create_request_dict = managed_member_create_request_instance.to_dict()
# create an instance of ManagedMemberCreateRequest from a dict
managed_member_create_request_form_dict = managed_member_create_request.from_dict(managed_member_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


