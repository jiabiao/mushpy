# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('east', 'beijing/road5', False),
]
bieyuan=Room('xueshan/bieyuan', u'ѩɽ��Ժ', None, 0, exits)

exits = [
	Exit('northwest', 'xueshan/dating', False),
]
cangjing=Room('xueshan/cangjing', u'�ؾ���', None, 0, exits)

exits = [
	Exit('southeast', 'xueshan/dating', False),
]
cangjingge=Room('xueshan/cangjingge', u'ѩɽ�ؾ���', None, 0, exits)

exits = [
	Exit('west', 'xueshan/tulu1', False),
	Exit('northeast', 'xingxiu/silk4', False),
]
caoyuan=Room('xueshan/caoyuan', u'��ԭ', 'xiyu', 0, exits)

exits = [
	Exit('west', 'xueshan/dadian', False),
	Exit('north', 'xueshan/zoulang1', False),
]
cedian1=Room('xueshan/cedian1', u'���', None, 0, exits)

exits = [
	Exit('east', 'xueshan/dadian', False),
	Exit('north', 'xueshan/zoulang2', False),
]
cedian2=Room('xueshan/cedian2', u'���', None, 0, exits)

exits = [
	Exit('west', 'xueshan/kufang', False),
	Exit('south', 'xueshan/jitan', False),
	Exit('north', 'xueshan/chang3', False),
	Exit('east', 'xueshan/chang2', False),
]
chang=Room('xueshan/chang', u'�����䳡', 'xueshan', 0, exits)

exits = [
	Exit('west', 'xueshan/chang', False),
	Exit('east', 'xueshan/guangchang', False),
]
chang2=Room('xueshan/chang2', u'�����䳡', 'xueshan', 0, exits)

exits = [
	Exit('south', 'xueshan/chang', False),
	Exit('north', 'xueshan/houyuan', False),
]
chang3=Room('xueshan/chang3', u'С���䳡', 'xueshan', 0, exits)

exits = [
	Exit('southwest', 'xueshan/dating', False),
]
chanshi=Room('xueshan/chanshi', u'����', None, 0, exits)

exits = [
	Exit('south', 'xueshan/xiaoyuan', False),
]
chufang=Room('xueshan/chufang', u'����', None, 0, exits)

exits = [
	Exit('west', 'xueshan/cedian2', False),
	Exit('south', 'xueshan/guangchang', False),
	Exit('east', 'xueshan/cedian1', False),
]
dadian=Room('xueshan/dadian', u'���', None, 0, exits)

exits = [
	Exit('southeast', 'xueshan/cangjing', False),
	Exit('west', 'xueshan/zoulang2', False),
	Exit('north', 'xueshan/cangjingge', False),
	Exit('northeast', 'xueshan/chanshi', False),
	Exit('east', 'xueshan/zoulang1', False),
]
dating=Room('xueshan/dating', u'����', None, 0, exits)

exits = [
	Exit('westup', 'xueshan/houyuan', False),
]
dilao=Room('xueshan/dilao', u'����', None, 0, exits)

exits = [
	Exit('west', 'xueshan/chang', False),
	Exit('south', 'xueshan/shanmen', False),
	Exit('north', 'xueshan/dadian', False),
	Exit('east', 'xueshan/xiaoyuan', False),
]
guangcha=Room('xueshan/guangcha', u'�㳡', 'xueshan', 0, exits)

exits = [
	Exit('west', 'xueshan/chang2', False),
	Exit('south', 'xueshan/shanmen', False),
	Exit('north', 'xueshan/dadian', False),
	Exit('east', 'xueshan/xiaoyuan', False),
]
guangchang=Room('xueshan/guangchang', u'�㳡', 'xueshan', 0, exits)

exits = [
	Exit('south', 'xueshan/neidian', False),
]
houdian=Room('xueshan/houdian', u'���', None, 0, exits)

exits = [
	Exit('south', 'xueshan/houyuan', False),
]
houmen=Room('xueshan/houmen', u'����', None, 0, exits)

exits = [
	Exit('south', 'xueshan/chang3', False),
	Exit('eastdown', 'xueshan/dilao', False),
	Exit('north', 'xueshan/houmen', False),
]
houyuan=Room('xueshan/houyuan', u'��Ժ', 'xueshan', 0, exits)

exits = [
	Exit('west', 'xueshan/shenghu', False),
	Exit('east', 'xueshan/hubian2', False),
]
hubian1=Room('xueshan/hubian1', u'����С·', 'xueshan', 0, exits)

exits = [
	Exit('west', 'xueshan/hubian1', False),
	Exit('northeast', 'xueshan/hubian3', False),
]
hubian2=Room('xueshan/hubian2', u'����С·', 'xueshan', 0, exits)

exits = [
	Exit('southwest', 'xueshan/hubian2', False),
	Exit('north', 'xueshan/hubian4', False),
]
hubian3=Room('xueshan/hubian3', u'����С·', 'xueshan', 0, exits)

exits = [
	Exit('south', 'xueshan/hubian3', False),
	Exit('north', 'xueshan/shanjiao', False),
]
hubian4=Room('xueshan/hubian4', u'����С·', 'xueshan', 0, exits)

exits = [
	Exit('north', 'xueshan/chang', False),
]
jitan=Room('xueshan/jitan', u'ѩɽ��̳', 'xueshan', 1, exits)

exits = [
	Exit('east', 'xueshan/tulu2', False),
]
kedian=Room('xueshan/kedian', u'�͵�', None, 0, exits)

exits = [
	Exit('east', 'xueshan/chang', False),
]
kufang=Room('xueshan/kufang', u'�ⷿ', None, 0, exits)

exits = [
	Exit('east', 'xueshan/neidian', False),
	Exit('north', 'xueshan/mishi', False),
]
midao=Room('xueshan/midao', u'�ܵ�', None, 0, exits)

exits = [
	Exit('south', 'xueshan/midao', False),
	Exit('down', 'city/xsmidao5', False),
]
mishi=Room('xueshan/mishi', u'����', None, 0, exits)

exits = [
	Exit('west', 'xueshan/midao', False),
	Exit('south', 'xueshan/zoulang3', False),
	Exit('north', 'xueshan/houdian', False),
	Exit('east', 'xueshan/tiantai', False),
]
neidian=Room('xueshan/neidian', u'�ڵ�', None, 0, exits)

exits = [
	Exit('south', 'xueshan/hubian4', False),
	Exit('westup', 'xuedao/nroad7', False),
]
shanjiao=Room('xueshan/shanjiao', u'ɽ��', 'xueshan', 0, exits)

exits = [
	Exit('eastdown', 'xuedao/nroad4', False),
	Exit('north', 'xueshan/guangchang', False),
]
shanmen=Room('xueshan/shanmen', u'ѩɽ��ɽ��', 'xueshan', 0, exits)

exits = [
	Exit('south', 'xueshan/tulu3', False),
	Exit('east', 'xueshan/hubian1', False),
]
shenghu=Room('xueshan/shenghu', u'ʥ��', 'xueshan', 0, exits)

exits = [
	Exit('west', 'xueshan/neidian', False),
]
tiantai=Room('xueshan/tiantai', u'��̨', None, 0, exits)

exits = [
	Exit('west', 'xueshan/tulu2', False),
	Exit('east', 'xueshan/caoyuan', False),
]
tulu1=Room('xueshan/tulu1', u'��·', 'xueshan', 0, exits)

exits = [
	Exit('west', 'xueshan/kedian', False),
	Exit('north', 'xueshan/tulu3', False),
	Exit('east', 'xueshan/tulu1', False),
]
tulu2=Room('xueshan/tulu2', u'��·', 'xueshan', 0, exits)

exits = [
	Exit('south', 'xueshan/tulu2', False),
	Exit('north', 'xueshan/shenghu', False),
]
tulu3=Room('xueshan/tulu3', u'��·', 'xueshan', 0, exits)

exits = [
	Exit('west', 'xueshan/guangchang', False),
	Exit('north', 'xueshan/chufang', False),
]
xiaoyuan=Room('xueshan/xiaoyuan', u'СԺ', 'xueshan', 0, exits)

exits = [
	Exit('west', 'xueshan/dating', False),
	Exit('northwest', 'xueshan/zoulang3', False),
	Exit('south', 'xueshan/cedian1', False),
]
zoulang1=Room('xueshan/zoulang1', u'����', None, 0, exits)

exits = [
	Exit('south', 'xueshan/cedian2', False),
	Exit('northeast', 'xueshan/zoulang3', False),
	Exit('east', 'xueshan/dating', False),
]
zoulang2=Room('xueshan/zoulang2', u'����', None, 0, exits)

exits = [
	Exit('eastdown', 'xueshan/zoulang1', False),
	Exit('westdown', 'xueshan/zoulang2', False),
	Exit('north', 'xueshan/neidian', False),
]
zoulang3=Room('xueshan/zoulang3', u'����', None, 0, exits)

