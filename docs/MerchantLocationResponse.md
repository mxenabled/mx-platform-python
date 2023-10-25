# MerchantLocationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**merchant_guid** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**street_address** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.merchant_location_response import MerchantLocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantLocationResponse from a JSON string
merchant_location_response_instance = MerchantLocationResponse.from_json(json)
# print the JSON string representation of the object
print MerchantLocationResponse.to_json()

# convert the object into a dict
merchant_location_response_dict = merchant_location_response_instance.to_dict()
# create an instance of MerchantLocationResponse from a dict
merchant_location_response_form_dict = merchant_location_response.from_dict(merchant_location_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


