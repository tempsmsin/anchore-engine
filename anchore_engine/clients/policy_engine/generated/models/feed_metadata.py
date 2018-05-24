# coding: utf-8

"""
    anchore_engine.services.policy_engine

    This is a policy evaluation service. It receives push-events from external systems for data updates and provides an api for requesting image policy checks  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: zach@anchore.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from anchore_engine.clients.policy_engine.generated.models.feed_group_metadata import FeedGroupMetadata  # noqa: F401,E501


class FeedMetadata(object):
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
        'name': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'groups': 'list[FeedGroupMetadata]',
        'last_full_sync': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'groups': 'groups',
        'last_full_sync': 'last_full_sync'
    }

    def __init__(self, name=None, created_at=None, updated_at=None, groups=None, last_full_sync=None):  # noqa: E501
        """FeedMetadata - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._created_at = None
        self._updated_at = None
        self._groups = None
        self._last_full_sync = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if groups is not None:
            self.groups = groups
        if last_full_sync is not None:
            self.last_full_sync = last_full_sync

    @property
    def name(self):
        """Gets the name of this FeedMetadata.  # noqa: E501

        name of the feed  # noqa: E501

        :return: The name of this FeedMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FeedMetadata.

        name of the feed  # noqa: E501

        :param name: The name of this FeedMetadata.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this FeedMetadata.  # noqa: E501

        Date the metadata record was created in engine (first seen on source)  # noqa: E501

        :return: The created_at of this FeedMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FeedMetadata.

        Date the metadata record was created in engine (first seen on source)  # noqa: E501

        :param created_at: The created_at of this FeedMetadata.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this FeedMetadata.  # noqa: E501

        Date the metadata was last updated  # noqa: E501

        :return: The updated_at of this FeedMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this FeedMetadata.

        Date the metadata was last updated  # noqa: E501

        :param updated_at: The updated_at of this FeedMetadata.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def groups(self):
        """Gets the groups of this FeedMetadata.  # noqa: E501


        :return: The groups of this FeedMetadata.  # noqa: E501
        :rtype: list[FeedGroupMetadata]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this FeedMetadata.


        :param groups: The groups of this FeedMetadata.  # noqa: E501
        :type: list[FeedGroupMetadata]
        """

        self._groups = groups

    @property
    def last_full_sync(self):
        """Gets the last_full_sync of this FeedMetadata.  # noqa: E501


        :return: The last_full_sync of this FeedMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._last_full_sync

    @last_full_sync.setter
    def last_full_sync(self, last_full_sync):
        """Sets the last_full_sync of this FeedMetadata.


        :param last_full_sync: The last_full_sync of this FeedMetadata.  # noqa: E501
        :type: datetime
        """

        self._last_full_sync = last_full_sync

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list([x.to_dict() if hasattr(x, "to_dict") else x for x in value])
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict([(item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item for item in list(value.items())])
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FeedMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
