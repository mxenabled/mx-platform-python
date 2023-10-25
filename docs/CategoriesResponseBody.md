# CategoriesResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[CategoryResponse]**](CategoryResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.categories_response_body import CategoriesResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of CategoriesResponseBody from a JSON string
categories_response_body_instance = CategoriesResponseBody.from_json(json)
# print the JSON string representation of the object
print CategoriesResponseBody.to_json()

# convert the object into a dict
categories_response_body_dict = categories_response_body_instance.to_dict()
# create an instance of CategoriesResponseBody from a dict
categories_response_body_form_dict = categories_response_body.from_dict(categories_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


