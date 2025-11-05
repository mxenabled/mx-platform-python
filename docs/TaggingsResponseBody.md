# TaggingsResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taggings** | [**List[TaggingResponse]**](TaggingResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.taggings_response_body import TaggingsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of TaggingsResponseBody from a JSON string
taggings_response_body_instance = TaggingsResponseBody.from_json(json)
# print the JSON string representation of the object
print TaggingsResponseBody.to_json()

# convert the object into a dict
taggings_response_body_dict = taggings_response_body_instance.to_dict()
# create an instance of TaggingsResponseBody from a dict
taggings_response_body_form_dict = taggings_response_body.from_dict(taggings_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


