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


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional
    from datetime import datetime
    from ask_sdk_model.interfaces.system.system_state import SystemState
    from ask_sdk_model.interfaces.audioplayer.audio_player_state import AudioPlayerState
    from ask_sdk_model.interfaces.viewport.viewport_state import ViewportState
    from ask_sdk_model.interfaces.display.display_state import DisplayState


class Context(object):
    """

    :param system: Provides information about the current state of the Alexa service and the device interacting with your skill.
    :type system: (optional) ask_sdk_model.interfaces.system.system_state.SystemState
    :param audio_player: Provides the current state for the AudioPlayer interface.
    :type audio_player: (optional) ask_sdk_model.interfaces.audioplayer.audio_player_state.AudioPlayerState
    :param display: Provides the current state for the Display interface.
    :type display: (optional) ask_sdk_model.interfaces.display.display_state.DisplayState
    :param viewport: Provides the characteristics of a device&#39;s viewport.
    :type viewport: (optional) ask_sdk_model.interfaces.viewport.viewport_state.ViewportState

    """
    deserialized_types = {
        'system': 'ask_sdk_model.interfaces.system.system_state.SystemState',
        'audio_player': 'ask_sdk_model.interfaces.audioplayer.audio_player_state.AudioPlayerState',
        'display': 'ask_sdk_model.interfaces.display.display_state.DisplayState',
        'viewport': 'ask_sdk_model.interfaces.viewport.viewport_state.ViewportState'
    }

    attribute_map = {
        'system': 'System',
        'audio_player': 'AudioPlayer',
        'display': 'Display',
        'viewport': 'Viewport'
    }

    def __init__(self, system=None, audio_player=None, display=None, viewport=None):
        # type: (Optional[SystemState], Optional[AudioPlayerState], Optional[DisplayState], Optional[ViewportState]) -> None
        """

        :param system: Provides information about the current state of the Alexa service and the device interacting with your skill.
        :type system: (optional) ask_sdk_model.interfaces.system.system_state.SystemState
        :param audio_player: Provides the current state for the AudioPlayer interface.
        :type audio_player: (optional) ask_sdk_model.interfaces.audioplayer.audio_player_state.AudioPlayerState
        :param display: Provides the current state for the Display interface.
        :type display: (optional) ask_sdk_model.interfaces.display.display_state.DisplayState
        :param viewport: Provides the characteristics of a device&#39;s viewport.
        :type viewport: (optional) ask_sdk_model.interfaces.viewport.viewport_state.ViewportState
        """
        self.__discriminator_value = None

        self.system = system
        self.audio_player = audio_player
        self.display = display
        self.viewport = viewport

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
        if not isinstance(other, Context):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
