# TagCreateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | [**TagCreateRequest**](TagCreateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.tag_create_request_body import TagCreateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of TagCreateRequestBody from a JSON string
tag_create_request_body_instance = TagCreateRequestBody.from_json(json)
# print the JSON string representation of the object
print TagCreateRequestBody.to_json()

# convert the object into a dict
tag_create_request_body_dict = tag_create_request_body_instance.to_dict()
# create an instance of TagCreateRequestBody from a dict
tag_create_request_body_form_dict = tag_create_request_body.from_dict(tag_create_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


