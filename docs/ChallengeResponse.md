# ChallengeResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**image_data** | **str** |  | [optional] 
**image_options** | [**List[ImageOptionResponse]**](ImageOptionResponse.md) |  | [optional] 
**label** | **str** |  | [optional] 
**options** | [**List[OptionResponse]**](OptionResponse.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.challenge_response import ChallengeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChallengeResponse from a JSON string
challenge_response_instance = ChallengeResponse.from_json(json)
# print the JSON string representation of the object
print ChallengeResponse.to_json()

# convert the object into a dict
challenge_response_dict = challenge_response_instance.to_dict()
# create an instance of ChallengeResponse from a dict
challenge_response_form_dict = challenge_response.from_dict(challenge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


