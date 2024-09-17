# TransactionCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | 
**var_date** | **str** |  | 
**description** | **str** |  | 
**type** | **str** | The type of transaction, which must be CREDIT or DEBIT. See Transaction Fields for more information. | 
**category_guid** | **str** | Unique identifier of the category. | [optional] 
**currency_code** | **str** |  | [optional] 
**has_been_viewed** | **bool** |  | [optional] 
**is_hidden** | **bool** |  | [optional] 
**is_international** | **bool** |  | [optional] 
**memo** | **str** |  | [optional] 
**metadata** | **str** |  | [optional] 
**skip_webhook** | **bool** | When set to true, this parameter will prevent a webhook from being triggered by the request. | [optional] 

## Example

```python
from mx_platform_python.models.transaction_create_request import TransactionCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCreateRequest from a JSON string
transaction_create_request_instance = TransactionCreateRequest.from_json(json)
# print the JSON string representation of the object
print TransactionCreateRequest.to_json()

# convert the object into a dict
transaction_create_request_dict = transaction_create_request_instance.to_dict()
# create an instance of TransactionCreateRequest from a dict
transaction_create_request_form_dict = transaction_create_request.from_dict(transaction_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


