# CreditCardProduct


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annual_fee** | **object** |  | [optional] 
**duration_of_introductory_rate_on_balance_transfer** | **object** |  | [optional] 
**duration_of_introductory_rate_on_purchases** | **object** |  | [optional] 
**guid** | **object** |  | [optional] 
**has_cashback_rewards** | **bool** |  | [optional] 
**has_other_rewards** | **bool** |  | [optional] 
**has_travel_rewards** | **bool** |  | [optional] 
**has_zero_introductory_annual_fee** | **bool** |  | [optional] 
**has_zero_percent_introductory_rate** | **bool** |  | [optional] 
**has_zero_percent_introductory_rate_on_balance_transfer** | **bool** |  | [optional] 
**financial_institution** | **bool** |  | [optional] 
**is_accepting_applications** | **bool** |  | [optional] 
**is_small_business_card** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.credit_card_product import CreditCardProduct

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCardProduct from a JSON string
credit_card_product_instance = CreditCardProduct.from_json(json)
# print the JSON string representation of the object
print CreditCardProduct.to_json()

# convert the object into a dict
credit_card_product_dict = credit_card_product_instance.to_dict()
# create an instance of CreditCardProduct from a dict
credit_card_product_form_dict = credit_card_product.from_dict(credit_card_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


