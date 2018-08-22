# coding: utf-8

#
# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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

import sys
import os
import re
import six
import typing
from .device_address import DeviceAddressServiceClient
from .directive import DirectiveServiceClient
from .list_management import ListManagementServiceClient
from .monetization import MonetizationServiceClient
from .ups import UpsServiceClient

if typing.TYPE_CHECKING:
    from .api_configuration import ApiConfiguration


class ServiceClientFactory(object):
    """ServiceClientFactory class to help build service clients.

    :param api_configuration: API Configuration for calling services
    :type api_configuration: ApiConfiguration
    """
    def __init__(self, api_configuration):
        # type: (ApiConfiguration) -> None
        self.api_configuration = api_configuration

    def get_device_address_service(self):
        # type: () -> DeviceAddressServiceClient
        """Get DeviceAddressServiceClient for device_address_service.

        :return: Client for calling the service
        :rtype: DeviceAddressServiceClient
        :raises: :py:class:`ValueError`
        """
        try:
            return DeviceAddressServiceClient(self.api_configuration)
        except Exception as e:
            raise ValueError(
                "ServiceClientFactory Error while initializing DeviceAddressServiceClient: " + e)

    def get_directive_service(self):
        # type: () -> DirectiveServiceClient
        """Get DirectiveServiceClient for directive_service.

        :return: Client for calling the service
        :rtype: DirectiveServiceClient
        :raises: :py:class:`ValueError`
        """
        try:
            return DirectiveServiceClient(self.api_configuration)
        except Exception as e:
            raise ValueError(
                "ServiceClientFactory Error while initializing DirectiveServiceClient: " + e)

    def get_list_management_service(self):
        # type: () -> ListManagementServiceClient
        """Get ListManagementServiceClient for list_management_service.

        :return: Client for calling the service
        :rtype: ListManagementServiceClient
        :raises: :py:class:`ValueError`
        """
        try:
            return ListManagementServiceClient(self.api_configuration)
        except Exception as e:
            raise ValueError(
                "ServiceClientFactory Error while initializing ListManagementServiceClient: " + e)

    def get_monetization_service(self):
        # type: () -> MonetizationServiceClient
        """Get MonetizationServiceClient for monetization_service.

        :return: Client for calling the service
        :rtype: MonetizationServiceClient
        :raises: :py:class:`ValueError`
        """
        try:
            return MonetizationServiceClient(self.api_configuration)
        except Exception as e:
            raise ValueError(
                "ServiceClientFactory Error while initializing MonetizationServiceClient: " + e)

    def get_ups_service(self):
        # type: () -> UpsServiceClient
        """Get UpsServiceClient for ups_service.

        :return: Client for calling the service
        :rtype: UpsServiceClient
        :raises: :py:class:`ValueError`
        """
        try:
            return UpsServiceClient(self.api_configuration)
        except Exception as e:
            raise ValueError(
                "ServiceClientFactory Error while initializing UpsServiceClient: " + e)

