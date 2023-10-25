# OAuthWindowResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**OAuthWindowResponse**](OAuthWindowResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.o_auth_window_response_body import OAuthWindowResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthWindowResponseBody from a JSON string
o_auth_window_response_body_instance = OAuthWindowResponseBody.from_json(json)
# print the JSON string representation of the object
print OAuthWindowResponseBody.to_json()

# convert the object into a dict
o_auth_window_response_body_dict = o_auth_window_response_body_instance.to_dict()
# create an instance of OAuthWindowResponseBody from a dict
o_auth_window_response_body_form_dict = o_auth_window_response_body.from_dict(o_auth_window_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


