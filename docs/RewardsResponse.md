# RewardsResponse


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
**updated_at** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.rewards_response import RewardsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RewardsResponse from a JSON string
rewards_response_instance = RewardsResponse.from_json(json)
# print the JSON string representation of the object
print RewardsResponse.to_json()

# convert the object into a dict
rewards_response_dict = rewards_response_instance.to_dict()
# create an instance of RewardsResponse from a dict
rewards_response_form_dict = rewards_response.from_dict(rewards_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


