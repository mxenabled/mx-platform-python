# UserCreateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**UserCreateRequest**](UserCreateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.user_create_request_body import UserCreateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreateRequestBody from a JSON string
user_create_request_body_instance = UserCreateRequestBody.from_json(json)
# print the JSON string representation of the object
print UserCreateRequestBody.to_json()

# convert the object into a dict
user_create_request_body_dict = user_create_request_body_instance.to_dict()
# create an instance of UserCreateRequestBody from a dict
user_create_request_body_form_dict = user_create_request_body.from_dict(user_create_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


