# MerchantResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.merchant_response import MerchantResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantResponse from a JSON string
merchant_response_instance = MerchantResponse.from_json(json)
# print the JSON string representation of the object
print MerchantResponse.to_json()

# convert the object into a dict
merchant_response_dict = merchant_response_instance.to_dict()
# create an instance of MerchantResponse from a dict
merchant_response_form_dict = merchant_response.from_dict(merchant_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


