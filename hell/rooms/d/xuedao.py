# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('west', 'xuedao/shandong2', False),
]
eyabi=Room('xuedao/eyabi', u'���±�', 'xuedao', 0, exits)

exits = [
	Exit('up', 'xuedao/sroad3', False),
]
hollow=Room('xuedao/hollow', u'ѩ��', None, 0, exits)

exits = [
	Exit('southup', 'xuedao/sroad3', False),
	Exit('northdown', 'xuedao/nroad5', False),
	Exit('westup', 'xuedao/nroad2', False),
]
nroad1=Room('xuedao/nroad1', u'ɽ·', 'xuedao', 0, exits)

exits = [
	Exit('eastdown', 'xuedao/nroad1', False),
	Exit('westup', 'xuedao/nroad3', False),
]
nroad2=Room('xuedao/nroad2', u'ɽ·', 'xuedao', 0, exits)

exits = [
	Exit('eastdown', 'xuedao/nroad2', False),
	Exit('south', 'xuedao/nroad4', False),
]
nroad3=Room('xuedao/nroad3', u'��ѩɽ��´', 'xuedao', 0, exits)

exits = [
	Exit('north', 'xuedao/nroad3', False),
	Exit('westup', 'xueshan/shanmen', False),
]
nroad4=Room('xuedao/nroad4', u'��ѩɽɽ·', 'xuedao', 0, exits)

exits = [
	Exit('southup', 'xuedao/nroad1', False),
	Exit('northdown', 'xuedao/nroad6', False),
]
nroad5=Room('xuedao/nroad5', u'ɽ·', 'xuedao', 0, exits)

exits = [
	Exit('southup', 'xuedao/nroad5', False),
	Exit('north', 'xuedao/nroad7', False),
]
nroad6=Room('xuedao/nroad6', u'ɽ·', 'xuedao', 0, exits)

exits = [
	Exit('south', 'xuedao/nroad6', False),
	Exit('eastdown', 'xueshan/shanjiao', False),
]
nroad7=Room('xuedao/nroad7', u'ɽ·', 'xuedao', 0, exits)

exits = [
	Exit('south', 'xuedao/shandong2', False),
]
nyabi=Room('xuedao/nyabi', u'���±�', 'xuedao', 0, exits)

exits = [
	Exit('out', 'xuedao/sroad8', False),
]
shandong1=Room('xuedao/shandong1', u'ɽ��', None, 0, exits)

exits = [
	Exit('west', 'xuedao/sroad9', False),
	Exit('south', 'xuedao/syabi', False),
	Exit('east', 'xuedao/eyabi', False),
	Exit('north', 'xuedao/nyabi', False),
	Exit('enter', 'xuedao/shandong3', False),
]
shandong2=Room('xuedao/shandong2', u'����', 'xuedao', 0, exits)

exits = [
	Exit('out', 'xuedao/shandong2', False),
	Exit('east', 'xuedao/xiuxishi', False),
]
shandong3=Room('xuedao/shandong3', u'ɽ��', None, 0, exits)

exits = [
	Exit('north', 'city3/nanheqiaos', False),
	Exit('westup', 'xuedao/sroad2', False),
]
sroad1=Room('xuedao/sroad1', u'ɽ·', 'xuedao', 0, exits)

exits = [
	Exit('eastdown', 'xuedao/sroad1', False),
	Exit('westup', 'xuedao/sroad3', False),
]
sroad2=Room('xuedao/sroad2', u'ɽ·', 'xuedao', 0, exits)

exits = [
	Exit('eastdown', 'xuedao/sroad2', False),
	Exit('northdown', 'xuedao/nroad1', False),
	Exit('westup', 'xuedao/sroad4', False),
]
sroad3=Room('xuedao/sroad3', u'ɽ·', 'xuedao', 0, exits)

exits = [
	Exit('eastdown', 'xuedao/sroad3', False),
	Exit('westup', 'xuedao/sroad5', False),
]
sroad4=Room('xuedao/sroad4', u'��ѩɽ��', 'xuedao', 0, exits)

exits = [
	Exit('southup', 'xuedao/sroad6', False),
	Exit('eastdown', 'xuedao/sroad4', False),
]
sroad5=Room('xuedao/sroad5', u'��ѩɽ', 'xuedao', 0, exits)

exits = [
	Exit('northdown', 'xuedao/sroad5', False),
	Exit('westup', 'xuedao/sroad7', False),
]
sroad6=Room('xuedao/sroad6', u'��ѩɽ��', 'xuedao', 0, exits)

exits = [
	Exit('southdown', 'xuedao/sroad8', False),
	Exit('eastdown', 'xuedao/sroad6', False),
]
sroad7=Room('xuedao/sroad7', u'��ѩɽ��', 'xuedao', 0, exits)

exits = [
	Exit('northup', 'xuedao/sroad7', False),
	Exit('north', 'xuedao/wangyougu', False),
	Exit('enter', 'xuedao/shandong1', False),
]
sroad8=Room('xuedao/sroad8', u'��ѩɽɽ��', 'xuedao', 0, exits)

exits = [
	Exit('east', 'xuedao/shandong2', False),
	Exit('northdown', 'xuedao/wangyougu', False),
]
sroad9=Room('xuedao/sroad9', u'��ѩɽɽ��', 'xuedao', 0, exits)

exits = [
	Exit('north', 'xuedao/shandong2', False),
]
syabi=Room('xuedao/syabi', u'���±�', 'xuedao', 0, exits)

exits = [
	Exit('southeast', 'xuedao/sroad9', False),
	Exit('southwest', 'xuedao/sroad8', False),
]
wangyougu=Room('xuedao/wangyougu', u'���ǹ�', 'xuedao', 0, exits)

exits = [
	Exit('west', 'xuedao/shandong3', False),
]
xiuxishi=Room('xuedao/xiuxishi', u'�ප', None, 0, exits)

