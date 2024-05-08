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


from typing import Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr

class ScheduledPaymentResponse(BaseModel):
    """
    ScheduledPaymentResponse
    """
    amount: Optional[Union[StrictFloat, StrictInt]] = None
    created_at: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    guid: Optional[StrictStr] = None
    is_completed: Optional[StrictBool] = None
    is_recurring: Optional[StrictBool] = None
    merchant_guid: Optional[StrictStr] = None
    occurs_on: Optional[StrictStr] = None
    recurrence_day: Optional[StrictInt] = None
    recurrence_type: Optional[StrictStr] = None
    transaction_type: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    user_guid: Optional[StrictStr] = None
    __properties = ["amount", "created_at", "description", "guid", "is_completed", "is_recurring", "merchant_guid", "occurs_on", "recurrence_day", "recurrence_type", "transaction_type", "updated_at", "user_guid"]

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
    def from_json(cls, json_str: str) -> ScheduledPaymentResponse:
        """Create an instance of ScheduledPaymentResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ScheduledPaymentResponse:
        """Create an instance of ScheduledPaymentResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ScheduledPaymentResponse.parse_obj(obj)

        _obj = ScheduledPaymentResponse.parse_obj({
            "amount": obj.get("amount"),
            "created_at": obj.get("created_at"),
            "description": obj.get("description"),
            "guid": obj.get("guid"),
            "is_completed": obj.get("is_completed"),
            "is_recurring": obj.get("is_recurring"),
            "merchant_guid": obj.get("merchant_guid"),
            "occurs_on": obj.get("occurs_on"),
            "recurrence_day": obj.get("recurrence_day"),
            "recurrence_type": obj.get("recurrence_type"),
            "transaction_type": obj.get("transaction_type"),
            "updated_at": obj.get("updated_at"),
            "user_guid": obj.get("user_guid")
        })
        return _obj


