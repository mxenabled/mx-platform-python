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

from mx_platform_python.models.spending_plan_iteration_response import SpendingPlanIterationResponse  # noqa: E501

class TestSpendingPlanIterationResponse(unittest.TestCase):
    """SpendingPlanIterationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SpendingPlanIterationResponse:
        """Test SpendingPlanIterationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SpendingPlanIterationResponse`
        """
        model = SpendingPlanIterationResponse()  # noqa: E501
        if include_optional:
            return SpendingPlanIterationResponse(
                created_at = '2016-10-13T18:08:00+00:00',
                end_on = '2023-05-31',
                guid = 'SPI-848e6648-3fa3-4632-ac8f-e65f03167102',
                iteration_number = 1,
                spending_plan_guid = 'SPL-dbfe201d-c341-4bff-93c0-62a918d0b600',
                start_on = '2023-05-01',
                updated_at = '2016-10-13T18:09:00+00:00',
                user_guid = 'USR-72086f59-6684-4adf-8f29-c4d32db43cd7'
            )
        else:
            return SpendingPlanIterationResponse(
        )
        """

    def testSpendingPlanIterationResponse(self):
        """Test SpendingPlanIterationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
