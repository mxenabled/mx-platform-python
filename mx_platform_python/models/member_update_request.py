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


from typing import List, Optional
from pydantic import BaseModel, StrictBool, StrictStr, conlist
from mx_platform_python.models.credential_request import CredentialRequest

class MemberUpdateRequest(BaseModel):
    """
    MemberUpdateRequest
    """
    background_aggregation_is_disabled: Optional[StrictBool] = None
    credentials: Optional[conlist(CredentialRequest)] = None
    id: Optional[StrictStr] = None
    metadata: Optional[StrictStr] = None
    skip_aggregation: Optional[StrictBool] = None
    __properties = ["background_aggregation_is_disabled", "credentials", "id", "metadata", "skip_aggregation"]

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
    def from_json(cls, json_str: str) -> MemberUpdateRequest:
        """Create an instance of MemberUpdateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in credentials (list)
        _items = []
        if self.credentials:
            for _item in self.credentials:
                if _item:
                    _items.append(_item.to_dict())
            _dict['credentials'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MemberUpdateRequest:
        """Create an instance of MemberUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MemberUpdateRequest.parse_obj(obj)

        _obj = MemberUpdateRequest.parse_obj({
            "background_aggregation_is_disabled": obj.get("background_aggregation_is_disabled"),
            "credentials": [CredentialRequest.from_dict(_item) for _item in obj.get("credentials")] if obj.get("credentials") is not None else None,
            "id": obj.get("id"),
            "metadata": obj.get("metadata"),
            "skip_aggregation": obj.get("skip_aggregation")
        })
        return _obj


