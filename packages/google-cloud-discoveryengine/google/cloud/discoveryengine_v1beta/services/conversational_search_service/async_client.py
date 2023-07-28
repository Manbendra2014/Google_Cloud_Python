# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import (
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.discoveryengine_v1beta import gapic_version as package_version

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.longrunning import operations_pb2
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore

from google.cloud.discoveryengine_v1beta.services.conversational_search_service import (
    pagers,
)
from google.cloud.discoveryengine_v1beta.types import (
    conversational_search_service,
    search_service,
)
from google.cloud.discoveryengine_v1beta.types import conversation as gcd_conversation
from google.cloud.discoveryengine_v1beta.types import conversation

from .client import ConversationalSearchServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, ConversationalSearchServiceTransport
from .transports.grpc_asyncio import ConversationalSearchServiceGrpcAsyncIOTransport


class ConversationalSearchServiceAsyncClient:
    """Service for conversational search."""

    _client: ConversationalSearchServiceClient

    DEFAULT_ENDPOINT = ConversationalSearchServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ConversationalSearchServiceClient.DEFAULT_MTLS_ENDPOINT

    conversation_path = staticmethod(
        ConversationalSearchServiceClient.conversation_path
    )
    parse_conversation_path = staticmethod(
        ConversationalSearchServiceClient.parse_conversation_path
    )
    data_store_path = staticmethod(ConversationalSearchServiceClient.data_store_path)
    parse_data_store_path = staticmethod(
        ConversationalSearchServiceClient.parse_data_store_path
    )
    document_path = staticmethod(ConversationalSearchServiceClient.document_path)
    parse_document_path = staticmethod(
        ConversationalSearchServiceClient.parse_document_path
    )
    serving_config_path = staticmethod(
        ConversationalSearchServiceClient.serving_config_path
    )
    parse_serving_config_path = staticmethod(
        ConversationalSearchServiceClient.parse_serving_config_path
    )
    common_billing_account_path = staticmethod(
        ConversationalSearchServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ConversationalSearchServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        ConversationalSearchServiceClient.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        ConversationalSearchServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        ConversationalSearchServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        ConversationalSearchServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        ConversationalSearchServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        ConversationalSearchServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        ConversationalSearchServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        ConversationalSearchServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ConversationalSearchServiceAsyncClient: The constructed client.
        """
        return ConversationalSearchServiceClient.from_service_account_info.__func__(ConversationalSearchServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ConversationalSearchServiceAsyncClient: The constructed client.
        """
        return ConversationalSearchServiceClient.from_service_account_file.__func__(ConversationalSearchServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return ConversationalSearchServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> ConversationalSearchServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            ConversationalSearchServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(ConversationalSearchServiceClient).get_transport_class,
        type(ConversationalSearchServiceClient),
    )

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, ConversationalSearchServiceTransport] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the conversational search service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.ConversationalSearchServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = ConversationalSearchServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def converse_conversation(
        self,
        request: Optional[
            Union[conversational_search_service.ConverseConversationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        query: Optional[conversation.TextInput] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> conversational_search_service.ConverseConversationResponse:
        r"""Converses a conversation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1beta

            async def sample_converse_conversation():
                # Create a client
                client = discoveryengine_v1beta.ConversationalSearchServiceAsyncClient()

                # Initialize request argument(s)
                request = discoveryengine_v1beta.ConverseConversationRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.converse_conversation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1beta.types.ConverseConversationRequest, dict]]):
                The request object. Request message for
                [ConversationalSearchService.ConverseConversation][google.cloud.discoveryengine.v1beta.ConversationalSearchService.ConverseConversation]
                method.
            name (:class:`str`):
                Required. The resource name of the Conversation to get.
                Format:
                ``projects/{project_number}/locations/{location_id}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}``.
                Use
                ``projects/{project_number}/locations/{location_id}/collections/{collection}/dataStores/{data_store_id}/conversations/-``
                to activate auto session mode, which automatically
                creates a new conversation inside a ConverseConversation
                session.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            query (:class:`google.cloud.discoveryengine_v1beta.types.TextInput`):
                Required. Current user input.
                This corresponds to the ``query`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.discoveryengine_v1beta.types.ConverseConversationResponse:
                Response message for
                   [ConversationalSearchService.ConverseConversation][google.cloud.discoveryengine.v1beta.ConversationalSearchService.ConverseConversation]
                   method.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, query])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = conversational_search_service.ConverseConversationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if query is not None:
            request.query = query

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.converse_conversation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_conversation(
        self,
        request: Optional[
            Union[conversational_search_service.CreateConversationRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        conversation: Optional[gcd_conversation.Conversation] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcd_conversation.Conversation:
        r"""Creates a Conversation.

        If the
        [Conversation][google.cloud.discoveryengine.v1beta.Conversation]
        to create already exists, an ALREADY_EXISTS error is returned.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1beta

            async def sample_create_conversation():
                # Create a client
                client = discoveryengine_v1beta.ConversationalSearchServiceAsyncClient()

                # Initialize request argument(s)
                request = discoveryengine_v1beta.CreateConversationRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_conversation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1beta.types.CreateConversationRequest, dict]]):
                The request object. Request for CreateConversation
                method.
            parent (:class:`str`):
                Required. Full resource name of parent data store.
                Format:
                ``projects/{project_number}/locations/{location_id}/collections/{collection}/dataStores/{data_store_id}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            conversation (:class:`google.cloud.discoveryengine_v1beta.types.Conversation`):
                Required. The conversation to create.
                This corresponds to the ``conversation`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.discoveryengine_v1beta.types.Conversation:
                External conversation proto
                definition.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, conversation])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = conversational_search_service.CreateConversationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if conversation is not None:
            request.conversation = conversation

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_conversation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_conversation(
        self,
        request: Optional[
            Union[conversational_search_service.DeleteConversationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes a Conversation.

        If the
        [Conversation][google.cloud.discoveryengine.v1beta.Conversation]
        to delete does not exist, a NOT_FOUND error is returned.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1beta

            async def sample_delete_conversation():
                # Create a client
                client = discoveryengine_v1beta.ConversationalSearchServiceAsyncClient()

                # Initialize request argument(s)
                request = discoveryengine_v1beta.DeleteConversationRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_conversation(request=request)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1beta.types.DeleteConversationRequest, dict]]):
                The request object. Request for DeleteConversation
                method.
            name (:class:`str`):
                Required. The resource name of the Conversation to
                delete. Format:
                ``projects/{project_number}/locations/{location_id}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = conversational_search_service.DeleteConversationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_conversation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def update_conversation(
        self,
        request: Optional[
            Union[conversational_search_service.UpdateConversationRequest, dict]
        ] = None,
        *,
        conversation: Optional[gcd_conversation.Conversation] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcd_conversation.Conversation:
        r"""Updates a Conversation.

        [Conversation][google.cloud.discoveryengine.v1beta.Conversation]
        action type cannot be changed. If the
        [Conversation][google.cloud.discoveryengine.v1beta.Conversation]
        to update does not exist, a NOT_FOUND error is returned.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1beta

            async def sample_update_conversation():
                # Create a client
                client = discoveryengine_v1beta.ConversationalSearchServiceAsyncClient()

                # Initialize request argument(s)
                request = discoveryengine_v1beta.UpdateConversationRequest(
                )

                # Make the request
                response = await client.update_conversation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1beta.types.UpdateConversationRequest, dict]]):
                The request object. Request for UpdateConversation
                method.
            conversation (:class:`google.cloud.discoveryengine_v1beta.types.Conversation`):
                Required. The Conversation to update.
                This corresponds to the ``conversation`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Indicates which fields in the provided
                [Conversation][google.cloud.discoveryengine.v1beta.Conversation]
                to update. The following are NOT supported:

                -  [conversation.name][]

                If not set or empty, all supported fields are updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.discoveryengine_v1beta.types.Conversation:
                External conversation proto
                definition.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([conversation, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = conversational_search_service.UpdateConversationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if conversation is not None:
            request.conversation = conversation
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_conversation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("conversation.name", request.conversation.name),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_conversation(
        self,
        request: Optional[
            Union[conversational_search_service.GetConversationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> conversation.Conversation:
        r"""Gets a Conversation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1beta

            async def sample_get_conversation():
                # Create a client
                client = discoveryengine_v1beta.ConversationalSearchServiceAsyncClient()

                # Initialize request argument(s)
                request = discoveryengine_v1beta.GetConversationRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_conversation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1beta.types.GetConversationRequest, dict]]):
                The request object. Request for GetConversation method.
            name (:class:`str`):
                Required. The resource name of the Conversation to get.
                Format:
                ``projects/{project_number}/locations/{location_id}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.discoveryengine_v1beta.types.Conversation:
                External conversation proto
                definition.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = conversational_search_service.GetConversationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_conversation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_conversations(
        self,
        request: Optional[
            Union[conversational_search_service.ListConversationsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListConversationsAsyncPager:
        r"""Lists all Conversations by their parent
        [DataStore][google.cloud.discoveryengine.v1beta.DataStore].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import discoveryengine_v1beta

            async def sample_list_conversations():
                # Create a client
                client = discoveryengine_v1beta.ConversationalSearchServiceAsyncClient()

                # Initialize request argument(s)
                request = discoveryengine_v1beta.ListConversationsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_conversations(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.discoveryengine_v1beta.types.ListConversationsRequest, dict]]):
                The request object. Request for ListConversations method.
            parent (:class:`str`):
                Required. The data store resource name. Format:
                ``projects/{project_number}/locations/{location_id}/collections/{collection}/dataStores/{data_store_id}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.discoveryengine_v1beta.services.conversational_search_service.pagers.ListConversationsAsyncPager:
                Response for ListConversations
                method.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = conversational_search_service.ListConversationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_conversations,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListConversationsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_operations(
        self,
        request: Optional[operations_pb2.ListOperationsRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operations_pb2.ListOperationsResponse:
        r"""Lists operations that match the specified filter in the request.

        Args:
            request (:class:`~.operations_pb2.ListOperationsRequest`):
                The request object. Request message for
                `ListOperations` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            ~.operations_pb2.ListOperationsResponse:
                Response message for ``ListOperations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.ListOperationsRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._client._transport.list_operations,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_operation(
        self,
        request: Optional[operations_pb2.GetOperationRequest] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operations_pb2.Operation:
        r"""Gets the latest state of a long-running operation.

        Args:
            request (:class:`~.operations_pb2.GetOperationRequest`):
                The request object. Request message for
                `GetOperation` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        Returns:
            ~.operations_pb2.Operation:
                An ``Operation`` object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = operations_pb2.GetOperationRequest(**request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method.wrap_method(
            self._client._transport.get_operation,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "ConversationalSearchServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


__all__ = ("ConversationalSearchServiceAsyncClient",)
