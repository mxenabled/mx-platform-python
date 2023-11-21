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

class SpendingPlanAccountResponse(BaseModel):
    """
    SpendingPlanAccountResponse
    """
    account_guid: Optional[StrictStr] = None
    client_guid: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = None
    guid: Optional[StrictStr] = None
    spending_plan_guid: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    user_guid: Optional[StrictStr] = None
    __properties = ["account_guid", "client_guid", "created_at", "guid", "spending_plan_guid", "updated_at", "user_guid"]

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
    def from_json(cls, json_str: str) -> SpendingPlanAccountResponse:
        """Create an instance of SpendingPlanAccountResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SpendingPlanAccountResponse:
        """Create an instance of SpendingPlanAccountResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SpendingPlanAccountResponse.parse_obj(obj)

        _obj = SpendingPlanAccountResponse.parse_obj({
            "account_guid": obj.get("account_guid"),
            "client_guid": obj.get("client_guid"),
            "created_at": obj.get("created_at"),
            "guid": obj.get("guid"),
            "spending_plan_guid": obj.get("spending_plan_guid"),
            "updated_at": obj.get("updated_at"),
            "user_guid": obj.get("user_guid")
        })
        return _obj

