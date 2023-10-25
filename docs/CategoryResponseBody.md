# CategoryResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**CategoryResponse**](CategoryResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.category_response_body import CategoryResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryResponseBody from a JSON string
category_response_body_instance = CategoryResponseBody.from_json(json)
# print the JSON string representation of the object
print CategoryResponseBody.to_json()

# convert the object into a dict
category_response_body_dict = category_response_body_instance.to_dict()
# create an instance of CategoryResponseBody from a dict
category_response_body_form_dict = category_response_body.from_dict(category_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


