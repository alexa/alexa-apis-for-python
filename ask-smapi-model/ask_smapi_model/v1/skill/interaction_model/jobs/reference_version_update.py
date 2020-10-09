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
from ask_smapi_model.v1.skill.interaction_model.jobs.job_definition import JobDefinition


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional, Union, Any
    from datetime import datetime
    from ask_smapi_model.v1.skill.interaction_model.jobs.resource_object import ResourceObject as Jobs_ResourceObjectV1
    from ask_smapi_model.v1.skill.interaction_model.jobs.referenced_resource_jobs_complete import ReferencedResourceJobsComplete as Jobs_ReferencedResourceJobsCompleteV1


class ReferenceVersionUpdate(JobDefinition):
    """
    Definition for ReferenceVersionUpdate job.


    :param trigger: Can only have ReferencedResourceJobsComplete trigger.
    :type trigger: (optional) ask_smapi_model.v1.skill.interaction_model.jobs.referenced_resource_jobs_complete.ReferencedResourceJobsComplete
    :param status: Current status of the job definition.
    :type status: (optional) str
    :param resource: The resource that the job is act on. Only slot and interactionModel are allowed.
    :type resource: (optional) ask_smapi_model.v1.skill.interaction_model.jobs.resource_object.ResourceObject
    :param references: Referenced resources working with ReferencedResourceJobsComplete trigger.
    :type references: (optional) list[ask_smapi_model.v1.skill.interaction_model.jobs.resource_object.ResourceObject]
    :param publish_to_live: Whether publish development stage to live after the updates.
    :type publish_to_live: (optional) bool

    """
    deserialized_types = {
        'object_type': 'str',
        'trigger': 'ask_smapi_model.v1.skill.interaction_model.jobs.referenced_resource_jobs_complete.ReferencedResourceJobsComplete',
        'status': 'str',
        'resource': 'ask_smapi_model.v1.skill.interaction_model.jobs.resource_object.ResourceObject',
        'references': 'list[ask_smapi_model.v1.skill.interaction_model.jobs.resource_object.ResourceObject]',
        'publish_to_live': 'bool'
    }  # type: Dict

    attribute_map = {
        'object_type': 'type',
        'trigger': 'trigger',
        'status': 'status',
        'resource': 'resource',
        'references': 'references',
        'publish_to_live': 'publishToLive'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, trigger=None, status=None, resource=None, references=None, publish_to_live=None):
        # type: (Optional[Jobs_ReferencedResourceJobsCompleteV1], Optional[str], Optional[Jobs_ResourceObjectV1], Optional[List[Jobs_ResourceObjectV1]], Optional[bool]) -> None
        """Definition for ReferenceVersionUpdate job.

        :param trigger: Can only have ReferencedResourceJobsComplete trigger.
        :type trigger: (optional) ask_smapi_model.v1.skill.interaction_model.jobs.referenced_resource_jobs_complete.ReferencedResourceJobsComplete
        :param status: Current status of the job definition.
        :type status: (optional) str
        :param resource: The resource that the job is act on. Only slot and interactionModel are allowed.
        :type resource: (optional) ask_smapi_model.v1.skill.interaction_model.jobs.resource_object.ResourceObject
        :param references: Referenced resources working with ReferencedResourceJobsComplete trigger.
        :type references: (optional) list[ask_smapi_model.v1.skill.interaction_model.jobs.resource_object.ResourceObject]
        :param publish_to_live: Whether publish development stage to live after the updates.
        :type publish_to_live: (optional) bool
        """
        self.__discriminator_value = "ReferenceVersionUpdate"  # type: str

        self.object_type = self.__discriminator_value
        super(ReferenceVersionUpdate, self).__init__(object_type=self.__discriminator_value, trigger=trigger, status=status)
        self.trigger = trigger
        self.resource = resource
        self.references = references
        self.publish_to_live = publish_to_live

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
        if not isinstance(other, ReferenceVersionUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
