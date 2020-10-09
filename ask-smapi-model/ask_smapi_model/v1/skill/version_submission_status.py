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


class VersionSubmissionStatus(Enum):
    """
    The lifecycle status of the skill version submission. * &#x60;LIVE&#x60; - The skill version is in the live stage * &#x60;CERTIFIED&#x60; - The skill version has gone through the certification review process and has been certified. * &#x60;IN_REVIEW&#x60; - The skill version is currently under review for certification and publication. During this time, you cannot edit the configuration. * &#x60;FAILED_CERTIFICATION&#x60; - The skill version has been submitted for certification, however it has failed certification review. Please submit a new version for certification. * &#x60;HIDDEN&#x60; - The skill version has been published but is no longer available to new users for activation. Existing users can still invoke this skill if it is the most recent version. * &#x60;REMOVED&#x60; - The skill version has been published but removed for use, due to Amazon&#39;s policy violation. You can update your skill and publish a new version to live to address the policy violation. * &#x60;WITHDRAWN_FROM_CERTIFICATION&#x60; - The skill version was submitted for certification but was withdrawn from review. 



    Allowed enum values: [LIVE, CERTIFIED, IN_REVIEW, FAILED_CERTIFICATION, HIDDEN, REMOVED, WITHDRAWN_FROM_CERTIFICATION]
    """
    LIVE = "LIVE"
    CERTIFIED = "CERTIFIED"
    IN_REVIEW = "IN_REVIEW"
    FAILED_CERTIFICATION = "FAILED_CERTIFICATION"
    HIDDEN = "HIDDEN"
    REMOVED = "REMOVED"
    WITHDRAWN_FROM_CERTIFICATION = "WITHDRAWN_FROM_CERTIFICATION"

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
        if not isinstance(other, VersionSubmissionStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (Any) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
