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


class InterfaceType(Enum):
    """
    Name of the interface.



    Allowed enum values: [AUDIO_PLAYER, VIDEO_APP, RENDER_TEMPLATE, GAME_ENGINE, GADGET_CONTROLLER, CAN_FULFILL_INTENT_REQUEST, ALEXA_PRESENTATION_APL, ALEXA_CAMERA_PHOTO_CAPTURE_CONTROLLER, ALEXA_CAMERA_VIDEO_CAPTURE_CONTROLLER, ALEXA_FILE_MANAGER_UPLOAD_CONTROLLER, CUSTOM_INTERFACE, ALEXA_AUGMENTATION_EFFECTS_CONTROLLER, APP_LINKS, ALEXA_EXTENSION, APP_LINKS_V2]
    """
    AUDIO_PLAYER = "AUDIO_PLAYER"
    VIDEO_APP = "VIDEO_APP"
    RENDER_TEMPLATE = "RENDER_TEMPLATE"
    GAME_ENGINE = "GAME_ENGINE"
    GADGET_CONTROLLER = "GADGET_CONTROLLER"
    CAN_FULFILL_INTENT_REQUEST = "CAN_FULFILL_INTENT_REQUEST"
    ALEXA_PRESENTATION_APL = "ALEXA_PRESENTATION_APL"
    ALEXA_CAMERA_PHOTO_CAPTURE_CONTROLLER = "ALEXA_CAMERA_PHOTO_CAPTURE_CONTROLLER"
    ALEXA_CAMERA_VIDEO_CAPTURE_CONTROLLER = "ALEXA_CAMERA_VIDEO_CAPTURE_CONTROLLER"
    ALEXA_FILE_MANAGER_UPLOAD_CONTROLLER = "ALEXA_FILE_MANAGER_UPLOAD_CONTROLLER"
    CUSTOM_INTERFACE = "CUSTOM_INTERFACE"
    ALEXA_AUGMENTATION_EFFECTS_CONTROLLER = "ALEXA_AUGMENTATION_EFFECTS_CONTROLLER"
    APP_LINKS = "APP_LINKS"
    ALEXA_EXTENSION = "ALEXA_EXTENSION"
    APP_LINKS_V2 = "APP_LINKS_V2"

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
        if not isinstance(other, InterfaceType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (Any) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
