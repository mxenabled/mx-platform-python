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

from mx_platform_python.models.credit_card_product_response import CreditCardProductResponse  # noqa: E501

class TestCreditCardProductResponse(unittest.TestCase):
    """CreditCardProductResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreditCardProductResponse:
        """Test CreditCardProductResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreditCardProductResponse`
        """
        model = CreditCardProductResponse()  # noqa: E501
        if include_optional:
            return CreditCardProductResponse(
                reward = mx_platform_python.models.credit_card_product.CreditCardProduct(
                    annual_fee = 45.0, 
                    duration_of_introductory_rate_on_balance_transfer = null, 
                    duration_of_introductory_rate_on_purchases = null, 
                    guid = CCA-b5bcd822-6d01-4e23-b8d6-846a225e714a, 
                    has_cashback_rewards = False, 
                    has_other_rewards = True, 
                    has_travel_rewards = True, 
                    has_zero_introductory_annual_fee = True, 
                    has_zero_percent_introductory_rate = False, 
                    has_zero_percent_introductory_rate_on_balance_transfer = True, 
                    financial_institution = True, 
                    is_accepting_applications = True, 
                    is_small_business_card = True, 
                    name = 'Chase Credit Card', )
            )
        else:
            return CreditCardProductResponse(
        )
        """

    def testCreditCardProductResponse(self):
        """Test CreditCardProductResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()