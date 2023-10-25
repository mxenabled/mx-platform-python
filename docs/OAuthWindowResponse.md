# OAuthWindowResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | [optional] 
**oauth_window_uri** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.o_auth_window_response import OAuthWindowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthWindowResponse from a JSON string
o_auth_window_response_instance = OAuthWindowResponse.from_json(json)
# print the JSON string representation of the object
print OAuthWindowResponse.to_json()

# convert the object into a dict
o_auth_window_response_dict = o_auth_window_response_instance.to_dict()
# create an instance of OAuthWindowResponse from a dict
o_auth_window_response_form_dict = o_auth_window_response.from_dict(o_auth_window_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


