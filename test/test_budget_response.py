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

from mx_platform_python.models.budget_response import BudgetResponse  # noqa: E501

class TestBudgetResponse(unittest.TestCase):
    """BudgetResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BudgetResponse:
        """Test BudgetResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BudgetResponse`
        """
        model = BudgetResponse()  # noqa: E501
        if include_optional:
            return BudgetResponse(
                amount = 153.0,
                category_guid = 'CAT-bd56d35a-a9a7-6e10-66c1-5b9cc1b6c81a',
                created_at = '2018-10-18T19:51:26+00:00',
                guid = 'BGT-6ca0e3ef-c65e-4655-8b5a-275a3c19c21d',
                is_exceeded = True,
                is_off_track = True,
                metadata = 'some metadata',
                name = 'Food & Dining',
                off_track_percentage = 1.337,
                parent_guid = '',
                percent_spent = 1276.34,
                projected_spending = 3562.4,
                revision = 561,
                transaction_total = 1952.8,
                updated_at = 2022-06-14T21:17:11+00:00,
                user_guid = USR-11141024-90b3-1bce-cac9-c06ced52ab4c
            )
        else:
            return BudgetResponse(
        )
        """

    def testBudgetResponse(self):
        """Test BudgetResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
