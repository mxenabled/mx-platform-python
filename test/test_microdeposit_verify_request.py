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

from mx_platform_python.models.microdeposit_verify_request import MicrodepositVerifyRequest  # noqa: E501

class TestMicrodepositVerifyRequest(unittest.TestCase):
    """MicrodepositVerifyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MicrodepositVerifyRequest:
        """Test MicrodepositVerifyRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MicrodepositVerifyRequest`
        """
        model = MicrodepositVerifyRequest()  # noqa: E501
        if include_optional:
            return MicrodepositVerifyRequest(
                deposit_amount_1 = 56,
                deposit_amount_2 = 56
            )
        else:
            return MicrodepositVerifyRequest(
        )
        """

    def testMicrodepositVerifyRequest(self):
        """Test MicrodepositVerifyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
