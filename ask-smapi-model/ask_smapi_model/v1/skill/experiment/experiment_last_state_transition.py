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
    from ask_smapi_model.v1.skill.experiment.destination_state import DestinationState as DestinationState_8dc8c95c
    from ask_smapi_model.v1.skill.experiment.state_transition_status import StateTransitionStatus as StateTransitionStatus_53bf1e4d
    from ask_smapi_model.v1.skill.experiment.source_state import SourceState as SourceState_88a676e0
    from ask_smapi_model.v1.skill.experiment.state_transition_error import StateTransitionError as StateTransitionError_990ec079


class ExperimentLastStateTransition(object):
    """
    Defines the last state transition information for the experiment. 


    :param source_state: 
    :type source_state: (optional) ask_smapi_model.v1.skill.experiment.source_state.SourceState
    :param target_state: 
    :type target_state: (optional) ask_smapi_model.v1.skill.experiment.destination_state.DestinationState
    :param status: 
    :type status: (optional) ask_smapi_model.v1.skill.experiment.state_transition_status.StateTransitionStatus
    :param start_time: 
    :type start_time: (optional) datetime
    :param end_time: 
    :type end_time: (optional) datetime
    :param errors: List of error objects which define what errors caused the state transition failure. 
    :type errors: (optional) list[ask_smapi_model.v1.skill.experiment.state_transition_error.StateTransitionError]

    """
    deserialized_types = {
        'source_state': 'ask_smapi_model.v1.skill.experiment.source_state.SourceState',
        'target_state': 'ask_smapi_model.v1.skill.experiment.destination_state.DestinationState',
        'status': 'ask_smapi_model.v1.skill.experiment.state_transition_status.StateTransitionStatus',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'errors': 'list[ask_smapi_model.v1.skill.experiment.state_transition_error.StateTransitionError]'
    }  # type: Dict

    attribute_map = {
        'source_state': 'sourceState',
        'target_state': 'targetState',
        'status': 'status',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'errors': 'errors'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, source_state=None, target_state=None, status=None, start_time=None, end_time=None, errors=None):
        # type: (Optional[SourceState_88a676e0], Optional[DestinationState_8dc8c95c], Optional[StateTransitionStatus_53bf1e4d], Optional[datetime], Optional[datetime], Optional[List[StateTransitionError_990ec079]]) -> None
        """Defines the last state transition information for the experiment. 

        :param source_state: 
        :type source_state: (optional) ask_smapi_model.v1.skill.experiment.source_state.SourceState
        :param target_state: 
        :type target_state: (optional) ask_smapi_model.v1.skill.experiment.destination_state.DestinationState
        :param status: 
        :type status: (optional) ask_smapi_model.v1.skill.experiment.state_transition_status.StateTransitionStatus
        :param start_time: 
        :type start_time: (optional) datetime
        :param end_time: 
        :type end_time: (optional) datetime
        :param errors: List of error objects which define what errors caused the state transition failure. 
        :type errors: (optional) list[ask_smapi_model.v1.skill.experiment.state_transition_error.StateTransitionError]
        """
        self.__discriminator_value = None  # type: str

        self.source_state = source_state
        self.target_state = target_state
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.errors = errors

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
        if not isinstance(other, ExperimentLastStateTransition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
