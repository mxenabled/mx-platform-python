# CredentialsResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**List[CredentialResponse]**](CredentialResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.credentials_response_body import CredentialsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsResponseBody from a JSON string
credentials_response_body_instance = CredentialsResponseBody.from_json(json)
# print the JSON string representation of the object
print CredentialsResponseBody.to_json()

# convert the object into a dict
credentials_response_body_dict = credentials_response_body_instance.to_dict()
# create an instance of CredentialsResponseBody from a dict
credentials_response_body_form_dict = credentials_response_body.from_dict(credentials_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


