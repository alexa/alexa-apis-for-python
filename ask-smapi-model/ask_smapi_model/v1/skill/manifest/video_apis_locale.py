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
    from ask_smapi_model.v1.skill.manifest.video_prompt_name import VideoPromptName as VideoPromptName_d8845a65
    from ask_smapi_model.v1.skill.manifest.video_fire_tv_catalog_ingestion import VideoFireTvCatalogIngestion as VideoFireTvCatalogIngestion_66ff327d
    from ask_smapi_model.v1.skill.manifest.video_feature import VideoFeature as VideoFeature_d9ebf070


class VideoApisLocale(object):
    """
    Defines the structure for localized video api information.


    :param video_provider_targeting_names: Defines the video provider&#39;s targeting name.
    :type video_provider_targeting_names: (optional) list[str]
    :param video_provider_logo_uri: 
    :type video_provider_logo_uri: (optional) str
    :param fire_tv_catalog_ingestion: 
    :type fire_tv_catalog_ingestion: (optional) ask_smapi_model.v1.skill.manifest.video_fire_tv_catalog_ingestion.VideoFireTvCatalogIngestion
    :param features: Defines the array of video features for this skill.
    :type features: (optional) list[ask_smapi_model.v1.skill.manifest.video_feature.VideoFeature]
    :param prompt_names: Name to use when Alexa renders the video skill name in a prompt to the user
    :type prompt_names: (optional) list[ask_smapi_model.v1.skill.manifest.video_prompt_name.VideoPromptName]

    """
    deserialized_types = {
        'video_provider_targeting_names': 'list[str]',
        'video_provider_logo_uri': 'str',
        'fire_tv_catalog_ingestion': 'ask_smapi_model.v1.skill.manifest.video_fire_tv_catalog_ingestion.VideoFireTvCatalogIngestion',
        'features': 'list[ask_smapi_model.v1.skill.manifest.video_feature.VideoFeature]',
        'prompt_names': 'list[ask_smapi_model.v1.skill.manifest.video_prompt_name.VideoPromptName]'
    }  # type: Dict

    attribute_map = {
        'video_provider_targeting_names': 'videoProviderTargetingNames',
        'video_provider_logo_uri': 'videoProviderLogoUri',
        'fire_tv_catalog_ingestion': 'fireTvCatalogIngestion',
        'features': 'features',
        'prompt_names': 'promptNames'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, video_provider_targeting_names=None, video_provider_logo_uri=None, fire_tv_catalog_ingestion=None, features=None, prompt_names=None):
        # type: (Optional[List[object]], Optional[str], Optional[VideoFireTvCatalogIngestion_66ff327d], Optional[List[VideoFeature_d9ebf070]], Optional[List[VideoPromptName_d8845a65]]) -> None
        """Defines the structure for localized video api information.

        :param video_provider_targeting_names: Defines the video provider&#39;s targeting name.
        :type video_provider_targeting_names: (optional) list[str]
        :param video_provider_logo_uri: 
        :type video_provider_logo_uri: (optional) str
        :param fire_tv_catalog_ingestion: 
        :type fire_tv_catalog_ingestion: (optional) ask_smapi_model.v1.skill.manifest.video_fire_tv_catalog_ingestion.VideoFireTvCatalogIngestion
        :param features: Defines the array of video features for this skill.
        :type features: (optional) list[ask_smapi_model.v1.skill.manifest.video_feature.VideoFeature]
        :param prompt_names: Name to use when Alexa renders the video skill name in a prompt to the user
        :type prompt_names: (optional) list[ask_smapi_model.v1.skill.manifest.video_prompt_name.VideoPromptName]
        """
        self.__discriminator_value = None  # type: str

        self.video_provider_targeting_names = video_provider_targeting_names
        self.video_provider_logo_uri = video_provider_logo_uri
        self.fire_tv_catalog_ingestion = fire_tv_catalog_ingestion
        self.features = features
        self.prompt_names = prompt_names

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
        if not isinstance(other, VideoApisLocale):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
