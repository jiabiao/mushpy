# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('northup', 'gumu/shanlu6', False),
]
baimatang=Room('gumu/baimatang', u'����̶', 'gumu', 0, exits)

exits = [
	Exit('west', 'gumu/shulin8', False),
	Exit('south', 'gumu/shulin9', False),
]
baoziyan=Room('gumu/baoziyan', u'������', 'gumu', 0, exits)

exits = [
	Exit('south', 'gumu/mumen', False),
	Exit('north', 'gumu/shulin3', False),
	Exit('east', 'gumu/caodi2', False),
]
caodi=Room('gumu/caodi', u'�ݵ�', 'gumu', 0, exits)

exits = [
	Exit('southeast', 'gumu/hanshuitan', False),
	Exit('west', 'gumu/caodi', False),
]
caodi2=Room('gumu/caodi2', u'�ݵ�', 'gumu', 0, exits)

exits = [
	Exit('southup', 'gumu/shanlu7', False),
]
caotangsi=Room('gumu/caotangsi', u'������', 'gumu', 0, exits)

exits = [
	Exit('southdown', 'gumu/daxiaochang', False),
]
chongyanggate=Room('gumu/chongyanggate', u'����������', 'gumu', 0, exits)

exits = [
	Exit('southdown', 'gumu/shanlu8', False),
	Exit('northup', 'quanzhen/shijie1', False),
	Exit('westup', 'gumu/shanlu7', False),
]
daxiaochang=Room('gumu/daxiaochang', u'��У��', 'gumu', 0, exits)

exits = [
	Exit('east', 'gumu/shenheyuan', False),
]
foyezhang=Room('gumu/foyezhang', u'��ү��', 'gumu', 0, exits)

exits = [
	Exit('northwest', 'gumu/caodi2', False),
]
hanshuitan=Room('gumu/hanshuitan', u'��ˮ̶', 'gumu', 0, exits)

exits = [
	Exit('westup', 'gumu/shulin7', False),
]
heifengdong=Room('gumu/heifengdong', u'�ڷﶴ', 'gumu', 0, exits)

exits = [
	Exit('north', 'gumu/zhengting', False),
]
houting=Room('gumu/houting', u'����', None, 0, exits)

exits = [
	Exit('east', 'gumu/mumen', False),
]
huangshalin=Room('gumu/huangshalin', u'��ɳ��', 'gumu', 0, exits)

exits = [
	Exit('southdown', 'gumu/shanlu11', False),
	Exit('westup', 'gumu/shanlu10', False),
]
jinliange=Room('gumu/jinliange', u'������', 'gumu', 0, exits)

exits = [
	Exit('southdown', 'gumu/shulin7', False),
	Exit('northup', 'gumu/shanlu8', False),
]
juyan=Room('gumu/juyan', u'������', 'gumu', 0, exits)

exits = [
	Exit('west', 'gumu/shulin5', False),
	Exit('northup', 'gumu/shanlu1', False),
	Exit('south', 'gumu/shulin4', False),
]
kongdi=Room('gumu/kongdi', u'�յ�', 'gumu', 0, exits)

exits = [
	Exit('south', 'gumu/liangong2', False),
	Exit('east', 'gumu/zhengting', False),
]
liangong=Room('gumu/liangong', u'��������', None, 0, exits)

exits = [
	Exit('south', 'gumu/liangong3', False),
	Exit('north', 'gumu/liangong', False),
]
liangong2=Room('gumu/liangong2', u'��������', None, 0, exits)

exits = [
	Exit('north', 'gumu/liangong2', False),
]
liangong3=Room('gumu/liangong3', u'С������', None, 0, exits)

exits = [
	Exit('up', 'gumu/hanshuitan', False),
]
mishi1=Room('gumu/mishi1', u'����', None, 0, exits)

exits = [
	Exit('up', 'gumu/houting', False),
	Exit('east', 'gumu/mishi3', False),
]
mishi2=Room('gumu/mishi2', u'����', None, 0, exits)

exits = [
	Exit('west', 'gumu/mishi2', False),
	Exit('south', 'gumu/mishi6', False),
	Exit('north', 'gumu/mishi5', False),
	Exit('east', 'gumu/mishi4', False),
]
mishi3=Room('gumu/mishi3', u'����', None, 0, exits)

exits = [
	Exit('west', 'gumu/mishi3', False),
]
mishi4=Room('gumu/mishi4', u'����', None, 0, exits)

exits = [
	Exit('south', 'gumu/mishi3', False),
]
mishi5=Room('gumu/mishi5', u'����', None, 0, exits)

exits = [
	Exit('south', 'gumu/mishi7', False),
	Exit('north', 'gumu/mishi3', False),
]
mishi6=Room('gumu/mishi6', u'����', None, 0, exits)

exits = [
	Exit('north', 'gumu/mishi6', False),
	Exit('east', 'gumu/mishi8', False),
]
mishi7=Room('gumu/mishi7', u'����', None, 0, exits)

exits = [
	Exit('out', 'city/guangchang', False),
	Exit('west', 'gumu/mishi7', False),
]
mishi8=Room('gumu/mishi8', u'����', None, 0, exits)

exits = [
	Exit('west', 'gumu/huangshalin', False),
	Exit('north', 'gumu/caodi', False),
]
mumen=Room('gumu/mumen', u'Ĺ��', 'gumu', 0, exits)

exits = [
	Exit('west', 'gumu/shanlu13', False),
]
puguangsi=Room('gumu/puguangsi', u'�չ���', 'gumu', 0, exits)

exits = [
	Exit('south', 'gumu/xiaoting', False),
	Exit('north', 'gumu/mumen', False),
]
qianting=Room('gumu/qianting', u'ǰ��', None, 0, exits)

exits = [
	Exit('northup', 'gumu/shanlu9', False),
	Exit('eastdown', 'gumu/shanlu10', False),
]
riyueyan=Room('gumu/riyueyan', u'������', 'gumu', 0, exits)

exits = [
	Exit('southeast', 'gumu/shanlu7', False),
	Exit('northdown', 'gumu/shandao2', False),
]
shandao1=Room('gumu/shandao1', u'ɽ��', 'gumu', 0, exits)

exits = [
	Exit('southup', 'gumu/shandao1', False),
	Exit('northdown', 'gumu/shulin10', False),
]
shandao2=Room('gumu/shandao2', u'ɽ��', 'gumu', 0, exits)

exits = [
	Exit('southup', 'gumu/shulin12', False),
	Exit('northdown', 'gumu/taiyi1', False),
]
shandao3=Room('gumu/shandao3', u'ɽ��', 'gumu', 0, exits)

exits = [
	Exit('out', 'gumu/xiaohebian', False),
	Exit('westdown', 'gumu/mishi7', False),
]
shandong=Room('gumu/shandong', u'ɽ��', 'gumu', 0, exits)

exits = [
	Exit('southdown', 'gumu/kongdi', False),
	Exit('northup', 'gumu/zhufeng', False),
]
shanlu1=Room('gumu/shanlu1', u'ɽ·', 'gumu', 0, exits)

exits = [
	Exit('eastdown', 'gumu/jinliange', False),
	Exit('westup', 'gumu/riyueyan', False),
]
shanlu10=Room('gumu/shanlu10', u'ɽ·', 'gumu', 0, exits)

exits = [
	Exit('southdown', 'gumu/shanlu12', False),
	Exit('northup', 'gumu/jinliange', False),
]
shanlu11=Room('gumu/shanlu11', u'ɽ·', 'gumu', 0, exits)

exits = [
	Exit('southdown', 'gumu/shanlu13', False),
	Exit('northup', 'gumu/shanlu11', False),
]
shanlu12=Room('gumu/shanlu12', u'ɽ·', 'gumu', 0, exits)

exits = [
	Exit('west', 'gumu/shanlu14', False),
	Exit('south', 'quanzhen/shanjiao', False),
	Exit('northup', 'gumu/shanlu12', False),
	Exit('east', 'gumu/puguangsi', False),
]
shanlu13=Room('gumu/shanlu13', u'��·', 'gumu', 0, exits)

exits = [
	Exit('northwest', 'gumu/shanlu15', False),
	Exit('east', 'gumu/shanlu13', False),
]
shanlu14=Room('gumu/shanlu14', u'ɽ��С��', 'gumu', 0, exits)

exits = [
	Exit('west', 'gumu/shanlu16', False),
	Exit('southeast', 'gumu/shanlu14', False),
]
shanlu15=Room('gumu/shanlu15', u'ɽ��С��', 'gumu', 0, exits)

exits = [
	Exit('south', 'gumu/xiaohebian', False),
	Exit('east', 'gumu/shanlu15', False),
]
shanlu16=Room('gumu/shanlu16', u'ɽ��С��', 'gumu', 0, exits)

exits = [
	Exit('eastup', 'gumu/zhufeng', False),
	Exit('northdown', 'gumu/shanlu3', False),
]
shanlu2=Room('gumu/shanlu2', u'ɽ·', 'gumu', 0, exits)

exits = [
	Exit('southup', 'gumu/shanlu2', False),
	Exit('eastdown', 'gumu/shanlu4', False),
]
shanlu3=Room('gumu/shanlu3', u'ɽ·', 'gumu', 0, exits)

exits = [
	Exit('eastdown', 'gumu/shanlu5', False),
	Exit('westup', 'gumu/shanlu3', False),
]
shanlu4=Room('gumu/shanlu4', u'ɽ·', 'gumu', 0, exits)

exits = [
	Exit('southdown', 'gumu/shanlu6', False),
	Exit('westup', 'gumu/shanlu4', False),
]
shanlu5=Room('gumu/shanlu5', u'ɽ·', 'gumu', 0, exits)

exits = [
	Exit('southdown', 'gumu/baimatang', False),
	Exit('eastdown', 'gumu/shanlu7', False),
	Exit('northup', 'gumu/shanlu5', False),
]
shanlu6=Room('gumu/shanlu6', u'ɽ·', 'gumu', 0, exits)

exits = [
	Exit('northwest', 'gumu/shandao1', False),
	Exit('eastdown', 'gumu/daxiaochang', False),
	Exit('northdown', 'gumu/caotangsi', False),
	Exit('westup', 'gumu/shanlu6', False),
]
shanlu7=Room('gumu/shanlu7', u'ɽ·', 'gumu', 0, exits)

exits = [
	Exit('southdown', 'gumu/juyan', False),
	Exit('northup', 'gumu/daxiaochang', False),
]
shanlu8=Room('gumu/shanlu8', u'ɽ��', 'gumu', 0, exits)

exits = [
	Exit('southdown', 'gumu/riyueyan', False),
	Exit('northup', 'gumu/shulin9', False),
]
shanlu9=Room('gumu/shanlu9', u'ɽ·', 'gumu', 0, exits)

exits = [
	Exit('southeast', 'gumu/shulin8', False),
	Exit('west', 'gumu/foyezhang', False),
	Exit('north', 'gumu/shulin7', False),
]
shenheyuan=Room('gumu/shenheyuan', u'���ԭ', 'gumu', 0, exits)

exits = [
	Exit('west', 'gumu/shulin5', False),
	Exit('southup', 'gumu/shulin1', False),
	Exit('east', 'gumu/shulin6', False),
	Exit('north', 'gumu/shulin4', False),
]
shulin0=Room('gumu/shulin0', u'С����', 'gumu', 0, exits)

exits = [
	Exit('southwest', 'gumu/shulin2', False),
	Exit('northdown', 'gumu/shulin0', False),
]
shulin1=Room('gumu/shulin1', u'С����', 'gumu', 0, exits)

exits = [
	Exit('southup', 'gumu/shandao2', False),
	Exit('north', 'gumu/shulin11', False),
]
shulin10=Room('gumu/shulin10', u'����', 'gumu', 0, exits)

exits = [
	Exit('south', 'gumu/shulin10', False),
	Exit('northdown', 'gumu/shulin12', False),
]
shulin11=Room('gumu/shulin11', u'����', 'gumu', 0, exits)

exits = [
	Exit('southup', 'gumu/shulin11', False),
	Exit('northdown', 'gumu/shandao3', False),
]
shulin12=Room('gumu/shulin12', u'����', 'gumu', 0, exits)

exits = [
	Exit('southwest', 'gumu/shulin3', False),
	Exit('northeast', 'gumu/shulin1', False),
]
shulin2=Room('gumu/shulin2', u'С����', 'gumu', 0, exits)

exits = [
	Exit('south', 'gumu/caodi', False),
	Exit('northeast', 'gumu/shulin2', False),
]
shulin3=Room('gumu/shulin3', u'С����', 'gumu', 0, exits)

exits = [
	Exit('west', 'gumu/shulin5', False),
	Exit('south', 'gumu/shulin0', False),
	Exit('east', 'gumu/shulin6', False),
	Exit('north', 'gumu/kongdi', False),
]
shulin4=Room('gumu/shulin4', u'С����', 'gumu', 0, exits)

exits = [
	Exit('west', 'gumu/shulin5', False),
	Exit('south', 'gumu/shulin4', False),
	Exit('north', 'gumu/shulin5', False),
	Exit('east', 'gumu/shulin0', False),
]
shulin5=Room('gumu/shulin5', u'С����', 'gumu', 0, exits)

exits = [
	Exit('west', 'gumu/shulin0', False),
	Exit('south', 'gumu/shulin6', False),
	Exit('east', 'gumu/shulin6', False),
	Exit('north', 'gumu/shulin4', False),
]
shulin6=Room('gumu/shulin6', u'С����', 'gumu', 0, exits)

exits = [
	Exit('eastdown', 'gumu/heifengdong', False),
	Exit('northup', 'gumu/juyan', False),
	Exit('south', 'gumu/shenheyuan', False),
]
shulin7=Room('gumu/shulin7', u'����', 'gumu', 0, exits)

exits = [
	Exit('northwest', 'gumu/shenheyuan', False),
	Exit('east', 'gumu/baoziyan', False),
]
shulin8=Room('gumu/shulin8', u'����', 'gumu', 0, exits)

exits = [
	Exit('southdown', 'gumu/shanlu9', False),
	Exit('north', 'gumu/baoziyan', False),
]
shulin9=Room('gumu/shulin9', u'����', 'gumu', 0, exits)

exits = [
	Exit('southup', 'gumu/shandao3', False),
]
taiyi1=Room('gumu/taiyi1', u'̫�ҳ�', 'gumu', 0, exits)

exits = [
]
taiyi2=Room('gumu/taiyi2', u'̫�ҳ�', 'gumu', 0, exits)

exits = [
	Exit('north', 'gumu/shanlu16', False),
	Exit('enter', 'gumu/shandong', False),
]
xiaohebian=Room('gumu/xiaohebian', u'С�ӱ�', 'gumu', 0, exits)

exits = [
	Exit('west', 'gumu/xiaowu1', False),
	Exit('south', 'gumu/zhengting', False),
	Exit('east', 'gumu/xiaowu2', False),
	Exit('north', 'gumu/qianting', False),
]
xiaoting=Room('gumu/xiaoting', u'С��', None, 0, exits)

exits = [
	Exit('east', 'gumu/xiaoting', False),
]
xiaowu1=Room('gumu/xiaowu1', u'С��', None, 0, exits)

exits = [
	Exit('west', 'gumu/xiaoting', False),
	Exit('east', 'gumu/xiaowu3', False),
]
xiaowu2=Room('gumu/xiaowu2', u'����', None, 0, exits)

exits = [
	Exit('west', 'gumu/xiaowu2', False),
]
xiaowu3=Room('gumu/xiaowu3', u'С��', None, 0, exits)

exits = [
	Exit('west', 'gumu/zhengting', False),
]
xiuxishi=Room('gumu/xiuxishi', u'��Ϣ��', None, 0, exits)

exits = [
	Exit('west', 'gumu/liangong', False),
	Exit('south', 'gumu/houting', False),
	Exit('east', 'gumu/xiuxishi', False),
	Exit('north', 'gumu/xiaoting', False),
]
zhengting=Room('gumu/zhengting', u'����', None, 0, exits)

exits = [
	Exit('southdown', 'gumu/shanlu1', False),
	Exit('westdown', 'gumu/shanlu2', False),
]
zhufeng=Room('gumu/zhufeng', u'����ɽ����', 'gumu', 0, exits)

