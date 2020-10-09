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
    from ask_smapi_model.v1.skill.manifest.flash_briefing_content_type import FlashBriefingContentType as Manifest_FlashBriefingContentTypeV1
    from ask_smapi_model.v1.skill.manifest.flash_briefing_update_frequency import FlashBriefingUpdateFrequency as Manifest_FlashBriefingUpdateFrequencyV1
    from ask_smapi_model.v1.skill.manifest.flash_briefing_genre import FlashBriefingGenre as Manifest_FlashBriefingGenreV1


class LocalizedFlashBriefingInfoItems(object):
    """

    :param logical_name: Logical name of the feed. This is used to signify relation among feeds across different locales. Example If you have \&quot;weather\&quot; feed in multiple locale then consider naming it \&quot;weather_update\&quot; and we will make sure to play the right feed if customer changes the language on device.
    :type logical_name: (optional) str
    :param name: Name that identifies this feed.
    :type name: (optional) str
    :param url: Url for the feed
    :type url: (optional) str
    :param image_uri: Uri for the feed image
    :type image_uri: (optional) str
    :param content_type: 
    :type content_type: (optional) ask_smapi_model.v1.skill.manifest.flash_briefing_content_type.FlashBriefingContentType
    :param genre: 
    :type genre: (optional) ask_smapi_model.v1.skill.manifest.flash_briefing_genre.FlashBriefingGenre
    :param update_frequency: 
    :type update_frequency: (optional) ask_smapi_model.v1.skill.manifest.flash_briefing_update_frequency.FlashBriefingUpdateFrequency
    :param vui_preamble: A short introduction for the feed that Alexa reads to the customer before the feed contents. Should start with \&quot;In\&quot; or \&quot;From\&quot;.
    :type vui_preamble: (optional) str
    :param is_default: True if this should be the default feed to be enabled when customer enables the skill false otherwise.
    :type is_default: (optional) bool

    """
    deserialized_types = {
        'logical_name': 'str',
        'name': 'str',
        'url': 'str',
        'image_uri': 'str',
        'content_type': 'ask_smapi_model.v1.skill.manifest.flash_briefing_content_type.FlashBriefingContentType',
        'genre': 'ask_smapi_model.v1.skill.manifest.flash_briefing_genre.FlashBriefingGenre',
        'update_frequency': 'ask_smapi_model.v1.skill.manifest.flash_briefing_update_frequency.FlashBriefingUpdateFrequency',
        'vui_preamble': 'str',
        'is_default': 'bool'
    }  # type: Dict

    attribute_map = {
        'logical_name': 'logicalName',
        'name': 'name',
        'url': 'url',
        'image_uri': 'imageUri',
        'content_type': 'contentType',
        'genre': 'genre',
        'update_frequency': 'updateFrequency',
        'vui_preamble': 'vuiPreamble',
        'is_default': 'isDefault'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, logical_name=None, name=None, url=None, image_uri=None, content_type=None, genre=None, update_frequency=None, vui_preamble=None, is_default=None):
        # type: (Optional[str], Optional[str], Optional[str], Optional[str], Optional[Manifest_FlashBriefingContentTypeV1], Optional[Manifest_FlashBriefingGenreV1], Optional[Manifest_FlashBriefingUpdateFrequencyV1], Optional[str], Optional[bool]) -> None
        """

        :param logical_name: Logical name of the feed. This is used to signify relation among feeds across different locales. Example If you have \&quot;weather\&quot; feed in multiple locale then consider naming it \&quot;weather_update\&quot; and we will make sure to play the right feed if customer changes the language on device.
        :type logical_name: (optional) str
        :param name: Name that identifies this feed.
        :type name: (optional) str
        :param url: Url for the feed
        :type url: (optional) str
        :param image_uri: Uri for the feed image
        :type image_uri: (optional) str
        :param content_type: 
        :type content_type: (optional) ask_smapi_model.v1.skill.manifest.flash_briefing_content_type.FlashBriefingContentType
        :param genre: 
        :type genre: (optional) ask_smapi_model.v1.skill.manifest.flash_briefing_genre.FlashBriefingGenre
        :param update_frequency: 
        :type update_frequency: (optional) ask_smapi_model.v1.skill.manifest.flash_briefing_update_frequency.FlashBriefingUpdateFrequency
        :param vui_preamble: A short introduction for the feed that Alexa reads to the customer before the feed contents. Should start with \&quot;In\&quot; or \&quot;From\&quot;.
        :type vui_preamble: (optional) str
        :param is_default: True if this should be the default feed to be enabled when customer enables the skill false otherwise.
        :type is_default: (optional) bool
        """
        self.__discriminator_value = None  # type: str

        self.logical_name = logical_name
        self.name = name
        self.url = url
        self.image_uri = image_uri
        self.content_type = content_type
        self.genre = genre
        self.update_frequency = update_frequency
        self.vui_preamble = vui_preamble
        self.is_default = is_default

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
        if not isinstance(other, LocalizedFlashBriefingInfoItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
