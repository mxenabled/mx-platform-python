# RepositionResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goals** | [**List[GoalsResponse]**](GoalsResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.reposition_response_body import RepositionResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of RepositionResponseBody from a JSON string
reposition_response_body_instance = RepositionResponseBody.from_json(json)
# print the JSON string representation of the object
print RepositionResponseBody.to_json()

# convert the object into a dict
reposition_response_body_dict = reposition_response_body_instance.to_dict()
# create an instance of RepositionResponseBody from a dict
reposition_response_body_form_dict = reposition_response_body.from_dict(reposition_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


