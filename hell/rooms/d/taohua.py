# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('west', 'taohua/qianyuan', False),
]
bingqi=Room('taohua/bingqi', u'������', None, 0, exits)

exits = [
	Exit('east', 'taohua/qianyuan', False),
]
chufang=Room('taohua/chufang', u'����', None, 0, exits)

exits = [
]
dahai=Room('taohua/dahai', u'��', 'taohua', 0, exits)

exits = [
	Exit('south', 'taohua/qianyuan', False),
	Exit('east', 'taohua/road1', False),
	Exit('north', 'taohua/tingzi', False),
]
damen=Room('taohua/damen', u'�һ�ɽׯ����', 'taohua', 0, exits)

exits = [
	Exit('west', 'taohua/dating', False),
	Exit('up', 'taohua/shufang', False),
]
daojufang=Room('taohua/daojufang', u'���߷�', None, 0, exits)

exits = [
	Exit('west', 'taohua/wofang', False),
	Exit('south', 'taohua/houyuan', False),
	Exit('east', 'taohua/daojufang', False),
	Exit('north', 'taohua/qianyuan', False),
]
dating=Room('taohua/dating', u'�һ�ɽׯ����', None, 0, exits)

exits = [
	Exit('out', 'taohua/road5', False),
]
dong=Room('taohua/dong', u'ɽ��', None, 0, exits)

exits = [
	Exit('south', 'taohua/tao_in', False),
]
haitan=Room('taohua/haitan', u'��̲', 'taohua', 0, exits)

exits = [
	Exit('southeast', 'taohua/wuchang1', False),
	Exit('west', 'taohua/xiaowu', False),
	Exit('south', 'taohua/wuchang3', False),
	Exit('southwest', 'taohua/wuchang2', False),
	Exit('east', 'taohua/siguoshi', False),
	Exit('north', 'taohua/dating', False),
]
houyuan=Room('taohua/houyuan', u'��Ժ', 'taohua', 0, exits)

exits = [
]
lantian=Room('taohua/lantian', u'����', 'taohua', 0, exits)

exits = [
	Exit('up', 'taohua/mudi', False),
	Exit('down', 'taohua/mushi', False),
]
mudao=Room('taohua/mudao', u'Ĺ��', None, 0, exits)

exits = [
	Exit('south', 'taohua/road3', False),
]
mudi=Room('taohua/mudi', u'Ĺ��', 'taohua', 0, exits)

exits = [
	Exit('up', 'taohua/mudao', False),
]
mushi=Room('taohua/mushi', u'Ĺ��', None, 0, exits)

exits = [
	Exit('west', 'taohua/chufang', False),
	Exit('south', 'taohua/dating', False),
	Exit('east', 'taohua/bingqi', False),
	Exit('north', 'taohua/damen', False),
]
qianyuan=Room('taohua/qianyuan', u'ǰԺ', 'taohua', 0, exits)

exits = [
	Exit('west', 'taohua/damen', False),
	Exit('east', 'taohua/road2', False),
]
road1=Room('taohua/road1', u'С·', 'taohua', 0, exits)

exits = [
	Exit('west', 'taohua/road1', False),
	Exit('south', 'taohua/road4', False),
	Exit('north', 'taohua/road3', False),
]
road2=Room('taohua/road2', u'С·', 'taohua', 0, exits)

exits = [
	Exit('south', 'taohua/road2', False),
	Exit('north', 'taohua/mudi', False),
]
road3=Room('taohua/road3', u'С·', 'taohua', 0, exits)

exits = [
	Exit('north', 'taohua/road2', False),
	Exit('east', 'taohua/road5', False),
]
road4=Room('taohua/road4', u'С·', 'taohua', 0, exits)

exits = [
	Exit('west', 'taohua/road4', False),
	Exit('enter', 'taohua/dong', False),
]
road5=Room('taohua/road5', u'����', 'taohua', 0, exits)

exits = [
	Exit('down', 'taohua/daojufang', False),
]
shufang=Room('taohua/shufang', u'�鷿', None, 0, exits)

exits = [
	Exit('west', 'taohua/houyuan', False),
]
siguoshi=Room('taohua/siguoshi', u'˼����', None, 0, exits)

exits = [
	Exit('west', 'taohua/tao0', False),
	Exit('south', 'taohua/tao0', False),
	Exit('north', 'taohua/tao0', False),
	Exit('east', 'taohua/tao0', False),
]
tao0=Room('taohua/tao0', u'�һ�����', 'taohua', 0, exits)

exits = [
	Exit('south', 'taohua/tao0', False),
	Exit('north', 'taohua/haitan', False),
]
tao_in=Room('taohua/tao_in', u'�������', 'taohua', 0, exits)

exits = [
	Exit('south', 'taohua/tingzi', False),
	Exit('north', 'taohua/tao0', False),
]
tao_out=Room('taohua/tao_out', u'���ֱ�', 'taohua', 0, exits)

exits = [
	Exit('south', 'taohua/damen', False),
	Exit('north', 'taohua/tao_out', False),
]
tingzi=Room('taohua/tingzi', u'�Խ�ͤ', 'taohua', 0, exits)

exits = [
	Exit('east', 'taohua/dating', False),
]
wofang=Room('taohua/wofang', u'�Է�', None, 0, exits)

exits = [
	Exit('northwest', 'taohua/houyuan', False),
]
wuchang1=Room('taohua/wuchang1', u'���г�', 'taohua', 0, exits)

exits = [
	Exit('northeast', 'taohua/houyuan', False),
]
wuchang2=Room('taohua/wuchang2', u'���г�', 'taohua', 0, exits)

exits = [
	Exit('north', 'taohua/houyuan', False),
]
wuchang3=Room('taohua/wuchang3', u'���г�', 'taohua', 0, exits)

exits = [
	Exit('east', 'taohua/houyuan', False),
]
xiaowu=Room('taohua/xiaowu', u'С��', None, 1, exits)

exits = [
]
xiuxishi=Room('taohua/xiuxishi', u'�һ���', None, 0, exits)

