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

from mx_platform_python.models.enhance_transaction_response import EnhanceTransactionResponse  # noqa: E501

class TestEnhanceTransactionResponse(unittest.TestCase):
    """EnhanceTransactionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnhanceTransactionResponse:
        """Test EnhanceTransactionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnhanceTransactionResponse`
        """
        model = EnhanceTransactionResponse()  # noqa: E501
        if include_optional:
            return EnhanceTransactionResponse(
                amount = 21.33,
                categorized_by = 13,
                category = 'Rental Car & Taxi',
                category_guid = 'CAT-9588eaad-90a4-bb5c-66c8-1812503d0db8',
                described_by = 6,
                description = 'Uber',
                extended_transaction_type = 'partner_transaction_type',
                id = 'ID-123',
                is_bill_pay = False,
                is_direct_deposit = False,
                is_expense = False,
                is_fee = False,
                is_income = False,
                is_international = False,
                is_overdraft_fee = False,
                is_payroll_advance = False,
                is_subscription = False,
                memo = 'Additional-information*on_transaction',
                merchant_category_code = 4121,
                merchant_guid = 'MCH-14f25b63-ef47-a38e-b2b6-d02b280b6e4e',
                merchant_location_guid = 'MCL-00024e59-18b5-4d79-b879-2a7896726fea',
                original_description = 'ubr* pending.uber.com',
                type = 'DEBIT'
            )
        else:
            return EnhanceTransactionResponse(
        )
        """

    def testEnhanceTransactionResponse(self):
        """Test EnhanceTransactionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
