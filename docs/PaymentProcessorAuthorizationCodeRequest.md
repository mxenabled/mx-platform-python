# PaymentProcessorAuthorizationCodeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** |  | 
**member_guid** | **str** |  | 
**user_guid** | **str** |  | 

## Example

```python
from mx_platform_python.models.payment_processor_authorization_code_request import PaymentProcessorAuthorizationCodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentProcessorAuthorizationCodeRequest from a JSON string
payment_processor_authorization_code_request_instance = PaymentProcessorAuthorizationCodeRequest.from_json(json)
# print the JSON string representation of the object
print PaymentProcessorAuthorizationCodeRequest.to_json()

# convert the object into a dict
payment_processor_authorization_code_request_dict = payment_processor_authorization_code_request_instance.to_dict()
# create an instance of PaymentProcessorAuthorizationCodeRequest from a dict
payment_processor_authorization_code_request_form_dict = payment_processor_authorization_code_request.from_dict(payment_processor_authorization_code_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


