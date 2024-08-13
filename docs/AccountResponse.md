# AccountResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** |  | [optional] 
**account_ownership** | **str** |  | [optional] 
**annuity_policy_to_date** | **str** |  | [optional] 
**annuity_provider** | **str** |  | [optional] 
**annuity_term_year** | **float** |  | [optional] 
**apr** | **float** |  | [optional] 
**apy** | **float** |  | [optional] 
**available_balance** | **float** |  | [optional] 
**available_credit** | **float** |  | [optional] 
**balance** | **float** |  | [optional] 
**cash_balance** | **float** |  | [optional] 
**cash_surrender_value** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
**credit_limit** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**day_payment_is_due** | **int** |  | [optional] 
**death_benefit** | **int** |  | [optional] 
**guid** | **str** |  | [optional] 
**holdings_value** | **float** |  | [optional] 
**id** | **str** |  | [optional] 
**imported_at** | **str** |  | [optional] 
**institution_code** | **str** |  | [optional] 
**insured_name** | **str** |  | [optional] 
**interest_rate** | **float** |  | [optional] 
**is_closed** | **bool** |  | [optional] 
**is_hidden** | **bool** |  | [optional] 
**is_manual** | **bool** |  | [optional] 
**last_payment** | **float** |  | [optional] 
**last_payment_at** | **str** |  | [optional] 
**loan_amount** | **float** |  | [optional] 
**margin_balance** | **float** |  | [optional] 
**matures_on** | **str** |  | [optional] 
**member_guid** | **str** |  | [optional] 
**member_id** | **str** |  | [optional] 
**member_is_managed_by_user** | **bool** |  | [optional] 
**metadata** | **str** |  | [optional] 
**minimum_balance** | **float** |  | [optional] 
**minimum_payment** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**original_balance** | **float** |  | [optional] 
**pay_out_amount** | **float** |  | [optional] 
**payment_due_at** | **str** |  | [optional] 
**payoff_balance** | **float** |  | [optional] 
**premium_amount** | **float** |  | [optional] 
**property_type** | **str** |  | [optional] 
**routing_number** | **str** |  | [optional] 
**started_on** | **str** |  | [optional] 
**statement_balance** | **float** |  | [optional] 
**subtype** | **str** |  | [optional] 
**today_ugl_amount** | **float** |  | [optional] 
**today_ugl_percentage** | **float** |  | [optional] 
**total_account_value** | **float** |  | [optional] 
**total_account_value_ugl** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.account_response import AccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountResponse from a JSON string
account_response_instance = AccountResponse.from_json(json)
# print the JSON string representation of the object
print AccountResponse.to_json()

# convert the object into a dict
account_response_dict = account_response_instance.to_dict()
# create an instance of AccountResponse from a dict
account_response_form_dict = account_response.from_dict(account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


