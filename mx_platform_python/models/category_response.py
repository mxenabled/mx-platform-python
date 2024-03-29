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
from pydantic import BaseModel, StrictBool, StrictStr

class CategoryResponse(BaseModel):
    """
    CategoryResponse
    """
    created_at: Optional[StrictStr] = None
    guid: Optional[StrictStr] = None
    is_default: Optional[StrictBool] = None
    is_income: Optional[StrictBool] = None
    metadata: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    parent_guid: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties = ["created_at", "guid", "is_default", "is_income", "metadata", "name", "parent_guid", "updated_at"]

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
    def from_json(cls, json_str: str) -> CategoryResponse:
        """Create an instance of CategoryResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if guid (nullable) is None
        # and __fields_set__ contains the field
        if self.guid is None and "guid" in self.__fields_set__:
            _dict['guid'] = None

        # set to None if is_default (nullable) is None
        # and __fields_set__ contains the field
        if self.is_default is None and "is_default" in self.__fields_set__:
            _dict['is_default'] = None

        # set to None if is_income (nullable) is None
        # and __fields_set__ contains the field
        if self.is_income is None and "is_income" in self.__fields_set__:
            _dict['is_income'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if parent_guid (nullable) is None
        # and __fields_set__ contains the field
        if self.parent_guid is None and "parent_guid" in self.__fields_set__:
            _dict['parent_guid'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CategoryResponse:
        """Create an instance of CategoryResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CategoryResponse.parse_obj(obj)

        _obj = CategoryResponse.parse_obj({
            "created_at": obj.get("created_at"),
            "guid": obj.get("guid"),
            "is_default": obj.get("is_default"),
            "is_income": obj.get("is_income"),
            "metadata": obj.get("metadata"),
            "name": obj.get("name"),
            "parent_guid": obj.get("parent_guid"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


