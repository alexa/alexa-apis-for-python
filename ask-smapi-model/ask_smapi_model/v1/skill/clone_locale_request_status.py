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


class CloneLocaleRequestStatus(Enum):
    """
    Status for a locale clone request CloneLocale API initiates cloning from a source locale to all target locales.   * &#x60;IN_PROGRESS&#x60; status would indicate the clone is still in progress.   * &#x60;SUCCEEDED&#x60; status would indicate the source locale was cloned successfully to all target locales.   * &#x60;INELIGIBLE&#x60; status would indicate the source locale was ineligible to be cloned to all target locales.   * &#x60;MIXED&#x60; status would indicate the different status of clone on different locales, and individual target locale statues should be checked.   * &#x60;FAILED&#x60; status would indicate the source locale was not cloned all target locales successfully despite the request being eligible due to internal service issues.   * &#x60;ROLLBACK_SUCCEEDED&#x60; status would indicate the skill was rolled back to the previous state in case any failure.   * &#x60;ROLLBACK_FAILED&#x60; status would indicate that in case of failure, the rollback to the previous state of the skill was attempted, but it failed. 



    Allowed enum values: [FAILED, INELIGIBLE, IN_PROGRESS, MIXED, ROLLBACK_FAILED, ROLLBACK_SUCCEEDED, SUCCEEDED]
    """
    FAILED = "FAILED"
    INELIGIBLE = "INELIGIBLE"
    IN_PROGRESS = "IN_PROGRESS"
    MIXED = "MIXED"
    ROLLBACK_FAILED = "ROLLBACK_FAILED"
    ROLLBACK_SUCCEEDED = "ROLLBACK_SUCCEEDED"
    SUCCEEDED = "SUCCEEDED"

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
        if not isinstance(other, CloneLocaleRequestStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (Any) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
