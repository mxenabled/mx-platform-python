# coding: utf-8

"""
    MX Platform API

    The MX Platform API is a powerful, fully-featured API designed to make aggregating and enhancing financial data easy and reliable. It can seamlessly connect your app or website to tens of thousands of financial institutions.

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr

class ConnectWidgetRequest(BaseModel):
    """
    ConnectWidgetRequest
    """
    client_redirect_url: Optional[StrictStr] = None
    color_scheme: Optional[StrictStr] = None
    current_institution_code: Optional[StrictStr] = None
    current_member_guid: Optional[StrictStr] = None
    disable_background_agg: Optional[StrictBool] = None
    disable_institution_search: Optional[StrictBool] = None
    include_identity: Optional[StrictBool] = None
    include_transactions: Optional[StrictBool] = None
    is_mobile_webview: Optional[StrictBool] = None
    mode: Optional[StrictStr] = None
    oauth_referral_source: Optional[StrictStr] = None
    ui_message_version: Optional[StrictInt] = None
    ui_message_webview_url_scheme: Optional[StrictStr] = None
    update_credentials: Optional[StrictBool] = None
    __properties = ["client_redirect_url", "color_scheme", "current_institution_code", "current_member_guid", "disable_background_agg", "disable_institution_search", "include_identity", "include_transactions", "is_mobile_webview", "mode", "oauth_referral_source", "ui_message_version", "ui_message_webview_url_scheme", "update_credentials"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ConnectWidgetRequest:
        """Create an instance of ConnectWidgetRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConnectWidgetRequest:
        """Create an instance of ConnectWidgetRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConnectWidgetRequest.parse_obj(obj)

        _obj = ConnectWidgetRequest.parse_obj({
            "client_redirect_url": obj.get("client_redirect_url"),
            "color_scheme": obj.get("color_scheme"),
            "current_institution_code": obj.get("current_institution_code"),
            "current_member_guid": obj.get("current_member_guid"),
            "disable_background_agg": obj.get("disable_background_agg"),
            "disable_institution_search": obj.get("disable_institution_search"),
            "include_identity": obj.get("include_identity"),
            "include_transactions": obj.get("include_transactions"),
            "is_mobile_webview": obj.get("is_mobile_webview"),
            "mode": obj.get("mode"),
            "oauth_referral_source": obj.get("oauth_referral_source"),
            "ui_message_version": obj.get("ui_message_version"),
            "ui_message_webview_url_scheme": obj.get("ui_message_webview_url_scheme"),
            "update_credentials": obj.get("update_credentials")
        })
        return _obj


