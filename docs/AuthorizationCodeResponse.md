# AuthorizationCodeResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.authorization_code_response import AuthorizationCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationCodeResponse from a JSON string
authorization_code_response_instance = AuthorizationCodeResponse.from_json(json)
# print the JSON string representation of the object
print AuthorizationCodeResponse.to_json()

# convert the object into a dict
authorization_code_response_dict = authorization_code_response_instance.to_dict()
# create an instance of AuthorizationCodeResponse from a dict
authorization_code_response_form_dict = authorization_code_response.from_dict(authorization_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


