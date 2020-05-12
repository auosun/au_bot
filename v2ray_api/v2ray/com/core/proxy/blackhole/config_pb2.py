# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2ray.com/core/proxy/blackhole/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v2ray.com.core.common.serial import typed_message_pb2 as v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v2ray.com/core/proxy/blackhole/config.proto',
  package='v2ray.core.proxy.blackhole',
  syntax='proto3',
  serialized_options=_b('\n\036com.v2ray.core.proxy.blackholeP\001Z\tblackhole\252\002\032V2Ray.Core.Proxy.Blackhole'),
  serialized_pb=_b('\n+v2ray.com/core/proxy/blackhole/config.proto\x12\x1av2ray.core.proxy.blackhole\x1a\x30v2ray.com/core/common/serial/typed_message.proto\"\x0e\n\x0cNoneResponse\"\x0e\n\x0cHTTPResponse\"B\n\x06\x43onfig\x12\x38\n\x08response\x18\x01 \x01(\x0b\x32&.v2ray.core.common.serial.TypedMessageBJ\n\x1e\x63om.v2ray.core.proxy.blackholeP\x01Z\tblackhole\xaa\x02\x1aV2Ray.Core.Proxy.Blackholeb\x06proto3')
  ,
  dependencies=[v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2.DESCRIPTOR,])




_NONERESPONSE = _descriptor.Descriptor(
  name='NoneResponse',
  full_name='v2ray.core.proxy.blackhole.NoneResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=125,
  serialized_end=139,
)


_HTTPRESPONSE = _descriptor.Descriptor(
  name='HTTPResponse',
  full_name='v2ray.core.proxy.blackhole.HTTPResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
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
  serialized_start=141,
  serialized_end=155,
)


_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='v2ray.core.proxy.blackhole.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='v2ray.core.proxy.blackhole.Config.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=157,
  serialized_end=223,
)

_CONFIG.fields_by_name['response'].message_type = v2ray_dot_com_dot_core_dot_common_dot_serial_dot_typed__message__pb2._TYPEDMESSAGE
DESCRIPTOR.message_types_by_name['NoneResponse'] = _NONERESPONSE
DESCRIPTOR.message_types_by_name['HTTPResponse'] = _HTTPRESPONSE
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NoneResponse = _reflection.GeneratedProtocolMessageType('NoneResponse', (_message.Message,), dict(
  DESCRIPTOR = _NONERESPONSE,
  __module__ = 'v2ray.com.core.proxy.blackhole.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.blackhole.NoneResponse)
  ))
_sym_db.RegisterMessage(NoneResponse)

HTTPResponse = _reflection.GeneratedProtocolMessageType('HTTPResponse', (_message.Message,), dict(
  DESCRIPTOR = _HTTPRESPONSE,
  __module__ = 'v2ray.com.core.proxy.blackhole.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.blackhole.HTTPResponse)
  ))
_sym_db.RegisterMessage(HTTPResponse)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'v2ray.com.core.proxy.blackhole.config_pb2'
  # @@protoc_insertion_point(class_scope:v2ray.core.proxy.blackhole.Config)
  ))
_sym_db.RegisterMessage(Config)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
