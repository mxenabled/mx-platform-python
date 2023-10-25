# SpendingPlansResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iteration_items** | [**List[SpendingPlanResponse]**](SpendingPlanResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.spending_plans_response_body import SpendingPlansResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of SpendingPlansResponseBody from a JSON string
spending_plans_response_body_instance = SpendingPlansResponseBody.from_json(json)
# print the JSON string representation of the object
print SpendingPlansResponseBody.to_json()

# convert the object into a dict
spending_plans_response_body_dict = spending_plans_response_body_instance.to_dict()
# create an instance of SpendingPlansResponseBody from a dict
spending_plans_response_body_form_dict = spending_plans_response_body.from_dict(spending_plans_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


