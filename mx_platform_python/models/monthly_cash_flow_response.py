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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr

class MonthlyCashFlowResponse(BaseModel):
    """
    MonthlyCashFlowResponse
    """
    guid: Optional[StrictStr] = Field(None, description="Unique identifier for the monthly cash flow profile. Defined by MX.")
    user_guid: Optional[StrictStr] = Field(None, description="Unique identifier for the user the monthly cash flow profile is attached to. Defined by MX.")
    budgeted_income: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The amount of the budgeted income for the user.")
    budgeted_expenses: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The amount of the budgeted expenses for the user.")
    goals_contribution: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The monthly dollar amount allocated for goals.")
    estimated_goals_contribution: Optional[StrictInt] = Field(None, description="The estimated monthly dollar amount allocated for goals calculated from income and budgets.")
    uses_estimated_goals_contribution: Optional[StrictBool] = None
    __properties = ["guid", "user_guid", "budgeted_income", "budgeted_expenses", "goals_contribution", "estimated_goals_contribution", "uses_estimated_goals_contribution"]

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
    def from_json(cls, json_str: str) -> MonthlyCashFlowResponse:
        """Create an instance of MonthlyCashFlowResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MonthlyCashFlowResponse:
        """Create an instance of MonthlyCashFlowResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MonthlyCashFlowResponse.parse_obj(obj)

        _obj = MonthlyCashFlowResponse.parse_obj({
            "guid": obj.get("guid"),
            "user_guid": obj.get("user_guid"),
            "budgeted_income": obj.get("budgeted_income"),
            "budgeted_expenses": obj.get("budgeted_expenses"),
            "goals_contribution": obj.get("goals_contribution"),
            "estimated_goals_contribution": obj.get("estimated_goals_contribution"),
            "uses_estimated_goals_contribution": obj.get("uses_estimated_goals_contribution")
        })
        return _obj


