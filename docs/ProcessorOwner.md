# ProcessorOwner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **object** |  | [optional] 
**owner_name** | **object** |  | [optional] 
**address** | **object** |  | [optional] 
**city** | **object** |  | [optional] 
**state** | **object** |  | [optional] 
**postal_code** | **object** |  | [optional] 
**country** | **object** |  | [optional] 
**email** | **object** |  | [optional] 
**phone** | **object** |  | [optional] 

## Example

```python
from mx_platform_python.models.processor_owner import ProcessorOwner

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessorOwner from a JSON string
processor_owner_instance = ProcessorOwner.from_json(json)
# print the JSON string representation of the object
print ProcessorOwner.to_json()

# convert the object into a dict
processor_owner_dict = processor_owner_instance.to_dict()
# create an instance of ProcessorOwner from a dict
processor_owner_form_dict = processor_owner.from_dict(processor_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


