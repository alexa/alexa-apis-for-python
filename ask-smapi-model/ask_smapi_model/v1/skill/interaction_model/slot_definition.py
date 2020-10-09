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


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional, Union, Any
    from datetime import datetime
    from ask_smapi_model.v1.skill.interaction_model.multiple_values_config import MultipleValuesConfig as InteractionModel_MultipleValuesConfigV1


class SlotDefinition(object):
    """
    Slot definition.


    :param name: The name of the slot.
    :type name: (optional) str
    :param object_type: The type of the slot. It can be a built-in or custom type.
    :type object_type: (optional) str
    :param multiple_values: Configuration object for multiple values capturing behavior for this slot.
    :type multiple_values: (optional) ask_smapi_model.v1.skill.interaction_model.multiple_values_config.MultipleValuesConfig
    :param samples: Phrases the user can speak e.g. to trigger an intent or provide value for a slot elicitation.
    :type samples: (optional) list[str]

    """
    deserialized_types = {
        'name': 'str',
        'object_type': 'str',
        'multiple_values': 'ask_smapi_model.v1.skill.interaction_model.multiple_values_config.MultipleValuesConfig',
        'samples': 'list[str]'
    }  # type: Dict

    attribute_map = {
        'name': 'name',
        'object_type': 'type',
        'multiple_values': 'multipleValues',
        'samples': 'samples'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, name=None, object_type=None, multiple_values=None, samples=None):
        # type: (Optional[str], Optional[str], Optional[InteractionModel_MultipleValuesConfigV1], Optional[List[object]]) -> None
        """Slot definition.

        :param name: The name of the slot.
        :type name: (optional) str
        :param object_type: The type of the slot. It can be a built-in or custom type.
        :type object_type: (optional) str
        :param multiple_values: Configuration object for multiple values capturing behavior for this slot.
        :type multiple_values: (optional) ask_smapi_model.v1.skill.interaction_model.multiple_values_config.MultipleValuesConfig
        :param samples: Phrases the user can speak e.g. to trigger an intent or provide value for a slot elicitation.
        :type samples: (optional) list[str]
        """
        self.__discriminator_value = None  # type: str

        self.name = name
        self.object_type = object_type
        self.multiple_values = multiple_values
        self.samples = samples

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
        if not isinstance(other, SlotDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
