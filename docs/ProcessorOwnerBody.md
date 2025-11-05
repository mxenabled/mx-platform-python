# ProcessorOwnerBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_owners** | [**List[ProcessorOwnerBodyAccountOwnersInner]**](ProcessorOwnerBodyAccountOwnersInner.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.processor_owner_body import ProcessorOwnerBody

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessorOwnerBody from a JSON string
processor_owner_body_instance = ProcessorOwnerBody.from_json(json)
# print the JSON string representation of the object
print ProcessorOwnerBody.to_json()

# convert the object into a dict
processor_owner_body_dict = processor_owner_body_instance.to_dict()
# create an instance of ProcessorOwnerBody from a dict
processor_owner_body_form_dict = processor_owner_body.from_dict(processor_owner_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


