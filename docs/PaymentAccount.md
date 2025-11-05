# PaymentAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from mx_platform_python.models.payment_account import PaymentAccount

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAccount from a JSON string
payment_account_instance = PaymentAccount.from_json(json)
# print the JSON string representation of the object
print PaymentAccount.to_json()

# convert the object into a dict
payment_account_dict = payment_account_instance.to_dict()
# create an instance of PaymentAccount from a dict
payment_account_form_dict = payment_account.from_dict(payment_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


