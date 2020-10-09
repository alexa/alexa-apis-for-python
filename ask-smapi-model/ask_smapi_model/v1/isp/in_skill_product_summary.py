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
    from ask_smapi_model.v1.isp.stage import Stage as Isp_StageV1
    from ask_smapi_model.v1.isp.purchasable_state import PurchasableState as Isp_PurchasableStateV1
    from ask_smapi_model.v1.isp.editable_state import EditableState as Isp_EditableStateV1
    from ask_smapi_model.v1.isp.status import Status as Isp_StatusV1
    from ask_smapi_model.v1.isp.summary_marketplace_pricing import SummaryMarketplacePricing as Isp_SummaryMarketplacePricingV1
    from ask_smapi_model.v1.isp.isp_summary_links import IspSummaryLinks as Isp_IspSummaryLinksV1
    from ask_smapi_model.v1.isp.product_type import ProductType as Isp_ProductTypeV1


class InSkillProductSummary(object):
    """
    Information about the in-skill product that is not editable.


    :param object_type: 
    :type object_type: (optional) ask_smapi_model.v1.isp.product_type.ProductType
    :param product_id: primary identifier of in-skill product.
    :type product_id: (optional) str
    :param reference_name: Developer selected in-skill product name. This is for developer reference only, it can be used to filter query results to identify a matching in-skill product.
    :type reference_name: (optional) str
    :param last_updated: Date of last update.
    :type last_updated: (optional) datetime
    :param name_by_locale: 
    :type name_by_locale: (optional) dict(str, str)
    :param status: 
    :type status: (optional) ask_smapi_model.v1.isp.status.Status
    :param stage: 
    :type stage: (optional) ask_smapi_model.v1.isp.stage.Stage
    :param editable_state: 
    :type editable_state: (optional) ask_smapi_model.v1.isp.editable_state.EditableState
    :param purchasable_state: 
    :type purchasable_state: (optional) ask_smapi_model.v1.isp.purchasable_state.PurchasableState
    :param links: 
    :type links: (optional) ask_smapi_model.v1.isp.isp_summary_links.IspSummaryLinks
    :param pricing: In-skill product pricing information.
    :type pricing: (optional) dict(str, ask_smapi_model.v1.isp.summary_marketplace_pricing.SummaryMarketplacePricing)

    """
    deserialized_types = {
        'object_type': 'ask_smapi_model.v1.isp.product_type.ProductType',
        'product_id': 'str',
        'reference_name': 'str',
        'last_updated': 'datetime',
        'name_by_locale': 'dict(str, str)',
        'status': 'ask_smapi_model.v1.isp.status.Status',
        'stage': 'ask_smapi_model.v1.isp.stage.Stage',
        'editable_state': 'ask_smapi_model.v1.isp.editable_state.EditableState',
        'purchasable_state': 'ask_smapi_model.v1.isp.purchasable_state.PurchasableState',
        'links': 'ask_smapi_model.v1.isp.isp_summary_links.IspSummaryLinks',
        'pricing': 'dict(str, ask_smapi_model.v1.isp.summary_marketplace_pricing.SummaryMarketplacePricing)'
    }  # type: Dict

    attribute_map = {
        'object_type': 'type',
        'product_id': 'productId',
        'reference_name': 'referenceName',
        'last_updated': 'lastUpdated',
        'name_by_locale': 'nameByLocale',
        'status': 'status',
        'stage': 'stage',
        'editable_state': 'editableState',
        'purchasable_state': 'purchasableState',
        'links': '_links',
        'pricing': 'pricing'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, object_type=None, product_id=None, reference_name=None, last_updated=None, name_by_locale=None, status=None, stage=None, editable_state=None, purchasable_state=None, links=None, pricing=None):
        # type: (Optional[Isp_ProductTypeV1], Optional[str], Optional[str], Optional[datetime], Optional[Dict[str, object]], Optional[Isp_StatusV1], Optional[Isp_StageV1], Optional[Isp_EditableStateV1], Optional[Isp_PurchasableStateV1], Optional[Isp_IspSummaryLinksV1], Optional[Dict[str, Isp_SummaryMarketplacePricingV1]]) -> None
        """Information about the in-skill product that is not editable.

        :param object_type: 
        :type object_type: (optional) ask_smapi_model.v1.isp.product_type.ProductType
        :param product_id: primary identifier of in-skill product.
        :type product_id: (optional) str
        :param reference_name: Developer selected in-skill product name. This is for developer reference only, it can be used to filter query results to identify a matching in-skill product.
        :type reference_name: (optional) str
        :param last_updated: Date of last update.
        :type last_updated: (optional) datetime
        :param name_by_locale: 
        :type name_by_locale: (optional) dict(str, str)
        :param status: 
        :type status: (optional) ask_smapi_model.v1.isp.status.Status
        :param stage: 
        :type stage: (optional) ask_smapi_model.v1.isp.stage.Stage
        :param editable_state: 
        :type editable_state: (optional) ask_smapi_model.v1.isp.editable_state.EditableState
        :param purchasable_state: 
        :type purchasable_state: (optional) ask_smapi_model.v1.isp.purchasable_state.PurchasableState
        :param links: 
        :type links: (optional) ask_smapi_model.v1.isp.isp_summary_links.IspSummaryLinks
        :param pricing: In-skill product pricing information.
        :type pricing: (optional) dict(str, ask_smapi_model.v1.isp.summary_marketplace_pricing.SummaryMarketplacePricing)
        """
        self.__discriminator_value = None  # type: str

        self.object_type = object_type
        self.product_id = product_id
        self.reference_name = reference_name
        self.last_updated = last_updated
        self.name_by_locale = name_by_locale
        self.status = status
        self.stage = stage
        self.editable_state = editable_state
        self.purchasable_state = purchasable_state
        self.links = links
        self.pricing = pricing

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
        if not isinstance(other, InSkillProductSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
