# StatementsResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 
**statements** | [**List[StatementResponse]**](StatementResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.statements_response_body import StatementsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of StatementsResponseBody from a JSON string
statements_response_body_instance = StatementsResponseBody.from_json(json)
# print the JSON string representation of the object
print StatementsResponseBody.to_json()

# convert the object into a dict
statements_response_body_dict = statements_response_body_instance.to_dict()
# create an instance of StatementsResponseBody from a dict
statements_response_body_form_dict = statements_response_body.from_dict(statements_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


