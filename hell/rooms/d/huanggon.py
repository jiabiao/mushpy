# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('north', 'huanggon/zoulang1', False),
]
fang1=Room('huanggon/fang1', u'����', None, 0, exits)

exits = [
	Exit('south', 'huanggon/zoulang1', False),
]
fang2=Room('huanggon/fang2', u'����', None, 0, exits)

exits = [
	Exit('west', 'huanggon/houhuayuan2', False),
	Exit('south', 'huanggon/qihedian', False),
]
houhuayuan=Room('huanggon/houhuayuan', u'��Է', 'huanggon', 0, exits)

exits = [
	Exit('west', 'huanggon/majuan', False),
	Exit('east', 'huanggon/houhuayuan', False),
]
houhuayuan2=Room('huanggon/houhuayuan2', u'��Է', 'huanggon', 0, exits)

exits = [
	Exit('east', 'huanggon/zoulang1', False),
]
houyuan=Room('huanggon/houyuan', u'��͵��Ժ', 'huanggon', 0, exits)

exits = [
]
inwell=Room('huanggon/inwell', u'����', 'huanggon', 0, exits)

exits = [
	Exit('east', 'huanggon/houhuayuan2', False),
]
majuan=Room('huanggon/majuan', u'��Ȧ', None, 0, exits)

exits = [
	Exit('west', 'huanggon/zoulang1', False),
	Exit('south', 'city2/zhengmen', False),
]
qihedian=Room('huanggon/qihedian', u'��͵�', 'huanggon', 0, exits)

exits = [
]
shanfang=Room('huanggon/shanfang', u'���ŷ�', None, 0, exits)

exits = [
	Exit('south', 'huanggon/tinglang1', False),
]
shufang=Room('huanggon/shufang', u'���鷿', None, 0, exits)

exits = [
	Exit('south', 'huanggon/tinglang2', False),
	Exit('north', 'huanggon/shufang', False),
]
tinglang1=Room('huanggon/tinglang1', u'����', 'huangon', 0, exits)

exits = [
	Exit('west', 'huanggon/tinglang3', False),
	Exit('south', 'huanggon/taihedai', False),
	Exit('north', 'huanggon/tinglang1', False),
]
tinglang2=Room('huanggon/tinglang2', u'����', 'huangon', 0, exits)

exits = [
	Exit('east', 'clude/net/kunning', False),
	Exit('north', 'huanggon/qihedian', False),
]
tinglang3=Room('huanggon/tinglang3', u'����', 'huangon', 0, exits)

exits = [
	Exit('west', 'huanggon/houyuan', False),
	Exit('south', 'huanggon/fang1', False),
	Exit('north', 'huanggon/fang2', False),
	Exit('east', 'huanggon/qihedian', False),
]
zoulang1=Room('huanggon/zoulang1', u'����', None, 0, exits)

