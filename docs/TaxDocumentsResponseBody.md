# TaxDocumentsResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 
**tax_documents** | [**List[TaxDocumentResponse]**](TaxDocumentResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.tax_documents_response_body import TaxDocumentsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of TaxDocumentsResponseBody from a JSON string
tax_documents_response_body_instance = TaxDocumentsResponseBody.from_json(json)
# print the JSON string representation of the object
print TaxDocumentsResponseBody.to_json()

# convert the object into a dict
tax_documents_response_body_dict = tax_documents_response_body_instance.to_dict()
# create an instance of TaxDocumentsResponseBody from a dict
tax_documents_response_body_form_dict = tax_documents_response_body.from_dict(tax_documents_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


