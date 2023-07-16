# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc_discord/main.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17grpc_discord/main.proto\x12\x0cgrpc_discord\"\x17\n\x04Ping\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x17\n\x04Pong\x12\x0f\n\x07message\x18\x01 \x01(\t\"#\n\x07\x43hannel\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\"J\n\x05Guild\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\x12\x13\n\x0bunavailable\x18\x04 \x01(\x08J\x04\x08\x05\x10\x06\"\x9d\x01\n\x04Role\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\"\n\x05guild\x18\x03 \x01(\x0b\x32\x13.grpc_discord.Guild\x12\r\n\x05\x63olor\x18\x04 \x01(\x05\x12\r\n\x05hoist\x18\x05 \x01(\x08\x12\x10\n\x08position\x18\x06 \x01(\x05\x12\x13\n\x0bmentionable\x18\x07 \x01(\x08\x12\x12\n\ncreated_at\x18\x08 \x01(\x03\"%\n\tAuthGroup\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\">\n\x13\x41uthGroupMembership\x12\'\n\x06groups\x18\x01 \x03(\x0b\x32\x17.grpc_discord.AuthGroup\"4\n\x0fRolesMembership\x12!\n\x05roles\x18\x01 \x03(\x0b\x32\x12.grpc_discord.Role\"\xce\x01\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x0b\n\x03\x62ot\x18\x03 \x01(\x08\x12\x15\n\rdiscriminator\x18\x04 \x01(\t\x12\x10\n\x08username\x18\x05 \x01(\t\x12\x11\n\tjoined_at\x18\x06 \x01(\x03\x12\x12\n\ncreated_at\x18\x07 \x01(\x03\x12$\n\x08top_role\x18\x08 \x01(\x0b\x32\x12.grpc_discord.Role\x12!\n\x05roles\x18\t \x03(\x0b\x32\x12.grpc_discord.Role\"`\n\x0eGetUserRequest\x12\x0c\n\x02id\x18\x01 \x01(\x03H\x00\x12\x16\n\x0c\x64isplay_name\x18\x02 \x01(\tH\x00\x12\x15\n\rinclude_roles\x18\x03 \x01(\x08\x42\x11\n\x0fsearch_criteria\"D\n\x0fGetUserResponse\x12 \n\x04user\x18\x01 \x01(\x0b\x32\x12.grpc_discord.User\x12\x0f\n\x07success\x18\x02 \x01(\x08\"7\n\x13\x44isableUserResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\"B\n\x0e\x42\x61nUserRequest\x12 \n\x04user\x18\x01 \x01(\x0b\x32\x12.grpc_discord.User\x12\x0e\n\x06reason\x18\x02 \x01(\t\"3\n\x0f\x42\x61nUserResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\"D\n\x10StripUserRequest\x12 \n\x04user\x18\x01 \x01(\x0b\x32\x12.grpc_discord.User\x12\x0e\n\x06reason\x18\x02 \x01(\t\"5\n\x11StripUserResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\"N\n\x18UpdateDisplayNameRequest\x12 \n\x04user\x18\x01 \x01(\x0b\x32\x12.grpc_discord.User\x12\x10\n\x08nickname\x18\x02 \x01(\t\"=\n\x19UpdateDisplayNameResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\"\xbc\x01\n\x16UpdateUserRolesRequest\x12 \n\x04user\x18\x01 \x01(\x0b\x32\x12.grpc_discord.User\x12\r\n\x05reset\x18\x02 \x01(\x08\x12\x33\n\x06groups\x18\x03 \x01(\x0b\x32!.grpc_discord.AuthGroupMembershipH\x00\x12.\n\x05roles\x18\x04 \x01(\x0b\x32\x1d.grpc_discord.RolesMembershipH\x00\x42\x0c\n\nmembership\";\n\x17UpdateUserRolesResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\"5\n\x0fKickUserRequest\x12\x0e\n\x06reason\x18\x01 \x01(\t\x12\x12\n\ndiscord_id\x18\x02 \x01(\x03\"4\n\x10KickUserResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\":\n\x13RegisterUserRequest\x12\x12\n\ndiscord_id\x18\x01 \x01(\x03\x12\x0f\n\x07\x61uth_id\x18\x02 \x01(\x05\"8\n\x14RegisterUserResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"H\n\x11UpdateUserRequest\x12\x12\n\ndiscord_id\x18\x01 \x01(\x03\x12\x0f\n\x07\x61uth_id\x18\x02 \x01(\x05\x12\x0e\n\x06\x61\x63tive\x18\x03 \x01(\x08\"6\n\x12UpdateUserResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"\'\n\x11InviteUserRequest\x12\x12\n\ndiscord_id\x18\x01 \x01(\x03\"6\n\x12InviteUserResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"}\n\x12SendMessageRequest\x12(\n\x07\x63hannel\x18\x01 \x01(\x0b\x32\x15.grpc_discord.ChannelH\x00\x12\"\n\x04user\x18\x02 \x01(\x0b\x32\x12.grpc_discord.UserH\x00\x12\x0f\n\x07message\x18\x03 \x01(\tB\x08\n\x06target\"7\n\x13SendMessageResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xad\x06\n\x07\x44iscord\x12/\n\x05\x43heck\x12\x12.grpc_discord.Ping\x1a\x12.grpc_discord.Pong\x12\x46\n\x07GetUser\x12\x1c.grpc_discord.GetUserRequest\x1a\x1d.grpc_discord.GetUserResponse\x12Q\n\x0eStripUserRoles\x12\x1e.grpc_discord.StripUserRequest\x1a\x1f.grpc_discord.StripUserResponse\x12\x62\n\x0fSetUserNickname\x12&.grpc_discord.UpdateDisplayNameRequest\x1a\'.grpc_discord.UpdateDisplayNameResponse\x12Z\n\x0bUpdateRoles\x12$.grpc_discord.UpdateUserRolesRequest\x1a%.grpc_discord.UpdateUserRolesResponse\x12I\n\x08KickUser\x12\x1d.grpc_discord.KickUserRequest\x1a\x1e.grpc_discord.KickUserResponse\x12U\n\x0cRegisterUser\x12!.grpc_discord.RegisterUserRequest\x1a\".grpc_discord.RegisterUserResponse\x12O\n\nUpdateUser\x12\x1f.grpc_discord.UpdateUserRequest\x1a .grpc_discord.UpdateUserResponse\x12O\n\nInviteUser\x12\x1f.grpc_discord.InviteUserRequest\x1a .grpc_discord.InviteUserResponse\x12R\n\x0bSendMessage\x12 .grpc_discord.SendMessageRequest\x1a!.grpc_discord.SendMessageResponseb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'grpc_discord.main_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PING._serialized_start=41
  _PING._serialized_end=64
  _PONG._serialized_start=66
  _PONG._serialized_end=89
  _CHANNEL._serialized_start=91
  _CHANNEL._serialized_end=126
  _GUILD._serialized_start=128
  _GUILD._serialized_end=202
  _ROLE._serialized_start=205
  _ROLE._serialized_end=362
  _AUTHGROUP._serialized_start=364
  _AUTHGROUP._serialized_end=401
  _AUTHGROUPMEMBERSHIP._serialized_start=403
  _AUTHGROUPMEMBERSHIP._serialized_end=465
  _ROLESMEMBERSHIP._serialized_start=467
  _ROLESMEMBERSHIP._serialized_end=519
  _USER._serialized_start=522
  _USER._serialized_end=728
  _GETUSERREQUEST._serialized_start=730
  _GETUSERREQUEST._serialized_end=826
  _GETUSERRESPONSE._serialized_start=828
  _GETUSERRESPONSE._serialized_end=896
  _DISABLEUSERRESPONSE._serialized_start=898
  _DISABLEUSERRESPONSE._serialized_end=953
  _BANUSERREQUEST._serialized_start=955
  _BANUSERREQUEST._serialized_end=1021
  _BANUSERRESPONSE._serialized_start=1023
  _BANUSERRESPONSE._serialized_end=1074
  _STRIPUSERREQUEST._serialized_start=1076
  _STRIPUSERREQUEST._serialized_end=1144
  _STRIPUSERRESPONSE._serialized_start=1146
  _STRIPUSERRESPONSE._serialized_end=1199
  _UPDATEDISPLAYNAMEREQUEST._serialized_start=1201
  _UPDATEDISPLAYNAMEREQUEST._serialized_end=1279
  _UPDATEDISPLAYNAMERESPONSE._serialized_start=1281
  _UPDATEDISPLAYNAMERESPONSE._serialized_end=1342
  _UPDATEUSERROLESREQUEST._serialized_start=1345
  _UPDATEUSERROLESREQUEST._serialized_end=1533
  _UPDATEUSERROLESRESPONSE._serialized_start=1535
  _UPDATEUSERROLESRESPONSE._serialized_end=1594
  _KICKUSERREQUEST._serialized_start=1596
  _KICKUSERREQUEST._serialized_end=1649
  _KICKUSERRESPONSE._serialized_start=1651
  _KICKUSERRESPONSE._serialized_end=1703
  _REGISTERUSERREQUEST._serialized_start=1705
  _REGISTERUSERREQUEST._serialized_end=1763
  _REGISTERUSERRESPONSE._serialized_start=1765
  _REGISTERUSERRESPONSE._serialized_end=1821
  _UPDATEUSERREQUEST._serialized_start=1823
  _UPDATEUSERREQUEST._serialized_end=1895
  _UPDATEUSERRESPONSE._serialized_start=1897
  _UPDATEUSERRESPONSE._serialized_end=1951
  _INVITEUSERREQUEST._serialized_start=1953
  _INVITEUSERREQUEST._serialized_end=1992
  _INVITEUSERRESPONSE._serialized_start=1994
  _INVITEUSERRESPONSE._serialized_end=2048
  _SENDMESSAGEREQUEST._serialized_start=2050
  _SENDMESSAGEREQUEST._serialized_end=2175
  _SENDMESSAGERESPONSE._serialized_start=2177
  _SENDMESSAGERESPONSE._serialized_end=2232
  _DISCORD._serialized_start=2235
  _DISCORD._serialized_end=3048
# @@protoc_insertion_point(module_scope)
