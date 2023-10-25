# PaymentProcessorAuthorizationCodeResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_code** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.payment_processor_authorization_code_response import PaymentProcessorAuthorizationCodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentProcessorAuthorizationCodeResponse from a JSON string
payment_processor_authorization_code_response_instance = PaymentProcessorAuthorizationCodeResponse.from_json(json)
# print the JSON string representation of the object
print PaymentProcessorAuthorizationCodeResponse.to_json()

# convert the object into a dict
payment_processor_authorization_code_response_dict = payment_processor_authorization_code_response_instance.to_dict()
# create an instance of PaymentProcessorAuthorizationCodeResponse from a dict
payment_processor_authorization_code_response_form_dict = payment_processor_authorization_code_response.from_dict(payment_processor_authorization_code_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


