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
    from ask_smapi_model.v1.skill.overwrite_mode import OverwriteMode as Skill_OverwriteModeV1


class CloneLocaleRequest(object):
    """
    Defines the request body for the cloneLocale API.


    :param source_locale: Locale with the assets that will be cloned.
    :type source_locale: (optional) str
    :param target_locales: A list of locale(s) where the assets will be copied to.
    :type target_locales: (optional) list[str]
    :param overwrite_mode: Can locale of skill be overwritten. Default value is DO_NOT_OVERWRITE.
    :type overwrite_mode: (optional) ask_smapi_model.v1.skill.overwrite_mode.OverwriteMode

    """
    deserialized_types = {
        'source_locale': 'str',
        'target_locales': 'list[str]',
        'overwrite_mode': 'ask_smapi_model.v1.skill.overwrite_mode.OverwriteMode'
    }  # type: Dict

    attribute_map = {
        'source_locale': 'sourceLocale',
        'target_locales': 'targetLocales',
        'overwrite_mode': 'overwriteMode'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, source_locale=None, target_locales=None, overwrite_mode=None):
        # type: (Optional[str], Optional[List[object]], Optional[Skill_OverwriteModeV1]) -> None
        """Defines the request body for the cloneLocale API.

        :param source_locale: Locale with the assets that will be cloned.
        :type source_locale: (optional) str
        :param target_locales: A list of locale(s) where the assets will be copied to.
        :type target_locales: (optional) list[str]
        :param overwrite_mode: Can locale of skill be overwritten. Default value is DO_NOT_OVERWRITE.
        :type overwrite_mode: (optional) ask_smapi_model.v1.skill.overwrite_mode.OverwriteMode
        """
        self.__discriminator_value = None  # type: str

        self.source_locale = source_locale
        self.target_locales = target_locales
        self.overwrite_mode = overwrite_mode

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
        if not isinstance(other, CloneLocaleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
