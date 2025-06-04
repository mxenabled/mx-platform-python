# MemberResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregated_at** | **str** |  | [optional] 
**background_aggregation_is_disabled** | **bool** |  | [optional] 
**connection_status** | **str** |  | [optional] 
**connection_status_message** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**institution_code** | **str** |  | [optional] 
**institution_guid** | **str** |  | [optional] 
**is_being_aggregated** | **bool** |  | [optional] 
**is_managed_by_user** | **bool** |  | [optional] 
**is_manual** | **bool** |  | [optional] 
**is_oauth** | **bool** |  | [optional] 
**metadata** | **str** |  | [optional] 
**most_recent_job_detail_code** | **int** |  | [optional] 
**most_recent_job_detail_text** | **bool** |  | [optional] 
**most_recent_job_guid** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**needs_updated_credentials** | **bool** |  | [optional] 
**oauth_window_uri** | **str** |  | [optional] 
**successfully_aggregated_at** | **str** |  | [optional] 
**use_cases** | **List[str]** | The use case associated with the member. Valid values are &#x60;PFM&#x60; and/or &#x60;MONEY_MOVEMENT&#x60;. Only set this if you&#39;ve met with MX and have opted in to using this field. | [optional] 
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


