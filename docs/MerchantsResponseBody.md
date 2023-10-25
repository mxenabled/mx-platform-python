# MerchantsResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchants** | [**List[MerchantResponse]**](MerchantResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.merchants_response_body import MerchantsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantsResponseBody from a JSON string
merchants_response_body_instance = MerchantsResponseBody.from_json(json)
# print the JSON string representation of the object
print MerchantsResponseBody.to_json()

# convert the object into a dict
merchants_response_body_dict = merchants_response_body_instance.to_dict()
# create an instance of MerchantsResponseBody from a dict
merchants_response_body_form_dict = merchants_response_body.from_dict(merchants_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


