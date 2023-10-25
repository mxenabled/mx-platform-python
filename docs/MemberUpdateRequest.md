# MemberUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background_aggregation_is_disabled** | **bool** |  | [optional] 
**credentials** | [**List[CredentialRequest]**](CredentialRequest.md) |  | [optional] 
**id** | **str** |  | [optional] 
**metadata** | **str** |  | [optional] 
**skip_aggregation** | **bool** |  | [optional] 

## Example

```python
from mx_platform_python.models.member_update_request import MemberUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MemberUpdateRequest from a JSON string
member_update_request_instance = MemberUpdateRequest.from_json(json)
# print the JSON string representation of the object
print MemberUpdateRequest.to_json()

# convert the object into a dict
member_update_request_dict = member_update_request_instance.to_dict()
# create an instance of MemberUpdateRequest from a dict
member_update_request_form_dict = member_update_request.from_dict(member_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


