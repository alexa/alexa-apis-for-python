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
    from ask_smapi_model.v1.isp.custom_product_prompts import CustomProductPrompts as Isp_CustomProductPromptsV1


class LocalizedPublishingInformation(object):
    """
    Defines the structure for locale specific publishing information in the in-skill product definition.


    :param name: Name of the in-skill product that is heard by customers and displayed in the Alexa app.
    :type name: (optional) str
    :param small_icon_uri: Uri for the small icon image of the in-skill product.
    :type small_icon_uri: (optional) str
    :param large_icon_uri: Uri for the large icon image of the in-skill product.
    :type large_icon_uri: (optional) str
    :param summary: Short description of the in-skill product that displays on the in-skill product list page in the Alexa App.
    :type summary: (optional) str
    :param description: Description of the in-skill product&#39;s purpose and features, and how it works. Should describe any prerequisites like hardware or account requirements and detailed steps for the customer to get started. This description displays to customers on the in-skill product detail card in the Alexa app.
    :type description: (optional) str
    :param example_phrases: Example phrases appear on the in-skill product detail page and are the key utterances that customers can say to interact directly with the in-skill product.
    :type example_phrases: (optional) list[str]
    :param keywords: Search terms that can be used to describe the in-skill product. This helps customers find an in-skill product.
    :type keywords: (optional) list[str]
    :param custom_product_prompts: 
    :type custom_product_prompts: (optional) ask_smapi_model.v1.isp.custom_product_prompts.CustomProductPrompts

    """
    deserialized_types = {
        'name': 'str',
        'small_icon_uri': 'str',
        'large_icon_uri': 'str',
        'summary': 'str',
        'description': 'str',
        'example_phrases': 'list[str]',
        'keywords': 'list[str]',
        'custom_product_prompts': 'ask_smapi_model.v1.isp.custom_product_prompts.CustomProductPrompts'
    }  # type: Dict

    attribute_map = {
        'name': 'name',
        'small_icon_uri': 'smallIconUri',
        'large_icon_uri': 'largeIconUri',
        'summary': 'summary',
        'description': 'description',
        'example_phrases': 'examplePhrases',
        'keywords': 'keywords',
        'custom_product_prompts': 'customProductPrompts'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, name=None, small_icon_uri=None, large_icon_uri=None, summary=None, description=None, example_phrases=None, keywords=None, custom_product_prompts=None):
        # type: (Optional[str], Optional[str], Optional[str], Optional[str], Optional[str], Optional[List[object]], Optional[List[object]], Optional[Isp_CustomProductPromptsV1]) -> None
        """Defines the structure for locale specific publishing information in the in-skill product definition.

        :param name: Name of the in-skill product that is heard by customers and displayed in the Alexa app.
        :type name: (optional) str
        :param small_icon_uri: Uri for the small icon image of the in-skill product.
        :type small_icon_uri: (optional) str
        :param large_icon_uri: Uri for the large icon image of the in-skill product.
        :type large_icon_uri: (optional) str
        :param summary: Short description of the in-skill product that displays on the in-skill product list page in the Alexa App.
        :type summary: (optional) str
        :param description: Description of the in-skill product&#39;s purpose and features, and how it works. Should describe any prerequisites like hardware or account requirements and detailed steps for the customer to get started. This description displays to customers on the in-skill product detail card in the Alexa app.
        :type description: (optional) str
        :param example_phrases: Example phrases appear on the in-skill product detail page and are the key utterances that customers can say to interact directly with the in-skill product.
        :type example_phrases: (optional) list[str]
        :param keywords: Search terms that can be used to describe the in-skill product. This helps customers find an in-skill product.
        :type keywords: (optional) list[str]
        :param custom_product_prompts: 
        :type custom_product_prompts: (optional) ask_smapi_model.v1.isp.custom_product_prompts.CustomProductPrompts
        """
        self.__discriminator_value = None  # type: str

        self.name = name
        self.small_icon_uri = small_icon_uri
        self.large_icon_uri = large_icon_uri
        self.summary = summary
        self.description = description
        self.example_phrases = example_phrases
        self.keywords = keywords
        self.custom_product_prompts = custom_product_prompts

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
        if not isinstance(other, LocalizedPublishingInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
