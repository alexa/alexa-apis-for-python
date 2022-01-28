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


class MetricValues(object):
    """
    Defines the body of the metric result values.


    :param mean: The mean (average) of each sample (T1 or C group).
    :type mean: (optional) float
    :param percent_diff: The relative percent difference between the mean of the T1 group and the mean of the C group.
    :type percent_diff: (optional) float
    :param confidence_interval_lower: The lower limit number of the confidence interval range. Confidence interval measures the probability that the mean falls within a range. 
    :type confidence_interval_lower: (optional) float
    :param confidence_interval_upper: The upper limit number of the confidence interval range.
    :type confidence_interval_upper: (optional) float
    :param p_value: The probability that the difference between the two means (from T1 and C) is due to random sampling error.
    :type p_value: (optional) float
    :param user_count: Count of users in the treatment sample.
    :type user_count: (optional) int

    """
    deserialized_types = {
        'mean': 'float',
        'percent_diff': 'float',
        'confidence_interval_lower': 'float',
        'confidence_interval_upper': 'float',
        'p_value': 'float',
        'user_count': 'int'
    }  # type: Dict

    attribute_map = {
        'mean': 'mean',
        'percent_diff': 'percentDiff',
        'confidence_interval_lower': 'confidenceIntervalLower',
        'confidence_interval_upper': 'confidenceIntervalUpper',
        'p_value': 'pValue',
        'user_count': 'userCount'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, mean=None, percent_diff=None, confidence_interval_lower=None, confidence_interval_upper=None, p_value=None, user_count=None):
        # type: (Optional[float], Optional[float], Optional[float], Optional[float], Optional[float], Optional[int]) -> None
        """Defines the body of the metric result values.

        :param mean: The mean (average) of each sample (T1 or C group).
        :type mean: (optional) float
        :param percent_diff: The relative percent difference between the mean of the T1 group and the mean of the C group.
        :type percent_diff: (optional) float
        :param confidence_interval_lower: The lower limit number of the confidence interval range. Confidence interval measures the probability that the mean falls within a range. 
        :type confidence_interval_lower: (optional) float
        :param confidence_interval_upper: The upper limit number of the confidence interval range.
        :type confidence_interval_upper: (optional) float
        :param p_value: The probability that the difference between the two means (from T1 and C) is due to random sampling error.
        :type p_value: (optional) float
        :param user_count: Count of users in the treatment sample.
        :type user_count: (optional) int
        """
        self.__discriminator_value = None  # type: str

        self.mean = mean
        self.percent_diff = percent_diff
        self.confidence_interval_lower = confidence_interval_lower
        self.confidence_interval_upper = confidence_interval_upper
        self.p_value = p_value
        self.user_count = user_count

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
        if not isinstance(other, MetricValues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
