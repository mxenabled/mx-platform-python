# PaymentProcessorAuthorizationCodeRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_processor_authorization_code** | [**PaymentProcessorAuthorizationCodeRequest**](PaymentProcessorAuthorizationCodeRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.payment_processor_authorization_code_request_body import PaymentProcessorAuthorizationCodeRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentProcessorAuthorizationCodeRequestBody from a JSON string
payment_processor_authorization_code_request_body_instance = PaymentProcessorAuthorizationCodeRequestBody.from_json(json)
# print the JSON string representation of the object
print PaymentProcessorAuthorizationCodeRequestBody.to_json()

# convert the object into a dict
payment_processor_authorization_code_request_body_dict = payment_processor_authorization_code_request_body_instance.to_dict()
# create an instance of PaymentProcessorAuthorizationCodeRequestBody from a dict
payment_processor_authorization_code_request_body_form_dict = payment_processor_authorization_code_request_body.from_dict(payment_processor_authorization_code_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


