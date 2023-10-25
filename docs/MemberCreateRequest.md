# MemberCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_aggregation_is_disabled** | **bool** |  | [optional] 
**credentials** | [**List[CredentialRequest]**](CredentialRequest.md) |  | 
**id** | **str** |  | [optional] 
**institution_code** | **str** |  | 
**is_oauth** | **bool** |  | [optional] 
**metadata** | **str** |  | [optional] 
**skip_aggregation** | **bool** |  | [optional] 

## Example

```python
from mx_platform_python.models.member_create_request import MemberCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MemberCreateRequest from a JSON string
member_create_request_instance = MemberCreateRequest.from_json(json)
# print the JSON string representation of the object
print MemberCreateRequest.to_json()

# convert the object into a dict
member_create_request_dict = member_create_request_instance.to_dict()
# create an instance of MemberCreateRequest from a dict
member_create_request_form_dict = member_create_request.from_dict(member_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


