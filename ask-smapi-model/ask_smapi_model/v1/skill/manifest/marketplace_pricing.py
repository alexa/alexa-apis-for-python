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
    from ask_smapi_model.v1.skill.manifest.free_trial_information import FreeTrialInformation as FreeTrialInformation_dd82f7a7
    from ask_smapi_model.v1.skill.manifest.currency import Currency as Currency_9d815c35
    from ask_smapi_model.v1.skill.manifest.subscription_information import SubscriptionInformation as SubscriptionInformation_8aecb324
    from ask_smapi_model.v1.skill.manifest.offer_type import OfferType as OfferType_c467d5fe


class MarketplacePricing(object):
    """
    Paid skill product pricing information.


    :param offer_type: 
    :type offer_type: (optional) ask_smapi_model.v1.skill.manifest.offer_type.OfferType
    :param price: Defines the price of a paid skill product. The price should be your suggested price, not including any VAT or similar taxes. Taxes are included in the final price to end users.
    :type price: (optional) float
    :param currency: 
    :type currency: (optional) ask_smapi_model.v1.skill.manifest.currency.Currency
    :param free_trial_information: 
    :type free_trial_information: (optional) ask_smapi_model.v1.skill.manifest.free_trial_information.FreeTrialInformation
    :param subscription_information: 
    :type subscription_information: (optional) ask_smapi_model.v1.skill.manifest.subscription_information.SubscriptionInformation

    """
    deserialized_types = {
        'offer_type': 'ask_smapi_model.v1.skill.manifest.offer_type.OfferType',
        'price': 'float',
        'currency': 'ask_smapi_model.v1.skill.manifest.currency.Currency',
        'free_trial_information': 'ask_smapi_model.v1.skill.manifest.free_trial_information.FreeTrialInformation',
        'subscription_information': 'ask_smapi_model.v1.skill.manifest.subscription_information.SubscriptionInformation'
    }  # type: Dict

    attribute_map = {
        'offer_type': 'offerType',
        'price': 'price',
        'currency': 'currency',
        'free_trial_information': 'freeTrialInformation',
        'subscription_information': 'subscriptionInformation'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, offer_type=None, price=None, currency=None, free_trial_information=None, subscription_information=None):
        # type: (Optional[OfferType_c467d5fe], Optional[float], Optional[Currency_9d815c35], Optional[FreeTrialInformation_dd82f7a7], Optional[SubscriptionInformation_8aecb324]) -> None
        """Paid skill product pricing information.

        :param offer_type: 
        :type offer_type: (optional) ask_smapi_model.v1.skill.manifest.offer_type.OfferType
        :param price: Defines the price of a paid skill product. The price should be your suggested price, not including any VAT or similar taxes. Taxes are included in the final price to end users.
        :type price: (optional) float
        :param currency: 
        :type currency: (optional) ask_smapi_model.v1.skill.manifest.currency.Currency
        :param free_trial_information: 
        :type free_trial_information: (optional) ask_smapi_model.v1.skill.manifest.free_trial_information.FreeTrialInformation
        :param subscription_information: 
        :type subscription_information: (optional) ask_smapi_model.v1.skill.manifest.subscription_information.SubscriptionInformation
        """
        self.__discriminator_value = None  # type: str

        self.offer_type = offer_type
        self.price = price
        self.currency = currency
        self.free_trial_information = free_trial_information
        self.subscription_information = subscription_information

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
        if not isinstance(other, MarketplacePricing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
