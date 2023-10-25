# HoldingsResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**holdings** | [**List[HoldingResponse]**](HoldingResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.holdings_response_body import HoldingsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of HoldingsResponseBody from a JSON string
holdings_response_body_instance = HoldingsResponseBody.from_json(json)
# print the JSON string representation of the object
print HoldingsResponseBody.to_json()

# convert the object into a dict
holdings_response_body_dict = holdings_response_body_instance.to_dict()
# create an instance of HoldingsResponseBody from a dict
holdings_response_body_form_dict = holdings_response_body.from_dict(holdings_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


