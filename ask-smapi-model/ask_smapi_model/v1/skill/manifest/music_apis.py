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
    from ask_smapi_model.v1.skill.manifest.lambda_endpoint import LambdaEndpoint as Manifest_LambdaEndpointV1
    from ask_smapi_model.v1.skill.manifest.music_capability import MusicCapability as Manifest_MusicCapabilityV1
    from ask_smapi_model.v1.skill.manifest.music_content_type import MusicContentType as Manifest_MusicContentTypeV1
    from ask_smapi_model.v1.skill.manifest.localized_music_info import LocalizedMusicInfo as Manifest_LocalizedMusicInfoV1
    from ask_smapi_model.v1.skill.manifest.lambda_region import LambdaRegion as Manifest_LambdaRegionV1
    from ask_smapi_model.v1.skill.manifest.music_interfaces import MusicInterfaces as Manifest_MusicInterfacesV1


class MusicApis(object):
    """
    Defines the structure of music api in the skill manifest.


    :param regions: Contains an array of the supported &lt;region&gt; Objects.
    :type regions: (optional) dict(str, ask_smapi_model.v1.skill.manifest.lambda_region.LambdaRegion)
    :param endpoint: 
    :type endpoint: (optional) ask_smapi_model.v1.skill.manifest.lambda_endpoint.LambdaEndpoint
    :param capabilities: Defines the structure of music capabilities information in the skill manifest.
    :type capabilities: (optional) list[ask_smapi_model.v1.skill.manifest.music_capability.MusicCapability]
    :param interfaces: A list of music skill interfaces that your skill supports.
    :type interfaces: (optional) list[ask_smapi_model.v1.skill.manifest.music_interfaces.MusicInterfaces]
    :param locales: Defines the structure of locale specific music information in the skill manifest.
    :type locales: (optional) dict(str, ask_smapi_model.v1.skill.manifest.localized_music_info.LocalizedMusicInfo)
    :param content_types: List of the type of content to be provided by the music skill.
    :type content_types: (optional) list[ask_smapi_model.v1.skill.manifest.music_content_type.MusicContentType]

    """
    deserialized_types = {
        'regions': 'dict(str, ask_smapi_model.v1.skill.manifest.lambda_region.LambdaRegion)',
        'endpoint': 'ask_smapi_model.v1.skill.manifest.lambda_endpoint.LambdaEndpoint',
        'capabilities': 'list[ask_smapi_model.v1.skill.manifest.music_capability.MusicCapability]',
        'interfaces': 'list[ask_smapi_model.v1.skill.manifest.music_interfaces.MusicInterfaces]',
        'locales': 'dict(str, ask_smapi_model.v1.skill.manifest.localized_music_info.LocalizedMusicInfo)',
        'content_types': 'list[ask_smapi_model.v1.skill.manifest.music_content_type.MusicContentType]'
    }  # type: Dict

    attribute_map = {
        'regions': 'regions',
        'endpoint': 'endpoint',
        'capabilities': 'capabilities',
        'interfaces': 'interfaces',
        'locales': 'locales',
        'content_types': 'contentTypes'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, regions=None, endpoint=None, capabilities=None, interfaces=None, locales=None, content_types=None):
        # type: (Optional[Dict[str, Manifest_LambdaRegionV1]], Optional[Manifest_LambdaEndpointV1], Optional[List[Manifest_MusicCapabilityV1]], Optional[List[Manifest_MusicInterfacesV1]], Optional[Dict[str, Manifest_LocalizedMusicInfoV1]], Optional[List[Manifest_MusicContentTypeV1]]) -> None
        """Defines the structure of music api in the skill manifest.

        :param regions: Contains an array of the supported &lt;region&gt; Objects.
        :type regions: (optional) dict(str, ask_smapi_model.v1.skill.manifest.lambda_region.LambdaRegion)
        :param endpoint: 
        :type endpoint: (optional) ask_smapi_model.v1.skill.manifest.lambda_endpoint.LambdaEndpoint
        :param capabilities: Defines the structure of music capabilities information in the skill manifest.
        :type capabilities: (optional) list[ask_smapi_model.v1.skill.manifest.music_capability.MusicCapability]
        :param interfaces: A list of music skill interfaces that your skill supports.
        :type interfaces: (optional) list[ask_smapi_model.v1.skill.manifest.music_interfaces.MusicInterfaces]
        :param locales: Defines the structure of locale specific music information in the skill manifest.
        :type locales: (optional) dict(str, ask_smapi_model.v1.skill.manifest.localized_music_info.LocalizedMusicInfo)
        :param content_types: List of the type of content to be provided by the music skill.
        :type content_types: (optional) list[ask_smapi_model.v1.skill.manifest.music_content_type.MusicContentType]
        """
        self.__discriminator_value = None  # type: str

        self.regions = regions
        self.endpoint = endpoint
        self.capabilities = capabilities
        self.interfaces = interfaces
        self.locales = locales
        self.content_types = content_types

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
        if not isinstance(other, MusicApis):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
