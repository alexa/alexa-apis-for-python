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
from ask_sdk_model.interfaces.alexa.datastore.commands_error import CommandsError


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional, Union, Any
    from datetime import datetime
    from ask_sdk_model.interfaces.alexa.datastore.execution_error_content import ExecutionErrorContent as ExecutionErrorContent_aa5000b0


class DataStoreInternalError(CommandsError):
    """
    Describes an execution error for unknown error from device DataStore.


    :param content: 
    :type content: (optional) ask_sdk_model.interfaces.alexa.datastore.execution_error_content.ExecutionErrorContent

    """
    deserialized_types = {
        'object_type': 'str',
        'content': 'ask_sdk_model.interfaces.alexa.datastore.execution_error_content.ExecutionErrorContent'
    }  # type: Dict

    attribute_map = {
        'object_type': 'type',
        'content': 'content'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, content=None):
        # type: (Optional[ExecutionErrorContent_aa5000b0]) -> None
        """Describes an execution error for unknown error from device DataStore.

        :param content: 
        :type content: (optional) ask_sdk_model.interfaces.alexa.datastore.execution_error_content.ExecutionErrorContent
        """
        self.__discriminator_value = "DATASTORE_INTERNAL_ERROR"  # type: str

        self.object_type = self.__discriminator_value
        super(DataStoreInternalError, self).__init__(object_type=self.__discriminator_value)
        self.content = content

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
        if not isinstance(other, DataStoreInternalError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
