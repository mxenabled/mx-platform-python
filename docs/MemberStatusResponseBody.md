# MemberStatusResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**MemberStatusResponse**](MemberStatusResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.member_status_response_body import MemberStatusResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of MemberStatusResponseBody from a JSON string
member_status_response_body_instance = MemberStatusResponseBody.from_json(json)
# print the JSON string representation of the object
print MemberStatusResponseBody.to_json()

# convert the object into a dict
member_status_response_body_dict = member_status_response_body_instance.to_dict()
# create an instance of MemberStatusResponseBody from a dict
member_status_response_body_form_dict = member_status_response_body.from_dict(member_status_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


