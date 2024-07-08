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

from mx_platform_python.models.scheduled_payment_response import ScheduledPaymentResponse  # noqa: E501

class TestScheduledPaymentResponse(unittest.TestCase):
    """ScheduledPaymentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ScheduledPaymentResponse:
        """Test ScheduledPaymentResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ScheduledPaymentResponse`
        """
        model = ScheduledPaymentResponse()  # noqa: E501
        if include_optional:
            return ScheduledPaymentResponse(
                amount = 13.54,
                created_at = '2023-04-27T23:14:16Z',
                description = 'Netflix',
                guid = 'SPA-c76e4a85-b2c4-4335-82b7-8f8b8f28c35a',
                is_completed = False,
                is_recurring = True,
                merchant_guid = 'MCH-b8a2624c-2176-59ec-c150-37854bc38aa8',
                occurs_on = '2022-01-15',
                recurrence_day = 15,
                recurrence_type = 'EVERY_MONTH',
                transaction_type = 'DEBIT',
                updated_at = '2023-04-27T23:14:16Z',
                user_guid = 'USR-72086f59-6684-4adf-8f29-c4d32db43cd7'
            )
        else:
            return ScheduledPaymentResponse(
        )
        """

    def testScheduledPaymentResponse(self):
        """Test ScheduledPaymentResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()