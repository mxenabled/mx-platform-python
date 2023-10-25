# PaginationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | [optional] 
**per_page** | **int** |  | [optional] 
**total_entries** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 

## Example

```python
from mx_platform_python.models.pagination_response import PaginationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationResponse from a JSON string
pagination_response_instance = PaginationResponse.from_json(json)
# print the JSON string representation of the object
print PaginationResponse.to_json()

# convert the object into a dict
pagination_response_dict = pagination_response_instance.to_dict()
# create an instance of PaginationResponse from a dict
pagination_response_form_dict = pagination_response.from_dict(pagination_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


