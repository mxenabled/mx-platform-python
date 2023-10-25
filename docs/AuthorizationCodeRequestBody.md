# AuthorizationCodeRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_code** | [**AuthorizationCodeRequest**](AuthorizationCodeRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.authorization_code_request_body import AuthorizationCodeRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationCodeRequestBody from a JSON string
authorization_code_request_body_instance = AuthorizationCodeRequestBody.from_json(json)
# print the JSON string representation of the object
print AuthorizationCodeRequestBody.to_json()

# convert the object into a dict
authorization_code_request_body_dict = authorization_code_request_body_instance.to_dict()
# create an instance of AuthorizationCodeRequestBody from a dict
authorization_code_request_body_form_dict = authorization_code_request_body.from_dict(authorization_code_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


