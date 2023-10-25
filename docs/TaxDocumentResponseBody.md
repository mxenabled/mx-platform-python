# TaxDocumentResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_document** | [**TaxDocumentResponse**](TaxDocumentResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.tax_document_response_body import TaxDocumentResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of TaxDocumentResponseBody from a JSON string
tax_document_response_body_instance = TaxDocumentResponseBody.from_json(json)
# print the JSON string representation of the object
print TaxDocumentResponseBody.to_json()

# convert the object into a dict
tax_document_response_body_dict = tax_document_response_body_instance.to_dict()
# create an instance of TaxDocumentResponseBody from a dict
tax_document_response_body_form_dict = tax_document_response_body.from_dict(tax_document_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


