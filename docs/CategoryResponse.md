# CategoryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | Category creation date-time. | [optional] 
**guid** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**is_income** | **bool** |  | [optional] 
**metadata** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**parent_guid** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.category_response import CategoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryResponse from a JSON string
category_response_instance = CategoryResponse.from_json(json)
# print the JSON string representation of the object
print CategoryResponse.to_json()

# convert the object into a dict
category_response_dict = category_response_instance.to_dict()
# create an instance of CategoryResponse from a dict
category_response_form_dict = category_response.from_dict(category_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


