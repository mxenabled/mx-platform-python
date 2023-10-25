# ManagedAccountCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**apr** | **float** |  | [optional] 
**apy** | **float** |  | [optional] 
**available_balance** | **float** |  | [optional] 
**available_credit** | **float** |  | [optional] 
**balance** | **float** |  | 
**cash_surrender_value** | **float** |  | [optional] 
**credit_limit** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**day_payment_is_due** | **int** |  | [optional] 
**death_benefit** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**interest_rate** | **float** |  | [optional] 
**is_closed** | **bool** |  | [optional] 
**is_hidden** | **bool** |  | [optional] 
**last_payment** | **float** |  | [optional] 
**last_payment_at** | **str** |  | [optional] 
**loan_amount** | **float** |  | [optional] 
**matures_on** | **str** |  | [optional] 
**metadata** | **str** |  | [optional] 
**minimum_balance** | **float** |  | [optional] 
**minimum_payment** | **float** |  | [optional] 
**name** | **str** |  | 
**nickname** | **str** |  | [optional] 
**original_balance** | **float** |  | [optional] 
**payment_due_at** | **str** |  | [optional] 
**payoff_balance** | **float** |  | [optional] 
**routing_number** | **str** |  | [optional] 
**started_on** | **str** |  | [optional] 
**subtype** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from mx_platform_python.models.managed_account_create_request import ManagedAccountCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedAccountCreateRequest from a JSON string
managed_account_create_request_instance = ManagedAccountCreateRequest.from_json(json)
# print the JSON string representation of the object
print ManagedAccountCreateRequest.to_json()

# convert the object into a dict
managed_account_create_request_dict = managed_account_create_request_instance.to_dict()
# create an instance of ManagedAccountCreateRequest from a dict
managed_account_create_request_form_dict = managed_account_create_request.from_dict(managed_account_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


