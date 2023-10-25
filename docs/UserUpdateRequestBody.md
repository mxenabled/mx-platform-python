# UserUpdateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserUpdateRequest**](UserUpdateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.user_update_request_body import UserUpdateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpdateRequestBody from a JSON string
user_update_request_body_instance = UserUpdateRequestBody.from_json(json)
# print the JSON string representation of the object
print UserUpdateRequestBody.to_json()

# convert the object into a dict
user_update_request_body_dict = user_update_request_body_instance.to_dict()
# create an instance of UserUpdateRequestBody from a dict
user_update_request_body_form_dict = user_update_request_body.from_dict(user_update_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


