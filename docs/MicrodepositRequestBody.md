# MicrodepositRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**micro_deposit** | [**MicrodepositRequest**](MicrodepositRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.microdeposit_request_body import MicrodepositRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of MicrodepositRequestBody from a JSON string
microdeposit_request_body_instance = MicrodepositRequestBody.from_json(json)
# print the JSON string representation of the object
print MicrodepositRequestBody.to_json()

# convert the object into a dict
microdeposit_request_body_dict = microdeposit_request_body_instance.to_dict()
# create an instance of MicrodepositRequestBody from a dict
microdeposit_request_body_form_dict = microdeposit_request_body.from_dict(microdeposit_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


