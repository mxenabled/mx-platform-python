# TransactionRuleUpdateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_rule** | [**TransactionRuleUpdateRequest**](TransactionRuleUpdateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.transaction_rule_update_request_body import TransactionRuleUpdateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRuleUpdateRequestBody from a JSON string
transaction_rule_update_request_body_instance = TransactionRuleUpdateRequestBody.from_json(json)
# print the JSON string representation of the object
print TransactionRuleUpdateRequestBody.to_json()

# convert the object into a dict
transaction_rule_update_request_body_dict = transaction_rule_update_request_body_instance.to_dict()
# create an instance of TransactionRuleUpdateRequestBody from a dict
transaction_rule_update_request_body_form_dict = transaction_rule_update_request_body.from_dict(transaction_rule_update_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


