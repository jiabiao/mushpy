# coding=gbk
from _objects import Room,Exit

exits = [
]
block=Room('death/block', u'空房间', None, 0, exits)

exits = [
	Exit('north', 'death/gateway', False),
]
gate=Room('death/gate', u'鬼门关', None, 0, exits)

exits = [
	Exit('south', 'death/gate', False),
	Exit('north', 'death/road1', False),
]
gateway=Room('death/gateway', u'酆都城门', None, 0, exits)

exits = [
	Exit('up', 'death/god2', False),
	Exit('down', 'city/wumiao', False),
]
god1=Room('death/god1', u'天堂', None, 0, exits)

exits = [
]
god2=Room('death/god2', u'圣殿', None, 0, exits)

exits = [
	Exit('east', 'death/road1', False),
]
inn1=Room('death/inn1', u'小店', None, 0, exits)

exits = [
	Exit('west', 'death/road1', False),
]
inn2=Room('death/inn2', u'黑店', None, 0, exits)

exits = [
	Exit('west', 'death/inn1', False),
	Exit('south', 'death/gateway', False),
	Exit('east', 'death/inn2', False),
	Exit('north', 'death/road2', False),
]
road1=Room('death/road1', u'鬼门大道', None, 0, exits)

exits = [
	Exit('south', 'death/road1', False),
	Exit('north', 'death/road3', False),
]
road2=Room('death/road2', u'鬼门大道', None, 0, exits)

exits = [
	Exit('south', 'death/road2', False),
]
road3=Room('death/road3', u'路的尽头', None, 0, exits)

