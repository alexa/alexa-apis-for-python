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

import pprint
import re  # noqa: F401
import six
import typing
from enum import Enum
from abc import ABCMeta, abstractmethod


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional
    from datetime import datetime


class Directive(object):
    """

    :param object_type: 
    :type object_type: (optional) str

    .. note::

        This is an abstract class. Use the following mapping, to figure out
        the model class to be instantiated, that sets ``type`` variable.

        | AudioPlayer.Stop: :py:class:`ask_sdk_model.interfaces.audioplayer.stop_directive.StopDirective`,
        |
        | Dialog.ConfirmSlot: :py:class:`ask_sdk_model.dialog.confirm_slot_directive.ConfirmSlotDirective`,
        |
        | AudioPlayer.Play: :py:class:`ask_sdk_model.interfaces.audioplayer.play_directive.PlayDirective`,
        |
        | Connections.SendRequest: :py:class:`ask_sdk_model.interfaces.connections.send_request_directive.SendRequestDirective`,
        |
        | Display.RenderTemplate: :py:class:`ask_sdk_model.interfaces.display.render_template_directive.RenderTemplateDirective`,
        |
        | GadgetController.SetLight: :py:class:`ask_sdk_model.interfaces.gadget_controller.set_light_directive.SetLightDirective`,
        |
        | Dialog.Delegate: :py:class:`ask_sdk_model.dialog.delegate_directive.DelegateDirective`,
        |
        | Hint: :py:class:`ask_sdk_model.interfaces.display.hint_directive.HintDirective`,
        |
        | Dialog.ConfirmIntent: :py:class:`ask_sdk_model.dialog.confirm_intent_directive.ConfirmIntentDirective`,
        |
        | GameEngine.StartInputHandler: :py:class:`ask_sdk_model.interfaces.game_engine.start_input_handler_directive.StartInputHandlerDirective`,
        |
        | VideoApp.Launch: :py:class:`ask_sdk_model.interfaces.videoapp.launch_directive.LaunchDirective`,
        |
        | GameEngine.StopInputHandler: :py:class:`ask_sdk_model.interfaces.game_engine.stop_input_handler_directive.StopInputHandlerDirective`,
        |
        | Connections.SendResponse: :py:class:`ask_sdk_model.interfaces.connections.send_response_directive.SendResponseDirective`,
        |
        | Dialog.ElicitSlot: :py:class:`ask_sdk_model.dialog.elicit_slot_directive.ElicitSlotDirective`,
        |
        | AudioPlayer.ClearQueue: :py:class:`ask_sdk_model.interfaces.audioplayer.clear_queue_directive.ClearQueueDirective`

    """
    deserialized_types = {
        'object_type': 'str'
    }

    attribute_map = {
        'object_type': 'type'
    }

    discriminator_value_class_map = {
        'AudioPlayer.Stop': 'ask_sdk_model.interfaces.audioplayer.stop_directive.StopDirective',
        'Dialog.ConfirmSlot': 'ask_sdk_model.dialog.confirm_slot_directive.ConfirmSlotDirective',
        'AudioPlayer.Play': 'ask_sdk_model.interfaces.audioplayer.play_directive.PlayDirective',
        'Connections.SendRequest': 'ask_sdk_model.interfaces.connections.send_request_directive.SendRequestDirective',
        'Display.RenderTemplate': 'ask_sdk_model.interfaces.display.render_template_directive.RenderTemplateDirective',
        'GadgetController.SetLight': 'ask_sdk_model.interfaces.gadget_controller.set_light_directive.SetLightDirective',
        'Dialog.Delegate': 'ask_sdk_model.dialog.delegate_directive.DelegateDirective',
        'Hint': 'ask_sdk_model.interfaces.display.hint_directive.HintDirective',
        'Dialog.ConfirmIntent': 'ask_sdk_model.dialog.confirm_intent_directive.ConfirmIntentDirective',
        'GameEngine.StartInputHandler': 'ask_sdk_model.interfaces.game_engine.start_input_handler_directive.StartInputHandlerDirective',
        'VideoApp.Launch': 'ask_sdk_model.interfaces.videoapp.launch_directive.LaunchDirective',
        'GameEngine.StopInputHandler': 'ask_sdk_model.interfaces.game_engine.stop_input_handler_directive.StopInputHandlerDirective',
        'Connections.SendResponse': 'ask_sdk_model.interfaces.connections.send_response_directive.SendResponseDirective',
        'Dialog.ElicitSlot': 'ask_sdk_model.dialog.elicit_slot_directive.ElicitSlotDirective',
        'AudioPlayer.ClearQueue': 'ask_sdk_model.interfaces.audioplayer.clear_queue_directive.ClearQueueDirective'
    }

    json_discriminator_key = "type"

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, object_type=None):
        # type: (Optional[str]) -> None
        """

        :param object_type: 
        :type object_type: (optional) str
        """
        self.__discriminator_value = None

        self.object_type = object_type

    @classmethod
    def get_real_child_model(cls, data):
        # type: (Dict[str, str]) -> str
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[cls.json_discriminator_key]
        return cls.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        # type: () -> Dict[str, object]
        """Returns the model properties as a dict"""
        result = {}

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
        if not isinstance(other, Directive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
