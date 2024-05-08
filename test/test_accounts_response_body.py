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

from mx_platform_python.models.accounts_response_body import AccountsResponseBody  # noqa: E501

class TestAccountsResponseBody(unittest.TestCase):
    """AccountsResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountsResponseBody:
        """Test AccountsResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountsResponseBody`
        """
        model = AccountsResponseBody()  # noqa: E501
        if include_optional:
            return AccountsResponseBody(
                accounts = [
                    mx_platform_python.models.account_response.AccountResponse(
                        account_number = '5366', 
                        account_ownership = 'INDIVIDUAL', 
                        annuity_policy_to_date = '2016-10-13T17:57:37.000Z', 
                        annuity_provider = 'Metlife', 
                        annuity_term_year = 2048, 
                        apr = 1.0, 
                        apy = 1.0, 
                        available_balance = 1000.0, 
                        available_credit = 1000.0, 
                        balance = 10000.0, 
                        cash_balance = 1000.0, 
                        cash_surrender_value = 1000.0, 
                        created_at = '2023-07-25T17:14:46Z', 
                        credit_limit = 100.0, 
                        currency_code = 'USD', 
                        day_payment_is_due = 20, 
                        death_benefit = 1000, 
                        guid = 'ACT-06d7f44b-caae-0f6e-1384-01f52e75dcb1', 
                        holdings_value = 1000.0, 
                        id = '1040434698', 
                        imported_at = '2015-10-13T17:57:37.000Z', 
                        institution_code = '3af3685e-05d9-7060-359f-008d0755e993', 
                        insured_name = 'Tommy Shelby', 
                        interest_rate = 1.0, 
                        is_closed = False, 
                        is_hidden = False, 
                        is_manual = False, 
                        last_payment = 100.0, 
                        last_payment_at = '2023-07-25T17:14:46Z', 
                        loan_amount = 1000.0, 
                        margin_balance = 1000.0, 
                        matures_on = '2015-10-13T17:57:37.000Z', 
                        member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b', 
                        member_id = 'member123', 
                        member_is_managed_by_user = False, 
                        metadata = 'some metadata', 
                        minimum_balance = 100.0, 
                        minimum_payment = 10.0, 
                        name = 'Test account 2', 
                        nickname = 'My Checking', 
                        original_balance = 10.0, 
                        pay_out_amount = 10.0, 
                        payment_due_at = '2015-10-13T17:57:37.000Z', 
                        payoff_balance = 10.0, 
                        premium_amount = 1.0, 
                        property_type = 'VEHICLE', 
                        routing_number = '68899990000000', 
                        started_on = '2015-10-13T17:57:37.000Z', 
                        subtype = 'NONE', 
                        today_ugl_amount = 1000.5, 
                        today_ugl_percentage = 6.9, 
                        total_account_value = 1.0, 
                        type = 'SAVINGS', 
                        updated_at = '2016-10-13T18:08:00.000Z', 
                        user_guid = 'USR-fa7537f3-48aa-a683-a02a-b18940482f54', 
                        user_id = 'user123', )
                    ],
                pagination = mx_platform_python.models.pagination_response.PaginationResponse(
                    current_page = 1, 
                    per_page = 25, 
                    total_entries = 1, 
                    total_pages = 1, )
            )
        else:
            return AccountsResponseBody(
        )
        """

    def testAccountsResponseBody(self):
        """Test AccountsResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
