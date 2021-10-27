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
    from ask_smapi_model.v1.skill.manifest.linked_android_common_intent import LinkedAndroidCommonIntent as LinkedAndroidCommonIntent_f1721a22
    from ask_smapi_model.v1.skill.manifest.linked_common_schemes import LinkedCommonSchemes as LinkedCommonSchemes_14e98c23
    from ask_smapi_model.v1.skill.manifest.linked_application import LinkedApplication as LinkedApplication_85efe66c


class AppLink(object):
    """
    Details required for app linking use cases.


    :param linked_applications: Allows developers to declare their Skill will use Alexa App Links, and list relevant apps. This field is required when using the APP_LINK interface.
    :type linked_applications: (optional) list[ask_smapi_model.v1.skill.manifest.linked_application.LinkedApplication]
    :param linked_web_domains: Allow developer to decalre their skill to link to the declared web domains.
    :type linked_web_domains: (optional) list[str]
    :param linked_android_common_intents: Allow developer to declare their skill to link to the speicified android common intents.
    :type linked_android_common_intents: (optional) list[ask_smapi_model.v1.skill.manifest.linked_android_common_intent.LinkedAndroidCommonIntent]
    :param linked_common_schemes: 
    :type linked_common_schemes: (optional) ask_smapi_model.v1.skill.manifest.linked_common_schemes.LinkedCommonSchemes

    """
    deserialized_types = {
        'linked_applications': 'list[ask_smapi_model.v1.skill.manifest.linked_application.LinkedApplication]',
        'linked_web_domains': 'list[str]',
        'linked_android_common_intents': 'list[ask_smapi_model.v1.skill.manifest.linked_android_common_intent.LinkedAndroidCommonIntent]',
        'linked_common_schemes': 'ask_smapi_model.v1.skill.manifest.linked_common_schemes.LinkedCommonSchemes'
    }  # type: Dict

    attribute_map = {
        'linked_applications': 'linkedApplications',
        'linked_web_domains': 'linkedWebDomains',
        'linked_android_common_intents': 'linkedAndroidCommonIntents',
        'linked_common_schemes': 'linkedCommonSchemes'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, linked_applications=None, linked_web_domains=None, linked_android_common_intents=None, linked_common_schemes=None):
        # type: (Optional[List[LinkedApplication_85efe66c]], Optional[List[object]], Optional[List[LinkedAndroidCommonIntent_f1721a22]], Optional[LinkedCommonSchemes_14e98c23]) -> None
        """Details required for app linking use cases.

        :param linked_applications: Allows developers to declare their Skill will use Alexa App Links, and list relevant apps. This field is required when using the APP_LINK interface.
        :type linked_applications: (optional) list[ask_smapi_model.v1.skill.manifest.linked_application.LinkedApplication]
        :param linked_web_domains: Allow developer to decalre their skill to link to the declared web domains.
        :type linked_web_domains: (optional) list[str]
        :param linked_android_common_intents: Allow developer to declare their skill to link to the speicified android common intents.
        :type linked_android_common_intents: (optional) list[ask_smapi_model.v1.skill.manifest.linked_android_common_intent.LinkedAndroidCommonIntent]
        :param linked_common_schemes: 
        :type linked_common_schemes: (optional) ask_smapi_model.v1.skill.manifest.linked_common_schemes.LinkedCommonSchemes
        """
        self.__discriminator_value = None  # type: str

        self.linked_applications = linked_applications
        self.linked_web_domains = linked_web_domains
        self.linked_android_common_intents = linked_android_common_intents
        self.linked_common_schemes = linked_common_schemes

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
        if not isinstance(other, AppLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
