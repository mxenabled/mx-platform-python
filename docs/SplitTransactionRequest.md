# SplitTransactionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount of money you want to re-categorize. | 
**description** | **str** | Description for the split transaction. | [optional] 
**category_guid** | **str** | Unique identifier of the category. | [optional] 
**memo** | **str** | Memo for the split transaction | [optional] 

## Example

```python
from mx_platform_python.models.split_transaction_request import SplitTransactionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SplitTransactionRequest from a JSON string
split_transaction_request_instance = SplitTransactionRequest.from_json(json)
# print the JSON string representation of the object
print SplitTransactionRequest.to_json()

# convert the object into a dict
split_transaction_request_dict = split_transaction_request_instance.to_dict()
# create an instance of SplitTransactionRequest from a dict
split_transaction_request_form_dict = split_transaction_request.from_dict(split_transaction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


