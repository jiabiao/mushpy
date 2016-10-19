# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('northwest', 'village/alley2', False),
	Exit('east', 'village/sroad3', False),
]
alley1=Room('village/alley1', u'С��', 'village', 0, exits)

exits = [
	Exit('southeast', 'village/alley1', False),
]
alley2=Room('village/alley2', u'С�ﾡͷ', 'village', 0, exits)

exits = [
	Exit('west', 'village/sroad4', False),
	Exit('east', 'village/bighouse2', False),
]
bighouse1=Room('village/bighouse1', u'ǰ��', None, 0, exits)

exits = [
	Exit('west', 'village/bighouse1', False),
]
bighouse2=Room('village/bighouse2', u'����', None, 0, exits)

exits = [
	Exit('west', 'village/eroad1', False),
	Exit('east', 'huashan/path1', False),
]
eexit=Room('village/eexit', u'�����', 'village', 0, exits)

exits = [
	Exit('north', 'village/eroad1', False),
]
ehouse1=Room('village/ehouse1', u'����', None, 0, exits)

exits = [
	Exit('south', 'village/eroad2', False),
]
ehouse2=Room('village/ehouse2', u'��լ', None, 0, exits)

exits = [
	Exit('west', 'village/eroad2', False),
	Exit('south', 'village/ehouse1', False),
	Exit('east', 'village/eexit', False),
]
eroad1=Room('village/eroad1', u'��ʯ·', 'village', 0, exits)

exits = [
	Exit('west', 'village/eroad3', False),
	Exit('north', 'village/ehouse2', False),
	Exit('east', 'village/eroad1', False),
]
eroad2=Room('village/eroad2', u'��ʯ·', 'village', 0, exits)

exits = [
	Exit('west', 'village/square', False),
	Exit('south', 'village/smithy1', False),
	Exit('east', 'village/eroad2', False),
	Exit('north', 'village/shop', False),
]
eroad3=Room('village/eroad3', u'��ʯ·', 'village', 0, exits)

exits = [
	Exit('south', 'changan/road2', False),
	Exit('north', 'village/hsroad2', False),
]
hsroad1=Room('village/hsroad1', u'��ʯ���', 'village', 0, exits)

exits = [
	Exit('northwest', 'village/hsroad3', False),
	Exit('south', 'village/hsroad1', False),
	Exit('northeast', 'huashan/jzroad1', False),
]
hsroad2=Room('village/hsroad2', u'��ʯ���', 'village', 0, exits)

exits = [
	Exit('southeast', 'village/hsroad2', False),
	Exit('north', 'village/sexit', False),
]
hsroad3=Room('village/hsroad3', u'����·', 'village', 0, exits)

exits = [
	Exit('northeast', 'village/nwroad2', False),
]
nwhouse=Room('village/nwhouse', u'��', None, 0, exits)

exits = [
	Exit('southeast', 'village/nwroad2', False),
	Exit('west', 'village/wexit', False),
	Exit('northeast', 'village/temple1', False),
]
nwroad1=Room('village/nwroad1', u'��ʯ·', 'village', 0, exits)

exits = [
	Exit('southeast', 'village/square', False),
	Exit('northwest', 'village/nwroad1', False),
	Exit('southwest', 'village/nwhouse', False),
]
nwroad2=Room('village/nwroad2', u'��ʯ·', 'village', 0, exits)

exits = [
	Exit('south', 'village/hsroad3', False),
	Exit('north', 'village/sroad1', False),
]
sexit=Room('village/sexit', u'�ϴ��', 'village', 0, exits)

exits = [
	Exit('south', 'village/wexit', False),
]
shack=Room('village/shack', u'��լ', None, 0, exits)

exits = [
	Exit('south', 'village/eroad3', False),
]
shop=Room('village/shop', u'�ӻ���', None, 0, exits)

exits = [
	Exit('west', 'village/sroad2', False),
]
shouse=Room('village/shouse', u'С����', None, 0, exits)

exits = [
	Exit('north', 'village/eroad3', False),
	Exit('east', 'village/smithy2', False),
]
smithy1=Room('village/smithy1', u'������', None, 0, exits)

exits = [
	Exit('west', 'village/smithy1', False),
]
smithy2=Room('village/smithy2', u'С����', None, 0, exits)

exits = [
	Exit('northwest', 'village/nwroad2', False),
	Exit('south', 'village/sroad4', False),
	Exit('east', 'village/eroad3', False),
]
square=Room('village/square', u'��ȳ�', 'village', 0, exits)

exits = [
	Exit('south', 'village/sexit', False),
	Exit('north', 'village/sroad2', False),
]
sroad1=Room('village/sroad1', u'��ʯ·', 'village', 0, exits)

exits = [
	Exit('south', 'village/sroad1', False),
	Exit('east', 'village/shouse', False),
	Exit('north', 'village/sroad3', False),
]
sroad2=Room('village/sroad2', u'��ʯ·', 'village', 0, exits)

exits = [
	Exit('west', 'village/alley1', False),
	Exit('south', 'village/sroad2', False),
	Exit('north', 'village/sroad4', False),
]
sroad3=Room('village/sroad3', u'��ʯ·', 'village', 0, exits)

exits = [
	Exit('south', 'village/sroad3', False),
	Exit('east', 'village/bighouse1', False),
	Exit('north', 'village/square', False),
]
sroad4=Room('village/sroad4', u'��ʯ·', 'village', 0, exits)

exits = [
	Exit('southwest', 'village/nwroad1', False),
]
temple1=Room('village/temple1', u'��̳��', None, 0, exits)

exits = [
	Exit('west', 'village/temple1', False),
]
temple2=Room('village/temple2', u'С����', None, 0, exits)

exits = [
	Exit('northwest', 'heimuya/road6', False),
	Exit('north', 'village/shack', False),
	Exit('east', 'village/nwroad1', False),
]
wexit=Room('village/wexit', u'�����', 'village', 0, exits)

