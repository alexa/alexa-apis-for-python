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
    from ask_smapi_model.v1.skill.experiment.state import State as State_1d082829
    from ask_smapi_model.v1.skill.experiment.experiment_history import ExperimentHistory as ExperimentHistory_4dc94b66


class ExperimentSummary(object):
    """
    Defines the shortened Experiment body which would contain a summary of experiment information. 


    :param experiment_id: Identifier for experiment within a skill.
    :type experiment_id: (optional) str
    :param name: Name that developer assigns to the experiment for easier identification.
    :type name: (optional) str
    :param state: 
    :type state: (optional) ask_smapi_model.v1.skill.experiment.state.State
    :param experiment_history: 
    :type experiment_history: (optional) ask_smapi_model.v1.skill.experiment.experiment_history.ExperimentHistory

    """
    deserialized_types = {
        'experiment_id': 'str',
        'name': 'str',
        'state': 'ask_smapi_model.v1.skill.experiment.state.State',
        'experiment_history': 'ask_smapi_model.v1.skill.experiment.experiment_history.ExperimentHistory'
    }  # type: Dict

    attribute_map = {
        'experiment_id': 'experimentId',
        'name': 'name',
        'state': 'state',
        'experiment_history': 'experimentHistory'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, experiment_id=None, name=None, state=None, experiment_history=None):
        # type: (Optional[str], Optional[str], Optional[State_1d082829], Optional[ExperimentHistory_4dc94b66]) -> None
        """Defines the shortened Experiment body which would contain a summary of experiment information. 

        :param experiment_id: Identifier for experiment within a skill.
        :type experiment_id: (optional) str
        :param name: Name that developer assigns to the experiment for easier identification.
        :type name: (optional) str
        :param state: 
        :type state: (optional) ask_smapi_model.v1.skill.experiment.state.State
        :param experiment_history: 
        :type experiment_history: (optional) ask_smapi_model.v1.skill.experiment.experiment_history.ExperimentHistory
        """
        self.__discriminator_value = None  # type: str

        self.experiment_id = experiment_id
        self.name = name
        self.state = state
        self.experiment_history = experiment_history

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
        if not isinstance(other, ExperimentSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
