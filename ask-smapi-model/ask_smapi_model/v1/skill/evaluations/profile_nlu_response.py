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
    from ask_smapi_model.v1.skill.evaluations.profile_nlu_selected_intent import ProfileNluSelectedIntent as Evaluations_ProfileNluSelectedIntentV1
    from ask_smapi_model.v1.skill.evaluations.intent import Intent as Evaluations_IntentV1
    from ask_smapi_model.v1.skill.evaluations.multi_turn import MultiTurn as Evaluations_MultiTurnV1


class ProfileNluResponse(object):
    """

    :param session_ended: Represents when an utterance results in the skill exiting. It would be true when NLU selects 1P ExitAppIntent or GoHomeIntent, and false otherwise. 
    :type session_ended: (optional) bool
    :param selected_intent: 
    :type selected_intent: (optional) ask_smapi_model.v1.skill.evaluations.profile_nlu_selected_intent.ProfileNluSelectedIntent
    :param considered_intents: All intents that Alexa considered for the utterance in the request, but did not select.
    :type considered_intents: (optional) list[ask_smapi_model.v1.skill.evaluations.intent.Intent]
    :param multi_turn: 
    :type multi_turn: (optional) ask_smapi_model.v1.skill.evaluations.multi_turn.MultiTurn

    """
    deserialized_types = {
        'session_ended': 'bool',
        'selected_intent': 'ask_smapi_model.v1.skill.evaluations.profile_nlu_selected_intent.ProfileNluSelectedIntent',
        'considered_intents': 'list[ask_smapi_model.v1.skill.evaluations.intent.Intent]',
        'multi_turn': 'ask_smapi_model.v1.skill.evaluations.multi_turn.MultiTurn'
    }  # type: Dict

    attribute_map = {
        'session_ended': 'sessionEnded',
        'selected_intent': 'selectedIntent',
        'considered_intents': 'consideredIntents',
        'multi_turn': 'multiTurn'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, session_ended=None, selected_intent=None, considered_intents=None, multi_turn=None):
        # type: (Optional[bool], Optional[Evaluations_ProfileNluSelectedIntentV1], Optional[List[Evaluations_IntentV1]], Optional[Evaluations_MultiTurnV1]) -> None
        """

        :param session_ended: Represents when an utterance results in the skill exiting. It would be true when NLU selects 1P ExitAppIntent or GoHomeIntent, and false otherwise. 
        :type session_ended: (optional) bool
        :param selected_intent: 
        :type selected_intent: (optional) ask_smapi_model.v1.skill.evaluations.profile_nlu_selected_intent.ProfileNluSelectedIntent
        :param considered_intents: All intents that Alexa considered for the utterance in the request, but did not select.
        :type considered_intents: (optional) list[ask_smapi_model.v1.skill.evaluations.intent.Intent]
        :param multi_turn: 
        :type multi_turn: (optional) ask_smapi_model.v1.skill.evaluations.multi_turn.MultiTurn
        """
        self.__discriminator_value = None  # type: str

        self.session_ended = session_ended
        self.selected_intent = selected_intent
        self.considered_intents = considered_intents
        self.multi_turn = multi_turn

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
        if not isinstance(other, ProfileNluResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
