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

from mx_platform_python.models.insight_response import InsightResponse  # noqa: E501

class TestInsightResponse(unittest.TestCase):
    """InsightResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightResponse:
        """Test InsightResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightResponse`
        """
        model = InsightResponse()  # noqa: E501
        if include_optional:
            return InsightResponse(
                active_at = '2022-01-07T12:00:00Z',
                client_guid = 'CLT-abcd-1234',
                created_at = '2022-01-12T18:16:51Z',
                cta_clicked_at = '2022-01-12T18:16:51Z',
                description = 'Gold's Gym charged you $36.71 more this month than normal. Did you upgrade your service?',
                guid = 'BET-abcd-1234',
                has_associated_accounts = False,
                has_associated_merchants = False,
                has_associated_scheduled_payments = False,
                has_associated_transactions = True,
                has_been_displayed = True,
                is_dismissed = False,
                micro_call_to_action = 'Learn more',
                micro_description = 'Netflix charged you $5.00 more this month than normal.',
                micro_title = 'Price increase',
                template = 'SubscriptionPriceIncrease',
                title = 'Price increase',
                updated_at = '2022-01-12T18:16:51Z',
                user_guid = 'USR-1234-abcd',
                user_id = user-partner-defined-1234
            )
        else:
            return InsightResponse(
        )
        """

    def testInsightResponse(self):
        """Test InsightResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
