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
    from typing import Dict, List, Optional, Union
    from datetime import datetime


class ResolutionsPerAuthorityStatusCode(Enum):
    """
    A code indicating the results of attempting to resolve the user utterance against the defined slot types. This can be one of the following: ER_SUCCESS_MATCH: The spoken value matched a value or synonym explicitly defined in your custom slot type. ER_SUCCESS_NO_MATCH: The spoken value did not match any values or synonyms explicitly defined in your custom slot type. ER_ERROR_TIMEOUT: An error occurred due to a timeout. ER_ERROR_EXCEPTION: An error occurred due to an exception during processing. 



    Allowed enum values: [ER_SUCCESS_MATCH, ER_SUCCESS_NO_MATCH, ER_ERROR_TIMEOUT, ER_ERROR_EXCEPTION]
    """
    ER_SUCCESS_MATCH = "ER_SUCCESS_MATCH"
    ER_SUCCESS_NO_MATCH = "ER_SUCCESS_NO_MATCH"
    ER_ERROR_TIMEOUT = "ER_ERROR_TIMEOUT"
    ER_ERROR_EXCEPTION = "ER_ERROR_EXCEPTION"

    def to_dict(self):
        # type: () -> Dict[str, object]
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
        # type: (object) -> bool
        """Returns true if both objects are equal"""
        if not isinstance(other, ResolutionsPerAuthorityStatusCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
