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

class TransactionCreateResponseBody(BaseModel):
    """
    TransactionCreateResponseBody
    """
    account_guid: Optional[StrictStr] = None
    account_id: Optional[StrictStr] = None
    amount: Optional[Union[StrictFloat, StrictInt]] = None
    category: Optional[StrictStr] = None
    category_guid: Optional[StrictStr] = None
    check_number_string: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = None
    currency_code: Optional[StrictStr] = None
    var_date: Optional[StrictStr] = Field(None, alias="date")
    description: Optional[StrictStr] = None
    extended_transaction_type: Optional[StrictStr] = None
    guid: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    is_bill_pay: Optional[StrictBool] = None
    is_direct_deposit: Optional[StrictBool] = None
    is_expense: Optional[StrictBool] = None
    is_fee: Optional[StrictBool] = None
    is_income: Optional[StrictBool] = None
    is_international: Optional[StrictBool] = None
    is_manual: Optional[StrictBool] = None
    is_overdraft_fee: Optional[StrictBool] = None
    is_payroll_advance: Optional[StrictBool] = None
    is_recurring: Optional[StrictBool] = None
    is_subscription: Optional[StrictBool] = None
    latitude: Optional[Union[StrictFloat, StrictInt]] = None
    localized_description: Optional[StrictStr] = None
    localized_memo: Optional[StrictStr] = None
    longitude: Optional[Union[StrictFloat, StrictInt]] = None
    member_guid: Optional[StrictStr] = None
    member_is_managed_by_user: Optional[StrictBool] = None
    memo: Optional[StrictStr] = None
    merchant_category_code: Optional[StrictInt] = None
    merchant_guid: Optional[StrictStr] = None
    merchant_location_guid: Optional[StrictStr] = None
    metadata: Optional[StrictStr] = None
    original_description: Optional[StrictStr] = None
    posted_at: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    top_level_category: Optional[StrictStr] = None
    transacted_at: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    user_guid: Optional[StrictStr] = None
    user_id: Optional[StrictStr] = None
    __properties = ["account_guid", "account_id", "amount", "category", "category_guid", "check_number_string", "created_at", "currency_code", "date", "description", "extended_transaction_type", "guid", "id", "is_bill_pay", "is_direct_deposit", "is_expense", "is_fee", "is_income", "is_international", "is_manual", "is_overdraft_fee", "is_payroll_advance", "is_recurring", "is_subscription", "latitude", "localized_description", "localized_memo", "longitude", "member_guid", "member_is_managed_by_user", "memo", "merchant_category_code", "merchant_guid", "merchant_location_guid", "metadata", "original_description", "posted_at", "status", "top_level_category", "transacted_at", "type", "updated_at", "user_guid", "user_id"]

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
    def from_json(cls, json_str: str) -> TransactionCreateResponseBody:
        """Create an instance of TransactionCreateResponseBody from a JSON string"""
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

        # set to None if account_id (nullable) is None
        # and __fields_set__ contains the field
        if self.account_id is None and "account_id" in self.__fields_set__:
            _dict['account_id'] = None

        # set to None if category (nullable) is None
        # and __fields_set__ contains the field
        if self.category is None and "category" in self.__fields_set__:
            _dict['category'] = None

        # set to None if category_guid (nullable) is None
        # and __fields_set__ contains the field
        if self.category_guid is None and "category_guid" in self.__fields_set__:
            _dict['category_guid'] = None

        # set to None if check_number_string (nullable) is None
        # and __fields_set__ contains the field
        if self.check_number_string is None and "check_number_string" in self.__fields_set__:
            _dict['check_number_string'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if currency_code (nullable) is None
        # and __fields_set__ contains the field
        if self.currency_code is None and "currency_code" in self.__fields_set__:
            _dict['currency_code'] = None

        # set to None if var_date (nullable) is None
        # and __fields_set__ contains the field
        if self.var_date is None and "var_date" in self.__fields_set__:
            _dict['date'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if extended_transaction_type (nullable) is None
        # and __fields_set__ contains the field
        if self.extended_transaction_type is None and "extended_transaction_type" in self.__fields_set__:
            _dict['extended_transaction_type'] = None

        # set to None if guid (nullable) is None
        # and __fields_set__ contains the field
        if self.guid is None and "guid" in self.__fields_set__:
            _dict['guid'] = None

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

        # set to None if is_manual (nullable) is None
        # and __fields_set__ contains the field
        if self.is_manual is None and "is_manual" in self.__fields_set__:
            _dict['is_manual'] = None

        # set to None if is_overdraft_fee (nullable) is None
        # and __fields_set__ contains the field
        if self.is_overdraft_fee is None and "is_overdraft_fee" in self.__fields_set__:
            _dict['is_overdraft_fee'] = None

        # set to None if is_payroll_advance (nullable) is None
        # and __fields_set__ contains the field
        if self.is_payroll_advance is None and "is_payroll_advance" in self.__fields_set__:
            _dict['is_payroll_advance'] = None

        # set to None if is_recurring (nullable) is None
        # and __fields_set__ contains the field
        if self.is_recurring is None and "is_recurring" in self.__fields_set__:
            _dict['is_recurring'] = None

        # set to None if is_subscription (nullable) is None
        # and __fields_set__ contains the field
        if self.is_subscription is None and "is_subscription" in self.__fields_set__:
            _dict['is_subscription'] = None

        # set to None if latitude (nullable) is None
        # and __fields_set__ contains the field
        if self.latitude is None and "latitude" in self.__fields_set__:
            _dict['latitude'] = None

        # set to None if localized_description (nullable) is None
        # and __fields_set__ contains the field
        if self.localized_description is None and "localized_description" in self.__fields_set__:
            _dict['localized_description'] = None

        # set to None if localized_memo (nullable) is None
        # and __fields_set__ contains the field
        if self.localized_memo is None and "localized_memo" in self.__fields_set__:
            _dict['localized_memo'] = None

        # set to None if longitude (nullable) is None
        # and __fields_set__ contains the field
        if self.longitude is None and "longitude" in self.__fields_set__:
            _dict['longitude'] = None

        # set to None if member_guid (nullable) is None
        # and __fields_set__ contains the field
        if self.member_guid is None and "member_guid" in self.__fields_set__:
            _dict['member_guid'] = None

        # set to None if member_is_managed_by_user (nullable) is None
        # and __fields_set__ contains the field
        if self.member_is_managed_by_user is None and "member_is_managed_by_user" in self.__fields_set__:
            _dict['member_is_managed_by_user'] = None

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

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        # set to None if original_description (nullable) is None
        # and __fields_set__ contains the field
        if self.original_description is None and "original_description" in self.__fields_set__:
            _dict['original_description'] = None

        # set to None if posted_at (nullable) is None
        # and __fields_set__ contains the field
        if self.posted_at is None and "posted_at" in self.__fields_set__:
            _dict['posted_at'] = None

        # set to None if status (nullable) is None
        # and __fields_set__ contains the field
        if self.status is None and "status" in self.__fields_set__:
            _dict['status'] = None

        # set to None if top_level_category (nullable) is None
        # and __fields_set__ contains the field
        if self.top_level_category is None and "top_level_category" in self.__fields_set__:
            _dict['top_level_category'] = None

        # set to None if transacted_at (nullable) is None
        # and __fields_set__ contains the field
        if self.transacted_at is None and "transacted_at" in self.__fields_set__:
            _dict['transacted_at'] = None

        # set to None if user_guid (nullable) is None
        # and __fields_set__ contains the field
        if self.user_guid is None and "user_guid" in self.__fields_set__:
            _dict['user_guid'] = None

        # set to None if user_id (nullable) is None
        # and __fields_set__ contains the field
        if self.user_id is None and "user_id" in self.__fields_set__:
            _dict['user_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransactionCreateResponseBody:
        """Create an instance of TransactionCreateResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TransactionCreateResponseBody.parse_obj(obj)

        _obj = TransactionCreateResponseBody.parse_obj({
            "account_guid": obj.get("account_guid"),
            "account_id": obj.get("account_id"),
            "amount": obj.get("amount"),
            "category": obj.get("category"),
            "category_guid": obj.get("category_guid"),
            "check_number_string": obj.get("check_number_string"),
            "created_at": obj.get("created_at"),
            "currency_code": obj.get("currency_code"),
            "var_date": obj.get("date"),
            "description": obj.get("description"),
            "extended_transaction_type": obj.get("extended_transaction_type"),
            "guid": obj.get("guid"),
            "id": obj.get("id"),
            "is_bill_pay": obj.get("is_bill_pay"),
            "is_direct_deposit": obj.get("is_direct_deposit"),
            "is_expense": obj.get("is_expense"),
            "is_fee": obj.get("is_fee"),
            "is_income": obj.get("is_income"),
            "is_international": obj.get("is_international"),
            "is_manual": obj.get("is_manual"),
            "is_overdraft_fee": obj.get("is_overdraft_fee"),
            "is_payroll_advance": obj.get("is_payroll_advance"),
            "is_recurring": obj.get("is_recurring"),
            "is_subscription": obj.get("is_subscription"),
            "latitude": obj.get("latitude"),
            "localized_description": obj.get("localized_description"),
            "localized_memo": obj.get("localized_memo"),
            "longitude": obj.get("longitude"),
            "member_guid": obj.get("member_guid"),
            "member_is_managed_by_user": obj.get("member_is_managed_by_user"),
            "memo": obj.get("memo"),
            "merchant_category_code": obj.get("merchant_category_code"),
            "merchant_guid": obj.get("merchant_guid"),
            "merchant_location_guid": obj.get("merchant_location_guid"),
            "metadata": obj.get("metadata"),
            "original_description": obj.get("original_description"),
            "posted_at": obj.get("posted_at"),
            "status": obj.get("status"),
            "top_level_category": obj.get("top_level_category"),
            "transacted_at": obj.get("transacted_at"),
            "type": obj.get("type"),
            "updated_at": obj.get("updated_at"),
            "user_guid": obj.get("user_guid"),
            "user_id": obj.get("user_id")
        })
        return _obj


