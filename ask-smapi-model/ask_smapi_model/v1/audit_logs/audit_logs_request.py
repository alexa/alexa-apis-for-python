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
    from ask_smapi_model.v1.audit_logs.sort_direction import SortDirection as AuditLogs_SortDirectionV1
    from ask_smapi_model.v1.audit_logs.request_filters import RequestFilters as AuditLogs_RequestFiltersV1
    from ask_smapi_model.v1.audit_logs.sort_field import SortField as AuditLogs_SortFieldV1
    from ask_smapi_model.v1.audit_logs.request_pagination_context import RequestPaginationContext as AuditLogs_RequestPaginationContextV1


class AuditLogsRequest(object):
    """

    :param vendor_id: Vendor Id. See developer.amazon.com/mycid.html.
    :type vendor_id: (optional) str
    :param request_filters: 
    :type request_filters: (optional) ask_smapi_model.v1.audit_logs.request_filters.RequestFilters
    :param sort_direction: 
    :type sort_direction: (optional) ask_smapi_model.v1.audit_logs.sort_direction.SortDirection
    :param sort_field: 
    :type sort_field: (optional) ask_smapi_model.v1.audit_logs.sort_field.SortField
    :param pagination_context: 
    :type pagination_context: (optional) ask_smapi_model.v1.audit_logs.request_pagination_context.RequestPaginationContext

    """
    deserialized_types = {
        'vendor_id': 'str',
        'request_filters': 'ask_smapi_model.v1.audit_logs.request_filters.RequestFilters',
        'sort_direction': 'ask_smapi_model.v1.audit_logs.sort_direction.SortDirection',
        'sort_field': 'ask_smapi_model.v1.audit_logs.sort_field.SortField',
        'pagination_context': 'ask_smapi_model.v1.audit_logs.request_pagination_context.RequestPaginationContext'
    }  # type: Dict

    attribute_map = {
        'vendor_id': 'vendorId',
        'request_filters': 'requestFilters',
        'sort_direction': 'sortDirection',
        'sort_field': 'sortField',
        'pagination_context': 'paginationContext'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, vendor_id=None, request_filters=None, sort_direction=None, sort_field=None, pagination_context=None):
        # type: (Optional[str], Optional[AuditLogs_RequestFiltersV1], Optional[AuditLogs_SortDirectionV1], Optional[AuditLogs_SortFieldV1], Optional[AuditLogs_RequestPaginationContextV1]) -> None
        """

        :param vendor_id: Vendor Id. See developer.amazon.com/mycid.html.
        :type vendor_id: (optional) str
        :param request_filters: 
        :type request_filters: (optional) ask_smapi_model.v1.audit_logs.request_filters.RequestFilters
        :param sort_direction: 
        :type sort_direction: (optional) ask_smapi_model.v1.audit_logs.sort_direction.SortDirection
        :param sort_field: 
        :type sort_field: (optional) ask_smapi_model.v1.audit_logs.sort_field.SortField
        :param pagination_context: 
        :type pagination_context: (optional) ask_smapi_model.v1.audit_logs.request_pagination_context.RequestPaginationContext
        """
        self.__discriminator_value = None  # type: str

        self.vendor_id = vendor_id
        self.request_filters = request_filters
        self.sort_direction = sort_direction
        self.sort_field = sort_field
        self.pagination_context = pagination_context

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
        if not isinstance(other, AuditLogsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
