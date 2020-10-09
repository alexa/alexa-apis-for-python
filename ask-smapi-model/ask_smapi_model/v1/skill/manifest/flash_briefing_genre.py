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


class FlashBriefingGenre(Enum):
    """
    Type or subject of the content in the feed.



    Allowed enum values: [HEADLINE_NEWS, BUSINESS, POLITICS, ENTERTAINMENT, TECHNOLOGY, HUMOR, LIFESTYLE, SPORTS, SCIENCE, HEALTH_AND_FITNESS, ARTS_AND_CULTURE, PRODUCTIVITY_AND_UTILITIES, OTHER]
    """
    HEADLINE_NEWS = "HEADLINE_NEWS"
    BUSINESS = "BUSINESS"
    POLITICS = "POLITICS"
    ENTERTAINMENT = "ENTERTAINMENT"
    TECHNOLOGY = "TECHNOLOGY"
    HUMOR = "HUMOR"
    LIFESTYLE = "LIFESTYLE"
    SPORTS = "SPORTS"
    SCIENCE = "SCIENCE"
    HEALTH_AND_FITNESS = "HEALTH_AND_FITNESS"
    ARTS_AND_CULTURE = "ARTS_AND_CULTURE"
    PRODUCTIVITY_AND_UTILITIES = "PRODUCTIVITY_AND_UTILITIES"
    OTHER = "OTHER"

    def to_dict(self):
        # type: () -> Dict[str, Any]
        """Returns the model properties as a dict"""
        result = {self.name: self.value}
        return result

    def to_str(self):
        # type: () -> str
        """Returns the string representation of the model"""
        return pprint.pformat(self.value)

    def __repr__(self):
        # type: () -> str
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        # type: (Any) -> bool
        """Returns true if both objects are equal"""
        if not isinstance(other, FlashBriefingGenre):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (Any) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
