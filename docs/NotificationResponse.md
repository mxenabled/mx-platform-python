# NotificationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guid** | **object** |  | [optional] 
**content** | **object** |  | [optional] 
**deep_link_guid** | **object** |  | [optional] 
**delivered_at** | **object** |  | [optional] 
**entity_guid** | **object** |  | [optional] 
**has_been_delivered** | **object** |  | [optional] 
**has_been_viewed** | **object** |  | [optional] 
**notification_type** | **object** |  | [optional] 
**subject** | **object** |  | [optional] 
**channel** | **object** |  | [optional] 

## Example

```python
from mx_platform_python.models.notification_response import NotificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationResponse from a JSON string
notification_response_instance = NotificationResponse.from_json(json)
# print the JSON string representation of the object
print NotificationResponse.to_json()

# convert the object into a dict
notification_response_dict = notification_response_instance.to_dict()
# create an instance of NotificationResponse from a dict
notification_response_form_dict = notification_response.from_dict(notification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


