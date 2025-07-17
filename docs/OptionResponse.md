# OptionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.option_response import OptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OptionResponse from a JSON string
option_response_instance = OptionResponse.from_json(json)
# print the JSON string representation of the object
print OptionResponse.to_json()

# convert the object into a dict
option_response_dict = option_response_instance.to_dict()
# create an instance of OptionResponse from a dict
option_response_form_dict = option_response.from_dict(option_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


