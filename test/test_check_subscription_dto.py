# coding: utf-8

"""
    TON Rocket Pay API

    This API based on @tonRocketBot (@ton_rocket_test_bot for testnest) Payment System. In order to use it, you need to get API key from bot. Open it and go to Rocket Pay > Create App > API token.<br><br>This page is fully interactive. Provide obtained API key to AUTHORIZE button on the right, and you can try all API methods by simply clicking buttons and filling forms here<br><br>API token must be specified in header of each request. Header name is <b>Rocket-Pay-Key</b>. Only exception is /version endpoint<br><br>If endpoint can send webhooks in response, it is provided on endpoint page on Callbacks bookmark. Now only /tg-invoices endpoint sends webhooks. You can turn them on in bot in app management page<br>In order to verify webhooks information integrity, we send you in headers parameter <b>rocket-pay-signature</b>, which is hex representation of HMAC-SHA-256 signature used to sign request body with a secret key that is SHA256 hash of your app token.<br><br>This specification fully complies with OpenAPI 3.0 standard, so if you want to see schemas of request bodies or responses, please click \"Schema\" inside endpoint. All mandatory fields marked with *, all types and limits also described inside schemas<br><br><h2>Change Log</h2><h3>version 1.3</h3>Added support for multi-invoices:<br>post /tg-invoices - added request parameter numPayments (default - 1), added response parameter totalActivations, activationsLeft<br>webhook /tg-invoices - added parameter payment (telegram user ID and number of items purchased for this payment)<br>get /tg-invoices - added response parameter totalActivations, activationsLeft<br>get /tg-invoices/{id} - added response parameter numPayments and payments (list, info about payments that were maid for this invoice)<br>  # noqa: E501

    OpenAPI spec version: 1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import rocketpay
from rocketpay.models.check_subscription_dto import CheckSubscriptionDto  # noqa: E501
from rocketpay.rest import ApiException


class TestCheckSubscriptionDto(unittest.TestCase):
    """CheckSubscriptionDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCheckSubscriptionDto(self):
        """Test CheckSubscriptionDto"""
        # FIXME: construct object with mandatory attributes with example values
        # model = rocketpay.models.check_subscription_dto.CheckSubscriptionDto()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
