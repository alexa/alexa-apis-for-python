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
    from ask_smapi_model.v1.skill.manifest.viewport_mode import ViewportMode as Manifest_ViewportModeV1
    from ask_smapi_model.v1.skill.manifest.viewport_shape import ViewportShape as Manifest_ViewportShapeV1


class ViewportSpecification(object):
    """
    Defines a viewport specification.


    :param mode: 
    :type mode: (optional) ask_smapi_model.v1.skill.manifest.viewport_mode.ViewportMode
    :param shape: 
    :type shape: (optional) ask_smapi_model.v1.skill.manifest.viewport_shape.ViewportShape
    :param min_width: Defines the minimum width of viewport that comply with this specification.
    :type min_width: (optional) int
    :param max_width: Defines the maximum width of viewport that comply with this specification.
    :type max_width: (optional) int
    :param min_height: Defines the minimum height of viewport that comply with this specification.
    :type min_height: (optional) int
    :param max_height: Defines the maximum height of viewport that comply with this specification.
    :type max_height: (optional) int

    """
    deserialized_types = {
        'mode': 'ask_smapi_model.v1.skill.manifest.viewport_mode.ViewportMode',
        'shape': 'ask_smapi_model.v1.skill.manifest.viewport_shape.ViewportShape',
        'min_width': 'int',
        'max_width': 'int',
        'min_height': 'int',
        'max_height': 'int'
    }  # type: Dict

    attribute_map = {
        'mode': 'mode',
        'shape': 'shape',
        'min_width': 'minWidth',
        'max_width': 'maxWidth',
        'min_height': 'minHeight',
        'max_height': 'maxHeight'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, mode=None, shape=None, min_width=None, max_width=None, min_height=None, max_height=None):
        # type: (Optional[Manifest_ViewportModeV1], Optional[Manifest_ViewportShapeV1], Optional[int], Optional[int], Optional[int], Optional[int]) -> None
        """Defines a viewport specification.

        :param mode: 
        :type mode: (optional) ask_smapi_model.v1.skill.manifest.viewport_mode.ViewportMode
        :param shape: 
        :type shape: (optional) ask_smapi_model.v1.skill.manifest.viewport_shape.ViewportShape
        :param min_width: Defines the minimum width of viewport that comply with this specification.
        :type min_width: (optional) int
        :param max_width: Defines the maximum width of viewport that comply with this specification.
        :type max_width: (optional) int
        :param min_height: Defines the minimum height of viewport that comply with this specification.
        :type min_height: (optional) int
        :param max_height: Defines the maximum height of viewport that comply with this specification.
        :type max_height: (optional) int
        """
        self.__discriminator_value = None  # type: str

        self.mode = mode
        self.shape = shape
        self.min_width = min_width
        self.max_width = max_width
        self.min_height = min_height
        self.max_height = max_height

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
        if not isinstance(other, ViewportSpecification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
