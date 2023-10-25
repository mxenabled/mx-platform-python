# MerchantResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant** | [**MerchantResponse**](MerchantResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.merchant_response_body import MerchantResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantResponseBody from a JSON string
merchant_response_body_instance = MerchantResponseBody.from_json(json)
# print the JSON string representation of the object
print MerchantResponseBody.to_json()

# convert the object into a dict
merchant_response_body_dict = merchant_response_body_instance.to_dict()
# create an instance of MerchantResponseBody from a dict
merchant_response_body_form_dict = merchant_response_body.from_dict(merchant_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


