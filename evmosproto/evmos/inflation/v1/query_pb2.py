# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: evmos/inflation/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from evmosproto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from evmosproto.evmos.inflation.v1 import genesis_pb2 as evmos_dot_inflation_dot_v1_dot_genesis__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='evmos/inflation/v1/query.proto',
  package='evmos.inflation.v1',
  syntax='proto3',
  serialized_options=b'Z*github.com/tharsis/evmos/x/inflation/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1e\x65vmos/inflation/v1/query.proto\x12\x12\x65vmos.inflation.v1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a evmos/inflation/v1/genesis.proto\"\x14\n\x12QueryPeriodRequest\"%\n\x13QueryPeriodResponse\x12\x0e\n\x06period\x18\x01 \x01(\x04\" \n\x1eQueryEpochMintProvisionRequest\"o\n\x1fQueryEpochMintProvisionResponse\x12L\n\x14\x65poch_mint_provision\x18\x01 \x01(\x0c\x42.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xc8\xde\x1f\x00\"\x14\n\x12QueryParamsRequest\"G\n\x13QueryParamsResponse\x12\x30\n\x06params\x18\x01 \x01(\x0b\x32\x1a.evmos.inflation.v1.ParamsB\x04\xc8\xde\x1f\x00\x32\xb7\x03\n\x05Query\x12}\n\x06Period\x12&.evmos.inflation.v1.QueryPeriodRequest\x1a\'.evmos.inflation.v1.QueryPeriodResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/evmos/inflation/v1/period\x12\xaf\x01\n\x12\x45pochMintProvision\x12\x32.evmos.inflation.v1.QueryEpochMintProvisionRequest\x1a\x33.evmos.inflation.v1.QueryEpochMintProvisionResponse\"0\x82\xd3\xe4\x93\x02*\x12(/evmos/inflation/v1/epoch_mint_provision\x12}\n\x06Params\x12&.evmos.inflation.v1.QueryParamsRequest\x1a\'.evmos.inflation.v1.QueryParamsResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/evmos/inflation/v1/paramsB,Z*github.com/tharsis/evmos/x/inflation/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,evmos_dot_inflation_dot_v1_dot_genesis__pb2.DESCRIPTOR,])




_QUERYPERIODREQUEST = _descriptor.Descriptor(
  name='QueryPeriodRequest',
  full_name='evmos.inflation.v1.QueryPeriodRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=140,
  serialized_end=160,
)


_QUERYPERIODRESPONSE = _descriptor.Descriptor(
  name='QueryPeriodResponse',
  full_name='evmos.inflation.v1.QueryPeriodResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='period', full_name='evmos.inflation.v1.QueryPeriodResponse.period', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=162,
  serialized_end=199,
)


_QUERYEPOCHMINTPROVISIONREQUEST = _descriptor.Descriptor(
  name='QueryEpochMintProvisionRequest',
  full_name='evmos.inflation.v1.QueryEpochMintProvisionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=201,
  serialized_end=233,
)


_QUERYEPOCHMINTPROVISIONRESPONSE = _descriptor.Descriptor(
  name='QueryEpochMintProvisionResponse',
  full_name='evmos.inflation.v1.QueryEpochMintProvisionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='epoch_mint_provision', full_name='evmos.inflation.v1.QueryEpochMintProvisionResponse.epoch_mint_provision', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Dec\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=235,
  serialized_end=346,
)


_QUERYPARAMSREQUEST = _descriptor.Descriptor(
  name='QueryParamsRequest',
  full_name='evmos.inflation.v1.QueryParamsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=348,
  serialized_end=368,
)


_QUERYPARAMSRESPONSE = _descriptor.Descriptor(
  name='QueryParamsResponse',
  full_name='evmos.inflation.v1.QueryParamsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='evmos.inflation.v1.QueryParamsResponse.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=370,
  serialized_end=441,
)

_QUERYPARAMSRESPONSE.fields_by_name['params'].message_type = evmos_dot_inflation_dot_v1_dot_genesis__pb2._PARAMS
DESCRIPTOR.message_types_by_name['QueryPeriodRequest'] = _QUERYPERIODREQUEST
DESCRIPTOR.message_types_by_name['QueryPeriodResponse'] = _QUERYPERIODRESPONSE
DESCRIPTOR.message_types_by_name['QueryEpochMintProvisionRequest'] = _QUERYEPOCHMINTPROVISIONREQUEST
DESCRIPTOR.message_types_by_name['QueryEpochMintProvisionResponse'] = _QUERYEPOCHMINTPROVISIONRESPONSE
DESCRIPTOR.message_types_by_name['QueryParamsRequest'] = _QUERYPARAMSREQUEST
DESCRIPTOR.message_types_by_name['QueryParamsResponse'] = _QUERYPARAMSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryPeriodRequest = _reflection.GeneratedProtocolMessageType('QueryPeriodRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPERIODREQUEST,
  '__module__' : 'evmos.inflation.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.inflation.v1.QueryPeriodRequest)
  })
_sym_db.RegisterMessage(QueryPeriodRequest)

QueryPeriodResponse = _reflection.GeneratedProtocolMessageType('QueryPeriodResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPERIODRESPONSE,
  '__module__' : 'evmos.inflation.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.inflation.v1.QueryPeriodResponse)
  })
_sym_db.RegisterMessage(QueryPeriodResponse)

QueryEpochMintProvisionRequest = _reflection.GeneratedProtocolMessageType('QueryEpochMintProvisionRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYEPOCHMINTPROVISIONREQUEST,
  '__module__' : 'evmos.inflation.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.inflation.v1.QueryEpochMintProvisionRequest)
  })
_sym_db.RegisterMessage(QueryEpochMintProvisionRequest)

QueryEpochMintProvisionResponse = _reflection.GeneratedProtocolMessageType('QueryEpochMintProvisionResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYEPOCHMINTPROVISIONRESPONSE,
  '__module__' : 'evmos.inflation.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.inflation.v1.QueryEpochMintProvisionResponse)
  })
_sym_db.RegisterMessage(QueryEpochMintProvisionResponse)

QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSREQUEST,
  '__module__' : 'evmos.inflation.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.inflation.v1.QueryParamsRequest)
  })
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSRESPONSE,
  '__module__' : 'evmos.inflation.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.inflation.v1.QueryParamsResponse)
  })
_sym_db.RegisterMessage(QueryParamsResponse)


DESCRIPTOR._options = None
_QUERYEPOCHMINTPROVISIONRESPONSE.fields_by_name['epoch_mint_provision']._options = None
_QUERYPARAMSRESPONSE.fields_by_name['params']._options = None

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='evmos.inflation.v1.Query',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=444,
  serialized_end=883,
  methods=[
  _descriptor.MethodDescriptor(
    name='Period',
    full_name='evmos.inflation.v1.Query.Period',
    index=0,
    containing_service=None,
    input_type=_QUERYPERIODREQUEST,
    output_type=_QUERYPERIODRESPONSE,
    serialized_options=b'\202\323\344\223\002\034\022\032/evmos/inflation/v1/period',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EpochMintProvision',
    full_name='evmos.inflation.v1.Query.EpochMintProvision',
    index=1,
    containing_service=None,
    input_type=_QUERYEPOCHMINTPROVISIONREQUEST,
    output_type=_QUERYEPOCHMINTPROVISIONRESPONSE,
    serialized_options=b'\202\323\344\223\002*\022(/evmos/inflation/v1/epoch_mint_provision',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Params',
    full_name='evmos.inflation.v1.Query.Params',
    index=2,
    containing_service=None,
    input_type=_QUERYPARAMSREQUEST,
    output_type=_QUERYPARAMSRESPONSE,
    serialized_options=b'\202\323\344\223\002\034\022\032/evmos/inflation/v1/params',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)