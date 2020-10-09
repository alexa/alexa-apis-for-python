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


class PermissionName(Enum):
    """
    Name of the required permission.



    Allowed enum values: [payments_autopay_consent, alexa_async_event_write, avs_distributed_audio, alexa_devices_all_address_full_read, alexa_devices_all_address_country_and_postal_code_read, alexa_devices_all_geolocation_read, alexa_health_profile_write, alexa_household_lists_read, alexa_household_lists_write, alexa_personality_explicit_read, alexa_personality_explicit_write, alexa_profile_name_read, alexa_profile_email_read, alexa_profile_mobile_number_read, alexa_profile_given_name_read, alexa_customer_id_read, alexa_person_id_read, alexa_raw_person_id_read, alexa_utterance_id_read, alexa_devices_all_notifications_write, alexa_devices_all_notifications_urgent_write, alexa_alerts_reminders_skill_readwrite, alexa_alerts_timers_skill_readwrite, alexa_skill_cds_monetization, alexa_music_cast, alexa_skill_products_entitlements, alexa_skill_proactive_enablement, alexa_authenticate_2_mandatory, alexa_authenticate_2_optional, alexa_user_experience_guidance_read, alexa_device_id_read, alexa_device_type_read]
    """
    payments_autopay_consent = "payments:autopay_consent"
    alexa_async_event_write = "alexa::async_event:write"
    avs_distributed_audio = "avs::distributed_audio"
    alexa_devices_all_address_full_read = "alexa::devices:all:address:full:read"
    alexa_devices_all_address_country_and_postal_code_read = "alexa:devices:all:address:country_and_postal_code:read"
    alexa_devices_all_geolocation_read = "alexa::devices:all:geolocation:read"
    alexa_health_profile_write = "alexa::health:profile:write"
    alexa_household_lists_read = "alexa::household:lists:read"
    alexa_household_lists_write = "alexa::household:lists:write"
    alexa_personality_explicit_read = "alexa::personality:explicit:read"
    alexa_personality_explicit_write = "alexa::personality:explicit:write"
    alexa_profile_name_read = "alexa::profile:name:read"
    alexa_profile_email_read = "alexa::profile:email:read"
    alexa_profile_mobile_number_read = "alexa::profile:mobile_number:read"
    alexa_profile_given_name_read = "alexa::profile:given_name:read"
    alexa_customer_id_read = "alexa::customer_id:read"
    alexa_person_id_read = "alexa::person_id:read"
    alexa_raw_person_id_read = "alexa::raw_person_id:read"
    alexa_utterance_id_read = "alexa::utterance_id:read"
    alexa_devices_all_notifications_write = "alexa::devices:all:notifications:write"
    alexa_devices_all_notifications_urgent_write = "alexa::devices:all:notifications:urgent:write"
    alexa_alerts_reminders_skill_readwrite = "alexa::alerts:reminders:skill:readwrite"
    alexa_alerts_timers_skill_readwrite = "alexa::alerts:timers:skill:readwrite"
    alexa_skill_cds_monetization = "alexa::skill:cds:monetization"
    alexa_music_cast = "alexa::music:cast"
    alexa_skill_products_entitlements = "alexa::skill:products:entitlements"
    alexa_skill_proactive_enablement = "alexa::skill:proactive_enablement"
    alexa_authenticate_2_mandatory = "alexa::authenticate:2:mandatory"
    alexa_authenticate_2_optional = "alexa::authenticate:2:optional"
    alexa_user_experience_guidance_read = "alexa::user_experience_guidance:read"
    alexa_device_id_read = "alexa::device_id:read"
    alexa_device_type_read = "alexa::device_type:read"

    def to_dict(self):
        # type: () -> Dict[str, Any]
        """Returns the model properties as a dict"""
        result = {self.name: self.value}
        return result

    def to_str(self):
        # type: () -> str
        """Returns the string representation of the model"""
        return pprint.pformat(self.value)

    def __repr__(self):
        # type: () -> str
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        # type: (Any) -> bool
        """Returns true if both objects are equal"""
        if not isinstance(other, PermissionName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (Any) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
