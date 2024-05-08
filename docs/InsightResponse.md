# InsightResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_at** | **str** |  | [optional] 
**client_guid** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**cta_clicked_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**has_associated_accounts** | **bool** |  | [optional] 
**has_associated_merchants** | **bool** |  | [optional] 
**has_associated_scheduled_payments** | **bool** |  | [optional] 
**has_associated_transactions** | **bool** |  | [optional] 
**has_been_displayed** | **bool** |  | [optional] 
**is_dismissed** | **bool** |  | [optional] 
**micro_call_to_action** | **str** |  | [optional] 
**micro_description** | **str** |  | [optional] 
**micro_title** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 
**user_id** | **object** |  | [optional] 

## Example

```python
from mx_platform_python.models.insight_response import InsightResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InsightResponse from a JSON string
insight_response_instance = InsightResponse.from_json(json)
# print the JSON string representation of the object
print InsightResponse.to_json()

# convert the object into a dict
insight_response_dict = insight_response_instance.to_dict()
# create an instance of InsightResponse from a dict
insight_response_form_dict = insight_response.from_dict(insight_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


