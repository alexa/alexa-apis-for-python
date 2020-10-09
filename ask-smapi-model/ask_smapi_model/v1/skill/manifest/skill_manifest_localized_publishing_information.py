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


class SkillManifestLocalizedPublishingInformation(object):
    """
    Defines the structure for locale specific publishing information in the skill manifest.


    :param name: Name of the skill that is displayed to customers in the Alexa app.
    :type name: (optional) str
    :param small_icon_uri: URL to a small icon for the skill, which is shown in the list of skills (108x108px).
    :type small_icon_uri: (optional) str
    :param large_icon_uri: URL to a large icon that represents this skill (512x512px).
    :type large_icon_uri: (optional) str
    :param summary: Summary description of the skill, which is shown when viewing the list of skills.
    :type summary: (optional) str
    :param description: A full description explaining the skill’s core functionality and any prerequisites to using it (such as additional hardware, software, or accounts). For a Flash Briefing skill, you must list the feeds for the skill.
    :type description: (optional) str
    :param updates_description: Updates description of the skill&#39;s new features and fixes in the version. Should describe changes in the revisions of the skill.
    :type updates_description: (optional) str
    :param example_phrases: Three example phrases that illustrate how users can invoke your skill. For accuracy, these phrases must come directly from your sample utterances.
    :type example_phrases: (optional) list[str]
    :param keywords: Sample keyword phrases that describe the skill.
    :type keywords: (optional) list[str]

    """
    deserialized_types = {
        'name': 'str',
        'small_icon_uri': 'str',
        'large_icon_uri': 'str',
        'summary': 'str',
        'description': 'str',
        'updates_description': 'str',
        'example_phrases': 'list[str]',
        'keywords': 'list[str]'
    }  # type: Dict

    attribute_map = {
        'name': 'name',
        'small_icon_uri': 'smallIconUri',
        'large_icon_uri': 'largeIconUri',
        'summary': 'summary',
        'description': 'description',
        'updates_description': 'updatesDescription',
        'example_phrases': 'examplePhrases',
        'keywords': 'keywords'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, name=None, small_icon_uri=None, large_icon_uri=None, summary=None, description=None, updates_description=None, example_phrases=None, keywords=None):
        # type: (Optional[str], Optional[str], Optional[str], Optional[str], Optional[str], Optional[str], Optional[List[object]], Optional[List[object]]) -> None
        """Defines the structure for locale specific publishing information in the skill manifest.

        :param name: Name of the skill that is displayed to customers in the Alexa app.
        :type name: (optional) str
        :param small_icon_uri: URL to a small icon for the skill, which is shown in the list of skills (108x108px).
        :type small_icon_uri: (optional) str
        :param large_icon_uri: URL to a large icon that represents this skill (512x512px).
        :type large_icon_uri: (optional) str
        :param summary: Summary description of the skill, which is shown when viewing the list of skills.
        :type summary: (optional) str
        :param description: A full description explaining the skill’s core functionality and any prerequisites to using it (such as additional hardware, software, or accounts). For a Flash Briefing skill, you must list the feeds for the skill.
        :type description: (optional) str
        :param updates_description: Updates description of the skill&#39;s new features and fixes in the version. Should describe changes in the revisions of the skill.
        :type updates_description: (optional) str
        :param example_phrases: Three example phrases that illustrate how users can invoke your skill. For accuracy, these phrases must come directly from your sample utterances.
        :type example_phrases: (optional) list[str]
        :param keywords: Sample keyword phrases that describe the skill.
        :type keywords: (optional) list[str]
        """
        self.__discriminator_value = None  # type: str

        self.name = name
        self.small_icon_uri = small_icon_uri
        self.large_icon_uri = large_icon_uri
        self.summary = summary
        self.description = description
        self.updates_description = updates_description
        self.example_phrases = example_phrases
        self.keywords = keywords

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
        if not isinstance(other, SkillManifestLocalizedPublishingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
