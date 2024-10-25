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

class AccountResponse(BaseModel):
    """
    AccountResponse
    """
    account_number: Optional[StrictStr] = None
    account_ownership: Optional[StrictStr] = None
    annuity_policy_to_date: Optional[StrictStr] = None
    annuity_provider: Optional[StrictStr] = None
    annuity_term_year: Optional[Union[StrictFloat, StrictInt]] = None
    apr: Optional[Union[StrictFloat, StrictInt]] = None
    apy: Optional[Union[StrictFloat, StrictInt]] = None
    available_balance: Optional[Union[StrictFloat, StrictInt]] = None
    available_credit: Optional[Union[StrictFloat, StrictInt]] = None
    balance: Optional[Union[StrictFloat, StrictInt]] = None
    cash_balance: Optional[Union[StrictFloat, StrictInt]] = None
    cash_surrender_value: Optional[Union[StrictFloat, StrictInt]] = None
    created_at: Optional[StrictStr] = None
    credit_limit: Optional[Union[StrictFloat, StrictInt]] = None
    currency_code: Optional[StrictStr] = None
    day_payment_is_due: Optional[StrictInt] = None
    death_benefit: Optional[StrictInt] = None
    federal_insurance_status: Optional[StrictStr] = None
    guid: Optional[StrictStr] = None
    holdings_value: Optional[Union[StrictFloat, StrictInt]] = None
    id: Optional[StrictStr] = None
    imported_at: Optional[StrictStr] = None
    institution_code: Optional[StrictStr] = None
    insured_name: Optional[StrictStr] = None
    interest_rate: Optional[Union[StrictFloat, StrictInt]] = None
    is_closed: Optional[StrictBool] = None
    is_hidden: Optional[StrictBool] = None
    is_manual: Optional[StrictBool] = None
    last_payment: Optional[Union[StrictFloat, StrictInt]] = None
    last_payment_at: Optional[StrictStr] = None
    loan_amount: Optional[Union[StrictFloat, StrictInt]] = None
    margin_balance: Optional[Union[StrictFloat, StrictInt]] = None
    matures_on: Optional[StrictStr] = None
    member_guid: Optional[StrictStr] = None
    member_id: Optional[StrictStr] = None
    member_is_managed_by_user: Optional[StrictBool] = None
    metadata: Optional[StrictStr] = None
    minimum_balance: Optional[Union[StrictFloat, StrictInt]] = None
    minimum_payment: Optional[Union[StrictFloat, StrictInt]] = None
    name: Optional[StrictStr] = None
    nickname: Optional[StrictStr] = None
    original_balance: Optional[Union[StrictFloat, StrictInt]] = None
    pay_out_amount: Optional[Union[StrictFloat, StrictInt]] = None
    payment_due_at: Optional[StrictStr] = None
    payoff_balance: Optional[Union[StrictFloat, StrictInt]] = None
    premium_amount: Optional[Union[StrictFloat, StrictInt]] = None
    property_type: Optional[StrictStr] = None
    routing_number: Optional[StrictStr] = None
    started_on: Optional[StrictStr] = None
    statement_balance: Optional[Union[StrictFloat, StrictInt]] = None
    subtype: Optional[StrictStr] = None
    today_ugl_amount: Optional[Union[StrictFloat, StrictInt]] = None
    today_ugl_percentage: Optional[Union[StrictFloat, StrictInt]] = None
    total_account_value: Optional[Union[StrictFloat, StrictInt]] = None
    total_account_value_ugl: Optional[Union[StrictFloat, StrictInt]] = None
    type: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    user_guid: Optional[StrictStr] = None
    user_id: Optional[StrictStr] = None
    __properties = ["account_number", "account_ownership", "annuity_policy_to_date", "annuity_provider", "annuity_term_year", "apr", "apy", "available_balance", "available_credit", "balance", "cash_balance", "cash_surrender_value", "created_at", "credit_limit", "currency_code", "day_payment_is_due", "death_benefit", "federal_insurance_status", "guid", "holdings_value", "id", "imported_at", "institution_code", "insured_name", "interest_rate", "is_closed", "is_hidden", "is_manual", "last_payment", "last_payment_at", "loan_amount", "margin_balance", "matures_on", "member_guid", "member_id", "member_is_managed_by_user", "metadata", "minimum_balance", "minimum_payment", "name", "nickname", "original_balance", "pay_out_amount", "payment_due_at", "payoff_balance", "premium_amount", "property_type", "routing_number", "started_on", "statement_balance", "subtype", "today_ugl_amount", "today_ugl_percentage", "total_account_value", "total_account_value_ugl", "type", "updated_at", "user_guid", "user_id"]

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
    def from_json(cls, json_str: str) -> AccountResponse:
        """Create an instance of AccountResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if account_number (nullable) is None
        # and __fields_set__ contains the field
        if self.account_number is None and "account_number" in self.__fields_set__:
            _dict['account_number'] = None

        # set to None if account_ownership (nullable) is None
        # and __fields_set__ contains the field
        if self.account_ownership is None and "account_ownership" in self.__fields_set__:
            _dict['account_ownership'] = None

        # set to None if annuity_policy_to_date (nullable) is None
        # and __fields_set__ contains the field
        if self.annuity_policy_to_date is None and "annuity_policy_to_date" in self.__fields_set__:
            _dict['annuity_policy_to_date'] = None

        # set to None if annuity_provider (nullable) is None
        # and __fields_set__ contains the field
        if self.annuity_provider is None and "annuity_provider" in self.__fields_set__:
            _dict['annuity_provider'] = None

        # set to None if annuity_term_year (nullable) is None
        # and __fields_set__ contains the field
        if self.annuity_term_year is None and "annuity_term_year" in self.__fields_set__:
            _dict['annuity_term_year'] = None

        # set to None if apr (nullable) is None
        # and __fields_set__ contains the field
        if self.apr is None and "apr" in self.__fields_set__:
            _dict['apr'] = None

        # set to None if apy (nullable) is None
        # and __fields_set__ contains the field
        if self.apy is None and "apy" in self.__fields_set__:
            _dict['apy'] = None

        # set to None if available_balance (nullable) is None
        # and __fields_set__ contains the field
        if self.available_balance is None and "available_balance" in self.__fields_set__:
            _dict['available_balance'] = None

        # set to None if available_credit (nullable) is None
        # and __fields_set__ contains the field
        if self.available_credit is None and "available_credit" in self.__fields_set__:
            _dict['available_credit'] = None

        # set to None if balance (nullable) is None
        # and __fields_set__ contains the field
        if self.balance is None and "balance" in self.__fields_set__:
            _dict['balance'] = None

        # set to None if cash_balance (nullable) is None
        # and __fields_set__ contains the field
        if self.cash_balance is None and "cash_balance" in self.__fields_set__:
            _dict['cash_balance'] = None

        # set to None if cash_surrender_value (nullable) is None
        # and __fields_set__ contains the field
        if self.cash_surrender_value is None and "cash_surrender_value" in self.__fields_set__:
            _dict['cash_surrender_value'] = None

        # set to None if credit_limit (nullable) is None
        # and __fields_set__ contains the field
        if self.credit_limit is None and "credit_limit" in self.__fields_set__:
            _dict['credit_limit'] = None

        # set to None if currency_code (nullable) is None
        # and __fields_set__ contains the field
        if self.currency_code is None and "currency_code" in self.__fields_set__:
            _dict['currency_code'] = None

        # set to None if day_payment_is_due (nullable) is None
        # and __fields_set__ contains the field
        if self.day_payment_is_due is None and "day_payment_is_due" in self.__fields_set__:
            _dict['day_payment_is_due'] = None

        # set to None if death_benefit (nullable) is None
        # and __fields_set__ contains the field
        if self.death_benefit is None and "death_benefit" in self.__fields_set__:
            _dict['death_benefit'] = None

        # set to None if federal_insurance_status (nullable) is None
        # and __fields_set__ contains the field
        if self.federal_insurance_status is None and "federal_insurance_status" in self.__fields_set__:
            _dict['federal_insurance_status'] = None

        # set to None if guid (nullable) is None
        # and __fields_set__ contains the field
        if self.guid is None and "guid" in self.__fields_set__:
            _dict['guid'] = None

        # set to None if holdings_value (nullable) is None
        # and __fields_set__ contains the field
        if self.holdings_value is None and "holdings_value" in self.__fields_set__:
            _dict['holdings_value'] = None

        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if imported_at (nullable) is None
        # and __fields_set__ contains the field
        if self.imported_at is None and "imported_at" in self.__fields_set__:
            _dict['imported_at'] = None

        # set to None if institution_code (nullable) is None
        # and __fields_set__ contains the field
        if self.institution_code is None and "institution_code" in self.__fields_set__:
            _dict['institution_code'] = None

        # set to None if insured_name (nullable) is None
        # and __fields_set__ contains the field
        if self.insured_name is None and "insured_name" in self.__fields_set__:
            _dict['insured_name'] = None

        # set to None if interest_rate (nullable) is None
        # and __fields_set__ contains the field
        if self.interest_rate is None and "interest_rate" in self.__fields_set__:
            _dict['interest_rate'] = None

        # set to None if is_closed (nullable) is None
        # and __fields_set__ contains the field
        if self.is_closed is None and "is_closed" in self.__fields_set__:
            _dict['is_closed'] = None

        # set to None if is_hidden (nullable) is None
        # and __fields_set__ contains the field
        if self.is_hidden is None and "is_hidden" in self.__fields_set__:
            _dict['is_hidden'] = None

        # set to None if is_manual (nullable) is None
        # and __fields_set__ contains the field
        if self.is_manual is None and "is_manual" in self.__fields_set__:
            _dict['is_manual'] = None

        # set to None if last_payment (nullable) is None
        # and __fields_set__ contains the field
        if self.last_payment is None and "last_payment" in self.__fields_set__:
            _dict['last_payment'] = None

        # set to None if last_payment_at (nullable) is None
        # and __fields_set__ contains the field
        if self.last_payment_at is None and "last_payment_at" in self.__fields_set__:
            _dict['last_payment_at'] = None

        # set to None if loan_amount (nullable) is None
        # and __fields_set__ contains the field
        if self.loan_amount is None and "loan_amount" in self.__fields_set__:
            _dict['loan_amount'] = None

        # set to None if margin_balance (nullable) is None
        # and __fields_set__ contains the field
        if self.margin_balance is None and "margin_balance" in self.__fields_set__:
            _dict['margin_balance'] = None

        # set to None if matures_on (nullable) is None
        # and __fields_set__ contains the field
        if self.matures_on is None and "matures_on" in self.__fields_set__:
            _dict['matures_on'] = None

        # set to None if member_guid (nullable) is None
        # and __fields_set__ contains the field
        if self.member_guid is None and "member_guid" in self.__fields_set__:
            _dict['member_guid'] = None

        # set to None if member_id (nullable) is None
        # and __fields_set__ contains the field
        if self.member_id is None and "member_id" in self.__fields_set__:
            _dict['member_id'] = None

        # set to None if member_is_managed_by_user (nullable) is None
        # and __fields_set__ contains the field
        if self.member_is_managed_by_user is None and "member_is_managed_by_user" in self.__fields_set__:
            _dict['member_is_managed_by_user'] = None

        # set to None if metadata (nullable) is None
        # and __fields_set__ contains the field
        if self.metadata is None and "metadata" in self.__fields_set__:
            _dict['metadata'] = None

        # set to None if minimum_balance (nullable) is None
        # and __fields_set__ contains the field
        if self.minimum_balance is None and "minimum_balance" in self.__fields_set__:
            _dict['minimum_balance'] = None

        # set to None if minimum_payment (nullable) is None
        # and __fields_set__ contains the field
        if self.minimum_payment is None and "minimum_payment" in self.__fields_set__:
            _dict['minimum_payment'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if nickname (nullable) is None
        # and __fields_set__ contains the field
        if self.nickname is None and "nickname" in self.__fields_set__:
            _dict['nickname'] = None

        # set to None if original_balance (nullable) is None
        # and __fields_set__ contains the field
        if self.original_balance is None and "original_balance" in self.__fields_set__:
            _dict['original_balance'] = None

        # set to None if pay_out_amount (nullable) is None
        # and __fields_set__ contains the field
        if self.pay_out_amount is None and "pay_out_amount" in self.__fields_set__:
            _dict['pay_out_amount'] = None

        # set to None if payment_due_at (nullable) is None
        # and __fields_set__ contains the field
        if self.payment_due_at is None and "payment_due_at" in self.__fields_set__:
            _dict['payment_due_at'] = None

        # set to None if payoff_balance (nullable) is None
        # and __fields_set__ contains the field
        if self.payoff_balance is None and "payoff_balance" in self.__fields_set__:
            _dict['payoff_balance'] = None

        # set to None if premium_amount (nullable) is None
        # and __fields_set__ contains the field
        if self.premium_amount is None and "premium_amount" in self.__fields_set__:
            _dict['premium_amount'] = None

        # set to None if property_type (nullable) is None
        # and __fields_set__ contains the field
        if self.property_type is None and "property_type" in self.__fields_set__:
            _dict['property_type'] = None

        # set to None if routing_number (nullable) is None
        # and __fields_set__ contains the field
        if self.routing_number is None and "routing_number" in self.__fields_set__:
            _dict['routing_number'] = None

        # set to None if started_on (nullable) is None
        # and __fields_set__ contains the field
        if self.started_on is None and "started_on" in self.__fields_set__:
            _dict['started_on'] = None

        # set to None if statement_balance (nullable) is None
        # and __fields_set__ contains the field
        if self.statement_balance is None and "statement_balance" in self.__fields_set__:
            _dict['statement_balance'] = None

        # set to None if subtype (nullable) is None
        # and __fields_set__ contains the field
        if self.subtype is None and "subtype" in self.__fields_set__:
            _dict['subtype'] = None

        # set to None if today_ugl_amount (nullable) is None
        # and __fields_set__ contains the field
        if self.today_ugl_amount is None and "today_ugl_amount" in self.__fields_set__:
            _dict['today_ugl_amount'] = None

        # set to None if today_ugl_percentage (nullable) is None
        # and __fields_set__ contains the field
        if self.today_ugl_percentage is None and "today_ugl_percentage" in self.__fields_set__:
            _dict['today_ugl_percentage'] = None

        # set to None if total_account_value (nullable) is None
        # and __fields_set__ contains the field
        if self.total_account_value is None and "total_account_value" in self.__fields_set__:
            _dict['total_account_value'] = None

        # set to None if total_account_value_ugl (nullable) is None
        # and __fields_set__ contains the field
        if self.total_account_value_ugl is None and "total_account_value_ugl" in self.__fields_set__:
            _dict['total_account_value_ugl'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

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
    def from_dict(cls, obj: dict) -> AccountResponse:
        """Create an instance of AccountResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AccountResponse.parse_obj(obj)

        _obj = AccountResponse.parse_obj({
            "account_number": obj.get("account_number"),
            "account_ownership": obj.get("account_ownership"),
            "annuity_policy_to_date": obj.get("annuity_policy_to_date"),
            "annuity_provider": obj.get("annuity_provider"),
            "annuity_term_year": obj.get("annuity_term_year"),
            "apr": obj.get("apr"),
            "apy": obj.get("apy"),
            "available_balance": obj.get("available_balance"),
            "available_credit": obj.get("available_credit"),
            "balance": obj.get("balance"),
            "cash_balance": obj.get("cash_balance"),
            "cash_surrender_value": obj.get("cash_surrender_value"),
            "created_at": obj.get("created_at"),
            "credit_limit": obj.get("credit_limit"),
            "currency_code": obj.get("currency_code"),
            "day_payment_is_due": obj.get("day_payment_is_due"),
            "death_benefit": obj.get("death_benefit"),
            "federal_insurance_status": obj.get("federal_insurance_status"),
            "guid": obj.get("guid"),
            "holdings_value": obj.get("holdings_value"),
            "id": obj.get("id"),
            "imported_at": obj.get("imported_at"),
            "institution_code": obj.get("institution_code"),
            "insured_name": obj.get("insured_name"),
            "interest_rate": obj.get("interest_rate"),
            "is_closed": obj.get("is_closed"),
            "is_hidden": obj.get("is_hidden"),
            "is_manual": obj.get("is_manual"),
            "last_payment": obj.get("last_payment"),
            "last_payment_at": obj.get("last_payment_at"),
            "loan_amount": obj.get("loan_amount"),
            "margin_balance": obj.get("margin_balance"),
            "matures_on": obj.get("matures_on"),
            "member_guid": obj.get("member_guid"),
            "member_id": obj.get("member_id"),
            "member_is_managed_by_user": obj.get("member_is_managed_by_user"),
            "metadata": obj.get("metadata"),
            "minimum_balance": obj.get("minimum_balance"),
            "minimum_payment": obj.get("minimum_payment"),
            "name": obj.get("name"),
            "nickname": obj.get("nickname"),
            "original_balance": obj.get("original_balance"),
            "pay_out_amount": obj.get("pay_out_amount"),
            "payment_due_at": obj.get("payment_due_at"),
            "payoff_balance": obj.get("payoff_balance"),
            "premium_amount": obj.get("premium_amount"),
            "property_type": obj.get("property_type"),
            "routing_number": obj.get("routing_number"),
            "started_on": obj.get("started_on"),
            "statement_balance": obj.get("statement_balance"),
            "subtype": obj.get("subtype"),
            "today_ugl_amount": obj.get("today_ugl_amount"),
            "today_ugl_percentage": obj.get("today_ugl_percentage"),
            "total_account_value": obj.get("total_account_value"),
            "total_account_value_ugl": obj.get("total_account_value_ugl"),
            "type": obj.get("type"),
            "updated_at": obj.get("updated_at"),
            "user_guid": obj.get("user_guid"),
            "user_id": obj.get("user_id")
        })
        return _obj


