# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('southeast', 'city3/northroad1', False),
]
bingqidian=Room('city3/bingqidian', u'������', None, 0, exits)

exits = [
	Exit('south', 'city3/path2', False),
]
caotang=Room('city3/caotang', u'�Ÿ�����', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/jiudian', False),
]
chufang=Room('city3/chufang', u'��¥����', None, 0, exits)

exits = [
	Exit('west', 'city3/eastroad2', False),
	Exit('east', 'city3/fuheqiaoe', False),
]
eastgate=Room('city3/eastgate', u'����', 'chengdu', 0, exits)

exits = [
	Exit('northwest', 'city3/northroad3', False),
	Exit('south', 'city3/eastroad2', False),
	Exit('northeast', 'city3/jiudian', False),
]
eastroad1=Room('city3/eastroad1', u'�����', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/shuduroad1', False),
	Exit('south', 'city3/eastroad3', False),
	Exit('north', 'city3/eastroad1', False),
	Exit('east', 'city3/eastgate', False),
]
eastroad2=Room('city3/eastroad2', u'�����', 'chengdu', 0, exits)

exits = [
	Exit('southeast', 'city3/wangjianglou', False),
	Exit('southwest', 'city3/southroad1', False),
	Exit('north', 'city3/eastroad2', False),
]
eastroad3=Room('city3/eastroad3', u'�����', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/eastgate', False),
	Exit('east', 'city3/road2', False),
]
fuheqiaoe=Room('city3/fuheqiaoe', u'������', 'chengdu', 0, exits)

exits = [
	Exit('south', 'city3/northgate', False),
	Exit('north', 'qingcheng/qcroad1', False),
]
fuheqiaon=Room('city3/fuheqiaon', u'������', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/shuduroad2', False),
	Exit('south', 'city3/tiduroad', False),
	Exit('north', 'city3/tidugate', False),
	Exit('east', 'city3/shuduroad1', False),
]
guangchang=Room('city3/guangchang', u'�㳡', 'chengdu', 0, exits)

exits = [
	Exit('southwest', 'city3/eastroad1', False),
	Exit('east', 'city3/chufang', False),
]
jiudian=Room('city3/jiudian', u'�سǾ�¥', None, 0, exits)

exits = [
	Exit('northwest', 'city3/southroad1', False),
	Exit('east', 'city3/majiu', False),
	Exit('up', 'city3/kedian2', False),
]
kedian=Room('city3/kedian', u'������', None, 0, exits)

exits = [
	Exit('down', 'city3/kedian', False),
]
kedian2=Room('city3/kedian2', u'�͵��¥', None, 0, exits)

exits = [
	Exit('northup', 'city3/wuhouci', False),
	Exit('south', 'city3/wuhoucigate', False),
]
liubeidian=Room('city3/liubeidian', u'������', None, 0, exits)

exits = [
	Exit('west', 'city3/kedian', False),
]
majiu=Room('city3/majiu', u'���', 'city3', 0, exits)

exits = [
	Exit('south', 'xuedao/sroad1', False),
	Exit('north', 'city3/southgate', False),
]
nanheqiaos=Room('city3/nanheqiaos', u'�Ϻ���', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/path1', False),
	Exit('east', 'city3/westgate', False),
]
nanheqiaow=Room('city3/nanheqiaow', u'�Ϻ���', 'chengdu', 0, exits)

exits = [
	Exit('south', 'city3/northroad2', False),
	Exit('north', 'city3/fuheqiaon', False),
]
northgate=Room('city3/northgate', u'������', 'chengdu', 0, exits)

exits = [
	Exit('northwest', 'city3/bingqidian', False),
	Exit('southwest', 'city3/westroad3', False),
	Exit('east', 'city3/northroad2', False),
]
northroad1=Room('city3/northroad1', u'�����', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/northroad1', False),
	Exit('south', 'city3/tanggate', False),
	Exit('north', 'city3/northgate', False),
	Exit('east', 'city3/northroad3', False),
]
northroad2=Room('city3/northroad2', u'�����', 'chengdu', 0, exits)

exits = [
	Exit('southeast', 'city3/eastroad1', False),
	Exit('west', 'city3/northroad2', False),
	Exit('northeast', 'city3/wuguan', False),
]
northroad3=Room('city3/northroad3', u'�����', 'chengdu', 0, exits)

exits = [
	Exit('east', 'city3/nanheqiaow', False),
	Exit('north', 'city3/path2', False),
]
path1=Room('city3/path1', u'佻�Ϫ', 'chengdu', 0, exits)

exits = [
	Exit('south', 'city3/path1', False),
	Exit('north', 'city3/caotang', False),
]
path2=Room('city3/path2', u'佻�Ϫ', 'chengdu', 0, exits)

exits = [
	Exit('down', 'city3/wuguan', False),
]
practice=Room('city3/practice', u'��ݲ�����', None, 0, exits)

exits = [
	Exit('northeast', 'city3/westroad1', False),
]
qingyanggong=Room('city3/qingyanggong', u'����', None, 0, exits)

exits = [
	Exit('northwest', 'city3/road2', False),
	Exit('east', 'emei/qsjie1', False),
]
road1=Room('city3/road1', u'��ʯ���', 'emei', 0, exits)

exits = [
	Exit('west', 'city3/fuheqiaoe', False),
	Exit('southeast', 'city3/road1', False),
]
road2=Room('city3/road2', u'��ʯ���', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/guangchang', False),
	Exit('east', 'city3/eastroad2', False),
]
shuduroad1=Room('city3/shuduroad1', u'�񶼵�', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/westroad2', False),
	Exit('east', 'city3/guangchang', False),
]
shuduroad2=Room('city3/shuduroad2', u'�񶼵�', 'chengdu', 0, exits)

exits = [
	Exit('south', 'city3/nanheqiaos', False),
	Exit('north', 'city3/southroad2', False),
]
southgate=Room('city3/southgate', u'�ϳ���', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/southroad2', False),
	Exit('southeast', 'city3/kedian', False),
	Exit('northeast', 'city3/eastroad3', False),
]
southroad1=Room('city3/southroad1', u'�ϴ��', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/southroad3', False),
	Exit('south', 'city3/southgate', False),
	Exit('east', 'city3/southroad1', False),
	Exit('north', 'city3/tiduroad', False),
]
southroad2=Room('city3/southroad2', u'�ϴ��', 'chengdu', 0, exits)

exits = [
	Exit('northwest', 'city3/westroad1', False),
	Exit('southwest', 'city3/wuhoucigate', False),
	Exit('east', 'city3/southroad2', False),
]
southroad3=Room('city3/southroad3', u'�ϴ��', 'chengdu', 0, exits)

exits = [
	Exit('north', 'city3/northroad2', False),
]
tanggate=Room('city3/tanggate', u'���Ŵ���', 'chengdu', 0, exits)

exits = [
	Exit('south', 'city3/tidugate', False),
]
tidufu=Room('city3/tidufu', u'�ᶽ��', None, 0, exits)

exits = [
	Exit('south', 'city3/guangchang', False),
	Exit('north', 'city3/tidufu', False),
]
tidugate=Room('city3/tidugate', u'�ᶽ����', 'chengdu', 0, exits)

exits = [
	Exit('south', 'city3/southroad2', False),
	Exit('north', 'city3/guangchang', False),
]
tiduroad=Room('city3/tiduroad', u'�ᶽ��', 'chengdu', 0, exits)

exits = [
	Exit('northwest', 'city3/eastroad3', False),
]
wangjianglou=Room('city3/wangjianglou', u'����¥', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/nanheqiaow', False),
	Exit('east', 'city3/westroad2', False),
]
westgate=Room('city3/westgate', u'����', 'chengdu', 0, exits)

exits = [
	Exit('southeast', 'city3/southroad3', False),
	Exit('southwest', 'city3/qingyanggong', False),
	Exit('north', 'city3/westroad2', False),
]
westroad1=Room('city3/westroad1', u'�����', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/westgate', False),
	Exit('south', 'city3/westroad1', False),
	Exit('north', 'city3/westroad3', False),
	Exit('east', 'city3/shuduroad2', False),
]
westroad2=Room('city3/westroad2', u'�����', 'chengdu', 0, exits)

exits = [
	Exit('northwest', 'city3/yaodian', False),
	Exit('south', 'city3/westroad2', False),
	Exit('northeast', 'city3/northroad1', False),
]
westroad3=Room('city3/westroad3', u'�����', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/wuguanxiao', False),
	Exit('south', 'city3/wuguanlong', False),
	Exit('southwest', 'city3/northroad3', False),
	Exit('up', 'city3/practice', False),
	Exit('north', 'city3/wuguanliu', False),
	Exit('east', 'city3/wuguanchen', False),
	Exit('down', 'city3/wuxiuxi', False),
]
wuguan=Room('city3/wuguan', u'��ţ���', None, 0, exits)

exits = [
	Exit('west', 'city3/wuguan', False),
]
wuguanchen=Room('city3/wuguanchen', u'��ţ���һ��', None, 0, exits)

exits = [
	Exit('south', 'city3/wuguan', False),
]
wuguanliu=Room('city3/wuguanliu', u'��ţ����Ĳ�', None, 0, exits)

exits = [
	Exit('north', 'city3/wuguan', False),
]
wuguanlong=Room('city3/wuguanlong', u'��ţ��ݶ���', None, 0, exits)

exits = [
	Exit('east', 'city3/wuguan', False),
]
wuguanxiao=Room('city3/wuguanxiao', u'��ţ�������', None, 0, exits)

exits = [
	Exit('southdown', 'city3/liubeidian', False),
]
wuhouci=Room('city3/wuhouci', u'�������', None, 0, exits)

exits = [
	Exit('north', 'city3/liubeidian', False),
	Exit('northeast', 'city3/southroad3', False),
]
wuhoucigate=Room('city3/wuhoucigate', u'���������', 'chengdu', 0, exits)

exits = [
	Exit('up', 'city3/wuguan', False),
]
wuxiuxi=Room('city3/wuxiuxi', u'��ţ��ݵ�����', None, 0, exits)

exits = [
	Exit('southeast', 'city3/westroad3', False),
]
yaodian=Room('city3/yaodian', u'������ҩ��', None, 0, exits)

