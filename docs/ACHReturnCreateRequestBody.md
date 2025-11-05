# ACHReturnCreateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ach_return** | [**ACHReturnCreateRequest**](ACHReturnCreateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.ach_return_create_request_body import ACHReturnCreateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ACHReturnCreateRequestBody from a JSON string
ach_return_create_request_body_instance = ACHReturnCreateRequestBody.from_json(json)
# print the JSON string representation of the object
print ACHReturnCreateRequestBody.to_json()

# convert the object into a dict
ach_return_create_request_body_dict = ach_return_create_request_body_instance.to_dict()
# create an instance of ACHReturnCreateRequestBody from a dict
ach_return_create_request_body_form_dict = ach_return_create_request_body.from_dict(ach_return_create_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


