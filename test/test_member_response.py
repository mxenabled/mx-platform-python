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

from mx_platform_python.models.member_response import MemberResponse  # noqa: E501

class TestMemberResponse(unittest.TestCase):
    """MemberResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MemberResponse:
        """Test MemberResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MemberResponse`
        """
        model = MemberResponse()  # noqa: E501
        if include_optional:
            return MemberResponse(
                actionable_error = '{\"error_type\": \"MEMBER\", \"error_code\": 1000, \"error_message\": \"This Member has no eligible checking, savings, or money market accounts.\", \"user_message\": \"We could not find any accounts eligible for transfers. Please link a checking or savings account.\", \"locale\": \"en\"}',
                aggregated_at = '2016-10-13T18:07:57.000Z',
                background_aggregation_is_disabled = False,
                connection_status = 'CONNECTED',
                guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b',
                id = 'unique_id',
                institution_code = 'chase',
                is_being_aggregated = False,
                is_managed_by_user = False,
                is_manual = False,
                is_oauth = False,
                metadata = '\"credentials_last_refreshed_at\": \"2015-10-15\"',
                most_recent_job_detail_code = '(deprecated)',
                most_recent_job_detail_text = '(deprecated)',
                name = 'Chase Bank',
                oauth_window_uri = 'https://mxbank.mx.com/oauth/authorize?client_id=b8OikQ4Ep3NuSUrQ13DdvFuwpNx-qqoAsJDVAQCyLkQ&redirect_uri=https%3A%2F%2Fint-app.moneydesktop.com%2Foauth%2Fredirect_from&response_type=code&scope=openid&state=d745bd4ee6f0f9c184757f574bcc2df2',
                successfully_aggregated_at = '2016-10-13T17:57:38.000Z',
                use_cases = ["PFM","IAV"],
                user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54',
                user_id = 'user123'
            )
        else:
            return MemberResponse(
        )
        """

    def testMemberResponse(self):
        """Test MemberResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
