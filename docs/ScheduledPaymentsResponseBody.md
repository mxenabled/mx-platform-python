# ScheduledPaymentsResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled_payments** | [**List[ScheduledPaymentResponse]**](ScheduledPaymentResponse.md) |  | [optional] 
**pagination** | [**PaginationResponse**](PaginationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.scheduled_payments_response_body import ScheduledPaymentsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledPaymentsResponseBody from a JSON string
scheduled_payments_response_body_instance = ScheduledPaymentsResponseBody.from_json(json)
# print the JSON string representation of the object
print ScheduledPaymentsResponseBody.to_json()

# convert the object into a dict
scheduled_payments_response_body_dict = scheduled_payments_response_body_instance.to_dict()
# create an instance of ScheduledPaymentsResponseBody from a dict
scheduled_payments_response_body_form_dict = scheduled_payments_response_body.from_dict(scheduled_payments_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


