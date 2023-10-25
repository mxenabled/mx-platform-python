# coding: utf-8

"""
    MX Platform API

    The MX Platform API is a powerful, fully-featured API designed to make aggregating and enhancing financial data easy and reliable. It can seamlessly connect your app or website to tens of thousands of financial institutions.

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from mx_platform_python.models.tagging_update_request import TaggingUpdateRequest  # noqa: E501

class TestTaggingUpdateRequest(unittest.TestCase):
    """TaggingUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaggingUpdateRequest:
        """Test TaggingUpdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaggingUpdateRequest`
        """
        model = TaggingUpdateRequest()  # noqa: E501
        if include_optional:
            return TaggingUpdateRequest(
                tag_guid = 'TAG-40faf068-abb4-405c-8f6a-e883ed541fff'
            )
        else:
            return TaggingUpdateRequest(
                tag_guid = 'TAG-40faf068-abb4-405c-8f6a-e883ed541fff',
        )
        """

    def testTaggingUpdateRequest(self):
        """Test TaggingUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
