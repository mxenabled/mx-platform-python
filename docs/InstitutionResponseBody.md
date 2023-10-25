# InstitutionResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institution** | [**InstitutionResponse**](InstitutionResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.institution_response_body import InstitutionResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of InstitutionResponseBody from a JSON string
institution_response_body_instance = InstitutionResponseBody.from_json(json)
# print the JSON string representation of the object
print InstitutionResponseBody.to_json()

# convert the object into a dict
institution_response_body_dict = institution_response_body_instance.to_dict()
# create an instance of InstitutionResponseBody from a dict
institution_response_body_form_dict = institution_response_body.from_dict(institution_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


