# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('west', 'taohua/qianyuan', False),
]
bingqi=Room('taohua/bingqi', u'兵器室', None, 0, exits)

exits = [
	Exit('east', 'taohua/qianyuan', False),
]
chufang=Room('taohua/chufang', u'厨房', None, 0, exits)

exits = [
]
dahai=Room('taohua/dahai', u'大海', 'taohua', 0, exits)

exits = [
	Exit('south', 'taohua/qianyuan', False),
	Exit('east', 'taohua/road1', False),
	Exit('north', 'taohua/tingzi', False),
]
damen=Room('taohua/damen', u'桃花山庄正门', 'taohua', 0, exits)

exits = [
	Exit('west', 'taohua/dating', False),
	Exit('up', 'taohua/shufang', False),
]
daojufang=Room('taohua/daojufang', u'道具房', None, 0, exits)

exits = [
	Exit('west', 'taohua/wofang', False),
	Exit('south', 'taohua/houyuan', False),
	Exit('east', 'taohua/daojufang', False),
	Exit('north', 'taohua/qianyuan', False),
]
dating=Room('taohua/dating', u'桃花山庄正厅', None, 0, exits)

exits = [
	Exit('out', 'taohua/road5', False),
]
dong=Room('taohua/dong', u'山洞', None, 0, exits)

exits = [
	Exit('south', 'taohua/tao_in', False),
]
haitan=Room('taohua/haitan', u'海滩', 'taohua', 0, exits)

exits = [
	Exit('southeast', 'taohua/wuchang1', False),
	Exit('west', 'taohua/xiaowu', False),
	Exit('south', 'taohua/wuchang3', False),
	Exit('southwest', 'taohua/wuchang2', False),
	Exit('east', 'taohua/siguoshi', False),
	Exit('north', 'taohua/dating', False),
]
houyuan=Room('taohua/houyuan', u'后院', 'taohua', 0, exits)

exits = [
]
lantian=Room('taohua/lantian', u'蓝天', 'taohua', 0, exits)

exits = [
	Exit('up', 'taohua/mudi', False),
	Exit('down', 'taohua/mushi', False),
]
mudao=Room('taohua/mudao', u'墓道', None, 0, exits)

exits = [
	Exit('south', 'taohua/road3', False),
]
mudi=Room('taohua/mudi', u'墓地', 'taohua', 0, exits)

exits = [
	Exit('up', 'taohua/mudao', False),
]
mushi=Room('taohua/mushi', u'墓室', None, 0, exits)

exits = [
	Exit('west', 'taohua/chufang', False),
	Exit('south', 'taohua/dating', False),
	Exit('east', 'taohua/bingqi', False),
	Exit('north', 'taohua/damen', False),
]
qianyuan=Room('taohua/qianyuan', u'前院', 'taohua', 0, exits)

exits = [
	Exit('west', 'taohua/damen', False),
	Exit('east', 'taohua/road2', False),
]
road1=Room('taohua/road1', u'小路', 'taohua', 0, exits)

exits = [
	Exit('west', 'taohua/road1', False),
	Exit('south', 'taohua/road4', False),
	Exit('north', 'taohua/road3', False),
]
road2=Room('taohua/road2', u'小路', 'taohua', 0, exits)

exits = [
	Exit('south', 'taohua/road2', False),
	Exit('north', 'taohua/mudi', False),
]
road3=Room('taohua/road3', u'小路', 'taohua', 0, exits)

exits = [
	Exit('north', 'taohua/road2', False),
	Exit('east', 'taohua/road5', False),
]
road4=Room('taohua/road4', u'小路', 'taohua', 0, exits)

exits = [
	Exit('west', 'taohua/road4', False),
	Exit('enter', 'taohua/dong', False),
]
road5=Room('taohua/road5', u'洞口', 'taohua', 0, exits)

exits = [
	Exit('down', 'taohua/daojufang', False),
]
shufang=Room('taohua/shufang', u'书房', None, 0, exits)

exits = [
	Exit('west', 'taohua/houyuan', False),
]
siguoshi=Room('taohua/siguoshi', u'思过室', None, 0, exits)

exits = [
	Exit('west', 'taohua/tao0', False),
	Exit('south', 'taohua/tao0', False),
	Exit('north', 'taohua/tao0', False),
	Exit('east', 'taohua/tao0', False),
]
tao0=Room('taohua/tao0', u'桃花迷阵', 'taohua', 0, exits)

exits = [
	Exit('south', 'taohua/tao0', False),
	Exit('north', 'taohua/haitan', False),
]
tao_in=Room('taohua/tao_in', u'迷阵入口', 'taohua', 0, exits)

exits = [
	Exit('south', 'taohua/tingzi', False),
	Exit('north', 'taohua/tao0', False),
]
tao_out=Room('taohua/tao_out', u'桃林边', 'taohua', 0, exits)

exits = [
	Exit('south', 'taohua/damen', False),
	Exit('north', 'taohua/tao_out', False),
]
tingzi=Room('taohua/tingzi', u'试剑亭', 'taohua', 0, exits)

exits = [
	Exit('east', 'taohua/dating', False),
]
wofang=Room('taohua/wofang', u'卧房', None, 0, exits)

exits = [
	Exit('northwest', 'taohua/houyuan', False),
]
wuchang1=Room('taohua/wuchang1', u'修行场', 'taohua', 0, exits)

exits = [
	Exit('northeast', 'taohua/houyuan', False),
]
wuchang2=Room('taohua/wuchang2', u'修行场', 'taohua', 0, exits)

exits = [
	Exit('north', 'taohua/houyuan', False),
]
wuchang3=Room('taohua/wuchang3', u'修行场', 'taohua', 0, exits)

exits = [
	Exit('east', 'taohua/houyuan', False),
]
xiaowu=Room('taohua/xiaowu', u'小屋', None, 1, exits)

exits = [
]
xiuxishi=Room('taohua/xiuxishi', u'桃花轩', None, 0, exits)

