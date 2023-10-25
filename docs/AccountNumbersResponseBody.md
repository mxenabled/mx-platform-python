# AccountNumbersResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_numbers** | [**List[AccountNumberResponse]**](AccountNumberResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.account_numbers_response_body import AccountNumbersResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of AccountNumbersResponseBody from a JSON string
account_numbers_response_body_instance = AccountNumbersResponseBody.from_json(json)
# print the JSON string representation of the object
print AccountNumbersResponseBody.to_json()

# convert the object into a dict
account_numbers_response_body_dict = account_numbers_response_body_instance.to_dict()
# create an instance of AccountNumbersResponseBody from a dict
account_numbers_response_body_form_dict = account_numbers_response_body.from_dict(account_numbers_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


