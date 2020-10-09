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
    from ask_smapi_model.v1.links import Links as V1_LinksV1
    from ask_smapi_model.v1.skill.history.intent_request import IntentRequest as History_IntentRequestV1


class IntentRequests(object):
    """
    Response to the GET Intent Request History API. It contains the collection of utterances for the skill, nextToken and other metadata related to the search query.


    :param links: 
    :type links: (optional) ask_smapi_model.v1.links.Links
    :param next_token: This token can be used to load the next page of the result.
    :type next_token: (optional) str
    :param is_truncated: This property is true when all the results matching the search request haven&#39;t been returned, false otherwise.
    :type is_truncated: (optional) bool
    :param total_count: Total number of records that matched the given search query.
    :type total_count: (optional) float
    :param start_index: Position of the current page in the result set.
    :type start_index: (optional) float
    :param skill_id: The Skill Id.
    :type skill_id: (optional) str
    :param items: List of intent requests for the skill
    :type items: (optional) list[ask_smapi_model.v1.skill.history.intent_request.IntentRequest]

    """
    deserialized_types = {
        'links': 'ask_smapi_model.v1.links.Links',
        'next_token': 'str',
        'is_truncated': 'bool',
        'total_count': 'float',
        'start_index': 'float',
        'skill_id': 'str',
        'items': 'list[ask_smapi_model.v1.skill.history.intent_request.IntentRequest]'
    }  # type: Dict

    attribute_map = {
        'links': '_links',
        'next_token': 'nextToken',
        'is_truncated': 'isTruncated',
        'total_count': 'totalCount',
        'start_index': 'startIndex',
        'skill_id': 'skillId',
        'items': 'items'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, links=None, next_token=None, is_truncated=None, total_count=None, start_index=None, skill_id=None, items=None):
        # type: (Optional[V1_LinksV1], Optional[str], Optional[bool], Optional[float], Optional[float], Optional[str], Optional[List[History_IntentRequestV1]]) -> None
        """Response to the GET Intent Request History API. It contains the collection of utterances for the skill, nextToken and other metadata related to the search query.

        :param links: 
        :type links: (optional) ask_smapi_model.v1.links.Links
        :param next_token: This token can be used to load the next page of the result.
        :type next_token: (optional) str
        :param is_truncated: This property is true when all the results matching the search request haven&#39;t been returned, false otherwise.
        :type is_truncated: (optional) bool
        :param total_count: Total number of records that matched the given search query.
        :type total_count: (optional) float
        :param start_index: Position of the current page in the result set.
        :type start_index: (optional) float
        :param skill_id: The Skill Id.
        :type skill_id: (optional) str
        :param items: List of intent requests for the skill
        :type items: (optional) list[ask_smapi_model.v1.skill.history.intent_request.IntentRequest]
        """
        self.__discriminator_value = None  # type: str

        self.links = links
        self.next_token = next_token
        self.is_truncated = is_truncated
        self.total_count = total_count
        self.start_index = start_index
        self.skill_id = skill_id
        self.items = items

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
        if not isinstance(other, IntentRequests):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
