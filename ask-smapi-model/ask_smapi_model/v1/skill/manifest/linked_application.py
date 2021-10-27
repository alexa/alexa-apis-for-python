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
    from ask_smapi_model.v1.skill.manifest.catalog_info import CatalogInfo as CatalogInfo_3fade9c6
    from ask_smapi_model.v1.skill.manifest.android_custom_intent import AndroidCustomIntent as AndroidCustomIntent_f7a91c8f
    from ask_smapi_model.v1.skill.manifest.friendly_name import FriendlyName as FriendlyName_168112fe


class LinkedApplication(object):
    """
    Applications associated with the skill.


    :param catalog_info: 
    :type catalog_info: (optional) ask_smapi_model.v1.skill.manifest.catalog_info.CatalogInfo
    :param custom_schemes: Supported schemes
    :type custom_schemes: (optional) list[str]
    :param domains: Supported domains
    :type domains: (optional) list[str]
    :param friendly_name: 
    :type friendly_name: (optional) ask_smapi_model.v1.skill.manifest.friendly_name.FriendlyName
    :param android_custom_intents: Supported android custom intent
    :type android_custom_intents: (optional) list[ask_smapi_model.v1.skill.manifest.android_custom_intent.AndroidCustomIntent]

    """
    deserialized_types = {
        'catalog_info': 'ask_smapi_model.v1.skill.manifest.catalog_info.CatalogInfo',
        'custom_schemes': 'list[str]',
        'domains': 'list[str]',
        'friendly_name': 'ask_smapi_model.v1.skill.manifest.friendly_name.FriendlyName',
        'android_custom_intents': 'list[ask_smapi_model.v1.skill.manifest.android_custom_intent.AndroidCustomIntent]'
    }  # type: Dict

    attribute_map = {
        'catalog_info': 'catalogInfo',
        'custom_schemes': 'customSchemes',
        'domains': 'domains',
        'friendly_name': 'friendlyName',
        'android_custom_intents': 'androidCustomIntents'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, catalog_info=None, custom_schemes=None, domains=None, friendly_name=None, android_custom_intents=None):
        # type: (Optional[CatalogInfo_3fade9c6], Optional[List[object]], Optional[List[object]], Optional[FriendlyName_168112fe], Optional[List[AndroidCustomIntent_f7a91c8f]]) -> None
        """Applications associated with the skill.

        :param catalog_info: 
        :type catalog_info: (optional) ask_smapi_model.v1.skill.manifest.catalog_info.CatalogInfo
        :param custom_schemes: Supported schemes
        :type custom_schemes: (optional) list[str]
        :param domains: Supported domains
        :type domains: (optional) list[str]
        :param friendly_name: 
        :type friendly_name: (optional) ask_smapi_model.v1.skill.manifest.friendly_name.FriendlyName
        :param android_custom_intents: Supported android custom intent
        :type android_custom_intents: (optional) list[ask_smapi_model.v1.skill.manifest.android_custom_intent.AndroidCustomIntent]
        """
        self.__discriminator_value = None  # type: str

        self.catalog_info = catalog_info
        self.custom_schemes = custom_schemes
        self.domains = domains
        self.friendly_name = friendly_name
        self.android_custom_intents = android_custom_intents

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
        if not isinstance(other, LinkedApplication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
