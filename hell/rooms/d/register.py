# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('west', 'register/roomw', False),
	Exit('south', 'register/rooms', False),
	Exit('north', 'register/roomn', False),
	Exit('east', 'register/roome', False),
]
entry=Room('register/entry', u'������Դ', None, 0, exits)

exits = [
]
prison=Room('register/prison', u'��ʮ�˲����', None, 0, exits)

exits = [
	Exit('out', 'register/yanluodian', False),
	Exit('west', 'register/entry', False),
]
roome=Room('register/roome', u'��������', None, 0, exits)

exits = [
	Exit('out', 'register/yanluodian', False),
	Exit('south', 'register/entry', False),
]
roomn=Room('register/roomn', u'�ĺ�����', None, 0, exits)

exits = [
	Exit('out', 'register/yanluodian', False),
	Exit('north', 'register/entry', False),
]
rooms=Room('register/rooms', u'������', None, 0, exits)

exits = [
	Exit('out', 'register/yanluodian', False),
	Exit('east', 'register/entry', False),
]
roomw=Room('register/roomw', u'���ռ�թ', None, 0, exits)

exits = [
]
yanluodian=Room('register/yanluodian', u'���޵�', None, 0, exits)

