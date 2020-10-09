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
    from ask_smapi_model.v1.audit_logs.client import Client as AuditLogs_ClientV1
    from ask_smapi_model.v1.audit_logs.requester import Requester as AuditLogs_RequesterV1
    from ask_smapi_model.v1.audit_logs.resource import Resource as AuditLogs_ResourceV1
    from ask_smapi_model.v1.audit_logs.operation import Operation as AuditLogs_OperationV1


class AuditLog(object):
    """

    :param x_amzn_request_id: UUID that identifies a specific request.
    :type x_amzn_request_id: (optional) str
    :param timestamp: Date-Time when the request was made.
    :type timestamp: (optional) datetime
    :param client: 
    :type client: (optional) ask_smapi_model.v1.audit_logs.client.Client
    :param operation: 
    :type operation: (optional) ask_smapi_model.v1.audit_logs.operation.Operation
    :param resources: Contains information about the resources affected in this request.
    :type resources: (optional) list[ask_smapi_model.v1.audit_logs.resource.Resource]
    :param requester: 
    :type requester: (optional) ask_smapi_model.v1.audit_logs.requester.Requester
    :param http_response_code: HTTP Status Code returned by this request.
    :type http_response_code: (optional) int

    """
    deserialized_types = {
        'x_amzn_request_id': 'str',
        'timestamp': 'datetime',
        'client': 'ask_smapi_model.v1.audit_logs.client.Client',
        'operation': 'ask_smapi_model.v1.audit_logs.operation.Operation',
        'resources': 'list[ask_smapi_model.v1.audit_logs.resource.Resource]',
        'requester': 'ask_smapi_model.v1.audit_logs.requester.Requester',
        'http_response_code': 'int'
    }  # type: Dict

    attribute_map = {
        'x_amzn_request_id': 'xAmznRequestId',
        'timestamp': 'timestamp',
        'client': 'client',
        'operation': 'operation',
        'resources': 'resources',
        'requester': 'requester',
        'http_response_code': 'httpResponseCode'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, x_amzn_request_id=None, timestamp=None, client=None, operation=None, resources=None, requester=None, http_response_code=None):
        # type: (Optional[str], Optional[datetime], Optional[AuditLogs_ClientV1], Optional[AuditLogs_OperationV1], Optional[List[AuditLogs_ResourceV1]], Optional[AuditLogs_RequesterV1], Optional[int]) -> None
        """

        :param x_amzn_request_id: UUID that identifies a specific request.
        :type x_amzn_request_id: (optional) str
        :param timestamp: Date-Time when the request was made.
        :type timestamp: (optional) datetime
        :param client: 
        :type client: (optional) ask_smapi_model.v1.audit_logs.client.Client
        :param operation: 
        :type operation: (optional) ask_smapi_model.v1.audit_logs.operation.Operation
        :param resources: Contains information about the resources affected in this request.
        :type resources: (optional) list[ask_smapi_model.v1.audit_logs.resource.Resource]
        :param requester: 
        :type requester: (optional) ask_smapi_model.v1.audit_logs.requester.Requester
        :param http_response_code: HTTP Status Code returned by this request.
        :type http_response_code: (optional) int
        """
        self.__discriminator_value = None  # type: str

        self.x_amzn_request_id = x_amzn_request_id
        self.timestamp = timestamp
        self.client = client
        self.operation = operation
        self.resources = resources
        self.requester = requester
        self.http_response_code = http_response_code

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
        if not isinstance(other, AuditLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
