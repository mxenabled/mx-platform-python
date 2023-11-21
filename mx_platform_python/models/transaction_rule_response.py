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

class TransactionRuleResponse(BaseModel):
    """
    TransactionRuleResponse
    """
    category_guid: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    guid: Optional[StrictStr] = None
    match_description: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    user_guid: Optional[StrictStr] = None
    __properties = ["category_guid", "created_at", "description", "guid", "match_description", "updated_at", "user_guid"]

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
    def from_json(cls, json_str: str) -> TransactionRuleResponse:
        """Create an instance of TransactionRuleResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if category_guid (nullable) is None
        # and __fields_set__ contains the field
        if self.category_guid is None and "category_guid" in self.__fields_set__:
            _dict['category_guid'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if guid (nullable) is None
        # and __fields_set__ contains the field
        if self.guid is None and "guid" in self.__fields_set__:
            _dict['guid'] = None

        # set to None if match_description (nullable) is None
        # and __fields_set__ contains the field
        if self.match_description is None and "match_description" in self.__fields_set__:
            _dict['match_description'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        # set to None if user_guid (nullable) is None
        # and __fields_set__ contains the field
        if self.user_guid is None and "user_guid" in self.__fields_set__:
            _dict['user_guid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransactionRuleResponse:
        """Create an instance of TransactionRuleResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionRuleResponse.parse_obj(obj)

        _obj = TransactionRuleResponse.parse_obj({
            "category_guid": obj.get("category_guid"),
            "created_at": obj.get("created_at"),
            "description": obj.get("description"),
            "guid": obj.get("guid"),
            "match_description": obj.get("match_description"),
            "updated_at": obj.get("updated_at"),
            "user_guid": obj.get("user_guid")
        })
        return _obj

