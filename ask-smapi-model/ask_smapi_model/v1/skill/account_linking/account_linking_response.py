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
    from ask_smapi_model.v1.skill.account_linking.account_linking_type import AccountLinkingType as AccountLinking_AccountLinkingTypeV1
    from ask_smapi_model.v1.skill.account_linking.account_linking_platform_authorization_url import AccountLinkingPlatformAuthorizationUrl as AccountLinking_AccountLinkingPlatformAuthorizationUrlV1
    from ask_smapi_model.v1.skill.account_linking.access_token_scheme_type import AccessTokenSchemeType as AccountLinking_AccessTokenSchemeTypeV1


class AccountLinkingResponse(object):
    """
    The account linking information of a skill.


    :param object_type: 
    :type object_type: (optional) ask_smapi_model.v1.skill.account_linking.account_linking_type.AccountLinkingType
    :param authorization_url: The url where customers will be redirected in the companion app to enter login credentials.
    :type authorization_url: (optional) str
    :param domains: The list of domains that the authorization URL will fetch content from.
    :type domains: (optional) list[str]
    :param client_id: The unique public string used to identify the client requesting for authentication.
    :type client_id: (optional) str
    :param scopes: The list of permissions which will be requested from the skill user.
    :type scopes: (optional) list[str]
    :param access_token_url: The url used for access token and token refresh requests.
    :type access_token_url: (optional) str
    :param access_token_scheme: 
    :type access_token_scheme: (optional) ask_smapi_model.v1.skill.account_linking.access_token_scheme_type.AccessTokenSchemeType
    :param default_token_expiration_in_seconds: The time in seconds for which access token is valid. If OAuth client returns \&quot;expires_in\&quot;, it will be overwrite this parameter. 
    :type default_token_expiration_in_seconds: (optional) int
    :param redirect_urls: The list of valid urls to redirect back to, when the linking process is initiated from a third party system.
    :type redirect_urls: (optional) list[str]
    :param authorization_urls_by_platform: The list of valid authorization urls for allowed platforms to initiate account linking.
    :type authorization_urls_by_platform: (optional) list[ask_smapi_model.v1.skill.account_linking.account_linking_platform_authorization_url.AccountLinkingPlatformAuthorizationUrl]

    """
    deserialized_types = {
        'object_type': 'ask_smapi_model.v1.skill.account_linking.account_linking_type.AccountLinkingType',
        'authorization_url': 'str',
        'domains': 'list[str]',
        'client_id': 'str',
        'scopes': 'list[str]',
        'access_token_url': 'str',
        'access_token_scheme': 'ask_smapi_model.v1.skill.account_linking.access_token_scheme_type.AccessTokenSchemeType',
        'default_token_expiration_in_seconds': 'int',
        'redirect_urls': 'list[str]',
        'authorization_urls_by_platform': 'list[ask_smapi_model.v1.skill.account_linking.account_linking_platform_authorization_url.AccountLinkingPlatformAuthorizationUrl]'
    }  # type: Dict

    attribute_map = {
        'object_type': 'type',
        'authorization_url': 'authorizationUrl',
        'domains': 'domains',
        'client_id': 'clientId',
        'scopes': 'scopes',
        'access_token_url': 'accessTokenUrl',
        'access_token_scheme': 'accessTokenScheme',
        'default_token_expiration_in_seconds': 'defaultTokenExpirationInSeconds',
        'redirect_urls': 'redirectUrls',
        'authorization_urls_by_platform': 'authorizationUrlsByPlatform'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, object_type=None, authorization_url=None, domains=None, client_id=None, scopes=None, access_token_url=None, access_token_scheme=None, default_token_expiration_in_seconds=None, redirect_urls=None, authorization_urls_by_platform=None):
        # type: (Optional[AccountLinking_AccountLinkingTypeV1], Optional[str], Optional[List[object]], Optional[str], Optional[List[object]], Optional[str], Optional[AccountLinking_AccessTokenSchemeTypeV1], Optional[int], Optional[List[object]], Optional[List[AccountLinking_AccountLinkingPlatformAuthorizationUrlV1]]) -> None
        """The account linking information of a skill.

        :param object_type: 
        :type object_type: (optional) ask_smapi_model.v1.skill.account_linking.account_linking_type.AccountLinkingType
        :param authorization_url: The url where customers will be redirected in the companion app to enter login credentials.
        :type authorization_url: (optional) str
        :param domains: The list of domains that the authorization URL will fetch content from.
        :type domains: (optional) list[str]
        :param client_id: The unique public string used to identify the client requesting for authentication.
        :type client_id: (optional) str
        :param scopes: The list of permissions which will be requested from the skill user.
        :type scopes: (optional) list[str]
        :param access_token_url: The url used for access token and token refresh requests.
        :type access_token_url: (optional) str
        :param access_token_scheme: 
        :type access_token_scheme: (optional) ask_smapi_model.v1.skill.account_linking.access_token_scheme_type.AccessTokenSchemeType
        :param default_token_expiration_in_seconds: The time in seconds for which access token is valid. If OAuth client returns \&quot;expires_in\&quot;, it will be overwrite this parameter. 
        :type default_token_expiration_in_seconds: (optional) int
        :param redirect_urls: The list of valid urls to redirect back to, when the linking process is initiated from a third party system.
        :type redirect_urls: (optional) list[str]
        :param authorization_urls_by_platform: The list of valid authorization urls for allowed platforms to initiate account linking.
        :type authorization_urls_by_platform: (optional) list[ask_smapi_model.v1.skill.account_linking.account_linking_platform_authorization_url.AccountLinkingPlatformAuthorizationUrl]
        """
        self.__discriminator_value = None  # type: str

        self.object_type = object_type
        self.authorization_url = authorization_url
        self.domains = domains
        self.client_id = client_id
        self.scopes = scopes
        self.access_token_url = access_token_url
        self.access_token_scheme = access_token_scheme
        self.default_token_expiration_in_seconds = default_token_expiration_in_seconds
        self.redirect_urls = redirect_urls
        self.authorization_urls_by_platform = authorization_urls_by_platform

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
        if not isinstance(other, AccountLinkingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
