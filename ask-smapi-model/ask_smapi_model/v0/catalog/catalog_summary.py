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
    from ask_smapi_model.v0.catalog.catalog_type import CatalogType as Catalog_CatalogTypeV0
    from ask_smapi_model.v0.catalog.catalog_usage import CatalogUsage as Catalog_CatalogUsageV0


class CatalogSummary(object):
    """

    :param id: Unique identifier of the added catalog object.
    :type id: (optional) str
    :param title: Title of the catalog.
    :type title: (optional) str
    :param object_type: 
    :type object_type: (optional) ask_smapi_model.v0.catalog.catalog_type.CatalogType
    :param usage: 
    :type usage: (optional) ask_smapi_model.v0.catalog.catalog_usage.CatalogUsage
    :param last_updated_date: The date time when the catalog was last updated.
    :type last_updated_date: (optional) datetime
    :param created_date: The date time when the catalog was created.
    :type created_date: (optional) datetime
    :param associated_skill_ids: The list of skill Ids associated with the catalog.
    :type associated_skill_ids: (optional) list[str]

    """
    deserialized_types = {
        'id': 'str',
        'title': 'str',
        'object_type': 'ask_smapi_model.v0.catalog.catalog_type.CatalogType',
        'usage': 'ask_smapi_model.v0.catalog.catalog_usage.CatalogUsage',
        'last_updated_date': 'datetime',
        'created_date': 'datetime',
        'associated_skill_ids': 'list[str]'
    }  # type: Dict

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'object_type': 'type',
        'usage': 'usage',
        'last_updated_date': 'lastUpdatedDate',
        'created_date': 'createdDate',
        'associated_skill_ids': 'associatedSkillIds'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, id=None, title=None, object_type=None, usage=None, last_updated_date=None, created_date=None, associated_skill_ids=None):
        # type: (Optional[str], Optional[str], Optional[Catalog_CatalogTypeV0], Optional[Catalog_CatalogUsageV0], Optional[datetime], Optional[datetime], Optional[List[object]]) -> None
        """

        :param id: Unique identifier of the added catalog object.
        :type id: (optional) str
        :param title: Title of the catalog.
        :type title: (optional) str
        :param object_type: 
        :type object_type: (optional) ask_smapi_model.v0.catalog.catalog_type.CatalogType
        :param usage: 
        :type usage: (optional) ask_smapi_model.v0.catalog.catalog_usage.CatalogUsage
        :param last_updated_date: The date time when the catalog was last updated.
        :type last_updated_date: (optional) datetime
        :param created_date: The date time when the catalog was created.
        :type created_date: (optional) datetime
        :param associated_skill_ids: The list of skill Ids associated with the catalog.
        :type associated_skill_ids: (optional) list[str]
        """
        self.__discriminator_value = None  # type: str

        self.id = id
        self.title = title
        self.object_type = object_type
        self.usage = usage
        self.last_updated_date = last_updated_date
        self.created_date = created_date
        self.associated_skill_ids = associated_skill_ids

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
        if not isinstance(other, CatalogSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
