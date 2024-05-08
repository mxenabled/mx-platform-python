# ScheduledPaymentResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**guid** | **str** |  | [optional] 
**is_completed** | **bool** |  | [optional] 
**is_recurring** | **bool** |  | [optional] 
**merchant_guid** | **str** |  | [optional] 
**occurs_on** | **str** |  | [optional] 
**recurrence_day** | **int** |  | [optional] 
**recurrence_type** | **str** |  | [optional] 
**transaction_type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**user_guid** | **str** |  | [optional] 

## Example

```python
from mx_platform_python.models.scheduled_payment_response import ScheduledPaymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledPaymentResponse from a JSON string
scheduled_payment_response_instance = ScheduledPaymentResponse.from_json(json)
# print the JSON string representation of the object
print ScheduledPaymentResponse.to_json()

# convert the object into a dict
scheduled_payment_response_dict = scheduled_payment_response_instance.to_dict()
# create an instance of ScheduledPaymentResponse from a dict
scheduled_payment_response_form_dict = scheduled_payment_response.from_dict(scheduled_payment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


