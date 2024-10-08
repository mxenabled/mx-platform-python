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

from mx_platform_python.models.goal_request import GoalRequest  # noqa: E501

class TestGoalRequest(unittest.TestCase):
    """GoalRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GoalRequest:
        """Test GoalRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GoalRequest`
        """
        model = GoalRequest()  # noqa: E501
        if include_optional:
            return GoalRequest(
                account_guid = 'ACT-4e431124-4a29-abf9-f059-ab232ac14dbf',
                amount = 4500.5,
                goal_type_name = 'PAYOFF',
                meta_type_name = 'VACATION',
                name = 'Save for Europe',
                completed_at = '2015-06-19T10:37:04-06:00',
                has_been_spent = False,
                is_complete = False,
                metadata = 'Additional information',
                position = 3,
                targeted_to_complete_at = '2026-12-08 00:00:00.000000'
            )
        else:
            return GoalRequest(
                account_guid = 'ACT-4e431124-4a29-abf9-f059-ab232ac14dbf',
                amount = 4500.5,
                goal_type_name = 'PAYOFF',
                meta_type_name = 'VACATION',
                name = 'Save for Europe',
        )
        """

    def testGoalRequest(self):
        """Test GoalRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
