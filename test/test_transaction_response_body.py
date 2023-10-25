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

from mx_platform_python.models.transaction_response_body import TransactionResponseBody  # noqa: E501

class TestTransactionResponseBody(unittest.TestCase):
    """TransactionResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionResponseBody:
        """Test TransactionResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionResponseBody`
        """
        model = TransactionResponseBody()  # noqa: E501
        if include_optional:
            return TransactionResponseBody(
                transaction = mx_platform_python.models.transaction_response.TransactionResponse(
                    account_guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1', 
                    account_id = 'account123', 
                    amount = 61.11, 
                    category = 'Groceries', 
                    category_guid = 'CAT-9588eaad-90a4-bb5c-66c8-1812503d0db8', 
                    check_number_string = '6812', 
                    created_at = '2016-10-06T09:43:42.000Z', 
                    currency_code = 'USD', 
                    date = '2013-09-23T00:00:00.000Z', 
                    description = 'Whole foods', 
                    extended_transaction_type = 'partner_transaction_type', 
                    guid = 'TRN-265abee9-889b-af6a-c69b-25157db2bdd9', 
                    id = 'transaction-265abee9-889b-af6a-c69b-25157db2bdd9', 
                    is_bill_pay = False, 
                    is_direct_deposit = False, 
                    is_expense = True, 
                    is_fee = False, 
                    is_income = False, 
                    is_international = False, 
                    is_overdraft_fee = False, 
                    is_payroll_advance = False, 
                    is_recurring = False, 
                    is_subscription = False, 
                    latitude = -43.2075, 
                    localized_description = 'This is a localized_description', 
                    localized_memo = 'This is a localized_memo', 
                    longitude = 139.691706, 
                    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b', 
                    member_is_managed_by_user = False, 
                    memo = 'This is a memo', 
                    merchant_category_code = 5411, 
                    merchant_guid = 'MCH-7ed79542-884d-2b1b-dd74-501c5cc9d25b', 
                    merchant_location_guid = 'MCL-00024e59-18b5-4d79-b879-2a7896726fea', 
                    metadata = 'some metadata', 
                    original_description = 'WHOLEFDS TSQ 102', 
                    posted_at = '2016-10-07T06:00:00.000Z', 
                    status = 'POSTED', 
                    top_level_category = 'Food & Dining', 
                    transacted_at = '2016-10-06T13:00:00.000Z', 
                    type = 'DEBIT', 
                    updated_at = '2016-10-07T05:49:12.000Z', 
                    user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54', 
                    user_id = 'user123', )
            )
        else:
            return TransactionResponseBody(
        )
        """

    def testTransactionResponseBody(self):
        """Test TransactionResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
