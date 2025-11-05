# VCResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verifiable_credential** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.vc_response import VCResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VCResponse from a JSON string
vc_response_instance = VCResponse.from_json(json)
# print the JSON string representation of the object
print VCResponse.to_json()

# convert the object into a dict
vc_response_dict = vc_response_instance.to_dict()
# create an instance of VCResponse from a dict
vc_response_form_dict = vc_response.from_dict(vc_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


