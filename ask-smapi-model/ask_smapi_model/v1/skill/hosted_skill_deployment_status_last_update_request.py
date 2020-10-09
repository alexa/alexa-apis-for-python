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
    from ask_smapi_model.v1.skill.hosted_skill_deployment_details import HostedSkillDeploymentDetails as Skill_HostedSkillDeploymentDetailsV1
    from ask_smapi_model.v1.skill.standardized_error import StandardizedError as Skill_StandardizedErrorV1
    from ask_smapi_model.v1.skill.status import Status as Skill_StatusV1


class HostedSkillDeploymentStatusLastUpdateRequest(object):
    """
    Contains attributes related to last modification request of a hosted skill deployment resource.


    :param status: 
    :type status: (optional) ask_smapi_model.v1.skill.status.Status
    :param errors: 
    :type errors: (optional) list[ask_smapi_model.v1.skill.standardized_error.StandardizedError]
    :param warnings: 
    :type warnings: (optional) list[ask_smapi_model.v1.skill.standardized_error.StandardizedError]
    :param deployment_details: 
    :type deployment_details: (optional) ask_smapi_model.v1.skill.hosted_skill_deployment_details.HostedSkillDeploymentDetails

    """
    deserialized_types = {
        'status': 'ask_smapi_model.v1.skill.status.Status',
        'errors': 'list[ask_smapi_model.v1.skill.standardized_error.StandardizedError]',
        'warnings': 'list[ask_smapi_model.v1.skill.standardized_error.StandardizedError]',
        'deployment_details': 'ask_smapi_model.v1.skill.hosted_skill_deployment_details.HostedSkillDeploymentDetails'
    }  # type: Dict

    attribute_map = {
        'status': 'status',
        'errors': 'errors',
        'warnings': 'warnings',
        'deployment_details': 'deploymentDetails'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, status=None, errors=None, warnings=None, deployment_details=None):
        # type: (Optional[Skill_StatusV1], Optional[List[Skill_StandardizedErrorV1]], Optional[List[Skill_StandardizedErrorV1]], Optional[Skill_HostedSkillDeploymentDetailsV1]) -> None
        """Contains attributes related to last modification request of a hosted skill deployment resource.

        :param status: 
        :type status: (optional) ask_smapi_model.v1.skill.status.Status
        :param errors: 
        :type errors: (optional) list[ask_smapi_model.v1.skill.standardized_error.StandardizedError]
        :param warnings: 
        :type warnings: (optional) list[ask_smapi_model.v1.skill.standardized_error.StandardizedError]
        :param deployment_details: 
        :type deployment_details: (optional) ask_smapi_model.v1.skill.hosted_skill_deployment_details.HostedSkillDeploymentDetails
        """
        self.__discriminator_value = None  # type: str

        self.status = status
        self.errors = errors
        self.warnings = warnings
        self.deployment_details = deployment_details

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
        if not isinstance(other, HostedSkillDeploymentStatusLastUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
