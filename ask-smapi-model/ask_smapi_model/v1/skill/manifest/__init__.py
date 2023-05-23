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

from .event_name import EventName
from .data_store_package import DataStorePackage
from .skill_manifest_envelope import SkillManifestEnvelope
from .alexa_search import AlexaSearch
from .amazon_conversations_dialog_manager import AMAZONConversationsDialogManager
from .version import Version
from .flash_briefing_genre import FlashBriefingGenre
from .distribution_mode import DistributionMode
from .custom_connections import CustomConnections
from .video_apis import VideoApis
from .music_content_name import MusicContentName
from .house_hold_list import HouseHoldList
from .skill_manifest_endpoint import SkillManifestEndpoint
from .game_engine_interface import GameEngineInterface
from .video_apis_locale import VideoApisLocale
from .knowledge_apis import KnowledgeApis
from .custom_apis import CustomApis
from .skill_manifest_localized_publishing_information import SkillManifestLocalizedPublishingInformation
from .app_link_interface import AppLinkInterface
from .music_capability import MusicCapability
from .knowledge_apis_enablement_channel import KnowledgeApisEnablementChannel
from .localized_music_info import LocalizedMusicInfo
from .ios_app_store_common_scheme_name import IOSAppStoreCommonSchemeName
from .video_catalog_info import VideoCatalogInfo
from .subscription_information import SubscriptionInformation
from .shopping_kit import ShoppingKit
from .dialog_manager import DialogManager
from .supported_controls import SupportedControls
from .distribution_countries import DistributionCountries
from .video_country_info import VideoCountryInfo
from .custom_product_prompts import CustomProductPrompts
from .display_interface_apml_version import DisplayInterfaceApmlVersion
from .alexa_data_store_package_manager_interface import AlexaDataStorePackageManagerInterface
from .event_name_type import EventNameType
from .viewport_shape import ViewportShape
from .dialog_management import DialogManagement
from .offer_type import OfferType
from .localized_flash_briefing_info import LocalizedFlashBriefingInfo
from .up_channel_items import UpChannelItems
from .flash_briefing_update_frequency import FlashBriefingUpdateFrequency
from .flash_briefing_apis import FlashBriefingApis
from .authorized_client_lwa_application_android import AuthorizedClientLwaApplicationAndroid
from .smart_home_apis import SmartHomeApis
from .currency import Currency
from .video_fire_tv_catalog_ingestion import VideoFireTvCatalogIngestion
from .video_prompt_name import VideoPromptName
from .authorized_client_lwa import AuthorizedClientLwa
from .skill_manifest_publishing_information import SkillManifestPublishingInformation
from .catalog_name import CatalogName
from .extension_request import ExtensionRequest
from .gadget_support_requirement import GadgetSupportRequirement
from .app_link_v2_interface import AppLinkV2Interface
from .skill_manifest_apis import SkillManifestApis
from .viewport_specification import ViewportSpecification
from .display_interface_template_version import DisplayInterfaceTemplateVersion
from .play_store_common_scheme_name import PlayStoreCommonSchemeName
from .region import Region
from .music_alias import MusicAlias
from .video_region import VideoRegion
from .video_feature import VideoFeature
from .android_common_intent_name import AndroidCommonIntentName
from .catalog_info import CatalogInfo
from .manifest_gadget_support import ManifestGadgetSupport
from .interface_type import InterfaceType
from .extension_initialization_request import ExtensionInitializationRequest
from .skill_manifest_localized_privacy_and_compliance import SkillManifestLocalizedPrivacyAndCompliance
from .friendly_name import FriendlyName
from .localized_knowledge_information import LocalizedKnowledgeInformation
from .automatic_distribution import AutomaticDistribution
from .skill_manifest_events import SkillManifestEvents
from .permission_items import PermissionItems
from .alexa_for_business_interface_request_name import AlexaForBusinessInterfaceRequestName
from .authorized_client_lwa_application import AuthorizedClientLwaApplication
from .alexa_for_business_interface_request import AlexaForBusinessInterfaceRequest
from .linked_common_schemes import LinkedCommonSchemes
from .authorized_client import AuthorizedClient
from .smart_home_protocol import SmartHomeProtocol
from .audio_interface import AudioInterface
from .custom_localized_information import CustomLocalizedInformation
from .music_apis import MusicApis
from .music_request import MusicRequest
from .demand_response_apis import DemandResponseApis
from .subscription_payment_frequency import SubscriptionPaymentFrequency
from .manifest_version import ManifestVersion
from .alexa_data_store_package_manager_implemented_interface import AlexaDataStorePackageManagerImplementedInterface
from .tax_information import TaxInformation
from .custom_task import CustomTask
from .permission_name import PermissionName
from .skill_manifest import SkillManifest
from .ssl_certificate_type import SSLCertificateType
from .linked_android_common_intent import LinkedAndroidCommonIntent
from .lambda_endpoint import LambdaEndpoint
from .alexa_presentation_html_interface import AlexaPresentationHtmlInterface
from .alexa_presentation_apl_interface import AlexaPresentationAplInterface
from .alexa_for_business_apis import AlexaForBusinessApis
from .localized_flash_briefing_info_items import LocalizedFlashBriefingInfoItems
from .viewport_mode import ViewportMode
from .source_language_for_locales import SourceLanguageForLocales
from .music_content_type import MusicContentType
from .locales_by_automatic_cloned_locale import LocalesByAutomaticClonedLocale
from .event_publications import EventPublications
from .voice_profile_feature import VoiceProfileFeature
from .free_trial_information import FreeTrialInformation
from .custom_localized_information_dialog_management import CustomLocalizedInformationDialogManagement
from .video_prompt_name_type import VideoPromptNameType
from .interface import Interface
from .display_interface import DisplayInterface
from .automatic_cloned_locale import AutomaticClonedLocale
from .gadget_controller_interface import GadgetControllerInterface
from .paid_skill_information import PaidSkillInformation
from .marketplace_pricing import MarketplacePricing
from .tax_information_category import TaxInformationCategory
from .lambda_region import LambdaRegion
from .localized_name import LocalizedName
from .music_wordmark import MusicWordmark
from .health_interface import HealthInterface
from .catalog_type import CatalogType
from .music_feature import MusicFeature
from .music_interfaces import MusicInterfaces
from .connections_payload import ConnectionsPayload
from .alexa_for_business_interface import AlexaForBusinessInterface
from .dialog_delegation_strategy import DialogDelegationStrategy
from .app_link import AppLink
from .android_custom_intent import AndroidCustomIntent
from .linked_application import LinkedApplication
from .supported_controls_type import SupportedControlsType
from .flash_briefing_content_type import FlashBriefingContentType
from .skill_manifest_privacy_and_compliance import SkillManifestPrivacyAndCompliance
from .video_app_interface import VideoAppInterface
from .lambda_ssl_certificate_type import LambdaSSLCertificateType
