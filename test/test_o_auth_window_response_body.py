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

from mx_platform_python.models.o_auth_window_response_body import OAuthWindowResponseBody  # noqa: E501

class TestOAuthWindowResponseBody(unittest.TestCase):
    """OAuthWindowResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OAuthWindowResponseBody:
        """Test OAuthWindowResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OAuthWindowResponseBody`
        """
        model = OAuthWindowResponseBody()  # noqa: E501
        if include_optional:
            return OAuthWindowResponseBody(
                member = mx_platform_python.models.o_auth_window_response.OAuthWindowResponse(
                    guid = 'MBR-df96fd60-7122-4464-b3c2-ff11d8c74f6f', 
                    oauth_window_uri = 'https://mxbank.mx.com/oauth/authorize?client_id=b8OikQ4Ep3NuSUrQ13DdvFuwpNx-qqoAsJDVAQCyLkQ&redirect_uri=https%3A%2F%2Fint-app.moneydesktop.com%2Foauth%2Fredirect_from&response_type=code&scope=openid&state=d745bd4ee6f0f9c184757f574bcc2df2', )
            )
        else:
            return OAuthWindowResponseBody(
        )
        """

    def testOAuthWindowResponseBody(self):
        """Test OAuthWindowResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
