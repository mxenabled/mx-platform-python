# RepeatingTransactionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** |  | [optional] 
**amount** | **float** |  | [optional] 
**description** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**member_guid** | **str** |  | [optional] 
**merchant_guid** | **str** |  | [optional] 
**last_posted_date** | **str** |  | [optional] 
**predicted_occurs_on** | **str** |  | [optional] 
**recurrence_type** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 
**repeating_transaction_type** | **str** |  | [optional] 
**transaction_type** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.repeating_transaction_response import RepeatingTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RepeatingTransactionResponse from a JSON string
repeating_transaction_response_instance = RepeatingTransactionResponse.from_json(json)
# print the JSON string representation of the object
print RepeatingTransactionResponse.to_json()

# convert the object into a dict
repeating_transaction_response_dict = repeating_transaction_response_instance.to_dict()
# create an instance of RepeatingTransactionResponse from a dict
repeating_transaction_response_form_dict = repeating_transaction_response.from_dict(repeating_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


