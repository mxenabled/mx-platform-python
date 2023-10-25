# AccountUpdateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**AccountUpdateRequest**](AccountUpdateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.account_update_request_body import AccountUpdateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUpdateRequestBody from a JSON string
account_update_request_body_instance = AccountUpdateRequestBody.from_json(json)
# print the JSON string representation of the object
print AccountUpdateRequestBody.to_json()

# convert the object into a dict
account_update_request_body_dict = account_update_request_body_instance.to_dict()
# create an instance of AccountUpdateRequestBody from a dict
account_update_request_body_form_dict = account_update_request_body.from_dict(account_update_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


