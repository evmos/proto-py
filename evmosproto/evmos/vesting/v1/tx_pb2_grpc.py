# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from evmosproto.evmos.vesting.v1 import tx_pb2 as evmos_dot_vesting_dot_v1_dot_tx__pb2


class MsgStub(object):
    """Msg defines the bank Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateClawbackVestingAccount = channel.unary_unary(
                '/evmos.vesting.v1.Msg/CreateClawbackVestingAccount',
                request_serializer=evmos_dot_vesting_dot_v1_dot_tx__pb2.MsgCreateClawbackVestingAccount.SerializeToString,
                response_deserializer=evmos_dot_vesting_dot_v1_dot_tx__pb2.MsgCreateClawbackVestingAccountResponse.FromString,
                )
        self.Clawback = channel.unary_unary(
                '/evmos.vesting.v1.Msg/Clawback',
                request_serializer=evmos_dot_vesting_dot_v1_dot_tx__pb2.MsgClawback.SerializeToString,
                response_deserializer=evmos_dot_vesting_dot_v1_dot_tx__pb2.MsgClawbackResponse.FromString,
                )


class MsgServicer(object):
    """Msg defines the bank Msg service.
    """

    def CreateClawbackVestingAccount(self, request, context):
        """CreateClawbackVestingAccount defines a method that enables creating a
        vesting account that is subject to clawback.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Clawback(self, request, context):
        """Clawback removes the unvested tokens from evmosproto.a ClawbackVestingAccount.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateClawbackVestingAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateClawbackVestingAccount,
                    request_deserializer=evmos_dot_vesting_dot_v1_dot_tx__pb2.MsgCreateClawbackVestingAccount.FromString,
                    response_serializer=evmos_dot_vesting_dot_v1_dot_tx__pb2.MsgCreateClawbackVestingAccountResponse.SerializeToString,
            ),
            'Clawback': grpc.unary_unary_rpc_method_handler(
                    servicer.Clawback,
                    request_deserializer=evmos_dot_vesting_dot_v1_dot_tx__pb2.MsgClawback.FromString,
                    response_serializer=evmos_dot_vesting_dot_v1_dot_tx__pb2.MsgClawbackResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'evmos.vesting.v1.Msg', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Msg(object):
    """Msg defines the bank Msg service.
    """

    @staticmethod
    def CreateClawbackVestingAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.vesting.v1.Msg/CreateClawbackVestingAccount',
            evmos_dot_vesting_dot_v1_dot_tx__pb2.MsgCreateClawbackVestingAccount.SerializeToString,
            evmos_dot_vesting_dot_v1_dot_tx__pb2.MsgCreateClawbackVestingAccountResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Clawback(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/evmos.vesting.v1.Msg/Clawback',
            evmos_dot_vesting_dot_v1_dot_tx__pb2.MsgClawback.SerializeToString,
            evmos_dot_vesting_dot_v1_dot_tx__pb2.MsgClawbackResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)