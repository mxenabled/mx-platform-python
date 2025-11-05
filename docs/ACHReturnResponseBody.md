# ACHReturnResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ach_return** | [**ACHResponse**](ACHResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.ach_return_response_body import ACHReturnResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ACHReturnResponseBody from a JSON string
ach_return_response_body_instance = ACHReturnResponseBody.from_json(json)
# print the JSON string representation of the object
print ACHReturnResponseBody.to_json()

# convert the object into a dict
ach_return_response_body_dict = ach_return_response_body_instance.to_dict()
# create an instance of ACHReturnResponseBody from a dict
ach_return_response_body_form_dict = ach_return_response_body.from_dict(ach_return_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


