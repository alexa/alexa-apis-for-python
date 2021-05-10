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
    from ask_smapi_model.v1.skill.manifest.source_language_for_locales import SourceLanguageForLocales as SourceLanguageForLocales_eb9c404a


class AutomaticDistribution(object):
    """
    optional. Used by developer to opt in to Automatic Skill Distribution, a feature where a skill will automatically be published in new eligible locales from the same language (e.g. from \&quot;en-US\&quot; to \&quot;en-CA\&quot; and \&quot;en-GB\&quot;). Locales that the developer has already created will not be overwritten.


    :param is_active: set to true to opt in to Automatic Skill Distribution. If false, then the skill will not be considered for Automatic Skill Distribution. Note that once a skill has gone through the automatic distribution process and this value is later set to false, any locales that were published through this feature will not be reverted. Any published locales will need to be suppressed manually via contacting DAG.
    :type is_active: (optional) bool
    :param source_locale_for_languages: list of items pairing a language with a source locale. Required if isActive is set to true. For each language there must be exactly one source locale.
    :type source_locale_for_languages: (optional) list[ask_smapi_model.v1.skill.manifest.source_language_for_locales.SourceLanguageForLocales]

    """
    deserialized_types = {
        'is_active': 'bool',
        'source_locale_for_languages': 'list[ask_smapi_model.v1.skill.manifest.source_language_for_locales.SourceLanguageForLocales]'
    }  # type: Dict

    attribute_map = {
        'is_active': 'isActive',
        'source_locale_for_languages': 'sourceLocaleForLanguages'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, is_active=None, source_locale_for_languages=None):
        # type: (Optional[bool], Optional[List[SourceLanguageForLocales_eb9c404a]]) -> None
        """optional. Used by developer to opt in to Automatic Skill Distribution, a feature where a skill will automatically be published in new eligible locales from the same language (e.g. from \&quot;en-US\&quot; to \&quot;en-CA\&quot; and \&quot;en-GB\&quot;). Locales that the developer has already created will not be overwritten.

        :param is_active: set to true to opt in to Automatic Skill Distribution. If false, then the skill will not be considered for Automatic Skill Distribution. Note that once a skill has gone through the automatic distribution process and this value is later set to false, any locales that were published through this feature will not be reverted. Any published locales will need to be suppressed manually via contacting DAG.
        :type is_active: (optional) bool
        :param source_locale_for_languages: list of items pairing a language with a source locale. Required if isActive is set to true. For each language there must be exactly one source locale.
        :type source_locale_for_languages: (optional) list[ask_smapi_model.v1.skill.manifest.source_language_for_locales.SourceLanguageForLocales]
        """
        self.__discriminator_value = None  # type: str

        self.is_active = is_active
        self.source_locale_for_languages = source_locale_for_languages

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
        if not isinstance(other, AutomaticDistribution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
