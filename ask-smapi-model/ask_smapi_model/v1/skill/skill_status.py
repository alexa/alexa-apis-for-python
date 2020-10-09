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
    from ask_smapi_model.v1.skill.hosted_skill_deployment_status import HostedSkillDeploymentStatus as Skill_HostedSkillDeploymentStatusV1
    from ask_smapi_model.v1.skill.manifest_status import ManifestStatus as Skill_ManifestStatusV1
    from ask_smapi_model.v1.skill.hosted_skill_provisioning_status import HostedSkillProvisioningStatus as Skill_HostedSkillProvisioningStatusV1
    from ask_smapi_model.v1.skill.skill_interaction_model_status import SkillInteractionModelStatus as Skill_SkillInteractionModelStatusV1


class SkillStatus(object):
    """
    Defines the structure for skill status response.


    :param manifest: 
    :type manifest: (optional) ask_smapi_model.v1.skill.manifest_status.ManifestStatus
    :param interaction_model: Status for available interaction models, keyed by locale.
    :type interaction_model: (optional) dict(str, ask_smapi_model.v1.skill.skill_interaction_model_status.SkillInteractionModelStatus)
    :param hosted_skill_deployment: 
    :type hosted_skill_deployment: (optional) ask_smapi_model.v1.skill.hosted_skill_deployment_status.HostedSkillDeploymentStatus
    :param hosted_skill_provisioning: 
    :type hosted_skill_provisioning: (optional) ask_smapi_model.v1.skill.hosted_skill_provisioning_status.HostedSkillProvisioningStatus

    """
    deserialized_types = {
        'manifest': 'ask_smapi_model.v1.skill.manifest_status.ManifestStatus',
        'interaction_model': 'dict(str, ask_smapi_model.v1.skill.skill_interaction_model_status.SkillInteractionModelStatus)',
        'hosted_skill_deployment': 'ask_smapi_model.v1.skill.hosted_skill_deployment_status.HostedSkillDeploymentStatus',
        'hosted_skill_provisioning': 'ask_smapi_model.v1.skill.hosted_skill_provisioning_status.HostedSkillProvisioningStatus'
    }  # type: Dict

    attribute_map = {
        'manifest': 'manifest',
        'interaction_model': 'interactionModel',
        'hosted_skill_deployment': 'hostedSkillDeployment',
        'hosted_skill_provisioning': 'hostedSkillProvisioning'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, manifest=None, interaction_model=None, hosted_skill_deployment=None, hosted_skill_provisioning=None):
        # type: (Optional[Skill_ManifestStatusV1], Optional[Dict[str, Skill_SkillInteractionModelStatusV1]], Optional[Skill_HostedSkillDeploymentStatusV1], Optional[Skill_HostedSkillProvisioningStatusV1]) -> None
        """Defines the structure for skill status response.

        :param manifest: 
        :type manifest: (optional) ask_smapi_model.v1.skill.manifest_status.ManifestStatus
        :param interaction_model: Status for available interaction models, keyed by locale.
        :type interaction_model: (optional) dict(str, ask_smapi_model.v1.skill.skill_interaction_model_status.SkillInteractionModelStatus)
        :param hosted_skill_deployment: 
        :type hosted_skill_deployment: (optional) ask_smapi_model.v1.skill.hosted_skill_deployment_status.HostedSkillDeploymentStatus
        :param hosted_skill_provisioning: 
        :type hosted_skill_provisioning: (optional) ask_smapi_model.v1.skill.hosted_skill_provisioning_status.HostedSkillProvisioningStatus
        """
        self.__discriminator_value = None  # type: str

        self.manifest = manifest
        self.interaction_model = interaction_model
        self.hosted_skill_deployment = hosted_skill_deployment
        self.hosted_skill_provisioning = hosted_skill_provisioning

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
        if not isinstance(other, SkillStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
