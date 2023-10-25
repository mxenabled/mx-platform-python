# TransactionRulesResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 
**transaction_rules** | [**List[TransactionRuleResponse]**](TransactionRuleResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.transaction_rules_response_body import TransactionRulesResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRulesResponseBody from a JSON string
transaction_rules_response_body_instance = TransactionRulesResponseBody.from_json(json)
# print the JSON string representation of the object
print TransactionRulesResponseBody.to_json()

# convert the object into a dict
transaction_rules_response_body_dict = transaction_rules_response_body_instance.to_dict()
# create an instance of TransactionRulesResponseBody from a dict
transaction_rules_response_body_form_dict = transaction_rules_response_body.from_dict(transaction_rules_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


