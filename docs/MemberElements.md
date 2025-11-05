# MemberElements


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** |  | [optional] 
**member_guid** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.member_elements import MemberElements

# TODO update the JSON string below
json = "{}"
# create an instance of MemberElements from a JSON string
member_elements_instance = MemberElements.from_json(json)
# print the JSON string representation of the object
print MemberElements.to_json()

# convert the object into a dict
member_elements_dict = member_elements_instance.to_dict()
# create an instance of MemberElements from a dict
member_elements_form_dict = member_elements.from_dict(member_elements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


