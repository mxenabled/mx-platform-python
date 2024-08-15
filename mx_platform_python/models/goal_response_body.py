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
from pydantic import BaseModel
from mx_platform_python.models.goal_response import GoalResponse

class GoalResponseBody(BaseModel):
    """
    GoalResponseBody
    """
    goal: Optional[GoalResponse] = None
    __properties = ["goal"]

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
    def from_json(cls, json_str: str) -> GoalResponseBody:
        """Create an instance of GoalResponseBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of goal
        if self.goal:
            _dict['goal'] = self.goal.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GoalResponseBody:
        """Create an instance of GoalResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GoalResponseBody.parse_obj(obj)

        _obj = GoalResponseBody.parse_obj({
            "goal": GoalResponse.from_dict(obj.get("goal")) if obj.get("goal") is not None else None
        })
        return _obj


