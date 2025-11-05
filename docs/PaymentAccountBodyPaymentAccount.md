# PaymentAccountBodyPaymentAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** |  | [optional] 
**member_guid** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 
**account_name** | **object** |  | [optional] 
**account_number** | **object** |  | [optional] 
**account_type** | **object** |  | [optional] 
**available_balance** | **object** |  | [optional] 
**balance** | **object** |  | [optional] 
**created_at** | **object** |  | [optional] 
**routing_number** | **object** |  | [optional] 
**transit_number** | **object** |  | [optional] 
**updated_at** | **object** |  | [optional] 

## Example

```python
from mx_platform_python.models.payment_account_body_payment_account import PaymentAccountBodyPaymentAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAccountBodyPaymentAccount from a JSON string
payment_account_body_payment_account_instance = PaymentAccountBodyPaymentAccount.from_json(json)
# print the JSON string representation of the object
print PaymentAccountBodyPaymentAccount.to_json()

# convert the object into a dict
payment_account_body_payment_account_dict = payment_account_body_payment_account_instance.to_dict()
# create an instance of PaymentAccountBodyPaymentAccount from a dict
payment_account_body_payment_account_form_dict = payment_account_body_payment_account.from_dict(payment_account_body_payment_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


