# CategoryCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **str** |  | [optional] 
**name** | **str** |  | 
**parent_guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.category_create_request import CategoryCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryCreateRequest from a JSON string
category_create_request_instance = CategoryCreateRequest.from_json(json)
# print the JSON string representation of the object
print CategoryCreateRequest.to_json()

# convert the object into a dict
category_create_request_dict = category_create_request_instance.to_dict()
# create an instance of CategoryCreateRequest from a dict
category_create_request_form_dict = category_create_request.from_dict(category_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


