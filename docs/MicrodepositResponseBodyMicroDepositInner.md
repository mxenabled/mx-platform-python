# MicrodepositResponseBodyMicroDepositInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** |  | [optional] 
**account_number** | **str** |  | 
**account_type** | **str** |  | 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**routing_number** | **str** |  | 
**error_message** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**institution_code** | **str** |  | [optional] 
**institution_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**verified_at** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.microdeposit_response_body_micro_deposit_inner import MicrodepositResponseBodyMicroDepositInner

# TODO update the JSON string below
json = "{}"
# create an instance of MicrodepositResponseBodyMicroDepositInner from a JSON string
microdeposit_response_body_micro_deposit_inner_instance = MicrodepositResponseBodyMicroDepositInner.from_json(json)
# print the JSON string representation of the object
print MicrodepositResponseBodyMicroDepositInner.to_json()

# convert the object into a dict
microdeposit_response_body_micro_deposit_inner_dict = microdeposit_response_body_micro_deposit_inner_instance.to_dict()
# create an instance of MicrodepositResponseBodyMicroDepositInner from a dict
microdeposit_response_body_micro_deposit_inner_form_dict = microdeposit_response_body_micro_deposit_inner.from_dict(microdeposit_response_body_micro_deposit_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


