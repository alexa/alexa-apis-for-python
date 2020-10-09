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


class BaseSchema(object):
    """
    Represents attributes common to all development notifications. 


    :param timestamp: ISO 8601 timestamp for the instant when event was created. 
    :type timestamp: (optional) datetime
    :param event_name: 
    :type event_name: (optional) str

    .. note::

        This is an abstract class. Use the following mapping, to figure out
        the model class to be instantiated, that sets ``eventName`` variable.

        | AlexaDevelopmentEvent.InteractionModelUpdate: :py:class:`ask_smapi_model.v0.event_schema.alexa_development_event.interaction_model_update.InteractionModelUpdate`,
        |
        | AlexaDevelopmentEvent.SkillPublish: :py:class:`ask_smapi_model.v0.event_schema.alexa_development_event.skill_publish.SkillPublish`,
        |
        | AlexaDevelopmentEvent.ManifestUpdate: :py:class:`ask_smapi_model.v0.event_schema.alexa_development_event.manifest_update.ManifestUpdate`,
        |
        | AlexaDevelopmentEvent.SkillCertification: :py:class:`ask_smapi_model.v0.event_schema.alexa_development_event.skill_certification.SkillCertification`

    """
    deserialized_types = {
        'timestamp': 'datetime',
        'event_name': 'str'
    }  # type: Dict

    attribute_map = {
        'timestamp': 'timestamp',
        'event_name': 'eventName'
    }  # type: Dict
    supports_multiple_types = False

    discriminator_value_class_map = {
        'AlexaDevelopmentEvent.InteractionModelUpdate': 'ask_smapi_model.v0.event_schema.alexa_development_event.interaction_model_update.InteractionModelUpdate',
        'AlexaDevelopmentEvent.SkillPublish': 'ask_smapi_model.v0.event_schema.alexa_development_event.skill_publish.SkillPublish',
        'AlexaDevelopmentEvent.ManifestUpdate': 'ask_smapi_model.v0.event_schema.alexa_development_event.manifest_update.ManifestUpdate',
        'AlexaDevelopmentEvent.SkillCertification': 'ask_smapi_model.v0.event_schema.alexa_development_event.skill_certification.SkillCertification'
    }

    json_discriminator_key = "eventName"

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, timestamp=None, event_name=None):
        # type: (Optional[datetime], Optional[str]) -> None
        """Represents attributes common to all development notifications. 

        :param timestamp: ISO 8601 timestamp for the instant when event was created. 
        :type timestamp: (optional) datetime
        :param event_name: 
        :type event_name: (optional) str
        """
        self.__discriminator_value = None  # type: str

        self.timestamp = timestamp
        self.event_name = event_name

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
        if not isinstance(other, BaseSchema):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
