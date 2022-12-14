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

class Invoice(object):
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
        'amount': 'float',
        'description': 'str',
        'hidden_message': 'str',
        'payload': 'str',
        'callback_url': 'str',
        'currency': 'str',
        'created': 'datetime',
        'paid': 'datetime',
        'status': 'str',
        'expired_in': 'float',
        'link': 'str',
        'total_activations': 'float',
        'activations_left': 'float'
    }

    attribute_map = {
        'id': 'id',
        'amount': 'amount',
        'description': 'description',
        'hidden_message': 'hiddenMessage',
        'payload': 'payload',
        'callback_url': 'callbackUrl',
        'currency': 'currency',
        'created': 'created',
        'paid': 'paid',
        'status': 'status',
        'expired_in': 'expiredIn',
        'link': 'link',
        'total_activations': 'totalActivations',
        'activations_left': 'activationsLeft'
    }

    def __init__(self, id=None, amount=None, description=None, hidden_message=None, payload=None, callback_url=None, currency=None, created=None, paid=None, status=None, expired_in=0, link=None, total_activations=None, activations_left=None):  # noqa: E501
        """Invoice - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._amount = None
        self._description = None
        self._hidden_message = None
        self._payload = None
        self._callback_url = None
        self._currency = None
        self._created = None
        self._paid = None
        self._status = None
        self._expired_in = None
        self._link = None
        self._total_activations = None
        self._activations_left = None
        self.discriminator = None
        self.id = id
        self.amount = amount
        if description is not None:
            self.description = description
        if hidden_message is not None:
            self.hidden_message = hidden_message
        if payload is not None:
            self.payload = payload
        if callback_url is not None:
            self.callback_url = callback_url
        self.currency = currency
        self.created = created
        if paid is not None:
            self.paid = paid
        self.status = status
        if expired_in is not None:
            self.expired_in = expired_in
        self.link = link
        self.total_activations = total_activations
        self.activations_left = activations_left

    @property
    def id(self):
        """Gets the id of this Invoice.  # noqa: E501

        Invoice ID  # noqa: E501

        :return: The id of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Invoice.

        Invoice ID  # noqa: E501

        :param id: The id of this Invoice.  # noqa: E501
        :type: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def amount(self):
        """Gets the amount of this Invoice.  # noqa: E501

        Amount of invoice  # noqa: E501

        :return: The amount of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Invoice.

        Amount of invoice  # noqa: E501

        :param amount: The amount of this Invoice.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def description(self):
        """Gets the description of this Invoice.  # noqa: E501

        Invoice description  # noqa: E501

        :return: The description of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Invoice.

        Invoice description  # noqa: E501

        :param description: The description of this Invoice.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def hidden_message(self):
        """Gets the hidden_message of this Invoice.  # noqa: E501

        Message that will be displayed after invoice payment  # noqa: E501

        :return: The hidden_message of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._hidden_message

    @hidden_message.setter
    def hidden_message(self, hidden_message):
        """Sets the hidden_message of this Invoice.

        Message that will be displayed after invoice payment  # noqa: E501

        :param hidden_message: The hidden_message of this Invoice.  # noqa: E501
        :type: str
        """

        self._hidden_message = hidden_message

    @property
    def payload(self):
        """Gets the payload of this Invoice.  # noqa: E501

        Any data that is attached to invoice  # noqa: E501

        :return: The payload of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this Invoice.

        Any data that is attached to invoice  # noqa: E501

        :param payload: The payload of this Invoice.  # noqa: E501
        :type: str
        """

        self._payload = payload

    @property
    def callback_url(self):
        """Gets the callback_url of this Invoice.  # noqa: E501

        url that will be set for Return button after invoice is paid  # noqa: E501

        :return: The callback_url of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """Sets the callback_url of this Invoice.

        url that will be set for Return button after invoice is paid  # noqa: E501

        :param callback_url: The callback_url of this Invoice.  # noqa: E501
        :type: str
        """

        self._callback_url = callback_url

    @property
    def currency(self):
        """Gets the currency of this Invoice.  # noqa: E501


        :return: The currency of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Invoice.


        :param currency: The currency of this Invoice.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def created(self):
        """Gets the created of this Invoice.  # noqa: E501

        When invoice was created  # noqa: E501

        :return: The created of this Invoice.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Invoice.

        When invoice was created  # noqa: E501

        :param created: The created of this Invoice.  # noqa: E501
        :type: datetime
        """
        # if created is None:
        #     raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def paid(self):
        """Gets the paid of this Invoice.  # noqa: E501

        When invoice was paid  # noqa: E501

        :return: The paid of this Invoice.  # noqa: E501
        :rtype: datetime
        """
        return self._paid

    @paid.setter
    def paid(self, paid):
        """Sets the paid of this Invoice.

        When invoice was paid  # noqa: E501

        :param paid: The paid of this Invoice.  # noqa: E501
        :type: datetime
        """

        self._paid = paid

    @property
    def status(self):
        """Gets the status of this Invoice.  # noqa: E501


        :return: The status of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Invoice.


        :param status: The status of this Invoice.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["active", "paid", "expired"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def expired_in(self):
        """Gets the expired_in of this Invoice.  # noqa: E501

        Invoice expire time in seconds, max 1 day, 0 - none expired  # noqa: E501

        :return: The expired_in of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._expired_in

    @expired_in.setter
    def expired_in(self, expired_in):
        """Sets the expired_in of this Invoice.

        Invoice expire time in seconds, max 1 day, 0 - none expired  # noqa: E501

        :param expired_in: The expired_in of this Invoice.  # noqa: E501
        :type: float
        """

        self._expired_in = expired_in

    @property
    def link(self):
        """Gets the link of this Invoice.  # noqa: E501


        :return: The link of this Invoice.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this Invoice.


        :param link: The link of this Invoice.  # noqa: E501
        :type: str
        """
        if link is None:
            raise ValueError("Invalid value for `link`, must not be `None`")  # noqa: E501

        self._link = link

    @property
    def total_activations(self):
        """Gets the total_activations of this Invoice.  # noqa: E501

        Total activations of invoice  # noqa: E501

        :return: The total_activations of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._total_activations

    @total_activations.setter
    def total_activations(self, total_activations):
        """Sets the total_activations of this Invoice.

        Total activations of invoice  # noqa: E501

        :param total_activations: The total_activations of this Invoice.  # noqa: E501
        :type: float
        """
        if total_activations is None:
            raise ValueError("Invalid value for `total_activations`, must not be `None`")  # noqa: E501

        self._total_activations = total_activations

    @property
    def activations_left(self):
        """Gets the activations_left of this Invoice.  # noqa: E501

        Activations left of invoice  # noqa: E501

        :return: The activations_left of this Invoice.  # noqa: E501
        :rtype: float
        """
        return self._activations_left

    @activations_left.setter
    def activations_left(self, activations_left):
        """Sets the activations_left of this Invoice.

        Activations left of invoice  # noqa: E501

        :param activations_left: The activations_left of this Invoice.  # noqa: E501
        :type: float
        """
        if activations_left is None:
            raise ValueError("Invalid value for `activations_left`, must not be `None`")  # noqa: E501

        self._activations_left = activations_left

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
        if issubclass(Invoice, dict):
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
        if not isinstance(other, Invoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
