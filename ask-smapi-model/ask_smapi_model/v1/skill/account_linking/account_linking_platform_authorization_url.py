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
    from ask_smapi_model.v1.skill.account_linking.platform_type import PlatformType as AccountLinking_PlatformTypeV1


class AccountLinkingPlatformAuthorizationUrl(object):
    """
    A key-value pair object that contains the OAuth2 authorization url to initiate the skill account linking process.


    :param platform_type: 
    :type platform_type: (optional) ask_smapi_model.v1.skill.account_linking.platform_type.PlatformType
    :param platform_authorization_url: Defines the OAuth2 Authorization URL that will be used in this platform to authenticate the customer / person.
    :type platform_authorization_url: (optional) str

    """
    deserialized_types = {
        'platform_type': 'ask_smapi_model.v1.skill.account_linking.platform_type.PlatformType',
        'platform_authorization_url': 'str'
    }  # type: Dict

    attribute_map = {
        'platform_type': 'platformType',
        'platform_authorization_url': 'platformAuthorizationUrl'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, platform_type=None, platform_authorization_url=None):
        # type: (Optional[AccountLinking_PlatformTypeV1], Optional[str]) -> None
        """A key-value pair object that contains the OAuth2 authorization url to initiate the skill account linking process.

        :param platform_type: 
        :type platform_type: (optional) ask_smapi_model.v1.skill.account_linking.platform_type.PlatformType
        :param platform_authorization_url: Defines the OAuth2 Authorization URL that will be used in this platform to authenticate the customer / person.
        :type platform_authorization_url: (optional) str
        """
        self.__discriminator_value = None  # type: str

        self.platform_type = platform_type
        self.platform_authorization_url = platform_authorization_url

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
        if not isinstance(other, AccountLinkingPlatformAuthorizationUrl):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
