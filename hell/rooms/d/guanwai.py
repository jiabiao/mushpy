# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('west', 'guanwai/caoguduo', False),
	Exit('north', 'guanwai/xiaoyuan', False),
	Exit('east', 'guanwai/milin1', False),
]
baihe=Room('guanwai/baihe', u'�׺�', 'guanwai', 0, exits)

exits = [
	Exit('eastdown', 'guanwai/tianchi1', False),
	Exit('southwest', 'guanwai/yuzhu', False),
	Exit('north', 'guanwai/luming', False),
]
baiyun=Room('guanwai/baiyun', u'���Ʒ�', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/xiaoxiang', False),
	Exit('south', 'guanwai/jishi', False),
]
beicheng=Room('guanwai/beicheng', u'����', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/chuanchang', False),
	Exit('east', 'guanwai/damenkan', False),
]
bingmian=Room('guanwai/bingmian', u'����', 'guanwai', 0, exits)

exits = [
	Exit('northwest', 'guanwai/mantianxing', False),
	Exit('east', 'guanwai/baihe', False),
]
caoguduo=Room('guanwai/caoguduo', u'�Ȳݶ�', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/xuedi3', False),
	Exit('east', 'guanwai/bingmian', False),
]
chuanchang=Room('guanwai/chuanchang', u'����', 'guanwai', 0, exits)

exits = [
	Exit('east', 'guanwai/shizilu', False),
]
chufang=Room('guanwai/chufang', u'����', None, 0, exits)

exits = [
	Exit('northwest', 'guanwai/pubu', False),
	Exit('southwest', 'guanwai/longmen', False),
]
damen=Room('guanwai/damen', u'����', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/bingmian', False),
	Exit('southeast', 'guanwai/ermenkan', False),
]
damenkan=Room('guanwai/damenkan', u'���ſ���', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/jishi', False),
	Exit('south', 'guanwai/tuyaoguan', False),
	Exit('northeast', 'guanwai/huandi1', False),
	Exit('east', 'guanwai/xuedi1', False),
]
dongcheng=Room('guanwai/dongcheng', u'����', 'guanwai', 0, exits)

exits = [
	Exit('northwest', 'guanwai/damenkan', False),
	Exit('east', 'guanwai/mantianxing', False),
]
ermenkan=Room('guanwai/ermenkan', u'���ſ���', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/famu1', False),
	Exit('southup', 'guanwai/luming', False),
]
famu=Room('guanwai/famu', u'��ľ��', 'guanwai', 0, exits)

exits = [
	Exit('east', 'guanwai/famu', False),
]
famu1=Room('guanwai/famu1', u'��ľ��', 'guanwai', 0, exits)

exits = [
	Exit('westdown', 'guanwai/milin3', False),
	Exit('east', 'guanwai/xiaotianchi', False),
]
heifengkou=Room('guanwai/heifengkou', u'�ڷ��', None, 0, exits)

exits = [
	Exit('west', 'guanwai/jingxiu', False),
	Exit('south', 'guanwai/xiaowu', False),
	Exit('east', 'guanwai/liangong', False),
	Exit('north', 'guanwai/shizilu', False),
]
houyuan=Room('guanwai/houyuan', u'��Ժ', None, 0, exits)

exits = [
	Exit('westdown', 'guanwai/tianchi1', False),
	Exit('north', 'guanwai/tianhuo', False),
]
huagai=Room('guanwai/huagai', u'���Ƿ�', 'guanwai', 0, exits)

exits = [
	Exit('southwest', 'guanwai/dongcheng', False),
	Exit('northeast', 'guanwai/huandi2', False),
]
huandi1=Room('guanwai/huandi1', u'��·', 'guanwai', 0, exits)

exits = [
	Exit('southwest', 'guanwai/huandi1', False),
	Exit('enter', 'guanwai/shanshenmiao', False),
]
huandi2=Room('guanwai/huandi2', u'��·', 'guanwai', 0, exits)

exits = [
	Exit('east', 'guanwai/houyuan', False),
]
jingxiu=Room('guanwai/jingxiu', u'������', None, 0, exits)

exits = [
	Exit('west', 'guanwai/kedian', False),
	Exit('south', 'guanwai/nancheng', False),
	Exit('east', 'guanwai/dongcheng', False),
	Exit('north', 'guanwai/beicheng', False),
]
jishi=Room('guanwai/jishi', u'����', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/majiu', False),
	Exit('up', 'guanwai/kedian2', False),
	Exit('east', 'guanwai/jishi', False),
]
kedian=Room('guanwai/kedian', u'�͵�', None, 0, exits)

exits = [
	Exit('down', 'guanwai/kedian', False),
]
kedian2=Room('guanwai/kedian2', u'�͵��¥', None, 0, exits)

exits = [
	Exit('northwest', 'guanwai/shanhaiguan', False),
	Exit('southwest', 'beijing/road3', False),
]
laolongtou=Room('guanwai/laolongtou', u'����ͷ', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/houyuan', False),
	Exit('south', 'guanwai/liangongs', False),
	Exit('east', 'guanwai/liangonge', False),
]
liangong=Room('guanwai/liangong', u'������', None, 0, exits)

exits = [
	Exit('west', 'guanwai/liangong', False),
]
liangonge=Room('guanwai/liangonge', u'��������', None, 0, exits)

exits = [
	Exit('north', 'guanwai/liangong', False),
]
liangongs=Room('guanwai/liangongs', u'��������', None, 0, exits)

exits = [
	Exit('southdown', 'guanwai/tianchi1', False),
	Exit('west', 'guanwai/luming', False),
	Exit('east', 'guanwai/tianhuo', False),
	Exit('northeast', 'guanwai/damen', False),
]
longmen=Room('guanwai/longmen', u'���ŷ�', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/baiyun', False),
	Exit('northdown', 'guanwai/famu', False),
	Exit('east', 'guanwai/longmen', False),
]
luming=Room('guanwai/luming', u'¹����', 'guanwai', 0, exits)

exits = [
	Exit('east', 'guanwai/kedian', False),
]
majiu=Room('guanwai/majiu', u'���', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/ermenkan', False),
	Exit('southeast', 'guanwai/caoguduo', False),
]
mantianxing=Room('guanwai/mantianxing', u'������', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/baihe', False),
	Exit('eastup', 'guanwai/milin2', False),
]
milin1=Room('guanwai/milin1', u'����', 'guanwai', 0, exits)

exits = [
	Exit('southup', 'guanwai/milin3', False),
	Exit('westdown', 'guanwai/milin1', False),
]
milin2=Room('guanwai/milin2', u'����', 'guanwai', 0, exits)

exits = [
	Exit('eastup', 'guanwai/heifengkou', False),
	Exit('northdown', 'guanwai/milin2', False),
]
milin3=Room('guanwai/milin3', u'����', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/road8', False),
	Exit('north', 'guanwai/nancheng', False),
]
muqiao=Room('guanwai/muqiao', u'ľ��', 'guanwai', 0, exits)

exits = [
	Exit('southeast', 'guanwai/tulu', False),
	Exit('west', 'guanwai/rouguan', False),
	Exit('south', 'guanwai/muqiao', False),
	Exit('north', 'guanwai/jishi', False),
]
nancheng=Room('guanwai/nancheng', u'�ϳ�', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/road3', False),
	Exit('northeast', 'guanwai/road4', False),
]
ningyuan=Room('guanwai/ningyuan', u'��Զ', 'guanwai', 0, exits)

exits = [
	Exit('southeast', 'guanwai/damen', False),
	Exit('westdown', 'guanwai/xiaotianchi', False),
]
pubu=Room('guanwai/pubu', u'�����ٲ�', 'guanwai', 0, exits)

exits = [
	Exit('southwest', 'guanwai/shanhaiguan', False),
	Exit('northeast', 'guanwai/road2', False),
]
road1=Room('guanwai/road1', u'�ٵ�', 'guanwai', 0, exits)

exits = [
	Exit('southwest', 'guanwai/road1', False),
	Exit('northeast', 'guanwai/road3', False),
]
road2=Room('guanwai/road2', u'�ٵ�', 'guanwai', 0, exits)

exits = [
	Exit('southwest', 'guanwai/road2', False),
	Exit('north', 'guanwai/ningyuan', False),
]
road3=Room('guanwai/road3', u'�ٵ�', 'guanwai', 0, exits)

exits = [
	Exit('southwest', 'guanwai/ningyuan', False),
	Exit('northeast', 'guanwai/road5', False),
]
road4=Room('guanwai/road4', u'���', 'guanwai', 0, exits)

exits = [
	Exit('southwest', 'guanwai/road4', False),
	Exit('north', 'guanwai/road6', False),
]
road5=Room('guanwai/road5', u'���', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/road5', False),
	Exit('north', 'guanwai/road7', False),
]
road6=Room('guanwai/road6', u'���', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/road6', False),
	Exit('north', 'guanwai/road8', False),
]
road7=Room('guanwai/road7', u'���', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/road7', False),
	Exit('north', 'guanwai/muqiao', False),
]
road8=Room('guanwai/road8', u'���', 'guanwai', 0, exits)

exits = [
	Exit('east', 'guanwai/nancheng', False),
]
rouguan=Room('guanwai/rouguan', u'�����', None, 0, exits)

exits = [
	Exit('southeast', 'guanwai/laolongtou', False),
	Exit('northeast', 'guanwai/road1', False),
]
shanhaiguan=Room('guanwai/shanhaiguan', u'ɽ����', 'guanwai', 0, exits)

exits = [
	Exit('out', 'guanwai/huandi2', False),
]
shanshenmiao=Room('guanwai/shanshenmiao', u'ɽ����', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/tulu', False),
]
shichang=Room('guanwai/shichang', u'��ʯ��', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/chufang', False),
	Exit('south', 'guanwai/houyuan', False),
	Exit('east', 'guanwai/taxue', False),
]
shizilu=Room('guanwai/shizilu', u'ʯ·', None, 0, exits)

exits = [
]
songhuajiang=Room('guanwai/songhuajiang', u'�ɻ�����', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/shizilu', False),
]
taxue=Room('guanwai/taxue', u'̤ѩԺ', None, 0, exits)

exits = [
	Exit('eastup', 'guanwai/huagai', False),
	Exit('northup', 'guanwai/longmen', False),
	Exit('south', 'guanwai/tianchi2', False),
	Exit('westup', 'guanwai/baiyun', False),
]
tianchi1=Room('guanwai/tianchi1', u'��ͷɽ���', 'guanwai', 0, exits)

exits = [
	Exit('north', 'guanwai/tianchi1', False),
]
tianchi2=Room('guanwai/tianchi2', u'��ͷɽ���', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/longmen', False),
	Exit('south', 'guanwai/huagai', False),
]
tianhuo=Room('guanwai/tianhuo', u'����', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/yuzhu', False),
]
tiyun=Room('guanwai/tiyun', u'���Ʒ�', 'guanwai', 0, exits)

exits = [
	Exit('northwest', 'guanwai/nancheng', False),
	Exit('east', 'guanwai/shichang', False),
]
tulu=Room('guanwai/tulu', u'��·', 'guanwai', 0, exits)

exits = [
	Exit('north', 'guanwai/xiaoxiang', False),
]
tuwu=Room('guanwai/tuwu', u'С����', 'guanwai', 0, exits)

exits = [
	Exit('north', 'guanwai/dongcheng', False),
]
tuyaoguan=Room('guanwai/tuyaoguan', u'��Ҥ��', None, 0, exits)

exits = [
	Exit('west', 'guanwai/heifengkou', False),
	Exit('eastup', 'guanwai/pubu', False),
]
xiaotianchi=Room('guanwai/xiaotianchi', u'С���', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/xiaoyuan', False),
	Exit('north', 'guanwai/houyuan', False),
]
xiaowu=Room('guanwai/xiaowu', u'Сé��', None, 0, exits)

exits = [
	Exit('south', 'guanwai/tuwu', False),
	Exit('east', 'guanwai/beicheng', False),
]
xiaoxiang=Room('guanwai/xiaoxiang', u'С��', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/baihe', False),
	Exit('north', 'guanwai/xiaowu', False),
]
xiaoyuan=Room('guanwai/xiaoyuan', u'СԺ��', None, 0, exits)

exits = [
]
xiuxishi=Room('guanwai/xiuxishi', u'��Ϣ��', None, 0, exits)

exits = [
	Exit('west', 'guanwai/dongcheng', False),
	Exit('northeast', 'guanwai/xuedi2', False),
]
xuedi1=Room('guanwai/xuedi1', u'ѩ��', 'guanwai', 0, exits)

exits = [
	Exit('southwest', 'guanwai/xuedi1', False),
	Exit('east', 'guanwai/xuedi3', False),
]
xuedi2=Room('guanwai/xuedi2', u'ѩ��', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/xuedi2', False),
	Exit('north', 'guanwai/chuanchang', False),
]
xuedi3=Room('guanwai/xuedi3', u'ѩ��', 'guanwai', 0, exits)

exits = [
	Exit('northeast', 'guanwai/baiyun', False),
	Exit('north', 'guanwai/tiyun', False),
]
yuzhu=Room('guanwai/yuzhu', u'������', 'guanwai', 0, exits)

