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
    from ask_smapi_model.v1.skill.manifest.skill_manifest_localized_privacy_and_compliance import SkillManifestLocalizedPrivacyAndCompliance as Manifest_SkillManifestLocalizedPrivacyAndComplianceV1


class SkillManifestPrivacyAndCompliance(object):
    """
    Defines the structure for privacy &amp; compliance information in the skill manifest.


    :param locales: Defines the structure for locale specific privacy &amp; compliance information in the skill manifest.
    :type locales: (optional) dict(str, ask_smapi_model.v1.skill.manifest.skill_manifest_localized_privacy_and_compliance.SkillManifestLocalizedPrivacyAndCompliance)
    :param allows_purchases: True if the skill allows users to make purchases or spend real money false otherwise.
    :type allows_purchases: (optional) bool
    :param uses_personal_info: True if the skill collects users&#39; personal information false otherwise.
    :type uses_personal_info: (optional) bool
    :param is_child_directed: True if the skill is directed to or targets children under the age of 13/16 false otherwise.
    :type is_child_directed: (optional) bool
    :param is_export_compliant: True if it is certified that the skill may be imported to and exported from the United States and all other countries and regions in which Amazon operate its program or in which skill owner have authorized sales to end users (without the need for Amazon to obtain any license or clearance or take any other action) and is in full compliance with all applicable laws and regulations governing imports and export including those applicable to software that makes use of encryption technology.
    :type is_export_compliant: (optional) bool
    :param contains_ads: True if the skill contains advertising false otherwise.
    :type contains_ads: (optional) bool
    :param uses_health_info: True if the skill developer is a Covered Entity (CE) or Business Associate (BA) as defined by the Health Insurance Portability And Accountability Act (HIPAA) and the skill requires Amazon to process PHI on their behalf, false otherwise. This is an optional property and treated as false if not set.
    :type uses_health_info: (optional) bool

    """
    deserialized_types = {
        'locales': 'dict(str, ask_smapi_model.v1.skill.manifest.skill_manifest_localized_privacy_and_compliance.SkillManifestLocalizedPrivacyAndCompliance)',
        'allows_purchases': 'bool',
        'uses_personal_info': 'bool',
        'is_child_directed': 'bool',
        'is_export_compliant': 'bool',
        'contains_ads': 'bool',
        'uses_health_info': 'bool'
    }  # type: Dict

    attribute_map = {
        'locales': 'locales',
        'allows_purchases': 'allowsPurchases',
        'uses_personal_info': 'usesPersonalInfo',
        'is_child_directed': 'isChildDirected',
        'is_export_compliant': 'isExportCompliant',
        'contains_ads': 'containsAds',
        'uses_health_info': 'usesHealthInfo'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, locales=None, allows_purchases=None, uses_personal_info=None, is_child_directed=None, is_export_compliant=None, contains_ads=None, uses_health_info=None):
        # type: (Optional[Dict[str, Manifest_SkillManifestLocalizedPrivacyAndComplianceV1]], Optional[bool], Optional[bool], Optional[bool], Optional[bool], Optional[bool], Optional[bool]) -> None
        """Defines the structure for privacy &amp; compliance information in the skill manifest.

        :param locales: Defines the structure for locale specific privacy &amp; compliance information in the skill manifest.
        :type locales: (optional) dict(str, ask_smapi_model.v1.skill.manifest.skill_manifest_localized_privacy_and_compliance.SkillManifestLocalizedPrivacyAndCompliance)
        :param allows_purchases: True if the skill allows users to make purchases or spend real money false otherwise.
        :type allows_purchases: (optional) bool
        :param uses_personal_info: True if the skill collects users&#39; personal information false otherwise.
        :type uses_personal_info: (optional) bool
        :param is_child_directed: True if the skill is directed to or targets children under the age of 13/16 false otherwise.
        :type is_child_directed: (optional) bool
        :param is_export_compliant: True if it is certified that the skill may be imported to and exported from the United States and all other countries and regions in which Amazon operate its program or in which skill owner have authorized sales to end users (without the need for Amazon to obtain any license or clearance or take any other action) and is in full compliance with all applicable laws and regulations governing imports and export including those applicable to software that makes use of encryption technology.
        :type is_export_compliant: (optional) bool
        :param contains_ads: True if the skill contains advertising false otherwise.
        :type contains_ads: (optional) bool
        :param uses_health_info: True if the skill developer is a Covered Entity (CE) or Business Associate (BA) as defined by the Health Insurance Portability And Accountability Act (HIPAA) and the skill requires Amazon to process PHI on their behalf, false otherwise. This is an optional property and treated as false if not set.
        :type uses_health_info: (optional) bool
        """
        self.__discriminator_value = None  # type: str

        self.locales = locales
        self.allows_purchases = allows_purchases
        self.uses_personal_info = uses_personal_info
        self.is_child_directed = is_child_directed
        self.is_export_compliant = is_export_compliant
        self.contains_ads = contains_ads
        self.uses_health_info = uses_health_info

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
        if not isinstance(other, SkillManifestPrivacyAndCompliance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
