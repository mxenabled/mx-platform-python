# RewardResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** |  | [optional] 
**balance_type** | **str** |  | [optional] 
**balance** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**expires_on** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**member_guid** | **str** |  | [optional] 
**unit_type** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.reward_response import RewardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RewardResponse from a JSON string
reward_response_instance = RewardResponse.from_json(json)
# print the JSON string representation of the object
print RewardResponse.to_json()

# convert the object into a dict
reward_response_dict = reward_response_instance.to_dict()
# create an instance of RewardResponse from a dict
reward_response_form_dict = reward_response.from_dict(reward_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


