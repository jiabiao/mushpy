# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'xiaoyao/xiaodao2', False),
]
bingqif=Room('xiaoyao/bingqif', u'������', None, 0, exits)

exits = [
	Exit('south', 'xiaoyao/xiaodao4', False),
]
liangong=Room('xiaoyao/liangong', u'ʯ��', None, 0, exits)

exits = [
	Exit('out', 'xiaoyao/qingcaop', False),
	Exit('down', 'xiaoyao/shishi', False),
]
midao=Room('xiaoyao/midao', u'����ͨ��', None, 0, exits)

exits = [
	Exit('south', 'xiaoyao/muwu3', False),
	Exit('north', 'xiaoyao/xiaodao4', False),
]
mubanlu=Room('xiaoyao/mubanlu', u'ľ��·', 'xiaoyao', 0, exits)

exits = [
	Exit('north', 'xiaoyao/xiaodao5', False),
]
muwu1=Room('xiaoyao/muwu1', u'ľ��', None, 0, exits)

exits = [
	Exit('south', 'xiaoyao/xiaodao3', False),
]
muwu2=Room('xiaoyao/muwu2', u'Сľ��', None, 0, exits)

exits = [
	Exit('north', 'xiaoyao/mubanlu', False),
]
muwu3=Room('xiaoyao/muwu3', u'������', None, 0, exits)

exits = [
	Exit('west', 'xiaoyao/xiaodao1', False),
	Exit('south', 'xiaoyao/xiaodao5', False),
	Exit('east', 'xiaoyao/xiaodao4', False),
	Exit('north', 'xiaoyao/xiaodao3', False),
	Exit('enter', 'xiaoyao/midao', False),
]
qingcaop=Room('xiaoyao/qingcaop', u'���ƺ', 'xiaoyao', 0, exits)

exits = [
	Exit('north', 'xiaoyao/xiaodao2', False),
]
shantang=Room('xiaoyao/shantang', u'�Ƽ�', None, 0, exits)

exits = [
	Exit('up', 'xiaoyao/midao', False),
]
shishi=Room('xiaoyao/shishi', u'ʯ��', None, 0, exits)

exits = [
	Exit('west', 'xiaoyao/xiaodao4', False),
	Exit('south', 'xiaoyao/shulin1', False),
	Exit('east', 'xiaoyao/shulin2', False),
	Exit('north', 'xiaoyao/shulin1', False),
]
shulin1=Room('xiaoyao/shulin1', u'����', 'xiaoyao', 0, exits)

exits = [
	Exit('west', 'xiaoyao/shulin2', False),
	Exit('south', 'xiaoyao/shulin1', False),
	Exit('east', 'xiaoyao/shulin2', False),
	Exit('north', 'xiaoyao/shulin3', False),
]
shulin2=Room('xiaoyao/shulin2', u'����', 'xiaoyao', 0, exits)

exits = [
	Exit('west', 'wudang/wdroad4', False),
	Exit('south', 'xiaoyao/shulin3', False),
	Exit('east', 'xiaoyao/shulin2', False),
	Exit('north', 'xiaoyao/shulin3', False),
]
shulin3=Room('xiaoyao/shulin3', u'����', 'xiaoyao', 0, exits)

exits = [
	Exit('south', 'xiaoyao/xiaodao1', False),
	Exit('north', 'xiaoyao/wuchang3', False),
]
wuchang1=Room('xiaoyao/wuchang1', u'��ң��', 'xiaoyao', 0, exits)

exits = [
	Exit('north', 'xiaoyao/xiaodao1', False),
]
wuchang2=Room('xiaoyao/wuchang2', u'��ң��', 'xiaoyao', 0, exits)

exits = [
	Exit('south', 'xiaoyao/wuchang1', False),
]
wuchang3=Room('xiaoyao/wuchang3', u'��ң��', 'xiaoyao', 0, exits)

exits = [
	Exit('west', 'xiaoyao/xiaodao2', False),
	Exit('south', 'xiaoyao/wuchang2', False),
	Exit('north', 'xiaoyao/wuchang1', False),
	Exit('east', 'xiaoyao/qingcaop', False),
]
xiaodao1=Room('xiaoyao/xiaodao1', u'�ּ�С��', 'xiaoyao', 0, exits)

exits = [
	Exit('west', 'xiaoyao/xiuxis', False),
	Exit('south', 'xiaoyao/shantang', False),
	Exit('north', 'xiaoyao/bingqif', False),
	Exit('east', 'xiaoyao/xiaodao1', False),
]
xiaodao2=Room('xiaoyao/xiaodao2', u'�ּ�С��', 'xiaoyao', 0, exits)

exits = [
	Exit('south', 'xiaoyao/qingcaop', False),
	Exit('north', 'xiaoyao/muwu2', False),
]
xiaodao3=Room('xiaoyao/xiaodao3', u'�ּ�С��', 'xiaoyao', 0, exits)

exits = [
	Exit('west', 'xiaoyao/qingcaop', False),
	Exit('south', 'xiaoyao/mubanlu', False),
	Exit('north', 'xiaoyao/liangong', False),
	Exit('east', 'xiaoyao/shulin1', False),
]
xiaodao4=Room('xiaoyao/xiaodao4', u'�ּ�С��', 'xiaoyao', 0, exits)

exits = [
	Exit('south', 'xiaoyao/muwu1', False),
	Exit('north', 'xiaoyao/qingcaop', False),
]
xiaodao5=Room('xiaoyao/xiaodao5', u'�ּ�С��', 'xiaoyao', 0, exits)

exits = [
	Exit('east', 'xiaoyao/xiaodao2', False),
]
xiuxis=Room('xiaoyao/xiuxis', u'С��', None, 0, exits)

