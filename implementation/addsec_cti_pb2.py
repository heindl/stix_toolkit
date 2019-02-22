# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cti_protobuf/addsec_cti.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='cti_protobuf/addsec_cti.proto',
  package='',
  serialized_pb=_b('\n\x1d\x63ti_protobuf/addsec_cti.proto\"\xab\x05\n\x0fObservationData\x12\x13\n\x08\x64\x61taType\x18\x01 \x02(\r:\x01\x30\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x12\x0b\n\x03num\x18\x03 \x01(\r\"\xe7\x04\n\x08\x44\x61taType\x12\x13\n\x0f\x44\x61taTypeUnknown\x10\x00\x12\x13\n\x0f\x44\x61taTypeHashMD5\x10\x01\x12\x14\n\x10\x44\x61taTypeHashSHA1\x10\x02\x12\x16\n\x12\x44\x61taTypeHashSHA256\x10\x03\x12\x13\n\x0f\x44\x61taTypeHashAS1\x10\x04\x12\x13\n\x0f\x44\x61taTypeHashAS2\x10\x05\x12\x0f\n\x0b\x44\x61taTypeCVE\x10\x06\x12\x19\n\x15\x44\x61taTypeVersionString\x10\x07\x12\x17\n\x13\x44\x61taTypeModelString\x10\x08\x12\x18\n\x14\x44\x61taTypeASLibVersion\x10\t\x12\x10\n\x0c\x44\x61taTypeFile\x10\n\x12\x10\n\x0c\x44\x61taTypeX509\x10\x0b\x12\x17\n\x13\x44\x61taTypeX509Subject\x10\x0c\x12\x16\n\x12\x44\x61taTypeX509Issuer\x10\r\x12\x14\n\x10\x44\x61taTypeUsername\x10\x0e\x12\x13\n\x0f\x44\x61taTypeProcess\x10\x0f\x12\x13\n\x0f\x44\x61taTypeCommand\x10\x10\x12\x17\n\x13\x44\x61taTypeApplication\x10\x11\x12\x12\n\x0e\x44\x61taTypeString\x10\x12\x12\x12\n\x0e\x44\x61taTypeNumber\x10\x13\x12\x10\n\x0c\x44\x61taTypeIPv4\x10\x14\x12\x10\n\x0c\x44\x61taTypeIPv6\x10\x15\x12\x10\n\x0c\x44\x61taTypePort\x10\x16\x12\x14\n\x10\x44\x61taTypeHostname\x10\x17\x12\x0f\n\x0b\x44\x61taTypeMAC\x10\x18\x12\x1b\n\x17\x44\x61taTypeASConfTimestamp\x10\x19\x12\x18\n\x14\x44\x61taTypeASDefVersion\x10\x1a\x12\x10\n\x0c\x44\x61taTypeHPKP\x10\x1b\"\xd0\x06\n\x0bObservation\x12\x1a\n\x0fobservationType\x18\x01 \x02(\r:\x01\x30\x12\x11\n\ttimestamp\x18\x02 \x01(\r\x12\x11\n\ttimeDelta\x18\x08 \x01(\r\x12\x15\n\nconfidence\x18\x03 \x01(\r:\x01\x30\x12\x11\n\x06impact\x18\x04 \x01(\r:\x01\x30\x12\x1f\n\x05\x64\x61tas\x18\x05 \x03(\x0b\x32\x10.ObservationData\x12\x0e\n\x06testId\x18\x06 \x01(\r\x12\x11\n\ttestSubId\x18\x07 \x01(\r\"\xd0\x02\n\x0fObservationType\x12\x1a\n\x16ObservationTypeUnknown\x10\x00\x12 \n\x1cObservationTypeInformational\x10\x01\x12(\n$ObservationTypeSystemCharacteristics\x10\x02\x12-\n)ObservationTypeApplicationCharacteristics\x10\x03\x12#\n\x1fObservationTypeMalwareArtifacts\x10\x04\x12 \n\x1cObservationTypeNetworkAttack\x10\x05\x12\x1f\n\x1bObservationTypeUserBehavior\x10\x06\x12\x1d\n\x19ObservationTypeCompliance\x10\x07\x12\x1f\n\x1bObservationTypeCustomerData\x10\x08\"\x97\x01\n\x15ObservationConfidence\x12 \n\x1cObservationConfidenceUnknown\x10\x00\x12\x1c\n\x18ObservationConfidenceLow\x10\x01\x12\x1f\n\x1bObservationConfidenceMedium\x10\x02\x12\x1d\n\x19ObservationConfidenceHigh\x10\x03\"\xa3\x01\n\x11ObservationImpact\x12\x1c\n\x18ObservationImpactUnknown\x10\x00\x12\x19\n\x15ObservationImpactNone\x10\x01\x12\x1a\n\x16ObservationImpactMinor\x10\x02\x12\x1d\n\x19ObservationImpactModerate\x10\x03\x12\x1a\n\x16ObservationImpactMajor\x10\x04\"\x9c\x04\n\x06Report\x12\x16\n\x0eorganizationId\x18\x01 \x01(\x0c\x12\x10\n\x08systemId\x18\x02 \x01(\x0c\x12\x19\n\x11systemIdSecondary\x18\x03 \x01(\x0c\x12\x15\n\nsystemType\x18\x04 \x01(\r:\x01\x30\x12\x15\n\rapplicationId\x18\x05 \x01(\x0c\x12\x0e\n\x06userId\x18\x06 \x01(\x0c\x12\x17\n\x0fuserIdSecondary\x18\x07 \x01(\x0c\x12\"\n\x0cobservations\x18\x08 \x03(\x0b\x32\x0c.Observation\x12\x10\n\x08timeBase\x18\t \x01(\r\"\xbf\x02\n\nSystemType\x12\x15\n\x11SystemTypeUnknown\x10\x00\x12\x11\n\rSystemTypeIOS\x10\x01\x12\x15\n\x11SystemTypeAndroid\x10\x02\x12\x1b\n\x17SystemTypeWindowsMobile\x10\x03\x12\x18\n\x14SystemTypeBlackberry\x10\x04\x12\x1a\n\x16SystemTypeAmazonMobile\x10\x05\x12\x11\n\rSystemTypeOSX\x10\x06\x12\x13\n\x0fSystemTypeLinux\x10\x07\x12\x15\n\x11SystemTypeWindows\x10\x08\x12\x11\n\rSystemTypeBSD\x10\t\x12\x1b\n\x17SystemTypeEmbeddedLinux\x10\n\x12\x11\n\rSystemTypeIOT\x10\x0b\x12\x1b\n\x17SystemTypeNetworkDevice\x10\x0c\x42\x1f\n\x18\x63om.additionsecurity.ctiH\x01\x88\x01\x00')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_OBSERVATIONDATA_DATATYPE = _descriptor.EnumDescriptor(
  name='DataType',
  full_name='ObservationData.DataType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DataTypeUnknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeHashMD5', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeHashSHA1', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeHashSHA256', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeHashAS1', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeHashAS2', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeCVE', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeVersionString', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeModelString', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeASLibVersion', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeFile', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeX509', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeX509Subject', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeX509Issuer', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeUsername', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeProcess', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeCommand', index=16, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeApplication', index=17, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeString', index=18, number=18,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeNumber', index=19, number=19,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeIPv4', index=20, number=20,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeIPv6', index=21, number=21,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypePort', index=22, number=22,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeHostname', index=23, number=23,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeMAC', index=24, number=24,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeASConfTimestamp', index=25, number=25,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeASDefVersion', index=26, number=26,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DataTypeHPKP', index=27, number=27,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=102,
  serialized_end=717,
)
_sym_db.RegisterEnumDescriptor(_OBSERVATIONDATA_DATATYPE)

_OBSERVATION_OBSERVATIONTYPE = _descriptor.EnumDescriptor(
  name='ObservationType',
  full_name='Observation.ObservationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ObservationTypeUnknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ObservationTypeInformational', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ObservationTypeSystemCharacteristics', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ObservationTypeApplicationCharacteristics', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ObservationTypeMalwareArtifacts', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ObservationTypeNetworkAttack', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ObservationTypeUserBehavior', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ObservationTypeCompliance', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ObservationTypeCustomerData', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=912,
  serialized_end=1248,
)
_sym_db.RegisterEnumDescriptor(_OBSERVATION_OBSERVATIONTYPE)

_OBSERVATION_OBSERVATIONCONFIDENCE = _descriptor.EnumDescriptor(
  name='ObservationConfidence',
  full_name='Observation.ObservationConfidence',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ObservationConfidenceUnknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ObservationConfidenceLow', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ObservationConfidenceMedium', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ObservationConfidenceHigh', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1251,
  serialized_end=1402,
)
_sym_db.RegisterEnumDescriptor(_OBSERVATION_OBSERVATIONCONFIDENCE)

_OBSERVATION_OBSERVATIONIMPACT = _descriptor.EnumDescriptor(
  name='ObservationImpact',
  full_name='Observation.ObservationImpact',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ObservationImpactUnknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ObservationImpactNone', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ObservationImpactMinor', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ObservationImpactModerate', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ObservationImpactMajor', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1405,
  serialized_end=1568,
)
_sym_db.RegisterEnumDescriptor(_OBSERVATION_OBSERVATIONIMPACT)

_REPORT_SYSTEMTYPE = _descriptor.EnumDescriptor(
  name='SystemType',
  full_name='Report.SystemType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SystemTypeUnknown', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SystemTypeIOS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SystemTypeAndroid', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SystemTypeWindowsMobile', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SystemTypeBlackberry', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SystemTypeAmazonMobile', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SystemTypeOSX', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SystemTypeLinux', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SystemTypeWindows', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SystemTypeBSD', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SystemTypeEmbeddedLinux', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SystemTypeIOT', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SystemTypeNetworkDevice', index=12, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1792,
  serialized_end=2111,
)
_sym_db.RegisterEnumDescriptor(_REPORT_SYSTEMTYPE)


_OBSERVATIONDATA = _descriptor.Descriptor(
  name='ObservationData',
  full_name='ObservationData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataType', full_name='ObservationData.dataType', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='ObservationData.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num', full_name='ObservationData.num', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OBSERVATIONDATA_DATATYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=717,
)


_OBSERVATION = _descriptor.Descriptor(
  name='Observation',
  full_name='Observation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='observationType', full_name='Observation.observationType', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Observation.timestamp', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeDelta', full_name='Observation.timeDelta', index=2,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='Observation.confidence', index=3,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='impact', full_name='Observation.impact', index=4,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datas', full_name='Observation.datas', index=5,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='testId', full_name='Observation.testId', index=6,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='testSubId', full_name='Observation.testSubId', index=7,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _OBSERVATION_OBSERVATIONTYPE,
    _OBSERVATION_OBSERVATIONCONFIDENCE,
    _OBSERVATION_OBSERVATIONIMPACT,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=720,
  serialized_end=1568,
)


_REPORT = _descriptor.Descriptor(
  name='Report',
  full_name='Report',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='organizationId', full_name='Report.organizationId', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='systemId', full_name='Report.systemId', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='systemIdSecondary', full_name='Report.systemIdSecondary', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='systemType', full_name='Report.systemType', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applicationId', full_name='Report.applicationId', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='userId', full_name='Report.userId', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='userIdSecondary', full_name='Report.userIdSecondary', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='observations', full_name='Report.observations', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timeBase', full_name='Report.timeBase', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REPORT_SYSTEMTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1571,
  serialized_end=2111,
)

_OBSERVATIONDATA_DATATYPE.containing_type = _OBSERVATIONDATA
_OBSERVATION.fields_by_name['datas'].message_type = _OBSERVATIONDATA
_OBSERVATION_OBSERVATIONTYPE.containing_type = _OBSERVATION
_OBSERVATION_OBSERVATIONCONFIDENCE.containing_type = _OBSERVATION
_OBSERVATION_OBSERVATIONIMPACT.containing_type = _OBSERVATION
_REPORT.fields_by_name['observations'].message_type = _OBSERVATION
_REPORT_SYSTEMTYPE.containing_type = _REPORT
DESCRIPTOR.message_types_by_name['ObservationData'] = _OBSERVATIONDATA
DESCRIPTOR.message_types_by_name['Observation'] = _OBSERVATION
DESCRIPTOR.message_types_by_name['Report'] = _REPORT

ObservationData = _reflection.GeneratedProtocolMessageType('ObservationData', (_message.Message,), dict(
  DESCRIPTOR = _OBSERVATIONDATA,
  __module__ = 'cti_protobuf.addsec_cti_pb2'
  # @@protoc_insertion_point(class_scope:ObservationData)
  ))
_sym_db.RegisterMessage(ObservationData)

Observation = _reflection.GeneratedProtocolMessageType('Observation', (_message.Message,), dict(
  DESCRIPTOR = _OBSERVATION,
  __module__ = 'cti_protobuf.addsec_cti_pb2'
  # @@protoc_insertion_point(class_scope:Observation)
  ))
_sym_db.RegisterMessage(Observation)

Report = _reflection.GeneratedProtocolMessageType('Report', (_message.Message,), dict(
  DESCRIPTOR = _REPORT,
  __module__ = 'cti_protobuf.addsec_cti_pb2'
  # @@protoc_insertion_point(class_scope:Report)
  ))
_sym_db.RegisterMessage(Report)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030com.additionsecurity.ctiH\001\210\001\000'))
# @@protoc_insertion_point(module_scope)
