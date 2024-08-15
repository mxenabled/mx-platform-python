# CreditCardProductResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_card_product** | [**CreditCardProduct**](CreditCardProduct.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.credit_card_product_response import CreditCardProductResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCardProductResponse from a JSON string
credit_card_product_response_instance = CreditCardProductResponse.from_json(json)
# print the JSON string representation of the object
print CreditCardProductResponse.to_json()

# convert the object into a dict
credit_card_product_response_dict = credit_card_product_response_instance.to_dict()
# create an instance of CreditCardProductResponse from a dict
credit_card_product_response_form_dict = credit_card_product_response.from_dict(credit_card_product_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


