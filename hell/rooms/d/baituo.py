# coding=gbk
from _objects import Room,Exit


exits = [
	Exit('northwest', 'baituo/guangchang', False),
	Exit('east', 'baituo/xijie', False),
]
bridge=Room('baituo/bridge', u'С��', 'baituo', 0, exits)

exits = [
	Exit('west', 'baituo/cao1', False),
	Exit('south', 'baituo/cao1', False),
	Exit('east', 'baituo/ximen', False),
	Exit('north', 'baituo/cao2', False),
]
cao1=Room('baituo/cao1', u'�ݴ�', 'baituo', 0, exits)

exits = [
	Exit('west', 'baituo/cao2', False),
	Exit('south', 'baituo/cao1', False),
	Exit('east', 'baituo/cao1', False),
	Exit('north', 'baituo/zhulin', False),
]
cao2=Room('baituo/cao2', u'�ݴ�', 'baituo', 0, exits)

exits = [
	Exit('northeast', 'baituo/shulin1', False),
]
caomeide=Room('baituo/caomeide', u'��ݮ��', 'baituo', 0, exits)

exits = [
	Exit('west', 'baituo/shijie', False),
]
caoping=Room('baituo/caoping', u'��ƺ', 'baituo', 0, exits)

exits = [
	Exit('southdown', 'baituo/zhulin', False),
	Exit('north', 'baituo/cave1', False),
]
cave=Room('baituo/cave', u'�Ҷ�', 'baituo', 0, exits)

exits = [
	Exit('south', 'baituo/cave', False),
]
cave1=Room('baituo/cave1', u'�Ҷ���', None, 0, exits)

exits = [
	Exit('east', 'baituo/dongnei', False),
]
cedong=Room('baituo/cedong', u'�ප', None, 0, exits)

exits = [
	Exit('west', 'baituo/chufang', False),
]
chaifang=Room('baituo/chaifang', u'��', None, 0, exits)

exits = [
	Exit('west', 'baituo/ximen', False),
	Exit('south', 'baituo/yaofang', False),
	Exit('east', 'baituo/liangong', False),
	Exit('north', 'baituo/restroom', False),
]
changlang=Room('baituo/changlang', u'����', None, 0, exits)

exits = [
	Exit('west', 'baituo/huayuan', False),
	Exit('east', 'baituo/chaifang', False),
]
chufang=Room('baituo/chufang', u'����', None, 1, exits)

exits = [
	Exit('southdown', 'baituo/shijie', False),
	Exit('north', 'baituo/yuanzi', False),
]
damen=Room('baituo/damen', u'����', 'baituo', 0, exits)

exits = [
	Exit('north', 'baituo/dongjie', False),
]
datiepu=Room('baituo/datiepu', u'������', None, 0, exits)

exits = [
	Exit('southdown', 'baituo/yuanzi', False),
	Exit('north', 'baituo/liangong', False),
]
dating=Room('baituo/dating', u'����', None, 0, exits)

exits = [
	Exit('southeast', 'baituo/gebi', False),
	Exit('west', 'baituo/xijie', False),
	Exit('south', 'baituo/datiepu', False),
	Exit('northeast', 'baituo/xiaolu1', False),
]
dongjie=Room('baituo/dongjie', u'����', 'baituo', 0, exits)

exits = [
	Exit('south', 'baituo/xiaolu4', False),
	Exit('north', 'baituo/dongnei', False),
]
dongkou=Room('baituo/dongkou', u'����', 'baituo', 0, exits)

exits = [
	Exit('west', 'baituo/cedong', False),
	Exit('south', 'baituo/dongkou', False),
]
dongnei=Room('baituo/dongnei', u'����', None, 0, exits)

exits = [
	Exit('west', 'baituo/liangong', False),
	Exit('2', 'baituo/room2', False),
	Exit('3', 'baituo/room3', False),
	Exit('1', 'baituo/room1', False),
]
fang=Room('baituo/fang', u'������', None, 0, exits)

exits = [
	Exit('southwest', 'baituo/xiaolu1', False),
]
fende=Room('baituo/fende', u'�ص�', 'baituo', 0, exits)

exits = [
	Exit('northwest', 'baituo/dongjie', False),
	Exit('east', 'xingxiu/shamo10', False),
]
gebi=Room('baituo/gebi', u'���', 'baituo', 0, exits)

exits = [
	Exit('southeast', 'baituo/bridge', False),
	Exit('northwest', 'baituo/shanlu', False),
	Exit('northup', 'baituo/shijie', False),
	Exit('east', 'baituo/nongshe', False),
]
guangchang=Room('baituo/guangchang', u'�㳡', 'baituo', 0, exits)

exits = [
	Exit('southeast', 'baituo/zhuyuan', False),
]
houyuan=Room('baituo/houyuan', u'��Ժ', 'baituo', 0, exits)

exits = [
	Exit('west', 'baituo/neishi', False),
	Exit('south', 'baituo/menlang', False),
	Exit('east', 'baituo/chufang', False),
	Exit('north', 'baituo/zhuyuan', False),
]
huayuan=Room('baituo/huayuan', u'��԰', 'baituo', 0, exits)

exits = [
	Exit('south', 'baituo/xijie', False),
]
jiudian=Room('baituo/jiudian', u'�Ƶ�', None, 0, exits)

exits = [
	Exit('west', 'baituo/changlang', False),
	Exit('south', 'baituo/dating', False),
	Exit('north', 'baituo/menlang', False),
	Exit('east', 'baituo/fang', False),
]
liangong=Room('baituo/liangong', u'������', 'baituo', 0, exits)

exits = [
	Exit('south', 'baituo/liangong', False),
	Exit('north', 'baituo/huayuan', False),
]
menlang=Room('baituo/menlang', u'����', 'baituo', 0, exits)

exits = [
	Exit('east', 'city/beidajie1', False),
]
midao=Room('baituo/midao', u'�ܵ�', None, 0, exits)

exits = [
	Exit('south', 'baituo/fende', False),
]
mumen=Room('baituo/mumen', u'Ĺ��', 'baituo', 0, exits)

exits = [
	Exit('east', 'baituo/huayuan', False),
]
neishi=Room('baituo/neishi', u'����', None, 0, exits)

exits = [
	Exit('west', 'baituo/guangchang', False),
]
nongshe=Room('baituo/nongshe', u'ũ��', None, 0, exits)

exits = [
	Exit('south', 'baituo/changlang', False),
]
restroom=Room('baituo/restroom', u'��Ϣ��', None, 0, exits)

exits = [
	Exit('out', 'baituo/fang', False),
]
room1=Room('baituo/room1', u'������', None, 0, exits)

exits = [
	Exit('out', 'baituo/fang', False),
]
room2=Room('baituo/room2', u'������', None, 0, exits)

exits = [
	Exit('out', 'baituo/fang', False),
]
room3=Room('baituo/room3', u'������', None, 0, exits)

exits = [
	Exit('southeast', 'baituo/guangchang', False),
	Exit('northwest', 'baituo/shanlu1', False),
]
shanlu=Room('baituo/shanlu', u'ɽ·', 'baituo', 0, exits)

exits = [
	Exit('southeast', 'baituo/shanlu', False),
	Exit('north', 'baituo/shulin', False),
]
shanlu1=Room('baituo/shanlu1', u'ɽ·', 'baituo', 0, exits)

exits = [
	Exit('west', 'baituo/tuyuan', False),
]
sheyuan=Room('baituo/sheyuan', u'��԰', 'baituo', 0, exits)

exits = [
	Exit('southdown', 'baituo/guangchang', False),
	Exit('northup', 'baituo/damen', False),
	Exit('east', 'baituo/caoping', False),
]
shijie=Room('baituo/shijie', u'ʯ��', 'baituo', 0, exits)

exits = [
	Exit('east', 'baituo/tuyuan', False),
]
shoushe=Room('baituo/shoushe', u'����', 'baituo', 0, exits)

exits = [
	Exit('west', 'baituo/shulin1', False),
	Exit('south', 'baituo/shanlu1', False),
]
shulin=Room('baituo/shulin', u'����', 'baituo', 0, exits)

exits = [
	Exit('southwest', 'baituo/caomeide', False),
	Exit('east', 'baituo/shulin', False),
]
shulin1=Room('baituo/shulin1', u'����', 'baituo', 0, exits)

exits = [
]
storeroom=Room('baituo/storeroom', u'������', None, 0, exits)

exits = [
	Exit('west', 'baituo/shoushe', False),
	Exit('southwest', 'baituo/zhuyuan', False),
	Exit('east', 'baituo/sheyuan', False),
]
tuyuan=Room('baituo/tuyuan', u'��Է', 'baituo', 0, exits)

exits = [
	Exit('east', 'baituo/yuanzi', False),
]
wuqiku=Room('baituo/wuqiku', u'������', None, 0, exits)

exits = [
	Exit('northup', 'baituo/xiaolu2', False),
	Exit('southwest', 'baituo/dongjie', False),
	Exit('northeast', 'baituo/fende', False),
]
xiaolu1=Room('baituo/xiaolu1', u'С·', 'baituo', 0, exits)

exits = [
	Exit('southdown', 'baituo/xiaolu1', False),
	Exit('northup', 'baituo/xiaolu3', False),
]
xiaolu2=Room('baituo/xiaolu2', u'С·', 'baituo', 0, exits)

exits = [
	Exit('southdown', 'baituo/xiaolu2', False),
	Exit('northeast', 'baituo/xiaolu4', False),
]
xiaolu3=Room('baituo/xiaolu3', u'С·', 'baituo', 0, exits)

exits = [
	Exit('southwest', 'baituo/xiaolu3', False),
	Exit('north', 'baituo/dongkou', False),
]
xiaolu4=Room('baituo/xiaolu4', u'С·', 'baituo', 0, exits)

exits = [
	Exit('west', 'baituo/bridge', False),
	Exit('north', 'baituo/jiudian', False),
	Exit('east', 'baituo/dongjie', False),
]
xijie=Room('baituo/xijie', u'����', 'baituo', 0, exits)

exits = [
	Exit('west', 'baituo/cao1', False),
	Exit('east', 'baituo/changlang', False),
]
ximen=Room('baituo/ximen', u'����', 'baituo', 0, exits)

exits = [
	Exit('north', 'baituo/changlang', False),
]
yaofang=Room('baituo/yaofang', u'ҩ��', None, 0, exits)

exits = [
	Exit('west', 'baituo/wuqiku', False),
	Exit('south', 'baituo/damen', False),
	Exit('northup', 'baituo/dating', False),
]
yuanzi=Room('baituo/yuanzi', u'Ժ��', 'baituo', 0, exits)

exits = [
	Exit('west', 'baituo/liangong', False),
]
zhailuo=Room('baituo/zhailuo', u'Сլ��', 'baituo', 0, exits)

exits = [
	Exit('south', 'baituo/cao2', False),
	Exit('northup', 'baituo/cave', False),
]
zhulin=Room('baituo/zhulin', u'����', None, 0, exits)

exits = [
	Exit('northwest', 'baituo/houyuan', False),
	Exit('south', 'baituo/huayuan', False),
	Exit('northeast', 'baituo/tuyuan', False),
]
zhuyuan=Room('baituo/zhuyuan', u'��԰', 'baituo', 0, exits)

