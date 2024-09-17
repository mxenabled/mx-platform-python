# MicrodepositResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**micro_deposit** | [**MicrodepositResponse**](MicrodepositResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.microdeposit_response_body import MicrodepositResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of MicrodepositResponseBody from a JSON string
microdeposit_response_body_instance = MicrodepositResponseBody.from_json(json)
# print the JSON string representation of the object
print MicrodepositResponseBody.to_json()

# convert the object into a dict
microdeposit_response_body_dict = microdeposit_response_body_instance.to_dict()
# create an instance of MicrodepositResponseBody from a dict
microdeposit_response_body_form_dict = microdeposit_response_body.from_dict(microdeposit_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


