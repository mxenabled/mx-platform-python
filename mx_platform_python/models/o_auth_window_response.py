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
from pydantic import BaseModel, StrictStr

class OAuthWindowResponse(BaseModel):
    """
    OAuthWindowResponse
    """
    guid: Optional[StrictStr] = None
    oauth_window_uri: Optional[StrictStr] = None
    __properties = ["guid", "oauth_window_uri"]

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
    def from_json(cls, json_str: str) -> OAuthWindowResponse:
        """Create an instance of OAuthWindowResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if guid (nullable) is None
        # and __fields_set__ contains the field
        if self.guid is None and "guid" in self.__fields_set__:
            _dict['guid'] = None

        # set to None if oauth_window_uri (nullable) is None
        # and __fields_set__ contains the field
        if self.oauth_window_uri is None and "oauth_window_uri" in self.__fields_set__:
            _dict['oauth_window_uri'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OAuthWindowResponse:
        """Create an instance of OAuthWindowResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OAuthWindowResponse.parse_obj(obj)

        _obj = OAuthWindowResponse.parse_obj({
            "guid": obj.get("guid"),
            "oauth_window_uri": obj.get("oauth_window_uri")
        })
        return _obj


