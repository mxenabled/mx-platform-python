# EnhanceTransactionsRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[EnhanceTransactionsRequest]**](EnhanceTransactionsRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.enhance_transactions_request_body import EnhanceTransactionsRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of EnhanceTransactionsRequestBody from a JSON string
enhance_transactions_request_body_instance = EnhanceTransactionsRequestBody.from_json(json)
# print the JSON string representation of the object
print EnhanceTransactionsRequestBody.to_json()

# convert the object into a dict
enhance_transactions_request_body_dict = enhance_transactions_request_body_instance.to_dict()
# create an instance of EnhanceTransactionsRequestBody from a dict
enhance_transactions_request_body_form_dict = enhance_transactions_request_body.from_dict(enhance_transactions_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


