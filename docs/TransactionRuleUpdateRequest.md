# TransactionRuleUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_guid** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**match_description** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.transaction_rule_update_request import TransactionRuleUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRuleUpdateRequest from a JSON string
transaction_rule_update_request_instance = TransactionRuleUpdateRequest.from_json(json)
# print the JSON string representation of the object
print TransactionRuleUpdateRequest.to_json()

# convert the object into a dict
transaction_rule_update_request_dict = transaction_rule_update_request_instance.to_dict()
# create an instance of TransactionRuleUpdateRequest from a dict
transaction_rule_update_request_form_dict = transaction_rule_update_request.from_dict(transaction_rule_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


