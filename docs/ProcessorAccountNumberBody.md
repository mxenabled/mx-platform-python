# ProcessorAccountNumberBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_numbers** | [**List[ProcessorAccountNumberBodyAccountNumbersInner]**](ProcessorAccountNumberBodyAccountNumbersInner.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.processor_account_number_body import ProcessorAccountNumberBody

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessorAccountNumberBody from a JSON string
processor_account_number_body_instance = ProcessorAccountNumberBody.from_json(json)
# print the JSON string representation of the object
print ProcessorAccountNumberBody.to_json()

# convert the object into a dict
processor_account_number_body_dict = processor_account_number_body_instance.to_dict()
# create an instance of ProcessorAccountNumberBody from a dict
processor_account_number_body_form_dict = processor_account_number_body.from_dict(processor_account_number_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


