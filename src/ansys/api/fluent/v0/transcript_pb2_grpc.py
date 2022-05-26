# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ansys.api.fluent.v0.transcript_pb2 as transcript__pb2


class TranscriptStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.BeginStreaming = channel.unary_stream(
                '/grpcRemoting.Transcript/BeginStreaming',
                request_serializer=transcript__pb2.TranscriptRequest.SerializeToString,
                response_deserializer=transcript__pb2.TranscriptResponse.FromString,
                )


class TranscriptServicer(object):
    """Missing associated documentation comment in .proto file."""

    def BeginStreaming(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TranscriptServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'BeginStreaming': grpc.unary_stream_rpc_method_handler(
                    servicer.BeginStreaming,
                    request_deserializer=transcript__pb2.TranscriptRequest.FromString,
                    response_serializer=transcript__pb2.TranscriptResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpcRemoting.Transcript', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Transcript(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def BeginStreaming(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/grpcRemoting.Transcript/BeginStreaming',
            transcript__pb2.TranscriptRequest.SerializeToString,
            transcript__pb2.TranscriptResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
