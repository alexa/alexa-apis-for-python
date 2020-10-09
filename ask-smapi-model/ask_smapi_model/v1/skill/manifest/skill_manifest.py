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
    from ask_smapi_model.v1.skill.manifest.permission_items import PermissionItems as Manifest_PermissionItemsV1
    from ask_smapi_model.v1.skill.manifest.skill_manifest_privacy_and_compliance import SkillManifestPrivacyAndCompliance as Manifest_SkillManifestPrivacyAndComplianceV1
    from ask_smapi_model.v1.skill.manifest.skill_manifest_apis import SkillManifestApis as Manifest_SkillManifestApisV1
    from ask_smapi_model.v1.skill.manifest.skill_manifest_events import SkillManifestEvents as Manifest_SkillManifestEventsV1
    from ask_smapi_model.v1.skill.manifest.skill_manifest_publishing_information import SkillManifestPublishingInformation as Manifest_SkillManifestPublishingInformationV1


class SkillManifest(object):
    """
    Defines the structure for a skill&#39;s metadata.


    :param manifest_version: Version of the skill manifest.
    :type manifest_version: (optional) str
    :param publishing_information: 
    :type publishing_information: (optional) ask_smapi_model.v1.skill.manifest.skill_manifest_publishing_information.SkillManifestPublishingInformation
    :param privacy_and_compliance: 
    :type privacy_and_compliance: (optional) ask_smapi_model.v1.skill.manifest.skill_manifest_privacy_and_compliance.SkillManifestPrivacyAndCompliance
    :param events: 
    :type events: (optional) ask_smapi_model.v1.skill.manifest.skill_manifest_events.SkillManifestEvents
    :param permissions: Defines the structure for required permissions information in the skill manifest.
    :type permissions: (optional) list[ask_smapi_model.v1.skill.manifest.permission_items.PermissionItems]
    :param apis: 
    :type apis: (optional) ask_smapi_model.v1.skill.manifest.skill_manifest_apis.SkillManifestApis

    """
    deserialized_types = {
        'manifest_version': 'str',
        'publishing_information': 'ask_smapi_model.v1.skill.manifest.skill_manifest_publishing_information.SkillManifestPublishingInformation',
        'privacy_and_compliance': 'ask_smapi_model.v1.skill.manifest.skill_manifest_privacy_and_compliance.SkillManifestPrivacyAndCompliance',
        'events': 'ask_smapi_model.v1.skill.manifest.skill_manifest_events.SkillManifestEvents',
        'permissions': 'list[ask_smapi_model.v1.skill.manifest.permission_items.PermissionItems]',
        'apis': 'ask_smapi_model.v1.skill.manifest.skill_manifest_apis.SkillManifestApis'
    }  # type: Dict

    attribute_map = {
        'manifest_version': 'manifestVersion',
        'publishing_information': 'publishingInformation',
        'privacy_and_compliance': 'privacyAndCompliance',
        'events': 'events',
        'permissions': 'permissions',
        'apis': 'apis'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, manifest_version=None, publishing_information=None, privacy_and_compliance=None, events=None, permissions=None, apis=None):
        # type: (Optional[str], Optional[Manifest_SkillManifestPublishingInformationV1], Optional[Manifest_SkillManifestPrivacyAndComplianceV1], Optional[Manifest_SkillManifestEventsV1], Optional[List[Manifest_PermissionItemsV1]], Optional[Manifest_SkillManifestApisV1]) -> None
        """Defines the structure for a skill&#39;s metadata.

        :param manifest_version: Version of the skill manifest.
        :type manifest_version: (optional) str
        :param publishing_information: 
        :type publishing_information: (optional) ask_smapi_model.v1.skill.manifest.skill_manifest_publishing_information.SkillManifestPublishingInformation
        :param privacy_and_compliance: 
        :type privacy_and_compliance: (optional) ask_smapi_model.v1.skill.manifest.skill_manifest_privacy_and_compliance.SkillManifestPrivacyAndCompliance
        :param events: 
        :type events: (optional) ask_smapi_model.v1.skill.manifest.skill_manifest_events.SkillManifestEvents
        :param permissions: Defines the structure for required permissions information in the skill manifest.
        :type permissions: (optional) list[ask_smapi_model.v1.skill.manifest.permission_items.PermissionItems]
        :param apis: 
        :type apis: (optional) ask_smapi_model.v1.skill.manifest.skill_manifest_apis.SkillManifestApis
        """
        self.__discriminator_value = None  # type: str

        self.manifest_version = manifest_version
        self.publishing_information = publishing_information
        self.privacy_and_compliance = privacy_and_compliance
        self.events = events
        self.permissions = permissions
        self.apis = apis

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
        if not isinstance(other, SkillManifest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
