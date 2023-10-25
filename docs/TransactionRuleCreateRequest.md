# TransactionRuleCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_guid** | **str** |  | 
**description** | **str** |  | [optional] 
**match_description** | **str** |  | 

## Example

```python
from mx_platform_python.models.transaction_rule_create_request import TransactionRuleCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionRuleCreateRequest from a JSON string
transaction_rule_create_request_instance = TransactionRuleCreateRequest.from_json(json)
# print the JSON string representation of the object
print TransactionRuleCreateRequest.to_json()

# convert the object into a dict
transaction_rule_create_request_dict = transaction_rule_create_request_instance.to_dict()
# create an instance of TransactionRuleCreateRequest from a dict
transaction_rule_create_request_form_dict = transaction_rule_create_request.from_dict(transaction_rule_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


