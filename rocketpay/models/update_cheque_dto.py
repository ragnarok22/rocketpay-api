# coding: utf-8

"""
    TON Rocket Pay API

    This API based on @tonRocketBot (@ton_rocket_test_bot for testnest) Payment System. In order to use it, you need to get API key from bot. Open it and go to Rocket Pay > Create App > API token.<br><br>This page is fully interactive. Provide obtained API key to AUTHORIZE button on the right, and you can try all API methods by simply clicking buttons and filling forms here<br><br>API token must be specified in header of each request. Header name is <b>Rocket-Pay-Key</b>. Only exception is /version endpoint<br><br>If endpoint can send webhooks in response, it is provided on endpoint page on Callbacks bookmark. Now only /tg-invoices endpoint sends webhooks. You can turn them on in bot in app management page<br>In order to verify webhooks information integrity, we send you in headers parameter <b>rocket-pay-signature</b>, which is hex representation of HMAC-SHA-256 signature used to sign request body with a secret key that is SHA256 hash of your app token.<br><br>This specification fully complies with OpenAPI 3.0 standard, so if you want to see schemas of request bodies or responses, please click \"Schema\" inside endpoint. All mandatory fields marked with *, all types and limits also described inside schemas<br><br><h2>Change Log</h2><h3>version 1.3</h3>Added support for multi-invoices:<br>post /tg-invoices - added request parameter numPayments (default - 1), added response parameter totalActivations, activationsLeft<br>webhook /tg-invoices - added parameter payment (telegram user ID and number of items purchased for this payment)<br>get /tg-invoices - added response parameter totalActivations, activationsLeft<br>get /tg-invoices/{id} - added response parameter numPayments and payments (list, info about payments that were maid for this invoice)<br>  # noqa: E501

    OpenAPI spec version: 1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UpdateChequeDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'password': 'str',
        'description': 'str',
        'send_notifications': 'bool',
        'enable_captcha': 'bool',
        'telegram_resources_ids': 'list[str]',
        'for_premium': 'bool',
        'linked_wallet': 'bool',
        'disabled_languages': 'list[str]'
    }

    attribute_map = {
        'password': 'password',
        'description': 'description',
        'send_notifications': 'sendNotifications',
        'enable_captcha': 'enableCaptcha',
        'telegram_resources_ids': 'telegramResourcesIds',
        'for_premium': 'forPremium',
        'linked_wallet': 'linkedWallet',
        'disabled_languages': 'disabledLanguages'
    }

    def __init__(self, password=None, description=None, send_notifications=True, enable_captcha=True, telegram_resources_ids=None, for_premium=False, linked_wallet=False, disabled_languages=None):  # noqa: E501
        """UpdateChequeDto - a model defined in Swagger"""  # noqa: E501
        self._password = None
        self._description = None
        self._send_notifications = None
        self._enable_captcha = None
        self._telegram_resources_ids = None
        self._for_premium = None
        self._linked_wallet = None
        self._disabled_languages = None
        self.discriminator = None
        if password is not None:
            self.password = password
        if description is not None:
            self.description = description
        if send_notifications is not None:
            self.send_notifications = send_notifications
        if enable_captcha is not None:
            self.enable_captcha = enable_captcha
        if telegram_resources_ids is not None:
            self.telegram_resources_ids = telegram_resources_ids
        if for_premium is not None:
            self.for_premium = for_premium
        if linked_wallet is not None:
            self.linked_wallet = linked_wallet
        if disabled_languages is not None:
            self.disabled_languages = disabled_languages

    @property
    def password(self):
        """Gets the password of this UpdateChequeDto.  # noqa: E501

        Password for cheque  # noqa: E501

        :return: The password of this UpdateChequeDto.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UpdateChequeDto.

        Password for cheque  # noqa: E501

        :param password: The password of this UpdateChequeDto.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def description(self):
        """Gets the description of this UpdateChequeDto.  # noqa: E501

        Description for cheque  # noqa: E501

        :return: The description of this UpdateChequeDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateChequeDto.

        Description for cheque  # noqa: E501

        :param description: The description of this UpdateChequeDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def send_notifications(self):
        """Gets the send_notifications of this UpdateChequeDto.  # noqa: E501

        Send notifications about activations  # noqa: E501

        :return: The send_notifications of this UpdateChequeDto.  # noqa: E501
        :rtype: bool
        """
        return self._send_notifications

    @send_notifications.setter
    def send_notifications(self, send_notifications):
        """Sets the send_notifications of this UpdateChequeDto.

        Send notifications about activations  # noqa: E501

        :param send_notifications: The send_notifications of this UpdateChequeDto.  # noqa: E501
        :type: bool
        """

        self._send_notifications = send_notifications

    @property
    def enable_captcha(self):
        """Gets the enable_captcha of this UpdateChequeDto.  # noqa: E501

        Enable captcha  # noqa: E501

        :return: The enable_captcha of this UpdateChequeDto.  # noqa: E501
        :rtype: bool
        """
        return self._enable_captcha

    @enable_captcha.setter
    def enable_captcha(self, enable_captcha):
        """Sets the enable_captcha of this UpdateChequeDto.

        Enable captcha  # noqa: E501

        :param enable_captcha: The enable_captcha of this UpdateChequeDto.  # noqa: E501
        :type: bool
        """

        self._enable_captcha = enable_captcha

    @property
    def telegram_resources_ids(self):
        """Gets the telegram_resources_ids of this UpdateChequeDto.  # noqa: E501

        IDs of telegram resources (groups, channels, private groups)  # noqa: E501

        :return: The telegram_resources_ids of this UpdateChequeDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._telegram_resources_ids

    @telegram_resources_ids.setter
    def telegram_resources_ids(self, telegram_resources_ids):
        """Sets the telegram_resources_ids of this UpdateChequeDto.

        IDs of telegram resources (groups, channels, private groups)  # noqa: E501

        :param telegram_resources_ids: The telegram_resources_ids of this UpdateChequeDto.  # noqa: E501
        :type: list[str]
        """

        self._telegram_resources_ids = telegram_resources_ids

    @property
    def for_premium(self):
        """Gets the for_premium of this UpdateChequeDto.  # noqa: E501

        Only users with Telegram Premium can activate this cheque  # noqa: E501

        :return: The for_premium of this UpdateChequeDto.  # noqa: E501
        :rtype: bool
        """
        return self._for_premium

    @for_premium.setter
    def for_premium(self, for_premium):
        """Sets the for_premium of this UpdateChequeDto.

        Only users with Telegram Premium can activate this cheque  # noqa: E501

        :param for_premium: The for_premium of this UpdateChequeDto.  # noqa: E501
        :type: bool
        """

        self._for_premium = for_premium

    @property
    def linked_wallet(self):
        """Gets the linked_wallet of this UpdateChequeDto.  # noqa: E501

        Only users with linked wallet can activate this cheque  # noqa: E501

        :return: The linked_wallet of this UpdateChequeDto.  # noqa: E501
        :rtype: bool
        """
        return self._linked_wallet

    @linked_wallet.setter
    def linked_wallet(self, linked_wallet):
        """Sets the linked_wallet of this UpdateChequeDto.

        Only users with linked wallet can activate this cheque  # noqa: E501

        :param linked_wallet: The linked_wallet of this UpdateChequeDto.  # noqa: E501
        :type: bool
        """

        self._linked_wallet = linked_wallet

    @property
    def disabled_languages(self):
        """Gets the disabled_languages of this UpdateChequeDto.  # noqa: E501

        Disable languages  # noqa: E501

        :return: The disabled_languages of this UpdateChequeDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._disabled_languages

    @disabled_languages.setter
    def disabled_languages(self, disabled_languages):
        """Sets the disabled_languages of this UpdateChequeDto.

        Disable languages  # noqa: E501

        :param disabled_languages: The disabled_languages of this UpdateChequeDto.  # noqa: E501
        :type: list[str]
        """

        self._disabled_languages = disabled_languages

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UpdateChequeDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateChequeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other