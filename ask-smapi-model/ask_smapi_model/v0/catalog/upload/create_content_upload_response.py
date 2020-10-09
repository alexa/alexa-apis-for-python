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
from ask_smapi_model.v0.catalog.upload.content_upload_summary import ContentUploadSummary


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional, Union, Any
    from datetime import datetime
    from ask_smapi_model.v0.catalog.upload.upload_ingestion_step import UploadIngestionStep as Upload_UploadIngestionStepV0
    from ask_smapi_model.v0.catalog.upload.presigned_upload_part import PresignedUploadPart as Upload_PresignedUploadPartV0
    from ask_smapi_model.v0.catalog.upload.upload_status import UploadStatus as Upload_UploadStatusV0


class CreateContentUploadResponse(ContentUploadSummary):
    """
    Request body for self-hosted catalog uploads.


    :param id: Unique identifier of the upload.
    :type id: (optional) str
    :param catalog_id: Provides a unique identifier of the catalog.
    :type catalog_id: (optional) str
    :param status: 
    :type status: (optional) ask_smapi_model.v0.catalog.upload.upload_status.UploadStatus
    :param created_date: 
    :type created_date: (optional) datetime
    :param last_updated_date: 
    :type last_updated_date: (optional) datetime
    :param ingestion_steps: 
    :type ingestion_steps: (optional) list[ask_smapi_model.v0.catalog.upload.upload_ingestion_step.UploadIngestionStep]
    :param presigned_upload_parts: Ordered list of presigned upload parts to perform a partitioned (multipart) file upload.
    :type presigned_upload_parts: (optional) list[ask_smapi_model.v0.catalog.upload.presigned_upload_part.PresignedUploadPart]

    """
    deserialized_types = {
        'id': 'str',
        'catalog_id': 'str',
        'status': 'ask_smapi_model.v0.catalog.upload.upload_status.UploadStatus',
        'created_date': 'datetime',
        'last_updated_date': 'datetime',
        'ingestion_steps': 'list[ask_smapi_model.v0.catalog.upload.upload_ingestion_step.UploadIngestionStep]',
        'presigned_upload_parts': 'list[ask_smapi_model.v0.catalog.upload.presigned_upload_part.PresignedUploadPart]'
    }  # type: Dict

    attribute_map = {
        'id': 'id',
        'catalog_id': 'catalogId',
        'status': 'status',
        'created_date': 'createdDate',
        'last_updated_date': 'lastUpdatedDate',
        'ingestion_steps': 'ingestionSteps',
        'presigned_upload_parts': 'presignedUploadParts'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, id=None, catalog_id=None, status=None, created_date=None, last_updated_date=None, ingestion_steps=None, presigned_upload_parts=None):
        # type: (Optional[str], Optional[str], Optional[Upload_UploadStatusV0], Optional[datetime], Optional[datetime], Optional[List[Upload_UploadIngestionStepV0]], Optional[List[Upload_PresignedUploadPartV0]]) -> None
        """Request body for self-hosted catalog uploads.

        :param id: Unique identifier of the upload.
        :type id: (optional) str
        :param catalog_id: Provides a unique identifier of the catalog.
        :type catalog_id: (optional) str
        :param status: 
        :type status: (optional) ask_smapi_model.v0.catalog.upload.upload_status.UploadStatus
        :param created_date: 
        :type created_date: (optional) datetime
        :param last_updated_date: 
        :type last_updated_date: (optional) datetime
        :param ingestion_steps: 
        :type ingestion_steps: (optional) list[ask_smapi_model.v0.catalog.upload.upload_ingestion_step.UploadIngestionStep]
        :param presigned_upload_parts: Ordered list of presigned upload parts to perform a partitioned (multipart) file upload.
        :type presigned_upload_parts: (optional) list[ask_smapi_model.v0.catalog.upload.presigned_upload_part.PresignedUploadPart]
        """
        self.__discriminator_value = None  # type: str

        super(CreateContentUploadResponse, self).__init__(id=id, catalog_id=catalog_id, status=status, created_date=created_date, last_updated_date=last_updated_date)
        self.ingestion_steps = ingestion_steps
        self.presigned_upload_parts = presigned_upload_parts

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
        if not isinstance(other, CreateContentUploadResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
