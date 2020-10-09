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
    from ask_smapi_model.v1.audit_logs.client_filter import ClientFilter as AuditLogs_ClientFilterV1
    from ask_smapi_model.v1.audit_logs.resource_filter import ResourceFilter as AuditLogs_ResourceFilterV1
    from ask_smapi_model.v1.audit_logs.requester_filter import RequesterFilter as AuditLogs_RequesterFilterV1
    from ask_smapi_model.v1.audit_logs.operation_filter import OperationFilter as AuditLogs_OperationFilterV1


class RequestFilters(object):
    """
    Request Filters for filtering audit logs.


    :param clients: List of Client IDs for filtering.
    :type clients: (optional) list[ask_smapi_model.v1.audit_logs.client_filter.ClientFilter]
    :param operations: Filters for a list of operation names and versions.
    :type operations: (optional) list[ask_smapi_model.v1.audit_logs.operation_filter.OperationFilter]
    :param resources: Filters for a list of resources and/or their types. See documentation for allowed types.
    :type resources: (optional) list[ask_smapi_model.v1.audit_logs.resource_filter.ResourceFilter]
    :param requesters: 
    :type requesters: (optional) list[ask_smapi_model.v1.audit_logs.requester_filter.RequesterFilter]
    :param start_time: Sets the start time for this search. Any audit logs with timestamps after this time (inclusive) will be included in the response.
    :type start_time: (optional) datetime
    :param end_time: Sets the end time for this search. Any audit logs with timestamps before this time (exclusive) will be included in the result.
    :type end_time: (optional) datetime
    :param http_response_codes: Filters for HTTP response codes. For example, &#39;200&#39; or &#39;503&#39;
    :type http_response_codes: (optional) list[str]

    """
    deserialized_types = {
        'clients': 'list[ask_smapi_model.v1.audit_logs.client_filter.ClientFilter]',
        'operations': 'list[ask_smapi_model.v1.audit_logs.operation_filter.OperationFilter]',
        'resources': 'list[ask_smapi_model.v1.audit_logs.resource_filter.ResourceFilter]',
        'requesters': 'list[ask_smapi_model.v1.audit_logs.requester_filter.RequesterFilter]',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'http_response_codes': 'list[str]'
    }  # type: Dict

    attribute_map = {
        'clients': 'clients',
        'operations': 'operations',
        'resources': 'resources',
        'requesters': 'requesters',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'http_response_codes': 'httpResponseCodes'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, clients=None, operations=None, resources=None, requesters=None, start_time=None, end_time=None, http_response_codes=None):
        # type: (Optional[List[AuditLogs_ClientFilterV1]], Optional[List[AuditLogs_OperationFilterV1]], Optional[List[AuditLogs_ResourceFilterV1]], Optional[List[AuditLogs_RequesterFilterV1]], Optional[datetime], Optional[datetime], Optional[List[object]]) -> None
        """Request Filters for filtering audit logs.

        :param clients: List of Client IDs for filtering.
        :type clients: (optional) list[ask_smapi_model.v1.audit_logs.client_filter.ClientFilter]
        :param operations: Filters for a list of operation names and versions.
        :type operations: (optional) list[ask_smapi_model.v1.audit_logs.operation_filter.OperationFilter]
        :param resources: Filters for a list of resources and/or their types. See documentation for allowed types.
        :type resources: (optional) list[ask_smapi_model.v1.audit_logs.resource_filter.ResourceFilter]
        :param requesters: 
        :type requesters: (optional) list[ask_smapi_model.v1.audit_logs.requester_filter.RequesterFilter]
        :param start_time: Sets the start time for this search. Any audit logs with timestamps after this time (inclusive) will be included in the response.
        :type start_time: (optional) datetime
        :param end_time: Sets the end time for this search. Any audit logs with timestamps before this time (exclusive) will be included in the result.
        :type end_time: (optional) datetime
        :param http_response_codes: Filters for HTTP response codes. For example, &#39;200&#39; or &#39;503&#39;
        :type http_response_codes: (optional) list[str]
        """
        self.__discriminator_value = None  # type: str

        self.clients = clients
        self.operations = operations
        self.resources = resources
        self.requesters = requesters
        self.start_time = start_time
        self.end_time = end_time
        self.http_response_codes = http_response_codes

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
        if not isinstance(other, RequestFilters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
