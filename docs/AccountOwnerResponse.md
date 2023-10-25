# AccountOwnerResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**member_guid** | **str** |  | [optional] 
**owner_name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.account_owner_response import AccountOwnerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountOwnerResponse from a JSON string
account_owner_response_instance = AccountOwnerResponse.from_json(json)
# print the JSON string representation of the object
print AccountOwnerResponse.to_json()

# convert the object into a dict
account_owner_response_dict = account_owner_response_instance.to_dict()
# create an instance of AccountOwnerResponse from a dict
account_owner_response_form_dict = account_owner_response.from_dict(account_owner_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


