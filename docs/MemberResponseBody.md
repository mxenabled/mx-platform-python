# MemberResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**MemberResponse**](MemberResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.member_response_body import MemberResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of MemberResponseBody from a JSON string
member_response_body_instance = MemberResponseBody.from_json(json)
# print the JSON string representation of the object
print MemberResponseBody.to_json()

# convert the object into a dict
member_response_body_dict = member_response_body_instance.to_dict()
# create an instance of MemberResponseBody from a dict
member_response_body_form_dict = member_response_body.from_dict(member_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


