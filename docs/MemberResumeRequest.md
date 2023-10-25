# MemberResumeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenges** | [**List[CredentialRequest]**](CredentialRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.member_resume_request import MemberResumeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MemberResumeRequest from a JSON string
member_resume_request_instance = MemberResumeRequest.from_json(json)
# print the JSON string representation of the object
print MemberResumeRequest.to_json()

# convert the object into a dict
member_resume_request_dict = member_resume_request_instance.to_dict()
# create an instance of MemberResumeRequest from a dict
member_resume_request_form_dict = member_resume_request.from_dict(member_resume_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


