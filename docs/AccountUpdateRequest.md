# AccountUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_subtype** | **str** | Can only be updated for manual accounts. | [optional] 
**account_type** | **str** | Can only be updated for manual accounts. | [optional] 
**apr** | **float** | Can only be updated for manual accounts. | [optional] 
**apy** | **float** | Can only be updated for manual accounts. | [optional] 
**available_balance** | **float** | Can only be updated for manual accounts. | [optional] 
**balance** | **float** | Can only be updated for manual accounts. | [optional] 
**cash_surrender_value** | **float** | Can only be updated for manual accounts. | [optional] 
**credit_limit** | **float** | Can only be updated for manual accounts. | [optional] 
**currency_code** | **str** | Can only be updated for manual accounts. | [optional] 
**death_benefit** | **int** | Can only be updated for manual accounts. | [optional] 
**interest_rate** | **float** | Can only be updated for manual accounts. | [optional] 
**is_business** | **bool** | Can be updated for manual accounts and aggregated accounts. | [optional] 
**is_closed** | **bool** | Can only be updated for manual accounts. | [optional] 
**is_hidden** | **bool** | Can be updated for manual accounts and aggregated accounts. | [optional] 
**loan_amount** | **float** | Can only be updated for manual accounts. | [optional] 
**metadata** | **str** | Can only be updated for manual accounts. | [optional] 
**name** | **str** | Can only be updated for manual accounts. | [optional] 
**nickname** | **str** | Can only be updated for manual accounts. | [optional] 
**original_balance** | **float** | Can only be updated for manual accounts. | [optional] 
**property_type** | **str** | Can only be updated for manual accounts. | [optional] 
**skip_webhook** | **bool** | If set to true, prevents sending an account webhook for the update if that webhook type is enabled for you. | [optional] 

## Example

```python
from mx_platform_python.models.account_update_request import AccountUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUpdateRequest from a JSON string
account_update_request_instance = AccountUpdateRequest.from_json(json)
# print the JSON string representation of the object
print AccountUpdateRequest.to_json()

# convert the object into a dict
account_update_request_dict = account_update_request_instance.to_dict()
# create an instance of AccountUpdateRequest from a dict
account_update_request_form_dict = account_update_request.from_dict(account_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


