# TaggingUpdateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tagging** | [**TaggingUpdateRequest**](TaggingUpdateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.tagging_update_request_body import TaggingUpdateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of TaggingUpdateRequestBody from a JSON string
tagging_update_request_body_instance = TaggingUpdateRequestBody.from_json(json)
# print the JSON string representation of the object
print TaggingUpdateRequestBody.to_json()

# convert the object into a dict
tagging_update_request_body_dict = tagging_update_request_body_instance.to_dict()
# create an instance of TaggingUpdateRequestBody from a dict
tagging_update_request_body_form_dict = tagging_update_request_body.from_dict(tagging_update_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


