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

class TaxDocumentResponse(BaseModel):
    """
    TaxDocumentResponse
    """
    content_hash: Optional[StrictStr] = None
    created_at: Optional[StrictStr] = None
    document_type: Optional[StrictStr] = None
    guid: Optional[StrictStr] = None
    issued_on: Optional[StrictStr] = None
    member_guid: Optional[StrictStr] = None
    tax_year: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    uri: Optional[StrictStr] = None
    user_guid: Optional[StrictStr] = None
    __properties = ["content_hash", "created_at", "document_type", "guid", "issued_on", "member_guid", "tax_year", "updated_at", "uri", "user_guid"]

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
    def from_json(cls, json_str: str) -> TaxDocumentResponse:
        """Create an instance of TaxDocumentResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if content_hash (nullable) is None
        # and __fields_set__ contains the field
        if self.content_hash is None and "content_hash" in self.__fields_set__:
            _dict['content_hash'] = None

        # set to None if created_at (nullable) is None
        # and __fields_set__ contains the field
        if self.created_at is None and "created_at" in self.__fields_set__:
            _dict['created_at'] = None

        # set to None if document_type (nullable) is None
        # and __fields_set__ contains the field
        if self.document_type is None and "document_type" in self.__fields_set__:
            _dict['document_type'] = None

        # set to None if guid (nullable) is None
        # and __fields_set__ contains the field
        if self.guid is None and "guid" in self.__fields_set__:
            _dict['guid'] = None

        # set to None if issued_on (nullable) is None
        # and __fields_set__ contains the field
        if self.issued_on is None and "issued_on" in self.__fields_set__:
            _dict['issued_on'] = None

        # set to None if member_guid (nullable) is None
        # and __fields_set__ contains the field
        if self.member_guid is None and "member_guid" in self.__fields_set__:
            _dict['member_guid'] = None

        # set to None if tax_year (nullable) is None
        # and __fields_set__ contains the field
        if self.tax_year is None and "tax_year" in self.__fields_set__:
            _dict['tax_year'] = None

        # set to None if updated_at (nullable) is None
        # and __fields_set__ contains the field
        if self.updated_at is None and "updated_at" in self.__fields_set__:
            _dict['updated_at'] = None

        # set to None if uri (nullable) is None
        # and __fields_set__ contains the field
        if self.uri is None and "uri" in self.__fields_set__:
            _dict['uri'] = None

        # set to None if user_guid (nullable) is None
        # and __fields_set__ contains the field
        if self.user_guid is None and "user_guid" in self.__fields_set__:
            _dict['user_guid'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TaxDocumentResponse:
        """Create an instance of TaxDocumentResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TaxDocumentResponse.parse_obj(obj)

        _obj = TaxDocumentResponse.parse_obj({
            "content_hash": obj.get("content_hash"),
            "created_at": obj.get("created_at"),
            "document_type": obj.get("document_type"),
            "guid": obj.get("guid"),
            "issued_on": obj.get("issued_on"),
            "member_guid": obj.get("member_guid"),
            "tax_year": obj.get("tax_year"),
            "updated_at": obj.get("updated_at"),
            "uri": obj.get("uri"),
            "user_guid": obj.get("user_guid")
        })
        return _obj

