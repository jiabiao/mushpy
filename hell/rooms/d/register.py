# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('west', 'register/roomw', False),
	Exit('south', 'register/rooms', False),
	Exit('north', 'register/roomn', False),
	Exit('east', 'register/roome', False),
]
entry=Room('register/entry', u'世外桃源', None, 0, exits)

exits = [
]
prison=Room('register/prison', u'第十八层地狱', None, 0, exits)

exits = [
	Exit('out', 'register/yanluodian', False),
	Exit('west', 'register/entry', False),
]
roome=Room('register/roome', u'光明磊落', None, 0, exits)

exits = [
	Exit('out', 'register/yanluodian', False),
	Exit('south', 'register/entry', False),
]
roomn=Room('register/roomn', u'心狠手辣', None, 0, exits)

exits = [
	Exit('out', 'register/yanluodian', False),
	Exit('north', 'register/entry', False),
]
rooms=Room('register/rooms', u'狡黠多变', None, 0, exits)

exits = [
	Exit('out', 'register/yanluodian', False),
	Exit('east', 'register/entry', False),
]
roomw=Room('register/roomw', u'阴险奸诈', None, 0, exits)

exits = [
]
yanluodian=Room('register/yanluodian', u'阎罗殿', None, 0, exits)

