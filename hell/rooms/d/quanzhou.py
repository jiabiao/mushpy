# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'quanzhou/zhongxin', False),
	Exit('north', 'fuzhou/puxian', False),
]
beimen=Room('quanzhou/beimen', u'Ȫ�ݱ���', 'quanzhou', 0, exits)

exits = [
	Exit('west', 'quanzhou/qzroad4', False),
]
chating=Room('quanzhou/chating', u'��ͤ', 'quanzhou', 0, exits)

exits = [
	Exit('south', 'quanzhou/dagou', False),
	Exit('eastup', 'quanzhou/riyuetang', False),
	Exit('north', 'quanzhou/jilong', False),
]
chiqian=Room('quanzhou/chiqian', u'��Ƕ��', 'quanzhou', 0, exits)

exits = [
	Exit('north', 'quanzhou/chiqian', False),
]
dagou=Room('quanzhou/dagou', u'�򹷸�', 'quanzhou', 0, exits)

exits = [
]
dahai=Room('quanzhou/dahai', u'��', 'taohua', 0, exits)

exits = [
	Exit('west', 'quanzhou/zhongxin', False),
]
haigang=Room('quanzhou/haigang', u'����', 'quanzhou', 0, exits)

exits = [
	Exit('west', 'quanzhou/qzroad2', False),
	Exit('south', 'quanzhou/jxnanmen', False),
	Exit('east', 'quanzhou/nanhu', False),
]
jiaxing=Room('quanzhou/jiaxing', u'���˳�', 'jiaxing', 0, exits)

exits = [
	Exit('west', 'quanzhou/nanhu', False),
]
jiaxinggang=Room('quanzhou/jiaxinggang', u'���˺���', 'quanzhou', 0, exits)

exits = [
	Exit('south', 'quanzhou/chiqian', False),
]
jilong=Room('quanzhou/jilong', u'������', 'quanzhou', 0, exits)

exits = [
	Exit('southeast', 'hangzhou/road1', False),
	Exit('south', 'quanzhou/qzroad4', False),
	Exit('southwest', 'quanzhou/majiu2', False),
	Exit('east', 'quanzhou/tieqiang', False),
	Exit('north', 'quanzhou/jiaxing', False),
]
jxnanmen=Room('quanzhou/jxnanmen', u'��������', 'jiaxing', 0, exits)

exits = [
	Exit('northwest', 'quanzhou/zhongxin', False),
]
majiu1=Room('quanzhou/majiu1', u'���', 'quanzhou', 0, exits)

exits = [
	Exit('northeast', 'quanzhou/jxnanmen', False),
]
majiu2=Room('quanzhou/majiu2', u'���', 'jiaxing', 0, exits)

exits = [
	Exit('southeast', 'quanzhou/nanhu1', False),
	Exit('west', 'quanzhou/jiaxing', False),
	Exit('south', 'quanzhou/tieqiang', False),
	Exit('east', 'quanzhou/jiaxinggang', False),
]
nanhu=Room('quanzhou/nanhu', u'�����Ϻ�', 'jiaxing', 0, exits)

exits = [
	Exit('northwest', 'quanzhou/nanhu', False),
	Exit('south', 'quanzhou/yanyu', False),
]
nanhu1=Room('quanzhou/nanhu1', u'�����Ϻ�', 'jiaxing', 0, exits)

exits = [
	Exit('north', 'quanzhou/zhongxin', False),
]
nanmen=Room('quanzhou/nanmen', u'Ȫ������', 'quanzhou', 0, exits)

exits = [
]
penghu=Room('quanzhou/penghu', u'�����', 'quanzhou', 0, exits)

exits = [
	Exit('northwest', 'taishan/yidao1', False),
	Exit('south', 'quanzhou/qzroad2', False),
]
qzroad1=Room('quanzhou/qzroad1', u'ɽ·', 'quanzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/dongmen', False),
	Exit('south', 'quanzhou/qzroad3', False),
	Exit('east', 'quanzhou/jiaxing', False),
	Exit('north', 'quanzhou/qzroad1', False),
]
qzroad2=Room('quanzhou/qzroad2', u'ɽ·', 'quanzhou', 0, exits)

exits = [
	Exit('east', 'quanzhou/qzroad4', False),
	Exit('north', 'quanzhou/qzroad2', False),
]
qzroad3=Room('quanzhou/qzroad3', u'ɽ·', 'quanzhou', 0, exits)

exits = [
	Exit('west', 'quanzhou/qzroad3', False),
	Exit('southup', 'fuzhou/fzroad1', False),
	Exit('east', 'quanzhou/chating', False),
	Exit('north', 'quanzhou/jxnanmen', False),
]
qzroad4=Room('quanzhou/qzroad4', u'ɽ·', 'quanzhou', 0, exits)

exits = [
	Exit('westdown', 'quanzhou/chiqian', False),
]
riyuetang=Room('quanzhou/riyuetang', u'����̶', 'quanzhou', 0, exits)

exits = [
	Exit('west', 'quanzhou/jxnanmen', False),
	Exit('north', 'quanzhou/nanhu', False),
]
tieqiang=Room('quanzhou/tieqiang', u'��ǹ��', 'jiaxing', 0, exits)

exits = [
	Exit('west', 'foshan/road14', False),
	Exit('east', 'quanzhou/ximen', False),
]
westbridge=Room('quanzhou/westbridge', u'���ŵ���', 'foshan', 0, exits)

exits = [
	Exit('west', 'quanzhou/zahuopu', False),
	Exit('north', 'quanzhou/laozhai', False),
	Exit('east', 'quanzhou/zhongxin', False),
]
xijie=Room('quanzhou/xijie', u'����', 'quanzhou', 0, exits)

exits = [
	Exit('west', 'quanzhou/westbridge', False),
	Exit('east', 'quanzhou/zhongxin', False),
]
ximen=Room('quanzhou/ximen', u'Ȫ������', 'quanzhou', 0, exits)

exits = [
	Exit('north', 'quanzhou/nanhu1', False),
	Exit('up', 'quanzhou/yanyu2', False),
]
yanyu=Room('quanzhou/yanyu', u'����¥', None, 0, exits)

exits = [
	Exit('down', 'quanzhou/yanyu', False),
]
yanyu2=Room('quanzhou/yanyu2', u'����¥��¥', None, 0, exits)

exits = [
	Exit('southeast', 'quanzhou/majiu1', False),
	Exit('west', 'quanzhou/ximen', False),
	Exit('south', 'quanzhou/nanmen', False),
	Exit('east', 'quanzhou/haigang', False),
	Exit('north', 'quanzhou/beimen', False),
]
zhongxin=Room('quanzhou/zhongxin', u'������', 'quanzhou', 0, exits)

