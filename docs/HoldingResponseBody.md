# HoldingResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holding** | [**HoldingResponse**](HoldingResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.holding_response_body import HoldingResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of HoldingResponseBody from a JSON string
holding_response_body_instance = HoldingResponseBody.from_json(json)
# print the JSON string representation of the object
print HoldingResponseBody.to_json()

# convert the object into a dict
holding_response_body_dict = holding_response_body_instance.to_dict()
# create an instance of HoldingResponseBody from a dict
holding_response_body_form_dict = holding_response_body.from_dict(holding_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


