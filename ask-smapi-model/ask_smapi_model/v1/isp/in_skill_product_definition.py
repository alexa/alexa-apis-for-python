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
    from ask_smapi_model.v1.isp.purchasable_state import PurchasableState as Isp_PurchasableStateV1
    from ask_smapi_model.v1.isp.privacy_and_compliance import PrivacyAndCompliance as Isp_PrivacyAndComplianceV1
    from ask_smapi_model.v1.isp.subscription_information import SubscriptionInformation as Isp_SubscriptionInformationV1
    from ask_smapi_model.v1.isp.publishing_information import PublishingInformation as Isp_PublishingInformationV1
    from ask_smapi_model.v1.isp.product_type import ProductType as Isp_ProductTypeV1


class InSkillProductDefinition(object):
    """
    Defines the structure for an in-skill product.


    :param version: Version of in-skill product definition.
    :type version: (optional) str
    :param object_type: 
    :type object_type: (optional) ask_smapi_model.v1.isp.product_type.ProductType
    :param reference_name: Developer selected in-skill product name. This is for developer reference only, it can be used to filter query results to identify a matching in-skill product.
    :type reference_name: (optional) str
    :param purchasable_state: 
    :type purchasable_state: (optional) ask_smapi_model.v1.isp.purchasable_state.PurchasableState
    :param subscription_information: 
    :type subscription_information: (optional) ask_smapi_model.v1.isp.subscription_information.SubscriptionInformation
    :param publishing_information: 
    :type publishing_information: (optional) ask_smapi_model.v1.isp.publishing_information.PublishingInformation
    :param privacy_and_compliance: 
    :type privacy_and_compliance: (optional) ask_smapi_model.v1.isp.privacy_and_compliance.PrivacyAndCompliance
    :param testing_instructions: Special instructions provided by the developer to test the in-skill product.
    :type testing_instructions: (optional) str

    """
    deserialized_types = {
        'version': 'str',
        'object_type': 'ask_smapi_model.v1.isp.product_type.ProductType',
        'reference_name': 'str',
        'purchasable_state': 'ask_smapi_model.v1.isp.purchasable_state.PurchasableState',
        'subscription_information': 'ask_smapi_model.v1.isp.subscription_information.SubscriptionInformation',
        'publishing_information': 'ask_smapi_model.v1.isp.publishing_information.PublishingInformation',
        'privacy_and_compliance': 'ask_smapi_model.v1.isp.privacy_and_compliance.PrivacyAndCompliance',
        'testing_instructions': 'str'
    }  # type: Dict

    attribute_map = {
        'version': 'version',
        'object_type': 'type',
        'reference_name': 'referenceName',
        'purchasable_state': 'purchasableState',
        'subscription_information': 'subscriptionInformation',
        'publishing_information': 'publishingInformation',
        'privacy_and_compliance': 'privacyAndCompliance',
        'testing_instructions': 'testingInstructions'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, version=None, object_type=None, reference_name=None, purchasable_state=None, subscription_information=None, publishing_information=None, privacy_and_compliance=None, testing_instructions=None):
        # type: (Optional[str], Optional[Isp_ProductTypeV1], Optional[str], Optional[Isp_PurchasableStateV1], Optional[Isp_SubscriptionInformationV1], Optional[Isp_PublishingInformationV1], Optional[Isp_PrivacyAndComplianceV1], Optional[str]) -> None
        """Defines the structure for an in-skill product.

        :param version: Version of in-skill product definition.
        :type version: (optional) str
        :param object_type: 
        :type object_type: (optional) ask_smapi_model.v1.isp.product_type.ProductType
        :param reference_name: Developer selected in-skill product name. This is for developer reference only, it can be used to filter query results to identify a matching in-skill product.
        :type reference_name: (optional) str
        :param purchasable_state: 
        :type purchasable_state: (optional) ask_smapi_model.v1.isp.purchasable_state.PurchasableState
        :param subscription_information: 
        :type subscription_information: (optional) ask_smapi_model.v1.isp.subscription_information.SubscriptionInformation
        :param publishing_information: 
        :type publishing_information: (optional) ask_smapi_model.v1.isp.publishing_information.PublishingInformation
        :param privacy_and_compliance: 
        :type privacy_and_compliance: (optional) ask_smapi_model.v1.isp.privacy_and_compliance.PrivacyAndCompliance
        :param testing_instructions: Special instructions provided by the developer to test the in-skill product.
        :type testing_instructions: (optional) str
        """
        self.__discriminator_value = None  # type: str

        self.version = version
        self.object_type = object_type
        self.reference_name = reference_name
        self.purchasable_state = purchasable_state
        self.subscription_information = subscription_information
        self.publishing_information = publishing_information
        self.privacy_and_compliance = privacy_and_compliance
        self.testing_instructions = testing_instructions

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
        if not isinstance(other, InSkillProductDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
