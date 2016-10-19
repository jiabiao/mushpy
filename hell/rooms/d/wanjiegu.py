# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'wanjiegu/hall', False),
]
backyard=Room('wanjiegu/backyard', u'��Ժ', 'wanjiegu', 0, exits)

exits = [
	Exit('south', 'wanjiegu/left_room', False),
]
bed_room=Room('wanjiegu/bed_room', u'����', None, 0, exits)

exits = [
	Exit('west', 'wanjiegu/port2', False),
	Exit('east', 'wanjiegu/port', False),
]
bridge=Room('wanjiegu/bridge', u'������', 'wanjiegu', 0, exits)

exits = [
	Exit('south', 'wanjiegu/right_room', False),
]
drug_room=Room('wanjiegu/drug_room', u'ҩ��', None, 0, exits)

exits = [
	Exit('east', 'wanjiegu/shan_road4', False),
]
entrance=Room('wanjiegu/entrance', u'��ɭ��', 'wanjiegu', 0, exits)

exits = [
	Exit('enter', 'wanjiegu/tunnel2', False),
]
grassland=Room('wanjiegu/grassland', u'�ݵ�', 'wanjiegu', 0, exits)

exits = [
	Exit('west', 'wanjiegu/left_room', False),
	Exit('south', 'wanjiegu/xiaoting', False),
	Exit('east', 'wanjiegu/right_room', False),
	Exit('north', 'wanjiegu/backyard', False),
]
hall=Room('wanjiegu/hall', u'����', None, 0, exits)

exits = [
	Exit('east', 'wanjiegu/hall', False),
	Exit('north', 'wanjiegu/bed_room', False),
]
left_room=Room('wanjiegu/left_room', u'���᷿', None, 0, exits)

exits = [
	Exit('west', 'wanjiegu/bridge', False),
	Exit('east', 'wanjiegu/riverside3', False),
]
port=Room('wanjiegu/port', u'���˶�', 'wanjiegu', 0, exits)

exits = [
	Exit('east', 'wanjiegu/bridge', False),
	Exit('westup', 'wanjiegu/slide3', False),
]
port2=Room('wanjiegu/port2', u'���׽���', 'wanjiegu', 0, exits)

exits = [
	Exit('west', 'wanjiegu/hall', False),
	Exit('north', 'wanjiegu/drug_room', False),
]
right_room=Room('wanjiegu/right_room', u'���᷿', None, 0, exits)

exits = [
	Exit('northup', 'wanjiegu/riverside2', False),
]
riverside1=Room('wanjiegu/riverside1', u'����С·', 'wanjiegu', 0, exits)

exits = [
	Exit('southdown', 'wanjiegu/riverside1', False),
	Exit('southeast', 'dali/road3', False),
	Exit('northdown', 'wanjiegu/riverside3', False),
]
riverside2=Room('wanjiegu/riverside2', u'����С·', 'wanjiegu', 0, exits)

exits = [
	Exit('west', 'wanjiegu/port', False),
	Exit('southup', 'wanjiegu/riverside2', False),
	Exit('north', 'wanjiegu/riverside4', False),
]
riverside3=Room('wanjiegu/riverside3', u'����С·', 'wanjiegu', 0, exits)

exits = [
	Exit('northwest', 'wanjiegu/wlshan', False),
	Exit('south', 'wanjiegu/riverside3', False),
]
riverside4=Room('wanjiegu/riverside4', u'����С·', 'wanjiegu', 0, exits)

exits = [
	Exit('northdown', 'wanjiegu/slide3', False),
	Exit('westup', 'wanjiegu/shan_road2', False),
]
shan_road1=Room('wanjiegu/shan_road1', u'ɽ·', 'wanjiegu', 0, exits)

exits = [
	Exit('eastdown', 'wanjiegu/shan_road1', False),
	Exit('westdown', 'wanjiegu/shan_road3', False),
]
shan_road2=Room('wanjiegu/shan_road2', u'ɽ·', 'wanjiegu', 0, exits)

exits = [
	Exit('eastup', 'wanjiegu/shan_road2', False),
	Exit('northdown', 'wanjiegu/shan_road4', False),
]
shan_road3=Room('wanjiegu/shan_road3', u'ɽ·', 'wanjiegu', 0, exits)

exits = [
	Exit('west', 'wanjiegu/entrance', False),
	Exit('southup', 'wanjiegu/shan_road3', False),
]
shan_road4=Room('wanjiegu/shan_road4', u'ɽ·', 'wanjiegu', 0, exits)

exits = [
	Exit('southup', 'wanjiegu/shan_road1', False),
	Exit('eastdown', 'wanjiegu/port2', False),
]
slide3=Room('wanjiegu/slide3', u'ɽ��', 'wanjiegu', 0, exits)

exits = [
	Exit('south', 'wanjiegu/backyard', False),
]
stone_room=Room('wanjiegu/stone_room', u'ʯ��', None, 0, exits)

exits = [
	Exit('out', 'wanjiegu/entrance', False),
]
tree_hole=Room('wanjiegu/tree_hole', u'����', None, 0, exits)

exits = [
	Exit('out', 'wanjiegu/tree_hole', False),
	Exit('north', 'wanjiegu/tunnel2', False),
]
tunnel1=Room('wanjiegu/tunnel1', u'�ص�', None, 0, exits)

exits = [
	Exit('out', 'wanjiegu/grassland', False),
	Exit('south', 'wanjiegu/tunnel1', False),
]
tunnel2=Room('wanjiegu/tunnel2', u'�ص�', None, 0, exits)

exits = [
	Exit('northeast', 'wanjiegu/wlroad2', False),
]
wlhoushan=Room('wanjiegu/wlhoushan', u'��ɽ', 'wanjiegu', 0, exits)

exits = [
	Exit('southeast', 'wanjiegu/wlshan', False),
	Exit('west', 'wanjiegu/wlroad2', False),
]
wlroad1=Room('wanjiegu/wlroad1', u'С·', 'wanjiegu', 0, exits)

exits = [
	Exit('southwest', 'wanjiegu/wlhoushan', False),
	Exit('east', 'wanjiegu/wlroad1', False),
]
wlroad2=Room('wanjiegu/wlroad2', u'С·', 'wanjiegu', 0, exits)

exits = [
	Exit('southeast', 'wanjiegu/riverside4', False),
	Exit('northwest', 'wanjiegu/wlroad1', False),
]
wlshan=Room('wanjiegu/wlshan', u'����ɽ', 'wanjiegu', 0, exits)

exits = [
	Exit('south', 'wanjiegu/grassland', False),
	Exit('north', 'wanjiegu/hall', False),
]
xiaoting=Room('wanjiegu/xiaoting', u'С��', None, 0, exits)

