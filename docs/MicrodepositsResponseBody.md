# MicrodepositsResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**micro_deposits** | [**List[MicrodepositResponse]**](MicrodepositResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.microdeposits_response_body import MicrodepositsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of MicrodepositsResponseBody from a JSON string
microdeposits_response_body_instance = MicrodepositsResponseBody.from_json(json)
# print the JSON string representation of the object
print MicrodepositsResponseBody.to_json()

# convert the object into a dict
microdeposits_response_body_dict = microdeposits_response_body_instance.to_dict()
# create an instance of MicrodepositsResponseBody from a dict
microdeposits_response_body_form_dict = microdeposits_response_body.from_dict(microdeposits_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


