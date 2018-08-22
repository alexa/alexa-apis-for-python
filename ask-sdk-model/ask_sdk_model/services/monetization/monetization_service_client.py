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
    from ask_sdk_model.services.monetization.error import Error
    from ask_sdk_model.services.monetization.in_skill_product import InSkillProduct
    from ask_sdk_model.services.monetization.in_skill_products_response import InSkillProductsResponse


class MonetizationServiceClient(BaseServiceClient):
    """ServiceClient for calling the MonetizationService APIs.

    :param api_configuration: Instance of :py:class:`ask_sdk_model.services.api_configuration.ApiConfiguration`
    :type api_configuration: ask_sdk_model.services.api_configuration.ApiConfiguration
    """

    def __init__(self, api_configuration):
        # type: (ApiConfiguration) -> None
        """
        :param api_configuration: Instance of :py:class:`ask_sdk_model.services.api_configuration.ApiConfiguration`
        :type api_configuration: ask_sdk_model.services.api_configuration.ApiConfiguration
        """
        super(MonetizationServiceClient, self).__init__(api_configuration)

    def get_in_skill_products(self, accept_language, **kwargs):
        # type: (str, str, str, str, str, float) -> Union[Error, InSkillProductsResponse]
        """
        Gets In-Skill Products based on user's context for the Skill.

        :param accept_language: (required) User's locale/language in context
        :type accept_language: str
        :param purchasable: Filter products based on whether they are purchasable by the user or not. * 'PURCHASABLE' - Products that are purchasable by the user. * 'NOT_PURCHASABLE' - Products that are not purchasable by the user.
        :type purchasable: str
        :param entitled: Filter products based on whether they are entitled to the user or not. * 'ENTITLED' - Products that the user is entitled to. * 'NOT_ENTITLED' - Products that the user is not entitled to.
        :type entitled: str
        :param product_type: Product type. * 'SUBSCRIPTION' - Once purchased, customers will own the content for the subscription period. * 'ENTITLEMENT' - Once purchased, customers will own the content forever.
        :type product_type: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element, the value of which can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that In-Skill Products API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 100 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned because maxResults was exceeded, the response contains isTruncated = true.
        :type max_results: float
        :rtype: Union[Error, InSkillProductsResponse]
        """
        operation_name = "get_in_skill_products"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'accept_language' is set
        if ('accept_language' not in params) or (params['accept_language'] is None):
            raise ValueError(
                "Missing the required parameter `accept_language` when calling `" + operation_name + "`")

        resource_path = '/v1/users/~current/skills/~current/inSkillProducts'.replace('{format}', 'json')
        path_params = {}

        query_params = []
        if 'purchasable' in params:
            query_params.append(('purchasable', params['purchasable']))
        if 'entitled' in params:
            query_params.append(('entitled', params['entitled']))
        if 'product_type' in params:
            query_params.append(('productType', params['product_type']))
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))

        header_params = []
        if 'accept_language' in params:
            header_params.append(('Accept-Language', params['accept_language']))

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Authentication setting
        authorization_value = "Bearer " + self._authorization_value
        header_params.append(("Authorization", authorization_value))

        error_definitions = []
        error_definitions.append(ServiceClientResponse(response_type="ask_sdk_model.services.monetization.in_skill_products_response.InSkillProductsResponse", status_code=200, message="Returns a list of In-Skill products on success."))
        error_definitions.append(ServiceClientResponse(response_type="ask_sdk_model.services.monetization.error.Error", status_code=400, message="Invalid request"))
        error_definitions.append(ServiceClientResponse(response_type="ask_sdk_model.services.monetization.error.Error", status_code=401, message="The authentication token is invalid or doesn&#39;t have access to make this request"))
        error_definitions.append(ServiceClientResponse(response_type="ask_sdk_model.services.monetization.error.Error", status_code=500, message="Internal Server Error"))

        return self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_sdk_model.services.monetization.in_skill_products_response.InSkillProductsResponse")

    def get_in_skill_product(self, accept_language, product_id, **kwargs):
        # type: (str, str) -> Union[Error, InSkillProduct]
        """
        Get In-Skill Product information based on user context for the Skill.

        :param accept_language: (required) User's locale/language in context
        :type accept_language: str
        :param product_id: (required) Product Id.
        :type product_id: str
        :rtype: Union[Error, InSkillProduct]
        """
        operation_name = "get_in_skill_product"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'accept_language' is set
        if ('accept_language' not in params) or (params['accept_language'] is None):
            raise ValueError(
                "Missing the required parameter `accept_language` when calling `" + operation_name + "`")
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError(
                "Missing the required parameter `product_id` when calling `" + operation_name + "`")

        resource_path = '/v1/users/~current/skills/~current/inSkillProducts/{productId}'.replace('{format}', 'json')
        path_params = {}
        if 'product_id' in params:
            path_params['productId'] = params['product_id']

        query_params = []

        header_params = []
        if 'accept_language' in params:
            header_params.append(('Accept-Language', params['accept_language']))

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Authentication setting
        authorization_value = "Bearer " + self._authorization_value
        header_params.append(("Authorization", authorization_value))

        error_definitions = []
        error_definitions.append(ServiceClientResponse(response_type="ask_sdk_model.services.monetization.in_skill_product.InSkillProduct", status_code=200, message="Returns an In-Skill Product on success."))
        error_definitions.append(ServiceClientResponse(response_type="ask_sdk_model.services.monetization.error.Error", status_code=400, message="Invalid request."))
        error_definitions.append(ServiceClientResponse(response_type="ask_sdk_model.services.monetization.error.Error", status_code=401, message="The authentication token is invalid or doesn&#39;t have access to make this request"))
        error_definitions.append(ServiceClientResponse(response_type="ask_sdk_model.services.monetization.error.Error", status_code=404, message="Requested resource not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_sdk_model.services.monetization.error.Error", status_code=500, message="Internal Server Error."))

        return self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_sdk_model.services.monetization.in_skill_product.InSkillProduct")
