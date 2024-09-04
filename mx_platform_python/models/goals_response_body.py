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
from mx_platform_python.models.goals_response import GoalsResponse
from mx_platform_python.models.pagination_response import PaginationResponse

class GoalsResponseBody(BaseModel):
    """
    GoalsResponseBody
    """
    goals: Optional[conlist(GoalsResponse)] = None
    pagination: Optional[PaginationResponse] = None
    __properties = ["goals", "pagination"]

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
    def from_json(cls, json_str: str) -> GoalsResponseBody:
        """Create an instance of GoalsResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in goals (list)
        _items = []
        if self.goals:
            for _item in self.goals:
                if _item:
                    _items.append(_item.to_dict())
            _dict['goals'] = _items
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict['pagination'] = self.pagination.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GoalsResponseBody:
        """Create an instance of GoalsResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GoalsResponseBody.parse_obj(obj)

        _obj = GoalsResponseBody.parse_obj({
            "goals": [GoalsResponse.from_dict(_item) for _item in obj.get("goals")] if obj.get("goals") is not None else None,
            "pagination": PaginationResponse.from_dict(obj.get("pagination")) if obj.get("pagination") is not None else None
        })
        return _obj

