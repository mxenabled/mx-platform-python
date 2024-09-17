# MicrodepositVerifyRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposit_amount_1** | **int** |  | [optional] 
**deposit_amount_2** | **int** |  | [optional] 

## Example

```python
from mx_platform_python.models.microdeposit_verify_request import MicrodepositVerifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MicrodepositVerifyRequest from a JSON string
microdeposit_verify_request_instance = MicrodepositVerifyRequest.from_json(json)
# print the JSON string representation of the object
print MicrodepositVerifyRequest.to_json()

# convert the object into a dict
microdeposit_verify_request_dict = microdeposit_verify_request_instance.to_dict()
# create an instance of MicrodepositVerifyRequest from a dict
microdeposit_verify_request_form_dict = microdeposit_verify_request.from_dict(microdeposit_verify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


