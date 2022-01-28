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


class SourceState(Enum):
    """
    These states are for recording the previous state from a transition action (Created, Pilot, Start, Stop) on the experiment. * &#x60;CREATED&#x60;: Result state for the &#39;Create&#39; action. Experiment has been created. * &#x60;ENABLED&#x60;: Result state for the &#39;Pilot&#39; action. Experiment configurations are deployed and customer overrides are activated. Actual experiment has not started yet. * &#x60;RUNNING&#x60;: Result state for the &#39;Start&#39; action. Experiment has started with the configured exposure. Skill customers selected within the exposure are contributing to the metric data. 



    Allowed enum values: [CREATED, ENABLED, RUNNING]
    """
    CREATED = "CREATED"
    ENABLED = "ENABLED"
    RUNNING = "RUNNING"

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
        if not isinstance(other, SourceState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (Any) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
