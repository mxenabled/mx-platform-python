# RepositionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **str** | The unique identifier for the goal. Defined by MX. | 
**position** | **int** | The priority of the goal in relation to multiple goals. | 

## Example

```python
from mx_platform_python.models.reposition_request import RepositionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RepositionRequest from a JSON string
reposition_request_instance = RepositionRequest.from_json(json)
# print the JSON string representation of the object
print RepositionRequest.to_json()

# convert the object into a dict
reposition_request_dict = reposition_request_instance.to_dict()
# create an instance of RepositionRequest from a dict
reposition_request_form_dict = reposition_request.from_dict(reposition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


