# coding: utf-8

#
# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License'). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the 'license' file accompanying this file. This file is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for
# the specific language governing permissions and limitations under the License.
#
from __future__ import absolute_import

from .audio_interface import AudioInterface
from .interface import Interface
from .free_trial_information import FreeTrialInformation
from .localized_flash_briefing_info import LocalizedFlashBriefingInfo
from .demand_response_apis import DemandResponseApis
from .automatic_distribution import AutomaticDistribution
from .video_region import VideoRegion
from .authorized_client_lwa_application_android import AuthorizedClientLwaApplicationAndroid
from .music_content_name import MusicContentName
from .custom_product_prompts import CustomProductPrompts
from .event_name_type import EventNameType
from .skill_manifest_localized_privacy_and_compliance import SkillManifestLocalizedPrivacyAndCompliance
from .video_fire_tv_catalog_ingestion import VideoFireTvCatalogIngestion
from .friendly_name import FriendlyName
from .up_channel_items import UpChannelItems
from .health_interface import HealthInterface
from .subscription_payment_frequency import SubscriptionPaymentFrequency
from .source_language_for_locales import SourceLanguageForLocales
from .flash_briefing_update_frequency import FlashBriefingUpdateFrequency
from .smart_home_protocol import SmartHomeProtocol
from .lambda_endpoint import LambdaEndpoint
from .video_prompt_name import VideoPromptName
from .event_name import EventName
from .music_content_type import MusicContentType
from .music_apis import MusicApis
from .music_alias import MusicAlias
from .knowledge_apis import KnowledgeApis
from .manifest_gadget_support import ManifestGadgetSupport
from .dialog_management import DialogManagement
from .offer_type import OfferType
from .house_hold_list import HouseHoldList
from .linked_common_schemes import LinkedCommonSchemes
from .interface_type import InterfaceType
from .authorized_client_lwa import AuthorizedClientLwa
from .lambda_region import LambdaRegion
from .video_catalog_info import VideoCatalogInfo
from .extension_initialization_request import ExtensionInitializationRequest
from .dialog_manager import DialogManager
from .custom_apis import CustomApis
from .voice_profile_feature import VoiceProfileFeature
from .skill_manifest import SkillManifest
from .data_store_package import DataStorePackage
from .alexa_data_store_package_manager_interface import AlexaDataStorePackageManagerInterface
from .automatic_cloned_locale import AutomaticClonedLocale
from .marketplace_pricing import MarketplacePricing
from .alexa_presentation_apl_interface import AlexaPresentationAplInterface
from .alexa_presentation_html_interface import AlexaPresentationHtmlInterface
from .tax_information import TaxInformation
from .viewport_specification import ViewportSpecification
from .skill_manifest_privacy_and_compliance import SkillManifestPrivacyAndCompliance
from .authorized_client import AuthorizedClient
from .permission_items import PermissionItems
from .alexa_for_business_interface import AlexaForBusinessInterface
from .version import Version
from .app_link import AppLink
from .alexa_search import AlexaSearch
from .music_interfaces import MusicInterfaces
from .region import Region
from .alexa_for_business_apis import AlexaForBusinessApis
from .authorized_client_lwa_application import AuthorizedClientLwaApplication
from .supported_controls_type import SupportedControlsType
from .skill_manifest_events import SkillManifestEvents
from .custom_connections import CustomConnections
from .extension_request import ExtensionRequest
from .flash_briefing_genre import FlashBriefingGenre
from .alexa_for_business_interface_request import AlexaForBusinessInterfaceRequest
from .smart_home_apis import SmartHomeApis
from .localized_music_info import LocalizedMusicInfo
from .video_prompt_name_type import VideoPromptNameType
from .amazon_conversations_dialog_manager import AMAZONConversationsDialogManager
from .play_store_common_scheme_name import PlayStoreCommonSchemeName
from .catalog_type import CatalogType
from .knowledge_apis_enablement_channel import KnowledgeApisEnablementChannel
from .app_link_interface import AppLinkInterface
from .music_request import MusicRequest
from .permission_name import PermissionName
from .display_interface_template_version import DisplayInterfaceTemplateVersion
from .skill_manifest_localized_publishing_information import SkillManifestLocalizedPublishingInformation
from .custom_task import CustomTask
from .skill_manifest_envelope import SkillManifestEnvelope
from .dialog_delegation_strategy import DialogDelegationStrategy
from .locales_by_automatic_cloned_locale import LocalesByAutomaticClonedLocale
from .currency import Currency
from .distribution_countries import DistributionCountries
from .localized_name import LocalizedName
from .linked_application import LinkedApplication
from .distribution_mode import DistributionMode
from .custom_localized_information_dialog_management import CustomLocalizedInformationDialogManagement
from .supported_controls import SupportedControls
from .video_apis import VideoApis
from .localized_knowledge_information import LocalizedKnowledgeInformation
from .linked_android_common_intent import LinkedAndroidCommonIntent
from .gadget_controller_interface import GadgetControllerInterface
from .event_publications import EventPublications
from .connections_payload import ConnectionsPayload
from .shopping_kit import ShoppingKit
from .ios_app_store_common_scheme_name import IOSAppStoreCommonSchemeName
from .manifest_version import ManifestVersion
from .viewport_shape import ViewportShape
from .alexa_data_store_package_manager_implemented_interface import AlexaDataStorePackageManagerImplementedInterface
from .catalog_info import CatalogInfo
from .display_interface_apml_version import DisplayInterfaceApmlVersion
from .video_app_interface import VideoAppInterface
from .tax_information_category import TaxInformationCategory
from .android_common_intent_name import AndroidCommonIntentName
from .music_capability import MusicCapability
from .subscription_information import SubscriptionInformation
from .viewport_mode import ViewportMode
from .flash_briefing_apis import FlashBriefingApis
from .flash_briefing_content_type import FlashBriefingContentType
from .custom_localized_information import CustomLocalizedInformation
from .gadget_support_requirement import GadgetSupportRequirement
from .game_engine_interface import GameEngineInterface
from .localized_flash_briefing_info_items import LocalizedFlashBriefingInfoItems
from .catalog_name import CatalogName
from .skill_manifest_endpoint import SkillManifestEndpoint
from .music_wordmark import MusicWordmark
from .paid_skill_information import PaidSkillInformation
from .video_feature import VideoFeature
from .skill_manifest_publishing_information import SkillManifestPublishingInformation
from .android_custom_intent import AndroidCustomIntent
from .app_link_v2_interface import AppLinkV2Interface
from .video_apis_locale import VideoApisLocale
from .music_feature import MusicFeature
from .ssl_certificate_type import SSLCertificateType
from .alexa_for_business_interface_request_name import AlexaForBusinessInterfaceRequestName
from .video_country_info import VideoCountryInfo
from .lambda_ssl_certificate_type import LambdaSSLCertificateType
from .skill_manifest_apis import SkillManifestApis
from .display_interface import DisplayInterface
