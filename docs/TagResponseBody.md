# TagResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | [**TagResponse**](TagResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.tag_response_body import TagResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of TagResponseBody from a JSON string
tag_response_body_instance = TagResponseBody.from_json(json)
# print the JSON string representation of the object
print TagResponseBody.to_json()

# convert the object into a dict
tag_response_body_dict = tag_response_body_instance.to_dict()
# create an instance of TagResponseBody from a dict
tag_response_body_form_dict = tag_response_body.from_dict(tag_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


