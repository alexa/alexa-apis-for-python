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
    from ask_smapi_model.v1.skill.certification.review_tracking_info_summary import ReviewTrackingInfoSummary as Certification_ReviewTrackingInfoSummaryV1
    from ask_smapi_model.v1.skill.certification.certification_status import CertificationStatus as Certification_CertificationStatusV1


class CertificationSummary(object):
    """
    Summary of the certification resource. This is a leaner view of the certification resource for the collections API.


    :param id: Certification Id for the skill.
    :type id: (optional) str
    :param status: 
    :type status: (optional) ask_smapi_model.v1.skill.certification.certification_status.CertificationStatus
    :param skill_submission_timestamp: Timestamp for when the skill was submitted for certification.
    :type skill_submission_timestamp: (optional) datetime
    :param review_tracking_info: 
    :type review_tracking_info: (optional) ask_smapi_model.v1.skill.certification.review_tracking_info_summary.ReviewTrackingInfoSummary

    """
    deserialized_types = {
        'id': 'str',
        'status': 'ask_smapi_model.v1.skill.certification.certification_status.CertificationStatus',
        'skill_submission_timestamp': 'datetime',
        'review_tracking_info': 'ask_smapi_model.v1.skill.certification.review_tracking_info_summary.ReviewTrackingInfoSummary'
    }  # type: Dict

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'skill_submission_timestamp': 'skillSubmissionTimestamp',
        'review_tracking_info': 'reviewTrackingInfo'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, id=None, status=None, skill_submission_timestamp=None, review_tracking_info=None):
        # type: (Optional[str], Optional[Certification_CertificationStatusV1], Optional[datetime], Optional[Certification_ReviewTrackingInfoSummaryV1]) -> None
        """Summary of the certification resource. This is a leaner view of the certification resource for the collections API.

        :param id: Certification Id for the skill.
        :type id: (optional) str
        :param status: 
        :type status: (optional) ask_smapi_model.v1.skill.certification.certification_status.CertificationStatus
        :param skill_submission_timestamp: Timestamp for when the skill was submitted for certification.
        :type skill_submission_timestamp: (optional) datetime
        :param review_tracking_info: 
        :type review_tracking_info: (optional) ask_smapi_model.v1.skill.certification.review_tracking_info_summary.ReviewTrackingInfoSummary
        """
        self.__discriminator_value = None  # type: str

        self.id = id
        self.status = status
        self.skill_submission_timestamp = skill_submission_timestamp
        self.review_tracking_info = review_tracking_info

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
        if not isinstance(other, CertificationSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
