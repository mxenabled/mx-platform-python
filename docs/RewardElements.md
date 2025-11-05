# RewardElements


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from mx_platform_python.models.reward_elements import RewardElements

# TODO update the JSON string below
json = "{}"
# create an instance of RewardElements from a JSON string
reward_elements_instance = RewardElements.from_json(json)
# print the JSON string representation of the object
print RewardElements.to_json()

# convert the object into a dict
reward_elements_dict = reward_elements_instance.to_dict()
# create an instance of RewardElements from a dict
reward_elements_form_dict = reward_elements.from_dict(reward_elements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


