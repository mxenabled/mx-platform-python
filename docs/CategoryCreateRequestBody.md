# CategoryCreateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**CategoryCreateRequest**](CategoryCreateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.category_create_request_body import CategoryCreateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryCreateRequestBody from a JSON string
category_create_request_body_instance = CategoryCreateRequestBody.from_json(json)
# print the JSON string representation of the object
print CategoryCreateRequestBody.to_json()

# convert the object into a dict
category_create_request_body_dict = category_create_request_body_instance.to_dict()
# create an instance of CategoryCreateRequestBody from a dict
category_create_request_body_form_dict = category_create_request_body.from_dict(category_create_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


