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

from mx_platform_python.models.managed_transaction_create_request import ManagedTransactionCreateRequest  # noqa: E501

class TestManagedTransactionCreateRequest(unittest.TestCase):
    """ManagedTransactionCreateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ManagedTransactionCreateRequest:
        """Test ManagedTransactionCreateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ManagedTransactionCreateRequest`
        """
        model = ManagedTransactionCreateRequest()  # noqa: E501
        if include_optional:
            return ManagedTransactionCreateRequest(
                amount = '61.11',
                category = 'Groceries',
                check_number_string = '6812',
                currency_code = 'USD',
                description = 'Whole foods',
                id = 'transaction-265abee9-889b-af6a-c69b-25157db2bdd9',
                is_international = False,
                latitude = -43.2075,
                localized_description = 'This is a localized_description',
                localized_memo = 'This is a localized_memo',
                longitude = 139.691706,
                memo = 'This is a memo',
                merchant_category_code = 5411,
                merchant_guid = 'MCH-7ed79542-884d-2b1b-dd74-501c5cc9d25b',
                merchant_location_guid = 'MCL-00024e59-18b5-4d79-b879-2a7896726fea',
                metadata = 'some metadata',
                posted_at = '2016-10-07T06:00:00.000Z',
                status = 'POSTED',
                transacted_at = '2016-10-06T13:00:00.000Z',
                type = 'DEBIT'
            )
        else:
            return ManagedTransactionCreateRequest(
                amount = '61.11',
                description = 'Whole foods',
                status = 'POSTED',
                transacted_at = '2016-10-06T13:00:00.000Z',
                type = 'DEBIT',
        )
        """

    def testManagedTransactionCreateRequest(self):
        """Test ManagedTransactionCreateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
