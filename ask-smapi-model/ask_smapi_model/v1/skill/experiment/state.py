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


class State(Enum):
    """
    * &#x60;CREATED&#x60; - The experiment is successfully created but has not been enabled or started. * &#x60;ENABLING&#x60; - The experiment has initiated the transition to becoming \&quot;ENABLED\&quot;. * &#x60;ENABLED&#x60; - The experiment configurations have been deployed but only customer treatment overrides set to T1 can view the T1 experience of a skill. No metrics are collected. * &#x60;RUNNING&#x60; - The experiment has started and a percentage of skill customers defined in the exposurePercentage will be entered into the experiment. Customers will randomly get assigned the T1 or C experience. Metric collection will begin. * &#x60;STOPPING&#x60; - The experiment has initated the transition to becoming \&quot;STOPPED\&quot;. * &#x60;STOPPED&#x60; - The experiment has ended and all customers will experience the C behavior. Metrics will stop being collected. * &#x60;FAILED&#x60; - The experiment configurations have failed to deploy while enabling or starting the experiment. 



    Allowed enum values: [CREATED, ENABLING, ENABLED, RUNNING, STOPPING, STOPPED, FAILED]
    """
    CREATED = "CREATED"
    ENABLING = "ENABLING"
    ENABLED = "ENABLED"
    RUNNING = "RUNNING"
    STOPPING = "STOPPING"
    STOPPED = "STOPPED"
    FAILED = "FAILED"

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
        if not isinstance(other, State):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (Any) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
