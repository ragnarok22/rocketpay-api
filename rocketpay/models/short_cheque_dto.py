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

class ShortChequeDto(object):
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
        'id': 'float',
        'currency': 'str',
        'total': 'float',
        'per_user': 'float',
        'users': 'float',
        'password': 'str',
        'description': 'str',
        'send_notifications': 'bool',
        'captcha_enabled': 'bool',
        'ref_program_percents': 'float',
        'ref_reward_per_user': 'float',
        'state': 'str',
        'link': 'str',
        'disabled_languages': 'AllOfShortChequeDtoDisabledLanguages',
        'for_premium': 'bool',
        'linked_wallet': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'currency': 'currency',
        'total': 'total',
        'per_user': 'perUser',
        'users': 'users',
        'password': 'password',
        'description': 'description',
        'send_notifications': 'sendNotifications',
        'captcha_enabled': 'captchaEnabled',
        'ref_program_percents': 'refProgramPercents',
        'ref_reward_per_user': 'refRewardPerUser',
        'state': 'state',
        'link': 'link',
        'disabled_languages': 'disabledLanguages',
        'for_premium': 'forPremium',
        'linked_wallet': 'linkedWallet'
    }

    def __init__(self, id=None, currency=None, total=None, per_user=None, users=None, password=None, description=None, send_notifications=None, captcha_enabled=None, ref_program_percents=None, ref_reward_per_user=None, state=None, link=None, disabled_languages=None, for_premium=None, linked_wallet=None):  # noqa: E501
        """ShortChequeDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._currency = None
        self._total = None
        self._per_user = None
        self._users = None
        self._password = None
        self._description = None
        self._send_notifications = None
        self._captcha_enabled = None
        self._ref_program_percents = None
        self._ref_reward_per_user = None
        self._state = None
        self._link = None
        self._disabled_languages = None
        self._for_premium = None
        self._linked_wallet = None
        self.discriminator = None
        self.id = id
        self.currency = currency
        self.total = total
        self.per_user = per_user
        self.users = users
        self.password = password
        self.description = description
        self.send_notifications = send_notifications
        self.captcha_enabled = captcha_enabled
        self.ref_program_percents = ref_program_percents
        self.ref_reward_per_user = ref_reward_per_user
        self.state = state
        self.link = link
        self.disabled_languages = disabled_languages
        self.for_premium = for_premium
        self.linked_wallet = linked_wallet

    @property
    def id(self):
        """Gets the id of this ShortChequeDto.  # noqa: E501

        Cheque ID  # noqa: E501

        :return: The id of this ShortChequeDto.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShortChequeDto.

        Cheque ID  # noqa: E501

        :param id: The id of this ShortChequeDto.  # noqa: E501
        :type: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def currency(self):
        """Gets the currency of this ShortChequeDto.  # noqa: E501


        :return: The currency of this ShortChequeDto.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ShortChequeDto.


        :param currency: The currency of this ShortChequeDto.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def total(self):
        """Gets the total of this ShortChequeDto.  # noqa: E501

        Total amount of cheque (this amount is charged from balance)  # noqa: E501

        :return: The total of this ShortChequeDto.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShortChequeDto.

        Total amount of cheque (this amount is charged from balance)  # noqa: E501

        :param total: The total of this ShortChequeDto.  # noqa: E501
        :type: float
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def per_user(self):
        """Gets the per_user of this ShortChequeDto.  # noqa: E501

        Amount of cheque per user  # noqa: E501

        :return: The per_user of this ShortChequeDto.  # noqa: E501
        :rtype: float
        """
        return self._per_user

    @per_user.setter
    def per_user(self, per_user):
        """Sets the per_user of this ShortChequeDto.

        Amount of cheque per user  # noqa: E501

        :param per_user: The per_user of this ShortChequeDto.  # noqa: E501
        :type: float
        """
        if per_user is None:
            raise ValueError("Invalid value for `per_user`, must not be `None`")  # noqa: E501

        self._per_user = per_user

    @property
    def users(self):
        """Gets the users of this ShortChequeDto.  # noqa: E501

        Number of users that can activate your cheque  # noqa: E501

        :return: The users of this ShortChequeDto.  # noqa: E501
        :rtype: float
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this ShortChequeDto.

        Number of users that can activate your cheque  # noqa: E501

        :param users: The users of this ShortChequeDto.  # noqa: E501
        :type: float
        """
        if users is None:
            raise ValueError("Invalid value for `users`, must not be `None`")  # noqa: E501

        self._users = users

    @property
    def password(self):
        """Gets the password of this ShortChequeDto.  # noqa: E501

        Cheque password  # noqa: E501

        :return: The password of this ShortChequeDto.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ShortChequeDto.

        Cheque password  # noqa: E501

        :param password: The password of this ShortChequeDto.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def description(self):
        """Gets the description of this ShortChequeDto.  # noqa: E501

        Cheque description  # noqa: E501

        :return: The description of this ShortChequeDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShortChequeDto.

        Cheque description  # noqa: E501

        :param description: The description of this ShortChequeDto.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def send_notifications(self):
        """Gets the send_notifications of this ShortChequeDto.  # noqa: E501

        send notifications about cheque activation to application cheque webhook or not  # noqa: E501

        :return: The send_notifications of this ShortChequeDto.  # noqa: E501
        :rtype: bool
        """
        return self._send_notifications

    @send_notifications.setter
    def send_notifications(self, send_notifications):
        """Sets the send_notifications of this ShortChequeDto.

        send notifications about cheque activation to application cheque webhook or not  # noqa: E501

        :param send_notifications: The send_notifications of this ShortChequeDto.  # noqa: E501
        :type: bool
        """
        if send_notifications is None:
            raise ValueError("Invalid value for `send_notifications`, must not be `None`")  # noqa: E501

        self._send_notifications = send_notifications

    @property
    def captcha_enabled(self):
        """Gets the captcha_enabled of this ShortChequeDto.  # noqa: E501

        enable / disable cheque captcha  # noqa: E501

        :return: The captcha_enabled of this ShortChequeDto.  # noqa: E501
        :rtype: bool
        """
        return self._captcha_enabled

    @captcha_enabled.setter
    def captcha_enabled(self, captcha_enabled):
        """Sets the captcha_enabled of this ShortChequeDto.

        enable / disable cheque captcha  # noqa: E501

        :param captcha_enabled: The captcha_enabled of this ShortChequeDto.  # noqa: E501
        :type: bool
        """
        if captcha_enabled is None:
            raise ValueError("Invalid value for `captcha_enabled`, must not be `None`")  # noqa: E501

        self._captcha_enabled = captcha_enabled

    @property
    def ref_program_percents(self):
        """Gets the ref_program_percents of this ShortChequeDto.  # noqa: E501

        percentage of cheque that rewarded for referral program  # noqa: E501

        :return: The ref_program_percents of this ShortChequeDto.  # noqa: E501
        :rtype: float
        """
        return self._ref_program_percents

    @ref_program_percents.setter
    def ref_program_percents(self, ref_program_percents):
        """Sets the ref_program_percents of this ShortChequeDto.

        percentage of cheque that rewarded for referral program  # noqa: E501

        :param ref_program_percents: The ref_program_percents of this ShortChequeDto.  # noqa: E501
        :type: float
        """
        if ref_program_percents is None:
            raise ValueError("Invalid value for `ref_program_percents`, must not be `None`")  # noqa: E501

        self._ref_program_percents = ref_program_percents

    @property
    def ref_reward_per_user(self):
        """Gets the ref_reward_per_user of this ShortChequeDto.  # noqa: E501

        amount of referral user reward  # noqa: E501

        :return: The ref_reward_per_user of this ShortChequeDto.  # noqa: E501
        :rtype: float
        """
        return self._ref_reward_per_user

    @ref_reward_per_user.setter
    def ref_reward_per_user(self, ref_reward_per_user):
        """Sets the ref_reward_per_user of this ShortChequeDto.

        amount of referral user reward  # noqa: E501

        :param ref_reward_per_user: The ref_reward_per_user of this ShortChequeDto.  # noqa: E501
        :type: float
        """
        if ref_reward_per_user is None:
            raise ValueError("Invalid value for `ref_reward_per_user`, must not be `None`")  # noqa: E501

        self._ref_reward_per_user = ref_reward_per_user

    @property
    def state(self):
        """Gets the state of this ShortChequeDto.  # noqa: E501

        Active - cheque created and has unclaimed activations. Completed - cheque totally activated.  # noqa: E501

        :return: The state of this ShortChequeDto.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShortChequeDto.

        Active - cheque created and has unclaimed activations. Completed - cheque totally activated.  # noqa: E501

        :param state: The state of this ShortChequeDto.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["active", "completed", "draft"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def link(self):
        """Gets the link of this ShortChequeDto.  # noqa: E501


        :return: The link of this ShortChequeDto.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this ShortChequeDto.


        :param link: The link of this ShortChequeDto.  # noqa: E501
        :type: str
        """
        if link is None:
            raise ValueError("Invalid value for `link`, must not be `None`")  # noqa: E501

        self._link = link

    @property
    def disabled_languages(self):
        """Gets the disabled_languages of this ShortChequeDto.  # noqa: E501

        Disable languages  # noqa: E501

        :return: The disabled_languages of this ShortChequeDto.  # noqa: E501
        :rtype: AllOfShortChequeDtoDisabledLanguages
        """
        return self._disabled_languages

    @disabled_languages.setter
    def disabled_languages(self, disabled_languages):
        """Sets the disabled_languages of this ShortChequeDto.

        Disable languages  # noqa: E501

        :param disabled_languages: The disabled_languages of this ShortChequeDto.  # noqa: E501
        :type: AllOfShortChequeDtoDisabledLanguages
        """
        if disabled_languages is None:
            raise ValueError("Invalid value for `disabled_languages`, must not be `None`")  # noqa: E501

        self._disabled_languages = disabled_languages

    @property
    def for_premium(self):
        """Gets the for_premium of this ShortChequeDto.  # noqa: E501

        Only users with Telegram Premium can activate this cheque  # noqa: E501

        :return: The for_premium of this ShortChequeDto.  # noqa: E501
        :rtype: bool
        """
        return self._for_premium

    @for_premium.setter
    def for_premium(self, for_premium):
        """Sets the for_premium of this ShortChequeDto.

        Only users with Telegram Premium can activate this cheque  # noqa: E501

        :param for_premium: The for_premium of this ShortChequeDto.  # noqa: E501
        :type: bool
        """
        if for_premium is None:
            raise ValueError("Invalid value for `for_premium`, must not be `None`")  # noqa: E501

        self._for_premium = for_premium

    @property
    def linked_wallet(self):
        """Gets the linked_wallet of this ShortChequeDto.  # noqa: E501

        Only users with connected wallets can activate this cheque  # noqa: E501

        :return: The linked_wallet of this ShortChequeDto.  # noqa: E501
        :rtype: bool
        """
        return self._linked_wallet

    @linked_wallet.setter
    def linked_wallet(self, linked_wallet):
        """Sets the linked_wallet of this ShortChequeDto.

        Only users with connected wallets can activate this cheque  # noqa: E501

        :param linked_wallet: The linked_wallet of this ShortChequeDto.  # noqa: E501
        :type: bool
        """
        if linked_wallet is None:
            raise ValueError("Invalid value for `linked_wallet`, must not be `None`")  # noqa: E501

        self._linked_wallet = linked_wallet

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
        if issubclass(ShortChequeDto, dict):
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
        if not isinstance(other, ShortChequeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
