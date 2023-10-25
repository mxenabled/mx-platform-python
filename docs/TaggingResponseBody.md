# TaggingResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tagging** | [**TaggingResponse**](TaggingResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.tagging_response_body import TaggingResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of TaggingResponseBody from a JSON string
tagging_response_body_instance = TaggingResponseBody.from_json(json)
# print the JSON string representation of the object
print TaggingResponseBody.to_json()

# convert the object into a dict
tagging_response_body_dict = tagging_response_body_instance.to_dict()
# create an instance of TaggingResponseBody from a dict
tagging_response_body_form_dict = tagging_response_body.from_dict(tagging_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


