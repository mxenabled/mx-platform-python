# AccountResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**AccountResponse**](AccountResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.account_response_body import AccountResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of AccountResponseBody from a JSON string
account_response_body_instance = AccountResponseBody.from_json(json)
# print the JSON string representation of the object
print AccountResponseBody.to_json()

# convert the object into a dict
account_response_body_dict = account_response_body_instance.to_dict()
# create an instance of AccountResponseBody from a dict
account_response_body_form_dict = account_response_body.from_dict(account_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


