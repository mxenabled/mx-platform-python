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

class AccountNumberResponse(BaseModel):
    """
    AccountNumberResponse
    """
    account_guid: Optional[StrictStr] = None
    account_number: Optional[StrictStr] = None
    guid: Optional[StrictStr] = None
    institution_number: Optional[StrictStr] = None
    member_guid: Optional[StrictStr] = None
    passed_validation: Optional[StrictBool] = None
    routing_number: Optional[StrictStr] = None
    transit_number: Optional[StrictStr] = None
    user_guid: Optional[StrictStr] = None
    __properties = ["account_guid", "account_number", "guid", "institution_number", "member_guid", "passed_validation", "routing_number", "transit_number", "user_guid"]

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
    def from_json(cls, json_str: str) -> AccountNumberResponse:
        """Create an instance of AccountNumberResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if account_guid (nullable) is None
        # and __fields_set__ contains the field
        if self.account_guid is None and "account_guid" in self.__fields_set__:
            _dict['account_guid'] = None

        # set to None if account_number (nullable) is None
        # and __fields_set__ contains the field
        if self.account_number is None and "account_number" in self.__fields_set__:
            _dict['account_number'] = None

        # set to None if guid (nullable) is None
        # and __fields_set__ contains the field
        if self.guid is None and "guid" in self.__fields_set__:
            _dict['guid'] = None

        # set to None if institution_number (nullable) is None
        # and __fields_set__ contains the field
        if self.institution_number is None and "institution_number" in self.__fields_set__:
            _dict['institution_number'] = None

        # set to None if member_guid (nullable) is None
        # and __fields_set__ contains the field
        if self.member_guid is None and "member_guid" in self.__fields_set__:
            _dict['member_guid'] = None

        # set to None if passed_validation (nullable) is None
        # and __fields_set__ contains the field
        if self.passed_validation is None and "passed_validation" in self.__fields_set__:
            _dict['passed_validation'] = None

        # set to None if routing_number (nullable) is None
        # and __fields_set__ contains the field
        if self.routing_number is None and "routing_number" in self.__fields_set__:
            _dict['routing_number'] = None

        # set to None if transit_number (nullable) is None
        # and __fields_set__ contains the field
        if self.transit_number is None and "transit_number" in self.__fields_set__:
            _dict['transit_number'] = None

        # set to None if user_guid (nullable) is None
        # and __fields_set__ contains the field
        if self.user_guid is None and "user_guid" in self.__fields_set__:
            _dict['user_guid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AccountNumberResponse:
        """Create an instance of AccountNumberResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccountNumberResponse.parse_obj(obj)

        _obj = AccountNumberResponse.parse_obj({
            "account_guid": obj.get("account_guid"),
            "account_number": obj.get("account_number"),
            "guid": obj.get("guid"),
            "institution_number": obj.get("institution_number"),
            "member_guid": obj.get("member_guid"),
            "passed_validation": obj.get("passed_validation"),
            "routing_number": obj.get("routing_number"),
            "transit_number": obj.get("transit_number"),
            "user_guid": obj.get("user_guid")
        })
        return _obj

