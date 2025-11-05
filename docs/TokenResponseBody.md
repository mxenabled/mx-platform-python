# TokenResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tokens** | [**List[TokenResponse]**](TokenResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.token_response_body import TokenResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of TokenResponseBody from a JSON string
token_response_body_instance = TokenResponseBody.from_json(json)
# print the JSON string representation of the object
print TokenResponseBody.to_json()

# convert the object into a dict
token_response_body_dict = token_response_body_instance.to_dict()
# create an instance of TokenResponseBody from a dict
token_response_body_form_dict = token_response_body.from_dict(token_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


