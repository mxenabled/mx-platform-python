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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr

class SpendingPlanIterationItemCreateRequestBody(BaseModel):
    """
    SpendingPlanIterationItemCreateRequestBody
    """
    category_guid: Optional[StrictStr] = None
    item_type: Optional[Union[StrictFloat, StrictInt]] = None
    planned_amount: Union[StrictFloat, StrictInt] = Field(...)
    scheduled_payment_guid: Optional[StrictStr] = None
    top_level_category_guid: Optional[StrictStr] = None
    __properties = ["category_guid", "item_type", "planned_amount", "scheduled_payment_guid", "top_level_category_guid"]

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
    def from_json(cls, json_str: str) -> SpendingPlanIterationItemCreateRequestBody:
        """Create an instance of SpendingPlanIterationItemCreateRequestBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SpendingPlanIterationItemCreateRequestBody:
        """Create an instance of SpendingPlanIterationItemCreateRequestBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SpendingPlanIterationItemCreateRequestBody.parse_obj(obj)

        _obj = SpendingPlanIterationItemCreateRequestBody.parse_obj({
            "category_guid": obj.get("category_guid"),
            "item_type": obj.get("item_type"),
            "planned_amount": obj.get("planned_amount"),
            "scheduled_payment_guid": obj.get("scheduled_payment_guid"),
            "top_level_category_guid": obj.get("top_level_category_guid")
        })
        return _obj

