# MerchantLocationResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_location** | [**MerchantLocationResponse**](MerchantLocationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.merchant_location_response_body import MerchantLocationResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantLocationResponseBody from a JSON string
merchant_location_response_body_instance = MerchantLocationResponseBody.from_json(json)
# print the JSON string representation of the object
print MerchantLocationResponseBody.to_json()

# convert the object into a dict
merchant_location_response_body_dict = merchant_location_response_body_instance.to_dict()
# create an instance of MerchantLocationResponseBody from a dict
merchant_location_response_body_form_dict = merchant_location_response_body.from_dict(merchant_location_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


