# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('up', 'huashan/ziqitai', False),
]
shanbi=Room('jinshe/shanbi', u'ɽ��', 'jinshe', 0, exits)

exits = [
	Exit('south', 'jinshe/yongdao2', False),
]
shandong=Room('jinshe/shandong', u'ɽ��', 'jinshe', 0, exits)

exits = [
	Exit('out', 'jinshe/shanbi', False),
	Exit('east', 'jinshe/yongdao2', False),
]
yongdao1=Room('jinshe/yongdao1', u'��', None, 0, exits)

exits = [
	Exit('west', 'jinshe/yongdao1', False),
	Exit('north', 'jinshe/shandong', False),
]
yongdao2=Room('jinshe/yongdao2', u'��', None, 0, exits)

