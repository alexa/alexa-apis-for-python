# coding: utf-8

#
# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for
# the specific language governing permissions and limitations under the License.
#

import pprint
import re  # noqa: F401
import six
import typing
from enum import Enum
from abc import ABCMeta, abstractmethod


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional
    from datetime import datetime


class Command(object):
    """
    A message that can change the visual or audio presentation of the content on the screen.


    :param object_type: Defines the command type and dictates which properties must/can be included.
    :type object_type: (optional) str
    :param delay: The delay in milliseconds before this command starts executing; must be non-negative. Defaults to 0.
    :type delay: (optional) int
    :param description: A user-provided description of this command.
    :type description: (optional) str
    :param when: If false, the execution of the command is skipped. Defaults to true.
    :type when: (optional) bool

    .. note::

        This is an abstract class. Use the following mapping, to figure out
        the model class to be instantiated, that sets ``type`` variable.

        | SetPage: :py:class:`ask_sdk_model.interfaces.alexa.presentation.apl.set_page_command.SetPageCommand`,
        |
        | SpeakItem: :py:class:`ask_sdk_model.interfaces.alexa.presentation.apl.speak_item_command.SpeakItemCommand`,
        |
        | AutoPage: :py:class:`ask_sdk_model.interfaces.alexa.presentation.apl.auto_page_command.AutoPageCommand`

    """
    deserialized_types = {
        'object_type': 'str',
        'delay': 'int',
        'description': 'str',
        'when': 'bool'
    }

    attribute_map = {
        'object_type': 'type',
        'delay': 'delay',
        'description': 'description',
        'when': 'when'
    }

    discriminator_value_class_map = {
        'SetPage': 'ask_sdk_model.interfaces.alexa.presentation.apl.set_page_command.SetPageCommand',
        'SpeakItem': 'ask_sdk_model.interfaces.alexa.presentation.apl.speak_item_command.SpeakItemCommand',
        'AutoPage': 'ask_sdk_model.interfaces.alexa.presentation.apl.auto_page_command.AutoPageCommand'
    }

    json_discriminator_key = "type"

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, object_type=None, delay=None, description=None, when=None):
        # type: (Optional[str], Optional[int], Optional[str], Optional[bool]) -> None
        """A message that can change the visual or audio presentation of the content on the screen.

        :param object_type: Defines the command type and dictates which properties must/can be included.
        :type object_type: (optional) str
        :param delay: The delay in milliseconds before this command starts executing; must be non-negative. Defaults to 0.
        :type delay: (optional) int
        :param description: A user-provided description of this command.
        :type description: (optional) str
        :param when: If false, the execution of the command is skipped. Defaults to true.
        :type when: (optional) bool
        """
        self.__discriminator_value = None

        self.object_type = object_type
        self.delay = delay
        self.description = description
        self.when = when

    @classmethod
    def get_real_child_model(cls, data):
        # type: (Dict[str, str]) -> str
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[cls.json_discriminator_key]
        return cls.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        # type: () -> Dict[str, object]
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.deserialized_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else
                    x.value if isinstance(x, Enum) else x,
                    value
                ))
            elif isinstance(value, Enum):
                result[attr] = value.value
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else
                    (item[0], item[1].value)
                    if isinstance(item[1], Enum) else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        # type: () -> str
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        # type: () -> str
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are equal"""
        if not isinstance(other, Command):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
