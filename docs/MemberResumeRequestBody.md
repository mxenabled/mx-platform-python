# MemberResumeRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**MemberResumeRequest**](MemberResumeRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.member_resume_request_body import MemberResumeRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of MemberResumeRequestBody from a JSON string
member_resume_request_body_instance = MemberResumeRequestBody.from_json(json)
# print the JSON string representation of the object
print MemberResumeRequestBody.to_json()

# convert the object into a dict
member_resume_request_body_dict = member_resume_request_body_instance.to_dict()
# create an instance of MemberResumeRequestBody from a dict
member_resume_request_body_form_dict = member_resume_request_body.from_dict(member_resume_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


