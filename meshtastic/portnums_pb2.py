# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: portnums.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='portnums.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0eportnums.proto*\x93\x01\n\x07PortNum\x12\x0f\n\x0bUNKNOWN_APP\x10\x00\x12\x14\n\x10TEXT_MESSAGE_APP\x10\x01\x12\x17\n\x13REMOTE_HARDWARE_APP\x10\x02\x12\x10\n\x0cPOSITION_APP\x10\x03\x12\x10\n\x0cNODEINFO_APP\x10\x04\x12\x10\n\x0bPRIVATE_APP\x10\x80\x02\x12\x12\n\rIP_TUNNEL_APP\x10\x80\x08\x62\x06proto3'
)

_PORTNUM = _descriptor.EnumDescriptor(
  name='PortNum',
  full_name='PortNum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_APP', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TEXT_MESSAGE_APP', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REMOTE_HARDWARE_APP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POSITION_APP', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NODEINFO_APP', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PRIVATE_APP', index=5, number=256,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IP_TUNNEL_APP', index=6, number=1024,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=19,
  serialized_end=166,
)
_sym_db.RegisterEnumDescriptor(_PORTNUM)

PortNum = enum_type_wrapper.EnumTypeWrapper(_PORTNUM)
UNKNOWN_APP = 0
TEXT_MESSAGE_APP = 1
REMOTE_HARDWARE_APP = 2
POSITION_APP = 3
NODEINFO_APP = 4
PRIVATE_APP = 256
IP_TUNNEL_APP = 1024


DESCRIPTOR.enum_types_by_name['PortNum'] = _PORTNUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
