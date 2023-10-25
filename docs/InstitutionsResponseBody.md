# InstitutionsResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institutions** | [**List[InstitutionResponse]**](InstitutionResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.institutions_response_body import InstitutionsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of InstitutionsResponseBody from a JSON string
institutions_response_body_instance = InstitutionsResponseBody.from_json(json)
# print the JSON string representation of the object
print InstitutionsResponseBody.to_json()

# convert the object into a dict
institutions_response_body_dict = institutions_response_body_instance.to_dict()
# create an instance of InstitutionsResponseBody from a dict
institutions_response_body_form_dict = institutions_response_body.from_dict(institutions_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


