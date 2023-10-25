# StatementResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statement** | [**StatementResponse**](StatementResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.statement_response_body import StatementResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of StatementResponseBody from a JSON string
statement_response_body_instance = StatementResponseBody.from_json(json)
# print the JSON string representation of the object
print StatementResponseBody.to_json()

# convert the object into a dict
statement_response_body_dict = statement_response_body_instance.to_dict()
# create an instance of StatementResponseBody from a dict
statement_response_body_form_dict = statement_response_body.from_dict(statement_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


