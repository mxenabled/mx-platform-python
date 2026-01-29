# InstitutionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**forgot_password_url** | **str** |  | [optional] 
**forgot_username_url** | **str** |  | [optional] 
**instructional_text** | **str** | Render this text when end users are asked for their credentials, as it helps end users provide the correct credentials when creating a new member. May contain &#x60;&lt;a&gt;&lt;/a&gt;&#x60; tags to link to explanatory material. | [optional] 
**instructional_text_steps** | **List[str]** | An array of instructional steps that may contain html elements. | [optional] 
**is_disabled_by_client** | **bool** |  | [optional] 
**iso_country_code** | **str** |  | [optional] 
**medium_logo_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**small_logo_url** | **str** |  | [optional] 
**supports_account_identification** | **bool** |  | [optional] 
**supports_account_statement** | **bool** |  | [optional] 
**supports_account_verification** | **bool** |  | [optional] 
**supports_oauth** | **bool** |  | [optional] 
**supports_tax_document** | **bool** |  | [optional] 
**supports_transaction_history** | **bool** |  | [optional] 
**trouble_signing_in_url** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.institution_response import InstitutionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstitutionResponse from a JSON string
institution_response_instance = InstitutionResponse.from_json(json)
# print the JSON string representation of the object
print InstitutionResponse.to_json()

# convert the object into a dict
institution_response_dict = institution_response_instance.to_dict()
# create an instance of InstitutionResponse from a dict
institution_response_form_dict = institution_response.from_dict(institution_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


