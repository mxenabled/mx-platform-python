# TransactionRuleResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_guid** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**match_description** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.transaction_rule_response import TransactionRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRuleResponse from a JSON string
transaction_rule_response_instance = TransactionRuleResponse.from_json(json)
# print the JSON string representation of the object
print TransactionRuleResponse.to_json()

# convert the object into a dict
transaction_rule_response_dict = transaction_rule_response_instance.to_dict()
# create an instance of TransactionRuleResponse from a dict
transaction_rule_response_form_dict = transaction_rule_response.from_dict(transaction_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


