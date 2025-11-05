# NotificationsResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notifications** | [**List[NotificationResponse]**](NotificationResponse.md) |  | [optional] 

## Example

```python
from mx_platform_python.models.notifications_response_body import NotificationsResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsResponseBody from a JSON string
notifications_response_body_instance = NotificationsResponseBody.from_json(json)
# print the JSON string representation of the object
print NotificationsResponseBody.to_json()

# convert the object into a dict
notifications_response_body_dict = notifications_response_body_instance.to_dict()
# create an instance of NotificationsResponseBody from a dict
notifications_response_body_form_dict = notifications_response_body.from_dict(notifications_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


