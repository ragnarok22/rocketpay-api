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

class PaginationDto(object):
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
        'total': 'float',
        'limit': 'float',
        'offset': 'float'
    }

    attribute_map = {
        'total': 'total',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, total=None, limit=100, offset=100):  # noqa: E501
        """PaginationDto - a model defined in Swagger"""  # noqa: E501
        self._total = None
        self._limit = None
        self._offset = None
        self.discriminator = None
        self.total = total
        self.limit = limit
        self.offset = offset

    @property
    def total(self):
        """Gets the total of this PaginationDto.  # noqa: E501

        Total times  # noqa: E501

        :return: The total of this PaginationDto.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PaginationDto.

        Total times  # noqa: E501

        :param total: The total of this PaginationDto.  # noqa: E501
        :type: float
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def limit(self):
        """Gets the limit of this PaginationDto.  # noqa: E501


        :return: The limit of this PaginationDto.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PaginationDto.


        :param limit: The limit of this PaginationDto.  # noqa: E501
        :type: float
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this PaginationDto.  # noqa: E501


        :return: The offset of this PaginationDto.  # noqa: E501
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PaginationDto.


        :param offset: The offset of this PaginationDto.  # noqa: E501
        :type: float
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

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
        if issubclass(PaginationDto, dict):
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
        if not isinstance(other, PaginationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other