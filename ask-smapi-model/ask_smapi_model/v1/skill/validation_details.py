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
    from ask_smapi_model.v1.skill.instance import Instance as Skill_InstanceV1
    from ask_smapi_model.v1.skill.validation_failure_reason import ValidationFailureReason as Skill_ValidationFailureReasonV1
    from ask_smapi_model.v1.skill.image_attributes import ImageAttributes as Skill_ImageAttributesV1
    from ask_smapi_model.v1.skill.validation_endpoint import ValidationEndpoint as Skill_ValidationEndpointV1
    from ask_smapi_model.v1.skill.format import Format as Skill_FormatV1
    from ask_smapi_model.v1.skill.agreement_type import AgreementType as Skill_AgreementTypeV1
    from ask_smapi_model.v1.skill.validation_data_types import ValidationDataTypes as Skill_ValidationDataTypesV1
    from ask_smapi_model.v1.skill.validation_feature import ValidationFeature as Skill_ValidationFeatureV1


class ValidationDetails(object):
    """
    Standardized, machine readable structure that wraps all the information about a specific occurrence of an error of the type specified by the code.


    :param actual_image_attributes: Set of properties of the image provided by the customer.
    :type actual_image_attributes: (optional) ask_smapi_model.v1.skill.image_attributes.ImageAttributes
    :param actual_number_of_items: Number of items in an array provided by the customer.
    :type actual_number_of_items: (optional) int
    :param actual_string_length: Number of characters in a string provided by the customer.
    :type actual_string_length: (optional) int
    :param allowed_content_types: List of allowed content types for a resource.
    :type allowed_content_types: (optional) list[str]
    :param allowed_data_types: List of allowed data types for an instance.
    :type allowed_data_types: (optional) list[ask_smapi_model.v1.skill.validation_data_types.ValidationDataTypes]
    :param allowed_image_attributes: List of set of properties representing all possible allowed images.
    :type allowed_image_attributes: (optional) list[ask_smapi_model.v1.skill.image_attributes.ImageAttributes]
    :param conflicting_instance: Instance conflicting with another instance.
    :type conflicting_instance: (optional) ask_smapi_model.v1.skill.instance.Instance
    :param expected_format: Format in which instance value is expected in.
    :type expected_format: (optional) ask_smapi_model.v1.skill.format.Format
    :param expected_instance: Instance that is expected by a related instance.
    :type expected_instance: (optional) ask_smapi_model.v1.skill.instance.Instance
    :param expected_regex_pattern: Regular expression that a string instance is expected to match.
    :type expected_regex_pattern: (optional) str
    :param agreement_type: Type of the agreement that the customer must be compliant to.
    :type agreement_type: (optional) ask_smapi_model.v1.skill.agreement_type.AgreementType
    :param feature: Properties of a publicly known feature that has restricted access.
    :type feature: (optional) ask_smapi_model.v1.skill.validation_feature.ValidationFeature
    :param inconsistent_endpoint: Endpoint which has a different value for property named type when compared to original endpoint.
    :type inconsistent_endpoint: (optional) ask_smapi_model.v1.skill.validation_endpoint.ValidationEndpoint
    :param minimum_integer_value: Minimum allowed value of an integer instance.
    :type minimum_integer_value: (optional) int
    :param minimum_number_of_items: Minimum allowed number of items in an array.
    :type minimum_number_of_items: (optional) int
    :param minimum_string_length: Minimum allowed number of characters in a string.
    :type minimum_string_length: (optional) int
    :param maximum_integer_value: Maximum allowed value of an integer instance.
    :type maximum_integer_value: (optional) int
    :param maximum_number_of_items: Maximum allowed number of items in an array.
    :type maximum_number_of_items: (optional) int
    :param maximum_string_length: Maximum allowed number of characters in a string.
    :type maximum_string_length: (optional) int
    :param original_endpoint: An Endpoint instance
    :type original_endpoint: (optional) ask_smapi_model.v1.skill.validation_endpoint.ValidationEndpoint
    :param original_instance: An Instance
    :type original_instance: (optional) ask_smapi_model.v1.skill.instance.Instance
    :param reason: Represents what is wrong in the request.
    :type reason: (optional) ask_smapi_model.v1.skill.validation_failure_reason.ValidationFailureReason
    :param required_property: Property required but missing in the object.
    :type required_property: (optional) str
    :param unexpected_property: Property not expected but present in the object.
    :type unexpected_property: (optional) str

    """
    deserialized_types = {
        'actual_image_attributes': 'ask_smapi_model.v1.skill.image_attributes.ImageAttributes',
        'actual_number_of_items': 'int',
        'actual_string_length': 'int',
        'allowed_content_types': 'list[str]',
        'allowed_data_types': 'list[ask_smapi_model.v1.skill.validation_data_types.ValidationDataTypes]',
        'allowed_image_attributes': 'list[ask_smapi_model.v1.skill.image_attributes.ImageAttributes]',
        'conflicting_instance': 'ask_smapi_model.v1.skill.instance.Instance',
        'expected_format': 'ask_smapi_model.v1.skill.format.Format',
        'expected_instance': 'ask_smapi_model.v1.skill.instance.Instance',
        'expected_regex_pattern': 'str',
        'agreement_type': 'ask_smapi_model.v1.skill.agreement_type.AgreementType',
        'feature': 'ask_smapi_model.v1.skill.validation_feature.ValidationFeature',
        'inconsistent_endpoint': 'ask_smapi_model.v1.skill.validation_endpoint.ValidationEndpoint',
        'minimum_integer_value': 'int',
        'minimum_number_of_items': 'int',
        'minimum_string_length': 'int',
        'maximum_integer_value': 'int',
        'maximum_number_of_items': 'int',
        'maximum_string_length': 'int',
        'original_endpoint': 'ask_smapi_model.v1.skill.validation_endpoint.ValidationEndpoint',
        'original_instance': 'ask_smapi_model.v1.skill.instance.Instance',
        'reason': 'ask_smapi_model.v1.skill.validation_failure_reason.ValidationFailureReason',
        'required_property': 'str',
        'unexpected_property': 'str'
    }  # type: Dict

    attribute_map = {
        'actual_image_attributes': 'actualImageAttributes',
        'actual_number_of_items': 'actualNumberOfItems',
        'actual_string_length': 'actualStringLength',
        'allowed_content_types': 'allowedContentTypes',
        'allowed_data_types': 'allowedDataTypes',
        'allowed_image_attributes': 'allowedImageAttributes',
        'conflicting_instance': 'conflictingInstance',
        'expected_format': 'expectedFormat',
        'expected_instance': 'expectedInstance',
        'expected_regex_pattern': 'expectedRegexPattern',
        'agreement_type': 'agreementType',
        'feature': 'feature',
        'inconsistent_endpoint': 'inconsistentEndpoint',
        'minimum_integer_value': 'minimumIntegerValue',
        'minimum_number_of_items': 'minimumNumberOfItems',
        'minimum_string_length': 'minimumStringLength',
        'maximum_integer_value': 'maximumIntegerValue',
        'maximum_number_of_items': 'maximumNumberOfItems',
        'maximum_string_length': 'maximumStringLength',
        'original_endpoint': 'originalEndpoint',
        'original_instance': 'originalInstance',
        'reason': 'reason',
        'required_property': 'requiredProperty',
        'unexpected_property': 'unexpectedProperty'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, actual_image_attributes=None, actual_number_of_items=None, actual_string_length=None, allowed_content_types=None, allowed_data_types=None, allowed_image_attributes=None, conflicting_instance=None, expected_format=None, expected_instance=None, expected_regex_pattern=None, agreement_type=None, feature=None, inconsistent_endpoint=None, minimum_integer_value=None, minimum_number_of_items=None, minimum_string_length=None, maximum_integer_value=None, maximum_number_of_items=None, maximum_string_length=None, original_endpoint=None, original_instance=None, reason=None, required_property=None, unexpected_property=None):
        # type: (Optional[Skill_ImageAttributesV1], Optional[int], Optional[int], Optional[List[object]], Optional[List[Skill_ValidationDataTypesV1]], Optional[List[Skill_ImageAttributesV1]], Optional[Skill_InstanceV1], Optional[Skill_FormatV1], Optional[Skill_InstanceV1], Optional[str], Optional[Skill_AgreementTypeV1], Optional[Skill_ValidationFeatureV1], Optional[Skill_ValidationEndpointV1], Optional[int], Optional[int], Optional[int], Optional[int], Optional[int], Optional[int], Optional[Skill_ValidationEndpointV1], Optional[Skill_InstanceV1], Optional[Skill_ValidationFailureReasonV1], Optional[str], Optional[str]) -> None
        """Standardized, machine readable structure that wraps all the information about a specific occurrence of an error of the type specified by the code.

        :param actual_image_attributes: Set of properties of the image provided by the customer.
        :type actual_image_attributes: (optional) ask_smapi_model.v1.skill.image_attributes.ImageAttributes
        :param actual_number_of_items: Number of items in an array provided by the customer.
        :type actual_number_of_items: (optional) int
        :param actual_string_length: Number of characters in a string provided by the customer.
        :type actual_string_length: (optional) int
        :param allowed_content_types: List of allowed content types for a resource.
        :type allowed_content_types: (optional) list[str]
        :param allowed_data_types: List of allowed data types for an instance.
        :type allowed_data_types: (optional) list[ask_smapi_model.v1.skill.validation_data_types.ValidationDataTypes]
        :param allowed_image_attributes: List of set of properties representing all possible allowed images.
        :type allowed_image_attributes: (optional) list[ask_smapi_model.v1.skill.image_attributes.ImageAttributes]
        :param conflicting_instance: Instance conflicting with another instance.
        :type conflicting_instance: (optional) ask_smapi_model.v1.skill.instance.Instance
        :param expected_format: Format in which instance value is expected in.
        :type expected_format: (optional) ask_smapi_model.v1.skill.format.Format
        :param expected_instance: Instance that is expected by a related instance.
        :type expected_instance: (optional) ask_smapi_model.v1.skill.instance.Instance
        :param expected_regex_pattern: Regular expression that a string instance is expected to match.
        :type expected_regex_pattern: (optional) str
        :param agreement_type: Type of the agreement that the customer must be compliant to.
        :type agreement_type: (optional) ask_smapi_model.v1.skill.agreement_type.AgreementType
        :param feature: Properties of a publicly known feature that has restricted access.
        :type feature: (optional) ask_smapi_model.v1.skill.validation_feature.ValidationFeature
        :param inconsistent_endpoint: Endpoint which has a different value for property named type when compared to original endpoint.
        :type inconsistent_endpoint: (optional) ask_smapi_model.v1.skill.validation_endpoint.ValidationEndpoint
        :param minimum_integer_value: Minimum allowed value of an integer instance.
        :type minimum_integer_value: (optional) int
        :param minimum_number_of_items: Minimum allowed number of items in an array.
        :type minimum_number_of_items: (optional) int
        :param minimum_string_length: Minimum allowed number of characters in a string.
        :type minimum_string_length: (optional) int
        :param maximum_integer_value: Maximum allowed value of an integer instance.
        :type maximum_integer_value: (optional) int
        :param maximum_number_of_items: Maximum allowed number of items in an array.
        :type maximum_number_of_items: (optional) int
        :param maximum_string_length: Maximum allowed number of characters in a string.
        :type maximum_string_length: (optional) int
        :param original_endpoint: An Endpoint instance
        :type original_endpoint: (optional) ask_smapi_model.v1.skill.validation_endpoint.ValidationEndpoint
        :param original_instance: An Instance
        :type original_instance: (optional) ask_smapi_model.v1.skill.instance.Instance
        :param reason: Represents what is wrong in the request.
        :type reason: (optional) ask_smapi_model.v1.skill.validation_failure_reason.ValidationFailureReason
        :param required_property: Property required but missing in the object.
        :type required_property: (optional) str
        :param unexpected_property: Property not expected but present in the object.
        :type unexpected_property: (optional) str
        """
        self.__discriminator_value = None  # type: str

        self.actual_image_attributes = actual_image_attributes
        self.actual_number_of_items = actual_number_of_items
        self.actual_string_length = actual_string_length
        self.allowed_content_types = allowed_content_types
        self.allowed_data_types = allowed_data_types
        self.allowed_image_attributes = allowed_image_attributes
        self.conflicting_instance = conflicting_instance
        self.expected_format = expected_format
        self.expected_instance = expected_instance
        self.expected_regex_pattern = expected_regex_pattern
        self.agreement_type = agreement_type
        self.feature = feature
        self.inconsistent_endpoint = inconsistent_endpoint
        self.minimum_integer_value = minimum_integer_value
        self.minimum_number_of_items = minimum_number_of_items
        self.minimum_string_length = minimum_string_length
        self.maximum_integer_value = maximum_integer_value
        self.maximum_number_of_items = maximum_number_of_items
        self.maximum_string_length = maximum_string_length
        self.original_endpoint = original_endpoint
        self.original_instance = original_instance
        self.reason = reason
        self.required_property = required_property
        self.unexpected_property = unexpected_property

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
        if not isinstance(other, ValidationDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
