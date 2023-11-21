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

class EnhanceTransactionResponse(BaseModel):
    """
    EnhanceTransactionResponse
    """
    amount: Optional[Union[StrictFloat, StrictInt]] = None
    categorized_by: Optional[StrictInt] = None
    category: Optional[StrictStr] = None
    category_guid: Optional[StrictStr] = None
    described_by: Optional[StrictInt] = None
    description: Optional[StrictStr] = None
    extended_transaction_type: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    is_bill_pay: Optional[StrictBool] = None
    is_direct_deposit: Optional[StrictBool] = None
    is_expense: Optional[StrictBool] = None
    is_fee: Optional[StrictBool] = None
    is_income: Optional[StrictBool] = None
    is_international: Optional[StrictBool] = None
    is_overdraft_fee: Optional[StrictBool] = None
    is_payroll_advance: Optional[StrictBool] = None
    is_subscription: Optional[StrictBool] = None
    memo: Optional[StrictStr] = None
    merchant_category_code: Optional[StrictInt] = None
    merchant_guid: Optional[StrictStr] = None
    merchant_location_guid: Optional[StrictStr] = None
    original_description: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    __properties = ["amount", "categorized_by", "category", "category_guid", "described_by", "description", "extended_transaction_type", "id", "is_bill_pay", "is_direct_deposit", "is_expense", "is_fee", "is_income", "is_international", "is_overdraft_fee", "is_payroll_advance", "is_subscription", "memo", "merchant_category_code", "merchant_guid", "merchant_location_guid", "original_description", "type"]

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
    def from_json(cls, json_str: str) -> EnhanceTransactionResponse:
        """Create an instance of EnhanceTransactionResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if amount (nullable) is None
        # and __fields_set__ contains the field
        if self.amount is None and "amount" in self.__fields_set__:
            _dict['amount'] = None

        # set to None if categorized_by (nullable) is None
        # and __fields_set__ contains the field
        if self.categorized_by is None and "categorized_by" in self.__fields_set__:
            _dict['categorized_by'] = None

        # set to None if category (nullable) is None
        # and __fields_set__ contains the field
        if self.category is None and "category" in self.__fields_set__:
            _dict['category'] = None

        # set to None if category_guid (nullable) is None
        # and __fields_set__ contains the field
        if self.category_guid is None and "category_guid" in self.__fields_set__:
            _dict['category_guid'] = None

        # set to None if described_by (nullable) is None
        # and __fields_set__ contains the field
        if self.described_by is None and "described_by" in self.__fields_set__:
            _dict['described_by'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if extended_transaction_type (nullable) is None
        # and __fields_set__ contains the field
        if self.extended_transaction_type is None and "extended_transaction_type" in self.__fields_set__:
            _dict['extended_transaction_type'] = None

        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if is_bill_pay (nullable) is None
        # and __fields_set__ contains the field
        if self.is_bill_pay is None and "is_bill_pay" in self.__fields_set__:
            _dict['is_bill_pay'] = None

        # set to None if is_direct_deposit (nullable) is None
        # and __fields_set__ contains the field
        if self.is_direct_deposit is None and "is_direct_deposit" in self.__fields_set__:
            _dict['is_direct_deposit'] = None

        # set to None if is_expense (nullable) is None
        # and __fields_set__ contains the field
        if self.is_expense is None and "is_expense" in self.__fields_set__:
            _dict['is_expense'] = None

        # set to None if is_fee (nullable) is None
        # and __fields_set__ contains the field
        if self.is_fee is None and "is_fee" in self.__fields_set__:
            _dict['is_fee'] = None

        # set to None if is_income (nullable) is None
        # and __fields_set__ contains the field
        if self.is_income is None and "is_income" in self.__fields_set__:
            _dict['is_income'] = None

        # set to None if is_international (nullable) is None
        # and __fields_set__ contains the field
        if self.is_international is None and "is_international" in self.__fields_set__:
            _dict['is_international'] = None

        # set to None if is_overdraft_fee (nullable) is None
        # and __fields_set__ contains the field
        if self.is_overdraft_fee is None and "is_overdraft_fee" in self.__fields_set__:
            _dict['is_overdraft_fee'] = None

        # set to None if is_payroll_advance (nullable) is None
        # and __fields_set__ contains the field
        if self.is_payroll_advance is None and "is_payroll_advance" in self.__fields_set__:
            _dict['is_payroll_advance'] = None

        # set to None if is_subscription (nullable) is None
        # and __fields_set__ contains the field
        if self.is_subscription is None and "is_subscription" in self.__fields_set__:
            _dict['is_subscription'] = None

        # set to None if memo (nullable) is None
        # and __fields_set__ contains the field
        if self.memo is None and "memo" in self.__fields_set__:
            _dict['memo'] = None

        # set to None if merchant_category_code (nullable) is None
        # and __fields_set__ contains the field
        if self.merchant_category_code is None and "merchant_category_code" in self.__fields_set__:
            _dict['merchant_category_code'] = None

        # set to None if merchant_guid (nullable) is None
        # and __fields_set__ contains the field
        if self.merchant_guid is None and "merchant_guid" in self.__fields_set__:
            _dict['merchant_guid'] = None

        # set to None if merchant_location_guid (nullable) is None
        # and __fields_set__ contains the field
        if self.merchant_location_guid is None and "merchant_location_guid" in self.__fields_set__:
            _dict['merchant_location_guid'] = None

        # set to None if original_description (nullable) is None
        # and __fields_set__ contains the field
        if self.original_description is None and "original_description" in self.__fields_set__:
            _dict['original_description'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EnhanceTransactionResponse:
        """Create an instance of EnhanceTransactionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EnhanceTransactionResponse.parse_obj(obj)

        _obj = EnhanceTransactionResponse.parse_obj({
            "amount": obj.get("amount"),
            "categorized_by": obj.get("categorized_by"),
            "category": obj.get("category"),
            "category_guid": obj.get("category_guid"),
            "described_by": obj.get("described_by"),
            "description": obj.get("description"),
            "extended_transaction_type": obj.get("extended_transaction_type"),
            "id": obj.get("id"),
            "is_bill_pay": obj.get("is_bill_pay"),
            "is_direct_deposit": obj.get("is_direct_deposit"),
            "is_expense": obj.get("is_expense"),
            "is_fee": obj.get("is_fee"),
            "is_income": obj.get("is_income"),
            "is_international": obj.get("is_international"),
            "is_overdraft_fee": obj.get("is_overdraft_fee"),
            "is_payroll_advance": obj.get("is_payroll_advance"),
            "is_subscription": obj.get("is_subscription"),
            "memo": obj.get("memo"),
            "merchant_category_code": obj.get("merchant_category_code"),
            "merchant_guid": obj.get("merchant_guid"),
            "merchant_location_guid": obj.get("merchant_location_guid"),
            "original_description": obj.get("original_description"),
            "type": obj.get("type")
        })
        return _obj

