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

from mx_platform_python.models.enhance_transactions_request import EnhanceTransactionsRequest  # noqa: E501

class TestEnhanceTransactionsRequest(unittest.TestCase):
    """EnhanceTransactionsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EnhanceTransactionsRequest:
        """Test EnhanceTransactionsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EnhanceTransactionsRequest`
        """
        model = EnhanceTransactionsRequest()  # noqa: E501
        if include_optional:
            return EnhanceTransactionsRequest(
                amount = 21.33,
                description = 'ubr* pending.uber.com',
                extended_transaction_type = 'partner_transaction_type',
                id = 'ID-123',
                memo = 'Additional-information*on_transaction',
                merchant_category_code = 4121,
                type = 'DEBIT'
            )
        else:
            return EnhanceTransactionsRequest(
                description = 'ubr* pending.uber.com',
                id = 'ID-123',
        )
        """

    def testEnhanceTransactionsRequest(self):
        """Test EnhanceTransactionsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
