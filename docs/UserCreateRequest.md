# UserCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_disabled** | **bool** |  | [optional] 
**metadata** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.user_create_request import UserCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreateRequest from a JSON string
user_create_request_instance = UserCreateRequest.from_json(json)
# print the JSON string representation of the object
print UserCreateRequest.to_json()

# convert the object into a dict
user_create_request_dict = user_create_request_instance.to_dict()
# create an instance of UserCreateRequest from a dict
user_create_request_form_dict = user_create_request.from_dict(user_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


