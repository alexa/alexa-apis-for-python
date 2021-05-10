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
from ask_sdk_model_runtime.utils import user_agent_info

from ask_sdk_model_runtime.authentication_configuration import AuthenticationConfiguration
from ask_sdk_model_runtime.lwa.lwa_client import LwaClient


if typing.TYPE_CHECKING:
    from typing import Dict, List, Union, Any
    from datetime import datetime
    from ask_smapi_model.v0.development_events.subscription.subscription_info import SubscriptionInfo as SubscriptionInfo_917bdab3
    from ask_smapi_model.v0.development_events.subscriber.list_subscribers_response import ListSubscribersResponse as ListSubscribersResponse_d1d01857
    from ask_smapi_model.v1.skill.asr.annotation_sets.create_asr_annotation_set_response import CreateAsrAnnotationSetResponse as CreateAsrAnnotationSetResponse_f4ef9811
    from ask_smapi_model.v1.skill.interaction_model.conflict_detection.get_conflicts_response import GetConflictsResponse as GetConflictsResponse_502eb394
    from ask_smapi_model.v1.skill.asr.annotation_sets.update_asr_annotation_set_properties_request_object import UpdateAsrAnnotationSetPropertiesRequestObject as UpdateAsrAnnotationSetPropertiesRequestObject_946da673
    from ask_smapi_model.v1.skill.alexa_hosted.hosted_skill_repository_credentials_list import HostedSkillRepositoryCredentialsList as HostedSkillRepositoryCredentialsList_d39d5fdf
    from ask_smapi_model.v1.skill.clone_locale_status_response import CloneLocaleStatusResponse as CloneLocaleStatusResponse_8b6e06ed
    from ask_smapi_model.v1.skill.interaction_model.catalog.catalog_status import CatalogStatus as CatalogStatus_c70ba222
    from ask_smapi_model.v1.skill.invocations.invoke_skill_request import InvokeSkillRequest as InvokeSkillRequest_8cf8aff9
    from ask_smapi_model.v1.skill.invocations.invoke_skill_response import InvokeSkillResponse as InvokeSkillResponse_6f32f451
    from ask_smapi_model.v1.skill.asr.annotation_sets.create_asr_annotation_set_request_object import CreateAsrAnnotationSetRequestObject as CreateAsrAnnotationSetRequestObject_c8c6238c
    from ask_smapi_model.v1.skill.list_skill_versions_response import ListSkillVersionsResponse as ListSkillVersionsResponse_7522147d
    from ask_smapi_model.v1.skill.validations.validations_api_response import ValidationsApiResponse as ValidationsApiResponse_aa0c51ca
    from ask_smapi_model.v1.skill.publication.skill_publication_response import SkillPublicationResponse as SkillPublicationResponse_8da9d720
    from ask_smapi_model.v2.skill.invocations.invocations_api_response import InvocationsApiResponse as InvocationsApiResponse_3d7e3234
    from ask_smapi_model.v1.skill.interaction_model.jobs.create_job_definition_response import CreateJobDefinitionResponse as CreateJobDefinitionResponse_efaa9a6f
    from ask_smapi_model.v1.skill.interaction_model.model_type.slot_type_definition_output import SlotTypeDefinitionOutput as SlotTypeDefinitionOutput_20e87f7
    from ask_smapi_model.v1.skill.interaction_model.type_version.list_slot_type_version_response import ListSlotTypeVersionResponse as ListSlotTypeVersionResponse_7d552abf
    from ask_smapi_model.v1.skill.interaction_model.version.list_response import ListResponse as ListResponse_cb936759
    from ask_smapi_model.v1.skill.interaction_model.jobs.create_job_definition_request import CreateJobDefinitionRequest as CreateJobDefinitionRequest_e3d4c41
    from ask_smapi_model.v1.skill.upload_response import UploadResponse as UploadResponse_5aa06857
    from ask_smapi_model.v1.skill.interaction_model.version.catalog_version_data import CatalogVersionData as CatalogVersionData_86156352
    from ask_smapi_model.v1.skill.alexa_hosted.hosted_skill_metadata import HostedSkillMetadata as HostedSkillMetadata_b8976dfb
    from ask_smapi_model.v1.skill.beta_test.test_body import TestBody as TestBody_65065c26
    from ask_smapi_model.v1.skill.manifest.skill_manifest_envelope import SkillManifestEnvelope as SkillManifestEnvelope_fc0e823b
    from ask_smapi_model.v0.development_events.subscription.create_subscription_request import CreateSubscriptionRequest as CreateSubscriptionRequest_1931508e
    from ask_smapi_model.v1.skill.skill_credentials import SkillCredentials as SkillCredentials_a0f29ab1
    from ask_smapi_model.v1.catalog.create_content_upload_url_response import CreateContentUploadUrlResponse as CreateContentUploadUrlResponse_4a18d03c
    from ask_smapi_model.v1.skill.interaction_model.catalog.catalog_response import CatalogResponse as CatalogResponse_2f6fe800
    from ask_smapi_model.v1.skill.asr.annotation_sets.list_asr_annotation_sets_response import ListASRAnnotationSetsResponse as ListASRAnnotationSetsResponse_a9a02e93
    from ask_smapi_model.v1.skill.asr.evaluations.post_asr_evaluations_response_object import PostAsrEvaluationsResponseObject as PostAsrEvaluationsResponseObject_1e0137c3
    from ask_smapi_model.v1.skill.history.intent_confidence_bin import IntentConfidenceBin as IntentConfidenceBin_4f7a62c8
    from ask_smapi_model.v1.skill.publication.publish_skill_request import PublishSkillRequest as PublishSkillRequest_efbc45c8
    from ask_smapi_model.v0.catalog.list_catalogs_response import ListCatalogsResponse as ListCatalogsResponse_3dd2a983
    from ask_smapi_model.v0.catalog.upload.list_uploads_response import ListUploadsResponse as ListUploadsResponse_59fc7728
    from ask_smapi_model.v1.skill.interaction_model.model_type.definition_data import DefinitionData as DefinitionData_dad4effb
    from ask_smapi_model.v1.skill.create_skill_with_package_request import CreateSkillWithPackageRequest as CreateSkillWithPackageRequest_cd7f22be
    from ask_smapi_model.v1.skill.interaction_model.type_version.slot_type_update import SlotTypeUpdate as SlotTypeUpdate_ae01835f
    from ask_smapi_model.v2.skill.invocations.invocations_api_request import InvocationsApiRequest as InvocationsApiRequest_a422fa08
    from ask_smapi_model.v1.smart_home_evaluation.list_sh_capability_evaluations_response import ListSHCapabilityEvaluationsResponse as ListSHCapabilityEvaluationsResponse_e6fe49d5
    from ask_smapi_model.v2.error import Error as Error_ea6c1a5a
    from ask_smapi_model.v1.isp.in_skill_product_summary_response import InSkillProductSummaryResponse as InSkillProductSummaryResponse_32ba64d7
    from ask_smapi_model.v0.bad_request_error import BadRequestError as BadRequestError_a8ac8b44
    from ask_smapi_model.v0.catalog.upload.create_content_upload_response import CreateContentUploadResponse as CreateContentUploadResponse_75cd6715
    from ask_smapi_model.v1.skill.simulations.simulations_api_request import SimulationsApiRequest as SimulationsApiRequest_606eed02
    from ask_smapi_model.v1.skill.history.dialog_act_name import DialogActName as DialogActName_df8326d6
    from ask_smapi_model.v1.skill.private.list_private_distribution_accounts_response import ListPrivateDistributionAccountsResponse as ListPrivateDistributionAccountsResponse_8783420d
    from ask_smapi_model.v1.skill.ssl_certificate_payload import SSLCertificatePayload as SSLCertificatePayload_97891902
    from ask_smapi_model.v1.skill.withdraw_request import WithdrawRequest as WithdrawRequest_d09390b7
    from ask_smapi_model.v1.isp.associated_skill_response import AssociatedSkillResponse as AssociatedSkillResponse_12067635
    from ask_smapi_model.v1.skill.asr.evaluations.get_asr_evaluation_status_response_object import GetAsrEvaluationStatusResponseObject as GetAsrEvaluationStatusResponseObject_f8b7f006
    from ask_smapi_model.v1.skill.alexa_hosted.hosted_skill_permission import HostedSkillPermission as HostedSkillPermission_eb71ebfb
    from ask_smapi_model.v1.skill.interaction_model.catalog.definition_data import DefinitionData as DefinitionData_ccdbb3c2
    from ask_smapi_model.v1.skill.interaction_model.model_type.update_request import UpdateRequest as UpdateRequest_43de537
    from ask_smapi_model.v1.skill.certification.list_certifications_response import ListCertificationsResponse as ListCertificationsResponse_f2a417c6
    from ask_smapi_model.v1.skill.import_response import ImportResponse as ImportResponse_364fa39f
    from ask_smapi_model.v1.skill.interaction_model.conflict_detection.get_conflict_detection_job_status_response import GetConflictDetectionJobStatusResponse as GetConflictDetectionJobStatusResponse_9e0e2cf1
    from ask_smapi_model.v1.skill.nlu.evaluations.list_nlu_evaluations_response import ListNLUEvaluationsResponse as ListNLUEvaluationsResponse_7ef8d08f
    from ask_smapi_model.v1.isp.create_in_skill_product_request import CreateInSkillProductRequest as CreateInSkillProductRequest_816cf44b
    from ask_smapi_model.v1.skill.asr.evaluations.post_asr_evaluations_request_object import PostAsrEvaluationsRequestObject as PostAsrEvaluationsRequestObject_133223f3
    from ask_smapi_model.v1.skill.interaction_model.type_version.slot_type_version_data import SlotTypeVersionData as SlotTypeVersionData_1f3ee474
    from ask_smapi_model.v1.skill.interaction_model.interaction_model_data import InteractionModelData as InteractionModelData_487fc9ea
    from ask_smapi_model.v1.skill.resource_schema.get_resource_schema_response import GetResourceSchemaResponse as GetResourceSchemaResponse_9df87651
    from ask_smapi_model.v1.skill.interaction_model.version.catalog_update import CatalogUpdate as CatalogUpdate_ef887f31
    from ask_smapi_model.v1.vendor_management.vendors import Vendors as Vendors_f5f1b90b
    from ask_smapi_model.v1.skill.beta_test.testers.list_testers_response import ListTestersResponse as ListTestersResponse_991ec8e9
    from ask_smapi_model.v1.skill.interaction_model.version.version_data import VersionData as VersionData_af79e8d3
    from ask_smapi_model.v1.skill.asr.evaluations.get_asr_evaluations_results_response import GetAsrEvaluationsResultsResponse as GetAsrEvaluationsResultsResponse_4f62e093
    from ask_smapi_model.v1.skill.beta_test.testers.testers_list import TestersList as TestersList_f8c0feda
    from ask_smapi_model.v1.skill.evaluations.profile_nlu_response import ProfileNluResponse as ProfileNluResponse_d24b74c1
    from ask_smapi_model.v1.smart_home_evaluation.get_sh_capability_evaluation_response import GetSHCapabilityEvaluationResponse as GetSHCapabilityEvaluationResponse_d484531f
    from ask_smapi_model.v1.skill.create_rollback_response import CreateRollbackResponse as CreateRollbackResponse_5a2e8250
    from ask_smapi_model.v1.smart_home_evaluation.get_sh_capability_evaluation_results_response import GetSHCapabilityEvaluationResultsResponse as GetSHCapabilityEvaluationResultsResponse_9a1d4db0
    from ask_smapi_model.v1.skill.history.publication_status import PublicationStatus as PublicationStatus_af1ce535
    from ask_smapi_model.v2.bad_request_error import BadRequestError as BadRequestError_765e0ac6
    from ask_smapi_model.v0.development_events.subscription.list_subscriptions_response import ListSubscriptionsResponse as ListSubscriptionsResponse_c033036c
    from ask_smapi_model.v1.smart_home_evaluation.list_sh_capability_test_plans_response import ListSHCapabilityTestPlansResponse as ListSHCapabilityTestPlansResponse_cb289d6
    from ask_smapi_model.v1.skill.standardized_error import StandardizedError as StandardizedError_f5106a89
    from ask_smapi_model.v1.skill.submit_skill_for_certification_request import SubmitSkillForCertificationRequest as SubmitSkillForCertificationRequest_1d77b7ee
    from ask_smapi_model.v2.skill.simulations.simulations_api_request import SimulationsApiRequest as SimulationsApiRequest_ae2e6503
    from ask_smapi_model.v1.skill.nlu.evaluations.evaluate_response import EvaluateResponse as EvaluateResponse_640ae5b5
    from ask_smapi_model.v0.development_events.subscription.update_subscription_request import UpdateSubscriptionRequest as UpdateSubscriptionRequest_71462c34
    from ask_smapi_model.v1.smart_home_evaluation.evaluate_sh_capability_request import EvaluateSHCapabilityRequest as EvaluateSHCapabilityRequest_2d391178
    from ask_smapi_model.v1.skill.create_skill_response import CreateSkillResponse as CreateSkillResponse_2bad1094
    from ask_smapi_model.v1.audit_logs.audit_logs_request import AuditLogsRequest as AuditLogsRequest_13316e3e
    from ask_smapi_model.v1.error import Error as Error_fbe913d9
    from ask_smapi_model.v1.skill.history.intent_requests import IntentRequests as IntentRequests_35db15c7
    from ask_smapi_model.v1.isp.update_in_skill_product_request import UpdateInSkillProductRequest as UpdateInSkillProductRequest_ee975cf1
    from ask_smapi_model.v1.skill.interaction_model.version.list_catalog_entity_versions_response import ListCatalogEntityVersionsResponse as ListCatalogEntityVersionsResponse_aa31060e
    from ask_smapi_model.v0.catalog.upload.get_content_upload_response import GetContentUploadResponse as GetContentUploadResponse_c8068011
    from ask_smapi_model.v1.skill.asr.annotation_sets.get_asr_annotation_sets_properties_response import GetASRAnnotationSetsPropertiesResponse as GetASRAnnotationSetsPropertiesResponse_1512206
    from ask_smapi_model.v1.smart_home_evaluation.evaluate_sh_capability_response import EvaluateSHCapabilityResponse as EvaluateSHCapabilityResponse_38ae7f22
    from ask_smapi_model.v1.catalog.upload.get_content_upload_response import GetContentUploadResponse as GetContentUploadResponse_b9580f92
    from ask_smapi_model.v1.skill.asr.annotation_sets.get_asr_annotation_set_annotations_response import GetAsrAnnotationSetAnnotationsResponse as GetAsrAnnotationSetAnnotationsResponse_e3efbdea
    from ask_smapi_model.v1.skill.simulations.simulations_api_response import SimulationsApiResponse as SimulationsApiResponse_328955bc
    from ask_smapi_model.v1.skill.clone_locale_request import CloneLocaleRequest as CloneLocaleRequest_2e00cdf4
    from ask_smapi_model.v1.skill.metrics.get_metric_data_response import GetMetricDataResponse as GetMetricDataResponse_722e44c4
    from ask_smapi_model.v1.skill.interaction_model.model_type.slot_type_status import SlotTypeStatus as SlotTypeStatus_a293ebfc
    from ask_smapi_model.v1.skill.interaction_model.type_version.version_data import VersionData as VersionData_faa770c8
    from ask_smapi_model.v1.skill.asr.evaluations.list_asr_evaluations_response import ListAsrEvaluationsResponse as ListAsrEvaluationsResponse_ef8cd586
    from ask_smapi_model.v1.isp.product_response import ProductResponse as ProductResponse_b388eec4
    from ask_smapi_model.v1.skill.alexa_hosted.hosted_skill_repository_credentials_request import HostedSkillRepositoryCredentialsRequest as HostedSkillRepositoryCredentialsRequest_79a1c791
    from ask_smapi_model.v1.skill.nlu.annotation_sets.get_nlu_annotation_set_properties_response import GetNLUAnnotationSetPropertiesResponse as GetNLUAnnotationSetPropertiesResponse_731f20d3
    from ask_smapi_model.v1.skill.nlu.annotation_sets.list_nlu_annotation_sets_response import ListNLUAnnotationSetsResponse as ListNLUAnnotationSetsResponse_5b1b0b6a
    from ask_smapi_model.v1.skill.account_linking.account_linking_response import AccountLinkingResponse as AccountLinkingResponse_b1f92882
    from ask_smapi_model.v1.skill.interaction_model.model_type.list_slot_type_response import ListSlotTypeResponse as ListSlotTypeResponse_b426c805
    from ask_smapi_model.v1.skill.evaluations.profile_nlu_request import ProfileNluRequest as ProfileNluRequest_501c0d87
    from ask_smapi_model.v1.skill.interaction_model.catalog.list_catalog_response import ListCatalogResponse as ListCatalogResponse_bc059ec9
    from ask_smapi_model.v1.skill.validations.validations_api_request import ValidationsApiRequest as ValidationsApiRequest_6f6e9aec
    import str
    from ask_smapi_model.v1.skill.interaction_model.jobs.validation_errors import ValidationErrors as ValidationErrors_d42055a1
    from ask_smapi_model.v1.skill.update_skill_with_package_request import UpdateSkillWithPackageRequest as UpdateSkillWithPackageRequest_d74ee124
    from ask_smapi_model.v1.skill.nlu.annotation_sets.create_nlu_annotation_set_response import CreateNLUAnnotationSetResponse as CreateNLUAnnotationSetResponse_b069cada
    from ask_smapi_model.v1.skill.interaction_model.jobs.list_job_definitions_response import ListJobDefinitionsResponse as ListJobDefinitionsResponse_72319c0d
    from ask_smapi_model.v1.isp.in_skill_product_definition_response import InSkillProductDefinitionResponse as InSkillProductDefinitionResponse_4aa468ff
    from ask_smapi_model.v2.skill.simulations.simulations_api_response import SimulationsApiResponse as SimulationsApiResponse_e4ad17d
    from ask_smapi_model.v1.skill.nlu.annotation_sets.update_nlu_annotation_set_properties_request import UpdateNLUAnnotationSetPropertiesRequest as UpdateNLUAnnotationSetPropertiesRequest_b569f485
    from ask_smapi_model.v0.development_events.subscriber.subscriber_info import SubscriberInfo as SubscriberInfo_854c325e
    from ask_smapi_model.v0.development_events.subscriber.update_subscriber_request import UpdateSubscriberRequest as UpdateSubscriberRequest_d5e3199f
    from ask_smapi_model.v1.skill.interaction_model.version.catalog_values import CatalogValues as CatalogValues_ef5c3823
    from ask_smapi_model.v1.skill.history.interaction_type import InteractionType as InteractionType_80494a05
    from ask_smapi_model.v1.skill.nlu.evaluations.evaluate_nlu_request import EvaluateNLURequest as EvaluateNLURequest_7a358f6a
    from ask_smapi_model.v1.isp.list_in_skill_product_response import ListInSkillProductResponse as ListInSkillProductResponse_505e7307
    from ask_smapi_model.v1.skill.interaction_model.jobs.update_job_status_request import UpdateJobStatusRequest as UpdateJobStatusRequest_f2d8379d
    from ask_smapi_model.v1.skill.account_linking.account_linking_request import AccountLinkingRequest as AccountLinkingRequest_cac174e
    from ask_smapi_model.v1.skill.asr.annotation_sets.update_asr_annotation_set_contents_payload import UpdateAsrAnnotationSetContentsPayload as UpdateAsrAnnotationSetContentsPayload_df3c6c8c
    from ask_smapi_model.v1.skill.beta_test.beta_test import BetaTest as BetaTest_e826b162
    from ask_smapi_model.v1.catalog.create_content_upload_url_request import CreateContentUploadUrlRequest as CreateContentUploadUrlRequest_4999fa1c
    from ask_smapi_model.v1.skill.skill_status import SkillStatus as SkillStatus_4fdd647b
    from ask_smapi_model.v0.development_events.subscriber.create_subscriber_request import CreateSubscriberRequest as CreateSubscriberRequest_a96d53b9
    from ask_smapi_model.v1.skill.rollback_request_status import RollbackRequestStatus as RollbackRequestStatus_71665366
    from ask_smapi_model.v0.catalog.create_catalog_request import CreateCatalogRequest as CreateCatalogRequest_f3cdf8bb
    from ask_smapi_model.v1.skill.interaction_model.catalog.update_request import UpdateRequest as UpdateRequest_12e0eebe
    from ask_smapi_model.v0.catalog.catalog_details import CatalogDetails as CatalogDetails_912693fa
    from ask_smapi_model.v1.skill.nlu.annotation_sets.create_nlu_annotation_set_request import CreateNLUAnnotationSetRequest as CreateNLUAnnotationSetRequest_16b1430c
    from ask_smapi_model.v1.skill.create_rollback_request import CreateRollbackRequest as CreateRollbackRequest_e7747a32
    from ask_smapi_model.v1.catalog.upload.catalog_upload_base import CatalogUploadBase as CatalogUploadBase_d7febd7
    from ask_smapi_model.v1.skill.certification.certification_response import CertificationResponse as CertificationResponse_97fdaad
    from ask_smapi_model.v1.skill.export_response import ExportResponse as ExportResponse_b235e7bd
    from ask_smapi_model.v0.catalog.upload.create_content_upload_request import CreateContentUploadRequest as CreateContentUploadRequest_bf7790d3
    from ask_smapi_model.v0.error import Error as Error_d660d58
    from ask_smapi_model.v1.skill.interaction_model.catalog.catalog_definition_output import CatalogDefinitionOutput as CatalogDefinitionOutput_21703cd9
    from ask_smapi_model.v0.catalog.upload.complete_upload_request import CompleteUploadRequest as CompleteUploadRequest_7b413950
    from ask_smapi_model.v1.skill.list_skill_response import ListSkillResponse as ListSkillResponse_527462d0
    from ask_smapi_model.v1.skill.nlu.annotation_sets.update_nlu_annotation_set_annotations_request import UpdateNLUAnnotationSetAnnotationsRequest as UpdateNLUAnnotationSetAnnotationsRequest_b336fe43
    from ask_smapi_model.v1.skill.interaction_model.jobs.job_definition import JobDefinition as JobDefinition_ee5db797
    from ask_smapi_model.v1.skill.nlu.evaluations.get_nlu_evaluation_response import GetNLUEvaluationResponse as GetNLUEvaluationResponse_2fb5e6ed
    from ask_smapi_model.v1.audit_logs.audit_logs_response import AuditLogsResponse as AuditLogsResponse_bbbe1918
    from ask_smapi_model.v1.skill.create_skill_request import CreateSkillRequest as CreateSkillRequest_92e74e84
    from ask_smapi_model.v1.skill.interaction_model.model_type.slot_type_response import SlotTypeResponse as SlotTypeResponse_1ca513dc
    from ask_smapi_model.v1.skill.nlu.evaluations.get_nlu_evaluation_results_response import GetNLUEvaluationResultsResponse as GetNLUEvaluationResultsResponse_5ca1fa54
    from ask_smapi_model.v1.skill.history.locale_in_query import LocaleInQuery as LocaleInQuery_6526a92e
    from ask_smapi_model.v1.skill.beta_test.update_beta_test_response import UpdateBetaTestResponse as UpdateBetaTestResponse_84abf38
    from ask_smapi_model.v1.skill.interaction_model.jobs.get_executions_response import GetExecutionsResponse as GetExecutionsResponse_1b1a1680
    from ask_smapi_model.v1.bad_request_error import BadRequestError as BadRequestError_f854b05


class SkillManagementServiceClient(BaseServiceClient):
    """ServiceClient for calling the SkillManagementService APIs.

    :param api_configuration: Instance of ApiConfiguration
    :type api_configuration: ask_sdk_model_runtime.api_configuration.ApiConfiguration
    """
    def __init__(self, api_configuration, authentication_configuration, lwa_client=None, custom_user_agent=None):
        # type: (ApiConfiguration, AuthenticationConfiguration, LwaClient, str) -> None
        """
        :param api_configuration: Instance of :py:class:`ask_sdk_model_runtime.api_configuration.ApiConfiguration`
        :type api_configuration: ask_sdk_model_runtime.api_configuration.ApiConfiguration
        :param authentication_configuration: Instance of :py:class:`ask_sdk_model_runtime.authentication_configuration.AuthenticationConfiguration`
        :type api_configuration: ask_sdk_model_runtime.authentication_configuration.AuthenticationConfiguration
        :param lwa_client: (Optional) Instance of :py:class:`ask_sdk_model_runtime.lwa.LwaClient`,
        can be passed when the LwaClient configuration is different from the authentication
        and api configuration passed
        :type lwa_client: ask_sdk_model_runtime.lwa.LwaClient
        :param custom_user_agent: Custom User Agent string provided by the developer.
        :type custom_user_agent: str
        """
        super(SkillManagementServiceClient, self).__init__(api_configuration)
        self.user_agent = user_agent_info(sdk_version="1.0.0", custom_user_agent=custom_user_agent)

        if lwa_client is None:
            self._lwa_service_client = LwaClient(
                api_configuration=ApiConfiguration(
                    serializer=api_configuration.serializer, 
                    api_client=api_configuration.api_client),
                authentication_configuration=authentication_configuration,
                grant_type='refresh_token')
        else:
            self._lwa_service_client = lwa_client

    def get_catalog_v0(self, catalog_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, BadRequestError_a8ac8b44, CatalogDetails_912693fa, Error_d660d58]
        """
        Returns information about a particular catalog.

        :param catalog_id: (required) Provides a unique identifier of the catalog.
        :type catalog_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, BadRequestError_a8ac8b44, CatalogDetails_912693fa, Error_d660d58]
        """
        operation_name = "get_catalog_v0"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params) or (params['catalog_id'] is None):
            raise ValueError(
                "Missing the required parameter `catalog_id` when calling `" + operation_name + "`")

        resource_path = '/v0/catalogs/{catalogId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.catalog.catalog_details.CatalogDetails", status_code=200, message="Successful operation."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v0.catalog.catalog_details.CatalogDetails")

        if full_response:
            return api_response
        return api_response.body
        

    def list_uploads_for_catalog_v0(self, catalog_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, BadRequestError_a8ac8b44, ListUploadsResponse_59fc7728, Error_d660d58]
        """
        Lists all the uploads for a particular catalog.

        :param catalog_id: (required) Provides a unique identifier of the catalog.
        :type catalog_id: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, BadRequestError_a8ac8b44, ListUploadsResponse_59fc7728, Error_d660d58]
        """
        operation_name = "list_uploads_for_catalog_v0"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params) or (params['catalog_id'] is None):
            raise ValueError(
                "Missing the required parameter `catalog_id` when calling `" + operation_name + "`")

        resource_path = '/v0/catalogs/{catalogId}/uploads'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']

        query_params = []  # type: List
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.catalog.upload.list_uploads_response.ListUploadsResponse", status_code=200, message="Successful operation."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v0.catalog.upload.list_uploads_response.ListUploadsResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def create_content_upload_v0(self, catalog_id, create_content_upload_request, **kwargs):
        # type: (str, CreateContentUploadRequest_bf7790d3, **Any) -> Union[ApiResponse, object, BadRequestError_a8ac8b44, CreateContentUploadResponse_75cd6715, Error_d660d58]
        """
        Creates a new upload for a catalog and returns presigned upload parts for uploading the file.

        :param catalog_id: (required) Provides a unique identifier of the catalog.
        :type catalog_id: str
        :param create_content_upload_request: (required) Defines the request body for updateCatalog API.
        :type create_content_upload_request: ask_smapi_model.v0.catalog.upload.create_content_upload_request.CreateContentUploadRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, BadRequestError_a8ac8b44, CreateContentUploadResponse_75cd6715, Error_d660d58]
        """
        operation_name = "create_content_upload_v0"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params) or (params['catalog_id'] is None):
            raise ValueError(
                "Missing the required parameter `catalog_id` when calling `" + operation_name + "`")
        # verify the required parameter 'create_content_upload_request' is set
        if ('create_content_upload_request' not in params) or (params['create_content_upload_request'] is None):
            raise ValueError(
                "Missing the required parameter `create_content_upload_request` when calling `" + operation_name + "`")

        resource_path = '/v0/catalogs/{catalogId}/uploads'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'create_content_upload_request' in params:
            body_params = params['create_content_upload_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.catalog.upload.create_content_upload_response.CreateContentUploadResponse", status_code=201, message="Content upload created."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v0.catalog.upload.create_content_upload_response.CreateContentUploadResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def get_content_upload_by_id_v0(self, catalog_id, upload_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, BadRequestError_a8ac8b44, Error_d660d58, GetContentUploadResponse_c8068011]
        """
        Gets detailed information about an upload which was created for a specific catalog. Includes the upload's ingestion steps and a presigned url for downloading the file.

        :param catalog_id: (required) Provides a unique identifier of the catalog.
        :type catalog_id: str
        :param upload_id: (required) Unique identifier of the upload.
        :type upload_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, BadRequestError_a8ac8b44, Error_d660d58, GetContentUploadResponse_c8068011]
        """
        operation_name = "get_content_upload_by_id_v0"
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

        resource_path = '/v0/catalogs/{catalogId}/uploads/{uploadId}'
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
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.catalog.upload.get_content_upload_response.GetContentUploadResponse", status_code=200, message="Successful operation."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v0.catalog.upload.get_content_upload_response.GetContentUploadResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def complete_catalog_upload_v0(self, catalog_id, upload_id, complete_upload_request_payload, **kwargs):
        # type: (str, str, CompleteUploadRequest_7b413950, **Any) -> Union[ApiResponse, object, BadRequestError_a8ac8b44, Error_d660d58]
        """
        Completes an upload. To be called after the file is uploaded to the backend data store using presigned url(s).

        :param catalog_id: (required) Provides a unique identifier of the catalog.
        :type catalog_id: str
        :param upload_id: (required) Unique identifier of the upload.
        :type upload_id: str
        :param complete_upload_request_payload: (required) Request payload to complete an upload.
        :type complete_upload_request_payload: ask_smapi_model.v0.catalog.upload.complete_upload_request.CompleteUploadRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, BadRequestError_a8ac8b44, Error_d660d58]
        """
        operation_name = "complete_catalog_upload_v0"
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
        # verify the required parameter 'complete_upload_request_payload' is set
        if ('complete_upload_request_payload' not in params) or (params['complete_upload_request_payload'] is None):
            raise ValueError(
                "Missing the required parameter `complete_upload_request_payload` when calling `" + operation_name + "`")

        resource_path = '/v0/catalogs/{catalogId}/uploads/{uploadId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']
        if 'upload_id' in params:
            path_params['uploadId'] = params['upload_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'complete_upload_request_payload' in params:
            body_params = params['complete_upload_request_payload']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

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
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=409, message="The request could not be completed due to a conflict with the current state of the target resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=503, message="Service Unavailable."))

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
        
        return None

    def list_catalogs_for_vendor_v0(self, vendor_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, ListCatalogsResponse_3dd2a983, BadRequestError_a8ac8b44, Error_d660d58]
        """
        Lists catalogs associated with a vendor.

        :param vendor_id: (required) The vendor ID.
        :type vendor_id: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: 
        :type max_results: int
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, ListCatalogsResponse_3dd2a983, BadRequestError_a8ac8b44, Error_d660d58]
        """
        operation_name = "list_catalogs_for_vendor_v0"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vendor_id' is set
        if ('vendor_id' not in params) or (params['vendor_id'] is None):
            raise ValueError(
                "Missing the required parameter `vendor_id` when calling `" + operation_name + "`")

        resource_path = '/v0/catalogs'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict

        query_params = []  # type: List
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))
        if 'vendor_id' in params:
            query_params.append(('vendorId', params['vendor_id']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.catalog.list_catalogs_response.ListCatalogsResponse", status_code=200, message="Successful operation."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v0.catalog.list_catalogs_response.ListCatalogsResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def create_catalog_v0(self, create_catalog_request, **kwargs):
        # type: (CreateCatalogRequest_f3cdf8bb, **Any) -> Union[ApiResponse, object, BadRequestError_a8ac8b44, CatalogDetails_912693fa, Error_d660d58]
        """
        Creates a new catalog based on information provided in the request.

        :param create_catalog_request: (required) Defines the request body for createCatalog API.
        :type create_catalog_request: ask_smapi_model.v0.catalog.create_catalog_request.CreateCatalogRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, BadRequestError_a8ac8b44, CatalogDetails_912693fa, Error_d660d58]
        """
        operation_name = "create_catalog_v0"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_catalog_request' is set
        if ('create_catalog_request' not in params) or (params['create_catalog_request'] is None):
            raise ValueError(
                "Missing the required parameter `create_catalog_request` when calling `" + operation_name + "`")

        resource_path = '/v0/catalogs'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'create_catalog_request' in params:
            body_params = params['create_catalog_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.catalog.catalog_details.CatalogDetails", status_code=201, message="Catalog created."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v0.catalog.catalog_details.CatalogDetails")

        if full_response:
            return api_response
        return api_response.body
        

    def list_subscribers_for_development_events_v0(self, vendor_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, ListSubscribersResponse_d1d01857, BadRequestError_a8ac8b44, Error_d660d58]
        """
        Lists the subscribers for a particular vendor.

        :param vendor_id: (required) The vendor ID.
        :type vendor_id: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, ListSubscribersResponse_d1d01857, BadRequestError_a8ac8b44, Error_d660d58]
        """
        operation_name = "list_subscribers_for_development_events_v0"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vendor_id' is set
        if ('vendor_id' not in params) or (params['vendor_id'] is None):
            raise ValueError(
                "Missing the required parameter `vendor_id` when calling `" + operation_name + "`")

        resource_path = '/v0/developmentEvents/subscribers'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict

        query_params = []  # type: List
        if 'vendor_id' in params:
            query_params.append(('vendorId', params['vendor_id']))
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.development_events.subscriber.list_subscribers_response.ListSubscribersResponse", status_code=200, message="Successful operation."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v0.development_events.subscriber.list_subscribers_response.ListSubscribersResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def create_subscriber_for_development_events_v0(self, create_subscriber_request, **kwargs):
        # type: (CreateSubscriberRequest_a96d53b9, **Any) -> Union[ApiResponse, object, BadRequestError_a8ac8b44, Error_d660d58]
        """
        Creates a new subscriber resource for a vendor.

        :param create_subscriber_request: (required) Defines the request body for createSubscriber API.
        :type create_subscriber_request: ask_smapi_model.v0.development_events.subscriber.create_subscriber_request.CreateSubscriberRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, BadRequestError_a8ac8b44, Error_d660d58]
        """
        operation_name = "create_subscriber_for_development_events_v0"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_subscriber_request' is set
        if ('create_subscriber_request' not in params) or (params['create_subscriber_request'] is None):
            raise ValueError(
                "Missing the required parameter `create_subscriber_request` when calling `" + operation_name + "`")

        resource_path = '/v0/developmentEvents/subscribers'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'create_subscriber_request' in params:
            body_params = params['create_subscriber_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=201, message="Created. Returns a URL to retrieve the subscriber in &#39;Location&#39; header."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=503, message="Service Unavailable."))

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
        
        return None

    def delete_subscriber_for_development_events_v0(self, subscriber_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, BadRequestError_a8ac8b44, Error_d660d58]
        """
        Deletes a specified subscriber.

        :param subscriber_id: (required) Unique identifier of the subscriber.
        :type subscriber_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, BadRequestError_a8ac8b44, Error_d660d58]
        """
        operation_name = "delete_subscriber_for_development_events_v0"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscriber_id' is set
        if ('subscriber_id' not in params) or (params['subscriber_id'] is None):
            raise ValueError(
                "Missing the required parameter `subscriber_id` when calling `" + operation_name + "`")

        resource_path = '/v0/developmentEvents/subscribers/{subscriberId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'subscriber_id' in params:
            path_params['subscriberId'] = params['subscriber_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Successful operation."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=503, message="Service Unavailable."))

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
        
        return None

    def get_subscriber_for_development_events_v0(self, subscriber_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, SubscriberInfo_854c325e, BadRequestError_a8ac8b44, Error_d660d58]
        """
        Returns information about specified subscriber.

        :param subscriber_id: (required) Unique identifier of the subscriber.
        :type subscriber_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, SubscriberInfo_854c325e, BadRequestError_a8ac8b44, Error_d660d58]
        """
        operation_name = "get_subscriber_for_development_events_v0"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscriber_id' is set
        if ('subscriber_id' not in params) or (params['subscriber_id'] is None):
            raise ValueError(
                "Missing the required parameter `subscriber_id` when calling `" + operation_name + "`")

        resource_path = '/v0/developmentEvents/subscribers/{subscriberId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'subscriber_id' in params:
            path_params['subscriberId'] = params['subscriber_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.development_events.subscriber.subscriber_info.SubscriberInfo", status_code=200, message="Successful operation."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v0.development_events.subscriber.subscriber_info.SubscriberInfo")

        if full_response:
            return api_response
        return api_response.body
        

    def set_subscriber_for_development_events_v0(self, subscriber_id, update_subscriber_request, **kwargs):
        # type: (str, UpdateSubscriberRequest_d5e3199f, **Any) -> Union[ApiResponse, object, BadRequestError_a8ac8b44, Error_d660d58]
        """
        Updates the properties of a subscriber.

        :param subscriber_id: (required) Unique identifier of the subscriber.
        :type subscriber_id: str
        :param update_subscriber_request: (required) Defines the request body for updateSubscriber API.
        :type update_subscriber_request: ask_smapi_model.v0.development_events.subscriber.update_subscriber_request.UpdateSubscriberRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, BadRequestError_a8ac8b44, Error_d660d58]
        """
        operation_name = "set_subscriber_for_development_events_v0"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscriber_id' is set
        if ('subscriber_id' not in params) or (params['subscriber_id'] is None):
            raise ValueError(
                "Missing the required parameter `subscriber_id` when calling `" + operation_name + "`")
        # verify the required parameter 'update_subscriber_request' is set
        if ('update_subscriber_request' not in params) or (params['update_subscriber_request'] is None):
            raise ValueError(
                "Missing the required parameter `update_subscriber_request` when calling `" + operation_name + "`")

        resource_path = '/v0/developmentEvents/subscribers/{subscriberId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'subscriber_id' in params:
            path_params['subscriberId'] = params['subscriber_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'update_subscriber_request' in params:
            body_params = params['update_subscriber_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

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
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=503, message="Service Unavailable."))

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
        
        return None

    def list_subscriptions_for_development_events_v0(self, vendor_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, BadRequestError_a8ac8b44, ListSubscriptionsResponse_c033036c, Error_d660d58]
        """
        Lists all the subscriptions for a vendor/subscriber depending on the query parameter.

        :param vendor_id: (required) The vendor ID.
        :type vendor_id: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param subscriber_id: Unique identifier of the subscriber. If this query parameter is provided, the list would be filtered by the owning subscriberId.
        :type subscriber_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, BadRequestError_a8ac8b44, ListSubscriptionsResponse_c033036c, Error_d660d58]
        """
        operation_name = "list_subscriptions_for_development_events_v0"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vendor_id' is set
        if ('vendor_id' not in params) or (params['vendor_id'] is None):
            raise ValueError(
                "Missing the required parameter `vendor_id` when calling `" + operation_name + "`")

        resource_path = '/v0/developmentEvents/subscriptions'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict

        query_params = []  # type: List
        if 'vendor_id' in params:
            query_params.append(('vendorId', params['vendor_id']))
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))
        if 'subscriber_id' in params:
            query_params.append(('subscriberId', params['subscriber_id']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.development_events.subscription.list_subscriptions_response.ListSubscriptionsResponse", status_code=200, message="Successful operation."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v0.development_events.subscription.list_subscriptions_response.ListSubscriptionsResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def create_subscription_for_development_events_v0(self, **kwargs):
        # type: (**Any) -> Union[ApiResponse, object, BadRequestError_a8ac8b44, Error_d660d58]
        """
        Creates a new subscription for a subscriber. This needs to be authorized by the client/vendor who created the subscriber and the vendor who publishes the event.

        :param create_subscription_request: Request body for createSubscription API.
        :type create_subscription_request: ask_smapi_model.v0.development_events.subscription.create_subscription_request.CreateSubscriptionRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, BadRequestError_a8ac8b44, Error_d660d58]
        """
        operation_name = "create_subscription_for_development_events_v0"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']

        resource_path = '/v0/developmentEvents/subscriptions'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'create_subscription_request' in params:
            body_params = params['create_subscription_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=201, message="Created; Returns a URL to retrieve the subscription in &#39;Location&#39; header."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=503, message="Service Unavailable."))

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
        
        return None

    def delete_subscription_for_development_events_v0(self, subscription_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, BadRequestError_a8ac8b44, Error_d660d58]
        """
        Deletes a particular subscription. Both, the vendor who created the subscriber and the vendor who publishes the event can delete this resource with appropriate authorization.

        :param subscription_id: (required) Unique identifier of the subscription.
        :type subscription_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, BadRequestError_a8ac8b44, Error_d660d58]
        """
        operation_name = "delete_subscription_for_development_events_v0"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params) or (params['subscription_id'] is None):
            raise ValueError(
                "Missing the required parameter `subscription_id` when calling `" + operation_name + "`")

        resource_path = '/v0/developmentEvents/subscriptions/{subscriptionId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'subscription_id' in params:
            path_params['subscriptionId'] = params['subscription_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Successful operation."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=503, message="Service Unavailable."))

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
        
        return None

    def get_subscription_for_development_events_v0(self, subscription_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, BadRequestError_a8ac8b44, SubscriptionInfo_917bdab3, Error_d660d58]
        """
        Returns information about a particular subscription. Both, the vendor who created the subscriber and the vendor who publishes the event can retrieve this resource with appropriate authorization.

        :param subscription_id: (required) Unique identifier of the subscription.
        :type subscription_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, BadRequestError_a8ac8b44, SubscriptionInfo_917bdab3, Error_d660d58]
        """
        operation_name = "get_subscription_for_development_events_v0"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params) or (params['subscription_id'] is None):
            raise ValueError(
                "Missing the required parameter `subscription_id` when calling `" + operation_name + "`")

        resource_path = '/v0/developmentEvents/subscriptions/{subscriptionId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'subscription_id' in params:
            path_params['subscriptionId'] = params['subscription_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.development_events.subscription.subscription_info.SubscriptionInfo", status_code=200, message="Successful operation."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v0.development_events.subscription.subscription_info.SubscriptionInfo")

        if full_response:
            return api_response
        return api_response.body
        

    def set_subscription_for_development_events_v0(self, subscription_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, BadRequestError_a8ac8b44, Error_d660d58]
        """
        Updates the mutable properties of a subscription. This needs to be authorized by the client/vendor who created the subscriber and the vendor who publishes the event. The subscriberId cannot be updated.

        :param subscription_id: (required) Unique identifier of the subscription.
        :type subscription_id: str
        :param update_subscription_request: Request body for updateSubscription API.
        :type update_subscription_request: ask_smapi_model.v0.development_events.subscription.update_subscription_request.UpdateSubscriptionRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, BadRequestError_a8ac8b44, Error_d660d58]
        """
        operation_name = "set_subscription_for_development_events_v0"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params) or (params['subscription_id'] is None):
            raise ValueError(
                "Missing the required parameter `subscription_id` when calling `" + operation_name + "`")

        resource_path = '/v0/developmentEvents/subscriptions/{subscriptionId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'subscription_id' in params:
            path_params['subscriptionId'] = params['subscription_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'update_subscription_request' in params:
            body_params = params['update_subscription_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="No content."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=503, message="Service Unavailable."))

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
        
        return None

    def associate_catalog_with_skill_v0(self, skill_id, catalog_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, BadRequestError_a8ac8b44, Error_d660d58]
        """
        Associate skill with catalog.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param catalog_id: (required) Provides a unique identifier of the catalog.
        :type catalog_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, BadRequestError_a8ac8b44, Error_d660d58]
        """
        operation_name = "associate_catalog_with_skill_v0"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params) or (params['catalog_id'] is None):
            raise ValueError(
                "Missing the required parameter `catalog_id` when calling `" + operation_name + "`")

        resource_path = '/v0/skills/{skillId}/catalogs/{catalogId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=201, message="Successful operation."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=503, message="Service Unavailable."))

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
        
        return None

    def list_catalogs_for_skill_v0(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, ListCatalogsResponse_3dd2a983, BadRequestError_a8ac8b44, Error_d660d58]
        """
        Lists all the catalogs associated with a skill.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: 
        :type max_results: int
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, ListCatalogsResponse_3dd2a983, BadRequestError_a8ac8b44, Error_d660d58]
        """
        operation_name = "list_catalogs_for_skill_v0"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v0/skills/{skillId}/catalogs'
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
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.catalog.list_catalogs_response.ListCatalogsResponse", status_code=200, message="Successful operation."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=500, message="Internal Server Error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v0.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v0.catalog.list_catalogs_response.ListCatalogsResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def create_catalog_upload_v1(self, catalog_id, catalog_upload_request_body, **kwargs):
        # type: (str, CatalogUploadBase_d7febd7, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        Create new upload
        Creates a new upload for a catalog and returns location to track the upload process.

        :param catalog_id: (required) Provides a unique identifier of the catalog.
        :type catalog_id: str
        :param catalog_upload_request_body: (required) Provides the request body for create content upload
        :type catalog_upload_request_body: ask_smapi_model.v1.catalog.upload.catalog_upload_base.CatalogUploadBase
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def get_content_upload_by_id_v1(self, catalog_id, upload_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, GetContentUploadResponse_b9580f92]
        """
        Get upload
        Gets detailed information about an upload which was created for a specific catalog. Includes the upload's ingestion steps and a url for downloading the file.

        :param catalog_id: (required) Provides a unique identifier of the catalog.
        :type catalog_id: str
        :param upload_id: (required) Unique identifier of the upload.
        :type upload_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, GetContentUploadResponse_b9580f92]
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
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.catalog.upload.get_content_upload_response.GetContentUploadResponse", status_code=200, message="Successful operation."))
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
        # type: (str, CreateContentUploadUrlRequest_4999fa1c, **Any) -> Union[ApiResponse, object, Error_fbe913d9, CreateContentUploadUrlResponse_4a18d03c, BadRequestError_f854b05]
        """
        Generates preSigned urls to upload data

        :param catalog_id: (required) Provides a unique identifier of the catalog.
        :type catalog_id: str
        :param generate_catalog_upload_url_request_body: (required) Request body to generate catalog upload url
        :type generate_catalog_upload_url_request_body: ask_smapi_model.v1.catalog.create_content_upload_url_request.CreateContentUploadUrlRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, CreateContentUploadUrlResponse_4a18d03c, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        

    def query_development_audit_logs_v1(self, get_audit_logs_request, **kwargs):
        # type: (AuditLogsRequest_13316e3e, **Any) -> Union[ApiResponse, object, Error_fbe913d9, AuditLogsResponse_bbbe1918, BadRequestError_f854b05]
        """
        The SMAPI Audit Logs API provides customers with an audit history of all SMAPI calls made by a developer or developers with permissions on that account.

        :param get_audit_logs_request: (required) Request object encompassing vendorId, optional request filters and optional pagination context.
        :type get_audit_logs_request: ask_smapi_model.v1.audit_logs.audit_logs_request.AuditLogsRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, AuditLogsResponse_bbbe1918, BadRequestError_f854b05]
        """
        operation_name = "query_development_audit_logs_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'get_audit_logs_request' is set
        if ('get_audit_logs_request' not in params) or (params['get_audit_logs_request'] is None):
            raise ValueError(
                "Missing the required parameter `get_audit_logs_request` when calling `" + operation_name + "`")

        resource_path = '/v1/developmentAuditLogs/query'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'get_audit_logs_request' in params:
            body_params = params['get_audit_logs_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.audit_logs.audit_logs_response.AuditLogsResponse", status_code=200, message="Returns a list of audit logs for the given vendor."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Invalid request"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="Unauthorized"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=403, message="Forbidden"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="Not Found"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Too Many Requests"))
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
            response_type="ask_smapi_model.v1.audit_logs.audit_logs_response.AuditLogsResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def get_isp_list_for_vendor_v1(self, vendor_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, ListInSkillProductResponse_505e7307]
        """
        Get the list of in-skill products for the vendor.

        :param vendor_id: (required) The vendor ID.
        :type vendor_id: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
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
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, ListInSkillProductResponse_505e7307]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (CreateInSkillProductRequest_816cf44b, **Any) -> Union[ApiResponse, object, Error_fbe913d9, ProductResponse_b388eec4, BadRequestError_f854b05]
        """
        Creates a new in-skill product for given vendorId.

        :param create_in_skill_product_request: (required) defines the request body for createInSkillProduct API.
        :type create_in_skill_product_request: ask_smapi_model.v1.isp.create_in_skill_product_request.CreateInSkillProductRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, ProductResponse_b388eec4, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        Disassociates an in-skill product from a skill.

        :param product_id: (required) The in-skill product ID.
        :type product_id: str
        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def associate_isp_with_skill_v1(self, product_id, skill_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        Associates an in-skill product with a skill.

        :param product_id: (required) The in-skill product ID.
        :type product_id: str
        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def delete_isp_for_product_v1(self, product_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def reset_entitlement_for_product_v1(self, product_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        Resets the entitlement(s) of the Product for the current user.

        :param product_id: (required) The in-skill product ID.
        :type product_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def get_isp_definition_v1(self, product_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, InSkillProductDefinitionResponse_4aa468ff, Error_fbe913d9, BadRequestError_f854b05]
        """
        Returns the in-skill product definition for given productId.

        :param product_id: (required) The in-skill product ID.
        :type product_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, InSkillProductDefinitionResponse_4aa468ff, Error_fbe913d9, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (str, str, UpdateInSkillProductRequest_ee975cf1, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def get_isp_associated_skills_v1(self, product_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, AssociatedSkillResponse_12067635, Error_fbe913d9, BadRequestError_f854b05]
        """
        Get the associated skills for the in-skill product.

        :param product_id: (required) The in-skill product ID.
        :type product_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, AssociatedSkillResponse_12067635, Error_fbe913d9, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
            response_type="ask_smapi_model.v1.isp.associated_skill_response.AssociatedSkillResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def get_isp_summary_v1(self, product_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, InSkillProductSummaryResponse_32ba64d7]
        """
        Get the summary information for an in-skill product.

        :param product_id: (required) The in-skill product ID.
        :type product_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, InSkillProductSummaryResponse_32ba64d7]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Delete the catalog. 

        :param catalog_id: (required) Provides a unique identifier of the catalog.
        :type catalog_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def get_interaction_model_catalog_definition_v1(self, catalog_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, CatalogDefinitionOutput_21703cd9]
        """
        get the catalog definition 

        :param catalog_id: (required) Provides a unique identifier of the catalog.
        :type catalog_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, CatalogDefinitionOutput_21703cd9]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (str, UpdateRequest_12e0eebe, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        update description and vendorGuidance string for certain version of a catalog. 

        :param catalog_id: (required) Provides a unique identifier of the catalog.
        :type catalog_id: str
        :param update_request: (required) 
        :type update_request: ask_smapi_model.v1.skill.interaction_model.catalog.update_request.UpdateRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def get_interaction_model_catalog_update_status_v1(self, catalog_id, update_request_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, CatalogStatus_c70ba222]
        """
        Get the status of catalog resource and its sub-resources for a given catalogId. 

        :param catalog_id: (required) Provides a unique identifier of the catalog.
        :type catalog_id: str
        :param update_request_id: (required) The identifier for slotType version creation process
        :type update_request_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, CatalogStatus_c70ba222]
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
        header_params.append(('User-Agent', self.user_agent))

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
        

    def list_interaction_model_catalog_versions_v1(self, catalog_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, ListCatalogEntityVersionsResponse_aa31060e, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        List all the historical versions of the given catalogId.

        :param catalog_id: (required) Provides a unique identifier of the catalog.
        :type catalog_id: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param sort_direction: Sets the sorting direction of the result items. When set to 'asc' these items are returned in ascending order of sortField value and when set to 'desc' these items are returned in descending order of sortField value.
        :type sort_direction: str
        :param sort_field: Sets the field on which the sorting would be applied.
        :type sort_field: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, ListCatalogEntityVersionsResponse_aa31060e, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        operation_name = "list_interaction_model_catalog_versions_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'catalog_id' is set
        if ('catalog_id' not in params) or (params['catalog_id'] is None):
            raise ValueError(
                "Missing the required parameter `catalog_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/catalogs/{catalogId}/versions'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'catalog_id' in params:
            path_params['catalogId'] = params['catalog_id']

        query_params = []  # type: List
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'sort_direction' in params:
            query_params.append(('sortDirection', params['sort_direction']))
        if 'sort_field' in params:
            query_params.append(('sortField', params['sort_field']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.version.list_catalog_entity_versions_response.ListCatalogEntityVersionsResponse", status_code=200, message="Returns list of catalogs for the vendor."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error e.g. the catalog definition is invalid."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The specified catalog does not exist."))
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
            response_type="ask_smapi_model.v1.skill.interaction_model.version.list_catalog_entity_versions_response.ListCatalogEntityVersionsResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def create_interaction_model_catalog_version_v1(self, catalog_id, catalog, **kwargs):
        # type: (str, VersionData_af79e8d3, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Create a new version of catalog entity for the given catalogId. 

        :param catalog_id: (required) Provides a unique identifier of the catalog.
        :type catalog_id: str
        :param catalog: (required) 
        :type catalog: ask_smapi_model.v1.skill.interaction_model.version.version_data.VersionData
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def delete_interaction_model_catalog_version_v1(self, catalog_id, version, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Delete catalog version. 

        :param catalog_id: (required) Provides a unique identifier of the catalog.
        :type catalog_id: str
        :param version: (required) Version for interaction model.
        :type version: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def get_interaction_model_catalog_version_v1(self, catalog_id, version, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, CatalogVersionData_86156352]
        """
        Get catalog version data of given catalog version. 

        :param catalog_id: (required) Provides a unique identifier of the catalog.
        :type catalog_id: str
        :param version: (required) Version for interaction model.
        :type version: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, CatalogVersionData_86156352]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Update description and vendorGuidance string for certain version of a catalog. 

        :param catalog_id: (required) Provides a unique identifier of the catalog.
        :type catalog_id: str
        :param version: (required) Version for interaction model.
        :type version: str
        :param catalog_update: 
        :type catalog_update: ask_smapi_model.v1.skill.interaction_model.version.catalog_update.CatalogUpdate
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def get_interaction_model_catalog_values_v1(self, catalog_id, version, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, CatalogValues_ef5c3823, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Get catalog values from the given catalogId & version. 

        :param catalog_id: (required) Provides a unique identifier of the catalog.
        :type catalog_id: str
        :param version: (required) Version for interaction model.
        :type version: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, CatalogValues_ef5c3823, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, ListCatalogResponse_bc059ec9]
        """
        List all catalogs for the vendor. 

        :param vendor_id: (required) The vendor ID.
        :type vendor_id: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param sort_direction: Sets the sorting direction of the result items. When set to 'asc' these items are returned in ascending order of sortField value and when set to 'desc' these items are returned in descending order of sortField value.
        :type sort_direction: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, ListCatalogResponse_bc059ec9]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (DefinitionData_ccdbb3c2, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, CatalogResponse_2f6fe800]
        """
        Create a new version of catalog within the given catalogId. 

        :param catalog: (required) 
        :type catalog: ask_smapi_model.v1.skill.interaction_model.catalog.definition_data.DefinitionData
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, CatalogResponse_2f6fe800]
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
        header_params.append(('User-Agent', self.user_agent))

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
        

    def list_job_definitions_for_interaction_model_v1(self, vendor_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, ListJobDefinitionsResponse_72319c0d]
        """
        Retrieve a list of jobs associated with the vendor.

        :param vendor_id: (required) The vendor ID.
        :type vendor_id: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, ListJobDefinitionsResponse_72319c0d]
        """
        operation_name = "list_job_definitions_for_interaction_model_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vendor_id' is set
        if ('vendor_id' not in params) or (params['vendor_id'] is None):
            raise ValueError(
                "Missing the required parameter `vendor_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/jobs'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict

        query_params = []  # type: List
        if 'vendor_id' in params:
            query_params.append(('vendorId', params['vendor_id']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.jobs.list_job_definitions_response.ListJobDefinitionsResponse", status_code=200, message="List of all jobs associated with the vendor."))
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
            response_type="ask_smapi_model.v1.skill.interaction_model.jobs.list_job_definitions_response.ListJobDefinitionsResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def delete_job_definition_for_interaction_model_v1(self, job_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, ValidationErrors_d42055a1]
        """
        Delete the job definition for a given jobId.

        :param job_id: (required) The identifier for dynamic jobs.
        :type job_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, ValidationErrors_d42055a1]
        """
        operation_name = "delete_job_definition_for_interaction_model_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError(
                "Missing the required parameter `job_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/jobs/{jobId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="No content, confirms the resource is updated."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.jobs.validation_errors.ValidationErrors", status_code=400, message="Server cannot process the request due to a client error."))
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
        
        return None

    def cancel_next_job_execution_for_interaction_model_v1(self, job_id, execution_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, ValidationErrors_d42055a1]
        """
        Cancel the next execution for the given job.

        :param job_id: (required) The identifier for dynamic jobs.
        :type job_id: str
        :param execution_id: (required) The identifier for dynamic job executions. Currently only allowed for scheduled executions.
        :type execution_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, ValidationErrors_d42055a1]
        """
        operation_name = "cancel_next_job_execution_for_interaction_model_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError(
                "Missing the required parameter `job_id` when calling `" + operation_name + "`")
        # verify the required parameter 'execution_id' is set
        if ('execution_id' not in params) or (params['execution_id'] is None):
            raise ValueError(
                "Missing the required parameter `execution_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/jobs/{jobId}/executions/{executionId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']
        if 'execution_id' in params:
            path_params['executionId'] = params['execution_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="No Content; Confirms that the next execution is canceled."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.jobs.validation_errors.ValidationErrors", status_code=400, message="Server cannot process the request due to a client error."))
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
        
        return None

    def list_job_executions_for_interaction_model_v1(self, job_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, GetExecutionsResponse_1b1a1680, BadRequestError_f854b05]
        """
        List the execution history associated with the job definition, with default sortField to be the executions' timestamp.

        :param job_id: (required) The identifier for dynamic jobs.
        :type job_id: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param sort_direction: Sets the sorting direction of the result items. When set to 'asc' these items are returned in ascending order of sortField value and when set to 'desc' these items are returned in descending order of sortField value.
        :type sort_direction: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, GetExecutionsResponse_1b1a1680, BadRequestError_f854b05]
        """
        operation_name = "list_job_executions_for_interaction_model_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError(
                "Missing the required parameter `job_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/jobs/{jobId}/executions'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = []  # type: List
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'sort_direction' in params:
            query_params.append(('sortDirection', params['sort_direction']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.jobs.get_executions_response.GetExecutionsResponse", status_code=200, message="Retrun list of executions associated with the job definition."))
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
            response_type="ask_smapi_model.v1.skill.interaction_model.jobs.get_executions_response.GetExecutionsResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def get_job_definition_for_interaction_model_v1(self, job_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, JobDefinition_ee5db797, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Get the job definition for a given jobId. 

        :param job_id: (required) The identifier for dynamic jobs.
        :type job_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, JobDefinition_ee5db797, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        operation_name = "get_job_definition_for_interaction_model_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError(
                "Missing the required parameter `job_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/jobs/{jobId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.jobs.job_definition.JobDefinition", status_code=200, message="The job definition for a given jobId."))
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
            response_type="ask_smapi_model.v1.skill.interaction_model.jobs.job_definition.JobDefinition")

        if full_response:
            return api_response
        return api_response.body
        

    def set_job_status_for_interaction_model_v1(self, job_id, update_job_status_request, **kwargs):
        # type: (str, UpdateJobStatusRequest_f2d8379d, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, ValidationErrors_d42055a1]
        """
        Update the JobStatus to Enable or Disable a job.

        :param job_id: (required) The identifier for dynamic jobs.
        :type job_id: str
        :param update_job_status_request: (required) Request to update Job Definition status.
        :type update_job_status_request: ask_smapi_model.v1.skill.interaction_model.jobs.update_job_status_request.UpdateJobStatusRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, ValidationErrors_d42055a1]
        """
        operation_name = "set_job_status_for_interaction_model_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError(
                "Missing the required parameter `job_id` when calling `" + operation_name + "`")
        # verify the required parameter 'update_job_status_request' is set
        if ('update_job_status_request' not in params) or (params['update_job_status_request'] is None):
            raise ValueError(
                "Missing the required parameter `update_job_status_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/jobs/{jobId}/status'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'update_job_status_request' in params:
            body_params = params['update_job_status_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="No content; Confirms that the fields are updated."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.jobs.validation_errors.ValidationErrors", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
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
        
        return None

    def create_job_definition_for_interaction_model_v1(self, create_job_definition_request, **kwargs):
        # type: (CreateJobDefinitionRequest_e3d4c41, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, CreateJobDefinitionResponse_efaa9a6f, ValidationErrors_d42055a1]
        """
        Creates a new Job Definition from the Job Definition request provided. This can be either a CatalogAutoRefresh, which supports time-based configurations for catalogs, or a ReferencedResourceVersionUpdate, which is used for slotTypes and Interaction models to be automatically updated on the dynamic update of their referenced catalog. 

        :param create_job_definition_request: (required) Request to create a new Job Definition.
        :type create_job_definition_request: ask_smapi_model.v1.skill.interaction_model.jobs.create_job_definition_request.CreateJobDefinitionRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, CreateJobDefinitionResponse_efaa9a6f, ValidationErrors_d42055a1]
        """
        operation_name = "create_job_definition_for_interaction_model_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'create_job_definition_request' is set
        if ('create_job_definition_request' not in params) or (params['create_job_definition_request'] is None):
            raise ValueError(
                "Missing the required parameter `create_job_definition_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/jobs'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'create_job_definition_request' in params:
            body_params = params['create_job_definition_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.jobs.create_job_definition_response.CreateJobDefinitionResponse", status_code=201, message="Returns the generated jobId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.jobs.validation_errors.ValidationErrors", status_code=400, message="Server cannot process the request due to a client error."))
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
            response_type="ask_smapi_model.v1.skill.interaction_model.jobs.create_job_definition_response.CreateJobDefinitionResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def list_interaction_model_slot_types_v1(self, vendor_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, ListSlotTypeResponse_b426c805, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        List all slot types for the vendor. 

        :param vendor_id: (required) The vendor ID.
        :type vendor_id: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param sort_direction: Sets the sorting direction of the result items. When set to 'asc' these items are returned in ascending order of sortField value and when set to 'desc' these items are returned in descending order of sortField value.
        :type sort_direction: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, ListSlotTypeResponse_b426c805, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        operation_name = "list_interaction_model_slot_types_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vendor_id' is set
        if ('vendor_id' not in params) or (params['vendor_id'] is None):
            raise ValueError(
                "Missing the required parameter `vendor_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/slotTypes'
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
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.model_type.list_slot_type_response.ListSlotTypeResponse", status_code=200, message="Returns list of slot types for the vendor."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
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
            response_type="ask_smapi_model.v1.skill.interaction_model.model_type.list_slot_type_response.ListSlotTypeResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def create_interaction_model_slot_type_v1(self, slot_type, **kwargs):
        # type: (DefinitionData_dad4effb, **Any) -> Union[ApiResponse, object, SlotTypeResponse_1ca513dc, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Create a new version of slot type within the given slotTypeId. 

        :param slot_type: (required) 
        :type slot_type: ask_smapi_model.v1.skill.interaction_model.model_type.definition_data.DefinitionData
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, SlotTypeResponse_1ca513dc, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        operation_name = "create_interaction_model_slot_type_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slot_type' is set
        if ('slot_type' not in params) or (params['slot_type'] is None):
            raise ValueError(
                "Missing the required parameter `slot_type` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/slotTypes'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'slot_type' in params:
            body_params = params['slot_type']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.model_type.slot_type_response.SlotTypeResponse", status_code=200, message="Returns the generated slotTypeId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error e.g. the slot type definition is invalid."))
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
            response_type="ask_smapi_model.v1.skill.interaction_model.model_type.slot_type_response.SlotTypeResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def delete_interaction_model_slot_type_v1(self, slot_type_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Delete the slot type. 

        :param slot_type_id: (required) The identifier for a slot type.
        :type slot_type_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        operation_name = "delete_interaction_model_slot_type_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slot_type_id' is set
        if ('slot_type_id' not in params) or (params['slot_type_id'] is None):
            raise ValueError(
                "Missing the required parameter `slot_type_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/slotTypes/{slotTypeId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'slot_type_id' in params:
            path_params['slotTypeId'] = params['slot_type_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="No content; just confirm the slot type is deleted."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="The slot type cannot be deleted from reasons due to in-use by other entities."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="There is no slot type defined for the slotTypeId."))
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
        
        return None

    def get_interaction_model_slot_type_definition_v1(self, slot_type_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, SlotTypeDefinitionOutput_20e87f7, BadRequestError_f854b05]
        """
        Get the slot type definition. 

        :param slot_type_id: (required) The identifier for a slot type.
        :type slot_type_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, SlotTypeDefinitionOutput_20e87f7, BadRequestError_f854b05]
        """
        operation_name = "get_interaction_model_slot_type_definition_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slot_type_id' is set
        if ('slot_type_id' not in params) or (params['slot_type_id'] is None):
            raise ValueError(
                "Missing the required parameter `slot_type_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/slotTypes/{slotTypeId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'slot_type_id' in params:
            path_params['slotTypeId'] = params['slot_type_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.model_type.slot_type_definition_output.SlotTypeDefinitionOutput", status_code=200, message="The slot type definition."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="The slot type cannot be retrieved due to errors listed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="There is no slot type defined for the slotTypeId."))
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
            response_type="ask_smapi_model.v1.skill.interaction_model.model_type.slot_type_definition_output.SlotTypeDefinitionOutput")

        if full_response:
            return api_response
        return api_response.body
        

    def update_interaction_model_slot_type_v1(self, slot_type_id, update_request, **kwargs):
        # type: (str, UpdateRequest_43de537, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Update description and vendorGuidance string for certain version of a slot type. 

        :param slot_type_id: (required) The identifier for a slot type.
        :type slot_type_id: str
        :param update_request: (required) 
        :type update_request: ask_smapi_model.v1.skill.interaction_model.model_type.update_request.UpdateRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        operation_name = "update_interaction_model_slot_type_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slot_type_id' is set
        if ('slot_type_id' not in params) or (params['slot_type_id'] is None):
            raise ValueError(
                "Missing the required parameter `slot_type_id` when calling `" + operation_name + "`")
        # verify the required parameter 'update_request' is set
        if ('update_request' not in params) or (params['update_request'] is None):
            raise ValueError(
                "Missing the required parameter `update_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/slotTypes/{slotTypeId}/update'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'slot_type_id' in params:
            path_params['slotTypeId'] = params['slot_type_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'update_request' in params:
            body_params = params['update_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

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
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="There is no slot type defined for the slotTypeId."))
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
        
        return None

    def get_interaction_model_slot_type_build_status_v1(self, slot_type_id, update_request_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, SlotTypeStatus_a293ebfc, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Get the status of slot type resource and its sub-resources for a given slotTypeId. 

        :param slot_type_id: (required) The identifier for a slot type.
        :type slot_type_id: str
        :param update_request_id: (required) The identifier for slotType version creation process
        :type update_request_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, SlotTypeStatus_a293ebfc, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        operation_name = "get_interaction_model_slot_type_build_status_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slot_type_id' is set
        if ('slot_type_id' not in params) or (params['slot_type_id'] is None):
            raise ValueError(
                "Missing the required parameter `slot_type_id` when calling `" + operation_name + "`")
        # verify the required parameter 'update_request_id' is set
        if ('update_request_id' not in params) or (params['update_request_id'] is None):
            raise ValueError(
                "Missing the required parameter `update_request_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/slotTypes/{slotTypeId}/updateRequest/{updateRequestId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'slot_type_id' in params:
            path_params['slotTypeId'] = params['slot_type_id']
        if 'update_request_id' in params:
            path_params['updateRequestId'] = params['update_request_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.model_type.slot_type_status.SlotTypeStatus", status_code=200, message="Returns the build status and error codes for the given slotTypeId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="There is no slot type defined for the slotTypeId."))
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
            response_type="ask_smapi_model.v1.skill.interaction_model.model_type.slot_type_status.SlotTypeStatus")

        if full_response:
            return api_response
        return api_response.body
        

    def list_interaction_model_slot_type_versions_v1(self, slot_type_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, ListSlotTypeVersionResponse_7d552abf, BadRequestError_f854b05]
        """
        List all slot type versions for the slot type id. 

        :param slot_type_id: (required) The identifier for a slot type.
        :type slot_type_id: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param sort_direction: Sets the sorting direction of the result items. When set to 'asc' these items are returned in ascending order of sortField value and when set to 'desc' these items are returned in descending order of sortField value.
        :type sort_direction: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, ListSlotTypeVersionResponse_7d552abf, BadRequestError_f854b05]
        """
        operation_name = "list_interaction_model_slot_type_versions_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slot_type_id' is set
        if ('slot_type_id' not in params) or (params['slot_type_id'] is None):
            raise ValueError(
                "Missing the required parameter `slot_type_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/slotTypes/{slotTypeId}/versions'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'slot_type_id' in params:
            path_params['slotTypeId'] = params['slot_type_id']

        query_params = []  # type: List
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'sort_direction' in params:
            query_params.append(('sortDirection', params['sort_direction']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.type_version.list_slot_type_version_response.ListSlotTypeVersionResponse", status_code=200, message="Returns list of slot type version for the slot type id."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
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
            response_type="ask_smapi_model.v1.skill.interaction_model.type_version.list_slot_type_version_response.ListSlotTypeVersionResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def create_interaction_model_slot_type_version_v1(self, slot_type_id, slot_type, **kwargs):
        # type: (str, VersionData_faa770c8, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Create a new version of slot type entity for the given slotTypeId. 

        :param slot_type_id: (required) The identifier for a slot type.
        :type slot_type_id: str
        :param slot_type: (required) 
        :type slot_type: ask_smapi_model.v1.skill.interaction_model.type_version.version_data.VersionData
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        operation_name = "create_interaction_model_slot_type_version_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slot_type_id' is set
        if ('slot_type_id' not in params) or (params['slot_type_id'] is None):
            raise ValueError(
                "Missing the required parameter `slot_type_id` when calling `" + operation_name + "`")
        # verify the required parameter 'slot_type' is set
        if ('slot_type' not in params) or (params['slot_type'] is None):
            raise ValueError(
                "Missing the required parameter `slot_type` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/slotTypes/{slotTypeId}/versions'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'slot_type_id' in params:
            path_params['slotTypeId'] = params['slot_type_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'slot_type' in params:
            body_params = params['slot_type']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

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
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error e.g. the slot type definition is invalid."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The specified slot type does not exist."))
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
        
        return None

    def delete_interaction_model_slot_type_version_v1(self, slot_type_id, version, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Delete slot type version. 

        :param slot_type_id: (required) The identifier for a slot type.
        :type slot_type_id: str
        :param version: (required) Version for interaction model.
        :type version: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        operation_name = "delete_interaction_model_slot_type_version_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slot_type_id' is set
        if ('slot_type_id' not in params) or (params['slot_type_id'] is None):
            raise ValueError(
                "Missing the required parameter `slot_type_id` when calling `" + operation_name + "`")
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError(
                "Missing the required parameter `version` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/slotTypes/{slotTypeId}/versions/{version}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'slot_type_id' in params:
            path_params['slotTypeId'] = params['slot_type_id']
        if 'version' in params:
            path_params['version'] = params['version']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

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
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="There is no slot type version for this slotTypeId."))
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
        
        return None

    def get_interaction_model_slot_type_version_v1(self, slot_type_id, version, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, SlotTypeVersionData_1f3ee474]
        """
        Get slot type version data of given slot type version. 

        :param slot_type_id: (required) The identifier for a slot type.
        :type slot_type_id: str
        :param version: (required) Version for interaction model.
        :type version: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, SlotTypeVersionData_1f3ee474]
        """
        operation_name = "get_interaction_model_slot_type_version_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slot_type_id' is set
        if ('slot_type_id' not in params) or (params['slot_type_id'] is None):
            raise ValueError(
                "Missing the required parameter `slot_type_id` when calling `" + operation_name + "`")
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError(
                "Missing the required parameter `version` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/slotTypes/{slotTypeId}/versions/{version}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'slot_type_id' in params:
            path_params['slotTypeId'] = params['slot_type_id']
        if 'version' in params:
            path_params['version'] = params['version']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.type_version.slot_type_version_data.SlotTypeVersionData", status_code=200, message="Returns the slot type version metadata for the given slotTypeId and version."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="There is no slot type defined for the slotTypeId."))
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
            response_type="ask_smapi_model.v1.skill.interaction_model.type_version.slot_type_version_data.SlotTypeVersionData")

        if full_response:
            return api_response
        return api_response.body
        

    def update_interaction_model_slot_type_version_v1(self, slot_type_id, version, slot_type_update, **kwargs):
        # type: (str, str, SlotTypeUpdate_ae01835f, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Update description and vendorGuidance string for certain version of a slot type. 

        :param slot_type_id: (required) The identifier for a slot type.
        :type slot_type_id: str
        :param version: (required) Version for interaction model.
        :type version: str
        :param slot_type_update: (required) 
        :type slot_type_update: ask_smapi_model.v1.skill.interaction_model.type_version.slot_type_update.SlotTypeUpdate
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        operation_name = "update_interaction_model_slot_type_version_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'slot_type_id' is set
        if ('slot_type_id' not in params) or (params['slot_type_id'] is None):
            raise ValueError(
                "Missing the required parameter `slot_type_id` when calling `" + operation_name + "`")
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError(
                "Missing the required parameter `version` when calling `" + operation_name + "`")
        # verify the required parameter 'slot_type_update' is set
        if ('slot_type_update' not in params) or (params['slot_type_update'] is None):
            raise ValueError(
                "Missing the required parameter `slot_type_update` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/api/custom/interactionModel/slotTypes/{slotTypeId}/versions/{version}/update'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'slot_type_id' in params:
            path_params['slotTypeId'] = params['slot_type_id']
        if 'version' in params:
            path_params['version'] = params['version']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'slot_type_update' in params:
            body_params = params['slot_type_update']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

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
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="There is no slot type defined for the slotTypeId."))
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
        
        return None

    def get_status_of_export_request_v1(self, export_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, ExportResponse_b235e7bd, BadRequestError_f854b05]
        """
        Get status for given exportId 

        :param export_id: (required) The Export ID.
        :type export_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, ExportResponse_b235e7bd, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
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
        # type: (str, **Any) -> Union[ApiResponse, object, ListSkillResponse_527462d0, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Get the list of skills for the vendor.

        :param vendor_id: (required) The vendor ID.
        :type vendor_id: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param skill_id: The list of skillIds that you wish to get the summary for. A maximum of 10 skillIds can be specified to get the skill summary in single listSkills call. Please note that this parameter must not be used with 'nextToken' or/and 'maxResults' parameter.
        :type skill_id: list[str]
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, ListSkillResponse_527462d0, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, ImportResponse_364fa39f]
        """
        Get status for given importId. 

        :param import_id: (required) The Import ID.
        :type import_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, ImportResponse_364fa39f]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (CreateSkillWithPackageRequest_cd7f22be, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Creates a new import for a skill. 

        :param create_skill_with_package_request: (required) Defines the request body for createPackage API.
        :type create_skill_with_package_request: ask_smapi_model.v1.skill.create_skill_with_package_request.CreateSkillWithPackageRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def create_skill_for_vendor_v1(self, create_skill_request, **kwargs):
        # type: (CreateSkillRequest_92e74e84, **Any) -> Union[ApiResponse, object, CreateSkillResponse_2bad1094, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Creates a new skill for given vendorId.

        :param create_skill_request: (required) Defines the request body for createSkill API.
        :type create_skill_request: ask_smapi_model.v1.skill.create_skill_request.CreateSkillRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, CreateSkillResponse_2bad1094, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        

    def get_resource_schema_v1(self, resource, vendor_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, GetResourceSchemaResponse_9df87651, BadRequestError_f854b05]
        """
        GetResourceSchema API provides schema for skill related resources. The schema returned by this API will be specific to vendor because it considers public beta features allowed for the vendor.

        :param resource: (required) Name of the ASK resource for which schema is requested.
        :type resource: str
        :param vendor_id: (required) The vendor ID.
        :type vendor_id: str
        :param operation: This parameter is required when resource is manifest because skill manifest schema differs based on operation. For example, submit for certification schema has more validations than create skill schema.
        :type operation: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, GetResourceSchemaResponse_9df87651, BadRequestError_f854b05]
        """
        operation_name = "get_resource_schema_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'resource' is set
        if ('resource' not in params) or (params['resource'] is None):
            raise ValueError(
                "Missing the required parameter `resource` when calling `" + operation_name + "`")
        # verify the required parameter 'vendor_id' is set
        if ('vendor_id' not in params) or (params['vendor_id'] is None):
            raise ValueError(
                "Missing the required parameter `vendor_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/resourceSchema/{resource}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'resource' in params:
            path_params['resource'] = params['resource']

        query_params = []  # type: List
        if 'vendor_id' in params:
            query_params.append(('vendorId', params['vendor_id']))
        if 'operation' in params:
            query_params.append(('operation', params['operation']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.resource_schema.get_resource_schema_response.GetResourceSchemaResponse", status_code=200, message="Returns a S3 presigned URL to location of schema"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Invalid request"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="Unauthorized"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=403, message="Forbidden"))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Too Many Requests"))
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
            response_type="ask_smapi_model.v1.skill.resource_schema.get_resource_schema_response.GetResourceSchemaResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def get_alexa_hosted_skill_metadata_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, HostedSkillMetadata_b8976dfb, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Get Alexa hosted skill's metadata

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, HostedSkillMetadata_b8976dfb, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (str, HostedSkillRepositoryCredentialsRequest_79a1c791, **Any) -> Union[ApiResponse, object, HostedSkillRepositoryCredentialsList_d39d5fdf, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Generates hosted skill repository credentials to access the hosted skill repository.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param hosted_skill_repository_credentials_request: (required) defines the request body for hosted skill repository credentials
        :type hosted_skill_repository_credentials_request: ask_smapi_model.v1.skill.alexa_hosted.hosted_skill_repository_credentials_request.HostedSkillRepositoryCredentialsRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, HostedSkillRepositoryCredentialsList_d39d5fdf, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        

    def get_annotations_for_asr_annotation_set_v1(self, skill_id, annotation_set_id, accept, **kwargs):
        # type: (str, str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, GetAsrAnnotationSetAnnotationsResponse_e3efbdea, BadRequestError_f854b05]
        """
        Download the annotation set contents.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param annotation_set_id: (required) Identifier of the ASR annotation set.
        :type annotation_set_id: str
        :param accept: (required) - `application/json`: indicate to download annotation set contents in JSON format - `text/csv`: indicate to download annotation set contents in CSV format 
        :type accept: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. Defaults to 1000. If more results are present, the response will contain a paginationContext. 
        :type max_results: float
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, GetAsrAnnotationSetAnnotationsResponse_e3efbdea, BadRequestError_f854b05]
        """
        operation_name = "get_annotations_for_asr_annotation_set_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'annotation_set_id' is set
        if ('annotation_set_id' not in params) or (params['annotation_set_id'] is None):
            raise ValueError(
                "Missing the required parameter `annotation_set_id` when calling `" + operation_name + "`")
        # verify the required parameter 'accept' is set
        if ('accept' not in params) or (params['accept'] is None):
            raise ValueError(
                "Missing the required parameter `accept` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/asrAnnotationSets/{annotationSetId}/annotations'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'annotation_set_id' in params:
            path_params['annotationSetId'] = params['annotation_set_id']

        query_params = []  # type: List
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))

        header_params = []  # type: List
        if 'accept' in params:
            header_params.append(('Accept', params['accept']))

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.asr.annotation_sets.get_asr_annotation_set_annotations_response.GetAsrAnnotationSetAnnotationsResponse", status_code=200, message="The annotation set contents payload in specified format.  This API also supports pagination for annotation set contents requested in  &#x60;application/json&#x60; content type. Paginaiton for requested content  type &#x60;text/csv&#x60; is not supported. In this case, the nextToken and  maxResults query parameters would be ignored even if they are  specified as query parameters. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=503, message="Service Unavailable."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=0, message="Internal Server Error."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.asr.annotation_sets.get_asr_annotation_set_annotations_response.GetAsrAnnotationSetAnnotationsResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def set_annotations_for_asr_annotation_set_v1(self, skill_id, annotation_set_id, update_asr_annotation_set_contents_request, **kwargs):
        # type: (str, str, UpdateAsrAnnotationSetContentsPayload_df3c6c8c, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        Update the annotations in the annotation set
        API that updates the annotaions in the annotation set 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param annotation_set_id: (required) Identifier of the ASR annotation set.
        :type annotation_set_id: str
        :param update_asr_annotation_set_contents_request: (required) Payload containing annotation set contents. Two formats are accepted here: - `application/json`: Annotation set payload in JSON format. - `text/csv`: Annotation set payload in CSV format. Note that for CSV format, the first row should describe the column attributes. Columns should be delimited by comma.  The subsequent rows should describe annotation data and each annotation attributes has to follow the strict ordering defined in the first row. Each annotation fields should be delimited by comma. 
        :type update_asr_annotation_set_contents_request: ask_smapi_model.v1.skill.asr.annotation_sets.update_asr_annotation_set_contents_payload.UpdateAsrAnnotationSetContentsPayload
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        operation_name = "set_annotations_for_asr_annotation_set_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'annotation_set_id' is set
        if ('annotation_set_id' not in params) or (params['annotation_set_id'] is None):
            raise ValueError(
                "Missing the required parameter `annotation_set_id` when calling `" + operation_name + "`")
        # verify the required parameter 'update_asr_annotation_set_contents_request' is set
        if ('update_asr_annotation_set_contents_request' not in params) or (params['update_asr_annotation_set_contents_request'] is None):
            raise ValueError(
                "Missing the required parameter `update_asr_annotation_set_contents_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/asrAnnotationSets/{annotationSetId}/annotations'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'annotation_set_id' in params:
            path_params['annotationSetId'] = params['annotation_set_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'update_asr_annotation_set_contents_request' in params:
            body_params = params['update_asr_annotation_set_contents_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="ASR annotation set contents have been updated successfully."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=503, message="Service Unavailable."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=0, message="Internal Server Error."))

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
        
        return None

    def delete_asr_annotation_set_v1(self, skill_id, annotation_set_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        Delete the ASR annotation set
        API which deletes the ASR annotation set. Developers cannot get/list the deleted annotation set. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param annotation_set_id: (required) Identifier of the ASR annotation set.
        :type annotation_set_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        operation_name = "delete_asr_annotation_set_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'annotation_set_id' is set
        if ('annotation_set_id' not in params) or (params['annotation_set_id'] is None):
            raise ValueError(
                "Missing the required parameter `annotation_set_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/asrAnnotationSets/{annotationSetId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'annotation_set_id' in params:
            path_params['annotationSetId'] = params['annotation_set_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="ASR annotation set exists and is deleted successfully."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=409, message="The request could not be completed due to a conflict with the current state of the target resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=503, message="Service Unavailable."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=0, message="Internal Server Error."))

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
        
        return None

    def get_asr_annotation_set_v1(self, skill_id, annotation_set_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, GetASRAnnotationSetsPropertiesResponse_1512206, BadRequestError_f854b05]
        """
        Get the metadata of an ASR annotation set
        Return the metadata for an ASR annotation set. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param annotation_set_id: (required) Identifier of the ASR annotation set.
        :type annotation_set_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, GetASRAnnotationSetsPropertiesResponse_1512206, BadRequestError_f854b05]
        """
        operation_name = "get_asr_annotation_set_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'annotation_set_id' is set
        if ('annotation_set_id' not in params) or (params['annotation_set_id'] is None):
            raise ValueError(
                "Missing the required parameter `annotation_set_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/asrAnnotationSets/{annotationSetId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'annotation_set_id' in params:
            path_params['annotationSetId'] = params['annotation_set_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.asr.annotation_sets.get_asr_annotation_sets_properties_response.GetASRAnnotationSetsPropertiesResponse", status_code=200, message="The ASR annotation set exists."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=503, message="Service Unavailable."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=0, message="Internal Server Error."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.asr.annotation_sets.get_asr_annotation_sets_properties_response.GetASRAnnotationSetsPropertiesResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def set_asr_annotation_set_v1(self, skill_id, annotation_set_id, update_asr_annotation_set_properties_request_v1, **kwargs):
        # type: (str, str, UpdateAsrAnnotationSetPropertiesRequestObject_946da673, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        update the ASR annotation set properties.
        API which updates the ASR annotation set properties. Currently, the only data can be updated is annotation set name. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param annotation_set_id: (required) Identifier of the ASR annotation set.
        :type annotation_set_id: str
        :param update_asr_annotation_set_properties_request_v1: (required) Payload sent to the update ASR annotation set properties API.
        :type update_asr_annotation_set_properties_request_v1: ask_smapi_model.v1.skill.asr.annotation_sets.update_asr_annotation_set_properties_request_object.UpdateAsrAnnotationSetPropertiesRequestObject
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        operation_name = "set_asr_annotation_set_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'annotation_set_id' is set
        if ('annotation_set_id' not in params) or (params['annotation_set_id'] is None):
            raise ValueError(
                "Missing the required parameter `annotation_set_id` when calling `" + operation_name + "`")
        # verify the required parameter 'update_asr_annotation_set_properties_request_v1' is set
        if ('update_asr_annotation_set_properties_request_v1' not in params) or (params['update_asr_annotation_set_properties_request_v1'] is None):
            raise ValueError(
                "Missing the required parameter `update_asr_annotation_set_properties_request_v1` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/asrAnnotationSets/{annotationSetId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'annotation_set_id' in params:
            path_params['annotationSetId'] = params['annotation_set_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'update_asr_annotation_set_properties_request_v1' in params:
            body_params = params['update_asr_annotation_set_properties_request_v1']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="ASR annotation set exists and properties are updated successfully."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=503, message="Service Unavailable."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=0, message="Internal Server Error."))

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
        
        return None

    def list_asr_annotation_sets_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, ListASRAnnotationSetsResponse_a9a02e93]
        """
        List ASR annotation sets metadata for a given skill.
        API which requests all the ASR annotation sets for a skill. Returns the annotation set id and properties for each ASR annotation set. Supports paging of results. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. Defaults to 1000. If more results are present, the response will contain a paginationContext. 
        :type max_results: float
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, ListASRAnnotationSetsResponse_a9a02e93]
        """
        operation_name = "list_asr_annotation_sets_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/asrAnnotationSets'
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
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.asr.annotation_sets.list_asr_annotation_sets_response.ListASRAnnotationSetsResponse", status_code=200, message="ASR annotation sets metadata are returned."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=503, message="Service Unavailable."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=0, message="Internal Server Error."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.asr.annotation_sets.list_asr_annotation_sets_response.ListASRAnnotationSetsResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def create_asr_annotation_set_v1(self, skill_id, create_asr_annotation_set_request, **kwargs):
        # type: (str, CreateAsrAnnotationSetRequestObject_c8c6238c, **Any) -> Union[ApiResponse, object, Error_fbe913d9, CreateAsrAnnotationSetResponse_f4ef9811, BadRequestError_f854b05]
        """
        Create a new ASR annotation set for a skill
        This is an API that creates a new ASR annotation set with a name and returns the annotationSetId which can later be used to retrieve or reference the annotation set 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param create_asr_annotation_set_request: (required) Payload sent to the create ASR annotation set API.
        :type create_asr_annotation_set_request: ask_smapi_model.v1.skill.asr.annotation_sets.create_asr_annotation_set_request_object.CreateAsrAnnotationSetRequestObject
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, CreateAsrAnnotationSetResponse_f4ef9811, BadRequestError_f854b05]
        """
        operation_name = "create_asr_annotation_set_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'create_asr_annotation_set_request' is set
        if ('create_asr_annotation_set_request' not in params) or (params['create_asr_annotation_set_request'] is None):
            raise ValueError(
                "Missing the required parameter `create_asr_annotation_set_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/asrAnnotationSets'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'create_asr_annotation_set_request' in params:
            body_params = params['create_asr_annotation_set_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.asr.annotation_sets.create_asr_annotation_set_response.CreateAsrAnnotationSetResponse", status_code=200, message="ASR annotation set created successfully."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=503, message="Service Unavailable."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=0, message="Internal Server Error."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.asr.annotation_sets.create_asr_annotation_set_response.CreateAsrAnnotationSetResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def delete_asr_evaluation_v1(self, skill_id, evaluation_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        Delete an evaluation.
        API which enables the deletion of an evaluation.  

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param evaluation_id: (required) Identifier of the evaluation.
        :type evaluation_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        operation_name = "delete_asr_evaluation_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'evaluation_id' is set
        if ('evaluation_id' not in params) or (params['evaluation_id'] is None):
            raise ValueError(
                "Missing the required parameter `evaluation_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/asrEvaluations/{evaluationId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'evaluation_id' in params:
            path_params['evaluationId'] = params['evaluation_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="ASR evaluation exists and is deleted successfully."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=503, message="Service Unavailable."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=0, message="Internal Server Error."))

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
        
        return None

    def list_asr_evaluations_results_v1(self, skill_id, evaluation_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, GetAsrEvaluationsResultsResponse_4f62e093, BadRequestError_f854b05]
        """
        List results for a completed Evaluation.
        Paginated API which returns the test case results of an evaluation. This should be considered the \"expensive\" operation while GetAsrEvaluationsStatus is \"cheap\". 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param evaluation_id: (required) Identifier of the evaluation.
        :type evaluation_id: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. Defaults to 1000. If more results are present, the response will contain a nextToken. 
        :type max_results: float
        :param status: query parameter used to filter evaluation result status.   * `PASSED` - filter evaluation result status of `PASSED`   * `FAILED` - filter evaluation result status of `FAILED` 
        :type status: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, GetAsrEvaluationsResultsResponse_4f62e093, BadRequestError_f854b05]
        """
        operation_name = "list_asr_evaluations_results_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'evaluation_id' is set
        if ('evaluation_id' not in params) or (params['evaluation_id'] is None):
            raise ValueError(
                "Missing the required parameter `evaluation_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/asrEvaluations/{evaluationId}/results'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'evaluation_id' in params:
            path_params['evaluationId'] = params['evaluation_id']

        query_params = []  # type: List
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))
        if 'status' in params:
            query_params.append(('status', params['status']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.asr.evaluations.get_asr_evaluations_results_response.GetAsrEvaluationsResultsResponse", status_code=200, message="Evaluation exists and its status is queryable."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=503, message="Service Unavailable."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=0, message="Internal Server Error."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.asr.evaluations.get_asr_evaluations_results_response.GetAsrEvaluationsResultsResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def get_asr_evaluation_status_v1(self, skill_id, evaluation_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, GetAsrEvaluationStatusResponseObject_f8b7f006, Error_fbe913d9, BadRequestError_f854b05]
        """
        Get high level information and status of a asr evaluation.
        API which requests high level information about the evaluation like the current state of the job, status of the evaluation (if complete). Also returns the request used to start the job, like the number of total evaluations, number of completed evaluations, and start time. This should be considered the \"cheap\" operation while GetAsrEvaluationsResults is \"expensive\". 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param evaluation_id: (required) Identifier of the evaluation.
        :type evaluation_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, GetAsrEvaluationStatusResponseObject_f8b7f006, Error_fbe913d9, BadRequestError_f854b05]
        """
        operation_name = "get_asr_evaluation_status_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'evaluation_id' is set
        if ('evaluation_id' not in params) or (params['evaluation_id'] is None):
            raise ValueError(
                "Missing the required parameter `evaluation_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/asrEvaluations/{evaluationId}/status'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'evaluation_id' in params:
            path_params['evaluationId'] = params['evaluation_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.asr.evaluations.get_asr_evaluation_status_response_object.GetAsrEvaluationStatusResponseObject", status_code=200, message="Evaluation exists and its status is queryable."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=503, message="Service Unavailable."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=0, message="Internal Server Error."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.asr.evaluations.get_asr_evaluation_status_response_object.GetAsrEvaluationStatusResponseObject")

        if full_response:
            return api_response
        return api_response.body
        

    def list_asr_evaluations_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, ListAsrEvaluationsResponse_ef8cd586, Error_fbe913d9, BadRequestError_f854b05]
        """
        List asr evaluations run for a skill.
        API that allows developers to get historical ASR evaluations they run before. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param locale: locale in bcp 47 format. Used to filter results with the specified locale. If omitted, the response would include all evaluations regardless of what locale was used in the evaluation
        :type locale: str
        :param stage: Query parameter used to filter evaluations with specified skill stage.   * `development` - skill in `development` stage   * `live` - skill in `live` stage 
        :type stage: str
        :param annotation_set_id: filter to evaluations started using this annotationSetId
        :type annotation_set_id: str
        :param max_results: Sets the maximum number of results returned in the response body. Defaults to 1000. If more results are present, the response will contain a nextToken. 
        :type max_results: float
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, ListAsrEvaluationsResponse_ef8cd586, Error_fbe913d9, BadRequestError_f854b05]
        """
        operation_name = "list_asr_evaluations_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/asrEvaluations'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'locale' in params:
            query_params.append(('locale', params['locale']))
        if 'stage' in params:
            query_params.append(('stage', params['stage']))
        if 'annotation_set_id' in params:
            query_params.append(('annotationSetId', params['annotation_set_id']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.asr.evaluations.list_asr_evaluations_response.ListAsrEvaluationsResponse", status_code=200, message="Evaluations are returned."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=503, message="Service Unavailable."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=0, message="Internal Server Error."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.asr.evaluations.list_asr_evaluations_response.ListAsrEvaluationsResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def create_asr_evaluation_v1(self, post_asr_evaluations_request, skill_id, **kwargs):
        # type: (PostAsrEvaluationsRequestObject_133223f3, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, PostAsrEvaluationsResponseObject_1e0137c3]
        """
        Start an evaluation against the ASR model built by the skill's interaction model.
        This is an asynchronous API that starts an evaluation against the ASR model built by the skill's interaction model. The operation outputs an evaluationId which allows the retrieval of the current status of the operation and the results upon completion. This operation is unified, meaning both internal and external skill developers may use it to evaluate ASR models. 

        :param post_asr_evaluations_request: (required) Payload sent to trigger evaluation run.
        :type post_asr_evaluations_request: ask_smapi_model.v1.skill.asr.evaluations.post_asr_evaluations_request_object.PostAsrEvaluationsRequestObject
        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, PostAsrEvaluationsResponseObject_1e0137c3]
        """
        operation_name = "create_asr_evaluation_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'post_asr_evaluations_request' is set
        if ('post_asr_evaluations_request' not in params) or (params['post_asr_evaluations_request'] is None):
            raise ValueError(
                "Missing the required parameter `post_asr_evaluations_request` when calling `" + operation_name + "`")
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/asrEvaluations'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'post_asr_evaluations_request' in params:
            body_params = params['post_asr_evaluations_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.asr.evaluations.post_asr_evaluations_response_object.PostAsrEvaluationsResponseObject", status_code=200, message="Evaluation has successfully begun."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=409, message="The request could not be completed due to a conflict with the current state of the target resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=503, message="Service Unavailable."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=0, message="Internal Server Error."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.skill.asr.evaluations.post_asr_evaluations_response_object.PostAsrEvaluationsResponseObject")

        if full_response:
            return api_response
        return api_response.body
        

    def end_beta_test_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        End beta test.
        End a beta test for a given Alexa skill. System will revoke the entitlement of each tester and send access-end notification email to them. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def get_beta_test_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BetaTest_e826b162, BadRequestError_f854b05]
        """
        Get beta test.
        Get beta test for a given Alexa skill.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BetaTest_e826b162, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=409, message="Thrown if user tries to request a new simulation while the old simulation is in progress."))
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
        # type: (str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=201, message="Success. Return a URL to track the resource in &#39;Location&#39; header."))
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
        
        return None

    def update_beta_test_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, UpdateBetaTestResponse_84abf38, BadRequestError_f854b05]
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
        :rtype: Union[ApiResponse, object, Error_fbe913d9, UpdateBetaTestResponse_84abf38, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.beta_test.update_beta_test_response.UpdateBetaTestResponse", status_code=204, message="Success. No content."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=409, message="Thrown if user tries to request a new simulation while the old simulation is in progress."))
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
            response_type="ask_smapi_model.v1.skill.beta_test.update_beta_test_response.UpdateBetaTestResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def start_beta_test_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        Start beta test
        Start a beta test for a given Alexa skill. System will send invitation emails to each tester in the test, and add entitlement on the acceptance. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def add_testers_to_beta_test_v1(self, skill_id, testers_request, **kwargs):
        # type: (str, TestersList_f8c0feda, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def get_list_of_testers_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, ListTestersResponse_991ec8e9]
        """
        List testers.
        List all testers in a beta test for the given Alexa skill.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 500 results, you can add this parameter to your request. The response might contain fewer results than maxResults, but it will never contain more.
        :type max_results: int
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, ListTestersResponse_991ec8e9]
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
        header_params.append(('User-Agent', self.user_agent))

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
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=409, message="The request could not be completed due to a conflict with the current state of the target resource."))
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
        # type: (str, TestersList_f8c0feda, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def request_feedback_from_testers_v1(self, skill_id, testers_request, **kwargs):
        # type: (str, TestersList_f8c0feda, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def send_reminder_to_testers_v1(self, skill_id, testers_request, **kwargs):
        # type: (str, TestersList_f8c0feda, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def get_certification_review_v1(self, skill_id, certification_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, CertificationResponse_97fdaad, BadRequestError_f854b05]
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
        :rtype: Union[ApiResponse, object, Error_fbe913d9, CertificationResponse_97fdaad, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error e.g. if any request parameter is invalid like certification Id or pagination token etc. If the maxResults is not in the range of 1 to 50, it also qualifies for this error. "))
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
        # type: (str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, ListCertificationsResponse_f2a417c6]
        """
        Get list of all certifications available for a skill, including information about past certifications and any ongoing certification. The default sort order is descending on skillSubmissionTimestamp for Certifications. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, ListCertificationsResponse_f2a417c6]
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
        header_params.append(('User-Agent', self.user_agent))

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
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error e.g. if any request parameter is invalid like certification Id or pagination token etc. If the maxResults is not in the range of 1 to 50, it also qualifies for this error. "))
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
        

    def get_skill_credentials_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, SkillCredentials_a0f29ab1, StandardizedError_f5106a89]
        """
        Get the client credentials for the skill.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, SkillCredentials_a0f29ab1, StandardizedError_f5106a89]
        """
        operation_name = "get_skill_credentials_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/credentials'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.skill_credentials.SkillCredentials", status_code=200, message="Response contains the skill credentials."))
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
            response_type="ask_smapi_model.v1.skill.skill_credentials.SkillCredentials")

        if full_response:
            return api_response
        return api_response.body
        

    def delete_skill_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Delete the skill and model for given skillId.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def get_utterance_data_v1(self, skill_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, IntentRequests_35db15c7]
        """
        The Intent Request History API provides customers with the aggregated and anonymized transcription of user speech data and intent request details for their skills.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) The stage of the skill to be used for evaluation. An error will be returned if this skill stage is not enabled on the account used for evaluation.
        :type stage: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param sort_direction: Sets the sorting direction of the result items. When set to 'asc' these items are returned in ascending order of sortField value and when set to 'desc' these items are returned in descending order of sortField value.
        :type sort_direction: str
        :param sort_field: Sets the field on which the sorting would be applied.
        :type sort_field: str
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
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, IntentRequests_35db15c7]
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
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")

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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (UpdateSkillWithPackageRequest_d74ee124, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=412, message="Precondition failed."))
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
        
        return None

    def invoke_skill_v1(self, skill_id, invoke_skill_request, **kwargs):
        # type: (str, InvokeSkillRequest_8cf8aff9, **Any) -> Union[ApiResponse, object, InvokeSkillResponse_6f32f451, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        This is a synchronous API that invokes the Lambda or third party HTTPS endpoint for a given skill. A successful response will contain information related to what endpoint was called, payload sent to and received from the endpoint. In cases where requests to this API results in an error, the response will contain an error code and a description of the problem. In cases where invoking the skill endpoint specifically fails, the response will contain a status attribute indicating that a failure occurred and details about what was sent to the endpoint. The skill must belong to and be enabled by the user of this API. Also, note that calls to the skill endpoint will timeout after 10 seconds. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param invoke_skill_request: (required) Payload sent to the skill invocation API.
        :type invoke_skill_request: ask_smapi_model.v1.skill.invocations.invoke_skill_request.InvokeSkillRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, InvokeSkillResponse_6f32f451, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        operation_name = "invoke_skill_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'invoke_skill_request' is set
        if ('invoke_skill_request' not in params) or (params['invoke_skill_request'] is None):
            raise ValueError(
                "Missing the required parameter `invoke_skill_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/invocations'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'invoke_skill_request' in params:
            body_params = params['invoke_skill_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.invocations.invoke_skill_response.InvokeSkillResponse", status_code=200, message="Skill was invoked."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad request due to invalid or missing data."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="API user does not have permission to call this API or is currently in a state that does not allow invocation of this skill. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The specified skill does not exist."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=429, message="API user has exceeded the permitted request rate."))
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
            response_type="ask_smapi_model.v1.skill.invocations.invoke_skill_response.InvokeSkillResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def get_skill_metrics_v1(self, skill_id, start_time, end_time, period, metric, stage, skill_type, **kwargs):
        # type: (str, datetime, datetime, str, str, str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, GetMetricDataResponse_722e44c4]
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
        :type max_results: int
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, GetMetricDataResponse_722e44c4]
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
        header_params.append(('User-Agent', self.user_agent))

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
        

    def get_annotations_for_nlu_annotation_sets_v1(self, skill_id, annotation_id, accept, **kwargs):
        # type: (str, str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        Get the annotations of an NLU annotation set

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param annotation_id: (required) Identifier of the NLU annotation set.
        :type annotation_id: str
        :param accept: (required) Standard HTTP. Pass `application/json` or `test/csv` for GET calls. 
        :type accept: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        operation_name = "get_annotations_for_nlu_annotation_sets_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'annotation_id' is set
        if ('annotation_id' not in params) or (params['annotation_id'] is None):
            raise ValueError(
                "Missing the required parameter `annotation_id` when calling `" + operation_name + "`")
        # verify the required parameter 'accept' is set
        if ('accept' not in params) or (params['accept'] is None):
            raise ValueError(
                "Missing the required parameter `accept` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/nluAnnotationSets/{annotationId}/annotations'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'annotation_id' in params:
            path_params['annotationId'] = params['annotation_id']

        query_params = []  # type: List

        header_params = []  # type: List
        if 'accept' in params:
            header_params.append(('Accept', params['accept']))

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=200, message="The specific version of a NLU annotation set has the content."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
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
            response_type=None)

        if full_response:
            return api_response
        
        return None

    def update_annotations_for_nlu_annotation_sets_v1(self, skill_id, annotation_id, content_type, update_nlu_annotation_set_annotations_request, **kwargs):
        # type: (str, str, str, UpdateNLUAnnotationSetAnnotationsRequest_b336fe43, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        Replace the annotations in NLU annotation set.
        API which replaces the annotations in NLU annotation set. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param annotation_id: (required) Identifier of the NLU annotation set.
        :type annotation_id: str
        :param content_type: (required) Standard HTTP. Pass `application/json` or `test/csv` for POST calls with a json/csv body. 
        :type content_type: str
        :param update_nlu_annotation_set_annotations_request: (required) Payload sent to the update NLU annotation set API.
        :type update_nlu_annotation_set_annotations_request: ask_smapi_model.v1.skill.nlu.annotation_sets.update_nlu_annotation_set_annotations_request.UpdateNLUAnnotationSetAnnotationsRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        operation_name = "update_annotations_for_nlu_annotation_sets_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'annotation_id' is set
        if ('annotation_id' not in params) or (params['annotation_id'] is None):
            raise ValueError(
                "Missing the required parameter `annotation_id` when calling `" + operation_name + "`")
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params) or (params['content_type'] is None):
            raise ValueError(
                "Missing the required parameter `content_type` when calling `" + operation_name + "`")
        # verify the required parameter 'update_nlu_annotation_set_annotations_request' is set
        if ('update_nlu_annotation_set_annotations_request' not in params) or (params['update_nlu_annotation_set_annotations_request'] is None):
            raise ValueError(
                "Missing the required parameter `update_nlu_annotation_set_annotations_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/nluAnnotationSets/{annotationId}/annotations'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'annotation_id' in params:
            path_params['annotationId'] = params['annotation_id']

        query_params = []  # type: List

        header_params = []  # type: List
        if 'content_type' in params:
            header_params.append(('Content-Type', params['content_type']))

        body_params = None
        if 'update_nlu_annotation_set_annotations_request' in params:
            body_params = params['update_nlu_annotation_set_annotations_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=200, message="NLU annotation set exists and starts the update."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
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
        
        return None

    def delete_properties_for_nlu_annotation_sets_v1(self, skill_id, annotation_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        Delete the NLU annotation set
        API which deletes the NLU annotation set. Developers cannot get/list the deleted annotation set. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param annotation_id: (required) Identifier of the NLU annotation set.
        :type annotation_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        operation_name = "delete_properties_for_nlu_annotation_sets_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'annotation_id' is set
        if ('annotation_id' not in params) or (params['annotation_id'] is None):
            raise ValueError(
                "Missing the required parameter `annotation_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/nluAnnotationSets/{annotationId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'annotation_id' in params:
            path_params['annotationId'] = params['annotation_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="NLU annotation set exists and is deleted successfully."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=429, message="Exceed the permitted request limit. Throttling criteria includes total requests, per API, ClientId, and CustomerId."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=500, message="Internal Server Error."))

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
        
        return None

    def get_properties_for_nlu_annotation_sets_v1(self, skill_id, annotation_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, GetNLUAnnotationSetPropertiesResponse_731f20d3, BadRequestError_f854b05]
        """
        Get the properties of an NLU annotation set
        Return the properties for an NLU annotation set. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param annotation_id: (required) Identifier of the NLU annotation set.
        :type annotation_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, GetNLUAnnotationSetPropertiesResponse_731f20d3, BadRequestError_f854b05]
        """
        operation_name = "get_properties_for_nlu_annotation_sets_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'annotation_id' is set
        if ('annotation_id' not in params) or (params['annotation_id'] is None):
            raise ValueError(
                "Missing the required parameter `annotation_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/nluAnnotationSets/{annotationId}/properties'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'annotation_id' in params:
            path_params['annotationId'] = params['annotation_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.nlu.annotation_sets.get_nlu_annotation_set_properties_response.GetNLUAnnotationSetPropertiesResponse", status_code=200, message="The NLU annotation set exists."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
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
            response_type="ask_smapi_model.v1.skill.nlu.annotation_sets.get_nlu_annotation_set_properties_response.GetNLUAnnotationSetPropertiesResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def update_properties_for_nlu_annotation_sets_v1(self, skill_id, annotation_id, update_nlu_annotation_set_properties_request, **kwargs):
        # type: (str, str, UpdateNLUAnnotationSetPropertiesRequest_b569f485, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        update the NLU annotation set properties.
        API which updates the NLU annotation set properties. Currently, the only data can be updated is annotation set name. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param annotation_id: (required) Identifier of the NLU annotation set.
        :type annotation_id: str
        :param update_nlu_annotation_set_properties_request: (required) Payload sent to the update NLU annotation set properties API.
        :type update_nlu_annotation_set_properties_request: ask_smapi_model.v1.skill.nlu.annotation_sets.update_nlu_annotation_set_properties_request.UpdateNLUAnnotationSetPropertiesRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05]
        """
        operation_name = "update_properties_for_nlu_annotation_sets_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'annotation_id' is set
        if ('annotation_id' not in params) or (params['annotation_id'] is None):
            raise ValueError(
                "Missing the required parameter `annotation_id` when calling `" + operation_name + "`")
        # verify the required parameter 'update_nlu_annotation_set_properties_request' is set
        if ('update_nlu_annotation_set_properties_request' not in params) or (params['update_nlu_annotation_set_properties_request'] is None):
            raise ValueError(
                "Missing the required parameter `update_nlu_annotation_set_properties_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/nluAnnotationSets/{annotationId}/properties'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'annotation_id' in params:
            path_params['annotationId'] = params['annotation_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'update_nlu_annotation_set_properties_request' in params:
            body_params = params['update_nlu_annotation_set_properties_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=201, message="NLU annotation set exists and properties are updated successfully."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
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
        
        return None

    def list_nlu_annotation_sets_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, ListNLUAnnotationSetsResponse_5b1b0b6a, BadRequestError_f854b05]
        """
        List NLU annotation sets for a given skill.
        API which requests all the NLU annotation sets for a skill. Returns the annotationId and properties for each NLU annotation set. Developers can filter the results using locale. Supports paging of results. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param locale: filter to NLU annotation set created using this locale
        :type locale: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. Defaults to 10. If more results are present, the response will contain a nextToken and a _link.next href. 
        :type max_results: float
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, ListNLUAnnotationSetsResponse_5b1b0b6a, BadRequestError_f854b05]
        """
        operation_name = "list_nlu_annotation_sets_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/nluAnnotationSets'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List
        if 'locale' in params:
            query_params.append(('locale', params['locale']))
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.nlu.annotation_sets.list_nlu_annotation_sets_response.ListNLUAnnotationSetsResponse", status_code=200, message="NLU annotation sets are returned."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
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
            response_type="ask_smapi_model.v1.skill.nlu.annotation_sets.list_nlu_annotation_sets_response.ListNLUAnnotationSetsResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def create_nlu_annotation_set_v1(self, skill_id, create_nlu_annotation_set_request, **kwargs):
        # type: (str, CreateNLUAnnotationSetRequest_16b1430c, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, CreateNLUAnnotationSetResponse_b069cada]
        """
        Create a new NLU annotation set for a skill which will generate a new annotationId.
        This is an API that creates a new NLU annotation set with properties and returns the annotationId. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param create_nlu_annotation_set_request: (required) Payload sent to the create NLU annotation set API.
        :type create_nlu_annotation_set_request: ask_smapi_model.v1.skill.nlu.annotation_sets.create_nlu_annotation_set_request.CreateNLUAnnotationSetRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, CreateNLUAnnotationSetResponse_b069cada]
        """
        operation_name = "create_nlu_annotation_set_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'create_nlu_annotation_set_request' is set
        if ('create_nlu_annotation_set_request' not in params) or (params['create_nlu_annotation_set_request'] is None):
            raise ValueError(
                "Missing the required parameter `create_nlu_annotation_set_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/nluAnnotationSets'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'create_nlu_annotation_set_request' in params:
            body_params = params['create_nlu_annotation_set_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.nlu.annotation_sets.create_nlu_annotation_set_response.CreateNLUAnnotationSetResponse", status_code=201, message="NLU annotation set created successfully."))
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
            response_type="ask_smapi_model.v1.skill.nlu.annotation_sets.create_nlu_annotation_set_response.CreateNLUAnnotationSetResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def get_nlu_evaluation_v1(self, skill_id, evaluation_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, GetNLUEvaluationResponse_2fb5e6ed, BadRequestError_f854b05]
        """
        Get top level information and status of a nlu evaluation.
        API which requests top level information about the evaluation like the current state of the job, status of the evaluation (if complete). Also returns data used to start the job, like the number of test cases, stage, locale, and start time. This should be considered the 'cheap' operation while getResultForNLUEvaluations is 'expensive'. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param evaluation_id: (required) Identifier of the evaluation.
        :type evaluation_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, GetNLUEvaluationResponse_2fb5e6ed, BadRequestError_f854b05]
        """
        operation_name = "get_nlu_evaluation_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'evaluation_id' is set
        if ('evaluation_id' not in params) or (params['evaluation_id'] is None):
            raise ValueError(
                "Missing the required parameter `evaluation_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/nluEvaluations/{evaluationId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'evaluation_id' in params:
            path_params['evaluationId'] = params['evaluation_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.nlu.evaluations.get_nlu_evaluation_response.GetNLUEvaluationResponse", status_code=200, message="Evaluation exists and its status is queryable."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
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
            response_type="ask_smapi_model.v1.skill.nlu.evaluations.get_nlu_evaluation_response.GetNLUEvaluationResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def get_result_for_nlu_evaluations_v1(self, skill_id, evaluation_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, GetNLUEvaluationResultsResponse_5ca1fa54, BadRequestError_f854b05]
        """
        Get test case results for a completed Evaluation.
        Paginated API which returns the test case results of an evaluation. This should be considered the 'expensive' operation while getNluEvaluation is 'cheap'. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param evaluation_id: (required) Identifier of the evaluation.
        :type evaluation_id: str
        :param sort_field: 
        :type sort_field: str
        :param test_case_status: only returns test cases with this status
        :type test_case_status: str
        :param actual_intent_name: only returns test cases with intents which resolve to this intent
        :type actual_intent_name: str
        :param expected_intent_name: only returns test cases with intents which are expected to be this intent
        :type expected_intent_name: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. Defaults to 1000. If more results are present, the response will contain a nextToken and a _link.next href. 
        :type max_results: float
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, GetNLUEvaluationResultsResponse_5ca1fa54, BadRequestError_f854b05]
        """
        operation_name = "get_result_for_nlu_evaluations_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'evaluation_id' is set
        if ('evaluation_id' not in params) or (params['evaluation_id'] is None):
            raise ValueError(
                "Missing the required parameter `evaluation_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/nluEvaluations/{evaluationId}/results'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'evaluation_id' in params:
            path_params['evaluationId'] = params['evaluation_id']

        query_params = []  # type: List
        if 'sort_field' in params:
            query_params.append(('sort.field', params['sort_field']))
        if 'test_case_status' in params:
            query_params.append(('testCaseStatus', params['test_case_status']))
        if 'actual_intent_name' in params:
            query_params.append(('actualIntentName', params['actual_intent_name']))
        if 'expected_intent_name' in params:
            query_params.append(('expectedIntentName', params['expected_intent_name']))
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.nlu.evaluations.get_nlu_evaluation_results_response.GetNLUEvaluationResultsResponse", status_code=200, message="Evaluation exists and its status is queryable."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
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
            response_type="ask_smapi_model.v1.skill.nlu.evaluations.get_nlu_evaluation_results_response.GetNLUEvaluationResultsResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def list_nlu_evaluations_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, ListNLUEvaluationsResponse_7ef8d08f, BadRequestError_f854b05]
        """
        List nlu evaluations run for a skill.
        API which requests recently run nlu evaluations started by a vendor for a skill. Returns the evaluation id and some of the parameters used to start the evaluation. Developers can filter the results using locale and stage. Supports paging of results. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param locale: filter to evaluations started using this locale
        :type locale: str
        :param stage: filter to evaluations started using this stage
        :type stage: str
        :param annotation_id: filter to evaluations started using this annotationId
        :type annotation_id: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. Defaults to 10. If more results are present, the response will contain a nextToken and a _link.next href. 
        :type max_results: float
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, ListNLUEvaluationsResponse_7ef8d08f, BadRequestError_f854b05]
        """
        operation_name = "list_nlu_evaluations_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/nluEvaluations'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List
        if 'locale' in params:
            query_params.append(('locale', params['locale']))
        if 'stage' in params:
            query_params.append(('stage', params['stage']))
        if 'annotation_id' in params:
            query_params.append(('annotationId', params['annotation_id']))
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.nlu.evaluations.list_nlu_evaluations_response.ListNLUEvaluationsResponse", status_code=200, message="Evaluations are returned."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
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
            response_type="ask_smapi_model.v1.skill.nlu.evaluations.list_nlu_evaluations_response.ListNLUEvaluationsResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def create_nlu_evaluations_v1(self, evaluate_nlu_request, skill_id, **kwargs):
        # type: (EvaluateNLURequest_7a358f6a, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, EvaluateResponse_640ae5b5, BadRequestError_f854b05]
        """
        Start an evaluation against the NLU model built by the skill's interaction model.
        This is an asynchronous API that starts an evaluation against the NLU model built by the skill's interaction model. The operation outputs an evaluationId which allows the retrieval of the current status of the operation and the results upon completion. This operation is unified, meaning both internal and external skill developers may use it evaluate NLU models. 

        :param evaluate_nlu_request: (required) Payload sent to the evaluate NLU API.
        :type evaluate_nlu_request: ask_smapi_model.v1.skill.nlu.evaluations.evaluate_nlu_request.EvaluateNLURequest
        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, EvaluateResponse_640ae5b5, BadRequestError_f854b05]
        """
        operation_name = "create_nlu_evaluations_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'evaluate_nlu_request' is set
        if ('evaluate_nlu_request' not in params) or (params['evaluate_nlu_request'] is None):
            raise ValueError(
                "Missing the required parameter `evaluate_nlu_request` when calling `" + operation_name + "`")
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/nluEvaluations'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'evaluate_nlu_request' in params:
            body_params = params['evaluate_nlu_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.nlu.evaluations.evaluate_response.EvaluateResponse", status_code=200, message="Evaluation has successfully begun."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=404, message="The resource being requested is not found."))
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
            response_type="ask_smapi_model.v1.skill.nlu.evaluations.evaluate_response.EvaluateResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def publish_skill_v1(self, skill_id, accept_language, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, SkillPublicationResponse_8da9d720, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        If the skill is in certified stage, initiate publishing immediately or set a date at which the skill can publish at. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param accept_language: (required) User's locale/language in context.
        :type accept_language: str
        :param publish_skill_request: Defines the request body for publish skill API.
        :type publish_skill_request: ask_smapi_model.v1.skill.publication.publish_skill_request.PublishSkillRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, SkillPublicationResponse_8da9d720, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        operation_name = "publish_skill_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'accept_language' is set
        if ('accept_language' not in params) or (params['accept_language'] is None):
            raise ValueError(
                "Missing the required parameter `accept_language` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/publications'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List
        if 'accept_language' in params:
            header_params.append(('Accept-Language', params['accept_language']))

        body_params = None
        if 'publish_skill_request' in params:
            body_params = params['publish_skill_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.publication.skill_publication_response.SkillPublicationResponse", status_code=202, message="Successfully processed skill publication request."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
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
            response_type="ask_smapi_model.v1.skill.publication.skill_publication_response.SkillPublicationResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def get_skill_publications_v1(self, skill_id, accept_language, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, SkillPublicationResponse_8da9d720, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Retrieves the latest skill publishing details of the certified stage of the skill. The publishesAtDate and status of skill publishing. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param accept_language: (required) User's locale/language in context.
        :type accept_language: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, SkillPublicationResponse_8da9d720, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        operation_name = "get_skill_publications_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'accept_language' is set
        if ('accept_language' not in params) or (params['accept_language'] is None):
            raise ValueError(
                "Missing the required parameter `accept_language` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/publications/~latest'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List
        if 'accept_language' in params:
            header_params.append(('Accept-Language', params['accept_language']))

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.publication.skill_publication_response.SkillPublicationResponse", status_code=200, message="Successfully retrieved latest skill publication information."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
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
            response_type="ask_smapi_model.v1.skill.publication.skill_publication_response.SkillPublicationResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def rollback_skill_v1(self, skill_id, create_rollback_request, **kwargs):
        # type: (str, CreateRollbackRequest_e7747a32, **Any) -> Union[ApiResponse, object, CreateRollbackResponse_5a2e8250, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Submit a target skill version to rollback to. Only one rollback or publish operation can be outstanding for a given skillId.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param create_rollback_request: (required) defines the request body to create a rollback request
        :type create_rollback_request: ask_smapi_model.v1.skill.create_rollback_request.CreateRollbackRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, CreateRollbackResponse_5a2e8250, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        operation_name = "rollback_skill_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'create_rollback_request' is set
        if ('create_rollback_request' not in params) or (params['create_rollback_request'] is None):
            raise ValueError(
                "Missing the required parameter `create_rollback_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/rollbacks'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'create_rollback_request' in params:
            body_params = params['create_rollback_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.create_rollback_response.CreateRollbackResponse", status_code=201, message="Rollback request created; Returns the generated identifier to track the rollback request and returns a URL to track the status in Location header."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
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
            response_type="ask_smapi_model.v1.skill.create_rollback_response.CreateRollbackResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def get_rollback_for_skill_v1(self, skill_id, rollback_request_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, RollbackRequestStatus_71665366]
        """
        Get the rollback status of a skill given an associated rollbackRequestId. Use ~latest in place of rollbackRequestId to get the latest rollback status.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param rollback_request_id: (required) Defines the identifier for a rollback request. If set to ~latest, request returns the status of the latest rollback request.
        :type rollback_request_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, RollbackRequestStatus_71665366]
        """
        operation_name = "get_rollback_for_skill_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'rollback_request_id' is set
        if ('rollback_request_id' not in params) or (params['rollback_request_id'] is None):
            raise ValueError(
                "Missing the required parameter `rollback_request_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/rollbacks/{rollbackRequestId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'rollback_request_id' in params:
            path_params['rollbackRequestId'] = params['rollback_request_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.rollback_request_status.RollbackRequestStatus", status_code=200, message="Returns the rollback status for a given skillId and rollbackRequestId. Returns the latest rollback status if ~latest is used in place of rollbackRequestId."))
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
            response_type="ask_smapi_model.v1.skill.rollback_request_status.RollbackRequestStatus")

        if full_response:
            return api_response
        return api_response.body
        

    def simulate_skill_v1(self, skill_id, simulations_api_request, **kwargs):
        # type: (str, SimulationsApiRequest_606eed02, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, SimulationsApiResponse_328955bc]
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
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, SimulationsApiResponse_328955bc]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, SimulationsApiResponse_328955bc]
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
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, SimulationsApiResponse_328955bc]
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
        header_params.append(('User-Agent', self.user_agent))

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
        

    def get_smart_home_capability_evaluation_v1(self, skill_id, evaluation_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, GetSHCapabilityEvaluationResponse_d484531f]
        """
        Get top level information and status of a Smart Home capability evaluation.
        Get top level information and status of a Smart Home capability evaluation.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param evaluation_id: (required) A unique ID to identify each Smart Home capability evaluation.
        :type evaluation_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, GetSHCapabilityEvaluationResponse_d484531f]
        """
        operation_name = "get_smart_home_capability_evaluation_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'evaluation_id' is set
        if ('evaluation_id' not in params) or (params['evaluation_id'] is None):
            raise ValueError(
                "Missing the required parameter `evaluation_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/smartHome/testing/capabilityEvaluations/{evaluationId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'evaluation_id' in params:
            path_params['evaluationId'] = params['evaluation_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.smart_home_evaluation.get_sh_capability_evaluation_response.GetSHCapabilityEvaluationResponse", status_code=200, message="Successfully retrieved the evaluation status."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad Request. Returned when the request payload is malformed or when, at least, one required property is missing or invalid. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="API user does not have permission or is currently in a state that does not allow calls to this API. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=404, message="The specified skill, test plan, or evaluation does not exist. The error response will contain a description that indicates the specific resource type that was not found. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=429, message="Exceeded the permitted request limit. Throttling criteria includes total requests, per API and CustomerId. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=0, message="Internal server error. "))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.smart_home_evaluation.get_sh_capability_evaluation_response.GetSHCapabilityEvaluationResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def get_smarthome_capablity_evaluation_results_v1(self, skill_id, evaluation_id, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, GetSHCapabilityEvaluationResultsResponse_9a1d4db0]
        """
        Get test case results for an evaluation run.
        Get test case results for an evaluation run.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param evaluation_id: (required) A unique ID to identify each Smart Home capability evaluation.
        :type evaluation_id: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, GetSHCapabilityEvaluationResultsResponse_9a1d4db0]
        """
        operation_name = "get_smarthome_capablity_evaluation_results_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'evaluation_id' is set
        if ('evaluation_id' not in params) or (params['evaluation_id'] is None):
            raise ValueError(
                "Missing the required parameter `evaluation_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/smartHome/testing/capabilityEvaluations/{evaluationId}/results'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'evaluation_id' in params:
            path_params['evaluationId'] = params['evaluation_id']

        query_params = []  # type: List
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.smart_home_evaluation.get_sh_capability_evaluation_results_response.GetSHCapabilityEvaluationResultsResponse", status_code=200, message="Successfully retrieved the evaluation result content."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad Request. Returned when the request payload is malformed or when, at least, one required property is missing or invalid. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="API user does not have permission or is currently in a state that does not allow calls to this API. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=404, message="The specified skill, test plan, or evaluation does not exist. The error response will contain a description that indicates the specific resource type that was not found. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=429, message="Exceeded the permitted request limit. Throttling criteria includes total requests, per API and CustomerId. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=0, message="Internal server error. "))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.smart_home_evaluation.get_sh_capability_evaluation_results_response.GetSHCapabilityEvaluationResultsResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def list_smarthome_capability_evaluations_v1(self, skill_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, ListSHCapabilityEvaluationsResponse_e6fe49d5, BadRequestError_f854b05]
        """
        List Smart Home capability evaluation runs for a skill.
        List Smart Home capability evaluation runs for a skill.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) The stage of the skill to be used for evaluation. An error will be returned if this skill stage is not enabled on the account used for evaluation.
        :type stage: str
        :param start_timestamp_from: The begnning of the start time to query evaluation result.
        :type start_timestamp_from: datetime
        :param start_timestamp_to: The end of the start time to query evaluation result.
        :type start_timestamp_to: datetime
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, ListSHCapabilityEvaluationsResponse_e6fe49d5, BadRequestError_f854b05]
        """
        operation_name = "list_smarthome_capability_evaluations_v1"
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

        resource_path = '/v1/skills/{skillId}/smartHome/testing/capabilityEvaluations'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List
        if 'stage' in params:
            query_params.append(('stage', params['stage']))
        if 'start_timestamp_from' in params:
            query_params.append(('startTimestampFrom', params['start_timestamp_from']))
        if 'start_timestamp_to' in params:
            query_params.append(('startTimestampTo', params['start_timestamp_to']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.smart_home_evaluation.list_sh_capability_evaluations_response.ListSHCapabilityEvaluationsResponse", status_code=200, message="Successfully retrieved the evaluation infomation."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad Request. Returned when the request payload is malformed or when, at least, one required property is missing or invalid. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="API user does not have permission or is currently in a state that does not allow calls to this API. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=404, message="The specified skill, test plan, or evaluation does not exist. The error response will contain a description that indicates the specific resource type that was not found. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=429, message="Exceeded the permitted request limit. Throttling criteria includes total requests, per API and CustomerId. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=0, message="Internal server error. "))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.smart_home_evaluation.list_sh_capability_evaluations_response.ListSHCapabilityEvaluationsResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def create_smarthome_capability_evaluation_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, EvaluateSHCapabilityResponse_38ae7f22]
        """
        Start a capability evaluation against a Smart Home skill.
        Start a capability evaluation against a Smart Home skill.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param evaluate_sh_capability_payload: Payload sent to start a capability evaluation against a Smart Home skill.
        :type evaluate_sh_capability_payload: ask_smapi_model.v1.smart_home_evaluation.evaluate_sh_capability_request.EvaluateSHCapabilityRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, EvaluateSHCapabilityResponse_38ae7f22]
        """
        operation_name = "create_smarthome_capability_evaluation_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/smartHome/testing/capabilityEvaluations'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'evaluate_sh_capability_payload' in params:
            body_params = params['evaluate_sh_capability_payload']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.smart_home_evaluation.evaluate_sh_capability_response.EvaluateSHCapabilityResponse", status_code=200, message="Evaluation has successfully begun."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad Request. Returned when the request payload is malformed or when, at least, one required property is missing or invalid. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="API user does not have permission or is currently in a state that does not allow calls to this API. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=404, message="The specified skill, test plan, or evaluation does not exist. The error response will contain a description that indicates the specific resource type that was not found. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=409, message="A test run is already in progress for the specified endpoint. Please retry after some time. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=429, message="Exceeded the permitted request limit. Throttling criteria includes total requests, per API and CustomerId. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=0, message="Internal server error. "))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.smart_home_evaluation.evaluate_sh_capability_response.EvaluateSHCapabilityResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def list_smarthome_capability_test_plans_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, ListSHCapabilityTestPlansResponse_cb289d6, BadRequestError_f854b05]
        """
        List all the test plan names and ids for a given skill ID.
        List all the test plan names and ids for a given skill ID.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, ListSHCapabilityTestPlansResponse_cb289d6, BadRequestError_f854b05]
        """
        operation_name = "list_smarthome_capability_test_plans_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/smartHome/testing/capabilityTestPlans'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']

        query_params = []  # type: List
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.smart_home_evaluation.list_sh_capability_test_plans_response.ListSHCapabilityTestPlansResponse", status_code=200, message="Successfully got the list of test plans."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Bad Request. Returned when the request payload is malformed or when, at least, one required property is missing or invalid. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="API user does not have permission or is currently in a state that does not allow calls to this API. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=404, message="The specified skill, test plan, or evaluation does not exist. The error response will contain a description that indicates the specific resource type that was not found. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=429, message="Exceeded the permitted request limit. Throttling criteria includes total requests, per API and CustomerId. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.error.Error", status_code=0, message="Internal server error. "))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v1.smart_home_evaluation.list_sh_capability_test_plans_response.ListSHCapabilityTestPlansResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def get_ssl_certificates_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, SSLCertificatePayload_97891902]
        """
        Returns the ssl certificate sets currently associated with this skill. Sets consist of one ssl certificate blob associated with a region as well as the default certificate for the skill.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, SSLCertificatePayload_97891902]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (str, SSLCertificatePayload_97891902, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Updates the ssl certificates associated with this skill.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param ssl_certificate_payload: (required) Defines the input/output of the ssl certificates api for a skill.
        :type ssl_certificate_payload: ask_smapi_model.v1.skill.ssl_certificate_payload.SSLCertificatePayload
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def delete_skill_enablement_v1(self, skill_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Deletes the enablement for given skillId/stage and customerId (retrieved from Auth token).

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def get_skill_enablement_status_v1(self, skill_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Checks whether an enablement exist for given skillId/stage and customerId (retrieved from Auth token)

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
            response_type=None)

        if full_response:
            return api_response
        
        return None

    def set_skill_enablement_v1(self, skill_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Creates/Updates the enablement for given skillId/stage and customerId (retrieved from Auth token)

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
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
        
        return None

    def create_export_request_for_skill_v1(self, skill_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Creates a new export for a skill with given skillId and stage. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def get_isp_list_for_skill_id_v1(self, skill_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, ListInSkillProductResponse_505e7307]
        """
        Get the list of in-skill products for the skillId.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, ListInSkillProductResponse_505e7307]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (ProfileNluRequest_501c0d87, str, str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, ProfileNluResponse_d24b74c1]
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
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, ProfileNluResponse_d24b74c1]
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
        header_params.append(('User-Agent', self.user_agent))

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
        

    def get_conflict_detection_job_status_for_interaction_model_v1(self, skill_id, locale, stage, version, **kwargs):
        # type: (str, str, str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, GetConflictDetectionJobStatusResponse_9e0e2cf1]
        """
        Retrieve conflict detection job status for skill.
        This API returns the job status of conflict detection job for a specified interaction model.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param locale: (required) The locale for the model requested e.g. en-GB, en-US, de-DE.
        :type locale: str
        :param stage: (required) Stage of the interaction model.
        :type stage: str
        :param version: (required) Version of interaction model. Use \"~current\" to get the model of the current version.
        :type version: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, GetConflictDetectionJobStatusResponse_9e0e2cf1]
        """
        operation_name = "get_conflict_detection_job_status_for_interaction_model_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'locale' is set
        if ('locale' not in params) or (params['locale'] is None):
            raise ValueError(
                "Missing the required parameter `locale` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError(
                "Missing the required parameter `version` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stage}/interactionModel/locales/{locale}/versions/{version}/conflictDetectionJobStatus'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'locale' in params:
            path_params['locale'] = params['locale']
        if 'stage' in params:
            path_params['stage'] = params['stage']
        if 'version' in params:
            path_params['version'] = params['version']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.conflict_detection.get_conflict_detection_job_status_response.GetConflictDetectionJobStatusResponse", status_code=200, message="Get conflict detection results successfully."))
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
            response_type="ask_smapi_model.v1.skill.interaction_model.conflict_detection.get_conflict_detection_job_status_response.GetConflictDetectionJobStatusResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def get_conflicts_for_interaction_model_v1(self, skill_id, locale, stage, version, **kwargs):
        # type: (str, str, str, str, **Any) -> Union[ApiResponse, object, GetConflictsResponse_502eb394, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Retrieve conflict detection results for a specified interaction model.
        This is a paginated API that retrieves results of conflict detection job for a specified interaction model.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param locale: (required) The locale for the model requested e.g. en-GB, en-US, de-DE.
        :type locale: str
        :param stage: (required) Stage of the interaction model.
        :type stage: str
        :param version: (required) Version of interaction model. Use \"~current\" to get the model of the current version.
        :type version: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. Defaults to 100. If more results are present, the response will contain a nextToken and a _link.next href.
        :type max_results: float
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, GetConflictsResponse_502eb394, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        operation_name = "get_conflicts_for_interaction_model_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")
        # verify the required parameter 'locale' is set
        if ('locale' not in params) or (params['locale'] is None):
            raise ValueError(
                "Missing the required parameter `locale` when calling `" + operation_name + "`")
        # verify the required parameter 'stage' is set
        if ('stage' not in params) or (params['stage'] is None):
            raise ValueError(
                "Missing the required parameter `stage` when calling `" + operation_name + "`")
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError(
                "Missing the required parameter `version` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stage}/interactionModel/locales/{locale}/versions/{version}/conflicts'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'locale' in params:
            path_params['locale'] = params['locale']
        if 'stage' in params:
            path_params['stage'] = params['stage']
        if 'version' in params:
            path_params['version'] = params['version']

        query_params = []  # type: List
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))
        if 'max_results' in params:
            query_params.append(('maxResults', params['max_results']))

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.interaction_model.conflict_detection.get_conflicts_response.GetConflictsResponse", status_code=200, message="Get conflict detection results sucessfully."))
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
            response_type="ask_smapi_model.v1.skill.interaction_model.conflict_detection.get_conflicts_response.GetConflictsResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def list_private_distribution_accounts_v1(self, skill_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, ListPrivateDistributionAccountsResponse_8783420d, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        List private distribution accounts. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, ListPrivateDistributionAccountsResponse_8783420d, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (str, str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def set_private_distribution_account_id_v1(self, skill_id, stage, id, **kwargs):
        # type: (str, str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def delete_account_linking_info_v1(self, skill_id, stage_v2, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Delete AccountLinking information of a skill for the given stage. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage_v2: (required) Stages of a skill including the new certified stage. * `development` - skills which are currently in development corresponds to this stage. * `certified` -  skills which have completed certification and ready for publishing corresponds to this stage. * `live` - skills which are currently live corresponds to this stage. 
        :type stage_v2: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def get_account_linking_info_v1(self, skill_id, stage_v2, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, AccountLinkingResponse_b1f92882, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Get AccountLinking information for the skill. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage_v2: (required) Stages of a skill including the new certified stage. * `development` - skills which are currently in development corresponds to this stage. * `certified` -  skills which have completed certification and ready for publishing corresponds to this stage. * `live` - skills which are currently live corresponds to this stage. 
        :type stage_v2: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, AccountLinkingResponse_b1f92882, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (str, str, AccountLinkingRequest_cac174e, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def clone_locale_v1(self, skill_id, stage_v2, clone_locale_request, **kwargs):
        # type: (str, str, CloneLocaleRequest_2e00cdf4, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Creates a new clone locale workflow for a skill with given skillId, source locale, and target locales. In a single workflow, a locale can be cloned to multiple target locales. However, only one such workflow can be started at any time. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage_v2: (required) Stages of a skill on which locales can be cloned. Currently only `development` stage is supported. * `development` - skills which are currently in development corresponds to this stage. 
        :type stage_v2: str
        :param clone_locale_request: (required) Defines the request body for the cloneLocale API.
        :type clone_locale_request: ask_smapi_model.v1.skill.clone_locale_request.CloneLocaleRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        operation_name = "clone_locale_v1"
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
        # verify the required parameter 'clone_locale_request' is set
        if ('clone_locale_request' not in params) or (params['clone_locale_request'] is None):
            raise ValueError(
                "Missing the required parameter `clone_locale_request` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stageV2}/cloneLocale'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage_v2' in params:
            path_params['stageV2'] = params['stage_v2']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'clone_locale_request' in params:
            body_params = params['clone_locale_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

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
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
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
        
        return None

    def get_clone_locale_status_v1(self, skill_id, stage_v2, clone_locale_request_id, **kwargs):
        # type: (str, str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, CloneLocaleStatusResponse_8b6e06ed]
        """
        Returns the status of a clone locale workflow associated with the unique identifier of cloneLocaleRequestId. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage_v2: (required) Stages of a skill on which locales can be cloned. Currently only `development` stage is supported. * `development` - skills which are currently in development corresponds to this stage. 
        :type stage_v2: str
        :param clone_locale_request_id: (required) Defines the identifier for a clone locale workflow. If set to ~latest, request returns the status of the latest clone locale workflow. 
        :type clone_locale_request_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, CloneLocaleStatusResponse_8b6e06ed]
        """
        operation_name = "get_clone_locale_status_v1"
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
        # verify the required parameter 'clone_locale_request_id' is set
        if ('clone_locale_request_id' not in params) or (params['clone_locale_request_id'] is None):
            raise ValueError(
                "Missing the required parameter `clone_locale_request_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/stages/{stageV2}/cloneLocaleRequests/{cloneLocaleRequestId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage_v2' in params:
            path_params['stageV2'] = params['stage_v2']
        if 'clone_locale_request_id' in params:
            path_params['cloneLocaleRequestId'] = params['clone_locale_request_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.clone_locale_status_response.CloneLocaleStatusResponse", status_code=200, message="OK."))
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
            response_type="ask_smapi_model.v1.skill.clone_locale_status_response.CloneLocaleStatusResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def get_interaction_model_v1(self, skill_id, stage_v2, locale, **kwargs):
        # type: (str, str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, InteractionModelData_487fc9ea]
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
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, InteractionModelData_487fc9ea]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (str, str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Get the latest metadata for the interaction model resource for the given stage. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage_v2: (required) Stages of a skill including the new certified stage. * `development` - skills which are currently in development corresponds to this stage. * `certified` -  skills which have completed certification and ready for publishing corresponds to this stage. * `live` - skills which are currently live corresponds to this stage. 
        :type stage_v2: str
        :param locale: (required) The locale for the model requested e.g. en-GB, en-US, de-DE.
        :type locale: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type=None, status_code=204, message="Success. There is no content but returns etag."))
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
        
        return None

    def set_interaction_model_v1(self, skill_id, stage_v2, locale, interaction_model, **kwargs):
        # type: (str, str, str, InteractionModelData_487fc9ea, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=400, message="Server cannot process the request due to a client error e.g. the input interaction model is invalid."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.bad_request_error.BadRequestError", status_code=403, message="The operation being requested is not allowed."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.standardized_error.StandardizedError", status_code=404, message="The specified skill or stage or locale does not exist."))
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
        
        return None

    def list_interaction_model_versions_v1(self, skill_id, stage_v2, locale, **kwargs):
        # type: (str, str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, ListResponse_cb936759]
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
        :type max_results: int
        :param sort_direction: Sets the sorting direction of the result items. When set to 'asc' these items are returned in ascending order of sortField value and when set to 'desc' these items are returned in descending order of sortField value.
        :type sort_direction: str
        :param sort_field: Sets the field on which the sorting would be applied.
        :type sort_field: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, ListResponse_cb936759]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (str, str, str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, InteractionModelData_487fc9ea]
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
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05, InteractionModelData_487fc9ea]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (str, str, **Any) -> Union[ApiResponse, object, SkillManifestEnvelope_fc0e823b, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Returns the skill manifest for given skillId and stage.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage_v2: (required) Stages of a skill including the new certified stage. * `development` - skills which are currently in development corresponds to this stage. * `certified` -  skills which have completed certification and ready for publishing corresponds to this stage. * `live` - skills which are currently live corresponds to this stage. 
        :type stage_v2: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, SkillManifestEnvelope_fc0e823b, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (str, str, SkillManifestEnvelope_fc0e823b, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def submit_skill_validation_v1(self, validations_api_request, skill_id, stage, **kwargs):
        # type: (ValidationsApiRequest_6f6e9aec, str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, ValidationsApiResponse_aa0c51ca]
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
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, ValidationsApiResponse_aa0c51ca]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (str, str, str, **Any) -> Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, ValidationsApiResponse_aa0c51ca]
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
        :rtype: Union[ApiResponse, object, Error_fbe913d9, BadRequestError_f854b05, ValidationsApiResponse_aa0c51ca]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (str, **Any) -> Union[ApiResponse, object, SkillStatus_4fdd647b, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Get the status of skill resource and its sub-resources for a given skillId.

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param resource: Resource name for which status information is desired. It is an optional, filtering parameter and can be used more than once, to retrieve status for all the desired (sub)resources only, in single API call. If this parameter is not specified, status for all the resources/sub-resources will be returned. 
        :type resource: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, SkillStatus_4fdd647b, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Submit the skill for certification. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param submit_skill_for_certification_request: Defines the request body for submitSkillForCertification API.
        :type submit_skill_for_certification_request: ask_smapi_model.v1.skill.submit_skill_for_certification_request.SubmitSkillForCertificationRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def list_versions_for_skill_v1(self, skill_id, **kwargs):
        # type: (str, **Any) -> Union[ApiResponse, object, ListSkillVersionsResponse_7522147d, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Retrieve a list of all skill versions associated with this skill id

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param next_token: When response to this API call is truncated (that is, isTruncated response element value is true), the response also includes the nextToken element. The value of nextToken can be used in the next request as the continuation-token to list the next set of objects. The continuation token is an opaque value that Skill Management API understands. Token has expiry of 24 hours.
        :type next_token: str
        :param max_results: Sets the maximum number of results returned in the response body. If you want to retrieve fewer than upper limit of 50 results, you can add this parameter to your request. maxResults should not exceed the upper limit. The response might contain fewer results than maxResults, but it will never contain more. If there are additional results that satisfy the search criteria, but these results were not returned, the response contains isTruncated = true.
        :type max_results: int
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, ListSkillVersionsResponse_7522147d, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        operation_name = "list_versions_for_skill_v1"
        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'skill_id' is set
        if ('skill_id' not in params) or (params['skill_id'] is None):
            raise ValueError(
                "Missing the required parameter `skill_id` when calling `" + operation_name + "`")

        resource_path = '/v1/skills/{skillId}/versions'
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
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v1.skill.list_skill_versions_response.ListSkillVersionsResponse", status_code=200, message="Successfully retrieved skill versions"))
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
            response_type="ask_smapi_model.v1.skill.list_skill_versions_response.ListSkillVersionsResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def withdraw_skill_from_certification_v1(self, skill_id, withdraw_request, **kwargs):
        # type: (str, WithdrawRequest_d09390b7, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
        """
        Withdraws the skill from certification. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param withdraw_request: (required) The reason and message (in case of OTHER) to withdraw a skill.
        :type withdraw_request: ask_smapi_model.v1.skill.withdraw_request.WithdrawRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, BadRequestError_f854b05]
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
        header_params.append(('User-Agent', self.user_agent))

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
        
        return None

    def create_upload_url_v1(self, **kwargs):
        # type: (**Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, UploadResponse_5aa06857]
        """
        Creates a new uploadUrl. 

        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, UploadResponse_5aa06857]
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
        header_params.append(('User-Agent', self.user_agent))

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
        # type: (**Any) -> Union[ApiResponse, object, Error_fbe913d9, Vendors_f5f1b90b]
        """
        Get the list of Vendor information. 

        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, Error_fbe913d9, Vendors_f5f1b90b]
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
        header_params.append(('User-Agent', self.user_agent))

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
        

    def get_alexa_hosted_skill_user_permissions_v1(self, vendor_id, hosted_skill_permission_type, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, StandardizedError_f5106a89, HostedSkillPermission_eb71ebfb, BadRequestError_f854b05]
        """
        Get the current user permissions about Alexa hosted skill features.

        :param vendor_id: (required) vendorId
        :type vendor_id: str
        :param hosted_skill_permission_type: (required) The permission of a hosted skill feature that customer needs to check.
        :type hosted_skill_permission_type: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, StandardizedError_f5106a89, HostedSkillPermission_eb71ebfb, BadRequestError_f854b05]
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
        # verify the required parameter 'hosted_skill_permission_type' is set
        if ('hosted_skill_permission_type' not in params) or (params['hosted_skill_permission_type'] is None):
            raise ValueError(
                "Missing the required parameter `hosted_skill_permission_type` when calling `" + operation_name + "`")

        resource_path = '/v1/vendors/{vendorId}/alexaHosted/permissions/{hostedSkillPermissionType}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'vendor_id' in params:
            path_params['vendorId'] = params['vendor_id']
        if 'hosted_skill_permission_type' in params:
            path_params['hostedSkillPermissionType'] = params['hosted_skill_permission_type']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

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
        

    def invoke_skill_end_point_v2(self, skill_id, stage, **kwargs):
        # type: (str, str, **Any) -> Union[ApiResponse, object, BadRequestError_765e0ac6, InvocationsApiResponse_3d7e3234, Error_ea6c1a5a]
        """
        Invokes the Lambda or third party HTTPS endpoint for the given skill against a given stage.
        This is a synchronous API that invokes the Lambda or third party HTTPS endpoint for a given skill. A successful response will contain information related to what endpoint was called, payload sent to and received from the endpoint. In cases where requests to this API results in an error, the response will contain an error code and a description of the problem. In cases where invoking the skill endpoint specifically fails, the response will contain a status attribute indicating that a failure occurred and details about what was sent to the endpoint. The skill must belong to and be enabled by the user of this API. Also,  note that calls to the skill endpoint will timeout after 10 seconds. This  API is currently designed in a way that allows extension to an asynchronous  API if a significantly bigger timeout is required. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param invocations_api_request: Payload sent to the skill invocation API.
        :type invocations_api_request: ask_smapi_model.v2.skill.invocations.invocations_api_request.InvocationsApiRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, BadRequestError_765e0ac6, InvocationsApiResponse_3d7e3234, Error_ea6c1a5a]
        """
        operation_name = "invoke_skill_end_point_v2"
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

        resource_path = '/v2/skills/{skillId}/stages/{stage}/invocations'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'invocations_api_request' in params:
            body_params = params['invocations_api_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.skill.invocations.invocations_api_response.InvocationsApiResponse", status_code=200, message="Skill was invoked."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.bad_request_error.BadRequestError", status_code=400, message="Bad request due to invalid or missing data."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.bad_request_error.BadRequestError", status_code=403, message="API user does not have permission to call this API or is currently in a state that does not allow invocation of this skill. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.error.Error", status_code=404, message="The specified skill does not exist."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.error.Error", status_code=429, message="API user has exceeded the permitted request rate."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.error.Error", status_code=500, message="Internal service error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v2.skill.invocations.invocations_api_response.InvocationsApiResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def simulate_skill_v2(self, skill_id, stage, simulations_api_request, **kwargs):
        # type: (str, str, SimulationsApiRequest_ae2e6503, **Any) -> Union[ApiResponse, object, SimulationsApiResponse_e4ad17d, BadRequestError_765e0ac6, Error_ea6c1a5a]
        """
        Simulate executing a skill with the given id against a given stage.
        This is an asynchronous API that simulates a skill execution in the Alexa eco-system given an utterance text of what a customer would say to Alexa. A successful response will contain a header with the location of the simulation resource. In cases where requests to this API results in an error, the response will contain an error code and a description of the problem. The skill being simulated must belong to and be enabled  by the user of this API. Concurrent requests per user is currently not supported. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param simulations_api_request: (required) Payload sent to the skill simulation API.
        :type simulations_api_request: ask_smapi_model.v2.skill.simulations.simulations_api_request.SimulationsApiRequest
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, SimulationsApiResponse_e4ad17d, BadRequestError_765e0ac6, Error_ea6c1a5a]
        """
        operation_name = "simulate_skill_v2"
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
        # verify the required parameter 'simulations_api_request' is set
        if ('simulations_api_request' not in params) or (params['simulations_api_request'] is None):
            raise ValueError(
                "Missing the required parameter `simulations_api_request` when calling `" + operation_name + "`")

        resource_path = '/v2/skills/{skillId}/stages/{stage}/simulations'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        if 'simulations_api_request' in params:
            body_params = params['simulations_api_request']
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.skill.simulations.simulations_api_response.SimulationsApiResponse", status_code=200, message="Skill simulation has successfully began."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.bad_request_error.BadRequestError", status_code=400, message="Bad request due to invalid or missing data."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.bad_request_error.BadRequestError", status_code=403, message="API user does not have permission to call this API or is currently in a state that does not allow simulation of this skill. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.error.Error", status_code=404, message="The specified skill does not exist."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.error.Error", status_code=409, message="This requests conflicts with another one currently being processed. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.error.Error", status_code=429, message="API user has exceeded the permitted request rate."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.error.Error", status_code=500, message="Internal service error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="POST",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v2.skill.simulations.simulations_api_response.SimulationsApiResponse")

        if full_response:
            return api_response
        return api_response.body
        

    def get_skill_simulation_v2(self, skill_id, stage, simulation_id, **kwargs):
        # type: (str, str, str, **Any) -> Union[ApiResponse, object, SimulationsApiResponse_e4ad17d, BadRequestError_765e0ac6, Error_ea6c1a5a]
        """
        Get the result of a previously executed simulation.
        This API gets the result of a previously executed simulation. A successful response will contain the status of the executed simulation. If the simulation successfully completed, the response will also contain information related to skill invocation. In cases where requests to this API results in an error, the response will contain an error code and a description of the problem. In cases where the simulation failed, the response will contain a status attribute indicating that a failure occurred and details about what was sent to the skill endpoint. Note that simulation results are stored for 10 minutes. A request for an expired simulation result will return a 404 HTTP status code. 

        :param skill_id: (required) The skill ID.
        :type skill_id: str
        :param stage: (required) Stage for skill.
        :type stage: str
        :param simulation_id: (required) Id of the simulation.
        :type simulation_id: str
        :param full_response: Boolean value to check if response should contain headers and status code information.
            This value had to be passed through keyword arguments, by default the parameter value is set to False. 
        :type full_response: boolean
        :rtype: Union[ApiResponse, object, SimulationsApiResponse_e4ad17d, BadRequestError_765e0ac6, Error_ea6c1a5a]
        """
        operation_name = "get_skill_simulation_v2"
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
        # verify the required parameter 'simulation_id' is set
        if ('simulation_id' not in params) or (params['simulation_id'] is None):
            raise ValueError(
                "Missing the required parameter `simulation_id` when calling `" + operation_name + "`")

        resource_path = '/v2/skills/{skillId}/stages/{stage}/simulations/{simulationId}'
        resource_path = resource_path.replace('{format}', 'json')

        path_params = {}  # type: Dict
        if 'skill_id' in params:
            path_params['skillId'] = params['skill_id']
        if 'stage' in params:
            path_params['stage'] = params['stage']
        if 'simulation_id' in params:
            path_params['simulationId'] = params['simulation_id']

        query_params = []  # type: List

        header_params = []  # type: List

        body_params = None
        header_params.append(('Content-type', 'application/json'))
        header_params.append(('User-Agent', self.user_agent))

        # Response Type
        full_response = False
        if 'full_response' in params:
            full_response = params['full_response']

        # Authentication setting
        access_token = self._lwa_service_client.get_access_token_from_refresh_token()
        authorization_value = "Bearer " + access_token
        header_params.append(('Authorization', authorization_value))

        error_definitions = []  # type: List
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.skill.simulations.simulations_api_response.SimulationsApiResponse", status_code=200, message="Successfully retrieved skill simulation information."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.error.Error", status_code=401, message="The auth token is invalid/expired or doesn&#39;t have access to the resource."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.bad_request_error.BadRequestError", status_code=403, message="API user does not have permission or is currently in a state that does not allow calls to this API. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.error.Error", status_code=404, message="The specified skill or simulation does not exist. The error response will contain a description that indicates the specific resource type that was not found. "))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.error.Error", status_code=429, message="API user has exceeded the permitted request rate."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.error.Error", status_code=500, message="Internal service error."))
        error_definitions.append(ServiceClientResponse(response_type="ask_smapi_model.v2.error.Error", status_code=503, message="Service Unavailable."))

        api_response = self.invoke(
            method="GET",
            endpoint=self._api_endpoint,
            path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            response_definitions=error_definitions,
            response_type="ask_smapi_model.v2.skill.simulations.simulations_api_response.SimulationsApiResponse")

        if full_response:
            return api_response
        return api_response.body
        
