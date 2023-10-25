# CategoryUpdateRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**CategoryUpdateRequest**](CategoryUpdateRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.category_update_request_body import CategoryUpdateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryUpdateRequestBody from a JSON string
category_update_request_body_instance = CategoryUpdateRequestBody.from_json(json)
# print the JSON string representation of the object
print CategoryUpdateRequestBody.to_json()

# convert the object into a dict
category_update_request_body_dict = category_update_request_body_instance.to_dict()
# create an instance of CategoryUpdateRequestBody from a dict
category_update_request_body_form_dict = category_update_request_body.from_dict(category_update_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


