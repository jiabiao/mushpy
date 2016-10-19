# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('caihong', 'room/caihong/xiaoyuan', False),
	Exit('west', 'shaolin/yidao2', False),
	Exit('panlong', 'room/panlong/dayuan', False),
	Exit('dule', 'room/dule/xiaoyuan', False),
]
xiaoyuan=Room('room/xiaoyuan', u'СԺ', 'city', 0, exits)

