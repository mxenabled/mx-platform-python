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

from mx_platform_python.models.tax_document_response_body import TaxDocumentResponseBody  # noqa: E501

class TestTaxDocumentResponseBody(unittest.TestCase):
    """TaxDocumentResponseBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaxDocumentResponseBody:
        """Test TaxDocumentResponseBody
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaxDocumentResponseBody`
        """
        model = TaxDocumentResponseBody()  # noqa: E501
        if include_optional:
            return TaxDocumentResponseBody(
                tax_document = mx_platform_python.models.tax_document_response.TaxDocumentResponse(
                    content_hash = 'a16c580c4fcdfa8088edaa7b4d35b290', 
                    created_at = '2022-10-18T19:23:16Z', 
                    document_type = 'TAX1099_C', 
                    guid = 'TAX-ee8776ea-468b-4b02-b95d-743adf6ba50e', 
                    issued_on = '2022-03-31', 
                    member_guid = 'MBR-7c6f361b-e582-15b6-60c0-358f12466b4b', 
                    tax_year = '2023', 
                    updated_at = '2022-10-18T19:23:16Z', 
                    uri = '/users/USR-11141024-90b3-1bce-cac9-c06ced52ab4c/members/MBR-7c6f361b-e582-15b6-60c0-358f12466b4b/tax_documents/TAX-ee8776ea-468b-4b02-b95d-743adf6ba50e.pdf', 
                    user_guid = 'USR-11141024-90b3-1bce-cac9-c06ced52ab4c', )
            )
        else:
            return TaxDocumentResponseBody(
        )
        """

    def testTaxDocumentResponseBody(self):
        """Test TaxDocumentResponseBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
