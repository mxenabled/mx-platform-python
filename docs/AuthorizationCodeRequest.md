# AuthorizationCodeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.authorization_code_request import AuthorizationCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationCodeRequest from a JSON string
authorization_code_request_instance = AuthorizationCodeRequest.from_json(json)
# print the JSON string representation of the object
print AuthorizationCodeRequest.to_json()

# convert the object into a dict
authorization_code_request_dict = authorization_code_request_instance.to_dict()
# create an instance of AuthorizationCodeRequest from a dict
authorization_code_request_form_dict = authorization_code_request.from_dict(authorization_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


