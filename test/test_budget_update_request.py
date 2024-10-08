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

from mx_platform_python.models.budget_update_request import BudgetUpdateRequest  # noqa: E501

class TestBudgetUpdateRequest(unittest.TestCase):
    """BudgetUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BudgetUpdateRequest:
        """Test BudgetUpdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BudgetUpdateRequest`
        """
        model = BudgetUpdateRequest()  # noqa: E501
        if include_optional:
            return BudgetUpdateRequest(
                amount = 1000,
                metadata = 'Additional information',
                skip_webhook = True
            )
        else:
            return BudgetUpdateRequest(
        )
        """

    def testBudgetUpdateRequest(self):
        """Test BudgetUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
