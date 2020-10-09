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
from ask_smapi_model.v0.event_schema.base_schema import BaseSchema


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional, Union, Any
    from datetime import datetime
    from ask_smapi_model.v0.event_schema.skill_event_attributes import SkillEventAttributes as EventSchema_SkillEventAttributesV0


class ManifestUpdate(BaseSchema):
    """
    &#39;AlexaDevelopmentEvent.ManifestUpdate&#39; event represents the status of the update request on the Manifest. This event is generated when request to create a skill or update an existing skill is completed. The request may complete either with &#x60;SUCCEEDED&#x60; or &#x60;FAILED&#x60; status.


    :param timestamp: ISO 8601 timestamp for the instant when event was created. 
    :type timestamp: (optional) datetime
    :param request_id: A development notification includes a unique identifier that identifies the original request that resulted in the development notification. The requestId for original request is returned by Amazon APIs in response&#39;s &#39;X-Amzn-RequestId&#39; header. 
    :type request_id: (optional) str
    :param payload: 
    :type payload: (optional) ask_smapi_model.v0.event_schema.skill_event_attributes.SkillEventAttributes

    """
    deserialized_types = {
        'timestamp': 'datetime',
        'event_name': 'str',
        'request_id': 'str',
        'payload': 'ask_smapi_model.v0.event_schema.skill_event_attributes.SkillEventAttributes'
    }  # type: Dict

    attribute_map = {
        'timestamp': 'timestamp',
        'event_name': 'eventName',
        'request_id': 'requestId',
        'payload': 'payload'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, timestamp=None, request_id=None, payload=None):
        # type: (Optional[datetime], Optional[str], Optional[EventSchema_SkillEventAttributesV0]) -> None
        """&#39;AlexaDevelopmentEvent.ManifestUpdate&#39; event represents the status of the update request on the Manifest. This event is generated when request to create a skill or update an existing skill is completed. The request may complete either with &#x60;SUCCEEDED&#x60; or &#x60;FAILED&#x60; status.

        :param timestamp: ISO 8601 timestamp for the instant when event was created. 
        :type timestamp: (optional) datetime
        :param request_id: A development notification includes a unique identifier that identifies the original request that resulted in the development notification. The requestId for original request is returned by Amazon APIs in response&#39;s &#39;X-Amzn-RequestId&#39; header. 
        :type request_id: (optional) str
        :param payload: 
        :type payload: (optional) ask_smapi_model.v0.event_schema.skill_event_attributes.SkillEventAttributes
        """
        self.__discriminator_value = "AlexaDevelopmentEvent.ManifestUpdate"  # type: str

        self.event_name = self.__discriminator_value
        super(ManifestUpdate, self).__init__(timestamp=timestamp, event_name=self.__discriminator_value)
        self.request_id = request_id
        self.payload = payload

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
        if not isinstance(other, ManifestUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
