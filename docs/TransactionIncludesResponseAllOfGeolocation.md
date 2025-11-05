# TransactionIncludesResponseAllOfGeolocation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.transaction_includes_response_all_of_geolocation import TransactionIncludesResponseAllOfGeolocation

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionIncludesResponseAllOfGeolocation from a JSON string
transaction_includes_response_all_of_geolocation_instance = TransactionIncludesResponseAllOfGeolocation.from_json(json)
# print the JSON string representation of the object
print TransactionIncludesResponseAllOfGeolocation.to_json()

# convert the object into a dict
transaction_includes_response_all_of_geolocation_dict = transaction_includes_response_all_of_geolocation_instance.to_dict()
# create an instance of TransactionIncludesResponseAllOfGeolocation from a dict
transaction_includes_response_all_of_geolocation_form_dict = transaction_includes_response_all_of_geolocation.from_dict(transaction_includes_response_all_of_geolocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


