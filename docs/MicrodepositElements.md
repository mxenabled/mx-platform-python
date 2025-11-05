# MicrodepositElements


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** |  | [optional] 
**account_number** | **str** |  | 
**account_type** | **str** |  | 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**routing_number** | **str** |  | 

## Example

```python
from mx_platform_python.models.microdeposit_elements import MicrodepositElements

# TODO update the JSON string below
json = "{}"
# create an instance of MicrodepositElements from a JSON string
microdeposit_elements_instance = MicrodepositElements.from_json(json)
# print the JSON string representation of the object
print MicrodepositElements.to_json()

# convert the object into a dict
microdeposit_elements_dict = microdeposit_elements_instance.to_dict()
# create an instance of MicrodepositElements from a dict
microdeposit_elements_form_dict = microdeposit_elements.from_dict(microdeposit_elements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


