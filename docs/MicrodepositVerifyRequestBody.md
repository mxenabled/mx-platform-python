# MicrodepositVerifyRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**micro_deposit** | [**MicrodepositVerifyRequest**](MicrodepositVerifyRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.microdeposit_verify_request_body import MicrodepositVerifyRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of MicrodepositVerifyRequestBody from a JSON string
microdeposit_verify_request_body_instance = MicrodepositVerifyRequestBody.from_json(json)
# print the JSON string representation of the object
print MicrodepositVerifyRequestBody.to_json()

# convert the object into a dict
microdeposit_verify_request_body_dict = microdeposit_verify_request_body_instance.to_dict()
# create an instance of MicrodepositVerifyRequestBody from a dict
microdeposit_verify_request_body_form_dict = microdeposit_verify_request_body.from_dict(microdeposit_verify_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


