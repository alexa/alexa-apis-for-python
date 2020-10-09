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
    from ask_smapi_model.v1.skill.certification.estimation_update import EstimationUpdate as Certification_EstimationUpdateV1


class ReviewTrackingInfo(object):
    """
    Structure for review tracking information of the skill.


    :param estimated_completion_timestamp: Timestamp for estimated completion of certification review for the skill.
    :type estimated_completion_timestamp: (optional) datetime
    :param actual_completion_timestamp: Timestamp for actual completion of certification review for the skill.
    :type actual_completion_timestamp: (optional) datetime
    :param last_updated: Timestamp for when the last update was made to review tracking info.
    :type last_updated: (optional) datetime
    :param estimation_updates: List of updates to estimation completion time for certification review for the skill.
    :type estimation_updates: (optional) list[ask_smapi_model.v1.skill.certification.estimation_update.EstimationUpdate]

    """
    deserialized_types = {
        'estimated_completion_timestamp': 'datetime',
        'actual_completion_timestamp': 'datetime',
        'last_updated': 'datetime',
        'estimation_updates': 'list[ask_smapi_model.v1.skill.certification.estimation_update.EstimationUpdate]'
    }  # type: Dict

    attribute_map = {
        'estimated_completion_timestamp': 'estimatedCompletionTimestamp',
        'actual_completion_timestamp': 'actualCompletionTimestamp',
        'last_updated': 'lastUpdated',
        'estimation_updates': 'estimationUpdates'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, estimated_completion_timestamp=None, actual_completion_timestamp=None, last_updated=None, estimation_updates=None):
        # type: (Optional[datetime], Optional[datetime], Optional[datetime], Optional[List[Certification_EstimationUpdateV1]]) -> None
        """Structure for review tracking information of the skill.

        :param estimated_completion_timestamp: Timestamp for estimated completion of certification review for the skill.
        :type estimated_completion_timestamp: (optional) datetime
        :param actual_completion_timestamp: Timestamp for actual completion of certification review for the skill.
        :type actual_completion_timestamp: (optional) datetime
        :param last_updated: Timestamp for when the last update was made to review tracking info.
        :type last_updated: (optional) datetime
        :param estimation_updates: List of updates to estimation completion time for certification review for the skill.
        :type estimation_updates: (optional) list[ask_smapi_model.v1.skill.certification.estimation_update.EstimationUpdate]
        """
        self.__discriminator_value = None  # type: str

        self.estimated_completion_timestamp = estimated_completion_timestamp
        self.actual_completion_timestamp = actual_completion_timestamp
        self.last_updated = last_updated
        self.estimation_updates = estimation_updates

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
        if not isinstance(other, ReviewTrackingInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
