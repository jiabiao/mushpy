# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('west', 'suzhou/road5', False),
	Exit('eastup', 'item/road2', False),
]
road1=Room('item/road1', u'小径', 'suzhou', 0, exits)

exits = [
	Exit('eastdown', 'item/road3', False),
	Exit('westdown', 'item/road1', False),
]
road2=Room('item/road2', u'小径', 'suzhou', 0, exits)

exits = [
	Exit('northeast', 'item/road4', False),
	Exit('westup', 'item/road2', False),
]
road3=Room('item/road3', u'小径', 'suzhou', 0, exits)

exits = [
	Exit('southwest', 'item/road3', False),
	Exit('east', 'item/road5', False),
]
road4=Room('item/road4', u'小径', 'suzhou', 0, exits)

exits = [
	Exit('west', 'item/road4', False),
	Exit('enter', 'item/xiaowu', False),
]
road5=Room('item/road5', u'小径', 'suzhou', 0, exits)

exits = [
	Exit('out', 'item/road5', False),
]
xiaowu=Room('item/xiaowu', u'铸剑室', None, 0, exits)

