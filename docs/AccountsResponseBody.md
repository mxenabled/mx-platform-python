# AccountsResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[AccountResponse]**](AccountResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.accounts_response_body import AccountsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of AccountsResponseBody from a JSON string
accounts_response_body_instance = AccountsResponseBody.from_json(json)
# print the JSON string representation of the object
print AccountsResponseBody.to_json()

# convert the object into a dict
accounts_response_body_dict = accounts_response_body_instance.to_dict()
# create an instance of AccountsResponseBody from a dict
accounts_response_body_form_dict = accounts_response_body.from_dict(accounts_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


