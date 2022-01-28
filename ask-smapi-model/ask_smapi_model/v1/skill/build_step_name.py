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


class BuildStepName(Enum):
    """
    Name of the build step. Possible values - * &#x60;DIALOG_MODEL_BUILD&#x60; - Build status for dialog model. * &#x60;LANGUAGE_MODEL_QUICK_BUILD&#x60; - Build status for FST model. * &#x60;LANGUAGE_MODEL_FULL_BUILD&#x60; - Build status for statistical model. * &#x60;ALEXA_CONVERSATIONS_QUICK_BUILD&#x60; - AlexaConversations LowFidelity model build status. * &#x60;ALEXA_CONVERSATIONS_FULL_BUILD&#x60; - AlexaConversations HighFidelity model build status. 



    Allowed enum values: [DIALOG_MODEL_BUILD, LANGUAGE_MODEL_QUICK_BUILD, LANGUAGE_MODEL_FULL_BUILD, ALEXA_CONVERSATIONS_QUICK_BUILD, ALEXA_CONVERSATIONS_FULL_BUILD]
    """
    DIALOG_MODEL_BUILD = "DIALOG_MODEL_BUILD"
    LANGUAGE_MODEL_QUICK_BUILD = "LANGUAGE_MODEL_QUICK_BUILD"
    LANGUAGE_MODEL_FULL_BUILD = "LANGUAGE_MODEL_FULL_BUILD"
    ALEXA_CONVERSATIONS_QUICK_BUILD = "ALEXA_CONVERSATIONS_QUICK_BUILD"
    ALEXA_CONVERSATIONS_FULL_BUILD = "ALEXA_CONVERSATIONS_FULL_BUILD"

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
        if not isinstance(other, BuildStepName):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (Any) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
