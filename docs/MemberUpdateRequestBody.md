# MemberUpdateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**MemberUpdateRequest**](MemberUpdateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.member_update_request_body import MemberUpdateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of MemberUpdateRequestBody from a JSON string
member_update_request_body_instance = MemberUpdateRequestBody.from_json(json)
# print the JSON string representation of the object
print MemberUpdateRequestBody.to_json()

# convert the object into a dict
member_update_request_body_dict = member_update_request_body_instance.to_dict()
# create an instance of MemberUpdateRequestBody from a dict
member_update_request_body_form_dict = member_update_request_body.from_dict(member_update_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


