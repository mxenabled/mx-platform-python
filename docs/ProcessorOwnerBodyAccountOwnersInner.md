# ProcessorOwnerBodyAccountOwnersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** |  | [optional] 
**member_guid** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 
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
from mx_platform_python.models.processor_owner_body_account_owners_inner import ProcessorOwnerBodyAccountOwnersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessorOwnerBodyAccountOwnersInner from a JSON string
processor_owner_body_account_owners_inner_instance = ProcessorOwnerBodyAccountOwnersInner.from_json(json)
# print the JSON string representation of the object
print ProcessorOwnerBodyAccountOwnersInner.to_json()

# convert the object into a dict
processor_owner_body_account_owners_inner_dict = processor_owner_body_account_owners_inner_instance.to_dict()
# create an instance of ProcessorOwnerBodyAccountOwnersInner from a dict
processor_owner_body_account_owners_inner_form_dict = processor_owner_body_account_owners_inner.from_dict(processor_owner_body_account_owners_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


