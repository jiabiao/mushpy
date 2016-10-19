# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('east', 'motianya/mtxiaowu', False),
	Exit('down', 'motianya/mtyadi', False),
]
mtdating=Room('motianya/mtdating', u'崖顶', 'motianya', 0, exits)

exits = [
	Exit('south', 'motianya/mtyadi', False),
	Exit('east', 'motianya/mtroad1', False),
]
mtroad=Room('motianya/mtroad', u'山路', 'motianya', 0, exits)

exits = [
	Exit('west', 'motianya/mtroad', False),
	Exit('south', 'motianya/mtroad2', False),
	Exit('north', 'motianya/mtroad1', False),
	Exit('east', 'henshan/hsroad5', False),
]
mtroad1=Room('motianya/mtroad1', u'树林', 'motianya', 0, exits)

exits = [
	Exit('west', 'motianya/mtroad2', False),
	Exit('south', 'motianya/mtroad2', False),
	Exit('north', 'motianya/mtroad3', False),
	Exit('east', 'motianya/mtroad1', False),
]
mtroad2=Room('motianya/mtroad2', u'树林', 'motianya', 0, exits)

exits = [
	Exit('west', 'motianya/mtroad3', False),
	Exit('south', 'motianya/mtroad4', False),
	Exit('north', 'motianya/mtroad3', False),
	Exit('east', 'motianya/mtroad2', False),
]
mtroad3=Room('motianya/mtroad3', u'树林', 'motianya', 0, exits)

exits = [
	Exit('west', 'motianya/mtroad5', False),
	Exit('south', 'motianya/mtroad4', False),
	Exit('north', 'motianya/mtroad6', False),
	Exit('east', 'motianya/mtroad3', False),
]
mtroad4=Room('motianya/mtroad4', u'树林', 'motianya', 0, exits)

exits = [
	Exit('west', 'motianya/mtroad5', False),
	Exit('south', 'motianya/mtroad5', False),
	Exit('north', 'motianya/mtroad5', False),
	Exit('east', 'motianya/mtroad4', False),
]
mtroad5=Room('motianya/mtroad5', u'树林', 'motianya', 0, exits)

exits = [
	Exit('west', 'motianya/mtroad4', False),
	Exit('south', 'motianya/mtroad4', False),
	Exit('north', 'motianya/mtroad4', False),
	Exit('east', 'motianya/mtroad4', False),
]
mtroad6=Room('motianya/mtroad6', u'树林', 'motianya', 0, exits)

exits = [
	Exit('west', 'motianya/mtdating', False),
]
mtxiaowu=Room('motianya/mtxiaowu', u'木屋', None, 0, exits)

exits = [
	Exit('north', 'motianya/mtroad', False),
]
mtyadi=Room('motianya/mtyadi', u'崖底', 'motianya', 0, exits)

