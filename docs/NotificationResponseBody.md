# NotificationResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification** | [**NotificationResponse**](NotificationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.notification_response_body import NotificationResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationResponseBody from a JSON string
notification_response_body_instance = NotificationResponseBody.from_json(json)
# print the JSON string representation of the object
print NotificationResponseBody.to_json()

# convert the object into a dict
notification_response_body_dict = notification_response_body_instance.to_dict()
# create an instance of NotificationResponseBody from a dict
notification_response_body_form_dict = notification_response_body.from_dict(notification_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


