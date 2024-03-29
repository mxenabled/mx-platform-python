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

from mx_platform_python.models.member_resume_request import MemberResumeRequest  # noqa: E501

class TestMemberResumeRequest(unittest.TestCase):
    """MemberResumeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MemberResumeRequest:
        """Test MemberResumeRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MemberResumeRequest`
        """
        model = MemberResumeRequest()  # noqa: E501
        if include_optional:
            return MemberResumeRequest(
                challenges = [
                    mx_platform_python.models.credential_request.CredentialRequest(
                        guid = 'CRD-27d0edb8-1d50-5b90-bcbc-be270ca42b9f', 
                        value = 'password', )
                    ]
            )
        else:
            return MemberResumeRequest(
        )
        """

    def testMemberResumeRequest(self):
        """Test MemberResumeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
