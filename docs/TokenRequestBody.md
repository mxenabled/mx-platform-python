# TokenRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**MemberElements**](MemberElements.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.token_request_body import TokenRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of TokenRequestBody from a JSON string
token_request_body_instance = TokenRequestBody.from_json(json)
# print the JSON string representation of the object
print TokenRequestBody.to_json()

# convert the object into a dict
token_request_body_dict = token_request_body_instance.to_dict()
# create an instance of TokenRequestBody from a dict
token_request_body_form_dict = token_request_body.from_dict(token_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


