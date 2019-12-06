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

from ask_sdk_model_runtime.base_service_client import BaseServiceClient
from ask_sdk_model_runtime.api_configuration import ApiConfiguration
from ask_sdk_model_runtime.service_client_response import ServiceClientResponse
from ask_sdk_model_runtime.api_response import ApiResponse

from ask_sdk_model_runtime.authentication_configuration import AuthenticationConfiguration
from ask_sdk_model_runtime.lwa.lwa_client import LwaClient


if typing.TYPE_CHECKING:
    from typing import Dict, List, Union, Any
    from datetime import datetime
    from ask_smapi_model.v1.catalog.create_content_upload_url_response import CreateContentUploadUrlResponse
    from ask_smapi_model.v1.skill.history.intent_requests import IntentRequests
    from ask_smapi_model.v1.skill.history.dialog_act_name import DialogActName
    from ask_smapi_model.v1.skill.validations.validations_api_response import ValidationsApiResponse
    from ask_smapi_model.v1.skill.upload_response import UploadResponse
    from ask_smapi_model.v1.skill.interaction_model.catalog.catalog_status import CatalogStatus
    from ask_smapi_model.v1.skill.simulations.simulations_api_request import SimulationsApiRequest
    from ask_smapi_model.v1.skill.interaction_model.version.catalog_values import CatalogValues
    from ask_smapi_model.v1.skill.certification.certification_response import CertificationResponse
    from ask_smapi_model.v1.skill.history.intent_confidence_bin import IntentConfidenceBin
    from ask_smapi_model.v1.skill.create_skill_request import CreateSkillRequest
    from ask_smapi_model.v1.skill.manifest.skill_manifest_envelope import SkillManifestEnvelope
    from ask_smapi_model.v1.catalog.upload.get_content_upload_response import GetContentUploadResponse
    from ask_smapi_model.v1.skill.evaluations.profile_nlu_request import ProfileNluRequest
    from ask_smapi_model.v1.skill.alexa_hosted.hosted_skill_permission import HostedSkillPermission
    from ask_smapi_model.v1.isp.update_in_skill_product_request import UpdateInSkillProductRequest
    from ask_smapi_model.v1.skill.interaction_model.catalog.update_request import UpdateRequest
    from ask_smapi_model.v1.skill.interaction_model.catalog.definition_data import DefinitionData
    import str
    from ask_smapi_model.v1.skill.interaction_model.catalog.list_catalog_response import ListCatalogResponse
    from ask_smapi_model.v1.skill.alexa_hosted.hosted_skill_metadata import HostedSkillMetadata
    from ask_smapi_model.v1.error import Error
    from ask_smapi_model.v1.skill.list_skill_response import ListSkillResponse
    from ask_smapi_model.v1.skill.beta_test.testers.list_testers_response import ListTestersResponse
    from ask_smapi_model.v1.stage_type import StageType
    from ask_smapi_model.v1.skill.history.locale_in_query import LocaleInQuery
    from ask_smapi_model.v1.skill.simulations.simulations_api_response import SimulationsApiResponse
    from ask_smapi_model.v1.bad_request_error import BadRequestError
    from ask_smapi_model.v1.skill.evaluations.profile_nlu_response import ProfileNluResponse
    from ask_smapi_model.v1.skill.interaction_model.interaction_model_data import InteractionModelData
    from ask_smapi_model.v1.skill.interaction_model.version.version_data import VersionData
    from ask_smapi_model.v1.isp.create_in_skill_product_request import CreateInSkillProductRequest
    from ask_smapi_model.v1.skill.beta_test.testers.testers_list import TestersList
    from ask_smapi_model.v1.skill.history.interaction_type import InteractionType
    from ask_smapi_model.v1.skill.create_skill_response import CreateSkillResponse
    from ask_smapi_model.v1.skill.update_skill_with_package_request import UpdateSkillWithPackageRequest
    from ask_smapi_model.v1.catalog.upload.catalog_upload_base import CatalogUploadBase
    from ask_smapi_model.v1.catalog.create_content_upload_url_request import CreateContentUploadUrlRequest
    from ask_smapi_model.v1.skill.export_response import ExportResponse
    from ask_smapi_model.v1.skill.beta_test.test_body import TestBody
    from ask_smapi_model.v1.isp.product_response import ProductResponse
    from ask_smapi_model.v1.skill.validations.validations_api_request import ValidationsApiRequest
    from ask_smapi_model.v1.isp.associated_skill_response import AssociatedSkillResponse
    from ask_smapi_model.v1.skill.alexa_hosted.hosted_skill_repository_credentials_list import HostedSkillRepositoryCredentialsList
    from ask_smapi_model.v1.skill.metrics.get_metric_data_response import GetMetricDataResponse
    from ask_smapi_model.v1.skill.beta_test.beta_test import BetaTest
    from ask_smapi_model.v1.isp.in_skill_product_summary_response import InSkillProductSummaryResponse
    from ask_smapi_model.v1.skill.private.list_private_distribution_accounts_response import ListPrivateDistributionAccountsResponse
    from ask_smapi_model.v1.skill.account_linking.account_linking_request import AccountLinkingRequest
    from ask_smapi_model.v1.skill.withdraw_request import WithdrawRequest
    from ask_smapi_model.v1.vendor_management.vendors import Vendors
    from ask_smapi_model.v1.skill.interaction_model.version.catalog_version_data import CatalogVersionData
    from ask_smapi_model.v1.skill.alexa_hosted.hosted_skill_repository_credentials_request import HostedSkillRepositoryCredentialsRequest
    from ask_smapi_model.v1.skill.interaction_model.catalog.catalog_definition_output import CatalogDefinitionOutput
    from ask_smapi_model.v1.skill.interaction_model.catalog.catalog_response import CatalogResponse
    from ask_smapi_model.v1.skill.import_response import ImportResponse
    from ask_smapi_model.v1.skill.interaction_model.version.catalog_update import CatalogUpdate
    from ask_smapi_model.v1.skill.standardized_error import StandardizedError
    from ask_smapi_model.v1.skill.history.publication_status import PublicationStatus
    from ask_smapi_model.v1.skill.submit_skill_for_certification_request import SubmitSkillForCertificationRequest
    from ask_smapi_model.v1.skill.skill_status import SkillStatus
    from ask_smapi_model.v1.skill.account_linking.account_linking_response import AccountLinkingResponse
    from ask_smapi_model.v1.isp.in_skill_product_definition_response import InSkillProductDefinitionResponse
    from ask_smapi_model.v1.skill.ssl_certificate_payload import SSLCertificatePayload
    from ask_smapi_model.v1.isp.list_in_skill_product_response import ListInSkillProductResponse
    from ask_smapi_model.v1.skill.interaction_model.version.list_response import ListResponse
    from ask_smapi_model.v1.skill.certification.list_certifications_response import ListCertificationsResponse
    from ask_smapi_model.v1.skill.create_skill_with_package_request import CreateSkillWithPackageRequest


class SkillManagementServiceClient(BaseServiceClient):
    """ServiceClient for calling the SkillManagementService APIs.

    :param api_configuration: Instance of ApiConfiguration
    :type api_configuration: ask_sdk_model_runtime.api_configuration.ApiConfiguration
    """
    def __init__(self, api_configuration, authentication_configuration, lwa_client=None):
        # type: (ApiConfiguration, AuthenticationConfiguration, LwaClient) -> None
        """
        :param api_configuration: Instance of :py:class:`ask_sdk_model_runtime.api_configuration.ApiConfiguration`
        :type api_configuration: ask_sdk_model_runtime.api_configuration.ApiConfiguration
        :param authentication_configuration: Instance of :py:class:`ask_sdk_model_runtime.authentication_configuration.AuthenticationConfiguration`
        :type api_configuration: ask_sdk_model_runtime.authentication_configuration.AuthenticationConfiguration
        :param lwa_client: (Optional) Instance of :py:class:`ask_sdk_model_runtime.lwa.LwaClient`,
        can be passed when the LwaClient configuration is different from the authentication
        and api configuration passed
        :type lwa_client: ask_sdk_model_runtime.lwa.LwaClient
        """
        super(SkillManagementServiceClient, self).__init__(api_configuration)
        if lwa_client is None:
            self._lwa_service_client = LwaClient(
                api_configuration=ApiConfiguration(
                    serializer=api_configuration.serializer, 
                    api_client=api_configuration.api_client),
                authentication_configuration=authentication_configuration,
                grant_type='refresh_token')
        else:
            self._lwa_service_client = lwa_client

    def create_catalog_upload_v1(self, catalog_id, catalog_upload_request_body, **kwargs):
        # type: (str, CatalogUploadBase, **Any) -> Union[ApiResponse, Error, BadRequestError]
        """
        Create new upload
        Create a new upload for a catalog and returns location to track the upload process.

        :param catalog_id: (required) Unique identifier of the catalog
        :type catalog_id: str
        :param catalog_upload_request_body: (required) Request body for create content upload
        :type catalog_upload_request_body: ask_smapi_model.v1.catalog.upload.catalog_upload_base.CatalogUploadBase
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Error, BadRequestError]
        """
        operation_name = "create_catalog_upload_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params) or (params['catalog_id'] is None):
            raise ValueError(
                "Missing the required parameter `catalog_id` when calling `" + operation_name + "`")
        # verify the required parameter 'catalog_upload_request_body' is set
        if ('catalog_upload_request_body' not in params) or (params['catalog_upload_request_body'] is None):
            raise ValueError(
                "Missing the required parameter `catalog_upload_request_body` when calling `" + operation_name + "`")

        resource_path = '/v1/catalogs/{catalogId}/uploads'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'catalog_upload_request_body' in params:
            body_params = params['catalog_upload_request_body']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=202, message="Accepted"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def get_content_upload_by_id_v1(self, catalog_id, upload_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, Error, GetContentUploadResponse, BadRequestError]
        """
        Get upload
        Gets detailed information about an upload which was created for a specific catalog. Includes the upload's ingestion steps and a url for downloading the file.

        :param catalog_id: (required) Unique identifier of the catalog
        :type catalog_id: str
        :param upload_id: (required) Unique identifier of the upload
        :type upload_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Error, GetContentUploadResponse, BadRequestError]
        """
        operation_name = "get_content_upload_by_id_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params) or (params['catalog_id'] is None):
            raise ValueError(
                "Missing the required parameter `catalog_id` when calling `" + operation_name + "`")
        # verify the required parameter 'upload_id' is set
        if ('upload_id' not in params) or (params['upload_id'] is None):
            raise ValueError(
                "Missing the required parameter `upload_id` when calling `" + operation_name + "`")

        resource_path = '/v1/catalogs/{catalogId}/uploads/{uploadId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']
        if 'upload_id' in params:
            path_params['uploadId'] = params['upload_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.catalog.upload.get_content_upload_response.GetContentUploadResponse", status_code=200, message="successful operation"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.catalog.upload.get_content_upload_response.GetContentUploadResponse")

        if full_response:
            return api_response
        return api_response.body

    def generate_catalog_upload_url_v1(self, catalog_id, generate_catalog_upload_url_request_body, **kwargs):
        # type: (str, CreateContentUploadUrlRequest, **Any) -> Union[ApiResponse, CreateContentUploadUrlResponse, Error, BadRequestError]
        """
        Generate preSigned urls to upload data

        :param catalog_id: (required) Unique identifier of the catalog
        :type catalog_id: str
        :param generate_catalog_upload_url_request_body: (required) Request body to generate catalog upload url
        :type generate_catalog_upload_url_request_body: ask_smapi_model.v1.catalog.create_content_upload_url_request.CreateContentUploadUrlRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, CreateContentUploadUrlResponse, Error, BadRequestError]
        """
        operation_name = "generate_catalog_upload_url_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params) or (params['catalog_id'] is None):
            raise ValueError(
                "Missing the required parameter `catalog_id` when calling `" + operation_name + "`")
        # verify the required parameter 'generate_catalog_upload_url_request_body' is set
        if ('generate_catalog_upload_url_request_body' not in params) or (params['generate_catalog_upload_url_request_body'] is None):
            raise ValueError(
                "Missing the required parameter `generate_catalog_upload_url_request_body` when calling `" + operation_name + "`")

        resource_path = '/v1/catalogs/{catalogId}/urls'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'generate_catalog_upload_url_request_body' in params:
            body_params = params['generate_catalog_upload_url_request_body']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.catalog.create_content_upload_url_response.CreateContentUploadUrlResponse", status_code=201, message="Successful operation."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.catalog.create_content_upload_url_response.CreateContentUploadUrlResponse")

        if full_response:
            return api_response
        return api_response.body

    def get_isp_list_for_vendor_v1(self, vendor_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, Error, ListInSkillProductResponse, BadRequestError]
        """
        Get the list of in-skill products for the vendor.

        :param vendor_id: (required) The vendor ID.
        :type vendor_id: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: float
        :param product_id: The list of in-skill product IDs that you wish to get the summary for. A maximum of 50 in-skill product IDs can be specified in a single listInSkillProducts call. Please note that this parameter must not be used with 'nextToken' and/or 'maxResults' parameter.
        :type product_id: list[str]
        :param stage: Filter in-skill products by specified stage.
        :type stage: str
        :param object_type: Type of in-skill product to filter on.
        :type object_type: str
        :param reference_name: Filter in-skill products by reference name.
        :type reference_name: str
        :param status: Status of in-skill product.
        :type status: str
        :param is_associated_with_skill: Filter in-skill products by whether or not they are associated to a skill.
        :type is_associated_with_skill: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Error, ListInSkillProductResponse, BadRequestError]
        """
        operation_name = "get_isp_list_for_vendor_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vendor_id' is set
        if ('vendor_id' not in params) or (params['vendor_id'] is None):
            raise ValueError(
                "Missing the required parameter `vendor_id` when calling `" + operation_name + "`")

        resource_path = '/v1/inSkillProducts'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict

        query_params = []  # type: List
        if 'vendor_id' in params:
            query_params.append(('vendorId', params['vendor_id']))
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))
        if 'product_id' in params:
            query_params.append(('productId', params['product_id']))
        if 'stage' in params:
            query_params.append(('stage', params['stage']))
        if 'object_type' in params:
            query_params.append(('type', params['object_type']))
        if 'reference_name' in params:
            query_params.append(('referenceName', params['reference_name']))
        if 'status' in params:
            query_params.append(('status', params['status']))
        if 'is_associated_with_skill' in params:
            query_params.append(('isAssociatedWithSkill', params['is_associated_with_skill']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.isp.list_in_skill_product_response.ListInSkillProductResponse", status_code=200, message="Response contains list of in-skill products for the specified vendor and stage."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad request. Returned when a required parameter is not present, badly formatted. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Too many requests received."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error"))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.isp.list_in_skill_product_response.ListInSkillProductResponse")

        if full_response:
            return api_response
        return api_response.body

    def create_isp_for_vendor_v1(self, create_in_skill_product_request, **kwargs):
        # type: (CreateInSkillProductRequest, **Any) -> Union[ApiResponse, ProductResponse, Error, BadRequestError]
        """
        Creates a new in-skill product for given vendorId.

        :param create_in_skill_product_request: (required) defines the request body for createInSkillProduct API.
        :type create_in_skill_product_request: ask_smapi_model.v1.isp.create_in_skill_product_request.CreateInSkillProductRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, ProductResponse, Error, BadRequestError]
        """
        operation_name = "create_isp_for_vendor_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_in_skill_product_request' is set
        if ('create_in_skill_product_request' not in params) or (params['create_in_skill_product_request'] is None):
            raise ValueError(
                "Missing the required parameter `create_in_skill_product_request` when calling `" + operation_name + "`")

        resource_path = '/v1/inSkillProducts'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'create_in_skill_product_request' in params:
            body_params = params['create_in_skill_product_request']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.isp.product_response.ProductResponse", status_code=201, message="Success."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad request. Returned when a required parameter is not present, badly formatted. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Too many requests received."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error"))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.isp.product_response.ProductResponse")

        if full_response:
            return api_response
        return api_response.body

    def disassociate_isp_with_skill_v1(self, product_id, skill_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, Error, BadRequestError]
        """
        Disassociates an in-skill product from a skill.

        :param product_id: (required) The in-skill product ID.
        :type product_id: str
        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Error, BadRequestError]
        """
        operation_name = "disassociate_isp_with_skill_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError(
                "Missing the required parameter `product_id` when calling `" + operation_name + "`")
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/inSkillProducts/{productId}/skills/{skillId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'product_id' in params:
            path_params['productId'] = params['product_id']
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Success. No content."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad request. Returned when a required parameter is not present, badly formatted. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="Request is forbidden."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="Requested resource not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Too many requests received."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error"))

        api_response = self.invoke(
            method="DELETE",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def associate_isp_with_skill_v1(self, product_id, skill_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, Error, BadRequestError]
        """
        Associates an in-skill product with a skill.

        :param product_id: (required) The in-skill product ID.
        :type product_id: str
        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Error, BadRequestError]
        """
        operation_name = "associate_isp_with_skill_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError(
                "Missing the required parameter `product_id` when calling `" + operation_name + "`")
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/inSkillProducts/{productId}/skills/{skillId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'product_id' in params:
            path_params['productId'] = params['product_id']
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Success. No content."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad request. Returned when a required parameter is not present, badly formatted. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="Request is forbidden."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="Requested resource not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Too many requests received."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error"))

        api_response = self.invoke(
            method="PUT",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def delete_isp_for_product_v1(self, product_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, Error, BadRequestError]
        """
        Deletes the in-skill product for given productId. Only development stage supported. Live in-skill products or in-skill products associated with a skill cannot be deleted by this API.

        :param product_id: (required) The in-skill product ID.
        :type product_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param if_match: Request header that specified an entity tag. The server will update the resource only if the eTag matches with the resource's current eTag.
        :type if_match: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Error, BadRequestError]
        """
        operation_name = "delete_isp_for_product_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError(
                "Missing the required parameter `product_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")

        resource_path = '/v1/inSkillProducts/{productId}/stages/{stage}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'product_id' in params:
            path_params['productId'] = params['product_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']

        query_params = []  # type: List

        header_params = []  # type: List
        if 'if_match' in params:
            header_params.append(('If-Match', params['if_match']))

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Success. No content."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad request. Returned when a required parameter is not present, badly formatted. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="Request is forbidden."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="Requested resource not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=412, message="Precondition failed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Too many requests received."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error"))

        api_response = self.invoke(
            method="DELETE",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def reset_entitlement_for_product_v1(self, product_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, Error, BadRequestError]
        """
        Resets the entitlement(s) of the Product for the current user.

        :param product_id: (required) The in-skill product ID.
        :type product_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Error, BadRequestError]
        """
        operation_name = "reset_entitlement_for_product_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError(
                "Missing the required parameter `product_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")

        resource_path = '/v1/inSkillProducts/{productId}/stages/{stage}/entitlement'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'product_id' in params:
            path_params['productId'] = params['product_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Success. No content."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad request. Returned when a required parameter is not present, badly formatted. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="Request is forbidden."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="Requested resource not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=412, message="Precondition failed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Too many requests received."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error"))

        api_response = self.invoke(
            method="DELETE",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def get_isp_definition_v1(self, product_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, Error, InSkillProductDefinitionResponse, BadRequestError]
        """
        Returns the in-skill product definition for given productId.

        :param product_id: (required) The in-skill product ID.
        :type product_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Error, InSkillProductDefinitionResponse, BadRequestError]
        """
        operation_name = "get_isp_definition_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError(
                "Missing the required parameter `product_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")

        resource_path = '/v1/inSkillProducts/{productId}/stages/{stage}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'product_id' in params:
            path_params['productId'] = params['product_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.isp.in_skill_product_definition_response.InSkillProductDefinitionResponse", status_code=200, message="Response contains the latest version of an in-skill product for the specified stage."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad request. Returned when a required parameter is not present, badly formatted. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="Requested resource not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Too many requests received."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error"))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.isp.in_skill_product_definition_response.InSkillProductDefinitionResponse")

        if full_response:
            return api_response
        return api_response.body

    def update_isp_for_product_v1(self, product_id, stage, update_in_skill_product_request, **kwargs):
        # type: (str, str, UpdateInSkillProductRequest, **Any) -> Union[ApiResponse, Error, BadRequestError]
        """
        Updates in-skill product definition for given productId. Only development stage supported.

        :param product_id: (required) The in-skill product ID.
        :type product_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param update_in_skill_product_request: (required) defines the request body for updateInSkillProduct API.
        :type update_in_skill_product_request: ask_smapi_model.v1.isp.update_in_skill_product_request.UpdateInSkillProductRequest
        :param if_match: Request header that specified an entity tag. The server will update the resource only if the eTag matches with the resource's current eTag.
        :type if_match: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Error, BadRequestError]
        """
        operation_name = "update_isp_for_product_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError(
                "Missing the required parameter `product_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")
        # verify the required parameter 'update_in_skill_product_request' is set
        if ('update_in_skill_product_request' not in params) or (params['update_in_skill_product_request'] is None):
            raise ValueError(
                "Missing the required parameter `update_in_skill_product_request` when calling `" + operation_name + "`")

        resource_path = '/v1/inSkillProducts/{productId}/stages/{stage}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'product_id' in params:
            path_params['productId'] = params['product_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']

        query_params = []  # type: List

        header_params = []  # type: List
        if 'if_match' in params:
            header_params.append(('If-Match', params['if_match']))

        body_params = None
        if 'update_in_skill_product_request' in params:
            body_params = params['update_in_skill_product_request']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Success."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad request. Returned when a required parameter is not present, badly formatted. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="Request is forbidden."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="Requested resource not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=412, message="Precondition failed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Too many requests received."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error"))

        api_response = self.invoke(
            method="PUT",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def get_isp_associated_skills_v1(self, product_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, AssociatedSkillResponse, Error]
        """
        Get the associated skills for the in-skill product.

        :param product_id: (required) The in-skill product ID.
        :type product_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: float
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, AssociatedSkillResponse, Error]
        """
        operation_name = "get_isp_associated_skills_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError(
                "Missing the required parameter `product_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")

        resource_path = '/v1/inSkillProducts/{productId}/stages/{stage}/skills'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'product_id' in params:
            path_params['productId'] = params['product_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']

        query_params = []  # type: List
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.isp.associated_skill_response.AssociatedSkillResponse", status_code=200, message="Returns skills associated with the in-skill product."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="Requested resource not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Too many requests received."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error"))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.isp.associated_skill_response.AssociatedSkillResponse")

        if full_response:
            return api_response
        return api_response.body

    def get_isp_summary_v1(self, product_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, InSkillProductSummaryResponse, Error]
        """
        Get the summary information for an in-skill product.

        :param product_id: (required) The in-skill product ID.
        :type product_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, InSkillProductSummaryResponse, Error]
        """
        operation_name = "get_isp_summary_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError(
                "Missing the required parameter `product_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")

        resource_path = '/v1/inSkillProducts/{productId}/stages/{stage}/summary'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'product_id' in params:
            path_params['productId'] = params['product_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.isp.in_skill_product_summary_response.InSkillProductSummaryResponse", status_code=200, message="Returns current in-skill product summary for productId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="Requested resource not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Too many requests received."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error"))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.isp.in_skill_product_summary_response.InSkillProductSummaryResponse")

        if full_response:
            return api_response
        return api_response.body

    def delete_interaction_model_catalog_v1(self, catalog_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Delete the catalog. 

        :param catalog_id: (required) Unique identifier of the catalog
        :type catalog_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "delete_interaction_model_catalog_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params) or (params['catalog_id'] is None):
            raise ValueError(
                "Missing the required parameter `catalog_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/catalogs/{catalogId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="No content; just confirm the catalog is deleted."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="The catalog cannot be deleted from reasons due to in-use by other entities."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="There is no catalog defined for the catalogId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="DELETE",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def get_interaction_model_catalog_definition_v1(self, catalog_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, CatalogDefinitionOutput, StandardizedError, BadRequestError]
        """
        get the catalog definition 

        :param catalog_id: (required) Unique identifier of the catalog
        :type catalog_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, CatalogDefinitionOutput, StandardizedError, BadRequestError]
        """
        operation_name = "get_interaction_model_catalog_definition_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params) or (params['catalog_id'] is None):
            raise ValueError(
                "Missing the required parameter `catalog_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/catalogs/{catalogId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.catalog.catalog_definition_output.CatalogDefinitionOutput", status_code=200, message="the catalog definition"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="The catalog cannot be retrieved due to errors listed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="There is no catalog defined for the catalogId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.interaction_model.catalog.catalog_definition_output.CatalogDefinitionOutput")

        if full_response:
            return api_response
        return api_response.body

    def update_interaction_model_catalog_v1(self, catalog_id, update_request, **kwargs):
        # type: (str, UpdateRequest, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        update description and vendorGuidance string for certain version of a catalog. 

        :param catalog_id: (required) Unique identifier of the catalog
        :type catalog_id: str
        :param update_request: (required) 
        :type update_request: ask_smapi_model.v1.skill.interaction_model.catalog.update_request.UpdateRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "update_interaction_model_catalog_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params) or (params['catalog_id'] is None):
            raise ValueError(
                "Missing the required parameter `catalog_id` when calling `" + operation_name + "`")
        # verify the required parameter 'update_request' is set
        if ('update_request' not in params) or (params['update_request'] is None):
            raise ValueError(
                "Missing the required parameter `update_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/catalogs/{catalogId}/update'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'update_request' in params:
            body_params = params['update_request']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="No content, indicates the fields were successfully updated."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="There is no catalog defined for the catalogId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def get_interaction_model_catalog_update_status_v1(self, catalog_id, update_request_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError, CatalogStatus]
        """
        Get the status of catalog resource and its sub-resources for a given catalogId. 

        :param catalog_id: (required) Unique identifier of the catalog
        :type catalog_id: str
        :param update_request_id: (required) The identifier for catalog version creation process
        :type update_request_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError, CatalogStatus]
        """
        operation_name = "get_interaction_model_catalog_update_status_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params) or (params['catalog_id'] is None):
            raise ValueError(
                "Missing the required parameter `catalog_id` when calling `" + operation_name + "`")
        # verify the required parameter 'update_request_id' is set
        if ('update_request_id' not in params) or (params['update_request_id'] is None):
            raise ValueError(
                "Missing the required parameter `update_request_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/catalogs/{catalogId}/updateRequest/{updateRequestId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']
        if 'update_request_id' in params:
            path_params['updateRequestId'] = params['update_request_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.catalog.catalog_status.CatalogStatus", status_code=200, message="Returns the build status and error codes for the given catalogId"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="There is no catalog defined for the catalogId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.interaction_model.catalog.catalog_status.CatalogStatus")

        if full_response:
            return api_response
        return api_response.body

    def create_interaction_model_catalog_version_v1(self, catalog_id, catalog, **kwargs):
        # type: (str, VersionData, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Create a new version of catalog entity for the given catalogId. 

        :param catalog_id: (required) Unique identifier of the catalog
        :type catalog_id: str
        :param catalog: (required) 
        :type catalog: ask_smapi_model.v1.skill.interaction_model.version.version_data.VersionData
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "create_interaction_model_catalog_version_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params) or (params['catalog_id'] is None):
            raise ValueError(
                "Missing the required parameter `catalog_id` when calling `" + operation_name + "`")
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params) or (params['catalog'] is None):
            raise ValueError(
                "Missing the required parameter `catalog` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/catalogs/{catalogId}/versions'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'catalog' in params:
            body_params = params['catalog']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=202, message="Returns update status location link on success."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error e.g. the catalog definition is invalid."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The specified catalog does not exist."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def delete_interaction_model_catalog_version_v1(self, catalog_id, version, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Delete catalog version. 

        :param catalog_id: (required) Unique identifier of the catalog
        :type catalog_id: str
        :param version: (required) Version for interaction model.
        :type version: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "delete_interaction_model_catalog_version_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params) or (params['catalog_id'] is None):
            raise ValueError(
                "Missing the required parameter `catalog_id` when calling `" + operation_name + "`")
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError(
                "Missing the required parameter `version` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/catalogs/{catalogId}/versions/{version}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']
        if 'version' in params:
            path_params['version'] = params['version']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="No Content; Confirms that version is successfully deleted."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="There is no catalog version for this catalogId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="DELETE",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def get_interaction_model_catalog_version_v1(self, catalog_id, version, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError, CatalogVersionData]
        """
        Get catalog version data of given catalog version. 

        :param catalog_id: (required) Unique identifier of the catalog
        :type catalog_id: str
        :param version: (required) Version for interaction model.
        :type version: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError, CatalogVersionData]
        """
        operation_name = "get_interaction_model_catalog_version_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params) or (params['catalog_id'] is None):
            raise ValueError(
                "Missing the required parameter `catalog_id` when calling `" + operation_name + "`")
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError(
                "Missing the required parameter `version` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/catalogs/{catalogId}/versions/{version}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']
        if 'version' in params:
            path_params['version'] = params['version']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.version.catalog_version_data.CatalogVersionData", status_code=200, message="Returns the catalog version metadata for the given catalogId and version."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="There is no catalog defined for the catalogId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.interaction_model.version.catalog_version_data.CatalogVersionData")

        if full_response:
            return api_response
        return api_response.body

    def update_interaction_model_catalog_version_v1(self, catalog_id, version, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Update description and vendorGuidance string for certain version of a catalog. 

        :param catalog_id: (required) Unique identifier of the catalog
        :type catalog_id: str
        :param version: (required) Version for interaction model.
        :type version: str
        :param catalog_update: 
        :type catalog_update: ask_smapi_model.v1.skill.interaction_model.version.catalog_update.CatalogUpdate
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "update_interaction_model_catalog_version_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params) or (params['catalog_id'] is None):
            raise ValueError(
                "Missing the required parameter `catalog_id` when calling `" + operation_name + "`")
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError(
                "Missing the required parameter `version` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/catalogs/{catalogId}/versions/{version}/update'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']
        if 'version' in params:
            path_params['version'] = params['version']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'catalog_update' in params:
            body_params = params['catalog_update']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="No Content; Confirms that version is successfully updated."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="There is no catalog defined for the catalogId"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def get_interaction_model_catalog_values_v1(self, catalog_id, version, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, StandardizedError, CatalogValues, BadRequestError]
        """
        Get catalog values from the given catalogId & version. 

        :param catalog_id: (required) Unique identifier of the catalog
        :type catalog_id: str
        :param version: (required) Version for interaction model.
        :type version: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: float
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, CatalogValues, BadRequestError]
        """
        operation_name = "get_interaction_model_catalog_values_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params) or (params['catalog_id'] is None):
            raise ValueError(
                "Missing the required parameter `catalog_id` when calling `" + operation_name + "`")
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError(
                "Missing the required parameter `version` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/catalogs/{catalogId}/versions/{version}/values'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']
        if 'version' in params:
            path_params['version'] = params['version']

        query_params = []  # type: List
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.version.catalog_values.CatalogValues", status_code=200, message="Returns list of catalog values for the given catalogId and version."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="There is no catalog defined for the catalogId"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.interaction_model.version.catalog_values.CatalogValues")

        if full_response:
            return api_response
        return api_response.body

    def list_interaction_model_catalogs_v1(self, vendor_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, StandardizedError, ListCatalogResponse, BadRequestError]
        """
        List all catalogs for the vendor. 

        :param vendor_id: (required) The vendor ID.
        :type vendor_id: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: float
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param sort_direction: Sets the sorting direction of the result items. When set to 'asc' these items are returned in ascending order of sortField value and when set to 'desc' these items are returned in descending order of sortField value.
        :type sort_direction: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, ListCatalogResponse, BadRequestError]
        """
        operation_name = "list_interaction_model_catalogs_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vendor_id' is set
        if ('vendor_id' not in params) or (params['vendor_id'] is None):
            raise ValueError(
                "Missing the required parameter `vendor_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/catalogs'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict

        query_params = []  # type: List
        if 'vendor_id' in params:
            query_params.append(('vendorId', params['vendor_id']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'sort_direction' in params:
            query_params.append(('sortDirection', params['sort_direction']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.catalog.list_catalog_response.ListCatalogResponse", status_code=200, message="Returns list of catalogs for the vendor."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="There is no catalog defined for the catalogId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.interaction_model.catalog.list_catalog_response.ListCatalogResponse")

        if full_response:
            return api_response
        return api_response.body

    def create_interaction_model_catalog_v1(self, catalog, **kwargs):
        # type: (DefinitionData, **Any) -> Union[ApiResponse, StandardizedError, CatalogResponse, BadRequestError]
        """
        Create a new version of catalog within the given catalogId. 

        :param catalog: (required) 
        :type catalog: ask_smapi_model.v1.skill.interaction_model.catalog.definition_data.DefinitionData
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, CatalogResponse, BadRequestError]
        """
        operation_name = "create_interaction_model_catalog_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog' is set
        if ('catalog' not in params) or (params['catalog'] is None):
            raise ValueError(
                "Missing the required parameter `catalog` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/catalogs'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'catalog' in params:
            body_params = params['catalog']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.catalog.catalog_response.CatalogResponse", status_code=200, message="Returns the generated catalogId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error e.g. the catalog definition is invalid."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=412, message="Precondition failed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.interaction_model.catalog.catalog_response.CatalogResponse")

        if full_response:
            return api_response
        return api_response.body

    def get_status_of_export_request_v1(self, export_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, StandardizedError, ExportResponse]
        """
        Get status for given exportId 

        :param export_id: (required) The Export ID.
        :type export_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, ExportResponse]
        """
        operation_name = "get_status_of_export_request_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'export_id' is set
        if ('export_id' not in params) or (params['export_id'] is None):
            raise ValueError(
                "Missing the required parameter `export_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/exports/{exportId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'export_id' in params:
            path_params['exportId'] = params['export_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.export_response.ExportResponse", status_code=200, message="OK."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.export_response.ExportResponse")

        if full_response:
            return api_response
        return api_response.body

    def list_skills_for_vendor_v1(self, vendor_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, ListSkillResponse, StandardizedError, BadRequestError]
        """
        Get the list of skills for the vendor.

        :param vendor_id: (required) The vendor ID.
        :type vendor_id: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: float
        :param skill_id: the list of skillIds that you wish to get the summary for. A maximum of 10 skillIds can be specified to get the skill summary in single listSkills call. Please note that this parameter must not be used with 'nextToken' or/and 'maxResults' parameter.
        :type skill_id: list[str]
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, ListSkillResponse, StandardizedError, BadRequestError]
        """
        operation_name = "list_skills_for_vendor_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vendor_id' is set
        if ('vendor_id' not in params) or (params['vendor_id'] is None):
            raise ValueError(
                "Missing the required parameter `vendor_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict

        query_params = []  # type: List
        if 'vendor_id' in params:
            query_params.append(('vendorId', params['vendor_id']))
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))
        if 'skill_id' in params:
            query_params.append(('skillId', params['skill_id']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.list_skill_response.ListSkillResponse", status_code=200, message="Returns list of skills for the vendor."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.list_skill_response.ListSkillResponse")

        if full_response:
            return api_response
        return api_response.body

    def get_import_status_v1(self, import_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, ImportResponse, StandardizedError]
        """
        Get status for given importId. 

        :param import_id: (required) The Import ID.
        :type import_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, ImportResponse, StandardizedError]
        """
        operation_name = "get_import_status_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'import_id' is set
        if ('import_id' not in params) or (params['import_id'] is None):
            raise ValueError(
                "Missing the required parameter `import_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/imports/{importId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'import_id' in params:
            path_params['importId'] = params['import_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.import_response.ImportResponse", status_code=200, message="OK."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.import_response.ImportResponse")

        if full_response:
            return api_response
        return api_response.body

    def create_skill_package_v1(self, create_skill_with_package_request, **kwargs):
        # type: (CreateSkillWithPackageRequest, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Creates a new import for a skill. 

        :param create_skill_with_package_request: (required) Defines the request body for createPackage API.
        :type create_skill_with_package_request: ask_smapi_model.v1.skill.create_skill_with_package_request.CreateSkillWithPackageRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "create_skill_package_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_skill_with_package_request' is set
        if ('create_skill_with_package_request' not in params) or (params['create_skill_with_package_request'] is None):
            raise ValueError(
                "Missing the required parameter `create_skill_with_package_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/imports'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'create_skill_with_package_request' in params:
            body_params = params['create_skill_with_package_request']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=202, message="Accepted."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=413, message="Payload too large."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def create_skill_for_vendor_v1(self, create_skill_request, **kwargs):
        # type: (CreateSkillRequest, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError, CreateSkillResponse]
        """
        Creates a new skill for given vendorId.

        :param create_skill_request: (required) Defines the request body for createSkill API.
        :type create_skill_request: ask_smapi_model.v1.skill.create_skill_request.CreateSkillRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError, CreateSkillResponse]
        """
        operation_name = "create_skill_for_vendor_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_skill_request' is set
        if ('create_skill_request' not in params) or (params['create_skill_request'] is None):
            raise ValueError(
                "Missing the required parameter `create_skill_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'create_skill_request' in params:
            body_params = params['create_skill_request']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.create_skill_response.CreateSkillResponse", status_code=202, message="Accepted; Returns a URL to track the status in &#39;Location&#39; header."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.create_skill_response.CreateSkillResponse")

        if full_response:
            return api_response
        return api_response.body

    def get_alexa_hosted_skill_metadata_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, StandardizedError, HostedSkillMetadata, BadRequestError]
        """
        Get Alexa hosted skill's metadata

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, HostedSkillMetadata, BadRequestError]
        """
        operation_name = "get_alexa_hosted_skill_metadata_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/alexaHosted'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.alexa_hosted.hosted_skill_metadata.HostedSkillMetadata", status_code=200, message="response contains the Alexa hosted skill&#39;s metadata"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error e.g. Authorization Url is invalid"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.alexa_hosted.hosted_skill_metadata.HostedSkillMetadata")

        if full_response:
            return api_response
        return api_response.body

    def generate_credentials_for_alexa_hosted_skill_v1(self, skill_id, hosted_skill_repository_credentials_request, **kwargs):
        # type: (str, HostedSkillRepositoryCredentialsRequest, **Any) -> Union[ApiResponse, HostedSkillRepositoryCredentialsList, StandardizedError, BadRequestError]
        """
        Generates hosted skill repository credentials to access the hosted skill repository.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param hosted_skill_repository_credentials_request: (required) defines the request body for hosted skill repository credentials
        :type hosted_skill_repository_credentials_request: ask_smapi_model.v1.skill.alexa_hosted.hosted_skill_repository_credentials_request.HostedSkillRepositoryCredentialsRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, HostedSkillRepositoryCredentialsList, StandardizedError, BadRequestError]
        """
        operation_name = "generate_credentials_for_alexa_hosted_skill_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'hosted_skill_repository_credentials_request' is set
        if ('hosted_skill_repository_credentials_request' not in params) or (params['hosted_skill_repository_credentials_request'] is None):
            raise ValueError(
                "Missing the required parameter `hosted_skill_repository_credentials_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/alexaHosted/repository/credentials/generate'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'hosted_skill_repository_credentials_request' in params:
            body_params = params['hosted_skill_repository_credentials_request']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.alexa_hosted.hosted_skill_repository_credentials_list.HostedSkillRepositoryCredentialsList", status_code=200, message="Response contains the hosted skill repository credentials"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error e.g. Authorization Url is invalid"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.alexa_hosted.hosted_skill_repository_credentials_list.HostedSkillRepositoryCredentialsList")

        if full_response:
            return api_response
        return api_response.body

    def end_beta_test_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, Error, BadRequestError]
        """
        End beta test.
        End a beta test for a given Alexa skill. System will revoke the entitlement of each tester and send access-end notification email to them. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Error, BadRequestError]
        """
        operation_name = "end_beta_test_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/betaTest/end'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=202, message="Accept. Return a URL to track the resource in &#39;Location&#39; header."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=409, message="The request could not be completed due to a conflict with the current state of the target resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def get_beta_test_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, BetaTest, Error, BadRequestError]
        """
        Get beta test.
        Get beta test for a given Alexa skill.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, BetaTest, Error, BadRequestError]
        """
        operation_name = "get_beta_test_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/betaTest'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.beta_test.beta_test.BetaTest", status_code=200, message="Success."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.beta_test.beta_test.BetaTest")

        if full_response:
            return api_response
        return api_response.body

    def create_beta_test_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, Error]
        """
        Create beta test.
        Create a beta test for a given Alexa skill.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param create_test_body: JSON object containing the details of a beta test used to create the test.
        :type create_test_body: ask_smapi_model.v1.skill.beta_test.test_body.TestBody
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Error]
        """
        operation_name = "create_beta_test_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/betaTest'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'create_test_body' in params:
            body_params = params['create_test_body']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Success. Return a URL to track the resource in &#39;Location&#39; header."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=409, message="The request could not be completed due to a conflict with the current state of the target resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def update_beta_test_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, Error, BadRequestError]
        """
        Update beta test.
        Update a beta test for a given Alexa skill.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param create_test_body: JSON object containing the details of a beta test used to create the test.
        :type create_test_body: ask_smapi_model.v1.skill.beta_test.test_body.TestBody
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Error, BadRequestError]
        """
        operation_name = "update_beta_test_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/betaTest'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'create_test_body' in params:
            body_params = params['create_test_body']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Success. No content."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error."))

        api_response = self.invoke(
            method="PUT",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def start_beta_test_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, Error, BadRequestError]
        """
        Start beta test
        Start a beta test for a given Alexa skill. System will send invitation emails to each tester in the test, and add entitlement on the acceptance. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Error, BadRequestError]
        """
        operation_name = "start_beta_test_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/betaTest/start'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=202, message="Accept. Return a URL to track the resource in &#39;Location&#39; header."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=409, message="The request could not be completed due to a conflict with the current state of the target resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def add_testers_to_beta_test_v1(self, skill_id, testers_request, **kwargs):
        # type: (str, TestersList, **Any) -> Union[ApiResponse, Error, BadRequestError]
        """
        Add testers to an existing beta test.
        Add testers to a beta test for the given Alexa skill.  System will send invitation email to each tester and add entitlement on the acceptance. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param testers_request: (required) JSON object containing the email address of beta testers.
        :type testers_request: ask_smapi_model.v1.skill.beta_test.testers.testers_list.TestersList
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Error, BadRequestError]
        """
        operation_name = "add_testers_to_beta_test_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'testers_request' is set
        if ('testers_request' not in params) or (params['testers_request'] is None):
            raise ValueError(
                "Missing the required parameter `testers_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/betaTest/testers/add'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'testers_request' in params:
            body_params = params['testers_request']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Success. No content."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def get_list_of_testers_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, Error, ListTestersResponse, BadRequestError]
        """
        List testers.
        List all testers in a beta test for the given Alexa skill.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: float
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Error, ListTestersResponse, BadRequestError]
        """
        operation_name = "get_list_of_testers_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/betaTest/testers'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.beta_test.testers.list_testers_response.ListTestersResponse", status_code=200, message="Success."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad request."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.beta_test.testers.list_testers_response.ListTestersResponse")

        if full_response:
            return api_response
        return api_response.body

    def remove_testers_from_beta_test_v1(self, skill_id, testers_request, **kwargs):
        # type: (str, TestersList, **Any) -> Union[ApiResponse, Error, BadRequestError]
        """
        Remove testers from an existing beta test.
        Remove testers from a beta test for the given Alexa skill.  System will send access end email to each tester and remove entitlement for them. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param testers_request: (required) JSON object containing the email address of beta testers.
        :type testers_request: ask_smapi_model.v1.skill.beta_test.testers.testers_list.TestersList
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Error, BadRequestError]
        """
        operation_name = "remove_testers_from_beta_test_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'testers_request' is set
        if ('testers_request' not in params) or (params['testers_request'] is None):
            raise ValueError(
                "Missing the required parameter `testers_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/betaTest/testers/remove'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'testers_request' in params:
            body_params = params['testers_request']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Success. No content."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def request_feedback_from_testers_v1(self, skill_id, testers_request, **kwargs):
        # type: (str, TestersList, **Any) -> Union[ApiResponse, Error, BadRequestError]
        """
        Request feedback from testers.
        Request feedback from the testers in a beta test for the given Alexa skill.  System will send notification emails to testers to request feedback. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param testers_request: (required) JSON object containing the email address of beta testers.
        :type testers_request: ask_smapi_model.v1.skill.beta_test.testers.testers_list.TestersList
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Error, BadRequestError]
        """
        operation_name = "request_feedback_from_testers_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'testers_request' is set
        if ('testers_request' not in params) or (params['testers_request'] is None):
            raise ValueError(
                "Missing the required parameter `testers_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/betaTest/testers/requestFeedback'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'testers_request' in params:
            body_params = params['testers_request']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Success. No content."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=409, message="The request could not be completed due to a conflict with the current state of the target resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def send_reminder_to_testers_v1(self, skill_id, testers_request, **kwargs):
        # type: (str, TestersList, **Any) -> Union[ApiResponse, Error, BadRequestError]
        """
        Send reminder to testers in a beta test.
        Send reminder to the testers in a beta test for the given Alexa skill.  System will send invitation email to each tester and add entitlement on the acceptance. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param testers_request: (required) JSON object containing the email address of beta testers.
        :type testers_request: ask_smapi_model.v1.skill.beta_test.testers.testers_list.TestersList
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Error, BadRequestError]
        """
        operation_name = "send_reminder_to_testers_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'testers_request' is set
        if ('testers_request' not in params) or (params['testers_request'] is None):
            raise ValueError(
                "Missing the required parameter `testers_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/betaTest/testers/sendReminder'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'testers_request' in params:
            body_params = params['testers_request']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Success. No content."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=409, message="The request could not be completed due to a conflict with the current state of the target resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def get_certification_review_v1(self, skill_id, certification_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, CertificationResponse, Error]
        """
        Gets a specific certification resource. The response contains the review tracking information for a skill to show how much time the skill is expected to remain under review by Amazon. Once the review is complete, the response also contains the outcome of the review. Old certifications may not be available, however any ongoing certification would always give a response. If the certification is unavailable the result will return a 404 HTTP status code. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param certification_id: (required) Id of the certification. Reserved word identifier of mostRecent can be used to get the most recent certification for the skill. Note that the behavior of the API in this case would be the same as when the actual certification id of the most recent certification is used in the request. 
        :type certification_id: str
        :param accept_language: User's locale/language in context.
        :type accept_language: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, CertificationResponse, Error]
        """
        operation_name = "get_certification_review_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'certification_id' is set
        if ('certification_id' not in params) or (params['certification_id'] is None):
            raise ValueError(
                "Missing the required parameter `certification_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/certifications/{certificationId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'certification_id' in params:
            path_params['certificationId'] = params['certification_id']

        query_params = []  # type: List

        header_params = []  # type: List
        if 'accept_language' in params:
            header_params.append(('Accept-Language', params['accept_language']))

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.certification.certification_response.CertificationResponse", status_code=200, message="Successfully retrieved skill certification information."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceeded the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.certification.certification_response.CertificationResponse")

        if full_response:
            return api_response
        return api_response.body

    def get_certifications_list_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, ListCertificationsResponse, Error]
        """
        Get list of all certifications available for a skill, including information about past certifications and any ongoing certification. The default sort order is descending on skillSubmissionTimestamp for Certifications. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: float
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, ListCertificationsResponse, Error]
        """
        operation_name = "get_certifications_list_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/certifications'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.certification.list_certifications_response.ListCertificationsResponse", status_code=200, message="Returns list of certifications for the skillId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=400, message="Server cannot process the request due to a client error e.g. if any request parameter is invalid like certification Id or pagination token etc. If the maxResults is not in the range of 1 to 50, it also qualifies for this error. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceeded the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.certification.list_certifications_response.ListCertificationsResponse")

        if full_response:
            return api_response
        return api_response.body

    def delete_skill_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Delete the skill and model for given skillId.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "delete_skill_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Success. No content."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="DELETE",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def get_utterance_data_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError, IntentRequests]
        """
        The Intent Request History API provides customers with the aggregated and anonymized transcription of user speech data and intent request details for their skills.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: float
        :param sort_direction: Sets the sorting direction of the result items. When set to 'asc' these items are returned in ascending order of sortField value and when set to 'desc' these items are returned in descending order of sortField value.
        :type sort_direction: str
        :param sort_field: Sets the field on which the sorting would be applied.
        :type sort_field: str
        :param stage: A filter used to retrieve items where the stage is equal to the given value.
        :type stage: list[ask_smapi_model.v1.stage_type.StageType]
        :param locale: 
        :type locale: list[ask_smapi_model.v1.skill.history.locale_in_query.LocaleInQuery]
        :param dialog_act_name: A filter used to retrieve items where the dialogAct name is equal to the given value. * `Dialog.ElicitSlot`: Alexa asked the user for the value of a specific slot. (https://developer.amazon.com/docs/custom-skills/dialog-interface-reference.html#elicitslot) * `Dialog.ConfirmSlot`: Alexa confirmed the value of a specific slot before continuing with the dialog. (https://developer.amazon.com/docs/custom-skills/dialog-interface-reference.html#confirmslot) * `Dialog.ConfirmIntent`: Alexa confirmed the all the information the user has provided for the intent before the skill took action. (https://developer.amazon.com/docs/custom-skills/dialog-interface-reference.html#confirmintent) 
        :type dialog_act_name: list[ask_smapi_model.v1.skill.history.dialog_act_name.DialogActName]
        :param intent_confidence_bin: 
        :type intent_confidence_bin: list[ask_smapi_model.v1.skill.history.intent_confidence_bin.IntentConfidenceBin]
        :param intent_name: A filter used to retrieve items where the intent name is equal to the given value.
        :type intent_name: list[str]
        :param intent_slots_name: A filter used to retrieve items where the one of the slot names is equal to the given value.
        :type intent_slots_name: list[str]
        :param interaction_type: 
        :type interaction_type: list[ask_smapi_model.v1.skill.history.interaction_type.InteractionType]
        :param publication_status: 
        :type publication_status: list[ask_smapi_model.v1.skill.history.publication_status.PublicationStatus]
        :param utterance_text: A filter used to retrieve items where the utterance text contains the given phrase. Each filter value can be at-least 1 character and at-most 100 characters long.
        :type utterance_text: list[str]
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError, IntentRequests]
        """
        operation_name = "get_utterance_data_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/history/intentRequests'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))
        if 'sort_direction' in params:
            query_params.append(('sortDirection', params['sort_direction']))
        if 'sort_field' in params:
            query_params.append(('sortField', params['sort_field']))
        if 'stage' in params:
            query_params.append(('stage', params['stage']))
        if 'locale' in params:
            query_params.append(('locale', params['locale']))
        if 'dialog_act_name' in params:
            query_params.append(('dialogAct.name', params['dialog_act_name']))
        if 'intent_confidence_bin' in params:
            query_params.append(('intent.confidence.bin', params['intent_confidence_bin']))
        if 'intent_name' in params:
            query_params.append(('intent.name', params['intent_name']))
        if 'intent_slots_name' in params:
            query_params.append(('intent.slots.name', params['intent_slots_name']))
        if 'interaction_type' in params:
            query_params.append(('interactionType', params['interaction_type']))
        if 'publication_status' in params:
            query_params.append(('publicationStatus', params['publication_status']))
        if 'utterance_text' in params:
            query_params.append(('utteranceText', params['utterance_text']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.history.intent_requests.IntentRequests", status_code=200, message="Returns a list of utterance items for the given skill."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad Request."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="Unauthorized."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="Skill Not Found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.history.intent_requests.IntentRequests")

        if full_response:
            return api_response
        return api_response.body

    def import_skill_package_v1(self, update_skill_with_package_request, skill_id, **kwargs):
        # type: (UpdateSkillWithPackageRequest, str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Creates a new import for a skill with given skillId. 

        :param update_skill_with_package_request: (required) Defines the request body for updatePackage API.
        :type update_skill_with_package_request: ask_smapi_model.v1.skill.update_skill_with_package_request.UpdateSkillWithPackageRequest
        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param if_match: Request header that specified an entity tag. The server will update the resource only if the eTag matches with the resource's current eTag.
        :type if_match: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "import_skill_package_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'update_skill_with_package_request' is set
        if ('update_skill_with_package_request' not in params) or (params['update_skill_with_package_request'] is None):
            raise ValueError(
                "Missing the required parameter `update_skill_with_package_request` when calling `" + operation_name + "`")
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/imports'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List
        if 'if_match' in params:
            header_params.append(('If-Match', params['if_match']))

        body_params = None
        if 'update_skill_with_package_request' in params:
            body_params = params['update_skill_with_package_request']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=202, message="Accepted."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=409, message="The request could not be completed due to a conflict with the current state of the target resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=413, message="Payload too large."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def get_skill_metrics_v1(self, skill_id, start_time, end_time, period, metric, stage, skill_type, **kwargs):
        # type: (str, datetime, datetime, str, str, str, str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError, GetMetricDataResponse]
        """
        Get analytic metrics report of skill usage.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param start_time: (required) The start time of query.
        :type start_time: datetime
        :param end_time: (required) The end time of query (The maximum time duration is 1 week)
        :type end_time: datetime
        :param period: (required) The aggregation period to use when retrieving the metric, follows ISO_8601#Durations format.
        :type period: str
        :param metric: (required) A distinct set of logic which predictably returns a set of data.
        :type metric: str
        :param stage: (required) The stage of the skill (live, development).
        :type stage: str
        :param skill_type: (required) The type of the skill (custom, smartHome and flashBriefing).
        :type skill_type: str
        :param intent: The intent of the skill.
        :type intent: str
        :param locale: The locale for the skill. e.g. en-GB, en-US, de-DE and etc.
        :type locale: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: float
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError, GetMetricDataResponse]
        """
        operation_name = "get_skill_metrics_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'start_time' is set
        if ('start_time' not in params) or (params['start_time'] is None):
            raise ValueError(
                "Missing the required parameter `start_time` when calling `" + operation_name + "`")
        # verify the required parameter 'end_time' is set
        if ('end_time' not in params) or (params['end_time'] is None):
            raise ValueError(
                "Missing the required parameter `end_time` when calling `" + operation_name + "`")
        # verify the required parameter 'period' is set
        if ('period' not in params) or (params['period'] is None):
            raise ValueError(
                "Missing the required parameter `period` when calling `" + operation_name + "`")
        # verify the required parameter 'metric' is set
        if ('metric' not in params) or (params['metric'] is None):
            raise ValueError(
                "Missing the required parameter `metric` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")
        # verify the required parameter 'skill_type' is set
        if ('skill_type' not in params) or (params['skill_type'] is None):
            raise ValueError(
                "Missing the required parameter `skill_type` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/metrics'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))
        if 'period' in params:
            query_params.append(('period', params['period']))
        if 'metric' in params:
            query_params.append(('metric', params['metric']))
        if 'stage' in params:
            query_params.append(('stage', params['stage']))
        if 'skill_type' in params:
            query_params.append(('skillType', params['skill_type']))
        if 'intent' in params:
            query_params.append(('intent', params['intent']))
        if 'locale' in params:
            query_params.append(('locale', params['locale']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.metrics.get_metric_data_response.GetMetricDataResponse", status_code=200, message="Get analytic metrics report successfully."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad request due to invalid or missing data."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.metrics.get_metric_data_response.GetMetricDataResponse")

        if full_response:
            return api_response
        return api_response.body

    def simulate_skill_v1(self, skill_id, simulations_api_request, **kwargs):
        # type: (str, SimulationsApiRequest, **Any) -> Union[ApiResponse, SimulationsApiResponse, Error, BadRequestError]
        """
        Simulate executing a skill with the given id.
        This is an asynchronous API that simulates a skill execution in the Alexa eco-system given an utterance text of what a customer would say to Alexa. A successful response will contain a header with the location of the simulation resource. In cases where requests to this API results in an error, the response will contain an error code and a description of the problem. The skill being simulated must be in development stage, and it must also belong to and be enabled by the user of this API. Concurrent requests per user is currently not supported. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param simulations_api_request: (required) Payload sent to the skill simulation API.
        :type simulations_api_request: ask_smapi_model.v1.skill.simulations.simulations_api_request.SimulationsApiRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, SimulationsApiResponse, Error, BadRequestError]
        """
        operation_name = "simulate_skill_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'simulations_api_request' is set
        if ('simulations_api_request' not in params) or (params['simulations_api_request'] is None):
            raise ValueError(
                "Missing the required parameter `simulations_api_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/simulations'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'simulations_api_request' in params:
            body_params = params['simulations_api_request']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.simulations.simulations_api_response.SimulationsApiResponse", status_code=200, message="Skill simulation has successfully began."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad request due to invalid or missing data."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="API user does not have permission to call this API or is currently in a state that does not allow simulation of this skill. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The specified skill does not exist."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=409, message="This requests conflicts with another one currently being processed. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="API user has exceeded the permitted request rate."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal service error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.simulations.simulations_api_response.SimulationsApiResponse")

        if full_response:
            return api_response
        return api_response.body

    def get_skill_simulation_v1(self, skill_id, simulation_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, SimulationsApiResponse, Error, BadRequestError]
        """
        Get the result of a previously executed simulation.
        This API gets the result of a previously executed simulation. A successful response will contain the status of the executed simulation. If the simulation successfully completed, the response will also contain information related to skill invocation. In cases where requests to this API results in an error, the response will contain an error code and a description of the problem. In cases where the simulation failed, the response will contain a status attribute indicating that a failure occurred and details about what was sent to the skill endpoint. Note that simulation results are stored for 10 minutes. A request for an expired simulation result will return a 404 HTTP status code. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param simulation_id: (required) Id of the simulation. 
        :type simulation_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, SimulationsApiResponse, Error, BadRequestError]
        """
        operation_name = "get_skill_simulation_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'simulation_id' is set
        if ('simulation_id' not in params) or (params['simulation_id'] is None):
            raise ValueError(
                "Missing the required parameter `simulation_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/simulations/{simulationId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'simulation_id' in params:
            path_params['simulationId'] = params['simulation_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.simulations.simulations_api_response.SimulationsApiResponse", status_code=200, message="Successfully retrieved skill simulation information."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="API user does not have permission or is currently in a state that does not allow calls to this API. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The specified skill or simulation does not exist. The error response will contain a description that indicates the specific resource type that was not found. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="API user has exceeded the permitted request rate."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal service error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.simulations.simulations_api_response.SimulationsApiResponse")

        if full_response:
            return api_response
        return api_response.body

    def get_ssl_certificates_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, StandardizedError, SSLCertificatePayload]
        """
        Returns the ssl certificate sets currently associated with this skill. Sets consist of one ssl certificate blob associated with a region as well as the default certificate for the skill.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, SSLCertificatePayload]
        """
        operation_name = "get_ssl_certificates_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/sslCertificateSets/~latest'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.ssl_certificate_payload.SSLCertificatePayload", status_code=200, message="Response contains the latest version of the ssl certificates."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.ssl_certificate_payload.SSLCertificatePayload")

        if full_response:
            return api_response
        return api_response.body

    def set_ssl_certificates_v1(self, skill_id, ssl_certificate_payload, **kwargs):
        # type: (str, SSLCertificatePayload, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Updates the ssl certificates associated with this skill.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param ssl_certificate_payload: (required) Defines the input/output of the ssl certificates api for a skill.
        :type ssl_certificate_payload: ask_smapi_model.v1.skill.ssl_certificate_payload.SSLCertificatePayload
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "set_ssl_certificates_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'ssl_certificate_payload' is set
        if ('ssl_certificate_payload' not in params) or (params['ssl_certificate_payload'] is None):
            raise ValueError(
                "Missing the required parameter `ssl_certificate_payload` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/sslCertificateSets/~latest'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'ssl_certificate_payload' in params:
            body_params = params['ssl_certificate_payload']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Accepted; Request was successful and get will now result in the new values."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="PUT",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def delete_skill_enablement_v1(self, skill_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Deletes the enablement for given skillId/stage and customerId (retrieved from Auth token).

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "delete_skill_enablement_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stage}/enablement'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="No Content; Confirms that enablement is successfully deleted."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="DELETE",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def get_skill_enablement_status_v1(self, skill_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Checks whether an enablement exist for given skillId/stage and customerId (retrieved from Auth token)

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "get_skill_enablement_status_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stage}/enablement'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="No Content; Confirms that enablement resource exists for given skillId &amp; stage."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def set_skill_enablement_v1(self, skill_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Creates/Updates the enablement for given skillId/stage and customerId (retrieved from Auth token)

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "set_skill_enablement_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stage}/enablement'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="No Content; Confirms that enablement is successfully created/updated."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=409, message="The request could not be completed due to a conflict with the current state of the target resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="PUT",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def create_export_request_for_skill_v1(self, skill_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, StandardizedError]
        """
        Creates a new export for a skill with given skillId and stage. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError]
        """
        operation_name = "create_export_request_for_skill_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stage}/exports'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=202, message="Accepted."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=409, message="The request could not be completed due to a conflict with the current state of the target resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def get_isp_list_for_skill_id_v1(self, skill_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, Error, ListInSkillProductResponse, BadRequestError]
        """
        Get the list of in-skill products for the skillId.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: float
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Error, ListInSkillProductResponse, BadRequestError]
        """
        operation_name = "get_isp_list_for_skill_id_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stage}/inSkillProducts'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']

        query_params = []  # type: List
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.isp.list_in_skill_product_response.ListInSkillProductResponse", status_code=200, message="Response contains list of in-skill products for the specified skillId and stage."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad request. Returned when a required parameter is not present, badly formatted. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="Requested resource not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Too many requests received."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error"))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.isp.list_in_skill_product_response.ListInSkillProductResponse")

        if full_response:
            return api_response
        return api_response.body

    def profile_nlu_v1(self, profile_nlu_request, skill_id, stage, locale, **kwargs):
        # type: (ProfileNluRequest, str, str, str, **Any) -> Union[ApiResponse, ProfileNluResponse, Error, BadRequestError]
        """
        Profile a test utterance.
        This is a synchronous API that profiles an utterance against interaction model.

        :param profile_nlu_request: (required) Payload sent to the profile nlu API.
        :type profile_nlu_request: ask_smapi_model.v1.skill.evaluations.profile_nlu_request.ProfileNluRequest
        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param locale: (required) The locale for the model requested e.g. en-GB, en-US, de-DE.
        :type locale: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, ProfileNluResponse, Error, BadRequestError]
        """
        operation_name = "profile_nlu_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'profile_nlu_request' is set
        if ('profile_nlu_request' not in params) or (params['profile_nlu_request'] is None):
            raise ValueError(
                "Missing the required parameter `profile_nlu_request` when calling `" + operation_name + "`")
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")
        # verify the required parameter 'locale' is set
        if ('locale' not in params) or (params['locale'] is None):
            raise ValueError(
                "Missing the required parameter `locale` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stage}/interactionModel/locales/{locale}/profileNlu'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']
        if 'locale' in params:
            path_params['locale'] = params['locale']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'profile_nlu_request' in params:
            body_params = params['profile_nlu_request']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.evaluations.profile_nlu_response.ProfileNluResponse", status_code=200, message="Profiled utterance against interaction model and returned nlu response successfully."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad request due to invalid or missing data."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=409, message="This requests conflicts with another one currently being processed. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="API user has exceeded the permitted request rate."))
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=500, message="Internal service error."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.evaluations.profile_nlu_response.ProfileNluResponse")

        if full_response:
            return api_response
        return api_response.body

    def list_private_distribution_accounts_v1(self, skill_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, StandardizedError, ListPrivateDistributionAccountsResponse, BadRequestError]
        """
        List private distribution accounts. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: float
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, ListPrivateDistributionAccountsResponse, BadRequestError]
        """
        operation_name = "list_private_distribution_accounts_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stage}/privateDistributionAccounts'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']

        query_params = []  # type: List
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.private.list_private_distribution_accounts_response.ListPrivateDistributionAccountsResponse", status_code=200, message="Returns list of private distribution accounts on success."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.private.list_private_distribution_accounts_response.ListPrivateDistributionAccountsResponse")

        if full_response:
            return api_response
        return api_response.body

    def delete_private_distribution_account_id_v1(self, skill_id, stage, id, **kwargs):
        # type: (str, str, str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Remove an id from the private distribution accounts. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param id: (required) ARN that a skill can be privately distributed to.
        :type id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "delete_private_distribution_account_id_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError(
                "Missing the required parameter `id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stage}/privateDistributionAccounts/{id}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Success."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="DELETE",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def set_private_distribution_account_id_v1(self, skill_id, stage, id, **kwargs):
        # type: (str, str, str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Add an id to the private distribution accounts. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param id: (required) ARN that a skill can be privately distributed to.
        :type id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "set_private_distribution_account_id_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError(
                "Missing the required parameter `id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stage}/privateDistributionAccounts/{id}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']
        if 'id' in params:
            path_params['id'] = params['id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Success."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="PUT",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def delete_account_linking_info_v1(self, skill_id, stage_v2, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Delete AccountLinking information of a skill for the given stage. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage_v2: (required) Stages of a skill including the new certified stage. * `development` - skills which are currently in development corresponds to this stage. * `certified` -  skills which have completed certification and ready for publishing corresponds to this stage. * `live` - skills which are currently live corresponds to this stage. 
        :type stage_v2: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "delete_account_linking_info_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage_v2' is set
        if ('stage_v2' not in params) or (params['stage_v2'] is None):
            raise ValueError(
                "Missing the required parameter `stage_v2` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stageV2}/accountLinkingClient'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage_v2' in params:
            path_params['stageV2'] = params['stage_v2']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Success. No content."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The specified skill/stage/accountLinkingClient doesn&#39;t exist."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="DELETE",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def get_account_linking_info_v1(self, skill_id, stage_v2, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError, AccountLinkingResponse]
        """
        Get AccountLinking information for the skill. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage_v2: (required) Stages of a skill including the new certified stage. * `development` - skills which are currently in development corresponds to this stage. * `certified` -  skills which have completed certification and ready for publishing corresponds to this stage. * `live` - skills which are currently live corresponds to this stage. 
        :type stage_v2: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError, AccountLinkingResponse]
        """
        operation_name = "get_account_linking_info_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage_v2' is set
        if ('stage_v2' not in params) or (params['stage_v2'] is None):
            raise ValueError(
                "Missing the required parameter `stage_v2` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stageV2}/accountLinkingClient'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage_v2' in params:
            path_params['stageV2'] = params['stage_v2']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.account_linking.account_linking_response.AccountLinkingResponse", status_code=200, message="Returns AccountLinking response of the skill."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.account_linking.account_linking_response.AccountLinkingResponse")

        if full_response:
            return api_response
        return api_response.body

    def update_account_linking_info_v1(self, skill_id, stage_v2, account_linking_request, **kwargs):
        # type: (str, str, AccountLinkingRequest, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Create AccountLinking information for the skill. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage_v2: (required) Stages of a skill including the new certified stage. * `development` - skills which are currently in development corresponds to this stage. * `certified` -  skills which have completed certification and ready for publishing corresponds to this stage. * `live` - skills which are currently live corresponds to this stage. 
        :type stage_v2: str
        :param account_linking_request: (required) The fields required to create accountLinking partner.
        :type account_linking_request: ask_smapi_model.v1.skill.account_linking.account_linking_request.AccountLinkingRequest
        :param if_match: Request header that specified an entity tag. The server will update the resource only if the eTag matches with the resource's current eTag.
        :type if_match: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "update_account_linking_info_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage_v2' is set
        if ('stage_v2' not in params) or (params['stage_v2'] is None):
            raise ValueError(
                "Missing the required parameter `stage_v2` when calling `" + operation_name + "`")
        # verify the required parameter 'account_linking_request' is set
        if ('account_linking_request' not in params) or (params['account_linking_request'] is None):
            raise ValueError(
                "Missing the required parameter `account_linking_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stageV2}/accountLinkingClient'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage_v2' in params:
            path_params['stageV2'] = params['stage_v2']

        query_params = []  # type: List

        header_params = []  # type: List
        if 'if_match' in params:
            header_params.append(('If-Match', params['if_match']))

        body_params = None
        if 'account_linking_request' in params:
            body_params = params['account_linking_request']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Success"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error e.g. Authorization Url is invalid."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=412, message="Precondition failed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="PUT",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def get_interaction_model_v1(self, skill_id, stage_v2, locale, **kwargs):
        # type: (str, str, str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError, InteractionModelData]
        """
        Gets the `InteractionModel` for the skill in the given stage. The path params **skillId**, **stage** and **locale** are required. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage_v2: (required) Stages of a skill including the new certified stage. * `development` - skills which are currently in development corresponds to this stage. * `certified` -  skills which have completed certification and ready for publishing corresponds to this stage. * `live` - skills which are currently live corresponds to this stage. 
        :type stage_v2: str
        :param locale: (required) The locale for the model requested e.g. en-GB, en-US, de-DE.
        :type locale: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError, InteractionModelData]
        """
        operation_name = "get_interaction_model_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage_v2' is set
        if ('stage_v2' not in params) or (params['stage_v2'] is None):
            raise ValueError(
                "Missing the required parameter `stage_v2` when calling `" + operation_name + "`")
        # verify the required parameter 'locale' is set
        if ('locale' not in params) or (params['locale'] is None):
            raise ValueError(
                "Missing the required parameter `locale` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stageV2}/interactionModel/locales/{locale}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage_v2' in params:
            path_params['stageV2'] = params['stage_v2']
        if 'locale' in params:
            path_params['locale'] = params['locale']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.interaction_model_data.InteractionModelData", status_code=200, message="Returns interaction model object on success"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The specified skill doesn&#39;t exist or there is no model defined for the locale."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.interaction_model.interaction_model_data.InteractionModelData")

        if full_response:
            return api_response
        return api_response.body

    def get_interaction_model_metadata_v1(self, skill_id, stage_v2, locale, **kwargs):
        # type: (str, str, str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Get the latest metadata for the interaction model resource for the given stage 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage_v2: (required) Stages of a skill including the new certified stage. * `development` - skills which are currently in development corresponds to this stage. * `certified` -  skills which have completed certification and ready for publishing corresponds to this stage. * `live` - skills which are currently live corresponds to this stage. 
        :type stage_v2: str
        :param locale: (required) The locale for the model requested e.g. en-GB, en-US, de-DE.
        :type locale: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "get_interaction_model_metadata_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage_v2' is set
        if ('stage_v2' not in params) or (params['stage_v2'] is None):
            raise ValueError(
                "Missing the required parameter `stage_v2` when calling `" + operation_name + "`")
        # verify the required parameter 'locale' is set
        if ('locale' not in params) or (params['locale'] is None):
            raise ValueError(
                "Missing the required parameter `locale` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stageV2}/interactionModel/locales/{locale}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage_v2' in params:
            path_params['stageV2'] = params['stage_v2']
        if 'locale' in params:
            path_params['locale'] = params['locale']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="success. There is no content but returns etag"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The specified skill or stage or locale does not exist"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="HEAD",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def set_interaction_model_v1(self, skill_id, stage_v2, locale, interaction_model, **kwargs):
        # type: (str, str, str, InteractionModelData, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Creates an `InteractionModel` for the skill. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage_v2: (required) Stages of a skill including the new certified stage. * `development` - skills which are currently in development corresponds to this stage. * `certified` -  skills which have completed certification and ready for publishing corresponds to this stage. * `live` - skills which are currently live corresponds to this stage. 
        :type stage_v2: str
        :param locale: (required) The locale for the model requested e.g. en-GB, en-US, de-DE.
        :type locale: str
        :param interaction_model: (required) 
        :type interaction_model: ask_smapi_model.v1.skill.interaction_model.interaction_model_data.InteractionModelData
        :param if_match: Request header that specified an entity tag. The server will update the resource only if the eTag matches with the resource's current eTag.
        :type if_match: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "set_interaction_model_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage_v2' is set
        if ('stage_v2' not in params) or (params['stage_v2'] is None):
            raise ValueError(
                "Missing the required parameter `stage_v2` when calling `" + operation_name + "`")
        # verify the required parameter 'locale' is set
        if ('locale' not in params) or (params['locale'] is None):
            raise ValueError(
                "Missing the required parameter `locale` when calling `" + operation_name + "`")
        # verify the required parameter 'interaction_model' is set
        if ('interaction_model' not in params) or (params['interaction_model'] is None):
            raise ValueError(
                "Missing the required parameter `interaction_model` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stageV2}/interactionModel/locales/{locale}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage_v2' in params:
            path_params['stageV2'] = params['stage_v2']
        if 'locale' in params:
            path_params['locale'] = params['locale']

        query_params = []  # type: List

        header_params = []  # type: List
        if 'if_match' in params:
            header_params.append(('If-Match', params['if_match']))

        body_params = None
        if 'interaction_model' in params:
            body_params = params['interaction_model']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=202, message="Returns build status location link on success."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error e.g. the input interaction model is invalid"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The specified skill or stage or locale does not exist"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=412, message="Precondition failed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="PUT",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def list_interaction_model_versions_v1(self, skill_id, stage_v2, locale, **kwargs):
        # type: (str, str, str, **Any) -> Union[ApiResponse, ListResponse, StandardizedError, BadRequestError]
        """
        Get the list of interactionModel versions of a skill for the vendor.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage_v2: (required) Stages of a skill including the new certified stage. * `development` - skills which are currently in development corresponds to this stage. * `certified` -  skills which have completed certification and ready for publishing corresponds to this stage. * `live` - skills which are currently live corresponds to this stage. 
        :type stage_v2: str
        :param locale: (required) The locale for the model requested e.g. en-GB, en-US, de-DE.
        :type locale: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: float
        :param sort_direction: Sets the sorting direction of the result items. When set to 'asc' these items are returned in ascending order of sortField value and when set to 'desc' these items are returned in descending order of sortField value.
        :type sort_direction: str
        :param sort_field: Sets the field on which the sorting would be applied.
        :type sort_field: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, ListResponse, StandardizedError, BadRequestError]
        """
        operation_name = "list_interaction_model_versions_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage_v2' is set
        if ('stage_v2' not in params) or (params['stage_v2'] is None):
            raise ValueError(
                "Missing the required parameter `stage_v2` when calling `" + operation_name + "`")
        # verify the required parameter 'locale' is set
        if ('locale' not in params) or (params['locale'] is None):
            raise ValueError(
                "Missing the required parameter `locale` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stageV2}/interactionModel/locales/{locale}/versions'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage_v2' in params:
            path_params['stageV2'] = params['stage_v2']
        if 'locale' in params:
            path_params['locale'] = params['locale']

        query_params = []  # type: List
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))
        if 'sort_direction' in params:
            query_params.append(('sortDirection', params['sort_direction']))
        if 'sort_field' in params:
            query_params.append(('sortField', params['sort_field']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.version.list_response.ListResponse", status_code=200, message="Returns list of interactionModel versions of a skill for the vendor."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error e.g. the input interaction model is invalid."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The specified skill doesn&#39;t exist or there is no model defined for the locale."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.interaction_model.version.list_response.ListResponse")

        if full_response:
            return api_response
        return api_response.body

    def get_interaction_model_version_v1(self, skill_id, stage_v2, locale, version, **kwargs):
        # type: (str, str, str, str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError, InteractionModelData]
        """
        Gets the specified version `InteractionModel` of a skill for the vendor. Use `~current` as version parameter to get the current version model. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage_v2: (required) Stages of a skill including the new certified stage. * `development` - skills which are currently in development corresponds to this stage. * `certified` -  skills which have completed certification and ready for publishing corresponds to this stage. * `live` - skills which are currently live corresponds to this stage. 
        :type stage_v2: str
        :param locale: (required) The locale for the model requested e.g. en-GB, en-US, de-DE.
        :type locale: str
        :param version: (required) Version for interaction model.
        :type version: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError, InteractionModelData]
        """
        operation_name = "get_interaction_model_version_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage_v2' is set
        if ('stage_v2' not in params) or (params['stage_v2'] is None):
            raise ValueError(
                "Missing the required parameter `stage_v2` when calling `" + operation_name + "`")
        # verify the required parameter 'locale' is set
        if ('locale' not in params) or (params['locale'] is None):
            raise ValueError(
                "Missing the required parameter `locale` when calling `" + operation_name + "`")
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError(
                "Missing the required parameter `version` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stageV2}/interactionModel/locales/{locale}/versions/{version}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage_v2' in params:
            path_params['stageV2'] = params['stage_v2']
        if 'locale' in params:
            path_params['locale'] = params['locale']
        if 'version' in params:
            path_params['version'] = params['version']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.interaction_model_data.InteractionModelData", status_code=200, message="Returns interaction model object on success."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error e.g. the input interaction model is invalid."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The specified skill doesn&#39;t exist or there is no model defined for the locale or version."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.interaction_model.interaction_model_data.InteractionModelData")

        if full_response:
            return api_response
        return api_response.body

    def get_skill_manifest_v1(self, skill_id, stage_v2, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError, SkillManifestEnvelope]
        """
        Returns the skill manifest for given skillId and stage.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage_v2: (required) Stages of a skill including the new certified stage. * `development` - skills which are currently in development corresponds to this stage. * `certified` -  skills which have completed certification and ready for publishing corresponds to this stage. * `live` - skills which are currently live corresponds to this stage. 
        :type stage_v2: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError, SkillManifestEnvelope]
        """
        operation_name = "get_skill_manifest_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage_v2' is set
        if ('stage_v2' not in params) or (params['stage_v2'] is None):
            raise ValueError(
                "Missing the required parameter `stage_v2` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stageV2}/manifest'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage_v2' in params:
            path_params['stageV2'] = params['stage_v2']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.manifest.skill_manifest_envelope.SkillManifestEnvelope", status_code=200, message="Response contains the latest version of skill manifest."))
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=303, message="See Other"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.manifest.skill_manifest_envelope.SkillManifestEnvelope")

        if full_response:
            return api_response
        return api_response.body

    def update_skill_manifest_v1(self, skill_id, stage_v2, update_skill_request, **kwargs):
        # type: (str, str, SkillManifestEnvelope, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Updates skill manifest for given skillId and stage.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage_v2: (required) Stages of a skill including the new certified stage. * `development` - skills which are currently in development corresponds to this stage. * `certified` -  skills which have completed certification and ready for publishing corresponds to this stage. * `live` - skills which are currently live corresponds to this stage. 
        :type stage_v2: str
        :param update_skill_request: (required) Defines the request body for updateSkill API.
        :type update_skill_request: ask_smapi_model.v1.skill.manifest.skill_manifest_envelope.SkillManifestEnvelope
        :param if_match: Request header that specified an entity tag. The server will update the resource only if the eTag matches with the resource's current eTag.
        :type if_match: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "update_skill_manifest_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage_v2' is set
        if ('stage_v2' not in params) or (params['stage_v2'] is None):
            raise ValueError(
                "Missing the required parameter `stage_v2` when calling `" + operation_name + "`")
        # verify the required parameter 'update_skill_request' is set
        if ('update_skill_request' not in params) or (params['update_skill_request'] is None):
            raise ValueError(
                "Missing the required parameter `update_skill_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stageV2}/manifest'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage_v2' in params:
            path_params['stageV2'] = params['stage_v2']

        query_params = []  # type: List

        header_params = []  # type: List
        if 'if_match' in params:
            header_params.append(('If-Match', params['if_match']))

        body_params = None
        if 'update_skill_request' in params:
            body_params = params['update_skill_request']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=202, message="Accepted; Returns a URL to track the status in &#39;Location&#39; header."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=409, message="The request could not be completed due to a conflict with the current state of the target resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=412, message="Precondition failed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="PUT",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def submit_skill_validation_v1(self, validations_api_request, skill_id, stage, **kwargs):
        # type: (ValidationsApiRequest, str, str, **Any) -> Union[ApiResponse, ValidationsApiResponse, Error, BadRequestError]
        """
        Validate a skill.
        This is an asynchronous API which allows a skill developer to execute various validations against their skill. 

        :param validations_api_request: (required) Payload sent to the skill validation API.
        :type validations_api_request: ask_smapi_model.v1.skill.validations.validations_api_request.ValidationsApiRequest
        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, ValidationsApiResponse, Error, BadRequestError]
        """
        operation_name = "submit_skill_validation_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'validations_api_request' is set
        if ('validations_api_request' not in params) or (params['validations_api_request'] is None):
            raise ValueError(
                "Missing the required parameter `validations_api_request` when calling `" + operation_name + "`")
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stage}/validations'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'validations_api_request' in params:
            body_params = params['validations_api_request']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.validations.validations_api_response.ValidationsApiResponse", status_code=202, message="Skill validation has successfully begun."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="API user does not have permission or is currently in a state that does not allow calls to this API. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The specified skill, stage or validation does not exist. The error response will contain a description that indicates the specific resource type that was not found. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=409, message="This requests conflicts with another one currently being processed. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="API user has exceeded the permitted request rate."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal service error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.validations.validations_api_response.ValidationsApiResponse")

        if full_response:
            return api_response
        return api_response.body

    def get_skill_validations_v1(self, skill_id, validation_id, stage, **kwargs):
        # type: (str, str, str, **Any) -> Union[ApiResponse, ValidationsApiResponse, Error, BadRequestError]
        """
        Get the result of a previously executed validation.
        This API gets the result of a previously executed validation. A successful response will contain the status of the executed validation. If the validation successfully completed, the response will also contain information related to executed validations. In cases where requests to this API results in an error, the response will contain a description of the problem. In cases where the validation failed, the response will contain a status attribute indicating that a failure occurred. Note that validation results are stored for 60 minutes. A request for an expired validation result will return a 404 HTTP status code. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param validation_id: (required) Id of the validation. Reserved word identifier of mostRecent can be used to get the most recent validation for the skill and stage. Note that the behavior of the API in this case would be the same as when the actual validation id of the most recent validation is used in the request. 
        :type validation_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param accept_language: User's locale/language in context.
        :type accept_language: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, ValidationsApiResponse, Error, BadRequestError]
        """
        operation_name = "get_skill_validations_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'validation_id' is set
        if ('validation_id' not in params) or (params['validation_id'] is None):
            raise ValueError(
                "Missing the required parameter `validation_id` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stage}/validations/{validationId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'validation_id' in params:
            path_params['validationId'] = params['validation_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']

        query_params = []  # type: List

        header_params = []  # type: List
        if 'accept_language' in params:
            header_params.append(('Accept-Language', params['accept_language']))

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.validations.validations_api_response.ValidationsApiResponse", status_code=200, message="Successfully retrieved skill validation information."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="API user does not have permission or is currently in a state that does not allow calls to this API. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The specified skill, stage, or validation does not exist. The error response will contain a description that indicates the specific resource type that was not found. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=409, message="This requests conflicts with another one currently being processed. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="API user has exceeded the permitted request rate."))
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=500, message="Internal service error."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.validations.validations_api_response.ValidationsApiResponse")

        if full_response:
            return api_response
        return api_response.body

    def get_skill_status_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError, SkillStatus]
        """
        Get the status of skill resource and its sub-resources for a given skillId.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param resource: Resource name for which status information is desired. It is an optional, filtering parameter and can be used more than once, to retrieve status for all the desired (sub)resources only, in single API call. If this parameter is not specified, status for all the resources/sub-resources will be returned. 
        :type resource: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError, SkillStatus]
        """
        operation_name = "get_skill_status_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/status'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List
        if 'resource' in params:
            query_params.append(('resource', params['resource']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.skill_status.SkillStatus", status_code=200, message="Returns status for skill resource and sub-resources."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.skill_status.SkillStatus")

        if full_response:
            return api_response
        return api_response.body

    def submit_skill_for_certification_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Submit the skill for certification. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param submit_skill_for_certification_request: Defines the request body for submitSkillForCertification API.
        :type submit_skill_for_certification_request: ask_smapi_model.v1.skill.submit_skill_for_certification_request.SubmitSkillForCertificationRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "submit_skill_for_certification_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/submit'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'submit_skill_for_certification_request' in params:
            body_params = params['submit_skill_for_certification_request']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=202, message="Success. There is no content but returns Location in the header."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def withdraw_skill_from_certification_v1(self, skill_id, withdraw_request, **kwargs):
        # type: (str, WithdrawRequest, **Any) -> Union[ApiResponse, StandardizedError, BadRequestError]
        """
        Withdraws the skill from certification. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param withdraw_request: (required) The reason and message (in case of OTHER) to withdraw a skill.
        :type withdraw_request: ask_smapi_model.v1.skill.withdraw_request.WithdrawRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, StandardizedError, BadRequestError]
        """
        operation_name = "withdraw_skill_from_certification_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'withdraw_request' is set
        if ('withdraw_request' not in params) or (params['withdraw_request'] is None):
            raise ValueError(
                "Missing the required parameter `withdraw_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/withdraw'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'withdraw_request' in params:
            body_params = params['withdraw_request']
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Success."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type=None)

        if full_response:
            return api_response
        

    def create_upload_url_v1(self, **kwargs):
        # type: (**Any) -> Union[ApiResponse, UploadResponse, StandardizedError]
        """
        Creates a new uploadUrl. 

        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, UploadResponse, StandardizedError]
        """
        operation_name = "create_upload_url_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/skills/uploads'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.upload_response.UploadResponse", status_code=201, message="Created."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceeds the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.upload_response.UploadResponse")

        if full_response:
            return api_response
        return api_response.body

    def get_vendor_list_v1(self, **kwargs):
        # type: (**Any) -> Union[ApiResponse, Vendors, Error]
        """
        Get the list of Vendor information. 

        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, Vendors, Error]
        """
        operation_name = "get_vendor_list_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']

        resource_path = '/v1/vendors'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.vendor_management.vendors.Vendors", status_code=200, message="Return vendor information on success."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.vendor_management.vendors.Vendors")

        if full_response:
            return api_response
        return api_response.body

    def get_alexa_hosted_skill_user_permissions_v1(self, vendor_id, permission, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, HostedSkillPermission, StandardizedError, BadRequestError]
        """
        Get the current user permissions about Alexa hosted skill features.

        :param vendor_id: (required) vendorId
        :type vendor_id: str
        :param permission: (required) The permission of a hosted skill feature that customer needs to check.
        :type permission: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, HostedSkillPermission, StandardizedError, BadRequestError]
        """
        operation_name = "get_alexa_hosted_skill_user_permissions_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vendor_id' is set
        if ('vendor_id' not in params) or (params['vendor_id'] is None):
            raise ValueError(
                "Missing the required parameter `vendor_id` when calling `" + operation_name + "`")
        # verify the required parameter 'permission' is set
        if ('permission' not in params) or (params['permission'] is None):
            raise ValueError(
                "Missing the required parameter `permission` when calling `" + operation_name + "`")

        resource_path = '/v1/vendors/{vendorId}/alexaHosted/permissions/{permission}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'vendor_id' in params:
            path_params['vendorId'] = params['vendor_id']
        if 'permission' in params:
            path_params['permission'] = params['permission']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.alexa_hosted.hosted_skill_permission.HostedSkillPermission", status_code=200, message="response contains the user&#39;s permission of hosted skill features"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error e.g. Authorization Url is invalid"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.alexa_hosted.hosted_skill_permission.HostedSkillPermission")

        if full_response:
            return api_response
        return api_response.body
