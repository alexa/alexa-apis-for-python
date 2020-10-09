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


class Event(Enum):
    """
    Represents an event that the subscriber is interested in. The event is of the format AlexaDevelopmentEvent.OPERATION. You can use wildcard event &#39;AlexaDevelopmentEvent.All&#39; for recieving all developer notifications listed below.   * &#39;AlexaDevelopmentEvent.ManifestUpdate&#39; - The event representing the status of the update request on the Manifest.   * &#39;AlexaDevelopmentEvent.SkillPublish&#39; -   The event representing the status of the skill publish process.   * &#39;AlexaDevelopmentEvent.SkillCertification&#39; -   The event represents if a skill has been certified or not.   * &#39;AlexaDevelopmentEvent.InteractionModelUpdate&#39; -   The event represents the status of an Interaction Model build for a particular locale.   * &#39;AlexaDevelopmentEvent.All&#39; - A wildcard event name that allows subscription to all the existing events. While using this, you must not specify any other event name. AlexaDevelopmentEvent.All avoids the need of specifying every development event name in order to receive all events pertaining to a vendor account. Similarly, it avoids the need of updating an existing subscription to be able to receive new events, whenever supproted by notification service. Test Subscriber API cannot use this wildcard. Please make sure that your code can gracefully handle new/previously unknown events, if you are using this wildcard. 



    Allowed enum values: [AlexaDevelopmentEvent_ManifestUpdate, AlexaDevelopmentEvent_SkillPublish, AlexaDevelopmentEvent_SkillCertification, AlexaDevelopmentEvent_InteractionModelUpdate, AlexaDevelopmentEvent_All]
    """
    AlexaDevelopmentEvent_ManifestUpdate = "AlexaDevelopmentEvent.ManifestUpdate"
    AlexaDevelopmentEvent_SkillPublish = "AlexaDevelopmentEvent.SkillPublish"
    AlexaDevelopmentEvent_SkillCertification = "AlexaDevelopmentEvent.SkillCertification"
    AlexaDevelopmentEvent_InteractionModelUpdate = "AlexaDevelopmentEvent.InteractionModelUpdate"
    AlexaDevelopmentEvent_All = "AlexaDevelopmentEvent.All"

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
        if not isinstance(other, Event):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (Any) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
