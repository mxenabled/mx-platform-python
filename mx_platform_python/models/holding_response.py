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
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr

class HoldingResponse(BaseModel):
    """
    HoldingResponse
    """
    account_guid: Optional[StrictStr] = None
    cost_basis: Optional[Union[StrictFloat, StrictInt]] = None
    created_at: Optional[StrictStr] = None
    currency_code: Optional[StrictStr] = None
    cusip: Optional[StrictStr] = None
    daily_change: Optional[Union[StrictFloat, StrictInt]] = None
    description: Optional[StrictStr] = None
    guid: Optional[StrictStr] = None
    holding_type: Optional[StrictStr] = None
    holding_type_id: Optional[StrictInt] = None
    id: Optional[StrictStr] = None
    market_value: Optional[Union[StrictFloat, StrictInt]] = None
    member_guid: Optional[StrictStr] = None
    metadata: Optional[StrictStr] = None
    purchase_price: Optional[Union[StrictFloat, StrictInt]] = None
    shares: Optional[Union[StrictFloat, StrictInt]] = None
    symbol: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    user_guid: Optional[StrictStr] = None
    __properties = ["account_guid", "cost_basis", "created_at", "currency_code", "cusip", "daily_change", "description", "guid", "holding_type", "holding_type_id", "id", "market_value", "member_guid", "metadata", "purchase_price", "shares", "symbol", "updated_at", "user_guid"]

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
    def from_json(cls, json_str: str) -> HoldingResponse:
        """Create an instance of HoldingResponse from a JSON string"""
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

        # set to None if cost_basis (nullable) is None
        # and __fields_set__ contains the field
        if self.cost_basis is None and "cost_basis" in self.__fields_set__:
            _dict['cost_basis'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if currency_code (nullable) is None
        # and __fields_set__ contains the field
        if self.currency_code is None and "currency_code" in self.__fields_set__:
            _dict['currency_code'] = None

        # set to None if cusip (nullable) is None
        # and __fields_set__ contains the field
        if self.cusip is None and "cusip" in self.__fields_set__:
            _dict['cusip'] = None

        # set to None if daily_change (nullable) is None
        # and __fields_set__ contains the field
        if self.daily_change is None and "daily_change" in self.__fields_set__:
            _dict['daily_change'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if guid (nullable) is None
        # and __fields_set__ contains the field
        if self.guid is None and "guid" in self.__fields_set__:
            _dict['guid'] = None

        # set to None if holding_type (nullable) is None
        # and __fields_set__ contains the field
        if self.holding_type is None and "holding_type" in self.__fields_set__:
            _dict['holding_type'] = None

        # set to None if holding_type_id (nullable) is None
        # and __fields_set__ contains the field
        if self.holding_type_id is None and "holding_type_id" in self.__fields_set__:
            _dict['holding_type_id'] = None

        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if market_value (nullable) is None
        # and __fields_set__ contains the field
        if self.market_value is None and "market_value" in self.__fields_set__:
            _dict['market_value'] = None

        # set to None if member_guid (nullable) is None
        # and __fields_set__ contains the field
        if self.member_guid is None and "member_guid" in self.__fields_set__:
            _dict['member_guid'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        # set to None if purchase_price (nullable) is None
        # and __fields_set__ contains the field
        if self.purchase_price is None and "purchase_price" in self.__fields_set__:
            _dict['purchase_price'] = None

        # set to None if shares (nullable) is None
        # and __fields_set__ contains the field
        if self.shares is None and "shares" in self.__fields_set__:
            _dict['shares'] = None

        # set to None if symbol (nullable) is None
        # and __fields_set__ contains the field
        if self.symbol is None and "symbol" in self.__fields_set__:
            _dict['symbol'] = None

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
    def from_dict(cls, obj: dict) -> HoldingResponse:
        """Create an instance of HoldingResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HoldingResponse.parse_obj(obj)

        _obj = HoldingResponse.parse_obj({
            "account_guid": obj.get("account_guid"),
            "cost_basis": obj.get("cost_basis"),
            "created_at": obj.get("created_at"),
            "currency_code": obj.get("currency_code"),
            "cusip": obj.get("cusip"),
            "daily_change": obj.get("daily_change"),
            "description": obj.get("description"),
            "guid": obj.get("guid"),
            "holding_type": obj.get("holding_type"),
            "holding_type_id": obj.get("holding_type_id"),
            "id": obj.get("id"),
            "market_value": obj.get("market_value"),
            "member_guid": obj.get("member_guid"),
            "metadata": obj.get("metadata"),
            "purchase_price": obj.get("purchase_price"),
            "shares": obj.get("shares"),
            "symbol": obj.get("symbol"),
            "updated_at": obj.get("updated_at"),
            "user_guid": obj.get("user_guid")
        })
        return _obj


