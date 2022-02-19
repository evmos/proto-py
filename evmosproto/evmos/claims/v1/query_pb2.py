# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: evmos/claims/v1/query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from evmosproto.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from evmosproto.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from evmosproto.cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from evmosproto.cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from evmosproto.evmos.claims.v1 import claims_pb2 as evmos_dot_claims_dot_v1_dot_claims__pb2
from evmosproto.evmos.claims.v1 import genesis_pb2 as evmos_dot_claims_dot_v1_dot_genesis__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='evmos/claims/v1/query.proto',
  package='evmos.claims.v1',
  syntax='proto3',
  serialized_options=b'Z\'github.com/tharsis/evmos/x/claims/types',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1b\x65vmos/claims/v1/query.proto\x12\x0f\x65vmos.claims.v1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1c\x65vmos/claims/v1/claims.proto\x1a\x1d\x65vmos/claims/v1/genesis.proto\"\x1c\n\x1aQueryTotalUnclaimedRequest\"y\n\x1bQueryTotalUnclaimedResponse\x12Z\n\x05\x63oins\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"\x14\n\x12QueryParamsRequest\"D\n\x13QueryParamsResponse\x12-\n\x06params\x18\x01 \x01(\x0b\x32\x17.evmos.claims.v1.ParamsB\x04\xc8\xde\x1f\x00\"W\n\x19QueryClaimsRecordsRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x95\x01\n\x1aQueryClaimsRecordsResponse\x12:\n\x06\x63laims\x18\x01 \x03(\x0b\x32$.evmos.claims.v1.ClaimsRecordAddressB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"+\n\x18QueryClaimsRecordRequest\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"\x9b\x01\n\x19QueryClaimsRecordResponse\x12P\n\x18initial_claimable_amount\x18\x01 \x01(\tB.\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xc8\xde\x1f\x00\x12,\n\x06\x63laims\x18\x02 \x03(\x0b\x32\x16.evmos.claims.v1.ClaimB\x04\xc8\xde\x1f\x00\x32\xc4\x04\n\x05Query\x12\x95\x01\n\x0eTotalUnclaimed\x12+.evmos.claims.v1.QueryTotalUnclaimedRequest\x1a,.evmos.claims.v1.QueryTotalUnclaimedResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /evmos/claims/v1/total_unclaimed\x12t\n\x06Params\x12#.evmos.claims.v1.QueryParamsRequest\x1a$.evmos.claims.v1.QueryParamsResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/evmos/claims/v1/params\x12\x91\x01\n\rClaimsRecords\x12*.evmos.claims.v1.QueryClaimsRecordsRequest\x1a+.evmos.claims.v1.QueryClaimsRecordsResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/evmos/claims/v1/claims_records\x12\x98\x01\n\x0c\x43laimsRecord\x12).evmos.claims.v1.QueryClaimsRecordRequest\x1a*.evmos.claims.v1.QueryClaimsRecordResponse\"1\x82\xd3\xe4\x93\x02+\x12)/evmos/claims/v1/claims_records/{address}B)Z\'github.com/tharsis/evmos/x/claims/typesb\x06proto3'
  ,
  dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2.DESCRIPTOR,cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,evmos_dot_claims_dot_v1_dot_claims__pb2.DESCRIPTOR,evmos_dot_claims_dot_v1_dot_genesis__pb2.DESCRIPTOR,])




_QUERYTOTALUNCLAIMEDREQUEST = _descriptor.Descriptor(
  name='QueryTotalUnclaimedRequest',
  full_name='evmos.claims.v1.QueryTotalUnclaimedRequest',
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
  serialized_start=237,
  serialized_end=265,
)


_QUERYTOTALUNCLAIMEDRESPONSE = _descriptor.Descriptor(
  name='QueryTotalUnclaimedResponse',
  full_name='evmos.claims.v1.QueryTotalUnclaimedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='coins', full_name='evmos.claims.v1.QueryTotalUnclaimedResponse.coins', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=267,
  serialized_end=388,
)


_QUERYPARAMSREQUEST = _descriptor.Descriptor(
  name='QueryParamsRequest',
  full_name='evmos.claims.v1.QueryParamsRequest',
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
  serialized_start=390,
  serialized_end=410,
)


_QUERYPARAMSRESPONSE = _descriptor.Descriptor(
  name='QueryParamsResponse',
  full_name='evmos.claims.v1.QueryParamsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='evmos.claims.v1.QueryParamsResponse.params', index=0,
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
  serialized_start=412,
  serialized_end=480,
)


_QUERYCLAIMSRECORDSREQUEST = _descriptor.Descriptor(
  name='QueryClaimsRecordsRequest',
  full_name='evmos.claims.v1.QueryClaimsRecordsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pagination', full_name='evmos.claims.v1.QueryClaimsRecordsRequest.pagination', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=482,
  serialized_end=569,
)


_QUERYCLAIMSRECORDSRESPONSE = _descriptor.Descriptor(
  name='QueryClaimsRecordsResponse',
  full_name='evmos.claims.v1.QueryClaimsRecordsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='claims', full_name='evmos.claims.v1.QueryClaimsRecordsResponse.claims', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagination', full_name='evmos.claims.v1.QueryClaimsRecordsResponse.pagination', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=572,
  serialized_end=721,
)


_QUERYCLAIMSRECORDREQUEST = _descriptor.Descriptor(
  name='QueryClaimsRecordRequest',
  full_name='evmos.claims.v1.QueryClaimsRecordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='evmos.claims.v1.QueryClaimsRecordRequest.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=723,
  serialized_end=766,
)


_QUERYCLAIMSRECORDRESPONSE = _descriptor.Descriptor(
  name='QueryClaimsRecordResponse',
  full_name='evmos.claims.v1.QueryClaimsRecordResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='initial_claimable_amount', full_name='evmos.claims.v1.QueryClaimsRecordResponse.initial_claimable_amount', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\332\336\037&github.com/cosmos/cosmos-sdk/types.Int\310\336\037\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='claims', full_name='evmos.claims.v1.QueryClaimsRecordResponse.claims', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=769,
  serialized_end=924,
)

_QUERYTOTALUNCLAIMEDRESPONSE.fields_by_name['coins'].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
_QUERYPARAMSRESPONSE.fields_by_name['params'].message_type = evmos_dot_claims_dot_v1_dot_genesis__pb2._PARAMS
_QUERYCLAIMSRECORDSREQUEST.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGEREQUEST
_QUERYCLAIMSRECORDSRESPONSE.fields_by_name['claims'].message_type = evmos_dot_claims_dot_v1_dot_claims__pb2._CLAIMSRECORDADDRESS
_QUERYCLAIMSRECORDSRESPONSE.fields_by_name['pagination'].message_type = cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2._PAGERESPONSE
_QUERYCLAIMSRECORDRESPONSE.fields_by_name['claims'].message_type = evmos_dot_claims_dot_v1_dot_claims__pb2._CLAIM
DESCRIPTOR.message_types_by_name['QueryTotalUnclaimedRequest'] = _QUERYTOTALUNCLAIMEDREQUEST
DESCRIPTOR.message_types_by_name['QueryTotalUnclaimedResponse'] = _QUERYTOTALUNCLAIMEDRESPONSE
DESCRIPTOR.message_types_by_name['QueryParamsRequest'] = _QUERYPARAMSREQUEST
DESCRIPTOR.message_types_by_name['QueryParamsResponse'] = _QUERYPARAMSRESPONSE
DESCRIPTOR.message_types_by_name['QueryClaimsRecordsRequest'] = _QUERYCLAIMSRECORDSREQUEST
DESCRIPTOR.message_types_by_name['QueryClaimsRecordsResponse'] = _QUERYCLAIMSRECORDSRESPONSE
DESCRIPTOR.message_types_by_name['QueryClaimsRecordRequest'] = _QUERYCLAIMSRECORDREQUEST
DESCRIPTOR.message_types_by_name['QueryClaimsRecordResponse'] = _QUERYCLAIMSRECORDRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QueryTotalUnclaimedRequest = _reflection.GeneratedProtocolMessageType('QueryTotalUnclaimedRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYTOTALUNCLAIMEDREQUEST,
  '__module__' : 'evmos.claims.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.claims.v1.QueryTotalUnclaimedRequest)
  })
_sym_db.RegisterMessage(QueryTotalUnclaimedRequest)

QueryTotalUnclaimedResponse = _reflection.GeneratedProtocolMessageType('QueryTotalUnclaimedResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYTOTALUNCLAIMEDRESPONSE,
  '__module__' : 'evmos.claims.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.claims.v1.QueryTotalUnclaimedResponse)
  })
_sym_db.RegisterMessage(QueryTotalUnclaimedResponse)

QueryParamsRequest = _reflection.GeneratedProtocolMessageType('QueryParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSREQUEST,
  '__module__' : 'evmos.claims.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.claims.v1.QueryParamsRequest)
  })
_sym_db.RegisterMessage(QueryParamsRequest)

QueryParamsResponse = _reflection.GeneratedProtocolMessageType('QueryParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPARAMSRESPONSE,
  '__module__' : 'evmos.claims.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.claims.v1.QueryParamsResponse)
  })
_sym_db.RegisterMessage(QueryParamsResponse)

QueryClaimsRecordsRequest = _reflection.GeneratedProtocolMessageType('QueryClaimsRecordsRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCLAIMSRECORDSREQUEST,
  '__module__' : 'evmos.claims.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.claims.v1.QueryClaimsRecordsRequest)
  })
_sym_db.RegisterMessage(QueryClaimsRecordsRequest)

QueryClaimsRecordsResponse = _reflection.GeneratedProtocolMessageType('QueryClaimsRecordsResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCLAIMSRECORDSRESPONSE,
  '__module__' : 'evmos.claims.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.claims.v1.QueryClaimsRecordsResponse)
  })
_sym_db.RegisterMessage(QueryClaimsRecordsResponse)

QueryClaimsRecordRequest = _reflection.GeneratedProtocolMessageType('QueryClaimsRecordRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCLAIMSRECORDREQUEST,
  '__module__' : 'evmos.claims.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.claims.v1.QueryClaimsRecordRequest)
  })
_sym_db.RegisterMessage(QueryClaimsRecordRequest)

QueryClaimsRecordResponse = _reflection.GeneratedProtocolMessageType('QueryClaimsRecordResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYCLAIMSRECORDRESPONSE,
  '__module__' : 'evmos.claims.v1.query_pb2'
  # @@protoc_insertion_point(class_scope:evmos.claims.v1.QueryClaimsRecordResponse)
  })
_sym_db.RegisterMessage(QueryClaimsRecordResponse)


DESCRIPTOR._options = None
_QUERYTOTALUNCLAIMEDRESPONSE.fields_by_name['coins']._options = None
_QUERYPARAMSRESPONSE.fields_by_name['params']._options = None
_QUERYCLAIMSRECORDSRESPONSE.fields_by_name['claims']._options = None
_QUERYCLAIMSRECORDRESPONSE.fields_by_name['initial_claimable_amount']._options = None
_QUERYCLAIMSRECORDRESPONSE.fields_by_name['claims']._options = None

_QUERY = _descriptor.ServiceDescriptor(
  name='Query',
  full_name='evmos.claims.v1.Query',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=927,
  serialized_end=1507,
  methods=[
  _descriptor.MethodDescriptor(
    name='TotalUnclaimed',
    full_name='evmos.claims.v1.Query.TotalUnclaimed',
    index=0,
    containing_service=None,
    input_type=_QUERYTOTALUNCLAIMEDREQUEST,
    output_type=_QUERYTOTALUNCLAIMEDRESPONSE,
    serialized_options=b'\202\323\344\223\002\"\022 /evmos/claims/v1/total_unclaimed',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Params',
    full_name='evmos.claims.v1.Query.Params',
    index=1,
    containing_service=None,
    input_type=_QUERYPARAMSREQUEST,
    output_type=_QUERYPARAMSRESPONSE,
    serialized_options=b'\202\323\344\223\002\031\022\027/evmos/claims/v1/params',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ClaimsRecords',
    full_name='evmos.claims.v1.Query.ClaimsRecords',
    index=2,
    containing_service=None,
    input_type=_QUERYCLAIMSRECORDSREQUEST,
    output_type=_QUERYCLAIMSRECORDSRESPONSE,
    serialized_options=b'\202\323\344\223\002!\022\037/evmos/claims/v1/claims_records',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ClaimsRecord',
    full_name='evmos.claims.v1.Query.ClaimsRecord',
    index=3,
    containing_service=None,
    input_type=_QUERYCLAIMSRECORDREQUEST,
    output_type=_QUERYCLAIMSRECORDRESPONSE,
    serialized_options=b'\202\323\344\223\002+\022)/evmos/claims/v1/claims_records/{address}',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_QUERY)

DESCRIPTOR.services_by_name['Query'] = _QUERY

# @@protoc_insertion_point(module_scope)