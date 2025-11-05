# ACHReturnCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** | The unique identifier for the account associated with the transaction. Defined by MX. | 
**account_number_last_four** | **str** | The last 4 digits of the account number used for the transaction by the Originating Depository Financial Institution (ODFI). | [optional] 
**ach_initiated_at** | **str** | The date and time when the transaction was initiated by the Originating Depository Financial Institution (ODFI) in ISO 8601 format without timestamp. | [optional] 
**corrected_account_number** | **str** | The account number correction reported by the RDFI. Populate only if the &#x60;resolution_code&#x60; is &#x60;NOTICE_OF_CHANGE&#x60;. | [optional] 
**corrected_routing_number** | **str** | The routing number correction reported by the RDFI. Populate only if the &#x60;resolution_code&#x60; is &#x60;NOTICE_OF_CHANGE&#x60;. Must be a valid 9-digit routing number format. | [optional] 
**id** | **str** | Client-defined identifier for this specific return submission. Allows you to track and reference you requests. | 
**member_guid** | **str** | The unique identifier for the member associated with the transaction. Defined by MX. | 
**return_account_number** | **str** | Incorrect account number used in the ACH transaction. | [optional] 
**return_code** | **str** | The associated ACH return code and notice of change code (for example, R02, R03, R04, R05, R20, NOC). See [Return Codes](/api-reference/platform-api/reference/ach-return-fields#return-codes) for a complete list. | 
**return_notes** | **str** | Notes that you set to inform MX on internal ACH processing. | [optional] 
**return_routing_number** | **str** | Incorrect routing number used in the ACH transaction. | [optional] 
**returned_at** | **str** | The date and time when the return was reported by the Receiving Financial Depository Institution (RDFI) in ISO 8601 format without timestamp. | [optional] 
**sec_code** | **str** | The SEC code (Standard Entry Class Code)–a three-letter code describing how a payment was authorized (for example, &#x60;WEB&#x60;). See [SEC Codes](/api-reference/platform-api/reference/ach-return-fields#sec-codes) for a complete list. | [optional] 
**transaction_amount** | **float** | The amount of the transaction. | [optional] 
**transaction_amount_range** | **float** | The transaction amount range, used for impact assessment. | [optional] 
**user_guid** | **str** | MX-defined identifier for the user associated with the ACH return. | 

## Example

```python
from mx_platform_python.models.ach_return_create_request import ACHReturnCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ACHReturnCreateRequest from a JSON string
ach_return_create_request_instance = ACHReturnCreateRequest.from_json(json)
# print the JSON string representation of the object
print ACHReturnCreateRequest.to_json()

# convert the object into a dict
ach_return_create_request_dict = ach_return_create_request_instance.to_dict()
# create an instance of ACHReturnCreateRequest from a dict
ach_return_create_request_form_dict = ach_return_create_request.from_dict(ach_return_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


