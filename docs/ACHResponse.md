# ACHResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** |  | [optional] 
**account_number_last_four** | **str** |  | [optional] 
**account_type** | **str** |  | [optional] 
**ach_initiated_at** | **str** |  | [optional] 
**client_guid** | **str** |  | [optional] 
**corrected_account_number** | **str** |  | [optional] 
**corrected_routing_number** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**institution_guid** | **str** |  | [optional] 
**investigation_notes** | **str** |  | [optional] 
**member_guid** | **str** |  | [optional] 
**processing_errors** | **str** |  | [optional] 
**resolution_code** | **str** |  | [optional] 
**resolution_detail** | **str** |  | [optional] 
**resolved_status_at** | **str** |  | [optional] 
**return_code** | **str** |  | [optional] 
**return_notes** | **str** |  | [optional] 
**return_account_number** | **str** |  | [optional] 
**return_routing_number** | **str** |  | [optional] 
**return_status** | **str** |  | [optional] 
**returned_at** | **str** |  | [optional] 
**sec_code** | **str** |  | [optional] 
**started_processing_at** | **str** |  | [optional] 
**submitted_at** | **str** |  | [optional] 
**transaction_amount** | **float** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.ach_response import ACHResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ACHResponse from a JSON string
ach_response_instance = ACHResponse.from_json(json)
# print the JSON string representation of the object
print ACHResponse.to_json()

# convert the object into a dict
ach_response_dict = ach_response_instance.to_dict()
# create an instance of ACHResponse from a dict
ach_response_form_dict = ach_response.from_dict(ach_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


