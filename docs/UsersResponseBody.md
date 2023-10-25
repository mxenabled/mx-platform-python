# UsersResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 
**users** | [**List[UserResponse]**](UserResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.users_response_body import UsersResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of UsersResponseBody from a JSON string
users_response_body_instance = UsersResponseBody.from_json(json)
# print the JSON string representation of the object
print UsersResponseBody.to_json()

# convert the object into a dict
users_response_body_dict = users_response_body_instance.to_dict()
# create an instance of UsersResponseBody from a dict
users_response_body_form_dict = users_response_body.from_dict(users_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


