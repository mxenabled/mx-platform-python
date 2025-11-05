# ProcessorAccountNumberBodyAccountNumbersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** |  | [optional] 
**member_guid** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 
**account_number** | **int** |  | [optional] 
**guid** | **str** |  | [optional] 
**institution_number** | **object** |  | [optional] 
**loan_guarantor** | **object** |  | [optional] 
**loan_reference_number** | **object** |  | [optional] 
**passed_validation** | **object** |  | [optional] 
**routing_number** | **int** |  | [optional] 
**sequence_number** | **object** |  | [optional] 
**transit_number** | **object** |  | [optional] 

## Example

```python
from mx_platform_python.models.processor_account_number_body_account_numbers_inner import ProcessorAccountNumberBodyAccountNumbersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessorAccountNumberBodyAccountNumbersInner from a JSON string
processor_account_number_body_account_numbers_inner_instance = ProcessorAccountNumberBodyAccountNumbersInner.from_json(json)
# print the JSON string representation of the object
print ProcessorAccountNumberBodyAccountNumbersInner.to_json()

# convert the object into a dict
processor_account_number_body_account_numbers_inner_dict = processor_account_number_body_account_numbers_inner_instance.to_dict()
# create an instance of ProcessorAccountNumberBodyAccountNumbersInner from a dict
processor_account_number_body_account_numbers_inner_form_dict = processor_account_number_body_account_numbers_inner.from_dict(processor_account_number_body_account_numbers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


