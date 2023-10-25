# AccountCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_subtype** | **str** |  | [optional] 
**account_type** | **str** |  | 
**apr** | **float** |  | [optional] 
**apy** | **float** |  | [optional] 
**available_balance** | **float** |  | [optional] 
**balance** | **float** |  | [optional] 
**cash_surrender_value** | **float** |  | [optional] 
**credit_limit** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**death_benefit** | **int** |  | [optional] 
**interest_rate** | **float** |  | [optional] 
**is_business** | **bool** |  | [optional] 
**is_closed** | **bool** |  | [optional] 
**is_hidden** | **bool** |  | [optional] 
**loan_amount** | **float** |  | [optional] 
**metadata** | **str** |  | [optional] 
**name** | **str** |  | 
**nickname** | **str** |  | [optional] 
**original_balance** | **float** |  | [optional] 
**property_type** | **str** |  | [optional] 
**skip_webhook** | **bool** |  | [optional] 

## Example

```python
from mx_platform_python.models.account_create_request import AccountCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountCreateRequest from a JSON string
account_create_request_instance = AccountCreateRequest.from_json(json)
# print the JSON string representation of the object
print AccountCreateRequest.to_json()

# convert the object into a dict
account_create_request_dict = account_create_request_instance.to_dict()
# create an instance of AccountCreateRequest from a dict
account_create_request_form_dict = account_create_request.from_dict(account_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


