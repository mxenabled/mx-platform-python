# PaymentAccountBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_account** | [**PaymentAccountBodyPaymentAccount**](PaymentAccountBodyPaymentAccount.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.payment_account_body import PaymentAccountBody

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentAccountBody from a JSON string
payment_account_body_instance = PaymentAccountBody.from_json(json)
# print the JSON string representation of the object
print PaymentAccountBody.to_json()

# convert the object into a dict
payment_account_body_dict = payment_account_body_instance.to_dict()
# create an instance of PaymentAccountBody from a dict
payment_account_body_form_dict = payment_account_body.from_dict(payment_account_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


