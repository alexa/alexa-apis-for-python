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
    from ask_smapi_model.v1.skill.rollback_request_status_types import RollbackRequestStatusTypes as Skill_RollbackRequestStatusTypesV1
    from ask_smapi_model.v1.skill.standardized_error import StandardizedError as Skill_StandardizedErrorV1


class RollbackRequestStatus(object):
    """
    Rollback request for a skill


    :param id: rollback request id
    :type id: (optional) str
    :param target_version: The target skill version to rollback to.
    :type target_version: (optional) str
    :param submission_time: 
    :type submission_time: (optional) datetime
    :param status: 
    :type status: (optional) ask_smapi_model.v1.skill.rollback_request_status_types.RollbackRequestStatusTypes
    :param errors: 
    :type errors: (optional) list[ask_smapi_model.v1.skill.standardized_error.StandardizedError]

    """
    deserialized_types = {
        'id': 'str',
        'target_version': 'str',
        'submission_time': 'datetime',
        'status': 'ask_smapi_model.v1.skill.rollback_request_status_types.RollbackRequestStatusTypes',
        'errors': 'list[ask_smapi_model.v1.skill.standardized_error.StandardizedError]'
    }  # type: Dict

    attribute_map = {
        'id': 'id',
        'target_version': 'targetVersion',
        'submission_time': 'submissionTime',
        'status': 'status',
        'errors': 'errors'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, id=None, target_version=None, submission_time=None, status=None, errors=None):
        # type: (Optional[str], Optional[str], Optional[datetime], Optional[Skill_RollbackRequestStatusTypesV1], Optional[List[Skill_StandardizedErrorV1]]) -> None
        """Rollback request for a skill

        :param id: rollback request id
        :type id: (optional) str
        :param target_version: The target skill version to rollback to.
        :type target_version: (optional) str
        :param submission_time: 
        :type submission_time: (optional) datetime
        :param status: 
        :type status: (optional) ask_smapi_model.v1.skill.rollback_request_status_types.RollbackRequestStatusTypes
        :param errors: 
        :type errors: (optional) list[ask_smapi_model.v1.skill.standardized_error.StandardizedError]
        """
        self.__discriminator_value = None  # type: str

        self.id = id
        self.target_version = target_version
        self.submission_time = submission_time
        self.status = status
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
        if not isinstance(other, RollbackRequestStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
