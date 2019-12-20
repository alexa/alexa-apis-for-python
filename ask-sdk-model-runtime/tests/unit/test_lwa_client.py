# -*- coding: utf-8 -*-
#
# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the
# License.
#
import six
import unittest

from dateutil import tz
import datetime
from pytest import raises

from ask_sdk_model_runtime import (
    ApiClient, ApiClientResponse, ApiConfiguration,
    AuthenticationConfiguration, Serializer, ServiceException)
from ask_sdk_model_runtime.lwa import (
    AccessToken, AccessTokenResponse, LwaClient)

if six.PY3:
    from unittest import mock
else:
    import mock


class MockedApiClient(ApiClient):
    def __init__(self):
        self.request = None

    def invoke(self, request):
        self.request = request
        return self.empty_response()

    def empty_response(self):
        fake_response = ApiClientResponse()
        fake_response.status_code = 200
        return fake_response


class TestBaseServiceClient(unittest.TestCase):
    def test_lwa_client_init_no_auth_config_throw_exception(self):
        with raises(ValueError) as exc:
            lwa_client = LwaClient(
                api_configuration=ApiConfiguration(),
                authentication_configuration=None)

        self.assertEqual(str(exc.value), (
            "authentication_configuration must be provided"), (
            "LwaClient Initialization didn't throw exception if a null "
            "Authentication Configuration is passed"))

    def test_get_access_token_for_null_scope_throw_exception(self):
        test_lwa_client = LwaClient(
            api_configuration=ApiConfiguration(),
            authentication_configuration=AuthenticationConfiguration())

        with raises(ValueError) as exc:
            test_lwa_client.get_access_token_for_scope(scope=None)

        self.assertEqual(str(exc.value), "scope must be provided", (
            "LWA Client get access token call didn't throw exception if a "
            "null scope is passed"))

    def test_get_access_token_retrieve_from_cache(self):
        test_lwa_client = LwaClient(
            api_configuration=ApiConfiguration(),
            authentication_configuration=AuthenticationConfiguration())
        test_scope = "test"
        expected_token_value = "test_token"
        test_token_expiry = (
                datetime.datetime.now(tz.tzutc()) +
                datetime.timedelta(hours=1))
        test_access_token = AccessToken(
            token=expected_token_value, expiry=test_token_expiry)

        test_lwa_client._scoped_token_cache[test_scope] = test_access_token

        actual_token_value = test_lwa_client.get_access_token_for_scope(
            scope=test_scope)

        self.assertEqual(expected_token_value, actual_token_value, (
            "LWA Client get access token call didn't retrieve unexpired "
            "scoped access token from cache when available"))

    def test_get_access_token_cache_miss_api_call_success(self):
        mocked_api_client = MockedApiClient()
        mocked_serializer = mock.MagicMock(spec=Serializer)
        mocked_serializer.serialize.return_value = "access token request"
        local_now = datetime.datetime.now(tz.tzutc())
        test_scope = "test"
        test_client_id = "test_client_id"
        test_client_secret = "test_client_secret"

        expected_token_value = "test_token"
        expected_headers = [(
            'Content-type', 'application/x-www-form-urlencoded')]
        expected_request_method = "POST"
        expected_request_url = "https://api.amazon.com/auth/O2/token"
        expected_request_body = (
            "grant_type=client_credentials&client_id={}&client_secret={}"
            "&scope={}").format(test_client_id, test_client_secret, test_scope)

        mocked_serializer.deserialize.return_value = AccessTokenResponse(
            access_token=expected_token_value, expires_in=10, scope=test_scope)

        test_lwa_client = LwaClient(
            api_configuration=ApiConfiguration(
                serializer=mocked_serializer,
                api_client=mocked_api_client),
            authentication_configuration=AuthenticationConfiguration(
                client_id=test_client_id,
                client_secret=test_client_secret))

        with mock.patch(
                "ask_sdk_model_runtime.lwa.lwa_client.datetime") as mock_date:
            mock_date.now.return_value = local_now
            actual_token_value = test_lwa_client.get_access_token_for_scope(
                scope=test_scope)

        self.assertEqual(expected_token_value, actual_token_value, (
            "LWA Client get access token call didn't retrieve scoped access token"))

        actual_token_expiry = test_lwa_client._scoped_token_cache[
            test_scope].expiry

        self.assertEqual((local_now + datetime.timedelta(
            seconds=10)), actual_token_expiry, (
            "LWA Client get access token call cached wrong access token "
            "expiry date"))

        self.assertEqual(mocked_api_client.request.headers, expected_headers, (
            "LWA Client get access token called API with wrong headers"))
        self.assertEqual(mocked_api_client.request.method, expected_request_method, (
            "LWA Client get access token called API with wrong HTTP method"))
        self.assertEqual(mocked_api_client.request.url, expected_request_url, (
            "LWA Client get access token called API with wrong HTTP URL"))
        mocked_serializer.serialize.assert_called_with(expected_request_body)

    def test_get_access_token_for_smapi_cache_miss_api_call_success(
            self):
        mocked_api_client = MockedApiClient()
        mocked_serializer = mock.MagicMock(spec=Serializer)
        mocked_serializer.serialize.return_value = "access token request"
        local_now = datetime.datetime.now(tz.tzutc())
        refresh_access_token = "refresh_access_token"
        test_refresh_token = "test_refresh_token"
        test_grant_type = "refresh_token"
        test_client_id = "test_client_id"
        test_client_secret = "test_client_secret"

        expected_token_value = "test_token"
        expected_headers = [(
            'Content-type', 'application/x-www-form-urlencoded')]
        expected_request_method = "POST"
        expected_request_url = "https://api.amazon.com/auth/O2/token"
        expected_request_body = (
            "grant_type={}&client_id={}&client_secret={}"
            "&refresh_token={}").format(test_grant_type, test_client_id,
                                        test_client_secret, test_refresh_token)

        mocked_serializer.deserialize.return_value = AccessTokenResponse(
            access_token=expected_token_value, expires_in=10, scope=None)

        test_lwa_client = LwaClient(
            api_configuration=ApiConfiguration(
                serializer=mocked_serializer,
                api_client=mocked_api_client),
            authentication_configuration=AuthenticationConfiguration(
                client_id=test_client_id,
                client_secret=test_client_secret,
                refresh_token=test_refresh_token),
            grant_type=test_grant_type
            )

        with mock.patch(
                "ask_sdk_model_runtime.lwa.lwa_client.datetime") as mock_date:
            mock_date.now.return_value = local_now
            actual_token_value = test_lwa_client.get_access_token_from_refresh_token()

        self.assertEqual(expected_token_value, actual_token_value, (
            "LWA Client get access token call didn't retrieve unexpired "
            "scoped access token from cache when available"))

        actual_token_expiry = test_lwa_client._scoped_token_cache[
            refresh_access_token].expiry

        self.assertEqual((local_now + datetime.timedelta(
            seconds=10)), actual_token_expiry, (
            "LWA Client get access token call cached wrong access token "
            "expiry date"))

        self.assertEqual(mocked_api_client.request.headers, expected_headers, (
            "LWA Client get access token called API with wrong headers"))
        self.assertEqual(mocked_api_client.request.method, expected_request_method, (
            "LWA Client get access token called API with wrong HTTP method"))
        self.assertEqual(mocked_api_client.request.url, expected_request_url, (
            "LWA Client get access token called API with wrong HTTP URL"))
        mocked_serializer.serialize.assert_called_with(expected_request_body)


    def test_get_access_token_for_default_endpoint_api_success(
            self):
        mocked_api_client = MockedApiClient()
        mocked_serializer = mock.MagicMock(spec=Serializer)
        mocked_serializer.serialize.return_value = "access token request"
        local_now = datetime.datetime.now(tz.tzutc())
        test_scope = "test"
        test_client_id = "test_client_id"
        test_client_secret = "test_client_secret"
        test_endpoint = "https://foo.com"

        expected_token_value = "test_token"
        expected_request_url = "{}/auth/O2/token".format(test_endpoint)

        mocked_serializer.deserialize.return_value = AccessTokenResponse(
            access_token=expected_token_value, expires_in=10, scope=test_scope)

        test_lwa_client = LwaClient(
            api_configuration=ApiConfiguration(
                serializer=mocked_serializer,
                api_client=mocked_api_client, 
                api_endpoint=test_endpoint),
            authentication_configuration=AuthenticationConfiguration(
                client_id=test_client_id,
                client_secret=test_client_secret))

        with mock.patch(
                "ask_sdk_model_runtime.lwa.lwa_client.datetime") as mock_date:
            mock_date.now.return_value = local_now
            actual_token_value = test_lwa_client.get_access_token_for_scope(
                scope=test_scope)

        self.assertEqual(expected_token_value, actual_token_value, (
            "LWA Client get access token call didn't retrieve scoped access "
            "token when a custom endpoint is passed"))

        self.assertEqual(mocked_api_client.request.url, expected_request_url, (
            "LWA Client get access token called API with wrong HTTP URL, "
            "when a custom endpoint is passed"))

    def test_get_access_token_api_call_fails_throws_exception(
            self):
        mocked_serializer = mock.MagicMock(spec=Serializer)
        mocked_serializer.serialize.return_value = "access token request"
        test_scope = "test"

        fake_response = ApiClientResponse()
        fake_response.status_code = 400
        fake_response.body = "test_body"

        fake_api_client = mock.MagicMock(spec=ApiClient)
        fake_api_client.invoke.return_value = fake_response

        mocked_serializer.deserialize.return_value = "test error body"

        test_lwa_client = LwaClient(
            api_configuration=ApiConfiguration(
                serializer=mocked_serializer,
                api_client=fake_api_client),
            authentication_configuration=AuthenticationConfiguration())

        with raises(ServiceException) as exc:
            _actual_token_value = test_lwa_client.get_access_token_for_scope(
                scope=test_scope)

        self.assertIn("Bad Request", str(exc.value), (
            "LWA Client get access token threw unknown exception when "
            "the LWA API call failed with an known exception"))


    def test_get_access_token_for_null_lwa_response_throw_exception(
            self):
        mocked_api_client = MockedApiClient()
        mocked_serializer = mock.MagicMock(spec=Serializer)
        test_scope = "test"

        test_lwa_client = LwaClient(
            api_configuration=ApiConfiguration(
                serializer=mocked_serializer,
                api_client=mocked_api_client),
            authentication_configuration=AuthenticationConfiguration())

        with mock.patch.object(
                test_lwa_client, "_generate_access_token", return_value=None):

            with raises(ValueError) as exc:
                test_lwa_client.get_access_token_for_scope(scope=test_scope)

            self.assertEqual(str(exc.value), "Invalid response from LWA Client " \
                                     "generate access token call", (
                "LWA Client get access token call didn't throw exception if a "
                "generate access token returns None "))