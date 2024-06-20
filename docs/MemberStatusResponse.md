# MemberStatusResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregated_at** | **str** |  | [optional] 
**challenges** | [**List[ChallengeResponse]**](ChallengeResponse.md) |  | [optional] 
**connection_status** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**has_processed_accounts** | **bool** |  | [optional] 
**has_processed_account_numbers** | **bool** |  | [optional] 
**has_processed_transactions** | **bool** |  | [optional] 
**is_authenticated** | **bool** |  | [optional] 
**is_being_aggregated** | **bool** |  | [optional] 
**successfully_aggregated_at** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.member_status_response import MemberStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberStatusResponse from a JSON string
member_status_response_instance = MemberStatusResponse.from_json(json)
# print the JSON string representation of the object
print MemberStatusResponse.to_json()

# convert the object into a dict
member_status_response_dict = member_status_response_instance.to_dict()
# create an instance of MemberStatusResponse from a dict
member_status_response_form_dict = member_status_response.from_dict(member_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


