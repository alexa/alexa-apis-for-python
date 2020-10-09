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
    from ask_smapi_model.v1.isp.localized_publishing_information import LocalizedPublishingInformation as Isp_LocalizedPublishingInformationV1
    from ask_smapi_model.v1.isp.distribution_countries import DistributionCountries as Isp_DistributionCountriesV1
    from ask_smapi_model.v1.isp.marketplace_pricing import MarketplacePricing as Isp_MarketplacePricingV1
    from ask_smapi_model.v1.isp.tax_information import TaxInformation as Isp_TaxInformationV1


class PublishingInformation(object):
    """
    Defines the structure for in-skill product publishing information.


    :param locales: Defines the structure for locale specific publishing information for an in-skill product.
    :type locales: (optional) dict(str, ask_smapi_model.v1.isp.localized_publishing_information.LocalizedPublishingInformation)
    :param distribution_countries: List of countries where the in-skill product is available.
    :type distribution_countries: (optional) list[ask_smapi_model.v1.isp.distribution_countries.DistributionCountries]
    :param pricing: Defines the structure for in-skill product pricing.
    :type pricing: (optional) dict(str, ask_smapi_model.v1.isp.marketplace_pricing.MarketplacePricing)
    :param tax_information: 
    :type tax_information: (optional) ask_smapi_model.v1.isp.tax_information.TaxInformation

    """
    deserialized_types = {
        'locales': 'dict(str, ask_smapi_model.v1.isp.localized_publishing_information.LocalizedPublishingInformation)',
        'distribution_countries': 'list[ask_smapi_model.v1.isp.distribution_countries.DistributionCountries]',
        'pricing': 'dict(str, ask_smapi_model.v1.isp.marketplace_pricing.MarketplacePricing)',
        'tax_information': 'ask_smapi_model.v1.isp.tax_information.TaxInformation'
    }  # type: Dict

    attribute_map = {
        'locales': 'locales',
        'distribution_countries': 'distributionCountries',
        'pricing': 'pricing',
        'tax_information': 'taxInformation'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, locales=None, distribution_countries=None, pricing=None, tax_information=None):
        # type: (Optional[Dict[str, Isp_LocalizedPublishingInformationV1]], Optional[List[Isp_DistributionCountriesV1]], Optional[Dict[str, Isp_MarketplacePricingV1]], Optional[Isp_TaxInformationV1]) -> None
        """Defines the structure for in-skill product publishing information.

        :param locales: Defines the structure for locale specific publishing information for an in-skill product.
        :type locales: (optional) dict(str, ask_smapi_model.v1.isp.localized_publishing_information.LocalizedPublishingInformation)
        :param distribution_countries: List of countries where the in-skill product is available.
        :type distribution_countries: (optional) list[ask_smapi_model.v1.isp.distribution_countries.DistributionCountries]
        :param pricing: Defines the structure for in-skill product pricing.
        :type pricing: (optional) dict(str, ask_smapi_model.v1.isp.marketplace_pricing.MarketplacePricing)
        :param tax_information: 
        :type tax_information: (optional) ask_smapi_model.v1.isp.tax_information.TaxInformation
        """
        self.__discriminator_value = None  # type: str

        self.locales = locales
        self.distribution_countries = distribution_countries
        self.pricing = pricing
        self.tax_information = tax_information

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
        if not isinstance(other, PublishingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
