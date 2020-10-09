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
    from ask_smapi_model.v1.isp.summary_price_listing import SummaryPriceListing as Isp_SummaryPriceListingV1


class SummaryMarketplacePricing(object):
    """
    Localized in-skill product pricing information.


    :param release_date: Date when in-skill product is available to customers for both purchase and use. Prior to this date the in-skill product will appear unavailable to customers and will not be purchasable.
    :type release_date: (optional) datetime
    :param default_price_listing: 
    :type default_price_listing: (optional) ask_smapi_model.v1.isp.summary_price_listing.SummaryPriceListing

    """
    deserialized_types = {
        'release_date': 'datetime',
        'default_price_listing': 'ask_smapi_model.v1.isp.summary_price_listing.SummaryPriceListing'
    }  # type: Dict

    attribute_map = {
        'release_date': 'releaseDate',
        'default_price_listing': 'defaultPriceListing'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, release_date=None, default_price_listing=None):
        # type: (Optional[datetime], Optional[Isp_SummaryPriceListingV1]) -> None
        """Localized in-skill product pricing information.

        :param release_date: Date when in-skill product is available to customers for both purchase and use. Prior to this date the in-skill product will appear unavailable to customers and will not be purchasable.
        :type release_date: (optional) datetime
        :param default_price_listing: 
        :type default_price_listing: (optional) ask_smapi_model.v1.isp.summary_price_listing.SummaryPriceListing
        """
        self.__discriminator_value = None  # type: str

        self.release_date = release_date
        self.default_price_listing = default_price_listing

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
        if not isinstance(other, SummaryMarketplacePricing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
