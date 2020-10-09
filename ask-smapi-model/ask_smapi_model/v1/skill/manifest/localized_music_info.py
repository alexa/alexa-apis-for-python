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
    from ask_smapi_model.v1.skill.manifest.music_alias import MusicAlias as Manifest_MusicAliasV1
    from ask_smapi_model.v1.skill.manifest.music_feature import MusicFeature as Manifest_MusicFeatureV1
    from ask_smapi_model.v1.skill.manifest.music_wordmark import MusicWordmark as Manifest_MusicWordmarkV1


class LocalizedMusicInfo(object):
    """
    Defines the structure of localized music information in the skill manifest.


    :param prompt_name: Name to be used when Alexa renders the music skill name.
    :type prompt_name: (optional) str
    :param aliases: 
    :type aliases: (optional) list[ask_smapi_model.v1.skill.manifest.music_alias.MusicAlias]
    :param features: 
    :type features: (optional) list[ask_smapi_model.v1.skill.manifest.music_feature.MusicFeature]
    :param wordmark_logos: 
    :type wordmark_logos: (optional) list[ask_smapi_model.v1.skill.manifest.music_wordmark.MusicWordmark]

    """
    deserialized_types = {
        'prompt_name': 'str',
        'aliases': 'list[ask_smapi_model.v1.skill.manifest.music_alias.MusicAlias]',
        'features': 'list[ask_smapi_model.v1.skill.manifest.music_feature.MusicFeature]',
        'wordmark_logos': 'list[ask_smapi_model.v1.skill.manifest.music_wordmark.MusicWordmark]'
    }  # type: Dict

    attribute_map = {
        'prompt_name': 'promptName',
        'aliases': 'aliases',
        'features': 'features',
        'wordmark_logos': 'wordmarkLogos'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, prompt_name=None, aliases=None, features=None, wordmark_logos=None):
        # type: (Optional[str], Optional[List[Manifest_MusicAliasV1]], Optional[List[Manifest_MusicFeatureV1]], Optional[List[Manifest_MusicWordmarkV1]]) -> None
        """Defines the structure of localized music information in the skill manifest.

        :param prompt_name: Name to be used when Alexa renders the music skill name.
        :type prompt_name: (optional) str
        :param aliases: 
        :type aliases: (optional) list[ask_smapi_model.v1.skill.manifest.music_alias.MusicAlias]
        :param features: 
        :type features: (optional) list[ask_smapi_model.v1.skill.manifest.music_feature.MusicFeature]
        :param wordmark_logos: 
        :type wordmark_logos: (optional) list[ask_smapi_model.v1.skill.manifest.music_wordmark.MusicWordmark]
        """
        self.__discriminator_value = None  # type: str

        self.prompt_name = prompt_name
        self.aliases = aliases
        self.features = features
        self.wordmark_logos = wordmark_logos

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
        if not isinstance(other, LocalizedMusicInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
