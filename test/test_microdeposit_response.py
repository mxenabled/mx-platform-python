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

from mx_platform_python.models.microdeposit_response import MicrodepositResponse  # noqa: E501

class TestMicrodepositResponse(unittest.TestCase):
    """MicrodepositResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MicrodepositResponse:
        """Test MicrodepositResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MicrodepositResponse`
        """
        model = MicrodepositResponse()  # noqa: E501
        if include_optional:
            return MicrodepositResponse(
                account_name = 'My test account',
                account_number = '3331261',
                account_type = 'CHECKING',
                email = 'joshyboy2@example.com',
                first_name = 'Joshy',
                last_name = 'Grobanne',
                routing_number = '091000019',
                error_message = '',
                guid = 'MIC-09ba578e-8448-4f7f-89e1-b62ff2517edb',
                institution_code = 'mxbank',
                institution_name = 'MX Bank',
                status = 'INITIATED',
                updated_at = '2023-06-01T19:18:06Z',
                verified_at = ''
            )
        else:
            return MicrodepositResponse(
        )
        """

    def testMicrodepositResponse(self):
        """Test MicrodepositResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
