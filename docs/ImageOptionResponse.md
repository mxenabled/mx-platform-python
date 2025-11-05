# ImageOptionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_uri** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.image_option_response import ImageOptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageOptionResponse from a JSON string
image_option_response_instance = ImageOptionResponse.from_json(json)
# print the JSON string representation of the object
print ImageOptionResponse.to_json()

# convert the object into a dict
image_option_response_dict = image_option_response_instance.to_dict()
# create an instance of ImageOptionResponse from a dict
image_option_response_form_dict = image_option_response.from_dict(image_option_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


