# UserUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_disabled** | **bool** |  | [optional] 
**metadata** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.user_update_request import UserUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpdateRequest from a JSON string
user_update_request_instance = UserUpdateRequest.from_json(json)
# print the JSON string representation of the object
print UserUpdateRequest.to_json()

# convert the object into a dict
user_update_request_dict = user_update_request_instance.to_dict()
# create an instance of UserUpdateRequest from a dict
user_update_request_form_dict = user_update_request.from_dict(user_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


