# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'hengshan/square', False),
]
baiyunan=Room('hengshan/baiyunan', u'������', None, 0, exits)

exits = [
	Exit('southdown', 'hengshan/beiyuemiao', False),
	Exit('northup', 'hengshan/shandao1', False),
	Exit('eastup', 'hengshan/yuyang', False),
	Exit('westup', 'hengshan/huixiantai', False),
]
beiyuedian=Room('hengshan/beiyuedian', u'������', None, 0, exits)

exits = [
	Exit('southdown', 'hengshan/guolaoling', False),
	Exit('west', 'hengshan/jijiaoshi', False),
	Exit('northup', 'hengshan/beiyuedian', False),
	Exit('east', 'hengshan/kutianjing', False),
]
beiyuemiao=Room('hengshan/beiyuemiao', u'������', None, 0, exits)

exits = [
	Exit('down', 'hengshan/cuipinggu2', False),
	Exit('westup', 'hengshan/cuiping2', False),
]
cuiping1=Room('hengshan/cuiping1', u'����ɽ��', 'hengshan', 0, exits)

exits = [
	Exit('eastdown', 'hengshan/cuiping1', False),
	Exit('eastup', 'hengshan/xuankong1', False),
]
cuiping2=Room('hengshan/cuiping2', u'����ɽ��', 'hengshan', 0, exits)

exits = [
	Exit('southeast', 'hengshan/cuipinggu2', False),
	Exit('northwest', 'hengshan/jinlongxia', False),
]
cuipinggu1=Room('hengshan/cuipinggu1', u'������', 'hengshan', 0, exits)

exits = [
	Exit('northwest', 'hengshan/cuipinggu1', False),
	Exit('up', 'hengshan/cuiping1', False),
]
cuipinggu2=Room('hengshan/cuipinggu2', u'������', 'hengshan', 0, exits)

exits = [
	Exit('west', 'hengshan/yunge', False),
	Exit('northeast', 'hengshan/hufengkou', False),
]
daziling=Room('hengshan/daziling', u'������', 'hengshan', 0, exits)

exits = [
	Exit('northup', 'hengshan/beiyuemiao', False),
	Exit('southwest', 'hengshan/hufengkou', False),
	Exit('westdown', 'hengshan/tongyuangu', False),
]
guolaoling=Room('hengshan/guolaoling', u'������', 'hengshan', 0, exits)

exits = [
	Exit('west', 'hengshan/xuangengsong', False),
	Exit('southwest', 'hengshan/daziling', False),
	Exit('northeast', 'hengshan/guolaoling', False),
]
hufengkou=Room('hengshan/hufengkou', u'�����', 'hengshan', 0, exits)

exits = [
	Exit('eastdown', 'hengshan/beiyuedian', False),
]
huixiantai=Room('hengshan/huixiantai', u'����̨', None, 0, exits)

exits = [
	Exit('east', 'hengshan/beiyuemiao', False),
]
jijiaoshi=Room('hengshan/jijiaoshi', u'����ʯ', 'hengshan', 0, exits)

exits = [
	Exit('southeast', 'hengshan/cuipinggu1', False),
	Exit('northeast', 'beijing/road6', False),
]
jinlongxia=Room('hengshan/jinlongxia', u'����Ͽ', 'hengshan', 0, exits)

exits = [
	Exit('west', 'hengshan/beiyuemiao', False),
]
kutianjing=Room('hengshan/kutianjing', u'����', 'hengshan', 0, exits)

exits = [
	Exit('down', 'hengshan/xuankong1', False),
]
sanjiaodian=Room('hengshan/sanjiaodian', u'���̵�', None, 0, exits)

exits = [
	Exit('southdown', 'hengshan/beiyuedian', False),
	Exit('northup', 'hengshan/shandao2', False),
]
shandao1=Room('hengshan/shandao1', u'���Է�ɽ��', None, 0, exits)

exits = [
	Exit('southdown', 'hengshan/beiyuedian', False),
	Exit('eastup', 'hengshan/square', False),
]
shandao2=Room('hengshan/shandao2', u'���Է�ɽ��', None, 0, exits)

exits = [
	Exit('north', 'hengshan/baiyunan', False),
	Exit('westdown', 'hengshan/shandao2', False),
]
square=Room('hengshan/square', u'���Է�㳡', 'hengshan', 0, exits)

exits = [
	Exit('eastup', 'hengshan/guolaoling', False),
]
tongyuangu=Room('hengshan/tongyuangu', u'ͨԪ��', 'hengshan', 0, exits)

exits = [
	Exit('east', 'hengshan/hufengkou', False),
]
xuangengsong=Room('hengshan/xuangengsong', u'������', 'hengshan', 0, exits)

exits = [
	Exit('south', 'hengshan/zhanqiao', False),
	Exit('westdown', 'hengshan/cuiping2', False),
	Exit('up', 'hengshan/sanjiaodian', False),
]
xuankong1=Room('hengshan/xuankong1', u'�����±�¥', None, 0, exits)

exits = [
	Exit('southup', 'hengshan/zhandao', False),
	Exit('north', 'hengshan/zhanqiao', False),
]
xuankong2=Room('hengshan/xuankong2', u'��������¥', None, 0, exits)

exits = [
	Exit('northdown', 'hengshan/zhandao', False),
	Exit('east', 'hengshan/daziling', False),
]
yunge=Room('hengshan/yunge', u'�Ƹ����', 'hengshan', 0, exits)

exits = [
	Exit('westdown', 'hengshan/beiyuedian', False),
]
yuyang=Room('hengshan/yuyang', u'��������', 'hengshan', 0, exits)

exits = [
	Exit('southup', 'hengshan/yunge', False),
	Exit('northdown', 'hengshan/xuankong2', False),
]
zhandao=Room('hengshan/zhandao', u'��ʽջ��', 'hengshan', 0, exits)

exits = [
	Exit('south', 'hengshan/xuankong2', False),
	Exit('north', 'hengshan/xuankong1', False),
]
zhanqiao=Room('hengshan/zhanqiao', u'����ջ��', 'hengshan', 0, exits)

