# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'shenlong/kongdi', False),
	Exit('north', 'shenlong/xiaowu', False),
]
caodi=Room('shenlong/caodi', u'�ݵ�', 'shenlong', 0, exits)

exits = [
	Exit('east', 'shenlong/kongdi', False),
]
caoping=Room('shenlong/caoping', u'��ƺ', 'shenlong', 0, exits)

exits = [
	Exit('west', 'shenlong/zoulang', False),
]
chufang=Room('shenlong/chufang', u'����', None, 0, exits)

exits = [
]
dahai=Room('shenlong/dahai', u'��', None, 0, exits)

exits = [
	Exit('south', 'shenlong/road2', False),
	Exit('north', 'shenlong/dating', False),
]
damen=Room('shenlong/damen', u'����', 'shenlong', 0, exits)

exits = [
	Exit('west', 'shenlong/zhulin', False),
	Exit('south', 'shenlong/damen', False),
	Exit('east', 'shenlong/zoulang', False),
	Exit('north', 'shenlong/houting', False),
]
dating=Room('shenlong/dating', u'�����̴���', None, 0, exits)

exits = [
	Exit('north', 'shenlong/lin1', False),
]
haitan=Room('shenlong/haitan', u'��̲', 'shenlong', 0, exits)

exits = [
	Exit('south', 'shenlong/dating', False),
]
houting=Room('shenlong/houting', u'�����̺���', 'shenlong', 0, exits)

exits = [
	Exit('east', 'shenlong/zhulin', False),
]
jushi=Room('shenlong/jushi', u'����', None, 0, exits)

exits = [
	Exit('west', 'shenlong/caoping', False),
	Exit('south', 'shenlong/lin2', False),
	Exit('north', 'shenlong/caodi', False),
	Exit('east', 'shenlong/road', False),
]
kongdi=Room('shenlong/kongdi', u'�յ�', 'shenlong', 0, exits)

exits = [
	Exit('south', 'shenlong/haitan', False),
]
lin1=Room('shenlong/lin1', u'��ľ��', 'shenlong', 0, exits)

exits = [
	Exit('south', 'shenlong/lin1', False),
	Exit('north', 'shenlong/kongdi', False),
]
lin2=Room('shenlong/lin2', u'��ľ��', 'shenlong', 0, exits)

exits = [
	Exit('west', 'shenlong/kongdi', False),
	Exit('north', 'shenlong/road2', False),
]
road=Room('shenlong/road', u'���', 'shenlong', 0, exits)

exits = [
	Exit('south', 'shenlong/road', False),
	Exit('north', 'shenlong/damen', False),
]
road2=Room('shenlong/road2', u'ɽ��', None, 0, exits)

exits = [
	Exit('south', 'shenlong/wuchang2', False),
	Exit('east', 'shenlong/wuchang3', False),
	Exit('north', 'shenlong/zoulang', False),
]
wuchang=Room('shenlong/wuchang', u'���䳡', None, 0, exits)

exits = [
	Exit('north', 'shenlong/wuchang', False),
]
wuchang2=Room('shenlong/wuchang2', u'���䳡', None, 0, exits)

exits = [
	Exit('west', 'shenlong/wuchang', False),
]
wuchang3=Room('shenlong/wuchang3', u'���䳡', None, 0, exits)

exits = [
	Exit('south', 'shenlong/caodi', False),
]
xiaowu=Room('shenlong/xiaowu', u'С��', 'shenlong', 0, exits)

exits = [
	Exit('south', 'shenlong/zoulang', False),
]
xiuxishi=Room('shenlong/xiuxishi', u'��Ϣ��', None, 0, exits)

exits = [
	Exit('west', 'shenlong/jushi', False),
	Exit('east', 'shenlong/dating', False),
]
zhulin=Room('shenlong/zhulin', u'����', 'shenlong', 0, exits)

exits = [
	Exit('west', 'shenlong/dating', False),
	Exit('south', 'shenlong/wuchang', False),
	Exit('north', 'shenlong/xiuxishi', False),
	Exit('east', 'shenlong/chufang', False),
]
zoulang=Room('shenlong/zoulang', u'����', 'shenlong', 0, exits)

