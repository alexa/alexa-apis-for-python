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
from ask_smapi_model.v1.skill.asr.evaluations.evaluation_metadata import EvaluationMetadata


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional, Union, Any
    from datetime import datetime
    from ask_smapi_model.v1.skill.asr.evaluations.error_object import ErrorObject as Evaluations_ErrorObjectV1
    from ask_smapi_model.v1.skill.asr.evaluations.evaluation_metadata_result import EvaluationMetadataResult as Evaluations_EvaluationMetadataResultV1
    from ask_smapi_model.v1.skill.asr.evaluations.evaluation_status import EvaluationStatus as Evaluations_EvaluationStatusV1
    from ask_smapi_model.v1.skill.asr.evaluations.post_asr_evaluations_request_object import PostAsrEvaluationsRequestObject as Evaluations_PostAsrEvaluationsRequestObjectV1


class EvaluationItems(EvaluationMetadata):
    """

    :param status: 
    :type status: (optional) ask_smapi_model.v1.skill.asr.evaluations.evaluation_status.EvaluationStatus
    :param total_evaluation_count: indicate the total number of evaluations that are supposed to be run in the evaluation request
    :type total_evaluation_count: (optional) float
    :param completed_evaluation_count: indicate the number of completed evaluations
    :type completed_evaluation_count: (optional) float
    :param start_timestamp: indicate the start time stamp of the ASR evaluation job. ISO-8601 Format.
    :type start_timestamp: (optional) datetime
    :param request: 
    :type request: (optional) ask_smapi_model.v1.skill.asr.evaluations.post_asr_evaluations_request_object.PostAsrEvaluationsRequestObject
    :param error: 
    :type error: (optional) ask_smapi_model.v1.skill.asr.evaluations.error_object.ErrorObject
    :param result: 
    :type result: (optional) ask_smapi_model.v1.skill.asr.evaluations.evaluation_metadata_result.EvaluationMetadataResult
    :param id: evaluation id
    :type id: (optional) str

    """
    deserialized_types = {
        'status': 'ask_smapi_model.v1.skill.asr.evaluations.evaluation_status.EvaluationStatus',
        'total_evaluation_count': 'float',
        'completed_evaluation_count': 'float',
        'start_timestamp': 'datetime',
        'request': 'ask_smapi_model.v1.skill.asr.evaluations.post_asr_evaluations_request_object.PostAsrEvaluationsRequestObject',
        'error': 'ask_smapi_model.v1.skill.asr.evaluations.error_object.ErrorObject',
        'result': 'ask_smapi_model.v1.skill.asr.evaluations.evaluation_metadata_result.EvaluationMetadataResult',
        'id': 'str'
    }  # type: Dict

    attribute_map = {
        'status': 'status',
        'total_evaluation_count': 'totalEvaluationCount',
        'completed_evaluation_count': 'completedEvaluationCount',
        'start_timestamp': 'startTimestamp',
        'request': 'request',
        'error': 'error',
        'result': 'result',
        'id': 'id'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, status=None, total_evaluation_count=None, completed_evaluation_count=None, start_timestamp=None, request=None, error=None, result=None, id=None):
        # type: (Optional[Evaluations_EvaluationStatusV1], Optional[float], Optional[float], Optional[datetime], Optional[Evaluations_PostAsrEvaluationsRequestObjectV1], Optional[Evaluations_ErrorObjectV1], Optional[Evaluations_EvaluationMetadataResultV1], Optional[str]) -> None
        """

        :param status: 
        :type status: (optional) ask_smapi_model.v1.skill.asr.evaluations.evaluation_status.EvaluationStatus
        :param total_evaluation_count: indicate the total number of evaluations that are supposed to be run in the evaluation request
        :type total_evaluation_count: (optional) float
        :param completed_evaluation_count: indicate the number of completed evaluations
        :type completed_evaluation_count: (optional) float
        :param start_timestamp: indicate the start time stamp of the ASR evaluation job. ISO-8601 Format.
        :type start_timestamp: (optional) datetime
        :param request: 
        :type request: (optional) ask_smapi_model.v1.skill.asr.evaluations.post_asr_evaluations_request_object.PostAsrEvaluationsRequestObject
        :param error: 
        :type error: (optional) ask_smapi_model.v1.skill.asr.evaluations.error_object.ErrorObject
        :param result: 
        :type result: (optional) ask_smapi_model.v1.skill.asr.evaluations.evaluation_metadata_result.EvaluationMetadataResult
        :param id: evaluation id
        :type id: (optional) str
        """
        self.__discriminator_value = None  # type: str

        super(EvaluationItems, self).__init__(status=status, total_evaluation_count=total_evaluation_count, completed_evaluation_count=completed_evaluation_count, start_timestamp=start_timestamp, request=request, error=error, result=result)
        self.id = id

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
        if not isinstance(other, EvaluationItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
