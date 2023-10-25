# ChallengesResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**challenges** | [**List[ChallengeResponse]**](ChallengeResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.challenges_response_body import ChallengesResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ChallengesResponseBody from a JSON string
challenges_response_body_instance = ChallengesResponseBody.from_json(json)
# print the JSON string representation of the object
print ChallengesResponseBody.to_json()

# convert the object into a dict
challenges_response_body_dict = challenges_response_body_instance.to_dict()
# create an instance of ChallengesResponseBody from a dict
challenges_response_body_form_dict = challenges_response_body.from_dict(challenges_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


