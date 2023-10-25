# UserResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserResponse**](UserResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.user_response_body import UserResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponseBody from a JSON string
user_response_body_instance = UserResponseBody.from_json(json)
# print the JSON string representation of the object
print UserResponseBody.to_json()

# convert the object into a dict
user_response_body_dict = user_response_body_instance.to_dict()
# create an instance of UserResponseBody from a dict
user_response_body_form_dict = user_response_body.from_dict(user_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


