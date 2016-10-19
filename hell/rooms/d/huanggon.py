# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('north', 'huanggon/zoulang1', False),
]
fang1=Room('huanggon/fang1', u'房舍', None, 0, exits)

exits = [
	Exit('south', 'huanggon/zoulang1', False),
]
fang2=Room('huanggon/fang2', u'房舍', None, 0, exits)

exits = [
	Exit('west', 'huanggon/houhuayuan2', False),
	Exit('south', 'huanggon/qihedian', False),
]
houhuayuan=Room('huanggon/houhuayuan', u'后花苑', 'huanggon', 0, exits)

exits = [
	Exit('west', 'huanggon/majuan', False),
	Exit('east', 'huanggon/houhuayuan', False),
]
houhuayuan2=Room('huanggon/houhuayuan2', u'后花苑', 'huanggon', 0, exits)

exits = [
	Exit('east', 'huanggon/zoulang1', False),
]
houyuan=Room('huanggon/houyuan', u'清和殿后院', 'huanggon', 0, exits)

exits = [
]
inwell=Room('huanggon/inwell', u'井底', 'huanggon', 0, exits)

exits = [
	Exit('east', 'huanggon/houhuayuan2', False),
]
majuan=Room('huanggon/majuan', u'马圈', None, 0, exits)

exits = [
	Exit('west', 'huanggon/zoulang1', False),
	Exit('south', 'city2/zhengmen', False),
]
qihedian=Room('huanggon/qihedian', u'清和殿', 'huanggon', 0, exits)

exits = [
]
shanfang=Room('huanggon/shanfang', u'御膳房', None, 0, exits)

exits = [
	Exit('south', 'huanggon/tinglang1', False),
]
shufang=Room('huanggon/shufang', u'御书房', None, 0, exits)

exits = [
	Exit('south', 'huanggon/tinglang2', False),
	Exit('north', 'huanggon/shufang', False),
]
tinglang1=Room('huanggon/tinglang1', u'厅廊', 'huangon', 0, exits)

exits = [
	Exit('west', 'huanggon/tinglang3', False),
	Exit('south', 'huanggon/taihedai', False),
	Exit('north', 'huanggon/tinglang1', False),
]
tinglang2=Room('huanggon/tinglang2', u'厅廊', 'huangon', 0, exits)

exits = [
	Exit('east', 'clude/net/kunning', False),
	Exit('north', 'huanggon/qihedian', False),
]
tinglang3=Room('huanggon/tinglang3', u'厅廊', 'huangon', 0, exits)

exits = [
	Exit('west', 'huanggon/houyuan', False),
	Exit('south', 'huanggon/fang1', False),
	Exit('north', 'huanggon/fang2', False),
	Exit('east', 'huanggon/qihedian', False),
]
zoulang1=Room('huanggon/zoulang1', u'走廊', None, 0, exits)

