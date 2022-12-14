# coding: utf-8

"""
    TON Rocket Pay API

    This API based on @tonRocketBot (@ton_rocket_test_bot for testnest) Payment System. In order to use it, you need to get API key from bot. Open it and go to Rocket Pay > Create App > API token.<br><br>This page is fully interactive. Provide obtained API key to AUTHORIZE button on the right, and you can try all API methods by simply clicking buttons and filling forms here<br><br>API token must be specified in header of each request. Header name is <b>Rocket-Pay-Key</b>. Only exception is /version endpoint<br><br>If endpoint can send webhooks in response, it is provided on endpoint page on Callbacks bookmark. Now only /tg-invoices endpoint sends webhooks. You can turn them on in bot in app management page<br>In order to verify webhooks information integrity, we send you in headers parameter <b>rocket-pay-signature</b>, which is hex representation of HMAC-SHA-256 signature used to sign request body with a secret key that is SHA256 hash of your app token.<br><br>This specification fully complies with OpenAPI 3.0 standard, so if you want to see schemas of request bodies or responses, please click \"Schema\" inside endpoint. All mandatory fields marked with *, all types and limits also described inside schemas<br><br><h2>Change Log</h2><h3>version 1.3</h3>Added support for multi-invoices:<br>post /tg-invoices - added request parameter numPayments (default - 1), added response parameter totalActivations, activationsLeft<br>webhook /tg-invoices - added parameter payment (telegram user ID and number of items purchased for this payment)<br>get /tg-invoices - added response parameter totalActivations, activationsLeft<br>get /tg-invoices/{id} - added response parameter numPayments and payments (list, info about payments that were maid for this invoice)<br>  # noqa: E501

    OpenAPI spec version: 1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from rocketpay.api_client import ApiClient


class CurrenciesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def currencies_controller_get_coins(self, **kwargs):  # noqa: E501
        """Returns available currencies  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.currencies_controller_get_coins(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AvailableCoins
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.currencies_controller_get_coins_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.currencies_controller_get_coins_with_http_info(**kwargs)  # noqa: E501
            return data

    def currencies_controller_get_coins_with_http_info(self, **kwargs):  # noqa: E501
        """Returns available currencies  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.currencies_controller_get_coins_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AvailableCoins
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method currencies_controller_get_coins" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/currencies/available', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AvailableCoins',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def currencies_controller_get_rates(self, coin_from, coin_to, **kwargs):  # noqa: E501
        """Returns rates from simple simple-order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.currencies_controller_get_rates(coin_from, coin_to, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float coin_from: ID of coin from (required)
        :param float coin_to: ID of coin to (required)
        :return: Rates
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.currencies_controller_get_rates_with_http_info(coin_from, coin_to, **kwargs)  # noqa: E501
        else:
            (data) = self.currencies_controller_get_rates_with_http_info(coin_from, coin_to, **kwargs)  # noqa: E501
            return data

    def currencies_controller_get_rates_with_http_info(self, coin_from, coin_to, **kwargs):  # noqa: E501
        """Returns rates from simple simple-order  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.currencies_controller_get_rates_with_http_info(coin_from, coin_to, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float coin_from: ID of coin from (required)
        :param float coin_to: ID of coin to (required)
        :return: Rates
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['coin_from', 'coin_to']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method currencies_controller_get_rates" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'coin_from' is set
        if ('coin_from' not in params or
                params['coin_from'] is None):
            raise ValueError("Missing the required parameter `coin_from` when calling `currencies_controller_get_rates`")  # noqa: E501
        # verify the required parameter 'coin_to' is set
        if ('coin_to' not in params or
                params['coin_to'] is None):
            raise ValueError("Missing the required parameter `coin_to` when calling `currencies_controller_get_rates`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'coin_from' in params:
            query_params.append(('coinFrom', params['coin_from']))  # noqa: E501
        if 'coin_to' in params:
            query_params.append(('coinTo', params['coin_to']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/currencies/rate', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Rates',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
