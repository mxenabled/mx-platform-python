# SpendingPlanIterationsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iterations** | [**List[SpendingPlanIterationResponse]**](SpendingPlanIterationResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.spending_plan_iterations_response import SpendingPlanIterationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SpendingPlanIterationsResponse from a JSON string
spending_plan_iterations_response_instance = SpendingPlanIterationsResponse.from_json(json)
# print the JSON string representation of the object
print SpendingPlanIterationsResponse.to_json()

# convert the object into a dict
spending_plan_iterations_response_dict = spending_plan_iterations_response_instance.to_dict()
# create an instance of SpendingPlanIterationsResponse from a dict
spending_plan_iterations_response_form_dict = spending_plan_iterations_response.from_dict(spending_plan_iterations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


