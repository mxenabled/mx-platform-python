# MicrodepositRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | 
**account_type** | **str** |  | 
**routing_number** | **str** |  | 
**account_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.microdeposit_request import MicrodepositRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MicrodepositRequest from a JSON string
microdeposit_request_instance = MicrodepositRequest.from_json(json)
# print the JSON string representation of the object
print MicrodepositRequest.to_json()

# convert the object into a dict
microdeposit_request_dict = microdeposit_request_instance.to_dict()
# create an instance of MicrodepositRequest from a dict
microdeposit_request_form_dict = microdeposit_request.from_dict(microdeposit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


