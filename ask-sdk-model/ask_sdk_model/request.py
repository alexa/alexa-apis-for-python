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


class Request(object):
    """
    A request object that provides the details of the user’s request. The request body contains the parameters necessary for the service to perform its logic and generate a response.


    :param object_type: Describes the type of the request.
    :type object_type: (optional) str
    :param request_id: Represents the unique identifier for the specific request.
    :type request_id: (optional) str
    :param timestamp: Provides the date and time when Alexa sent the request as an ISO 8601 formatted string. Used to verify the request when hosting your skill as a web service.
    :type timestamp: (optional) datetime

    .. note::

        This is an abstract class. Use the following mapping, to figure out
        the model class to be instantiated, that sets ``type`` variable.

        | AudioPlayer.PlaybackFinished: :py:class:`ask_sdk_model.interfaces.audioplayer.playback_finished_request.PlaybackFinishedRequest`,
        |
        | AlexaSkillEvent.SkillEnabled: :py:class:`ask_sdk_model.events.skillevents.skill_enabled_request.SkillEnabledRequest`,
        |
        | AlexaHouseholdListEvent.ListUpdated: :py:class:`ask_sdk_model.services.list_management.list_updated_event_request.ListUpdatedEventRequest`,
        |
        | AlexaSkillEvent.SkillDisabled: :py:class:`ask_sdk_model.events.skillevents.skill_disabled_request.SkillDisabledRequest`,
        |
        | Display.ElementSelected: :py:class:`ask_sdk_model.interfaces.display.element_selected_request.ElementSelectedRequest`,
        |
        | AlexaSkillEvent.SkillPermissionChanged: :py:class:`ask_sdk_model.events.skillevents.permission_changed_request.PermissionChangedRequest`,
        |
        | AlexaHouseholdListEvent.ItemsCreated: :py:class:`ask_sdk_model.services.list_management.list_items_created_event_request.ListItemsCreatedEventRequest`,
        |
        | SessionEndedRequest: :py:class:`ask_sdk_model.session_ended_request.SessionEndedRequest`,
        |
        | IntentRequest: :py:class:`ask_sdk_model.intent_request.IntentRequest`,
        |
        | AudioPlayer.PlaybackFailed: :py:class:`ask_sdk_model.interfaces.audioplayer.playback_failed_request.PlaybackFailedRequest`,
        |
        | LaunchRequest: :py:class:`ask_sdk_model.launch_request.LaunchRequest`,
        |
        | AudioPlayer.PlaybackStopped: :py:class:`ask_sdk_model.interfaces.audioplayer.playback_stopped_request.PlaybackStoppedRequest`,
        |
        | PlaybackController.PreviousCommandIssued: :py:class:`ask_sdk_model.interfaces.playbackcontroller.previous_command_issued_request.PreviousCommandIssuedRequest`,
        |
        | AlexaHouseholdListEvent.ItemsUpdated: :py:class:`ask_sdk_model.services.list_management.list_items_updated_event_request.ListItemsUpdatedEventRequest`,
        |
        | AlexaSkillEvent.SkillAccountLinked: :py:class:`ask_sdk_model.events.skillevents.account_linked_request.AccountLinkedRequest`,
        |
        | AlexaHouseholdListEvent.ListCreated: :py:class:`ask_sdk_model.services.list_management.list_created_event_request.ListCreatedEventRequest`,
        |
        | AudioPlayer.PlaybackStarted: :py:class:`ask_sdk_model.interfaces.audioplayer.playback_started_request.PlaybackStartedRequest`,
        |
        | AudioPlayer.PlaybackNearlyFinished: :py:class:`ask_sdk_model.interfaces.audioplayer.playback_nearly_finished_request.PlaybackNearlyFinishedRequest`,
        |
        | AlexaHouseholdListEvent.ItemsDeleted: :py:class:`ask_sdk_model.services.list_management.list_items_deleted_event_request.ListItemsDeletedEventRequest`,
        |
        | Connections.Response: :py:class:`ask_sdk_model.interfaces.connections.connections_response.ConnectionsResponse`,
        |
        | Messaging.MessageReceived: :py:class:`ask_sdk_model.interfaces.messaging.message_received_request.MessageReceivedRequest`,
        |
        | Connections.Request: :py:class:`ask_sdk_model.interfaces.connections.connections_request.ConnectionsRequest`,
        |
        | System.ExceptionEncountered: :py:class:`ask_sdk_model.interfaces.system.exception_encountered_request.ExceptionEncounteredRequest`,
        |
        | AlexaSkillEvent.SkillPermissionAccepted: :py:class:`ask_sdk_model.events.skillevents.permission_accepted_request.PermissionAcceptedRequest`,
        |
        | AlexaHouseholdListEvent.ListDeleted: :py:class:`ask_sdk_model.services.list_management.list_deleted_event_request.ListDeletedEventRequest`,
        |
        | GameEngine.InputHandlerEvent: :py:class:`ask_sdk_model.interfaces.game_engine.input_handler_event_request.InputHandlerEventRequest`,
        |
        | PlaybackController.NextCommandIssued: :py:class:`ask_sdk_model.interfaces.playbackcontroller.next_command_issued_request.NextCommandIssuedRequest`,
        |
        | PlaybackController.PauseCommandIssued: :py:class:`ask_sdk_model.interfaces.playbackcontroller.pause_command_issued_request.PauseCommandIssuedRequest`,
        |
        | PlaybackController.PlayCommandIssued: :py:class:`ask_sdk_model.interfaces.playbackcontroller.play_command_issued_request.PlayCommandIssuedRequest`

    """
    deserialized_types = {
        'object_type': 'str',
        'request_id': 'str',
        'timestamp': 'datetime'
    }

    attribute_map = {
        'object_type': 'type',
        'request_id': 'requestId',
        'timestamp': 'timestamp'
    }

    discriminator_value_class_map = {
        'AudioPlayer.PlaybackFinished': 'ask_sdk_model.interfaces.audioplayer.playback_finished_request.PlaybackFinishedRequest',
        'AlexaSkillEvent.SkillEnabled': 'ask_sdk_model.events.skillevents.skill_enabled_request.SkillEnabledRequest',
        'AlexaHouseholdListEvent.ListUpdated': 'ask_sdk_model.services.list_management.list_updated_event_request.ListUpdatedEventRequest',
        'AlexaSkillEvent.SkillDisabled': 'ask_sdk_model.events.skillevents.skill_disabled_request.SkillDisabledRequest',
        'Display.ElementSelected': 'ask_sdk_model.interfaces.display.element_selected_request.ElementSelectedRequest',
        'AlexaSkillEvent.SkillPermissionChanged': 'ask_sdk_model.events.skillevents.permission_changed_request.PermissionChangedRequest',
        'AlexaHouseholdListEvent.ItemsCreated': 'ask_sdk_model.services.list_management.list_items_created_event_request.ListItemsCreatedEventRequest',
        'SessionEndedRequest': 'ask_sdk_model.session_ended_request.SessionEndedRequest',
        'IntentRequest': 'ask_sdk_model.intent_request.IntentRequest',
        'AudioPlayer.PlaybackFailed': 'ask_sdk_model.interfaces.audioplayer.playback_failed_request.PlaybackFailedRequest',
        'LaunchRequest': 'ask_sdk_model.launch_request.LaunchRequest',
        'AudioPlayer.PlaybackStopped': 'ask_sdk_model.interfaces.audioplayer.playback_stopped_request.PlaybackStoppedRequest',
        'PlaybackController.PreviousCommandIssued': 'ask_sdk_model.interfaces.playbackcontroller.previous_command_issued_request.PreviousCommandIssuedRequest',
        'AlexaHouseholdListEvent.ItemsUpdated': 'ask_sdk_model.services.list_management.list_items_updated_event_request.ListItemsUpdatedEventRequest',
        'AlexaSkillEvent.SkillAccountLinked': 'ask_sdk_model.events.skillevents.account_linked_request.AccountLinkedRequest',
        'AlexaHouseholdListEvent.ListCreated': 'ask_sdk_model.services.list_management.list_created_event_request.ListCreatedEventRequest',
        'AudioPlayer.PlaybackStarted': 'ask_sdk_model.interfaces.audioplayer.playback_started_request.PlaybackStartedRequest',
        'AudioPlayer.PlaybackNearlyFinished': 'ask_sdk_model.interfaces.audioplayer.playback_nearly_finished_request.PlaybackNearlyFinishedRequest',
        'AlexaHouseholdListEvent.ItemsDeleted': 'ask_sdk_model.services.list_management.list_items_deleted_event_request.ListItemsDeletedEventRequest',
        'Connections.Response': 'ask_sdk_model.interfaces.connections.connections_response.ConnectionsResponse',
        'Messaging.MessageReceived': 'ask_sdk_model.interfaces.messaging.message_received_request.MessageReceivedRequest',
        'Connections.Request': 'ask_sdk_model.interfaces.connections.connections_request.ConnectionsRequest',
        'System.ExceptionEncountered': 'ask_sdk_model.interfaces.system.exception_encountered_request.ExceptionEncounteredRequest',
        'AlexaSkillEvent.SkillPermissionAccepted': 'ask_sdk_model.events.skillevents.permission_accepted_request.PermissionAcceptedRequest',
        'AlexaHouseholdListEvent.ListDeleted': 'ask_sdk_model.services.list_management.list_deleted_event_request.ListDeletedEventRequest',
        'GameEngine.InputHandlerEvent': 'ask_sdk_model.interfaces.game_engine.input_handler_event_request.InputHandlerEventRequest',
        'PlaybackController.NextCommandIssued': 'ask_sdk_model.interfaces.playbackcontroller.next_command_issued_request.NextCommandIssuedRequest',
        'PlaybackController.PauseCommandIssued': 'ask_sdk_model.interfaces.playbackcontroller.pause_command_issued_request.PauseCommandIssuedRequest',
        'PlaybackController.PlayCommandIssued': 'ask_sdk_model.interfaces.playbackcontroller.play_command_issued_request.PlayCommandIssuedRequest'
    }

    json_discriminator_key = "type"

    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, object_type=None, request_id=None, timestamp=None):
        # type: (Optional[str], Optional[str], Optional[datetime]) -> None
        """A request object that provides the details of the user’s request. The request body contains the parameters necessary for the service to perform its logic and generate a response.

        :param object_type: Describes the type of the request.
        :type object_type: (optional) str
        :param request_id: Represents the unique identifier for the specific request.
        :type request_id: (optional) str
        :param timestamp: Provides the date and time when Alexa sent the request as an ISO 8601 formatted string. Used to verify the request when hosting your skill as a web service.
        :type timestamp: (optional) datetime
        """
        self.__discriminator_value = None

        self.object_type = object_type
        self.request_id = request_id
        self.timestamp = timestamp

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
        if not isinstance(other, Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
