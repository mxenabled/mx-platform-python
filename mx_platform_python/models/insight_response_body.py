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


from typing import List, Optional
from pydantic import BaseModel, conlist
from mx_platform_python.models.insight_response import InsightResponse

class InsightResponseBody(BaseModel):
    """
    InsightResponseBody
    """
    insight: Optional[conlist(InsightResponse)] = None
    __properties = ["insight"]

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
    def from_json(cls, json_str: str) -> InsightResponseBody:
        """Create an instance of InsightResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in insight (list)
        _items = []
        if self.insight:
            for _item in self.insight:
                if _item:
                    _items.append(_item.to_dict())
            _dict['insight'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InsightResponseBody:
        """Create an instance of InsightResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InsightResponseBody.parse_obj(obj)

        _obj = InsightResponseBody.parse_obj({
            "insight": [InsightResponse.from_dict(_item) for _item in obj.get("insight")] if obj.get("insight") is not None else None
        })
        return _obj


