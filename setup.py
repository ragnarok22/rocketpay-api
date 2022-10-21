# coding: utf-8

"""
    TON Rocket Pay API

    This API based on @tonRocketBot (@ton_rocket_test_bot for testnest) Payment System. In order to use it, you need to get API key from bot. Open it and go to Rocket Pay > Create App > API token.<br><br>This page is fully interactive. Provide obtained API key to AUTHORIZE button on the right, and you can try all API methods by simply clicking buttons and filling forms here<br><br>API token must be specified in header of each request. Header name is <b>Rocket-Pay-Key</b>. Only exception is /version endpoint<br><br>If endpoint can send webhooks in response, it is provided on endpoint page on Callbacks bookmark. Now only /tg-invoices endpoint sends webhooks. You can turn them on in bot in app management page<br>In order to verify webhooks information integrity, we send you in headers parameter <b>rocket-pay-signature</b>, which is hex representation of HMAC-SHA-256 signature used to sign request body with a secret key that is SHA256 hash of your app token.<br><br>This specification fully complies with OpenAPI 3.0 standard, so if you want to see schemas of request bodies or responses, please click \"Schema\" inside endpoint. All mandatory fields marked with *, all types and limits also described inside schemas<br><br><h2>Change Log</h2><h3>version 1.3</h3>Added support for multi-invoices:<br>post /tg-invoices - added request parameter numPayments (default - 1), added response parameter totalActivations, activationsLeft<br>webhook /tg-invoices - added parameter payment (telegram user ID and number of items purchased for this payment)<br>get /tg-invoices - added response parameter totalActivations, activationsLeft<br>get /tg-invoices/{id} - added response parameter numPayments and payments (list, info about payments that were maid for this invoice)<br>  # noqa: E501

    OpenAPI spec version: 1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="TON Rocket Pay API",
    author_email="",
    url="",
    keywords=["Swagger", "TON Rocket Pay API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This API based on @tonRocketBot (@ton_rocket_test_bot for testnest) Payment System. In order to use it, you need to get API key from bot. Open it and go to Rocket Pay &gt; Create App &gt; API token.&lt;br&gt;&lt;br&gt;This page is fully interactive. Provide obtained API key to AUTHORIZE button on the right, and you can try all API methods by simply clicking buttons and filling forms here&lt;br&gt;&lt;br&gt;API token must be specified in header of each request. Header name is &lt;b&gt;Rocket-Pay-Key&lt;/b&gt;. Only exception is /version endpoint&lt;br&gt;&lt;br&gt;If endpoint can send webhooks in response, it is provided on endpoint page on Callbacks bookmark. Now only /tg-invoices endpoint sends webhooks. You can turn them on in bot in app management page&lt;br&gt;In order to verify webhooks information integrity, we send you in headers parameter &lt;b&gt;rocket-pay-signature&lt;/b&gt;, which is hex representation of HMAC-SHA-256 signature used to sign request body with a secret key that is SHA256 hash of your app token.&lt;br&gt;&lt;br&gt;This specification fully complies with OpenAPI 3.0 standard, so if you want to see schemas of request bodies or responses, please click \&quot;Schema\&quot; inside endpoint. All mandatory fields marked with *, all types and limits also described inside schemas&lt;br&gt;&lt;br&gt;&lt;h2&gt;Change Log&lt;/h2&gt;&lt;h3&gt;version 1.3&lt;/h3&gt;Added support for multi-invoices:&lt;br&gt;post /tg-invoices - added request parameter numPayments (default - 1), added response parameter totalActivations, activationsLeft&lt;br&gt;webhook /tg-invoices - added parameter payment (telegram user ID and number of items purchased for this payment)&lt;br&gt;get /tg-invoices - added response parameter totalActivations, activationsLeft&lt;br&gt;get /tg-invoices/{id} - added response parameter numPayments and payments (list, info about payments that were maid for this invoice)&lt;br&gt;  # noqa: E501
    """
)
