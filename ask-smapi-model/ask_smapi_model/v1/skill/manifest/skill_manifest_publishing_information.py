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
    from ask_smapi_model.v1.skill.manifest.skill_manifest_localized_publishing_information import SkillManifestLocalizedPublishingInformation as Manifest_SkillManifestLocalizedPublishingInformationV1
    from ask_smapi_model.v1.skill.manifest.distribution_mode import DistributionMode as Manifest_DistributionModeV1
    from ask_smapi_model.v1.skill.manifest.manifest_gadget_support import ManifestGadgetSupport as Manifest_ManifestGadgetSupportV1
    from ask_smapi_model.v1.skill.manifest.distribution_countries import DistributionCountries as Manifest_DistributionCountriesV1


class SkillManifestPublishingInformation(object):
    """
    Defines the structure for publishing information in the skill manifest.


    :param name: Name of the skill that is displayed to customers in the Alexa app.
    :type name: (optional) str
    :param description: Description of the skill&#39;s purpose and feature and how it works. Should describe any prerequisites like hardware or account requirements and detailed steps for the customer to get started. For Flash Briefing skill list the feeds offered within the skill. Use a conversational tone and correct grammar and punctuation. This description displays to customers on the skill detail card in the Alexa app.
    :type description: (optional) str
    :param locales: Defines the structure for locale specific publishing information in the skill manifest.
    :type locales: (optional) dict(str, ask_smapi_model.v1.skill.manifest.skill_manifest_localized_publishing_information.SkillManifestLocalizedPublishingInformation)
    :param is_available_worldwide: True if the skill should be distributed in all countries where Amazon distributes skill false otherwise.
    :type is_available_worldwide: (optional) bool
    :param distribution_mode: 
    :type distribution_mode: (optional) ask_smapi_model.v1.skill.manifest.distribution_mode.DistributionMode
    :param gadget_support: 
    :type gadget_support: (optional) ask_smapi_model.v1.skill.manifest.manifest_gadget_support.ManifestGadgetSupport
    :param testing_instructions: Special instructions provided by the developer to test the skill.
    :type testing_instructions: (optional) str
    :param category: Category that best describes a skill. Indicates the filter category for the skill in the Alexa App.
    :type category: (optional) str
    :param distribution_countries: Selected list of countries provided by the skill owner where Amazon can distribute the skill.
    :type distribution_countries: (optional) list[ask_smapi_model.v1.skill.manifest.distribution_countries.DistributionCountries]

    """
    deserialized_types = {
        'name': 'str',
        'description': 'str',
        'locales': 'dict(str, ask_smapi_model.v1.skill.manifest.skill_manifest_localized_publishing_information.SkillManifestLocalizedPublishingInformation)',
        'is_available_worldwide': 'bool',
        'distribution_mode': 'ask_smapi_model.v1.skill.manifest.distribution_mode.DistributionMode',
        'gadget_support': 'ask_smapi_model.v1.skill.manifest.manifest_gadget_support.ManifestGadgetSupport',
        'testing_instructions': 'str',
        'category': 'str',
        'distribution_countries': 'list[ask_smapi_model.v1.skill.manifest.distribution_countries.DistributionCountries]'
    }  # type: Dict

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'locales': 'locales',
        'is_available_worldwide': 'isAvailableWorldwide',
        'distribution_mode': 'distributionMode',
        'gadget_support': 'gadgetSupport',
        'testing_instructions': 'testingInstructions',
        'category': 'category',
        'distribution_countries': 'distributionCountries'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, name=None, description=None, locales=None, is_available_worldwide=None, distribution_mode=None, gadget_support=None, testing_instructions=None, category=None, distribution_countries=None):
        # type: (Optional[str], Optional[str], Optional[Dict[str, Manifest_SkillManifestLocalizedPublishingInformationV1]], Optional[bool], Optional[Manifest_DistributionModeV1], Optional[Manifest_ManifestGadgetSupportV1], Optional[str], Optional[str], Optional[List[Manifest_DistributionCountriesV1]]) -> None
        """Defines the structure for publishing information in the skill manifest.

        :param name: Name of the skill that is displayed to customers in the Alexa app.
        :type name: (optional) str
        :param description: Description of the skill&#39;s purpose and feature and how it works. Should describe any prerequisites like hardware or account requirements and detailed steps for the customer to get started. For Flash Briefing skill list the feeds offered within the skill. Use a conversational tone and correct grammar and punctuation. This description displays to customers on the skill detail card in the Alexa app.
        :type description: (optional) str
        :param locales: Defines the structure for locale specific publishing information in the skill manifest.
        :type locales: (optional) dict(str, ask_smapi_model.v1.skill.manifest.skill_manifest_localized_publishing_information.SkillManifestLocalizedPublishingInformation)
        :param is_available_worldwide: True if the skill should be distributed in all countries where Amazon distributes skill false otherwise.
        :type is_available_worldwide: (optional) bool
        :param distribution_mode: 
        :type distribution_mode: (optional) ask_smapi_model.v1.skill.manifest.distribution_mode.DistributionMode
        :param gadget_support: 
        :type gadget_support: (optional) ask_smapi_model.v1.skill.manifest.manifest_gadget_support.ManifestGadgetSupport
        :param testing_instructions: Special instructions provided by the developer to test the skill.
        :type testing_instructions: (optional) str
        :param category: Category that best describes a skill. Indicates the filter category for the skill in the Alexa App.
        :type category: (optional) str
        :param distribution_countries: Selected list of countries provided by the skill owner where Amazon can distribute the skill.
        :type distribution_countries: (optional) list[ask_smapi_model.v1.skill.manifest.distribution_countries.DistributionCountries]
        """
        self.__discriminator_value = None  # type: str

        self.name = name
        self.description = description
        self.locales = locales
        self.is_available_worldwide = is_available_worldwide
        self.distribution_mode = distribution_mode
        self.gadget_support = gadget_support
        self.testing_instructions = testing_instructions
        self.category = category
        self.distribution_countries = distribution_countries

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
        if not isinstance(other, SkillManifestPublishingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
