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
    from ask_smapi_model.v1.smart_home_evaluation.evaluate_sh_capability_request import EvaluateSHCapabilityRequest as EvaluateSHCapabilityRequest_2d391178
    from ask_smapi_model.v1.smart_home_evaluation.evaluation_entity_status import EvaluationEntityStatus as EvaluationEntityStatus_996e143
    from ask_smapi_model.v1.smart_home_evaluation.sh_evaluation_results_metric import SHEvaluationResultsMetric as SHEvaluationResultsMetric_64305eca
    from ask_smapi_model.v1.smart_home_evaluation.sh_capability_error import SHCapabilityError as SHCapabilityError_806131e7


class GetSHCapabilityEvaluationResponse(object):
    """

    :param end_timestamp: 
    :type end_timestamp: (optional) datetime
    :param start_timestamp: 
    :type start_timestamp: (optional) datetime
    :param status: 
    :type status: (optional) ask_smapi_model.v1.smart_home_evaluation.evaluation_entity_status.EvaluationEntityStatus
    :param error: 
    :type error: (optional) ask_smapi_model.v1.smart_home_evaluation.sh_capability_error.SHCapabilityError
    :param input: 
    :type input: (optional) ask_smapi_model.v1.smart_home_evaluation.evaluate_sh_capability_request.EvaluateSHCapabilityRequest
    :param metrics: 
    :type metrics: (optional) dict(str, ask_smapi_model.v1.smart_home_evaluation.sh_evaluation_results_metric.SHEvaluationResultsMetric)

    """
    deserialized_types = {
        'end_timestamp': 'datetime',
        'start_timestamp': 'datetime',
        'status': 'ask_smapi_model.v1.smart_home_evaluation.evaluation_entity_status.EvaluationEntityStatus',
        'error': 'ask_smapi_model.v1.smart_home_evaluation.sh_capability_error.SHCapabilityError',
        'input': 'ask_smapi_model.v1.smart_home_evaluation.evaluate_sh_capability_request.EvaluateSHCapabilityRequest',
        'metrics': 'dict(str, ask_smapi_model.v1.smart_home_evaluation.sh_evaluation_results_metric.SHEvaluationResultsMetric)'
    }  # type: Dict

    attribute_map = {
        'end_timestamp': 'endTimestamp',
        'start_timestamp': 'startTimestamp',
        'status': 'status',
        'error': 'error',
        'input': 'input',
        'metrics': 'metrics'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, end_timestamp=None, start_timestamp=None, status=None, error=None, input=None, metrics=None):
        # type: (Optional[datetime], Optional[datetime], Optional[EvaluationEntityStatus_996e143], Optional[SHCapabilityError_806131e7], Optional[EvaluateSHCapabilityRequest_2d391178], Optional[Dict[str, SHEvaluationResultsMetric_64305eca]]) -> None
        """

        :param end_timestamp: 
        :type end_timestamp: (optional) datetime
        :param start_timestamp: 
        :type start_timestamp: (optional) datetime
        :param status: 
        :type status: (optional) ask_smapi_model.v1.smart_home_evaluation.evaluation_entity_status.EvaluationEntityStatus
        :param error: 
        :type error: (optional) ask_smapi_model.v1.smart_home_evaluation.sh_capability_error.SHCapabilityError
        :param input: 
        :type input: (optional) ask_smapi_model.v1.smart_home_evaluation.evaluate_sh_capability_request.EvaluateSHCapabilityRequest
        :param metrics: 
        :type metrics: (optional) dict(str, ask_smapi_model.v1.smart_home_evaluation.sh_evaluation_results_metric.SHEvaluationResultsMetric)
        """
        self.__discriminator_value = None  # type: str

        self.end_timestamp = end_timestamp
        self.start_timestamp = start_timestamp
        self.status = status
        self.error = error
        self.input = input
        self.metrics = metrics

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
        if not isinstance(other, GetSHCapabilityEvaluationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
