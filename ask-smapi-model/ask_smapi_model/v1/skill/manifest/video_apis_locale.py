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
    from ask_smapi_model.v1.skill.manifest.video_catalog_info import VideoCatalogInfo as Manifest_VideoCatalogInfoV1


class VideoApisLocale(object):
    """
    Defines the structure for localized video api information.


    :param video_provider_targeting_names: Defines the video provider&#39;s targeting name.
    :type video_provider_targeting_names: (optional) list[str]
    :param video_provider_logo_uri: 
    :type video_provider_logo_uri: (optional) str
    :param catalog_information: 
    :type catalog_information: (optional) list[ask_smapi_model.v1.skill.manifest.video_catalog_info.VideoCatalogInfo]

    """
    deserialized_types = {
        'video_provider_targeting_names': 'list[str]',
        'video_provider_logo_uri': 'str',
        'catalog_information': 'list[ask_smapi_model.v1.skill.manifest.video_catalog_info.VideoCatalogInfo]'
    }  # type: Dict

    attribute_map = {
        'video_provider_targeting_names': 'videoProviderTargetingNames',
        'video_provider_logo_uri': 'videoProviderLogoUri',
        'catalog_information': 'catalogInformation'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, video_provider_targeting_names=None, video_provider_logo_uri=None, catalog_information=None):
        # type: (Optional[List[object]], Optional[str], Optional[List[Manifest_VideoCatalogInfoV1]]) -> None
        """Defines the structure for localized video api information.

        :param video_provider_targeting_names: Defines the video provider&#39;s targeting name.
        :type video_provider_targeting_names: (optional) list[str]
        :param video_provider_logo_uri: 
        :type video_provider_logo_uri: (optional) str
        :param catalog_information: 
        :type catalog_information: (optional) list[ask_smapi_model.v1.skill.manifest.video_catalog_info.VideoCatalogInfo]
        """
        self.__discriminator_value = None  # type: str

        self.video_provider_targeting_names = video_provider_targeting_names
        self.video_provider_logo_uri = video_provider_logo_uri
        self.catalog_information = catalog_information

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
