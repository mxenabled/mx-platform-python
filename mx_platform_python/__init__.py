# coding: utf-8

# flake8: noqa

"""
    MX Platform API

    The MX Platform API is a powerful, fully-featured API designed to make aggregating and enhancing financial data easy and reliable. It can seamlessly connect your app or website to tens of thousands of financial institutions.

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.42.0"

# import apis into sdk package
from mx_platform_python.api.budgets_api import BudgetsApi
from mx_platform_python.api.goals_api import GoalsApi
from mx_platform_python.api.insights_api import InsightsApi
from mx_platform_python.api.microdeposits_api import MicrodepositsApi
from mx_platform_python.api.mx_platform_api import MxPlatformApi
from mx_platform_python.api.spending_plan_api import SpendingPlanApi
from mx_platform_python.api.transactions_api import TransactionsApi

# import ApiClient
from mx_platform_python.api_response import ApiResponse
from mx_platform_python.api_client import ApiClient
from mx_platform_python.configuration import Configuration
from mx_platform_python.exceptions import OpenApiException
from mx_platform_python.exceptions import ApiTypeError
from mx_platform_python.exceptions import ApiValueError
from mx_platform_python.exceptions import ApiKeyError
from mx_platform_python.exceptions import ApiAttributeError
from mx_platform_python.exceptions import ApiException

# import models into sdk package
from mx_platform_python.models.account_create_request import AccountCreateRequest
from mx_platform_python.models.account_create_request_body import AccountCreateRequestBody
from mx_platform_python.models.account_number_response import AccountNumberResponse
from mx_platform_python.models.account_numbers_response_body import AccountNumbersResponseBody
from mx_platform_python.models.account_owner_response import AccountOwnerResponse
from mx_platform_python.models.account_owners_response_body import AccountOwnersResponseBody
from mx_platform_python.models.account_response import AccountResponse
from mx_platform_python.models.account_response_body import AccountResponseBody
from mx_platform_python.models.account_update_request import AccountUpdateRequest
from mx_platform_python.models.account_update_request_body import AccountUpdateRequestBody
from mx_platform_python.models.accounts_response_body import AccountsResponseBody
from mx_platform_python.models.authorization_code_request import AuthorizationCodeRequest
from mx_platform_python.models.authorization_code_request_body import AuthorizationCodeRequestBody
from mx_platform_python.models.authorization_code_response import AuthorizationCodeResponse
from mx_platform_python.models.authorization_code_response_body import AuthorizationCodeResponseBody
from mx_platform_python.models.budget_create_request import BudgetCreateRequest
from mx_platform_python.models.budget_create_request_body import BudgetCreateRequestBody
from mx_platform_python.models.budget_response import BudgetResponse
from mx_platform_python.models.budget_response_body import BudgetResponseBody
from mx_platform_python.models.budget_update_request import BudgetUpdateRequest
from mx_platform_python.models.budget_update_request_body import BudgetUpdateRequestBody
from mx_platform_python.models.categories_response_body import CategoriesResponseBody
from mx_platform_python.models.category_create_request import CategoryCreateRequest
from mx_platform_python.models.category_create_request_body import CategoryCreateRequestBody
from mx_platform_python.models.category_response import CategoryResponse
from mx_platform_python.models.category_response_body import CategoryResponseBody
from mx_platform_python.models.category_update_request import CategoryUpdateRequest
from mx_platform_python.models.category_update_request_body import CategoryUpdateRequestBody
from mx_platform_python.models.challenge_response import ChallengeResponse
from mx_platform_python.models.challenges_response_body import ChallengesResponseBody
from mx_platform_python.models.connect_widget_request import ConnectWidgetRequest
from mx_platform_python.models.connect_widget_request_body import ConnectWidgetRequestBody
from mx_platform_python.models.connect_widget_response import ConnectWidgetResponse
from mx_platform_python.models.connect_widget_response_body import ConnectWidgetResponseBody
from mx_platform_python.models.credential_request import CredentialRequest
from mx_platform_python.models.credential_response import CredentialResponse
from mx_platform_python.models.credentials_response_body import CredentialsResponseBody
from mx_platform_python.models.credit_card_product import CreditCardProduct
from mx_platform_python.models.credit_card_product_response import CreditCardProductResponse
from mx_platform_python.models.enhance_transaction_response import EnhanceTransactionResponse
from mx_platform_python.models.enhance_transactions_request import EnhanceTransactionsRequest
from mx_platform_python.models.enhance_transactions_request_body import EnhanceTransactionsRequestBody
from mx_platform_python.models.enhance_transactions_response_body import EnhanceTransactionsResponseBody
from mx_platform_python.models.goal_request import GoalRequest
from mx_platform_python.models.goal_request_body import GoalRequestBody
from mx_platform_python.models.goal_response import GoalResponse
from mx_platform_python.models.goal_response_body import GoalResponseBody
from mx_platform_python.models.goals_response import GoalsResponse
from mx_platform_python.models.goals_response_body import GoalsResponseBody
from mx_platform_python.models.holding_response import HoldingResponse
from mx_platform_python.models.holding_response_body import HoldingResponseBody
from mx_platform_python.models.holdings_response_body import HoldingsResponseBody
from mx_platform_python.models.image_option_response import ImageOptionResponse
from mx_platform_python.models.insight_response import InsightResponse
from mx_platform_python.models.insight_response_body import InsightResponseBody
from mx_platform_python.models.insight_update_request import InsightUpdateRequest
from mx_platform_python.models.insights_response_body import InsightsResponseBody
from mx_platform_python.models.institution_response import InstitutionResponse
from mx_platform_python.models.institution_response_body import InstitutionResponseBody
from mx_platform_python.models.institutions_response_body import InstitutionsResponseBody
from mx_platform_python.models.managed_account_create_request import ManagedAccountCreateRequest
from mx_platform_python.models.managed_account_create_request_body import ManagedAccountCreateRequestBody
from mx_platform_python.models.managed_account_update_request import ManagedAccountUpdateRequest
from mx_platform_python.models.managed_account_update_request_body import ManagedAccountUpdateRequestBody
from mx_platform_python.models.managed_member_create_request import ManagedMemberCreateRequest
from mx_platform_python.models.managed_member_create_request_body import ManagedMemberCreateRequestBody
from mx_platform_python.models.managed_member_update_request import ManagedMemberUpdateRequest
from mx_platform_python.models.managed_member_update_request_body import ManagedMemberUpdateRequestBody
from mx_platform_python.models.managed_transaction_create_request import ManagedTransactionCreateRequest
from mx_platform_python.models.managed_transaction_create_request_body import ManagedTransactionCreateRequestBody
from mx_platform_python.models.managed_transaction_update_request import ManagedTransactionUpdateRequest
from mx_platform_python.models.managed_transaction_update_request_body import ManagedTransactionUpdateRequestBody
from mx_platform_python.models.member_create_request import MemberCreateRequest
from mx_platform_python.models.member_create_request_body import MemberCreateRequestBody
from mx_platform_python.models.member_response import MemberResponse
from mx_platform_python.models.member_response_body import MemberResponseBody
from mx_platform_python.models.member_resume_request import MemberResumeRequest
from mx_platform_python.models.member_resume_request_body import MemberResumeRequestBody
from mx_platform_python.models.member_status_response import MemberStatusResponse
from mx_platform_python.models.member_status_response_body import MemberStatusResponseBody
from mx_platform_python.models.member_update_request import MemberUpdateRequest
from mx_platform_python.models.member_update_request_body import MemberUpdateRequestBody
from mx_platform_python.models.members_response_body import MembersResponseBody
from mx_platform_python.models.merchant_location_response import MerchantLocationResponse
from mx_platform_python.models.merchant_location_response_body import MerchantLocationResponseBody
from mx_platform_python.models.merchant_response import MerchantResponse
from mx_platform_python.models.merchant_response_body import MerchantResponseBody
from mx_platform_python.models.merchants_response_body import MerchantsResponseBody
from mx_platform_python.models.microdeposit_request import MicrodepositRequest
from mx_platform_python.models.microdeposit_request_body import MicrodepositRequestBody
from mx_platform_python.models.microdeposit_response import MicrodepositResponse
from mx_platform_python.models.microdeposit_response_body import MicrodepositResponseBody
from mx_platform_python.models.microdeposit_verify_request import MicrodepositVerifyRequest
from mx_platform_python.models.microdeposit_verify_request_body import MicrodepositVerifyRequestBody
from mx_platform_python.models.microdeposits_response_body import MicrodepositsResponseBody
from mx_platform_python.models.monthly_cash_flow_profile_request import MonthlyCashFlowProfileRequest
from mx_platform_python.models.monthly_cash_flow_profile_request_body import MonthlyCashFlowProfileRequestBody
from mx_platform_python.models.monthly_cash_flow_response import MonthlyCashFlowResponse
from mx_platform_python.models.monthly_cash_flow_response_body import MonthlyCashFlowResponseBody
from mx_platform_python.models.o_auth_window_response import OAuthWindowResponse
from mx_platform_python.models.o_auth_window_response_body import OAuthWindowResponseBody
from mx_platform_python.models.option_response import OptionResponse
from mx_platform_python.models.pagination_response import PaginationResponse
from mx_platform_python.models.payment_processor_authorization_code_request import PaymentProcessorAuthorizationCodeRequest
from mx_platform_python.models.payment_processor_authorization_code_request_body import PaymentProcessorAuthorizationCodeRequestBody
from mx_platform_python.models.payment_processor_authorization_code_response import PaymentProcessorAuthorizationCodeResponse
from mx_platform_python.models.payment_processor_authorization_code_response_body import PaymentProcessorAuthorizationCodeResponseBody
from mx_platform_python.models.reposition_request import RepositionRequest
from mx_platform_python.models.reposition_request_body import RepositionRequestBody
from mx_platform_python.models.reposition_response_body import RepositionResponseBody
from mx_platform_python.models.reward_response import RewardResponse
from mx_platform_python.models.reward_response_body import RewardResponseBody
from mx_platform_python.models.rewards_response import RewardsResponse
from mx_platform_python.models.rewards_response_body import RewardsResponseBody
from mx_platform_python.models.scheduled_payment_response import ScheduledPaymentResponse
from mx_platform_python.models.scheduled_payments_response_body import ScheduledPaymentsResponseBody
from mx_platform_python.models.spending_plan_account_response import SpendingPlanAccountResponse
from mx_platform_python.models.spending_plan_accounts_response import SpendingPlanAccountsResponse
from mx_platform_python.models.spending_plan_iteration_item_create_request_body import SpendingPlanIterationItemCreateRequestBody
from mx_platform_python.models.spending_plan_iteration_item_response import SpendingPlanIterationItemResponse
from mx_platform_python.models.spending_plan_iteration_items_response_body import SpendingPlanIterationItemsResponseBody
from mx_platform_python.models.spending_plan_iteration_response import SpendingPlanIterationResponse
from mx_platform_python.models.spending_plan_iterations_response import SpendingPlanIterationsResponse
from mx_platform_python.models.spending_plan_response import SpendingPlanResponse
from mx_platform_python.models.spending_plans_response_body import SpendingPlansResponseBody
from mx_platform_python.models.split_transaction_request import SplitTransactionRequest
from mx_platform_python.models.split_transaction_request_body import SplitTransactionRequestBody
from mx_platform_python.models.split_transactions_response_body import SplitTransactionsResponseBody
from mx_platform_python.models.statement_response import StatementResponse
from mx_platform_python.models.statement_response_body import StatementResponseBody
from mx_platform_python.models.statements_response_body import StatementsResponseBody
from mx_platform_python.models.tag_create_request import TagCreateRequest
from mx_platform_python.models.tag_create_request_body import TagCreateRequestBody
from mx_platform_python.models.tag_response import TagResponse
from mx_platform_python.models.tag_response_body import TagResponseBody
from mx_platform_python.models.tag_update_request import TagUpdateRequest
from mx_platform_python.models.tag_update_request_body import TagUpdateRequestBody
from mx_platform_python.models.tagging_create_request import TaggingCreateRequest
from mx_platform_python.models.tagging_create_request_body import TaggingCreateRequestBody
from mx_platform_python.models.tagging_response import TaggingResponse
from mx_platform_python.models.tagging_response_body import TaggingResponseBody
from mx_platform_python.models.tagging_update_request import TaggingUpdateRequest
from mx_platform_python.models.tagging_update_request_body import TaggingUpdateRequestBody
from mx_platform_python.models.taggings_response_body import TaggingsResponseBody
from mx_platform_python.models.tags_response_body import TagsResponseBody
from mx_platform_python.models.tax_document_response import TaxDocumentResponse
from mx_platform_python.models.tax_document_response_body import TaxDocumentResponseBody
from mx_platform_python.models.tax_documents_response_body import TaxDocumentsResponseBody
from mx_platform_python.models.transaction_create_request import TransactionCreateRequest
from mx_platform_python.models.transaction_create_request_body import TransactionCreateRequestBody
from mx_platform_python.models.transaction_create_response_body import TransactionCreateResponseBody
from mx_platform_python.models.transaction_response import TransactionResponse
from mx_platform_python.models.transaction_response_body import TransactionResponseBody
from mx_platform_python.models.transaction_rule_create_request import TransactionRuleCreateRequest
from mx_platform_python.models.transaction_rule_create_request_body import TransactionRuleCreateRequestBody
from mx_platform_python.models.transaction_rule_response import TransactionRuleResponse
from mx_platform_python.models.transaction_rule_response_body import TransactionRuleResponseBody
from mx_platform_python.models.transaction_rule_update_request import TransactionRuleUpdateRequest
from mx_platform_python.models.transaction_rule_update_request_body import TransactionRuleUpdateRequestBody
from mx_platform_python.models.transaction_rules_response_body import TransactionRulesResponseBody
from mx_platform_python.models.transaction_update_request import TransactionUpdateRequest
from mx_platform_python.models.transaction_update_request_body import TransactionUpdateRequestBody
from mx_platform_python.models.transactions_response_body import TransactionsResponseBody
from mx_platform_python.models.update_goal_request import UpdateGoalRequest
from mx_platform_python.models.update_goal_request_body import UpdateGoalRequestBody
from mx_platform_python.models.user_create_request import UserCreateRequest
from mx_platform_python.models.user_create_request_body import UserCreateRequestBody
from mx_platform_python.models.user_response import UserResponse
from mx_platform_python.models.user_response_body import UserResponseBody
from mx_platform_python.models.user_update_request import UserUpdateRequest
from mx_platform_python.models.user_update_request_body import UserUpdateRequestBody
from mx_platform_python.models.users_response_body import UsersResponseBody
from mx_platform_python.models.widget_request import WidgetRequest
from mx_platform_python.models.widget_request_body import WidgetRequestBody
from mx_platform_python.models.widget_response import WidgetResponse
from mx_platform_python.models.widget_response_body import WidgetResponseBody
