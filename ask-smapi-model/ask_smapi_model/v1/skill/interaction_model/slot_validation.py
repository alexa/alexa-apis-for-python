# coding: utf-8

#
# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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
    from typing import Dict, List, Optional, Union, Any
    from datetime import datetime


class SlotValidation(object):
    """
    Validation on a slot with support for prompt and confirmation.


    :param object_type: The exact type of validation e.g. isLessThan,isGreaterThan etc.
    :type object_type: (optional) str
    :param prompt: The prompt id that should be used if validation fails.
    :type prompt: (optional) str

    .. note::

        This is an abstract class. Use the following mapping, to figure out
        the model class to be instantiated, that sets ``type`` variable.

        | hasEntityResolutionMatch: :py:class:`ask_smapi_model.v1.skill.interaction_model.has_entity_resolution_match.HasEntityResolutionMatch`,
        |
        | isLessThanOrEqualTo: :py:class:`ask_smapi_model.v1.skill.interaction_model.is_less_than_or_equal_to.IsLessThanOrEqualTo`,
        |
        | isGreaterThan: :py:class:`ask_smapi_model.v1.skill.interaction_model.is_greater_than.IsGreaterThan`,
        |
        | isNotInSet: :py:class:`ask_smapi_model.v1.skill.interaction_model.is_not_in_set.IsNotInSet`,
        |
        | isInDuration: :py:class:`ask_smapi_model.v1.skill.interaction_model.is_in_duration.IsInDuration`,
        |
        | isLessThan: :py:class:`ask_smapi_model.v1.skill.interaction_model.is_less_than.IsLessThan`,
        |
        | isNotInDuration: :py:class:`ask_smapi_model.v1.skill.interaction_model.is_not_in_duration.IsNotInDuration`,
        |
        | isGreaterThanOrEqualTo: :py:class:`ask_smapi_model.v1.skill.interaction_model.is_greater_than_or_equal_to.IsGreaterThanOrEqualTo`,
        |
        | isInSet: :py:class:`ask_smapi_model.v1.skill.interaction_model.is_in_set.IsInSet`

    """
    deserialized_types = {
        'object_type': 'str',
        'prompt': 'str'
    }  # type: Dict

    attribute_map = {
        'object_type': 'type',
        'prompt': 'prompt'
    }  # type: Dict
    supports_multiple_types = False

    discriminator_value_class_map = {
        'hasEntityResolutionMatch': 'ask_smapi_model.v1.skill.interaction_model.has_entity_resolution_match.HasEntityResolutionMatch',
        'isLessThanOrEqualTo': 'ask_smapi_model.v1.skill.interaction_model.is_less_than_or_equal_to.IsLessThanOrEqualTo',
        'isGreaterThan': 'ask_smapi_model.v1.skill.interaction_model.is_greater_than.IsGreaterThan',
        'isNotInSet': 'ask_smapi_model.v1.skill.interaction_model.is_not_in_set.IsNotInSet',
        'isInDuration': 'ask_smapi_model.v1.skill.interaction_model.is_in_duration.IsInDuration',
        'isLessThan': 'ask_smapi_model.v1.skill.interaction_model.is_less_than.IsLessThan',
        'isNotInDuration': 'ask_smapi_model.v1.skill.interaction_model.is_not_in_duration.IsNotInDuration',
        'isGreaterThanOrEqualTo': 'ask_smapi_model.v1.skill.interaction_model.is_greater_than_or_equal_to.IsGreaterThanOrEqualTo',
        'isInSet': 'ask_smapi_model.v1.skill.interaction_model.is_in_set.IsInSet'
    }

    json_discriminator_key = "type"

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, object_type=None, prompt=None):
        # type: (Optional[str], Optional[str]) -> None
        """Validation on a slot with support for prompt and confirmation.

        :param object_type: The exact type of validation e.g. isLessThan,isGreaterThan etc.
        :type object_type: (optional) str
        :param prompt: The prompt id that should be used if validation fails.
        :type prompt: (optional) str
        """
        self.__discriminator_value = None  # type: str

        self.object_type = object_type
        self.prompt = prompt

    @classmethod
    def get_real_child_model(cls, data):
        # type: (Dict[str, str]) -> Optional[str]
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[cls.json_discriminator_key]
        return cls.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        # type: () -> Dict[str, object]
        """Returns the model properties as a dict"""
        result = {}  # type: Dict

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
        if not isinstance(other, SlotValidation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
