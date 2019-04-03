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

import sys
import os
import re
import six
import typing

from ask_sdk_model.services.base_service_client import BaseServiceClient
from ask_sdk_model.services.api_configuration import ApiConfiguration
from ask_sdk_model.services.service_client_response import ServiceClientResponse
from ask_sdk_model.services.authentication_configuration import AuthenticationConfiguration
from ask_sdk_model.services.lwa.lwa_client import LwaClient


if typing.TYPE_CHECKING:
    from typing import Dict, List, Union, Any
    from datetime import datetime
    from ask_sdk_model.services.skill_messaging.send_skill_messaging_request import SendSkillMessagingRequest
    from ask_sdk_model.services.skill_messaging.error import Error


class SkillMessagingServiceClient(BaseServiceClient):
    """ServiceClient for calling the SkillMessagingService APIs.

    :param api_configuration: Instance of :py:class:`ask_sdk_model.services.api_configuration.ApiConfiguration`
    :type api_configuration: ask_sdk_model.services.api_configuration.ApiConfiguration
    """
    def __init__(self, api_configuration, authentication_configuration):
        # type: (ApiConfiguration, AuthenticationConfiguration) -> None
        """
        :param api_configuration: Instance of :py:class:`ask_sdk_model.services.api_configuration.ApiConfiguration`
        :type api_configuration: ask_sdk_model.services.api_configuration.ApiConfiguration
        :param authentication_configuration: Instance of :py:class:`ask_sdk_model.services.authentication_configuration.AuthenticationConfiguration`
        :type api_configuration: ask_sdk_model.services.authentication_configuration.AuthenticationConfiguration
        """
        super(SkillMessagingServiceClient, self).__init__(api_configuration)
        self._lwa_service_client = LwaClient(
            api_configuration=api_configuration,
            authentication_configuration=authentication_configuration)

    def send_skill_message(self, user_id, send_skill_messaging_request, **kwargs):
        # type: (str, SendSkillMessagingRequest, **Any) -> Union[Error]
        """
        Send a message request to a skill for a specified user.

        :param user_id: (required) The user Id for the specific user to send the message
        :type user_id: str
        :param send_skill_messaging_request: (required) Message Request to be sent to the skill.
        :type send_skill_messaging_request: ask_sdk_model.services.skill_messaging.send_skill_messaging_request.SendSkillMessagingRequest
        :rtype: None
        """
        operation_name = "send_skill_message"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params) or (params['user_id'] is None):
            raise ValueError(
                "Missing the required parameter `user_id` when calling `" + operation_name + "`")
        # verify the required parameter 'send_skill_messaging_request' is set
        if ('send_skill_messaging_request' not in params) or (params['send_skill_messaging_request'] is None):
            raise ValueError(
                "Missing the required parameter `send_skill_messaging_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skillmessages/users/{userId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'user_id' in params:
            path_params['userId'] = params['user_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'send_skill_messaging_request' in params:
            body_params = params['send_skill_messaging_request']
        header_params.append(('Content-type', 'application/json'))

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_for_scope(
            "alexa:skill_messaging")
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=202, message="Message has been successfully accepted, and will be sent to the skill "))
        error_definitions.append(ServiceClientResponse(response_type="ask_sdk_model.services.skill_messaging.error.Error", status_code=400, message="Data is missing or not valid "))
        error_definitions.append(ServiceClientResponse(response_type="ask_sdk_model.services.skill_messaging.error.Error", status_code=403, message="The skill messaging authentication token is expired or not valid "))
        error_definitions.append(ServiceClientResponse(response_type="ask_sdk_model.services.skill_messaging.error.Error", status_code=404, message="The passed userId does not exist "))
        error_definitions.append(ServiceClientResponse(response_type="ask_sdk_model.services.skill_messaging.error.Error", status_code=429, message="The requester has exceeded their maximum allowable rate of messages "))
        error_definitions.append(ServiceClientResponse(response_type="ask_sdk_model.services.skill_messaging.error.Error", status_code=500, message="The SkillMessaging service encountered an internal error for a valid request. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_sdk_model.services.skill_messaging.error.Error", status_code=0, message="Unexpected error"))

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
