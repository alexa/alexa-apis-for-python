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
    from ask_smapi_model.v1.smart_home_evaluation.sh_capability_directive import SHCapabilityDirective as SHCapabilityDirective_72bbfeb5
    from ask_smapi_model.v1.smart_home_evaluation.test_case_result_status import TestCaseResultStatus as TestCaseResultStatus_5c4be03e
    from ask_smapi_model.v1.smart_home_evaluation.sh_capability_error import SHCapabilityError as SHCapabilityError_806131e7
    from ask_smapi_model.v1.smart_home_evaluation.sh_capability_response import SHCapabilityResponse as SHCapabilityResponse_5c94224d
    from ask_smapi_model.v1.smart_home_evaluation.sh_capability_state import SHCapabilityState as SHCapabilityState_db42e6b9


class TestCaseResult(object):
    """

    :param actual_capability_states: 
    :type actual_capability_states: (optional) list[ask_smapi_model.v1.smart_home_evaluation.sh_capability_state.SHCapabilityState]
    :param actual_response: 
    :type actual_response: (optional) ask_smapi_model.v1.smart_home_evaluation.sh_capability_response.SHCapabilityResponse
    :param directive: 
    :type directive: (optional) ask_smapi_model.v1.smart_home_evaluation.sh_capability_directive.SHCapabilityDirective
    :param error: 
    :type error: (optional) ask_smapi_model.v1.smart_home_evaluation.sh_capability_error.SHCapabilityError
    :param expected_capability_states: 
    :type expected_capability_states: (optional) list[ask_smapi_model.v1.smart_home_evaluation.sh_capability_state.SHCapabilityState]
    :param expected_response: 
    :type expected_response: (optional) ask_smapi_model.v1.smart_home_evaluation.sh_capability_response.SHCapabilityResponse
    :param name: 
    :type name: (optional) str
    :param status: 
    :type status: (optional) ask_smapi_model.v1.smart_home_evaluation.test_case_result_status.TestCaseResultStatus

    """
    deserialized_types = {
        'actual_capability_states': 'list[ask_smapi_model.v1.smart_home_evaluation.sh_capability_state.SHCapabilityState]',
        'actual_response': 'ask_smapi_model.v1.smart_home_evaluation.sh_capability_response.SHCapabilityResponse',
        'directive': 'ask_smapi_model.v1.smart_home_evaluation.sh_capability_directive.SHCapabilityDirective',
        'error': 'ask_smapi_model.v1.smart_home_evaluation.sh_capability_error.SHCapabilityError',
        'expected_capability_states': 'list[ask_smapi_model.v1.smart_home_evaluation.sh_capability_state.SHCapabilityState]',
        'expected_response': 'ask_smapi_model.v1.smart_home_evaluation.sh_capability_response.SHCapabilityResponse',
        'name': 'str',
        'status': 'ask_smapi_model.v1.smart_home_evaluation.test_case_result_status.TestCaseResultStatus'
    }  # type: Dict

    attribute_map = {
        'actual_capability_states': 'actualCapabilityStates',
        'actual_response': 'actualResponse',
        'directive': 'directive',
        'error': 'error',
        'expected_capability_states': 'expectedCapabilityStates',
        'expected_response': 'expectedResponse',
        'name': 'name',
        'status': 'status'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, actual_capability_states=None, actual_response=None, directive=None, error=None, expected_capability_states=None, expected_response=None, name=None, status=None):
        # type: (Optional[List[SHCapabilityState_db42e6b9]], Optional[SHCapabilityResponse_5c94224d], Optional[SHCapabilityDirective_72bbfeb5], Optional[SHCapabilityError_806131e7], Optional[List[SHCapabilityState_db42e6b9]], Optional[SHCapabilityResponse_5c94224d], Optional[str], Optional[TestCaseResultStatus_5c4be03e]) -> None
        """

        :param actual_capability_states: 
        :type actual_capability_states: (optional) list[ask_smapi_model.v1.smart_home_evaluation.sh_capability_state.SHCapabilityState]
        :param actual_response: 
        :type actual_response: (optional) ask_smapi_model.v1.smart_home_evaluation.sh_capability_response.SHCapabilityResponse
        :param directive: 
        :type directive: (optional) ask_smapi_model.v1.smart_home_evaluation.sh_capability_directive.SHCapabilityDirective
        :param error: 
        :type error: (optional) ask_smapi_model.v1.smart_home_evaluation.sh_capability_error.SHCapabilityError
        :param expected_capability_states: 
        :type expected_capability_states: (optional) list[ask_smapi_model.v1.smart_home_evaluation.sh_capability_state.SHCapabilityState]
        :param expected_response: 
        :type expected_response: (optional) ask_smapi_model.v1.smart_home_evaluation.sh_capability_response.SHCapabilityResponse
        :param name: 
        :type name: (optional) str
        :param status: 
        :type status: (optional) ask_smapi_model.v1.smart_home_evaluation.test_case_result_status.TestCaseResultStatus
        """
        self.__discriminator_value = None  # type: str

        self.actual_capability_states = actual_capability_states
        self.actual_response = actual_response
        self.directive = directive
        self.error = error
        self.expected_capability_states = expected_capability_states
        self.expected_response = expected_response
        self.name = name
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
        if not isinstance(other, TestCaseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
