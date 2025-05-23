# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: authorization.proto
# Protobuf Python Version: 6.30.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    0,
    '',
    'authorization.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x61uthorization.proto\x12\rauthorization\"\x1a\n\x07SendSUB\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"\x1a\n\tSendToken\x12\r\n\x05token\x18\x01 \x01(\t\"/\n\x0cReturnTokens\x12\x0e\n\x06\x61\x63\x63\x65ss\x18\x01 \x01(\t\x12\x0f\n\x07refresh\x18\x02 \x01(\t\"\x1e\n\x0cReturnAccess\x12\x0e\n\x06\x61\x63\x63\x65ss\x18\x01 \x01(\t\" \n\rReturnRefresh\x12\x0f\n\x07refresh\x18\x01 \x01(\t\"\x1f\n\x0cReturnUserId\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"$\n\x11ReturnLogoutState\x12\x0f\n\x07message\x18\x01 \x01(\t2\xeb\x02\n\rAuthorization\x12\x42\n\tGetTokens\x12\x16.authorization.SendSUB\x1a\x1b.authorization.ReturnTokens\"\x00\x12\x44\n\tGetAccess\x12\x18.authorization.SendToken\x1a\x1b.authorization.ReturnAccess\"\x00\x12\x44\n\nGetRefresh\x12\x16.authorization.SendSUB\x1a\x1c.authorization.ReturnRefresh\"\x00\x12\x44\n\tGetUserId\x12\x18.authorization.SendToken\x1a\x1b.authorization.ReturnUserId\"\x00\x12\x44\n\x06LogOut\x12\x16.authorization.SendSUB\x1a .authorization.ReturnLogoutState\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'authorization_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SENDSUB']._serialized_start=38
  _globals['_SENDSUB']._serialized_end=64
  _globals['_SENDTOKEN']._serialized_start=66
  _globals['_SENDTOKEN']._serialized_end=92
  _globals['_RETURNTOKENS']._serialized_start=94
  _globals['_RETURNTOKENS']._serialized_end=141
  _globals['_RETURNACCESS']._serialized_start=143
  _globals['_RETURNACCESS']._serialized_end=173
  _globals['_RETURNREFRESH']._serialized_start=175
  _globals['_RETURNREFRESH']._serialized_end=207
  _globals['_RETURNUSERID']._serialized_start=209
  _globals['_RETURNUSERID']._serialized_end=240
  _globals['_RETURNLOGOUTSTATE']._serialized_start=242
  _globals['_RETURNLOGOUTSTATE']._serialized_end=278
  _globals['_AUTHORIZATION']._serialized_start=281
  _globals['_AUTHORIZATION']._serialized_end=644
# @@protoc_insertion_point(module_scope)
