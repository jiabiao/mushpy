# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'heimuya/chitang', False),
	Exit('north', 'heimuya/baistep2', False),
]
baihutang=Room('heimuya/baihutang', u'�׻���', None, 0, exits)

exits = [
	Exit('south', 'heimuya/baistep2', False),
	Exit('east', 'heimuya/dating2', False),
]
baistep1=Room('heimuya/baistep1', u'����', None, 0, exits)

exits = [
	Exit('south', 'heimuya/baihutang', False),
	Exit('north', 'heimuya/baistep1', False),
]
baistep2=Room('heimuya/baistep2', u'����', None, 0, exits)

exits = [
]
basket=Room('heimuya/basket', u'��¨', 'heimuya', 0, exits)

exits = [
	Exit('northwest', 'baituo/guangchang', False),
	Exit('east', 'baituo/xijie', False),
]
bridge=Room('heimuya/bridge', u'С��', 'baituo', 0, exits)

exits = [
]
changtan=Room('heimuya/changtan', u'��̲', 'heimuya', 0, exits)

exits = [
	Exit('westdown', 'heimuya/up4', False),
	Exit('north', 'heimuya/huoting', False),
]
chengdedian=Room('heimuya/chengdedian', u'�ɵµ�', None, 0, exits)

exits = [
	Exit('west', 'heimuya/shenggu', False),
	Exit('east', 'heimuya/chufang2', False),
	Exit('north', 'heimuya/baihutang', False),
]
chitang=Room('heimuya/chitang', u'����', None, 0, exits)

exits = [
	Exit('south', 'heimuya/chlang2', False),
	Exit('north', 'heimuya/dating3', False),
]
chlang1=Room('heimuya/chlang1', u'����', None, 0, exits)

exits = [
	Exit('south', 'heimuya/qing', False),
	Exit('north', 'heimuya/chlang1', False),
]
chlang2=Room('heimuya/chlang2', u'����', None, 0, exits)

exits = [
	Exit('east', 'heimuya/grass2', False),
]
chufang1=Room('heimuya/chufang1', u'����', None, 0, exits)

exits = [
	Exit('west', 'heimuya/chitang', False),
]
chufang2=Room('heimuya/chufang2', u'����', None, 0, exits)

exits = [
	Exit('south', 'heimuya/grass2', False),
	Exit('northdown', 'heimuya/linjxd5', False),
]
dating1=Room('heimuya/dating1', u'����', None, 0, exits)

exits = [
	Exit('west', 'heimuya/baistep1', False),
	Exit('east', 'heimuya/linjxd6', False),
]
dating2=Room('heimuya/dating2', u'�׻���', None, 0, exits)

exits = [
	Exit('south', 'heimuya/chlang1', False),
	Exit('northdown', 'heimuya/guang', False),
]
dating3=Room('heimuya/dating3', u'������', None, 0, exits)

exits = [
	Exit('west', 'heimuya/road1', False),
	Exit('southup', 'heimuya/tian1', False),
]
dating4=Room('heimuya/dating4', u'������', None, 0, exits)

exits = [
	Exit('west', 'heimuya/didao1', False),
	Exit('south', 'heimuya/didao5', False),
	Exit('east', 'heimuya/didao2', False),
]
didao1=Room('heimuya/didao1', u'�ص�', None, 0, exits)

exits = [
	Exit('west', 'heimuya/didao1', False),
	Exit('south', 'heimuya/didao5', False),
	Exit('down', 'heimuya/mishi', False),
]
didao2=Room('heimuya/didao2', u'�ص�', None, 0, exits)

exits = [
	Exit('west', 'heimuya/didao3', False),
	Exit('south', 'heimuya/didao1', False),
	Exit('north', 'heimuya/didao4', False),
	Exit('east', 'heimuya/didao3', False),
]
didao3=Room('heimuya/didao3', u'�ص�', None, 0, exits)

exits = [
	Exit('west', 'heimuya/didao3', False),
	Exit('southup', 'heimuya/didao6', False),
	Exit('south', 'heimuya/didao4', False),
	Exit('east', 'heimuya/didao1', False),
]
didao4=Room('heimuya/didao4', u'�ص���ͷ', None, 0, exits)

exits = [
	Exit('west', 'heimuya/didao3', False),
	Exit('south', 'heimuya/didao1', False),
	Exit('north', 'heimuya/didao2', False),
	Exit('east', 'heimuya/didao3', False),
]
didao5=Room('heimuya/didao5', u'�ص�', None, 0, exits)

exits = [
	Exit('northdown', 'heimuya/didao4', False),
	Exit('north', 'heimuya/xiaohuayuan', False),
]
didao6=Room('heimuya/didao6', u'�ص���ͷ', None, 0, exits)

exits = [
]
duchuan=Room('heimuya/duchuan', u'�ɴ�', 'heimuya', 0, exits)

exits = [
]
duchuan1=Room('heimuya/duchuan1', u'�ɴ�', 'heimuya', 0, exits)

exits = [
	Exit('northeast', 'heimuya/road4', False),
]
dukou1=Room('heimuya/dukou1', u'���Ŷɿ�', 'heimuya', 0, exits)

exits = [
	Exit('southwest', 'huanghe/weifen', False),
]
dukou2=Room('heimuya/dukou2', u'���Ŷɿ�', 'heimuya', 0, exits)

exits = [
	Exit('north', 'heimuya/grass1', False),
]
fen0=Room('heimuya/fen0', u'������', None, 0, exits)

exits = [
	Exit('south', 'heimuya/fen0', False),
	Exit('north', 'heimuya/grass2', False),
	Exit('east', 'heimuya/mudi', False),
]
grass1=Room('heimuya/grass1', u'�ݵ�', 'inn', 0, exits)

exits = [
	Exit('west', 'heimuya/chufang1', False),
	Exit('south', 'heimuya/grass1', False),
	Exit('north', 'heimuya/dating1', False),
	Exit('east', 'heimuya/hua1', False),
]
grass2=Room('heimuya/grass2', u'�ݵ�', None, 0, exits)

exits = [
	Exit('west', 'heimuya/shidao1', False),
	Exit('southup', 'heimuya/dating3', False),
	Exit('east', 'heimuya/linjxd1', False),
]
guang=Room('heimuya/guang', u'ɽ��', 'heimuya', 0, exits)

exits = [
]
house1=Room('heimuya/house1', u'����', None, 0, exits)

exits = [
	Exit('west', 'heimuya/grass2', False),
]
hua1=Room('heimuya/hua1', u'��԰', None, 0, exits)

exits = [
	Exit('west', 'heimuya/restroom', False),
	Exit('south', 'heimuya/chengdedian', False),
	Exit('east', 'heimuya/house1', False),
]
huoting=Room('heimuya/huoting', u'�ɵµ����', None, 0, exits)

exits = [
	Exit('west', 'heimuya/guang', False),
	Exit('south', 'heimuya/linjxd2', False),
	Exit('east', 'heimuya/road1', False),
	Exit('north', 'heimuya/linjxd5', False),
]
linjxd1=Room('heimuya/linjxd1', u'�ּ�С��', None, 0, exits)

exits = [
	Exit('west', 'heimuya/linjxd2', False),
	Exit('south', 'heimuya/linjxd1', False),
	Exit('east', 'heimuya/linjxd2', False),
	Exit('north', 'heimuya/linjxd3', False),
]
linjxd2=Room('heimuya/linjxd2', u'�ּ�С��', None, 0, exits)

exits = [
	Exit('west', 'heimuya/linjxd5', False),
	Exit('south', 'heimuya/linjxd4', False),
	Exit('east', 'heimuya/linjxd5', False),
	Exit('north', 'heimuya/linjxd2', False),
]
linjxd3=Room('heimuya/linjxd3', u'�ּ�С��', None, 0, exits)

exits = [
	Exit('west', 'heimuya/linjxd5', False),
	Exit('south', 'heimuya/linjxd6', False),
	Exit('east', 'heimuya/linjxd2', False),
	Exit('north', 'heimuya/linjxd1', False),
]
linjxd4=Room('heimuya/linjxd4', u'�ּ�С��', None, 0, exits)

exits = [
	Exit('west', 'heimuya/linjxd5', False),
	Exit('southup', 'heimuya/dating1', False),
	Exit('east', 'heimuya/linjxd3', False),
	Exit('north', 'heimuya/linjxd4', False),
]
linjxd5=Room('heimuya/linjxd5', u'�ּ�С��', None, 0, exits)

exits = [
	Exit('west', 'heimuya/dating2', False),
	Exit('south', 'heimuya/linjxd1', False),
	Exit('east', 'heimuya/linjxd3', False),
	Exit('north', 'heimuya/linjxd4', False),
]
linjxd6=Room('heimuya/linjxd6', u'�ּ�С��', None, 0, exits)

exits = [
	Exit('west', 'heimuya/grass1', False),
]
mudi=Room('heimuya/mudi', u'Ĺ��', None, 0, exits)

exits = [
	Exit('west', 'heimuya/xiaoshe', False),
]
neishi=Room('heimuya/neishi', u'С������', None, 0, exits)

exits = [
	Exit('west', 'heimuya/road2', False),
	Exit('east', 'heimuya/road3', False),
]
pingdingzhou=Room('heimuya/pingdingzhou', u'ƽ����', 'heimuya', 0, exits)

exits = [
	Exit('east', 'heimuya/tang', False),
	Exit('north', 'heimuya/chlang2', False),
]
qing=Room('heimuya/qing', u'�����ô���', None, 0, exits)

exits = [
	Exit('east', 'heimuya/huoting', False),
]
restroom=Room('heimuya/restroom', u'��Ϣ��', None, 0, exits)

exits = [
	Exit('west', 'heimuya/linjxd1', False),
	Exit('southwest', 'heimuya/road4', False),
	Exit('east', 'heimuya/dating4', False),
	Exit('northeast', 'heimuya/road2', False),
]
road1=Room('heimuya/road1', u'��ʯ��', 'heimuya', 0, exits)

exits = [
	Exit('southwest', 'heimuya/road1', False),
	Exit('east', 'heimuya/pingdingzhou', False),
]
road2=Room('heimuya/road2', u'����·', 'heimuya', 0, exits)

exits = [
	Exit('west', 'heimuya/pingdingzhou', False),
	Exit('east', 'beijing/ximenwai', False),
]
road3=Room('heimuya/road3', u'����·', 'heimuya', 0, exits)

exits = [
	Exit('southwest', 'heimuya/dukou1', False),
	Exit('northeast', 'heimuya/road1', False),
]
road4=Room('heimuya/road4', u'����·', 'heimuya', 0, exits)

exits = [
	Exit('south', 'heimuya/road6', False),
	Exit('northeast', 'huanghe/weifen', False),
]
road5=Room('heimuya/road5', u'����·', 'heimuya', 0, exits)

exits = [
	Exit('southeast', 'village/wexit', False),
	Exit('north', 'heimuya/road5', False),
]
road6=Room('heimuya/road6', u'����·', 'heimuya', 0, exits)

exits = [
	Exit('eastdown', 'heimuya/changtan', False),
	Exit('westup', 'heimuya/shandao2', False),
]
shandao1=Room('heimuya/shandao1', u'ɽ��', 'heimuya', 0, exits)

exits = [
	Exit('eastdown', 'heimuya/shandao1', False),
	Exit('westup', 'heimuya/shijie1', False),
]
shandao2=Room('heimuya/shandao2', u'ɽ��', 'heimuya', 0, exits)

exits = [
	Exit('east', 'heimuya/chitang', False),
]
shenggu=Room('heimuya/shenggu', u'ʥ����', None, 0, exits)

exits = [
	Exit('north', 'heimuya/shidao2', False),
	Exit('east', 'heimuya/guang', False),
]
shidao1=Room('heimuya/shidao1', u'ʯ��', 'heimuya', 0, exits)

exits = [
	Exit('south', 'heimuya/shidao1', False),
	Exit('westdown', 'heimuya/xingxingtan', False),
]
shidao2=Room('heimuya/shidao2', u'ʯ��', 'heimuya', 0, exits)

exits = [
	Exit('eastdown', 'heimuya/shandao2', False),
	Exit('westup', 'heimuya/shijie2', False),
]
shijie1=Room('heimuya/shijie1', u'ʯ��', 'heimuya', 0, exits)

exits = [
	Exit('eastdown', 'heimuya/shijie1', False),
	Exit('westup', 'heimuya/shimen', False),
]
shijie2=Room('heimuya/shijie2', u'ʯ��', 'heimuya', 0, exits)

exits = [
	Exit('eastdown', 'heimuya/shijie2', False),
	Exit('westup', 'heimuya/up1', False),
]
shimen=Room('heimuya/shimen', u'ʯ��', 'heimuya', 0, exits)

exits = [
	Exit('west', 'heimuya/qing', False),
]
tang=Room('heimuya/tang', u'������', None, 0, exits)

exits = [
	Exit('northdown', 'heimuya/dating4', False),
]
tian1=Room('heimuya/tian1', u'������', None, 0, exits)

exits = [
	Exit('eastdown', 'heimuya/shimen', False),
]
up1=Room('heimuya/up1', u'����ƺ', None, 0, exits)

exits = [
	Exit('westdown', 'heimuya/up1', False),
]
up2=Room('heimuya/up2', u'����', None, 0, exits)

exits = [
	Exit('westdown', 'heimuya/up2', False),
]
up3=Room('heimuya/up3', u'����', None, 0, exits)

exits = [
	Exit('westdown', 'heimuya/up3', False),
]
up4=Room('heimuya/up4', u'����', None, 0, exits)

exits = [
	Exit('south', 'heimuya/didao6', False),
	Exit('enter', 'heimuya/xiaoshe', False),
]
xiaohuayuan=Room('heimuya/xiaohuayuan', u'С��԰', None, 0, exits)

exits = [
	Exit('out', 'heimuya/xiaohuayuan', False),
	Exit('east', 'heimuya/neishi', False),
]
xiaoshe=Room('heimuya/xiaoshe', u'С��', None, 0, exits)

exits = [
	Exit('eastup', 'heimuya/shidao2', False),
]
xingxingtan=Room('heimuya/xingxingtan', u'����̲', 'heimuya', 0, exits)

