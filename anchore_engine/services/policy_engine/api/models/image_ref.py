# coding: utf-8


from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from anchore_engine.services.policy_engine.api.models.base_model_ import Model
from anchore_engine.services.policy_engine.api import util


class ImageRef(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, type=None, value=None):  # noqa: E501
        """ImageRef - a model defined in Swagger

        :param type: The type of this ImageRef.  # noqa: E501
        :type type: str
        :param value: The value of this ImageRef.  # noqa: E501
        :type value: str
        """
        self.swagger_types = {
            'type': str,
            'value': str
        }

        self.attribute_map = {
            'type': 'type',
            'value': 'value'
        }

        self._type = type
        self._value = value

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ImageRef of this ImageRef.  # noqa: E501
        :rtype: ImageRef
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this ImageRef.


        :return: The type of this ImageRef.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ImageRef.


        :param type: The type of this ImageRef.
        :type type: str
        """
        allowed_values = ["tag", "digest", "id"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def value(self):
        """Gets the value of this ImageRef.


        :return: The value of this ImageRef.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ImageRef.


        :param value: The value of this ImageRef.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value
