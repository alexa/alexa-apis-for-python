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
    from ask_smapi_model.v1.links import Links as V1_LinksV1
    from ask_smapi_model.v1.skill.skill_summary import SkillSummary as Skill_SkillSummaryV1


class ListSkillResponse(object):
    """
    List of skills for the vendor.


    :param links: 
    :type links: (optional) ask_smapi_model.v1.links.Links
    :param skills: List of skill summaries. List might contain either one, two or three entries for a given skillId depending on the skill&#39;s publication history and the publication method. &#x60;Skill containing certified stage&#x60; * If a skill was never published to live, this list will contain two entries &#x60;:&#x60; one with stage &#39;development&#39; and another with stage &#39;certified&#39;. Both of these summaries will have same skillId. * For any skill that has been published to &#39;live&#39;, this list will contain three entries &#x60;:&#x60; one with stage &#39;development&#39;, one with stage &#x60;certified&#x60; and one with stage &#39;live&#39;. All of these summaries will have same skillId. &#x60;Skill without certified stage&#x60; * If a skill was never published to live, this list will contain only one entry for the skill with stage as &#39;development&#39;. * For any skill that has been published to &#39;live&#39;, this list will contain two entries &#x60;:&#x60; one with stage &#39;development&#39; and another with stage &#39;live&#39;. Both of these summaries will have same skillId. 
    :type skills: (optional) list[ask_smapi_model.v1.skill.skill_summary.SkillSummary]
    :param is_truncated: 
    :type is_truncated: (optional) bool
    :param next_token: 
    :type next_token: (optional) str

    """
    deserialized_types = {
        'links': 'ask_smapi_model.v1.links.Links',
        'skills': 'list[ask_smapi_model.v1.skill.skill_summary.SkillSummary]',
        'is_truncated': 'bool',
        'next_token': 'str'
    }  # type: Dict

    attribute_map = {
        'links': '_links',
        'skills': 'skills',
        'is_truncated': 'isTruncated',
        'next_token': 'nextToken'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, links=None, skills=None, is_truncated=None, next_token=None):
        # type: (Optional[V1_LinksV1], Optional[List[Skill_SkillSummaryV1]], Optional[bool], Optional[str]) -> None
        """List of skills for the vendor.

        :param links: 
        :type links: (optional) ask_smapi_model.v1.links.Links
        :param skills: List of skill summaries. List might contain either one, two or three entries for a given skillId depending on the skill&#39;s publication history and the publication method. &#x60;Skill containing certified stage&#x60; * If a skill was never published to live, this list will contain two entries &#x60;:&#x60; one with stage &#39;development&#39; and another with stage &#39;certified&#39;. Both of these summaries will have same skillId. * For any skill that has been published to &#39;live&#39;, this list will contain three entries &#x60;:&#x60; one with stage &#39;development&#39;, one with stage &#x60;certified&#x60; and one with stage &#39;live&#39;. All of these summaries will have same skillId. &#x60;Skill without certified stage&#x60; * If a skill was never published to live, this list will contain only one entry for the skill with stage as &#39;development&#39;. * For any skill that has been published to &#39;live&#39;, this list will contain two entries &#x60;:&#x60; one with stage &#39;development&#39; and another with stage &#39;live&#39;. Both of these summaries will have same skillId. 
        :type skills: (optional) list[ask_smapi_model.v1.skill.skill_summary.SkillSummary]
        :param is_truncated: 
        :type is_truncated: (optional) bool
        :param next_token: 
        :type next_token: (optional) str
        """
        self.__discriminator_value = None  # type: str

        self.links = links
        self.skills = skills
        self.is_truncated = is_truncated
        self.next_token = next_token

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
        if not isinstance(other, ListSkillResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
