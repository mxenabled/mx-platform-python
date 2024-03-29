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
from pydantic import BaseModel, StrictInt

class PaginationResponse(BaseModel):
    """
    PaginationResponse
    """
    current_page: Optional[StrictInt] = None
    per_page: Optional[StrictInt] = None
    total_entries: Optional[StrictInt] = None
    total_pages: Optional[StrictInt] = None
    __properties = ["current_page", "per_page", "total_entries", "total_pages"]

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
    def from_json(cls, json_str: str) -> PaginationResponse:
        """Create an instance of PaginationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaginationResponse:
        """Create an instance of PaginationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaginationResponse.parse_obj(obj)

        _obj = PaginationResponse.parse_obj({
            "current_page": obj.get("current_page"),
            "per_page": obj.get("per_page"),
            "total_entries": obj.get("total_entries"),
            "total_pages": obj.get("total_pages")
        })
        return _obj


