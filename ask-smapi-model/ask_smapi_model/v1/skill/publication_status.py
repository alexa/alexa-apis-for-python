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


class PublicationStatus(Enum):
    """
    Publication status of the skill. It is associated with the skill&#39;s stage. Skill in &#39;development&#39; stage can have publication status as &#39;DEVELOPMENT&#39; or &#39;CERTIFICATION&#39;. Skill in &#39;certified&#39; stage can have publication status as &#39;CERTIFIED&#39;. &#39;Skill in &#39;live&#39; stage can have publication status as &#39;PUBLISHED&#39;, &#39;HIDDEN&#39; or &#39;REMOVED&#39;. * &#x60;DEVELOPMENT&#x60; - The skill is available only to you. If you have enabled it for testing, you can test it on devices registered to your developer account. * &#x60;CERTIFICATION&#x60; - Amazon is currently reviewing the skill for publication. During this time, you cannot edit the configuration. * &#x60;CERTIFIED&#x60; - The skill has been certified and ready to be published. Skill can be either published immediately or an future release date can be set for the skill. You cannot edit the configuration for the certified skills. To start development, make your changes on the development version. * &#x60;PUBLISHED&#x60; - The skill has been published and is available to users. You cannot edit the configuration for live skills. To start development on an updated version, make your changes on the development version instead. * &#x60;HIDDEN&#x60; - The skill has been published but is no longer available to new users for activation. Existing users can still invoke this skill. * &#x60;REMOVED&#x60; - The skill has been published but removed for use, due to Amazon&#39;s policy violation. You can update your skill and publish a new version to live to address the policy violation. 



    Allowed enum values: [DEVELOPMENT, CERTIFICATION, CERTIFIED, PUBLISHED, HIDDEN, REMOVED]
    """
    DEVELOPMENT = "DEVELOPMENT"
    CERTIFICATION = "CERTIFICATION"
    CERTIFIED = "CERTIFIED"
    PUBLISHED = "PUBLISHED"
    HIDDEN = "HIDDEN"
    REMOVED = "REMOVED"

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
        if not isinstance(other, PublicationStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (Any) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
