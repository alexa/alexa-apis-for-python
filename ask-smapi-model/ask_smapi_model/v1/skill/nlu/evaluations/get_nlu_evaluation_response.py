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
from ask_smapi_model.v1.skill.nlu.evaluations.evaluation_entity import EvaluationEntity


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional, Union, Any
    from datetime import datetime
    from ask_smapi_model.v1.skill.nlu.evaluations.evaluation_inputs import EvaluationInputs as Evaluations_EvaluationInputsV1
    from ask_smapi_model.v1.skill.nlu.evaluations.status import Status as Evaluations_StatusV1
    from ask_smapi_model.v1.skill.nlu.evaluations.get_nlu_evaluation_response_links import GetNLUEvaluationResponseLinks as Evaluations_GetNLUEvaluationResponseLinksV1


class GetNLUEvaluationResponse(EvaluationEntity):
    """

    :param start_timestamp: 
    :type start_timestamp: (optional) datetime
    :param end_timestamp: 
    :type end_timestamp: (optional) datetime
    :param status: 
    :type status: (optional) ask_smapi_model.v1.skill.nlu.evaluations.status.Status
    :param error_message: Error message when evaluation job fails
    :type error_message: (optional) str
    :param inputs: 
    :type inputs: (optional) ask_smapi_model.v1.skill.nlu.evaluations.evaluation_inputs.EvaluationInputs
    :param links: 
    :type links: (optional) ask_smapi_model.v1.skill.nlu.evaluations.get_nlu_evaluation_response_links.GetNLUEvaluationResponseLinks

    """
    deserialized_types = {
        'start_timestamp': 'datetime',
        'end_timestamp': 'datetime',
        'status': 'ask_smapi_model.v1.skill.nlu.evaluations.status.Status',
        'error_message': 'str',
        'inputs': 'ask_smapi_model.v1.skill.nlu.evaluations.evaluation_inputs.EvaluationInputs',
        'links': 'ask_smapi_model.v1.skill.nlu.evaluations.get_nlu_evaluation_response_links.GetNLUEvaluationResponseLinks'
    }  # type: Dict

    attribute_map = {
        'start_timestamp': 'startTimestamp',
        'end_timestamp': 'endTimestamp',
        'status': 'status',
        'error_message': 'errorMessage',
        'inputs': 'inputs',
        'links': '_links'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, start_timestamp=None, end_timestamp=None, status=None, error_message=None, inputs=None, links=None):
        # type: (Optional[datetime], Optional[datetime], Optional[Evaluations_StatusV1], Optional[str], Optional[Evaluations_EvaluationInputsV1], Optional[Evaluations_GetNLUEvaluationResponseLinksV1]) -> None
        """

        :param start_timestamp: 
        :type start_timestamp: (optional) datetime
        :param end_timestamp: 
        :type end_timestamp: (optional) datetime
        :param status: 
        :type status: (optional) ask_smapi_model.v1.skill.nlu.evaluations.status.Status
        :param error_message: Error message when evaluation job fails
        :type error_message: (optional) str
        :param inputs: 
        :type inputs: (optional) ask_smapi_model.v1.skill.nlu.evaluations.evaluation_inputs.EvaluationInputs
        :param links: 
        :type links: (optional) ask_smapi_model.v1.skill.nlu.evaluations.get_nlu_evaluation_response_links.GetNLUEvaluationResponseLinks
        """
        self.__discriminator_value = None  # type: str

        super(GetNLUEvaluationResponse, self).__init__(start_timestamp=start_timestamp, end_timestamp=end_timestamp, status=status, error_message=error_message, inputs=inputs)
        self.links = links

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
        if not isinstance(other, GetNLUEvaluationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
