# AccountNumberResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**loan_guarantor** | **str** |  | [optional] 
**institution_number** | **str** |  | [optional] 
**member_guid** | **str** |  | [optional] 
**passed_validation** | **bool** |  | [optional] 
**routing_number** | **str** |  | [optional] 
**transit_number** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.account_number_response import AccountNumberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountNumberResponse from a JSON string
account_number_response_instance = AccountNumberResponse.from_json(json)
# print the JSON string representation of the object
print AccountNumberResponse.to_json()

# convert the object into a dict
account_number_response_dict = account_number_response_instance.to_dict()
# create an instance of AccountNumberResponse from a dict
account_number_response_form_dict = account_number_response.from_dict(account_number_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


