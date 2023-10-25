# TaxDocumentResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_hash** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**document_type** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**issued_on** | **str** |  | [optional] 
**member_guid** | **str** |  | [optional] 
**tax_year** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.tax_document_response import TaxDocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaxDocumentResponse from a JSON string
tax_document_response_instance = TaxDocumentResponse.from_json(json)
# print the JSON string representation of the object
print TaxDocumentResponse.to_json()

# convert the object into a dict
tax_document_response_dict = tax_document_response_instance.to_dict()
# create an instance of TaxDocumentResponse from a dict
tax_document_response_form_dict = tax_document_response.from_dict(tax_document_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


