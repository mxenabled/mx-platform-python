# TaggingCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag_guid** | **str** |  | 
**transaction_guid** | **str** |  | 

## Example

```python
from mx_platform_python.models.tagging_create_request import TaggingCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaggingCreateRequest from a JSON string
tagging_create_request_instance = TaggingCreateRequest.from_json(json)
# print the JSON string representation of the object
print TaggingCreateRequest.to_json()

# convert the object into a dict
tagging_create_request_dict = tagging_create_request_instance.to_dict()
# create an instance of TaggingCreateRequest from a dict
tagging_create_request_form_dict = tagging_create_request.from_dict(tagging_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


