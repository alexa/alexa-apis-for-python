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
    from ask_smapi_model.v1.stage_v2_type import StageV2Type as V1_StageV2TypeV1
    from ask_smapi_model.v1.skill.skill_summary_apis import SkillSummaryApis as Skill_SkillSummaryApisV1
    from ask_smapi_model.v1.skill.publication_status import PublicationStatus as Skill_PublicationStatusV1


class SkillSummary(object):
    """
    Information about the skills.


    :param skill_id: 
    :type skill_id: (optional) str
    :param stage: 
    :type stage: (optional) ask_smapi_model.v1.stage_v2_type.StageV2Type
    :param apis: List of APIs currently implemented by the skill.
    :type apis: (optional) list[ask_smapi_model.v1.skill.skill_summary_apis.SkillSummaryApis]
    :param publication_status: 
    :type publication_status: (optional) ask_smapi_model.v1.skill.publication_status.PublicationStatus
    :param last_updated: 
    :type last_updated: (optional) datetime
    :param name_by_locale: Name of the skill in skill locales (keys are locale names (e.g. &#39;en-US&#39;) whereas values are name of the skill in that locale. 
    :type name_by_locale: (optional) dict(str, str)
    :param asin: Amazon Standard Identification Number (ASIN) is unique blocks of 10 letters and/or numbers that identify items. More info about ASIN can be found here: https://www.amazon.com/gp/seller/asin-upc-isbn-info.html ASIN is available for those skills only, that have been published, at least once. 
    :type asin: (optional) str
    :param links: 
    :type links: (optional) ask_smapi_model.v1.links.Links

    """
    deserialized_types = {
        'skill_id': 'str',
        'stage': 'ask_smapi_model.v1.stage_v2_type.StageV2Type',
        'apis': 'list[ask_smapi_model.v1.skill.skill_summary_apis.SkillSummaryApis]',
        'publication_status': 'ask_smapi_model.v1.skill.publication_status.PublicationStatus',
        'last_updated': 'datetime',
        'name_by_locale': 'dict(str, str)',
        'asin': 'str',
        'links': 'ask_smapi_model.v1.links.Links'
    }  # type: Dict

    attribute_map = {
        'skill_id': 'skillId',
        'stage': 'stage',
        'apis': 'apis',
        'publication_status': 'publicationStatus',
        'last_updated': 'lastUpdated',
        'name_by_locale': 'nameByLocale',
        'asin': 'asin',
        'links': '_links'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, skill_id=None, stage=None, apis=None, publication_status=None, last_updated=None, name_by_locale=None, asin=None, links=None):
        # type: (Optional[str], Optional[V1_StageV2TypeV1], Optional[List[Skill_SkillSummaryApisV1]], Optional[Skill_PublicationStatusV1], Optional[datetime], Optional[Dict[str, object]], Optional[str], Optional[V1_LinksV1]) -> None
        """Information about the skills.

        :param skill_id: 
        :type skill_id: (optional) str
        :param stage: 
        :type stage: (optional) ask_smapi_model.v1.stage_v2_type.StageV2Type
        :param apis: List of APIs currently implemented by the skill.
        :type apis: (optional) list[ask_smapi_model.v1.skill.skill_summary_apis.SkillSummaryApis]
        :param publication_status: 
        :type publication_status: (optional) ask_smapi_model.v1.skill.publication_status.PublicationStatus
        :param last_updated: 
        :type last_updated: (optional) datetime
        :param name_by_locale: Name of the skill in skill locales (keys are locale names (e.g. &#39;en-US&#39;) whereas values are name of the skill in that locale. 
        :type name_by_locale: (optional) dict(str, str)
        :param asin: Amazon Standard Identification Number (ASIN) is unique blocks of 10 letters and/or numbers that identify items. More info about ASIN can be found here: https://www.amazon.com/gp/seller/asin-upc-isbn-info.html ASIN is available for those skills only, that have been published, at least once. 
        :type asin: (optional) str
        :param links: 
        :type links: (optional) ask_smapi_model.v1.links.Links
        """
        self.__discriminator_value = None  # type: str

        self.skill_id = skill_id
        self.stage = stage
        self.apis = apis
        self.publication_status = publication_status
        self.last_updated = last_updated
        self.name_by_locale = name_by_locale
        self.asin = asin
        self.links = links

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
        if not isinstance(other, SkillSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
