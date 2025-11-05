# RewardsResponseBodyRewardsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** |  | [optional] 
**member_guid** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 
**balance_type** | **str** |  | [optional] 
**balance** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**expires_on** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**unit_type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.rewards_response_body_rewards_inner import RewardsResponseBodyRewardsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RewardsResponseBodyRewardsInner from a JSON string
rewards_response_body_rewards_inner_instance = RewardsResponseBodyRewardsInner.from_json(json)
# print the JSON string representation of the object
print RewardsResponseBodyRewardsInner.to_json()

# convert the object into a dict
rewards_response_body_rewards_inner_dict = rewards_response_body_rewards_inner_instance.to_dict()
# create an instance of RewardsResponseBodyRewardsInner from a dict
rewards_response_body_rewards_inner_form_dict = rewards_response_body_rewards_inner.from_dict(rewards_response_body_rewards_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


