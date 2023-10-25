# StatementResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_guid** | **str** |  | [optional] 
**content_hash** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**member_guid** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.statement_response import StatementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StatementResponse from a JSON string
statement_response_instance = StatementResponse.from_json(json)
# print the JSON string representation of the object
print StatementResponse.to_json()

# convert the object into a dict
statement_response_dict = statement_response_instance.to_dict()
# create an instance of StatementResponse from a dict
statement_response_form_dict = statement_response.from_dict(statement_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


