# MicrodepositResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**institution_code** | **str** |  | [optional] 
**institution_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**verified_at** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.microdeposit_response import MicrodepositResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MicrodepositResponse from a JSON string
microdeposit_response_instance = MicrodepositResponse.from_json(json)
# print the JSON string representation of the object
print MicrodepositResponse.to_json()

# convert the object into a dict
microdeposit_response_dict = microdeposit_response_instance.to_dict()
# create an instance of MicrodepositResponse from a dict
microdeposit_response_form_dict = microdeposit_response.from_dict(microdeposit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


