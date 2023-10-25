# TagUpdateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | [**TagUpdateRequest**](TagUpdateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.tag_update_request_body import TagUpdateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of TagUpdateRequestBody from a JSON string
tag_update_request_body_instance = TagUpdateRequestBody.from_json(json)
# print the JSON string representation of the object
print TagUpdateRequestBody.to_json()

# convert the object into a dict
tag_update_request_body_dict = tag_update_request_body_instance.to_dict()
# create an instance of TagUpdateRequestBody from a dict
tag_update_request_body_form_dict = tag_update_request_body.from_dict(tag_update_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


