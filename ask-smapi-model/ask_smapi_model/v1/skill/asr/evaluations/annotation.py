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


class Annotation(object):
    """

    :param upload_id: upload id obtained when developer creates an upload using catalog API
    :type upload_id: (optional) str
    :param file_path_in_upload: file path in the uploaded zip file. For example, a zip containing a folder named &#39;a&#39; and there is an audio b.mp3 in that folder. The file path is a/b.mp3. Notice that forward slash (&#39;/&#39;) should be used to concatenate directories.
    :type file_path_in_upload: (optional) str
    :param evaluation_weight: weight of the test case in an evaluation, the value would be used for calculating metrics such as overall error rate.  The acceptable values are from 1 - 1000. 1 means least significant, 1000 means mot significant. Here is how weight  impact the &#x60;OVERALL_ERROR_RATE&#x60; calculation: For example, an annotation set consists of 3 annotations and they have weight of 8, 1, 1. The evaluation results  show that only the first annotation test case passed while the rest of the test cases failed. In this case,  the overall error rate is (8 / (8 + 1 + 1)) &#x3D; 0.8 
    :type evaluation_weight: (optional) float
    :param expected_transcription: expected transcription text for the input audio. The acceptable length of the string is between 1 and 500 Unicode characters
    :type expected_transcription: (optional) str

    """
    deserialized_types = {
        'upload_id': 'str',
        'file_path_in_upload': 'str',
        'evaluation_weight': 'float',
        'expected_transcription': 'str'
    }  # type: Dict

    attribute_map = {
        'upload_id': 'uploadId',
        'file_path_in_upload': 'filePathInUpload',
        'evaluation_weight': 'evaluationWeight',
        'expected_transcription': 'expectedTranscription'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, upload_id=None, file_path_in_upload=None, evaluation_weight=None, expected_transcription=None):
        # type: (Optional[str], Optional[str], Optional[float], Optional[str]) -> None
        """

        :param upload_id: upload id obtained when developer creates an upload using catalog API
        :type upload_id: (optional) str
        :param file_path_in_upload: file path in the uploaded zip file. For example, a zip containing a folder named &#39;a&#39; and there is an audio b.mp3 in that folder. The file path is a/b.mp3. Notice that forward slash (&#39;/&#39;) should be used to concatenate directories.
        :type file_path_in_upload: (optional) str
        :param evaluation_weight: weight of the test case in an evaluation, the value would be used for calculating metrics such as overall error rate.  The acceptable values are from 1 - 1000. 1 means least significant, 1000 means mot significant. Here is how weight  impact the &#x60;OVERALL_ERROR_RATE&#x60; calculation: For example, an annotation set consists of 3 annotations and they have weight of 8, 1, 1. The evaluation results  show that only the first annotation test case passed while the rest of the test cases failed. In this case,  the overall error rate is (8 / (8 + 1 + 1)) &#x3D; 0.8 
        :type evaluation_weight: (optional) float
        :param expected_transcription: expected transcription text for the input audio. The acceptable length of the string is between 1 and 500 Unicode characters
        :type expected_transcription: (optional) str
        """
        self.__discriminator_value = None  # type: str

        self.upload_id = upload_id
        self.file_path_in_upload = file_path_in_upload
        self.evaluation_weight = evaluation_weight
        self.expected_transcription = expected_transcription

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
        if not isinstance(other, Annotation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
