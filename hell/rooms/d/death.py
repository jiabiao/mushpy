# coding=gbk
from _objects import Room,Exit

exits = [
]
block=Room('death/block', u'�շ���', None, 0, exits)

exits = [
	Exit('north', 'death/gateway', False),
]
gate=Room('death/gate', u'���Ź�', None, 0, exits)

exits = [
	Exit('south', 'death/gate', False),
	Exit('north', 'death/road1', False),
]
gateway=Room('death/gateway', u'ۺ������', None, 0, exits)

exits = [
	Exit('up', 'death/god2', False),
	Exit('down', 'city/wumiao', False),
]
god1=Room('death/god1', u'����', None, 0, exits)

exits = [
]
god2=Room('death/god2', u'ʥ��', None, 0, exits)

exits = [
	Exit('east', 'death/road1', False),
]
inn1=Room('death/inn1', u'С��', None, 0, exits)

exits = [
	Exit('west', 'death/road1', False),
]
inn2=Room('death/inn2', u'�ڵ�', None, 0, exits)

exits = [
	Exit('west', 'death/inn1', False),
	Exit('south', 'death/gateway', False),
	Exit('east', 'death/inn2', False),
	Exit('north', 'death/road2', False),
]
road1=Room('death/road1', u'���Ŵ��', None, 0, exits)

exits = [
	Exit('south', 'death/road1', False),
	Exit('north', 'death/road3', False),
]
road2=Room('death/road2', u'���Ŵ��', None, 0, exits)

exits = [
	Exit('south', 'death/road2', False),
]
road3=Room('death/road3', u'·�ľ�ͷ', None, 0, exits)

