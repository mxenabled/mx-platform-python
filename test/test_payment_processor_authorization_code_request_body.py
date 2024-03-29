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

from mx_platform_python.models.payment_processor_authorization_code_request_body import PaymentProcessorAuthorizationCodeRequestBody  # noqa: E501

class TestPaymentProcessorAuthorizationCodeRequestBody(unittest.TestCase):
    """PaymentProcessorAuthorizationCodeRequestBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentProcessorAuthorizationCodeRequestBody:
        """Test PaymentProcessorAuthorizationCodeRequestBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentProcessorAuthorizationCodeRequestBody`
        """
        model = PaymentProcessorAuthorizationCodeRequestBody()  # noqa: E501
        if include_optional:
            return PaymentProcessorAuthorizationCodeRequestBody(
                payment_processor_authorization_code = mx_platform_python.models.payment_processor_authorization_code_request.PaymentProcessorAuthorizationCodeRequest(
                    account_guid = 'ACT-4d4c0068-33bc-4d06-bbd6-cd270fd0135c', 
                    member_guid = 'MBR-46637bc5-942d-4229-9370-ddd858bf805e', 
                    user_guid = 'USR-f12b1f5a-7cbe-467c-aa30-0a10d0b2f549', )
            )
        else:
            return PaymentProcessorAuthorizationCodeRequestBody(
        )
        """

    def testPaymentProcessorAuthorizationCodeRequestBody(self):
        """Test PaymentProcessorAuthorizationCodeRequestBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
