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
    from typing import Dict, List, Optional, Union
    from datetime import datetime
    from ask_smapi_model.v1.links import Links
    from ask_smapi_model.v1.skill.certification.certification_summary import CertificationSummary


class ListCertificationsResponse(object):
    """
    List of certification summary for a skill.


    :param links: 
    :type links: (optional) ask_smapi_model.v1.links.Links
    :param is_truncated: boolean value for if the response is truncated. isTruncated &#x3D; true if more than the assigned maxResults parameter value certification items are available for the skill. The results are then paginated and the remaining results can be retrieved in a similar paginated manner by using &#39;next&#39; link in the _links or using the nextToken in a following request. 
    :type is_truncated: (optional) bool
    :param next_token: Encrypted token present when isTruncated is true.
    :type next_token: (optional) str
    :param total_count: Total number of certification results available for the skill.
    :type total_count: (optional) int
    :param items: List of certifications available for a skill. The list of certifications is sorted in a default descending sort order on id field. 
    :type items: (optional) list[ask_smapi_model.v1.skill.certification.certification_summary.CertificationSummary]

    """
    deserialized_types = {
        'links': 'ask_smapi_model.v1.links.Links',
        'is_truncated': 'bool',
        'next_token': 'str',
        'total_count': 'int',
        'items': 'list[ask_smapi_model.v1.skill.certification.certification_summary.CertificationSummary]'
    }  # type: Dict

    attribute_map = {
        'links': '_links',
        'is_truncated': 'isTruncated',
        'next_token': 'nextToken',
        'total_count': 'totalCount',
        'items': 'items'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, links=None, is_truncated=None, next_token=None, total_count=None, items=None):
        # type: (Optional[Links], Optional[bool], Optional[str], Optional[int], Optional[List[CertificationSummary]]) -> None
        """List of certification summary for a skill.

        :param links: 
        :type links: (optional) ask_smapi_model.v1.links.Links
        :param is_truncated: boolean value for if the response is truncated. isTruncated &#x3D; true if more than the assigned maxResults parameter value certification items are available for the skill. The results are then paginated and the remaining results can be retrieved in a similar paginated manner by using &#39;next&#39; link in the _links or using the nextToken in a following request. 
        :type is_truncated: (optional) bool
        :param next_token: Encrypted token present when isTruncated is true.
        :type next_token: (optional) str
        :param total_count: Total number of certification results available for the skill.
        :type total_count: (optional) int
        :param items: List of certifications available for a skill. The list of certifications is sorted in a default descending sort order on id field. 
        :type items: (optional) list[ask_smapi_model.v1.skill.certification.certification_summary.CertificationSummary]
        """
        self.__discriminator_value = None  # type: str

        self.links = links
        self.is_truncated = is_truncated
        self.next_token = next_token
        self.total_count = total_count
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
        if not isinstance(other, ListCertificationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
