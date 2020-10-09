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
from ask_smapi_model.v1.skill.interaction_model.slot_validation import SlotValidation


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional, Union, Any
    from datetime import datetime


class IsNotInDuration(SlotValidation):
    """
    Validates that the given date or time (as a slot value) is not in a given interval. Unlike other range validations, duration based validations lets the developer define a dynamic range of date or time using ISO_8601 Duration Format. Based on the given &#39;start&#39; and &#39;end&#39; parameters an interval is created. The slot value given by the skill&#39;s user at runtime is then validated inside this interval. Both &#39;start&#39; and &#39;end&#39; parameters are in reference to the current date/time. Here the current date/time refers to the date/time when the skill&#39;s user made the request. 


    :param prompt: The prompt id that should be used if validation fails.
    :type prompt: (optional) str
    :param start: * &#x60;AMAZON.DATE&#x60;: ISO 8601 Duration using Y, M or D components or ISO 8601 Calendar Date in YYYY-MM-DD format. * &#x60;AMAZON.TIME&#x60;: ISO 8601 Duration using H or M component or ISO 8601 24-Hour Clock Time in hh:mm format. 
    :type start: (optional) str
    :param end: * &#x60;AMAZON.DATE&#x60;: ISO 8601 Duration using Y, M or D components or ISO 8601 Calendar Date in YYYY-MM-DD format. * &#x60;AMAZON.TIME&#x60;: ISO 8601 Duration using H or M component or ISO 8601 24-Hour Clock Time in hh:mm format. 
    :type end: (optional) str

    """
    deserialized_types = {
        'object_type': 'str',
        'prompt': 'str',
        'start': 'str',
        'end': 'str'
    }  # type: Dict

    attribute_map = {
        'object_type': 'type',
        'prompt': 'prompt',
        'start': 'start',
        'end': 'end'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, prompt=None, start=None, end=None):
        # type: (Optional[str], Optional[str], Optional[str]) -> None
        """Validates that the given date or time (as a slot value) is not in a given interval. Unlike other range validations, duration based validations lets the developer define a dynamic range of date or time using ISO_8601 Duration Format. Based on the given &#39;start&#39; and &#39;end&#39; parameters an interval is created. The slot value given by the skill&#39;s user at runtime is then validated inside this interval. Both &#39;start&#39; and &#39;end&#39; parameters are in reference to the current date/time. Here the current date/time refers to the date/time when the skill&#39;s user made the request. 

        :param prompt: The prompt id that should be used if validation fails.
        :type prompt: (optional) str
        :param start: * &#x60;AMAZON.DATE&#x60;: ISO 8601 Duration using Y, M or D components or ISO 8601 Calendar Date in YYYY-MM-DD format. * &#x60;AMAZON.TIME&#x60;: ISO 8601 Duration using H or M component or ISO 8601 24-Hour Clock Time in hh:mm format. 
        :type start: (optional) str
        :param end: * &#x60;AMAZON.DATE&#x60;: ISO 8601 Duration using Y, M or D components or ISO 8601 Calendar Date in YYYY-MM-DD format. * &#x60;AMAZON.TIME&#x60;: ISO 8601 Duration using H or M component or ISO 8601 24-Hour Clock Time in hh:mm format. 
        :type end: (optional) str
        """
        self.__discriminator_value = "isNotInDuration"  # type: str

        self.object_type = self.__discriminator_value
        super(IsNotInDuration, self).__init__(object_type=self.__discriminator_value, prompt=prompt)
        self.start = start
        self.end = end

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
        if not isinstance(other, IsNotInDuration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
