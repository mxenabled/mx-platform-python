# AuthorizationCodeResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_code** | [**List[AuthorizationCodeResponse]**](AuthorizationCodeResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.authorization_code_response_body import AuthorizationCodeResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationCodeResponseBody from a JSON string
authorization_code_response_body_instance = AuthorizationCodeResponseBody.from_json(json)
# print the JSON string representation of the object
print AuthorizationCodeResponseBody.to_json()

# convert the object into a dict
authorization_code_response_body_dict = authorization_code_response_body_instance.to_dict()
# create an instance of AuthorizationCodeResponseBody from a dict
authorization_code_response_body_form_dict = authorization_code_response_body.from_dict(authorization_code_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


