# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'guiyun/huayuan', False),
]
chufang=Room('guiyun/chufang', u'����', None, 0, exits)

exits = [
	Exit('south', 'guiyun/matou', False),
	Exit('enter', 'guiyun/qianyuan', False),
]
damen=Room('guiyun/damen', u'����', 'guiyun', 0, exits)

exits = [
	Exit('south', 'guiyun/qianyuan', False),
	Exit('east', 'guiyun/shufang', False),
	Exit('north', 'guiyun/huating', False),
]
dating=Room('guiyun/dating', u'����', None, 0, exits)

exits = [
]
duchuan=Room('guiyun/duchuan', u'�ɴ�', 'city', 0, exits)

exits = [
	Exit('west', 'guiyun/nvxiangfang', False),
	Exit('south', 'guiyun/dating', False),
	Exit('east', 'guiyun/nanxiangfang', False),
	Exit('north', 'guiyun/huayuan', False),
]
huating=Room('guiyun/huating', u'����', 'guiyun', 0, exits)

exits = [
	Exit('south', 'guiyun/huating', False),
	Exit('east', 'guiyun/liangong', False),
	Exit('north', 'guiyun/chufang', False),
]
huayuan=Room('guiyun/huayuan', u'��԰', 'guiyun', 0, exits)

exits = [
	Exit('out', 'guiyun/ship', False),
]
jinship=Room('guiyun/jinship', u'���ս��', 'guiyun', 0, exits)

exits = [
	Exit('west', 'guiyun/huayuan', False),
]
liangong=Room('guiyun/liangong', u'������', None, 0, exits)

exits = [
	Exit('north', 'guiyun/damen', False),
]
matou=Room('guiyun/matou', u'��ͷ', 'guiyun', 0, exits)

exits = [
	Exit('west', 'guiyun/huating', False),
]
nanxiangfang=Room('guiyun/nanxiangfang', u'���᷿', None, 0, exits)

exits = [
	Exit('north', 'guiyun/yixing', False),
]
nanxun=Room('guiyun/nanxun', u'�����', 'guiyun', 0, exits)

exits = [
	Exit('east', 'guiyun/huating', False),
]
nvxiangfang=Room('guiyun/nvxiangfang', u'Ů�᷿', None, 0, exits)

exits = [
	Exit('out', 'guiyun/damen', False),
	Exit('north', 'guiyun/dating', False),
]
qianyuan=Room('guiyun/qianyuan', u'ǰԺ', 'guiyun', 0, exits)

exits = [
	Exit('south', 'guiyun/taihu', False),
	Exit('northeast', 'guiyun/shanlu2', False),
	Exit('north', 'guiyun/shulin4', False),
]
shanlu1=Room('guiyun/shanlu1', u'ɽ·', 'guiyun', 0, exits)

exits = [
	Exit('southeast', 'suzhou/road1', False),
	Exit('southwest', 'guiyun/shanlu1', False),
]
shanlu2=Room('guiyun/shanlu2', u'ɽ·', 'guiyun', 0, exits)

exits = [
]
ship=Room('guiyun/ship', u'ս��', 'city', 0, exits)

exits = [
	Exit('west', 'guiyun/dating', False),
]
shufang=Room('guiyun/shufang', u'�鷿', None, 0, exits)

exits = [
	Exit('southeast', 'guiyun/shulin2', False),
	Exit('northwest', 'city/jiaowai4', False),
]
shulin1=Room('guiyun/shulin1', u'����', 'guiyun', 0, exits)

exits = [
	Exit('west', 'guiyun/shulin5', False),
	Exit('southeast', 'guiyun/shulin3', False),
	Exit('northwest', 'guiyun/shulin1', False),
]
shulin2=Room('guiyun/shulin2', u'����', 'guiyun', 0, exits)

exits = [
	Exit('northwest', 'guiyun/shulin2', False),
	Exit('east', 'guiyun/shulin4', False),
]
shulin3=Room('guiyun/shulin3', u'����', 'guiyun', 0, exits)

exits = [
	Exit('west', 'guiyun/shulin3', False),
	Exit('south', 'guiyun/shanlu1', False),
]
shulin4=Room('guiyun/shulin4', u'����', 'guiyun', 0, exits)

exits = [
	Exit('southwest', 'guiyun/tiandi', False),
	Exit('east', 'guiyun/shulin2', False),
]
shulin5=Room('guiyun/shulin5', u'����', 'guiyun', 0, exits)

exits = [
	Exit('north', 'guiyun/shanlu1', False),
]
taihu=Room('guiyun/taihu', u'̫��', 'guiyun', 0, exits)

exits = [
	Exit('west', 'guiyun/yixing', False),
	Exit('northeast', 'guiyun/shulin5', False),
]
tiandi=Room('guiyun/tiandi', u'���', 'guiyun', 0, exits)

exits = [
	Exit('northwest', 'wudang/wdroad2', False),
	Exit('south', 'guiyun/nanxun', False),
	Exit('east', 'guiyun/tiandi', False),
]
yixing=Room('guiyun/yixing', u'����', 'guiyun', 0, exits)

