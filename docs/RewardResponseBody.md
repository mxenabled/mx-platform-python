# RewardResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reward** | [**RewardsResponseBodyRewardsInner**](RewardsResponseBodyRewardsInner.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.reward_response_body import RewardResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of RewardResponseBody from a JSON string
reward_response_body_instance = RewardResponseBody.from_json(json)
# print the JSON string representation of the object
print RewardResponseBody.to_json()

# convert the object into a dict
reward_response_body_dict = reward_response_body_instance.to_dict()
# create an instance of RewardResponseBody from a dict
reward_response_body_form_dict = reward_response_body.from_dict(reward_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


