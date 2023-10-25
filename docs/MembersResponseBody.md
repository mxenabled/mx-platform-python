# MembersResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[MemberResponse]**](MemberResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.members_response_body import MembersResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of MembersResponseBody from a JSON string
members_response_body_instance = MembersResponseBody.from_json(json)
# print the JSON string representation of the object
print MembersResponseBody.to_json()

# convert the object into a dict
members_response_body_dict = members_response_body_instance.to_dict()
# create an instance of MembersResponseBody from a dict
members_response_body_form_dict = members_response_body.from_dict(members_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


