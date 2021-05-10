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
    from ask_smapi_model.v1.skill.manifest.smart_home_apis import SmartHomeApis as SmartHomeApis_768def7d
    from ask_smapi_model.v1.skill.manifest.demand_response_apis import DemandResponseApis as DemandResponseApis_d15fcaf7
    from ask_smapi_model.v1.skill.manifest.music_apis import MusicApis as MusicApis_7489e85c
    from ask_smapi_model.v1.skill.manifest.alexa_for_business_apis import AlexaForBusinessApis as AlexaForBusinessApis_8e9dbc0
    from ask_smapi_model.v1.skill.manifest.custom_apis import CustomApis as CustomApis_e197110a
    from ask_smapi_model.v1.skill.manifest.house_hold_list import HouseHoldList as HouseHoldList_76371b75
    from ask_smapi_model.v1.skill.manifest.video_apis import VideoApis as VideoApis_f912969c
    from ask_smapi_model.v1.skill.manifest.flash_briefing_apis import FlashBriefingApis as FlashBriefingApis_a7aeebab
    from ask_smapi_model.v1.skill.manifest.knowledge_apis import KnowledgeApis as KnowledgeApis_966f57bc


class SkillManifestApis(object):
    """
    Defines the structure for implemented apis information in the skill manifest.


    :param flash_briefing: 
    :type flash_briefing: (optional) ask_smapi_model.v1.skill.manifest.flash_briefing_apis.FlashBriefingApis
    :param custom: 
    :type custom: (optional) ask_smapi_model.v1.skill.manifest.custom_apis.CustomApis
    :param knowledge: 
    :type knowledge: (optional) ask_smapi_model.v1.skill.manifest.knowledge_apis.KnowledgeApis
    :param smart_home: 
    :type smart_home: (optional) ask_smapi_model.v1.skill.manifest.smart_home_apis.SmartHomeApis
    :param video: 
    :type video: (optional) ask_smapi_model.v1.skill.manifest.video_apis.VideoApis
    :param alexa_for_business: 
    :type alexa_for_business: (optional) ask_smapi_model.v1.skill.manifest.alexa_for_business_apis.AlexaForBusinessApis
    :param household_list: 
    :type household_list: (optional) ask_smapi_model.v1.skill.manifest.house_hold_list.HouseHoldList
    :param music: 
    :type music: (optional) ask_smapi_model.v1.skill.manifest.music_apis.MusicApis
    :param demand_response: 
    :type demand_response: (optional) ask_smapi_model.v1.skill.manifest.demand_response_apis.DemandResponseApis

    """
    deserialized_types = {
        'flash_briefing': 'ask_smapi_model.v1.skill.manifest.flash_briefing_apis.FlashBriefingApis',
        'custom': 'ask_smapi_model.v1.skill.manifest.custom_apis.CustomApis',
        'knowledge': 'ask_smapi_model.v1.skill.manifest.knowledge_apis.KnowledgeApis',
        'smart_home': 'ask_smapi_model.v1.skill.manifest.smart_home_apis.SmartHomeApis',
        'video': 'ask_smapi_model.v1.skill.manifest.video_apis.VideoApis',
        'alexa_for_business': 'ask_smapi_model.v1.skill.manifest.alexa_for_business_apis.AlexaForBusinessApis',
        'household_list': 'ask_smapi_model.v1.skill.manifest.house_hold_list.HouseHoldList',
        'music': 'ask_smapi_model.v1.skill.manifest.music_apis.MusicApis',
        'demand_response': 'ask_smapi_model.v1.skill.manifest.demand_response_apis.DemandResponseApis'
    }  # type: Dict

    attribute_map = {
        'flash_briefing': 'flashBriefing',
        'custom': 'custom',
        'knowledge': 'knowledge',
        'smart_home': 'smartHome',
        'video': 'video',
        'alexa_for_business': 'alexaForBusiness',
        'household_list': 'householdList',
        'music': 'music',
        'demand_response': 'demandResponse'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, flash_briefing=None, custom=None, knowledge=None, smart_home=None, video=None, alexa_for_business=None, household_list=None, music=None, demand_response=None):
        # type: (Optional[FlashBriefingApis_a7aeebab], Optional[CustomApis_e197110a], Optional[KnowledgeApis_966f57bc], Optional[SmartHomeApis_768def7d], Optional[VideoApis_f912969c], Optional[AlexaForBusinessApis_8e9dbc0], Optional[HouseHoldList_76371b75], Optional[MusicApis_7489e85c], Optional[DemandResponseApis_d15fcaf7]) -> None
        """Defines the structure for implemented apis information in the skill manifest.

        :param flash_briefing: 
        :type flash_briefing: (optional) ask_smapi_model.v1.skill.manifest.flash_briefing_apis.FlashBriefingApis
        :param custom: 
        :type custom: (optional) ask_smapi_model.v1.skill.manifest.custom_apis.CustomApis
        :param knowledge: 
        :type knowledge: (optional) ask_smapi_model.v1.skill.manifest.knowledge_apis.KnowledgeApis
        :param smart_home: 
        :type smart_home: (optional) ask_smapi_model.v1.skill.manifest.smart_home_apis.SmartHomeApis
        :param video: 
        :type video: (optional) ask_smapi_model.v1.skill.manifest.video_apis.VideoApis
        :param alexa_for_business: 
        :type alexa_for_business: (optional) ask_smapi_model.v1.skill.manifest.alexa_for_business_apis.AlexaForBusinessApis
        :param household_list: 
        :type household_list: (optional) ask_smapi_model.v1.skill.manifest.house_hold_list.HouseHoldList
        :param music: 
        :type music: (optional) ask_smapi_model.v1.skill.manifest.music_apis.MusicApis
        :param demand_response: 
        :type demand_response: (optional) ask_smapi_model.v1.skill.manifest.demand_response_apis.DemandResponseApis
        """
        self.__discriminator_value = None  # type: str

        self.flash_briefing = flash_briefing
        self.custom = custom
        self.knowledge = knowledge
        self.smart_home = smart_home
        self.video = video
        self.alexa_for_business = alexa_for_business
        self.household_list = household_list
        self.music = music
        self.demand_response = demand_response

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
        if not isinstance(other, SkillManifestApis):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
