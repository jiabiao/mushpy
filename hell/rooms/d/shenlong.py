# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'shenlong/kongdi', False),
	Exit('north', 'shenlong/xiaowu', False),
]
caodi=Room('shenlong/caodi', u'草地', 'shenlong', 0, exits)

exits = [
	Exit('east', 'shenlong/kongdi', False),
]
caoping=Room('shenlong/caoping', u'草坪', 'shenlong', 0, exits)

exits = [
	Exit('west', 'shenlong/zoulang', False),
]
chufang=Room('shenlong/chufang', u'厨房', None, 0, exits)

exits = [
]
dahai=Room('shenlong/dahai', u'大海', None, 0, exits)

exits = [
	Exit('south', 'shenlong/road2', False),
	Exit('north', 'shenlong/dating', False),
]
damen=Room('shenlong/damen', u'大门', 'shenlong', 0, exits)

exits = [
	Exit('west', 'shenlong/zhulin', False),
	Exit('south', 'shenlong/damen', False),
	Exit('east', 'shenlong/zoulang', False),
	Exit('north', 'shenlong/houting', False),
]
dating=Room('shenlong/dating', u'神龙教大厅', None, 0, exits)

exits = [
	Exit('north', 'shenlong/lin1', False),
]
haitan=Room('shenlong/haitan', u'海滩', 'shenlong', 0, exits)

exits = [
	Exit('south', 'shenlong/dating', False),
]
houting=Room('shenlong/houting', u'神龙教后厅', 'shenlong', 0, exits)

exits = [
	Exit('east', 'shenlong/zhulin', False),
]
jushi=Room('shenlong/jushi', u'竹屋', None, 0, exits)

exits = [
	Exit('west', 'shenlong/caoping', False),
	Exit('south', 'shenlong/lin2', False),
	Exit('north', 'shenlong/caodi', False),
	Exit('east', 'shenlong/road', False),
]
kongdi=Room('shenlong/kongdi', u'空地', 'shenlong', 0, exits)

exits = [
	Exit('south', 'shenlong/haitan', False),
]
lin1=Room('shenlong/lin1', u'灌木林', 'shenlong', 0, exits)

exits = [
	Exit('south', 'shenlong/lin1', False),
	Exit('north', 'shenlong/kongdi', False),
]
lin2=Room('shenlong/lin2', u'灌木林', 'shenlong', 0, exits)

exits = [
	Exit('west', 'shenlong/kongdi', False),
	Exit('north', 'shenlong/road2', False),
]
road=Room('shenlong/road', u'大道', 'shenlong', 0, exits)

exits = [
	Exit('south', 'shenlong/road', False),
	Exit('north', 'shenlong/damen', False),
]
road2=Room('shenlong/road2', u'山道', None, 0, exits)

exits = [
	Exit('south', 'shenlong/wuchang2', False),
	Exit('east', 'shenlong/wuchang3', False),
	Exit('north', 'shenlong/zoulang', False),
]
wuchang=Room('shenlong/wuchang', u'练武场', None, 0, exits)

exits = [
	Exit('north', 'shenlong/wuchang', False),
]
wuchang2=Room('shenlong/wuchang2', u'练武场', None, 0, exits)

exits = [
	Exit('west', 'shenlong/wuchang', False),
]
wuchang3=Room('shenlong/wuchang3', u'练武场', None, 0, exits)

exits = [
	Exit('south', 'shenlong/caodi', False),
]
xiaowu=Room('shenlong/xiaowu', u'小屋', 'shenlong', 0, exits)

exits = [
	Exit('south', 'shenlong/zoulang', False),
]
xiuxishi=Room('shenlong/xiuxishi', u'休息室', None, 0, exits)

exits = [
	Exit('west', 'shenlong/jushi', False),
	Exit('east', 'shenlong/dating', False),
]
zhulin=Room('shenlong/zhulin', u'竹林', 'shenlong', 0, exits)

exits = [
	Exit('west', 'shenlong/dating', False),
	Exit('south', 'shenlong/wuchang', False),
	Exit('north', 'shenlong/xiuxishi', False),
	Exit('east', 'shenlong/chufang', False),
]
zoulang=Room('shenlong/zoulang', u'走廊', 'shenlong', 0, exits)

