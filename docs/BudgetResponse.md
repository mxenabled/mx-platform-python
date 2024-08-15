# BudgetResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | A goal amount set by the user for a category&#39;s transaction total during a month. | [optional] 
**category_guid** | **str** | Unique identifier for the budget category. Defined by MX. | [optional] 
**created_at** | **str** | Date and time the budget was created, represented in ISO 8601 format with timestamp. | [optional] 
**guid** | **str** | Unique identifier for the budget. Defined by MX. | [optional] 
**is_exceeded** | **bool** | If the budget has been exceeded, this field will be true. Otherwise, this field will be false. | [optional] 
**is_off_track** | **bool** | If the budget is off track, this field will be true. Otherwise, this field will be false. | [optional] 
**metadata** | **str** | Additional information a partner can store on the budget. | [optional] 
**name** | **str** | The name of the budget that is visible to the user (ie \&quot;Food\&quot;, \&quot;Bills\&quot;, \&quot;Entertainment\&quot;, etc). | [optional] 
**off_track_percentage** | **float** | The percentage amount of off track spending. (Deprecated). | [optional] 
**parent_guid** | **str** | Unique identifier for the parent budget. Defined by MX. | [optional] 
**percent_spent** | **float** | The percentage of a budget that has been spent during the current calendar month Calculated as the transaction total divided by the amount and then multiplied by 100.A value of zero will be returned when &#x60;amount&#x60; is zero. | [optional] 
**projected_spending** | **float** | The projected amount of spending for the budget. | [optional] 
**revision** | **int** | The revision number of this budget record. | [optional] 
**transaction_total** | **object** | The cumulative amount of all transactions under the budget. | [optional] 
**updated_at** | **object** | Date and time the budget was updated, represented in ISO 8601 format with timestamp. | [optional] 
**user_guid** | **object** | Unique identifier for the user. Defined by MX. | [optional] 

## Example

```python
from mx_platform_python.models.budget_response import BudgetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetResponse from a JSON string
budget_response_instance = BudgetResponse.from_json(json)
# print the JSON string representation of the object
print BudgetResponse.to_json()

# convert the object into a dict
budget_response_dict = budget_response_instance.to_dict()
# create an instance of BudgetResponse from a dict
budget_response_form_dict = budget_response.from_dict(budget_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


