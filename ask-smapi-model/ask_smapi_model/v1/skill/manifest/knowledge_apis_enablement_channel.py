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


class KnowledgeApisEnablementChannel(Enum):
    """
    Defines how the skill can be enabled by developers. values can be set to &#39;PUBLIC&#39; (in Alexa Skill Store), &#39;ASP&#39; (A4R/A4H vendor devices), or &#39;A4B&#39; Public and ASP selections must have \&quot;distributionMode\&quot; &#x3D; &#39;PUBLIC&#39; and will only be eligible for distribution on personal or vendor (A4H/A4R or A4B) devices.



    Allowed enum values: [PUBLIC, ASP, A4B]
    """
    PUBLIC = "PUBLIC"
    ASP = "ASP"
    A4B = "A4B"

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
        if not isinstance(other, KnowledgeApisEnablementChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (Any) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
