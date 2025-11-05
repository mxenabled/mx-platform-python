# WidgetRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_redirect_url** | **str** | Only use this option if the &#x60;widget_type&#x60; is set to &#x60;connect_widget&#x60;. This determines the redirect destination at the end of OAuth when used with &#x60;is_mobile_webview: true&#x60; or &#x60;oauth_referral_source: &#39;APP&#39;&#x60;.  | [optional] 
**color_scheme** | **str** | This option can be passed to any &#x60;widget_type&#x60; but will not affect [legacy PFM widgets](products/experience/pfm/legacy-widget-overviews/). Load the widget with the specified &#x60;color_scheme&#x60;; options are &#x60;light&#x60;, &#x60;browser&#x60; (respects user&#39;s browser setting), and &#x60;dark&#x60;. Defaults to &#x60;light&#x60;. | [optional] 
**connections_use_case_filter** | **bool** | To use this parameter, you must also set &#x60;use_cases&#x60; in the same request. If &#x60;connections_use_case_filter&#x60; is set to &#x60;true&#x60;, the Connections Widget will only show connections (members) with the &#x60;use_cases&#x60; you set in the same request. For some examples, see [Filter Connections](/products/experience/pfm/widget-overviews/connections-widget#example-1). | [optional] 
**current_institution_code** | **str** | Only use this option if the &#x60;widget_type&#x60; is set to &#x60;connect_widget&#x60;. Load the widget into the credential view for the specified institution.  | [optional] 
**current_institution_guid** | **str** | Only use this option if the &#x60;widget_type&#x60; is set to &#x60;connect_widget&#x60;. Load the widget into the credential view for the specified institution.  | [optional] 
**current_member_guid** | **str** | Only use this option if the &#x60;widget_type&#x60; is set to &#x60;connect_widget&#x60;. Load the widget into a specific member that contains an error or requires multifactor authentication. The widget will determine the best view to load based on the member&#39;s current state. &#x60;current_member_guid&#x60; takes precedence over &#x60;current_institution_code&#x60; and &#x60;current_institution_guid&#x60;.  | [optional] 
**disable_background_agg** | **bool** | Only use this option if the &#x60;widget_type&#x60; is set to &#x60;connect_widget&#x60;. This determines whether background aggregation is enabled or disabled for the member created by the Connect Widget. Defaults to &#x60;false&#x60; in &#x60;aggregation&#x60; mode and &#x60;true&#x60; in &#x60;verification&#x60; mode. A global default for all members can be set by reaching out to MX.  | [optional] 
**disable_institution_search** | **bool** | Only use this option if the &#x60;widget_type&#x60; is set to &#x60;connect_widget&#x60;. This determines whether the institution search is displayed within the Connect Widget. This option must be used with &#x60;current_institution_code&#x60;, &#x60;current_instituion_guid&#x60;, or &#x60;current_member_guid&#x60;. When set to &#x60;true&#x60;, the institution search feature will be disabled and end users will not be able to navigate to it. Defaults to &#x60;false&#x60;.  | [optional] 
**enable_app2app** | **bool** | Only use this option if the &#x60;widget_type&#x60; is set to &#x60;connect_widget&#x60;. This indicates whether OAuth app2app behavior is enabled for institutions that support it. Defaults to &#x60;true&#x60;. When set to &#x60;false&#x60;, the widget will **not** direct the end user to the institution&#39;s mobile application. This setting is not persistent. This setting currently only affects Chase institutions.  | [optional] 
**include_identity** | **bool** | Only use this option if the &#x60;widget_type&#x60; is set to &#x60;connect_widget&#x60;. This determines whether an account owner identification (AOI, previously called identity verification) is run in addition to the process specified by the &#x60;mode&#x60;. Defaults to &#x60;false&#x60;. This can be set in either &#x60;aggregation&#x60; or &#x60;verification&#x60; mode. The AOI runs after the primary process is complete.  | [optional] 
**include_transactions** | **bool** | Only use this option if the &#x60;widget_type&#x60; is set to &#x60;connect_widget&#x60;. This determines whether transaction data are retrieved. Defaults to &#x60;true&#x60; in aggregation mode and &#x60;false&#x60; in verification mode. This can be set in either &#x60;aggregation&#x60; or &#x60;verification&#x60; mode. This option does not affect future foreground or background aggregations.  | [optional] 
**insight_guid** | **str** | Only use this option if the &#x60;widget_type&#x60; is set to &#x60;pulse_widget&#x60;. Set this to the insight guid you want to appear at the top of the insights feed.  | [optional] 
**iso_country_code** | **List[str]** | An array of strings that filters institutions in the widget by the specified country code. Acceptable codes include &#x60;US&#x60;, &#x60;CA&#x60;, and &#x60;MX&#x60; (Mexico).  | [optional] 
**is_mobile_webview** | **bool** | This option is for all &#x60;widget_type&#x60;s. This configures the widget to render in a mobile WebView. JavaScript event postMessages are replaced with URL updates.  | [optional] 
**microwidget_instance_id** | **str** | Only use this option if the &#x60;widget_type&#x60; is set to &#x60;micro_pulse_carousel_widget&#x60;. Set this to a unique value for each instance of the Micro Widget. This lets us collect unique data for each instance of the widget.  | [optional] 
**mode** | **str** | Only use this option if the &#x60;widget_type&#x60; is set to &#x60;connect_widget&#x60;. &#x60;mode&#x60; is the most important option for the Connect Widget. This determines what kind of process Connect will run, which affects how you should set many other options. Defaults to &#x60;aggregation&#x60;. &#x60;aggregation&#x60; mode retrieves account and transaction data; in other words, this runs a standard aggregation. &#x60;verification&#x60; mode retrieves account numbers and routing/transit numbers; in other words, it runs an Instant Account Verification (IAV). By default, verification mode does not retrieve transaction data; this default can be modified with secondary options. By default, background aggregation is disabled for all members created in verification mode; this default can be modified with secondary options.  | [optional] 
**oauth_referral_source** | **str** | Only use this option if the &#x60;widget_type&#x60; is set to &#x60;connect_widget&#x60;. This determines how MX will respond to the result of an OAuth flow. When set to &#x60;APP&#x60;, MX will redirect to the URI specified in the &#x60;ui_message_webview_url_scheme&#x60;. When set to &#x60;BROWSER&#x60;, MX will send a postMessage but not redirect. If &#x60;is_mobile_webview&#x60; is &#x60;true&#x60;, this defaults to &#x60;APP&#x60;. If false, it defaults to &#x60;BROWSER&#x60;.  | [optional] 
**ui_message_version** | **int** | This option is for all &#x60;widget_type&#x60;s. This determines which version of postMessage events are triggered. Defaults to 4. All new implementations must use version 4. Prior versions are deprecated.  | [optional] 
**ui_message_webview_url_scheme** | **str** | Only use this option if the &#x60;widget_type&#x60; is set to &#x60;connect_widget&#x60;. This is a client-defined scheme used in OAuth redirects in WebViews; also used in URL updates when these replace postMessages in WebViews. Defaults to &#x60;mx&#x60;.  | [optional] 
**update_credentials** | **bool** | Only use this option if the &#x60;widget_type&#x60; is set to &#x60;connect_widget&#x60;. Load the widget into a view that allows them to update the current member. Optionally used with &#x60;current_member_guid&#x60;. This option should be used sparingly. The best practice is to use &#x60;current_member_guid&#x60; and let the widget resolve the issue.  | [optional] 
**use_cases** | **List[str]** | The use case that will be associated with any members created through the widget. Valid values are &#x60;PFM&#x60; and/or &#x60;MONEY_MOVEMENT&#x60;. This is **required** if you&#39;ve met with MX, opted in to using this field, and are requesting a widget with a &#x60;widget_type&#x60; of &#x60;connect_widget&#x60; or &#x60;connections_widget&#x60;. | [optional] 
**widget_type** | **str** | This determines which widget URL you&#39;ll receive.  See [Widget Types](/api-reference/platform-api/reference/widget-types) for a list of potential values. Additional request parameters may only apply to some widget types.  | 

## Example

```python
from mx_platform_python.models.widget_request import WidgetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetRequest from a JSON string
widget_request_instance = WidgetRequest.from_json(json)
# print the JSON string representation of the object
print WidgetRequest.to_json()

# convert the object into a dict
widget_request_dict = widget_request_instance.to_dict()
# create an instance of WidgetRequest from a dict
widget_request_form_dict = widget_request.from_dict(widget_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


