# RewardsResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rewards** | [**List[RewardsResponse]**](RewardsResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.rewards_response_body import RewardsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of RewardsResponseBody from a JSON string
rewards_response_body_instance = RewardsResponseBody.from_json(json)
# print the JSON string representation of the object
print RewardsResponseBody.to_json()

# convert the object into a dict
rewards_response_body_dict = rewards_response_body_instance.to_dict()
# create an instance of RewardsResponseBody from a dict
rewards_response_body_form_dict = rewards_response_body.from_dict(rewards_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


