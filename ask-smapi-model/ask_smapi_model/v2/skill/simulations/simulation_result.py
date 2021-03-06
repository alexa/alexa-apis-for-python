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
    from ask_smapi_model.v2.skill.simulations.alexa_execution_info import AlexaExecutionInfo as AlexaExecutionInfo_9555ceb9
    from ask_smapi_model.v2.skill.simulations.skill_execution_info import SkillExecutionInfo as SkillExecutionInfo_232ba9f9
    from ask_smapi_model.v2.error import Error as Error_ea6c1a5a


class SimulationResult(object):
    """

    :param alexa_execution_info: 
    :type alexa_execution_info: (optional) ask_smapi_model.v2.skill.simulations.alexa_execution_info.AlexaExecutionInfo
    :param skill_execution_info: 
    :type skill_execution_info: (optional) ask_smapi_model.v2.skill.simulations.skill_execution_info.SkillExecutionInfo
    :param error: 
    :type error: (optional) ask_smapi_model.v2.error.Error

    """
    deserialized_types = {
        'alexa_execution_info': 'ask_smapi_model.v2.skill.simulations.alexa_execution_info.AlexaExecutionInfo',
        'skill_execution_info': 'ask_smapi_model.v2.skill.simulations.skill_execution_info.SkillExecutionInfo',
        'error': 'ask_smapi_model.v2.error.Error'
    }  # type: Dict

    attribute_map = {
        'alexa_execution_info': 'alexaExecutionInfo',
        'skill_execution_info': 'skillExecutionInfo',
        'error': 'error'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, alexa_execution_info=None, skill_execution_info=None, error=None):
        # type: (Optional[AlexaExecutionInfo_9555ceb9], Optional[SkillExecutionInfo_232ba9f9], Optional[Error_ea6c1a5a]) -> None
        """

        :param alexa_execution_info: 
        :type alexa_execution_info: (optional) ask_smapi_model.v2.skill.simulations.alexa_execution_info.AlexaExecutionInfo
        :param skill_execution_info: 
        :type skill_execution_info: (optional) ask_smapi_model.v2.skill.simulations.skill_execution_info.SkillExecutionInfo
        :param error: 
        :type error: (optional) ask_smapi_model.v2.error.Error
        """
        self.__discriminator_value = None  # type: str

        self.alexa_execution_info = alexa_execution_info
        self.skill_execution_info = skill_execution_info
        self.error = error

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
        if not isinstance(other, SimulationResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
