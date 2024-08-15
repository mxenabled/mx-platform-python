# RepositionRequestBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goals** | [**List[RepositionRequest]**](RepositionRequest.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.reposition_request_body import RepositionRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of RepositionRequestBody from a JSON string
reposition_request_body_instance = RepositionRequestBody.from_json(json)
# print the JSON string representation of the object
print RepositionRequestBody.to_json()

# convert the object into a dict
reposition_request_body_dict = reposition_request_body_instance.to_dict()
# create an instance of RepositionRequestBody from a dict
reposition_request_body_form_dict = reposition_request_body.from_dict(reposition_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


