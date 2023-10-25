# MemberResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregated_at** | **str** |  | [optional] 
**background_aggregation_is_disabled** | **bool** |  | [optional] 
**connection_status** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**institution_code** | **str** |  | [optional] 
**is_being_aggregated** | **bool** |  | [optional] 
**is_managed_by_user** | **bool** |  | [optional] 
**is_oauth** | **bool** |  | [optional] 
**metadata** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**oauth_window_uri** | **str** |  | [optional] 
**successfully_aggregated_at** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.member_response import MemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemberResponse from a JSON string
member_response_instance = MemberResponse.from_json(json)
# print the JSON string representation of the object
print MemberResponse.to_json()

# convert the object into a dict
member_response_dict = member_response_instance.to_dict()
# create an instance of MemberResponse from a dict
member_response_form_dict = member_response.from_dict(member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


