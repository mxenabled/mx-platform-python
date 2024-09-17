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

from mx_platform_python.models.microdeposit_request import MicrodepositRequest  # noqa: E501

class TestMicrodepositRequest(unittest.TestCase):
    """MicrodepositRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MicrodepositRequest:
        """Test MicrodepositRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MicrodepositRequest`
        """
        model = MicrodepositRequest()  # noqa: E501
        if include_optional:
            return MicrodepositRequest(
                account_number = '3331261',
                account_type = 'CHECKING',
                routing_number = '091000019',
                account_name = 'My test account',
                email = 'joshyboy2@example.com',
                first_name = 'Joshy',
                last_name = 'Grobanne'
            )
        else:
            return MicrodepositRequest(
                account_number = '3331261',
                account_type = 'CHECKING',
                routing_number = '091000019',
        )
        """

    def testMicrodepositRequest(self):
        """Test MicrodepositRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
