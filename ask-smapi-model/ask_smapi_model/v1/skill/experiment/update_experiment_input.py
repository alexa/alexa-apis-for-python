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
    from ask_smapi_model.v1.skill.experiment.metric_configuration import MetricConfiguration as MetricConfiguration_7789320a


class UpdateExperimentInput(object):
    """
    Defines the Experiment body used for requesting an experiment update. Only includes fields that are editable by the user. 


    :param description: Hypothesis that developer provides to describe the experiment&#39;s purpose.
    :type description: (optional) str
    :param planned_duration: The number of weeks the skill builder intends to run the experiment. Used for documentation purposes and by metric platform as a reference. Does not impact experiment execution. Format uses ISO-8601 representation of duration. (Example: 4 weeks &#x3D; \&quot;P4W\&quot;) 
    :type planned_duration: (optional) str
    :param exposure_percentage: The percentage of unique customers that will be part of the skill experiment while the experiment is running.
    :type exposure_percentage: (optional) int
    :param metric_configurations: List of metric configurations that determine which metrics are key/guardrail metrics and the expected metric direction.
    :type metric_configurations: (optional) list[ask_smapi_model.v1.skill.experiment.metric_configuration.MetricConfiguration]

    """
    deserialized_types = {
        'description': 'str',
        'planned_duration': 'str',
        'exposure_percentage': 'int',
        'metric_configurations': 'list[ask_smapi_model.v1.skill.experiment.metric_configuration.MetricConfiguration]'
    }  # type: Dict

    attribute_map = {
        'description': 'description',
        'planned_duration': 'plannedDuration',
        'exposure_percentage': 'exposurePercentage',
        'metric_configurations': 'metricConfigurations'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, description=None, planned_duration=None, exposure_percentage=None, metric_configurations=None):
        # type: (Optional[str], Optional[str], Optional[int], Optional[List[MetricConfiguration_7789320a]]) -> None
        """Defines the Experiment body used for requesting an experiment update. Only includes fields that are editable by the user. 

        :param description: Hypothesis that developer provides to describe the experiment&#39;s purpose.
        :type description: (optional) str
        :param planned_duration: The number of weeks the skill builder intends to run the experiment. Used for documentation purposes and by metric platform as a reference. Does not impact experiment execution. Format uses ISO-8601 representation of duration. (Example: 4 weeks &#x3D; \&quot;P4W\&quot;) 
        :type planned_duration: (optional) str
        :param exposure_percentage: The percentage of unique customers that will be part of the skill experiment while the experiment is running.
        :type exposure_percentage: (optional) int
        :param metric_configurations: List of metric configurations that determine which metrics are key/guardrail metrics and the expected metric direction.
        :type metric_configurations: (optional) list[ask_smapi_model.v1.skill.experiment.metric_configuration.MetricConfiguration]
        """
        self.__discriminator_value = None  # type: str

        self.description = description
        self.planned_duration = planned_duration
        self.exposure_percentage = exposure_percentage
        self.metric_configurations = metric_configurations

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
        if not isinstance(other, UpdateExperimentInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
