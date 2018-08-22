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

from ask_sdk_model.services.base_service_client import BaseServiceClient
from ask_sdk_model.services.api_configuration import ApiConfiguration
from ask_sdk_model.services.service_client_response import ServiceClientResponse


if typing.TYPE_CHECKING:
    from typing import Dict, List, Union
    from datetime import datetime
    from ask_sdk_model.services.directive.error import Error
    from ask_sdk_model.services.directive.send_directive_request import SendDirectiveRequest


class DirectiveServiceClient(BaseServiceClient):
    """ServiceClient for calling the DirectiveService APIs.

    :param api_configuration: Instance of :py:class:`ask_sdk_model.services.api_configuration.ApiConfiguration`
    :type api_configuration: ask_sdk_model.services.api_configuration.ApiConfiguration
    """

    def __init__(self, api_configuration):
        # type: (ApiConfiguration) -> None
        """
        :param api_configuration: Instance of :py:class:`ask_sdk_model.services.api_configuration.ApiConfiguration`
        :type api_configuration: ask_sdk_model.services.api_configuration.ApiConfiguration
        """
        super(DirectiveServiceClient, self).__init__(api_configuration)

    def enqueue(self, send_directive_request, **kwargs):
        # type: (SendDirectiveRequest) -> Union[Error]
        """
        Send directives to Alexa.

        :param send_directive_request: (required) Represents the request object to send in the payload.
        :type send_directive_request: ask_sdk_model.services.directive.send_directive_request.SendDirectiveRequest
        :rtype: None
        """
        operation_name = "enqueue"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'send_directive_request' is set
        if ('send_directive_request' not in params) or (params['send_directive_request'] is None):
            raise ValueError(
                "Missing the required parameter `send_directive_request` when calling `" + operation_name + "`")

        resource_path = '/v1/directives'.replace('{format}', 'json')
        path_params = {}

        query_params = []

        header_params = []

        body_params = None
        if 'send_directive_request' in params:
            body_params = params['send_directive_request']
        header_params.append(('Content-type', 'application/json'))

        # Authentication setting
        authorization_value = "Bearer " + self._authorization_value
        header_params.append(("Authorization", authorization_value))

        error_definitions = []
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Directive sent successfully."))
        error_definitions.append(ServiceClientResponse(response_type="ask_sdk_model.services.directive.error.Error", status_code=400, message="Directive not valid."))
        error_definitions.append(ServiceClientResponse(response_type="ask_sdk_model.services.directive.error.Error", status_code=401, message="Not Authorized."))
        error_definitions.append(ServiceClientResponse(response_type="ask_sdk_model.services.directive.error.Error", status_code=403, message="The skill is not allowed to send directives at the moment."))
        error_definitions.append(ServiceClientResponse(response_type="ask_sdk_model.services.directive.error.Error", status_code=0, message="Unexpected error."))

        self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)
