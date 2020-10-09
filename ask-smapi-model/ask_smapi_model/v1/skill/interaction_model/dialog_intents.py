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
    from ask_smapi_model.v1.skill.interaction_model.dialog_slot_items import DialogSlotItems as InteractionModel_DialogSlotItemsV1
    from ask_smapi_model.v1.skill.interaction_model.dialog_intents_prompts import DialogIntentsPrompts as InteractionModel_DialogIntentsPromptsV1
    from ask_smapi_model.v1.skill.interaction_model.delegation_strategy_type import DelegationStrategyType as InteractionModel_DelegationStrategyTypeV1


class DialogIntents(object):
    """

    :param name: Name of the intent that has a dialog specification.
    :type name: (optional) str
    :param delegation_strategy: Defines an intent-specific delegation strategy for this dialog intent. Overrides dialog-level setting.
    :type delegation_strategy: (optional) ask_smapi_model.v1.skill.interaction_model.delegation_strategy_type.DelegationStrategyType
    :param slots: List of slots that have dialog rules.
    :type slots: (optional) list[ask_smapi_model.v1.skill.interaction_model.dialog_slot_items.DialogSlotItems]
    :param confirmation_required: Describes whether confirmation of the intent is required.
    :type confirmation_required: (optional) bool
    :param prompts: 
    :type prompts: (optional) ask_smapi_model.v1.skill.interaction_model.dialog_intents_prompts.DialogIntentsPrompts

    """
    deserialized_types = {
        'name': 'str',
        'delegation_strategy': 'ask_smapi_model.v1.skill.interaction_model.delegation_strategy_type.DelegationStrategyType',
        'slots': 'list[ask_smapi_model.v1.skill.interaction_model.dialog_slot_items.DialogSlotItems]',
        'confirmation_required': 'bool',
        'prompts': 'ask_smapi_model.v1.skill.interaction_model.dialog_intents_prompts.DialogIntentsPrompts'
    }  # type: Dict

    attribute_map = {
        'name': 'name',
        'delegation_strategy': 'delegationStrategy',
        'slots': 'slots',
        'confirmation_required': 'confirmationRequired',
        'prompts': 'prompts'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, name=None, delegation_strategy=None, slots=None, confirmation_required=None, prompts=None):
        # type: (Optional[str], Optional[InteractionModel_DelegationStrategyTypeV1], Optional[List[InteractionModel_DialogSlotItemsV1]], Optional[bool], Optional[InteractionModel_DialogIntentsPromptsV1]) -> None
        """

        :param name: Name of the intent that has a dialog specification.
        :type name: (optional) str
        :param delegation_strategy: Defines an intent-specific delegation strategy for this dialog intent. Overrides dialog-level setting.
        :type delegation_strategy: (optional) ask_smapi_model.v1.skill.interaction_model.delegation_strategy_type.DelegationStrategyType
        :param slots: List of slots that have dialog rules.
        :type slots: (optional) list[ask_smapi_model.v1.skill.interaction_model.dialog_slot_items.DialogSlotItems]
        :param confirmation_required: Describes whether confirmation of the intent is required.
        :type confirmation_required: (optional) bool
        :param prompts: 
        :type prompts: (optional) ask_smapi_model.v1.skill.interaction_model.dialog_intents_prompts.DialogIntentsPrompts
        """
        self.__discriminator_value = None  # type: str

        self.name = name
        self.delegation_strategy = delegation_strategy
        self.slots = slots
        self.confirmation_required = confirmation_required
        self.prompts = prompts

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
        if not isinstance(other, DialogIntents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
