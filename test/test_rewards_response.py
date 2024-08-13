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

from mx_platform_python.models.rewards_response import RewardsResponse  # noqa: E501

class TestRewardsResponse(unittest.TestCase):
    """RewardsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RewardsResponse:
        """Test RewardsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RewardsResponse`
        """
        model = RewardsResponse()  # noqa: E501
        if include_optional:
            return RewardsResponse(
                account_guid = 'ACT-1234',
                balance_type = 'EXPIRING_BALANCE',
                balance = 102,
                created_at = '2020-01-28T21:09:01+0000',
                description = 'A description of the reward.',
                expires_on = '2020-02-28',
                guid = 'RWD-1234',
                member_guid = 'MBR-4567',
                unit_type = 'POINTS',
                user_guid = 'USR-1234'
            )
        else:
            return RewardsResponse(
        )
        """

    def testRewardsResponse(self):
        """Test RewardsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
