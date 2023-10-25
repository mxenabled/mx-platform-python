# CategoryUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.category_update_request import CategoryUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryUpdateRequest from a JSON string
category_update_request_instance = CategoryUpdateRequest.from_json(json)
# print the JSON string representation of the object
print CategoryUpdateRequest.to_json()

# convert the object into a dict
category_update_request_dict = category_update_request_instance.to_dict()
# create an instance of CategoryUpdateRequest from a dict
category_update_request_form_dict = category_update_request.from_dict(category_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


