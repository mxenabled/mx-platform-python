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

class WidgetResponse(BaseModel):
    """
    WidgetResponse
    """
    type: Optional[StrictStr] = None
    url: Optional[StrictStr] = None
    user_id: Optional[StrictStr] = None
    __properties = ["type", "url", "user_id"]

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
    def from_json(cls, json_str: str) -> WidgetResponse:
        """Create an instance of WidgetResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if url (nullable) is None
        # and __fields_set__ contains the field
        if self.url is None and "url" in self.__fields_set__:
            _dict['url'] = None

        # set to None if user_id (nullable) is None
        # and __fields_set__ contains the field
        if self.user_id is None and "user_id" in self.__fields_set__:
            _dict['user_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WidgetResponse:
        """Create an instance of WidgetResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WidgetResponse.parse_obj(obj)

        _obj = WidgetResponse.parse_obj({
            "type": obj.get("type"),
            "url": obj.get("url"),
            "user_id": obj.get("user_id")
        })
        return _obj


