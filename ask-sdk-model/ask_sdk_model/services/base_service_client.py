# -*- coding: utf-8 -*-
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
import six
import typing
from six.moves.urllib.parse import quote
from six.moves.urllib.parse import urlencode

from .api_client_request import ApiClientRequest
from .service_exception import ServiceException

if six.PY3:
    unicode_type = str
else:
    unicode_type = unicode

if typing.TYPE_CHECKING:
    from typing import TypeVar, Union, List, Dict, Tuple
    from .service_client_response import ServiceClientResponse
    from .api_configuration import ApiConfiguration
    T = TypeVar('T')


class BaseServiceClient(object):
    """Class to be used as the base class for the generated service clients.

    The class has to be implemented by the service clients and this class instantiation is not supported

    :param api_configuration: ApiConfiguration implementation
    :type api_configuration: ask_sdk_model.services.api_configuration.ApiConfiguration
    """

    def __init__(self, api_configuration):
        # type: (ApiConfiguration) -> None
        """Class to be used as the base class for the generated service clients.

        :param api_configuration: ApiConfiguration implementation
        :type api_configuration: ask_sdk_model.services.api_configuration.ApiConfiguration
        """
        self._api_client = api_configuration.api_client
        self._serializer = api_configuration.serializer
        self._authorization_value = api_configuration.authorization_value
        self._api_endpoint = api_configuration.api_endpoint

    def invoke(
            self, method, endpoint, path, query_params, header_params, path_params, response_definitions, body,
            response_type):
        # type: (str, str, str, List[Tuple[str, str]], List[Tuple[str, str]], Dict[str, str], List[ServiceClientResponse], T, Union[str, T]) -> Union[None, T]
        """Calls the ApiClient based on the ServiceClient specific data provided as well as handles the
        well-known responses from the Api.

        :param method: Http method
        :type method: str
        :param endpoint: Base endpoint to make the request to
        :type method: str
        :param path: Specific path to hit. It might contain variables to be interpolated with path_params
        :type path: str
        :param query_params: Parameter values to be sent as part of query string
        :type query_params: list(tuple(str, str))
        :param header_params: Parameter values to be sent as headers
        :type header_params: list(tuple(str, str))
        :param path_params: Parameter values to be interpolated in the path
        :type path_params: dict(str, str)
        :param response_definitions: Well-known expected responses by the ServiceClient
        :type response_definitions: list(ask_sdk_model.services.service_client_response.ServiceClientResponse)
        :param body: Request body
        :type body: object
        :param response_type: Type of the expected response if applicable
        :type response_type: class
        :return: Response object instance of the response_type provided
        :rtype: object
        :raises: :py:class:`ask_sdk_model.services.service_exception.ServiceException`
        """
        request = ApiClientRequest()
        request.url = BaseServiceClient.__build_url(
            endpoint=endpoint, path=path, query_params=query_params, path_params=path_params)
        request.method = method
        request.headers = header_params

        if body:
            request.body = self._serializer.serialize(body)

        try:
            response = self._api_client.invoke(request)
        except Exception as e:
            raise ServiceException(
                message="Call to service failed: {}".format(str(e)), status_code=500, headers=None, body=None)

        if BaseServiceClient.__is_code_successful(response.status_code):
            if response_type is None:
                return None
            return self._serializer.deserialize(response.body, response_type)

        if response_definitions:
            exception_metadata = [d for d in response_definitions if d.status_code == response.status_code]
            if exception_metadata:
                exception_metadata = exception_metadata[0]
                exception_body = self._serializer.deserialize(response.body, exception_metadata.response_type)
                raise ServiceException(
                    message=exception_metadata.message, status_code=exception_metadata.status_code,
                    headers=response.headers, body=exception_body)

        raise ServiceException(
            message="Unknown error", status_code=response.status_code, headers=response.headers, body=response.body)

    @staticmethod
    def __is_code_successful(response_code):
        # type: (int) -> bool
        """Check if the response is a successful response
        :type response_code: int
        :rtype: bool
        """
        return 200 <= response_code < 300

    @staticmethod
    def __interpolate_params(path, path_params):
        # type: (str, Dict[str, str]) -> str
        """Interpolate path with path params.

        :param path: Path to send the api call. Could contain variables in {} braces
        :type path: str
        :param path_params: Parameters to be interpolated in the path. Keys should match variables specified in the path # noqa: E501
        :type path_params: dict(str, str)
        :return: Interpolated path with path param values
        :rtype: str
        """
        if not path_params:
            return path

        for param_name, param_val in six.iteritems(path_params):
            path = path.replace('{' + param_name + '}', quote(str(param_val), safe=''))
        return path

    @staticmethod
    def __build_query_string(query_params, is_query_start):
        # type: (List[tuple[str, str]], bool) -> str
        """Build query string from query parameters.

        :param query_params: Parameters sent as part of query string
        :type query_params: list(tuple(str, str))
        :param is_query_start: Does query starts with constant
        :type is_query_start: bool
        :return: Query string built from query parameters
        :rtype: str
        """
        if not query_params:
            return ""

        query_string = "&" if is_query_start else "?"
        encoded_query_params = []
        for query_param in query_params:
            param_name = query_param[0]
            param_value = query_param[1]
            param_name = param_name.encode("utf-8") if isinstance(param_name, unicode_type) else param_name
            param_value = param_value.encode("utf-8") if isinstance(param_value, unicode_type) else param_value
            encoded_query_params.append((param_name, param_value))

        return query_string + urlencode(encoded_query_params)

    @staticmethod
    def __build_url(endpoint, path, query_params, path_params):
        # type: (str, str, List[tuple[str, str]], Dict[str, str]) -> str
        """Build URL from the provided parameters.

        :param endpoint: Endpoint to be sending the api call
        :type endpoint: str
        :param path: Path to send the api call. Could contain variables in {} braces
        :type path: str
        :param query_params: Query Parameters to be appended to the url
        :type query_params: list(tuple(str, str)
        :param path_params: Parameters to be interpolated in the path. Keys should match variables specified in the path # noqa: E501
        :type path_params: dict(str, str)
        :return Built url
        :rtype: str
        """
        process_endpoint = endpoint[:-1] if endpoint.endswith("/") else endpoint
        path_with_params = BaseServiceClient.__interpolate_params(path, path_params)
        is_constant_query_present = "?" in path_with_params
        query_string = BaseServiceClient.__build_query_string(query_params, is_constant_query_present)

        return '{}{}{}'.format(process_endpoint, path_with_params, query_string)
