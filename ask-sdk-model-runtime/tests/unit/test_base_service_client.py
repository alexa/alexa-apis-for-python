# -*- coding: utf-8 -*-
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
import six
import unittest
from pytest import raises

from ask_sdk_model_runtime import (
    ApiClient, ApiClientResponse, ApiConfiguration,
    BaseServiceClient, Serializer, ServiceException, ServiceClientResponse)

if six.PY3:
    from unittest import mock
else:
    import mock


class MockedApiClient(ApiClient):
    def invoke(self, request):
        self.request = request
        return self.empty_response()

    def empty_response(self):
        fake_response = ApiClientResponse()
        fake_response.status_code = 200
        return fake_response


class MockedBaseServiceClient(object):
    @staticmethod
    def empty_response():
        mocked_api_client = MockedApiClient()
        mocked_serializer = mock.MagicMock(spec=Serializer)
        api_configuration = ApiConfiguration(
            serializer=mocked_serializer, api_client=mocked_api_client,
            authorization_value="test_token", api_endpoint="test_endpoint")
        return BaseServiceClient(api_configuration=api_configuration)

    @staticmethod
    def service_client_null_api_client():
        mocked_serializer = mock.MagicMock(spec=Serializer)
        api_configuration = ApiConfiguration(
            serializer=mocked_serializer, api_client=None,
            authorization_value="test_token", api_endpoint="test_endpoint")
        return BaseServiceClient(api_configuration=api_configuration)
        
    @staticmethod
    def service_client_null_serializer():
        mocked_api_client = MockedApiClient()
        api_configuration = ApiConfiguration(
            serializer=None, api_client=mocked_api_client,
            authorization_value="test_token", api_endpoint="test_endpoint")
        return BaseServiceClient(api_configuration=api_configuration)


class TestBaseServiceClient(unittest.TestCase):
    def test_invoke_build_url_with_path_when_endpoint_path_passed(
            self):
        mocked_api_client = MockedApiClient()
        mocked_serializer = mock.MagicMock(spec=Serializer)
        endpoint = "http://test.com"
        path = "/v1/x/y"
        expected = "http://test.com/v1/x/y"

        mocked_base_service_client_api_client_empty_response = MockedBaseServiceClient.empty_response()
        mocked_base_service_client_api_client_empty_response.invoke(
            method="GET", endpoint=endpoint, path=path, query_params=[],
            header_params=[], path_params={},response_definitions=[],
            body=None, response_type=None)

        self.assertEqual(mocked_base_service_client_api_client_empty_response._api_client.request.url, expected,\
            "Build URL failed when endpoint and path passed")

    def test_invoke_build_url_with_no_duplicate_slash_path_when_endpoint_path_has_slash(self):
        endpoint = "http://test.com/"
        path = "/v1/x/y"
        expected = "http://test.com/v1/x/y"

        mocked_base_service_client_api_client_empty_response = MockedBaseServiceClient.empty_response()
        mocked_base_service_client_api_client_empty_response.invoke(
            method="GET", endpoint=endpoint, path=path, query_params=[],
            header_params=[], path_params={}, response_definitions=[],
            body=None, response_type=None)

        self.assertEqual(mocked_base_service_client_api_client_empty_response._api_client.request.url, expected,\
            "Build URL failed when endpoint and path with duplicate slash passed")

    def test_invoke_build_url_with_query_params(
            self):
        endpoint = "http://test.com/"
        path = "/v1/x/y/"
        query_params = [("filter", "test_filter"), ("select", "test_select"),
                        ("value", "test_value")]
        expected = "http://test.com/v1/x/y/?filter=test_filter&" \
                   "select=test_select&value=test_value"
        mocked_base_service_client_api_client_empty_response = MockedBaseServiceClient.empty_response()
        mocked_base_service_client_api_client_empty_response.invoke(
            method="GET", endpoint=endpoint, path=path,
            query_params=query_params, header_params=[], path_params={},
            response_definitions=[], body=None, response_type=None)

        self.assertEqual(mocked_base_service_client_api_client_empty_response._api_client.request.url, expected,\
            "Build URL failed when endpoint, path and query parameters passed")

    def test_invoke_build_url_with_query_params_list_container(self):
        endpoint = "http://test.com/"
        path = "/v1/x/y/"
        query_params = [("filter", ["test_filter_1", "test_filter_2"])]
        expected = "http://test.com/v1/x/y/?filter=test_filter_1&filter=test_filter_2"

        mocked_base_service_client_api_client_empty_response = MockedBaseServiceClient.empty_response()
        mocked_base_service_client_api_client_empty_response.invoke(
            method="GET", endpoint=endpoint, path=path, query_params=query_params, header_params=[], path_params={},
            response_definitions=[], body=None, response_type=None)

        self.assertEqual(mocked_base_service_client_api_client_empty_response._api_client.request.url, expected, \
            "Build URL failed when endpoint, path and query parameters containing list of values passed")

    def test_invoke_build_url_with_query_params_special_chars(
            self):
        endpoint = "http://test.com/"
        path = "/v1/x/y/"
        query_params = [(u"å", u"∫"), ("test", "test message with $ < > values")]
        expected = "http://test.com/v1/x/y/?%C3%A5=%E2%88%AB&" \
                   "test=test+message+with+%24+%3C+%3E+values"

        mocked_base_service_client_api_client_empty_response = MockedBaseServiceClient.empty_response()
        mocked_base_service_client_api_client_empty_response.invoke(
            method="GET", endpoint=endpoint, path=path,
            query_params=query_params, header_params=[], path_params={},
            response_definitions=[], body=None, response_type=None)

        self.assertEqual(mocked_base_service_client_api_client_empty_response._api_client.request.url, expected,\
            "Build URL failed when endpoint, path and query parameters containing special characters passed")

    def test_invoke_build_url_with_query_params_static_content(
            self):
        endpoint = "http://test.com/"
        path = "/v1/x/y/?a=b"
        query_params = [("c", "d")]
        expected = "http://test.com/v1/x/y/?a=b&c=d"

        mocked_base_service_client_api_client_empty_response = MockedBaseServiceClient.empty_response()
        mocked_base_service_client_api_client_empty_response.invoke(
            method="GET", endpoint=endpoint, path=path,
            query_params=query_params, header_params=[], path_params={},
            response_definitions=[], body=None, response_type=None)

        self.assertEqual(mocked_base_service_client_api_client_empty_response._api_client.request.url, expected,\
            "Build URL failed when endpoint, path and query parameters containing static content passed")

    def test_invoke_build_url_with_path_params_interpolated(
            self):
        endpoint = "http://test.com/"
        path = "/v1/{x_id}/y/{z_value}"
        path_params = {
            "x_id": "x",
            "z_value": "z"
        }
        expected = "http://test.com/v1/x/y/z"

        mocked_base_service_client_api_client_empty_response = MockedBaseServiceClient.empty_response()
        mocked_base_service_client_api_client_empty_response.invoke(
            method="GET", endpoint=endpoint, path=path, query_params=[],
            header_params=[], path_params=path_params, response_definitions=[],
            body=None, response_type=None)

        self.assertEqual(mocked_base_service_client_api_client_empty_response._api_client.request.url, expected,\
            "Build URL failed when endpoint, path and path parameters passed")

    def test_invoke_build_url_with_path_params_containing_special_chars_interpolated(
            self):
        endpoint = "http://test.com/"
        path = "/v1/{x_id}/y/{z_value}"
        path_params = {
            "x_id": "å",
            "z_value": "∫"
        }
        expected = "http://test.com/v1/%C3%A5/y/%E2%88%AB"

        mocked_base_service_client_api_client_empty_response = MockedBaseServiceClient.empty_response()
        mocked_base_service_client_api_client_empty_response.invoke(
            method="GET", endpoint=endpoint, path=path, query_params=[],
            header_params=[], path_params=path_params, response_definitions=[],
            body=None, response_type=None)

        self.assertEqual(mocked_base_service_client_api_client_empty_response._api_client.request.url, expected,\
            "Build URL failed when endpoint, path and path parameters containing special characters passed")

    def test_invoke_build_url_with_path_params_with_path_ending_in_slash(
            self):
        endpoint = "http://test.com/"
        path = "/v1/x/y/"
        expected = "http://test.com/v1/x/y/"

        mocked_base_service_client_api_client_empty_response = MockedBaseServiceClient.empty_response()
        mocked_base_service_client_api_client_empty_response.invoke(
            method="GET", endpoint=endpoint, path=path, query_params=[],
            header_params=[], path_params={}, response_definitions=[],
            body=None, response_type=None)

        self.assertEqual(mocked_base_service_client_api_client_empty_response._api_client.request.url, expected,\
            "Build URL failed when endpoint, path with ending slash passed")

    def test_invoke_serializes_body_when_passed(self):
        mocked_api_client = MockedApiClient()
        mocked_serializer = mock.MagicMock(spec=Serializer)
        mocked_serializer.serialize.return_value = "serialized_payload"
        fake_body = mock.Mock()
        fake_api_config = ApiConfiguration(
            serializer=mocked_serializer, api_client=mocked_api_client,
            authorization_value="test_token", api_endpoint="test_endpoint")
        fake_base_service_client = BaseServiceClient(api_configuration=fake_api_config)

        fake_base_service_client.invoke(
            method="GET", endpoint="http://test.com", path="", query_params=[],
            header_params=[], path_params={}, response_definitions=[],
            body=fake_body, response_type=None)

        mocked_serializer.serialize.assert_called_with(fake_body)

    def test_invoke_serializes_body_not_run_for_null_body(self):
        mocked_api_client = MockedApiClient()
        mocked_serializer = mock.MagicMock(spec=Serializer)
        fake_api_config = ApiConfiguration(
            serializer=mocked_serializer, api_client=mocked_api_client,
            authorization_value="test_token", api_endpoint="test_endpoint")
        fake_base_service_client = BaseServiceClient(api_configuration=fake_api_config)

        fake_base_service_client.invoke(
            method="GET", endpoint="http://test.com", path="", query_params=[],
            header_params=[], path_params={}, response_definitions=[],
            body=None, response_type=None)

        self.assertNotEqual(mocked_serializer.serialize.called, "Invoke called serializer for null body")

    def test_invoke_api_client_throws_exception(self):
        mocked_serializer = mock.MagicMock(spec=Serializer)
        fake_api_client = mock.MagicMock(spec=ApiClient)
        fake_api_client.invoke.side_effect = Exception("test exception")

        fake_api_config = ApiConfiguration(
            serializer=mocked_serializer, api_client=fake_api_client,
            authorization_value="test_token", api_endpoint="test_endpoint")
        fake_base_service_client = BaseServiceClient(api_configuration=fake_api_config)

        with raises(ServiceException) as exc:
            fake_base_service_client.invoke(
                method="GET", endpoint="http://test.com", path="",
                query_params=[], header_params=[], path_params={},
                response_definitions=[], body=None, response_type=None)

        self.assertEqual(str(exc.value), "Call to service failed: test exception", \
            "Service exception not raised during base service client invoke when api client invoke raises")
        self.assertEqual(exc.value.status_code, 500, (
            "Service exception raised during base service client invoke has different status code than expected, "
            "when api client invoke raises"))

    def test_invoke_serializes_response_if_present(self):
        mocked_serializer = mock.MagicMock(spec=Serializer)
        fake_response = ApiClientResponse()
        fake_response.body = "test_body"
        fake_response.status_code = 200
        fake_response_type = "test_response_type"

        fake_api_client = mock.MagicMock(spec=ApiClient)
        fake_api_client.invoke.return_value = fake_response

        mocked_serializer.deserialize.return_value = "deserialized_payload"

        fake_api_config = ApiConfiguration(
            serializer=mocked_serializer, api_client=fake_api_client,
            authorization_value="test_token", api_endpoint="test_endpoint")
        fake_base_service_client = BaseServiceClient(
            api_configuration=fake_api_config)

        response = fake_base_service_client.invoke(
            method="GET", endpoint="http://test.com", path="", query_params=[],
            header_params=[], path_params={}, response_definitions=[],
            body=None, response_type=fake_response_type)

        self.assertEqual(response.body, "deserialized_payload", "Response from api client not deserialized by base service client")
        mocked_serializer.deserialize.assert_called_with(payload=fake_response.body, obj_type=fake_response_type), \
            "Base service client called deserialize on Response from api client with wrong values"

    def test_invoke_return_api_response_for_no_content_response(self):
        mocked_serializer = mock.MagicMock(spec=Serializer)
        fake_response = ApiClientResponse()
        fake_response.body = ""
        fake_response.status_code = 204
        fake_response_type = "test_response_type"

        fake_api_client = mock.MagicMock(spec=ApiClient)
        fake_api_client.invoke.return_value = fake_response

        fake_api_config = ApiConfiguration(
            serializer=mocked_serializer, api_client=fake_api_client,
            authorization_value="test_token", api_endpoint="test_endpoint")
        fake_base_service_client = BaseServiceClient(
            api_configuration=fake_api_config)

        response = fake_base_service_client.invoke(
            method="GET", endpoint="http://test.com", path="", query_params=[],
            header_params=[], path_params={}, response_definitions=[],
            body=None, response_type=fake_response_type)

        self.assertIsNone(response.body, "Base service client returns invalid response when status code is 204")
        self.assertEqual(response.status_code, 204, "Base service client returns invalid status code")
        self.assertIsNot(mocked_serializer.deserialize.called, (
            "Base service client invoke method deserialized no content response body"))

    def test_invoke_return_full_api_response(self):
        mocked_serializer = mock.MagicMock(spec=Serializer)
        fake_response = ApiClientResponse()
        fake_response.body = "test_body"
        fake_response.status_code = 200
        fake_response.headers = "test_headers"
        fake_response_type = "test_response_type"

        fake_api_client = mock.MagicMock(spec=ApiClient)
        fake_api_client.invoke.return_value = fake_response

        fake_api_config = ApiConfiguration(
            serializer=mocked_serializer, api_client=fake_api_client,
            authorization_value="test_token", api_endpoint="test_endpoint")
        fake_base_service_client = BaseServiceClient(
            api_configuration=fake_api_config)

        mocked_serializer.deserialize.return_value = "deserialized_payload"

        response = fake_base_service_client.invoke(
            method="GET", endpoint="http://test.com", path="", query_params=[],
            header_params=[], path_params={}, response_definitions=[],
            body=None, response_type=fake_response_type)

        self.assertEqual(response.body, "deserialized_payload", ("Base service client returns invalid api response when status code is 204"))
        self.assertEqual(response.headers, "test_headers", ("Base service client return invalid api response with null headers"))
        self.assertEqual(response.status_code, 200, ("Base service client return invalid api response with null status_code"))

    def test_invoke_return_api_response_with_none_body(self):
        mocked_serializer = mock.MagicMock(spec=Serializer)
        fake_response = ApiClientResponse()
        fake_response.body = ""
        fake_response.status_code = 204
        fake_response.headers = "test_headers"
        fake_response_type = "test_response_type"

        fake_api_client = mock.MagicMock(spec=ApiClient)
        fake_api_client.invoke.return_value = fake_response

        fake_api_config = ApiConfiguration(
            serializer=mocked_serializer, api_client=fake_api_client,
            authorization_value="test_token", api_endpoint="test_endpoint")
        fake_base_service_client = BaseServiceClient(
            api_configuration=fake_api_config)

        response = fake_base_service_client.invoke(
            method="GET", endpoint="http://test.com", path="", query_params=[],
            header_params=[], path_params={}, response_definitions=[],
            body=None, response_type=fake_response_type)

        self.assertIsNone(response.body, ("Base service client returns invalid api response when status code is 204"))
        self.assertEqual(response.headers, "test_headers", ("Base service client return invalid api response with null headers"))
        self.assertEqual(response.status_code, 204, ("Base service client return invalid api response with null status_code"))

        self.assertIsNot(mocked_serializer.deserialize.called, (
            "Base service client invoke method deserialized no content response body"))

    def test_invoke_throw_exception_if_no_definitions_provided_for_unsuccessful_response(self):
        mocked_serializer = mock.MagicMock(spec=Serializer)
        fake_response = ApiClientResponse()
        fake_response.status_code = 450

        fake_api_client = mock.MagicMock(spec=ApiClient)
        fake_api_client.invoke.return_value = fake_response

        fake_api_config = ApiConfiguration(
            serializer=mocked_serializer, api_client=fake_api_client,
            authorization_value="test_token", api_endpoint="test_endpoint")
        fake_base_service_client = BaseServiceClient(api_configuration=fake_api_config)

        with raises(ServiceException) as exc:
            fake_base_service_client.invoke(
                method="GET", endpoint="http://test.com", path="",
                query_params=[], header_params=[], path_params={},
                response_definitions=[], body=None, response_type=None)

        self.assertEqual(str(exc.value), "Unknown error", (
            "Service exception not raised during base service client invoke when response is unsuccessful and "
            "no response definitions provided"))
        self.assertEqual(exc.value.status_code, 450, (
            "Service exception raised during base service client invoke has different status code than expected, "
            "when response is unsuccessful and no response definitions provided"))

    def test_invoke_throw_exception_with_matched_definition_for_unsuccessful_response(self):
        mocked_serializer = mock.MagicMock(spec=Serializer)
        fake_response = ApiClientResponse()
        fake_response.status_code = 450
        fake_response.body = "test_body"

        fake_api_client = mock.MagicMock(spec=ApiClient)
        fake_api_client.invoke.return_value = fake_response

        mocked_serializer.deserialize.return_value = "deserialized_error_body"

        fake_api_config = ApiConfiguration(
            serializer=mocked_serializer, api_client=fake_api_client,
            authorization_value="test_token", api_endpoint="test_endpoint")
        fake_base_service_client = BaseServiceClient(
            api_configuration=fake_api_config)

        fake_response_definition_1 = ServiceClientResponse(
            response_type="test_definition_1", status_code=450,
            message="test exception with definition 1")
        fake_response_definition_2 = ServiceClientResponse(
            response_type="test_definition_2", status_code=475,
            message="test exception with definition 2")
        fake_response_definitions = [fake_response_definition_2, fake_response_definition_1]

        with raises(ServiceException) as exc:
            fake_base_service_client.invoke(
                method="GET", endpoint="http://test.com", path="",
                query_params=[], header_params=[],path_params={},
                response_definitions=fake_response_definitions,
                body=None, response_type=None)

        self.assertEqual(str(exc.value), "test exception with definition 1", (
            "Incorrect service exception raised during base service client invoke when response is unsuccessful and "
            "matching response definitions provided"))
        mocked_serializer.deserialize.assert_called_with(
            payload=fake_response.body, obj_type="test_definition_1")
        self.assertEqual(str(exc.value.body), "deserialized_error_body", (
            "Service exception raised during base service client invoke, when response is unsuccessful, "
            "has different body that expected response"))

    def test_invoke_throw_exception_with_no_matched_definition_for_unsuccessful_response(self):
        mocked_serializer = mock.MagicMock(spec=Serializer)
        fake_response = ApiClientResponse()
        fake_response.status_code = 485
        fake_response.body = "test_body"

        fake_api_client = mock.MagicMock(spec=ApiClient)
        fake_api_client.invoke.return_value = fake_response

        fake_api_config = ApiConfiguration(
            serializer=mocked_serializer, api_client=fake_api_client,
            authorization_value="test_token", api_endpoint="test_endpoint")
        fake_base_service_client = BaseServiceClient(
            api_configuration=fake_api_config)

        fake_response_definition_1 = ServiceClientResponse(
            response_type="test_definition_1", status_code=450,
            message="test exception with definition 1")
        fake_response_definition_2 = ServiceClientResponse(
            response_type="test_definition_2", status_code=475,
            message="test exception with definition 2")
        fake_response_definitions = [fake_response_definition_2, fake_response_definition_1]

        with raises(ServiceException) as exc:
            fake_base_service_client.invoke(
                method="GET", endpoint="http://test.com", path="",
                query_params=[], header_params=[], path_params={},
                response_definitions=fake_response_definitions,
                body=None, response_type=None)

        self.assertEqual(str(exc.value), "Unknown error", (
            "Incorrect service exception raised during base service client invoke when response is unsuccessful and "
            "no matching response definitions found"))
        self.assertEqual(str(exc.value.body), "test_body", (
            "Service exception raised during base service client invoke, when response is unsuccessful, "
            "has different body that expected response"))
        self.assertEqual(exc.value.status_code, 485, (
            "Service exception raised during base service client invoke, when response is unsuccessful, "
            "has different status code that expected response"))

    def test_invoke_raises_value_error_with_none_api_client(self):
        endpoint = "http://test.com"
        path = "/v1/x/y"

        with raises(ValueError) as exc:
            mocked_base_service_client_api_client_none = MockedBaseServiceClient.service_client_null_api_client()
            mocked_base_service_client_api_client_none.invoke(
                method="GET", endpoint=endpoint, path=path, query_params=[],
                header_params=[], path_params={}, response_definitions=[],
                body=None, response_type=None)

        self.assertEqual(str(exc.value), 'API client is None', (
            "Base Service Client was initialized with no api client"
        ))

    def test_invoke_raises_value_error_with_none_serializer(
            self):
        endpoint = "http://test.com"
        path = "/v1/x/y"

        with raises(ValueError) as exc:
            mocked_base_service_client_serializer_none = MockedBaseServiceClient.service_client_null_serializer()
            mocked_base_service_client_serializer_none.invoke(
                method="GET", endpoint=endpoint, path=path, query_params=[],
                header_params=[], path_params={}, response_definitions=[],
                body=None, response_type=None)

        self.assertEqual(str(exc.value), 'Serializer is None', (
            "Base Service Client was initialized with no serializer"
        ))

    def test_invoke_throw_exception_if_no_response_status_code(self):
        mocked_serializer = mock.MagicMock(spec=Serializer)
        fake_response = ApiClientResponse()
        fake_response.status_code = None

        fake_api_client = mock.MagicMock(spec=ApiClient)
        fake_api_client.invoke.return_value = fake_response

        fake_api_config = ApiConfiguration(
            serializer=mocked_serializer, api_client=fake_api_client,
            authorization_value="test_token", api_endpoint="test_endpoint")
        fake_base_service_client = BaseServiceClient(
            api_configuration=fake_api_config)

        with raises(ServiceException) as exc:
            fake_base_service_client.invoke(
                method="GET", endpoint="http://test.com", path="",
                query_params=[], header_params=[], path_params={},
                response_definitions=[], body=None, response_type=None)

        self.assertEqual(str(exc.value), "Invalid Response, no status code", (
            "Service exception raised during base service client invoke, when response is unsuccessful, "
            "has no status code"))