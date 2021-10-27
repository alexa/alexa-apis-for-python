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
    from ask_smapi_model.v1.skill.manifest.android_common_intent_name import AndroidCommonIntentName as AndroidCommonIntentName_101c89f6
    from ask_smapi_model.v1.skill.manifest.catalog_name import CatalogName as CatalogName_f3573200


class LinkedAndroidCommonIntent(object):
    """
    Android common intents associated with the skill


    :param intent_name: 
    :type intent_name: (optional) ask_smapi_model.v1.skill.manifest.android_common_intent_name.AndroidCommonIntentName
    :param catalog_type: 
    :type catalog_type: (optional) ask_smapi_model.v1.skill.manifest.catalog_name.CatalogName

    """
    deserialized_types = {
        'intent_name': 'ask_smapi_model.v1.skill.manifest.android_common_intent_name.AndroidCommonIntentName',
        'catalog_type': 'ask_smapi_model.v1.skill.manifest.catalog_name.CatalogName'
    }  # type: Dict

    attribute_map = {
        'intent_name': 'intentName',
        'catalog_type': 'catalogType'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, intent_name=None, catalog_type=None):
        # type: (Optional[AndroidCommonIntentName_101c89f6], Optional[CatalogName_f3573200]) -> None
        """Android common intents associated with the skill

        :param intent_name: 
        :type intent_name: (optional) ask_smapi_model.v1.skill.manifest.android_common_intent_name.AndroidCommonIntentName
        :param catalog_type: 
        :type catalog_type: (optional) ask_smapi_model.v1.skill.manifest.catalog_name.CatalogName
        """
        self.__discriminator_value = None  # type: str

        self.intent_name = intent_name
        self.catalog_type = catalog_type

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
        if not isinstance(other, LinkedAndroidCommonIntent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
