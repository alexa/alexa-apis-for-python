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
    from ask_smapi_model.v1.skill.history.dialog_act import DialogAct as History_DialogActV1
    from ask_smapi_model.v1.skill.history.publication_status import PublicationStatus as History_PublicationStatusV1
    from ask_smapi_model.v1.stage_type import StageType as V1_StageTypeV1
    from ask_smapi_model.v1.skill.history.interaction_type import InteractionType as History_InteractionTypeV1
    from ask_smapi_model.v1.skill.history.intent_request_locales import IntentRequestLocales as History_IntentRequestLocalesV1
    from ask_smapi_model.v1.skill.history.intent import Intent as History_IntentV1


class IntentRequest(object):
    """

    :param dialog_act: 
    :type dialog_act: (optional) ask_smapi_model.v1.skill.history.dialog_act.DialogAct
    :param intent: 
    :type intent: (optional) ask_smapi_model.v1.skill.history.intent.Intent
    :param interaction_type: 
    :type interaction_type: (optional) ask_smapi_model.v1.skill.history.interaction_type.InteractionType
    :param locale: 
    :type locale: (optional) ask_smapi_model.v1.skill.history.intent_request_locales.IntentRequestLocales
    :param publication_status: 
    :type publication_status: (optional) ask_smapi_model.v1.skill.history.publication_status.PublicationStatus
    :param stage: 
    :type stage: (optional) ask_smapi_model.v1.stage_type.StageType
    :param utterance_text: The transcribed user speech.
    :type utterance_text: (optional) str

    """
    deserialized_types = {
        'dialog_act': 'ask_smapi_model.v1.skill.history.dialog_act.DialogAct',
        'intent': 'ask_smapi_model.v1.skill.history.intent.Intent',
        'interaction_type': 'ask_smapi_model.v1.skill.history.interaction_type.InteractionType',
        'locale': 'ask_smapi_model.v1.skill.history.intent_request_locales.IntentRequestLocales',
        'publication_status': 'ask_smapi_model.v1.skill.history.publication_status.PublicationStatus',
        'stage': 'ask_smapi_model.v1.stage_type.StageType',
        'utterance_text': 'str'
    }  # type: Dict

    attribute_map = {
        'dialog_act': 'dialogAct',
        'intent': 'intent',
        'interaction_type': 'interactionType',
        'locale': 'locale',
        'publication_status': 'publicationStatus',
        'stage': 'stage',
        'utterance_text': 'utteranceText'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, dialog_act=None, intent=None, interaction_type=None, locale=None, publication_status=None, stage=None, utterance_text=None):
        # type: (Optional[History_DialogActV1], Optional[History_IntentV1], Optional[History_InteractionTypeV1], Optional[History_IntentRequestLocalesV1], Optional[History_PublicationStatusV1], Optional[V1_StageTypeV1], Optional[str]) -> None
        """

        :param dialog_act: 
        :type dialog_act: (optional) ask_smapi_model.v1.skill.history.dialog_act.DialogAct
        :param intent: 
        :type intent: (optional) ask_smapi_model.v1.skill.history.intent.Intent
        :param interaction_type: 
        :type interaction_type: (optional) ask_smapi_model.v1.skill.history.interaction_type.InteractionType
        :param locale: 
        :type locale: (optional) ask_smapi_model.v1.skill.history.intent_request_locales.IntentRequestLocales
        :param publication_status: 
        :type publication_status: (optional) ask_smapi_model.v1.skill.history.publication_status.PublicationStatus
        :param stage: 
        :type stage: (optional) ask_smapi_model.v1.stage_type.StageType
        :param utterance_text: The transcribed user speech.
        :type utterance_text: (optional) str
        """
        self.__discriminator_value = None  # type: str

        self.dialog_act = dialog_act
        self.intent = intent
        self.interaction_type = interaction_type
        self.locale = locale
        self.publication_status = publication_status
        self.stage = stage
        self.utterance_text = utterance_text

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
        if not isinstance(other, IntentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
