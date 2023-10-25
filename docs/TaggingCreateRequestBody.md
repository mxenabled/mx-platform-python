# TaggingCreateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tagging** | [**TaggingCreateRequest**](TaggingCreateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.tagging_create_request_body import TaggingCreateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of TaggingCreateRequestBody from a JSON string
tagging_create_request_body_instance = TaggingCreateRequestBody.from_json(json)
# print the JSON string representation of the object
print TaggingCreateRequestBody.to_json()

# convert the object into a dict
tagging_create_request_body_dict = tagging_create_request_body_instance.to_dict()
# create an instance of TaggingCreateRequestBody from a dict
tagging_create_request_body_form_dict = tagging_create_request_body.from_dict(tagging_create_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


