# coding: utf-8

# flake8: noqa
"""
    TON Rocket Pay API

    This API based on @tonRocketBot (@ton_rocket_test_bot for testnest) Payment System. In order to use it, you need to get API key from bot. Open it and go to Rocket Pay > Create App > API token.<br><br>This page is fully interactive. Provide obtained API key to AUTHORIZE button on the right, and you can try all API methods by simply clicking buttons and filling forms here<br><br>API token must be specified in header of each request. Header name is <b>Rocket-Pay-Key</b>. Only exception is /version endpoint<br><br>If endpoint can send webhooks in response, it is provided on endpoint page on Callbacks bookmark. Now only /tg-invoices endpoint sends webhooks. You can turn them on in bot in app management page<br>In order to verify webhooks information integrity, we send you in headers parameter <b>rocket-pay-signature</b>, which is hex representation of HMAC-SHA-256 signature used to sign request body with a secret key that is SHA256 hash of your app token.<br><br>This specification fully complies with OpenAPI 3.0 standard, so if you want to see schemas of request bodies or responses, please click \"Schema\" inside endpoint. All mandatory fields marked with *, all types and limits also described inside schemas<br><br><h2>Change Log</h2><h3>version 1.3</h3>Added support for multi-invoices:<br>post /tg-invoices - added request parameter numPayments (default - 1), added response parameter totalActivations, activationsLeft<br>webhook /tg-invoices - added parameter payment (telegram user ID and number of items purchased for this payment)<br>get /tg-invoices - added response parameter totalActivations, activationsLeft<br>get /tg-invoices/{id} - added response parameter numPayments and payments (list, info about payments that were maid for this invoice)<br>  # noqa: E501

    OpenAPI spec version: 1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from rocketpay.models.all_of_cheque_disabled_languages import AllOfChequeDisabledLanguages
from rocketpay.models.all_of_coin_dto_fee_withdraw import AllOfCoinDtoFeeWithdraw
from rocketpay.models.all_of_pay_invoice_dto_payment import AllOfPayInvoiceDtoPayment
from rocketpay.models.all_of_short_cheque_dto_disabled_languages import AllOfShortChequeDtoDisabledLanguages
from rocketpay.models.all_of_subscription_interval import AllOfSubscriptionInterval
from rocketpay.models.all_of_subscription_tg_resource import AllOfSubscriptionTgResource
from rocketpay.models.api_bad_request_error import ApiBadRequestError
from rocketpay.models.api_error import ApiError
from rocketpay.models.app import App
from rocketpay.models.app_balance import AppBalance
from rocketpay.models.app_dto import AppDto
from rocketpay.models.available_coins import AvailableCoins
from rocketpay.models.available_coins_data import AvailableCoinsData
from rocketpay.models.check_subscription_dto import CheckSubscriptionDto
from rocketpay.models.cheque import Cheque
from rocketpay.models.coin_dto import CoinDto
from rocketpay.models.create_cheque_dto import CreateChequeDto
from rocketpay.models.create_invoice_dto import CreateInvoiceDto
from rocketpay.models.create_subscription_dto import CreateSubscriptionDto
from rocketpay.models.create_transfer_dto import CreateTransferDto
from rocketpay.models.create_withdrawal_dto import CreateWithdrawalDto
from rocketpay.models.delete_response_dto import DeleteResponseDto
from rocketpay.models.edit_subscription_interval_dto import EditSubscriptionIntervalDto
from rocketpay.models.full_invoice_dto import FullInvoiceDto
from rocketpay.models.full_invoice_response_dto import FullInvoiceResponseDto
from rocketpay.models.invoice import Invoice
from rocketpay.models.paginated_invoice_response import PaginatedInvoiceResponse
from rocketpay.models.paginated_short_cheque_dto_response import PaginatedShortChequeDtoResponse
from rocketpay.models.paginated_subscription_response import PaginatedSubscriptionResponse
from rocketpay.models.pagination_dto import PaginationDto
from rocketpay.models.pay_invoice_dto import PayInvoiceDto
from rocketpay.models.pay_invoice_stat_dto import PayInvoiceStatDto
from rocketpay.models.property_error import PropertyError
from rocketpay.models.rates import Rates
from rocketpay.models.response_dto import ResponseDto
from rocketpay.models.set import Set
from rocketpay.models.short_cheque_dto import ShortChequeDto
from rocketpay.models.simple_cheque_response import SimpleChequeResponse
from rocketpay.models.simple_full_invoice_dto_response import SimpleFullInvoiceDtoResponse
from rocketpay.models.simple_invoice_response import SimpleInvoiceResponse
from rocketpay.models.simple_short_cheque_dto_response import SimpleShortChequeDtoResponse
from rocketpay.models.simple_subscription_interval_response import SimpleSubscriptionIntervalResponse
from rocketpay.models.simple_subscription_response import SimpleSubscriptionResponse
from rocketpay.models.simple_transfer_dto_response import SimpleTransferDtoResponse
from rocketpay.models.simple_user_subscription_response import SimpleUserSubscriptionResponse
from rocketpay.models.simple_withdrawal_dto_response import SimpleWithdrawalDtoResponse
from rocketpay.models.subscription import Subscription
from rocketpay.models.subscription_interval import SubscriptionInterval
from rocketpay.models.subscription_interval_dto import SubscriptionIntervalDto
from rocketpay.models.subscription_resource import SubscriptionResource
from rocketpay.models.tg_resource import TgResource
from rocketpay.models.transfer_dto import TransferDto
from rocketpay.models.update_cheque_dto import UpdateChequeDto
from rocketpay.models.user_subscription import UserSubscription
from rocketpay.models.user_subscription_transaction import UserSubscriptionTransaction
from rocketpay.models.version import Version
from rocketpay.models.webhook_dto import WebhookDto
from rocketpay.models.withdraw_fee_dto import WithdrawFeeDto
from rocketpay.models.withdrawal_dto import WithdrawalDto
