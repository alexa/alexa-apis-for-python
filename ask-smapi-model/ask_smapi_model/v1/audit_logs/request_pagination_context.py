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


class RequestPaginationContext(object):
    """
    This object includes nextToken and maxResults.


    :param next_token: When the response to this API call is truncated, the response includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that this API understands. Token has expiry of 1 hour.
    :type next_token: (optional) str
    :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve more or less than the default of 50 results, you can add this parameter to your request. maxResults can exceed the upper limit of 250 but we will not return more items than that. The response might contain fewer results than maxResults for purpose of keeping SLA or because there are not enough items, but it will never contain more.
    :type max_results: (optional) float

    """
    deserialized_types = {
        'next_token': 'str',
        'max_results': 'float'
    }  # type: Dict

    attribute_map = {
        'next_token': 'nextToken',
        'max_results': 'maxResults'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, next_token=None, max_results=None):
        # type: (Optional[str], Optional[float]) -> None
        """This object includes nextToken and maxResults.

        :param next_token: When the response to this API call is truncated, the response includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that this API understands. Token has expiry of 1 hour.
        :type next_token: (optional) str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve more or less than the default of 50 results, you can add this parameter to your request. maxResults can exceed the upper limit of 250 but we will not return more items than that. The response might contain fewer results than maxResults for purpose of keeping SLA or because there are not enough items, but it will never contain more.
        :type max_results: (optional) float
        """
        self.__discriminator_value = None  # type: str

        self.next_token = next_token
        self.max_results = max_results

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
        if not isinstance(other, RequestPaginationContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
