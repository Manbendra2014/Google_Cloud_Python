# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.parallelstore.v1beta",
    manifest={
        "Instance",
        "ListInstancesRequest",
        "ListInstancesResponse",
        "GetInstanceRequest",
        "CreateInstanceRequest",
        "UpdateInstanceRequest",
        "DeleteInstanceRequest",
        "OperationMetadata",
    },
)


class Instance(proto.Message):
    r"""A Parallelstore instance.

    Attributes:
        name (str):
            Identifier. The resource name of the instance, in the format
            ``projects/{project}/locations/{location}/instances/{instance_id}``
        description (str):
            Optional. The description of the instance.
            2048 characters or less.
        state (google.cloud.parallelstore_v1beta.types.Instance.State):
            Output only. The instance state.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the instance was
            created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the instance was
            updated.
        labels (MutableMapping[str, str]):
            Optional. Cloud Labels are a flexible and lightweight
            mechanism for organizing cloud resources into groups that
            reflect a customer's organizational needs and deployment
            strategies. Cloud Labels can be used to filter collections
            of resources. They can be used to control how resource
            metrics are aggregated. And they can be used as arguments to
            policy management rules (e.g. route, firewall, load
            balancing, etc.).

            -  Label keys must be between 1 and 63 characters long and
               must conform to the following regular expression:
               ``[a-z][a-z0-9_-]{0,62}``.
            -  Label values must be between 0 and 63 characters long and
               must conform to the regular expression
               ``[a-z0-9_-]{0,63}``.
            -  No more than 64 labels can be associated with a given
               resource.

            See https://goo.gl/xmQnxf for more information on and
            examples of labels.

            If you plan to use labels in your own code, please note that
            additional characters may be allowed in the future.
            Therefore, you are advised to use an internal label
            representation, such as JSON, which doesn't rely upon
            specific characters being disallowed. For example,
            representing labels as the string: name + "*" + value would
            prove problematic if we were to allow "*" in a future
            release.
        capacity_gib (int):
            Required. Immutable. Storage capacity of
            Parallelstore instance in Gibibytes (GiB).
        daos_version (str):
            Output only. The version of DAOS software
            running in the instance
        access_points (MutableSequence[str]):
            Output only. List of access_points. Contains a list of IPv4
            addresses used for client side configuration.
        network (str):
            Optional. Immutable. The name of the Google Compute Engine
            `VPC network <https://cloud.google.com/vpc/docs/vpc>`__ to
            which the instance is connected.
        reserved_ip_range (str):
            Optional. Immutable. Contains the id of
            allocated IP address range associated with the
            private service access connection for example,
            "test-default" associated with IP range
            10.0.0.0/29. If no range id is provided all
            ranges will be considered.
    """

    class State(proto.Enum):
        r"""Represents the different states of a Parallelstore instance.

        Values:
            STATE_UNSPECIFIED (0):
                Not set.
            CREATING (1):
                The instance is being created.
            ACTIVE (2):
                The instance is available for use.
            DELETING (3):
                The instance is being deleted.
            FAILED (4):
                The instance is not usable.
        """
        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        DELETING = 3
        FAILED = 4

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=6,
    )
    capacity_gib: int = proto.Field(
        proto.INT64,
        number=8,
    )
    daos_version: str = proto.Field(
        proto.STRING,
        number=9,
    )
    access_points: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    network: str = proto.Field(
        proto.STRING,
        number=11,
    )
    reserved_ip_range: str = proto.Field(
        proto.STRING,
        number=12,
    )


class ListInstancesRequest(proto.Message):
    r"""Message for requesting list of Instances

    Attributes:
        parent (str):
            Required. The project and location for which to retrieve
            instance information, in the format
            ``projects/{project_id}/locations/{location}``. For
            Parallelstore locations map to Google Cloud zones, for
            example **us-central1-a**. To retrieve instance information
            for all locations, use "-" for the ``{location}`` value.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListInstancesResponse(proto.Message):
    r"""Message for response to listing Instances

    Attributes:
        instances (MutableSequence[google.cloud.parallelstore_v1beta.types.Instance]):
            The list of Parallelstore Instances
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    instances: MutableSequence["Instance"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Instance",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetInstanceRequest(proto.Message):
    r"""Request to get an instance's details.

    Attributes:
        name (str):
            Required. The instance resource name, in the format
            ``projects/{project_id}/locations/{location}/instances/{instance_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateInstanceRequest(proto.Message):
    r"""Request for
    [CreateInstance][google.cloud.parallelstore.v1beta.Parallelstore.CreateInstance]

    Attributes:
        parent (str):
            Required. The instance's project and location, in the format
            ``projects/{project}/locations/{location}``. Locations map
            to Google Cloud zones, for example **us-west1-b**.
        instance_id (str):
            Required. The logical name of the Parallelstore instance in
            the user project with the following restrictions:

            -  Must contain only lowercase letters, numbers, and
               hyphens.
            -  Must start with a letter.
            -  Must be between 1-63 characters.
            -  Must end with a number or a letter.
            -  Must be unique within the customer project / location
        instance (google.cloud.parallelstore_v1beta.types.Instance):
            Required. The instance to create.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and t he request times out.
            If you make the request again with the same
            request ID, the server can check if original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instance: "Instance" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Instance",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateInstanceRequest(proto.Message):
    r"""Message for updating a Instance

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update .Field mask is used to
            specify the fields to be overwritten in the Instance
            resource by the update. At least one path must be supplied
            in this field. The fields specified in the update_mask are
            relative to the resource, not the full request.
        instance (google.cloud.parallelstore_v1beta.types.Instance):
            Required. The instance to update
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and t he request times out.
            If you make the request again with the same
            request ID, the server can check if original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    instance: "Instance" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Instance",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteInstanceRequest(proto.Message):
    r"""Message for deleting a Instance

    Attributes:
        name (str):
            Required. Name of the resource
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and t he request times out.
            If you make the request again with the same
            request ID, the server can check if original
            operation with the same request ID was received,
            and if so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have been
            cancelled successfully have [Operation.error][] value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
