# TaggingResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | [optional] 
**member_is_managed_by_user** | **bool** |  | [optional] 
**tag_guid** | **str** |  | [optional] 
**transaction_guid** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.tagging_response import TaggingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaggingResponse from a JSON string
tagging_response_instance = TaggingResponse.from_json(json)
# print the JSON string representation of the object
print TaggingResponse.to_json()

# convert the object into a dict
tagging_response_dict = tagging_response_instance.to_dict()
# create an instance of TaggingResponse from a dict
tagging_response_form_dict = tagging_response.from_dict(tagging_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


