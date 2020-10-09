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
    from ask_smapi_model.v1.skill.validations.response_validation_importance import ResponseValidationImportance as Validations_ResponseValidationImportanceV1
    from ask_smapi_model.v1.skill.validations.response_validation_status import ResponseValidationStatus as Validations_ResponseValidationStatusV1


class ResponseValidation(object):
    """

    :param title: Short, human readable title of the validation performed. 
    :type title: (optional) str
    :param description: Human readable description of the validation performed. May include instructions to address validation failure. 
    :type description: (optional) str
    :param category: Dot-delimited category. 
    :type category: (optional) str
    :param locale: Locale of the validation. 
    :type locale: (optional) str
    :param importance: 
    :type importance: (optional) ask_smapi_model.v1.skill.validations.response_validation_importance.ResponseValidationImportance
    :param status: 
    :type status: (optional) ask_smapi_model.v1.skill.validations.response_validation_status.ResponseValidationStatus

    """
    deserialized_types = {
        'title': 'str',
        'description': 'str',
        'category': 'str',
        'locale': 'str',
        'importance': 'ask_smapi_model.v1.skill.validations.response_validation_importance.ResponseValidationImportance',
        'status': 'ask_smapi_model.v1.skill.validations.response_validation_status.ResponseValidationStatus'
    }  # type: Dict

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'category': 'category',
        'locale': 'locale',
        'importance': 'importance',
        'status': 'status'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, title=None, description=None, category=None, locale=None, importance=None, status=None):
        # type: (Optional[str], Optional[str], Optional[str], Optional[str], Optional[Validations_ResponseValidationImportanceV1], Optional[Validations_ResponseValidationStatusV1]) -> None
        """

        :param title: Short, human readable title of the validation performed. 
        :type title: (optional) str
        :param description: Human readable description of the validation performed. May include instructions to address validation failure. 
        :type description: (optional) str
        :param category: Dot-delimited category. 
        :type category: (optional) str
        :param locale: Locale of the validation. 
        :type locale: (optional) str
        :param importance: 
        :type importance: (optional) ask_smapi_model.v1.skill.validations.response_validation_importance.ResponseValidationImportance
        :param status: 
        :type status: (optional) ask_smapi_model.v1.skill.validations.response_validation_status.ResponseValidationStatus
        """
        self.__discriminator_value = None  # type: str

        self.title = title
        self.description = description
        self.category = category
        self.locale = locale
        self.importance = importance
        self.status = status

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
        if not isinstance(other, ResponseValidation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
