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
    from ask_sdk_model.interfaces.amazonpay.model.v1.seller_billing_agreement_attributes import SellerBillingAgreementAttributes


class BillingAgreementAttributes(object):
    """
    The merchant can choose to set the attributes specified in the BillingAgreementAttributes.


    :param platform_id: Represents the SellerId of the Solution Provider that developed the eCommerce platform. This value is only used by Solution Providers, for whom it is required. It should not be provided by merchants creating their own custom integration. Do not specify the SellerId of the merchant for this request parameter. If you are a merchant, do not enter a PlatformId.
    :type platform_id: (optional) str
    :param seller_note: Represents a description of the billing agreement that is displayed in emails to the buyer.
    :type seller_note: (optional) str
    :param seller_billing_agreement_attributes: 
    :type seller_billing_agreement_attributes: (optional) ask_sdk_model.interfaces.amazonpay.model.v1.seller_billing_agreement_attributes.SellerBillingAgreementAttributes

    """
    deserialized_types = {
        'platform_id': 'str',
        'seller_note': 'str',
        'seller_billing_agreement_attributes': 'ask_sdk_model.interfaces.amazonpay.model.v1.seller_billing_agreement_attributes.SellerBillingAgreementAttributes'
    }

    attribute_map = {
        'platform_id': 'platformId',
        'seller_note': 'sellerNote',
        'seller_billing_agreement_attributes': 'sellerBillingAgreementAttributes'
    }

    def __init__(self, platform_id=None, seller_note=None, seller_billing_agreement_attributes=None):
        # type: (Optional[str], Optional[str], Optional[SellerBillingAgreementAttributes]) -> None
        """The merchant can choose to set the attributes specified in the BillingAgreementAttributes.

        :param platform_id: Represents the SellerId of the Solution Provider that developed the eCommerce platform. This value is only used by Solution Providers, for whom it is required. It should not be provided by merchants creating their own custom integration. Do not specify the SellerId of the merchant for this request parameter. If you are a merchant, do not enter a PlatformId.
        :type platform_id: (optional) str
        :param seller_note: Represents a description of the billing agreement that is displayed in emails to the buyer.
        :type seller_note: (optional) str
        :param seller_billing_agreement_attributes: 
        :type seller_billing_agreement_attributes: (optional) ask_sdk_model.interfaces.amazonpay.model.v1.seller_billing_agreement_attributes.SellerBillingAgreementAttributes
        """
        self.__discriminator_value = None

        self.platform_id = platform_id
        self.seller_note = seller_note
        self.seller_billing_agreement_attributes = seller_billing_agreement_attributes

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
        if not isinstance(other, BillingAgreementAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
