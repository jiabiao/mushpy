# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('west', 'lingzhou/xiaolu2', False),
]
baxian=Room('lingzhou/baxian', u'���ɵ���', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/center', False),
	Exit('north', 'lingzhou/gonggate', False),
]
beidajie=Room('lingzhou/beidajie', u'�����', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/caifang', True),
	Exit('east', 'lingzhou/xiaolu3', False),
]
biangate=Room('lingzhou/biangate', u'����', None, 0, exits)

exits = [
	Exit('west', 'lingzhou/malan', False),
	Exit('south', 'lingzhou/xiaoxiaochang', False),
	Exit('east', 'lingzhou/xidajie', False),
	Exit('north', 'lingzhou/yinfang', False),
]
biaoqiyin=Room('lingzhou/biaoqiyin', u'����Ӫ', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/xidajie', False),
	Exit('south', 'lingzhou/nandajie', False),
	Exit('east', 'lingzhou/dongdajie', False),
	Exit('north', 'lingzhou/beidajie', False),
]
center=Room('lingzhou/center', u'������', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/nandajie', False),
	Exit('up', 'lingzhou/chema2', False),
	Exit('east', 'lingzhou/majiu', False),
]
chema=Room('lingzhou/chema', u'�����', None, 0, exits)

exits = [
	Exit('down', 'lingzhou/chema', False),
]
chema2=Room('lingzhou/chema2', u'������¥', None, 0, exits)

exits = [
	Exit('south', 'lingzhou/wangling', False),
	Exit('north', 'lingzhou/deling', False),
]
chiling=Room('lingzhou/chiling', u'����', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/luorilin1', False),
	Exit('northeast', 'lingzhou/luorilin2', False),
	Exit('north', 'lingzhou/xiaolu1', False),
]
dalu=Room('lingzhou/dalu', u'���д�·', 'lingzhou', 0, exits)

exits = [
	Exit('north', 'lingzhou/xidajie', False),
]
daodian=Room('lingzhou/daodian', u'����', None, 0, exits)

exits = [
	Exit('out', 'lingzhou/kongdi', False),
]
dawu=Room('lingzhou/dawu', u'���д���', None, 0, exits)

exits = [
	Exit('south', 'lingzhou/chiling', False),
	Exit('north', 'lingzhou/gongling', False),
]
deling=Room('lingzhou/deling', u'����', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/center', False),
	Exit('south', 'lingzhou/jiangjungate', False),
	Exit('east', 'lingzhou/dongmen', False),
	Exit('north', 'lingzhou/yamen', False),
]
dongdajie=Room('lingzhou/dongdajie', u'�����', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/dongdajie', False),
	Exit('northeast', 'lingzhou/luorilin1', False),
]
dongmen=Room('lingzhou/dongmen', u'���ݶ���', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/beidajie', False),
	Exit('north', 'lingzhou/gongsquare', True),
]
gonggate=Room('lingzhou/gonggate', u'�ʹ�����', None, 0, exits)

exits = [
	Exit('south', 'lingzhou/deling', False),
]
gongling=Room('lingzhou/gongling', u'����', 'lingzhou', 0, exits)

exits = [
	Exit('southwest', 'lingzhou/xiaoba', False),
	Exit('north', 'lingzhou/nanmen', False),
]
huangyangtan=Room('lingzhou/huangyangtan', u'����̲', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/jiangjunyuan', True),
	Exit('north', 'lingzhou/dongdajie', False),
]
jiangjungate=Room('lingzhou/jiangjungate', u'�󽫾���', None, 0, exits)

exits = [
	Exit('south', 'lingzhou/neizai', False),
	Exit('north', 'lingzhou/jiangjungate', True),
	Exit('east', 'lingzhou/xiaoyuan', False),
]
jiangjunyuan=Room('lingzhou/jiangjunyuan', u'��������Ժ', None, 0, exits)

exits = [
	Exit('east', 'lingzhou/nandajie', False),
]
jiuguan=Room('lingzhou/jiuguan', u'�ƹ�', 'lingzhou', 0, exits)

exits = [
	Exit('northwest', 'lingzhou/qingxinquan', False),
	Exit('southwest', 'lingzhou/tulu', False),
	Exit('enter', 'lingzhou/dawu', False),
]
kongdi=Room('lingzhou/kongdi', u'���пյ�', 'lingzhou', 0, exits)

exits = [
	Exit('southwest', 'lingzhou/dongmen', False),
	Exit('north', 'lingzhou/dalu', False),
]
luorilin1=Room('lingzhou/luorilin1', u'������', 'lingzhou', 0, exits)

exits = [
	Exit('southwest', 'lingzhou/dalu', False),
	Exit('north', 'lingzhou/tulu', False),
]
luorilin2=Room('lingzhou/luorilin2', u'������', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/chema', False),
]
majiu=Room('lingzhou/majiu', u'���', 'lingzhou', 0, exits)

exits = [
	Exit('east', 'lingzhou/biaoqiyin', False),
]
malan=Room('lingzhou/malan', u'����', 'lingzhou', 0, exits)

exits = [
	Exit('southwest', 'lingzhou/xuanhebao', False),
	Exit('northeast', 'lingzhou/qingtongxia', False),
]
mingshazhou=Room('lingzhou/mingshazhou', u'��ɳ��', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/jiuguan', False),
	Exit('south', 'lingzhou/nanmen', False),
	Exit('east', 'lingzhou/chema', False),
	Exit('north', 'lingzhou/center', False),
]
nandajie=Room('lingzhou/nandajie', u'�ϴ��', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/huangyangtan', False),
	Exit('north', 'lingzhou/nandajie', False),
]
nanmen=Room('lingzhou/nanmen', u'��������', 'lingzhou', 0, exits)

exits = [
	Exit('north', 'lingzhou/jiangjunyuan', False),
]
neizai=Room('lingzhou/neizai', u'��������լ', None, 0, exits)

exits = [
	Exit('southwest', 'lingzhou/mingshazhou', False),
	Exit('northeast', 'lingzhou/xiaoba', False),
]
qingtongxia=Room('lingzhou/qingtongxia', u'��ͭϿ', 'lingzhou', 0, exits)

exits = [
	Exit('southeast', 'lingzhou/kongdi', False),
	Exit('northdown', 'lingzhou/wangling', False),
]
qingxinquan=Room('lingzhou/qingxinquan', u'����Ȫ', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/luorilin2', False),
	Exit('northeast', 'lingzhou/kongdi', False),
]
tulu=Room('lingzhou/tulu', u'������·', 'lingzhou', 0, exits)

exits = [
	Exit('southup', 'lingzhou/qingxinquan', False),
	Exit('north', 'lingzhou/chiling', False),
]
wangling=Room('lingzhou/wangling', u'��������', 'lingzhou', 0, exits)

exits = [
	Exit('southwest', 'lingzhou/qingtongxia', False),
	Exit('northeast', 'lingzhou/huangyangtan', False),
]
xiaoba=Room('lingzhou/xiaoba', u'С��', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/dalu', False),
	Exit('north', 'lingzhou/xiaolu2', False),
]
xiaolu1=Room('lingzhou/xiaolu1', u'����С·', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/xiaolu3', False),
	Exit('south', 'lingzhou/xiaolu1', False),
	Exit('east', 'lingzhou/baxian', False),
]
xiaolu2=Room('lingzhou/xiaolu2', u'����С·', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/biangate', False),
	Exit('east', 'lingzhou/xiaolu2', False),
]
xiaolu3=Room('lingzhou/xiaolu3', u'����С·', 'lingzhou', 0, exits)

exits = [
	Exit('north', 'lingzhou/biaoqiyin', False),
]
xiaoxiaochang=Room('lingzhou/xiaoxiaochang', u'СУ��', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/jiangjunyuan', False),
]
xiaoyuan=Room('lingzhou/xiaoyuan', u'������СԺ', None, 0, exits)

exits = [
	Exit('west', 'lingzhou/biaoqiyin', False),
	Exit('south', 'lingzhou/daodian', False),
	Exit('east', 'lingzhou/center', False),
	Exit('north', 'lingzhou/yipingate', False),
]
xidajie=Room('lingzhou/xidajie', u'�����', 'lingzhou', 0, exits)

exits = [
	Exit('northeast', 'lingzhou/mingshazhou', False),
]
xuanhebao=Room('lingzhou/xuanhebao', u'���ͱ�', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/dongdajie', False),
]
yamen=Room('lingzhou/yamen', u'����', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/biaoqiyin', False),
]
yinfang=Room('lingzhou/yinfang', u'Ӫ��', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/yipindayuan', False),
]
yipindating=Room('lingzhou/yipindating', u'һƷ�ô���', None, 0, exits)

exits = [
	Exit('west', 'lingzhou/yipinzhang', False),
	Exit('south', 'lingzhou/yipingate', False),
	Exit('east', 'lingzhou/yipinjieyin', False),
	Exit('north', 'lingzhou/yipindating', False),
]
yipindayuan=Room('lingzhou/yipindayuan', u'һƷ�ô�Ժ', None, 0, exits)

exits = [
	Exit('south', 'lingzhou/xidajie', False),
	Exit('north', 'lingzhou/yipindayuan', True),
]
yipingate=Room('lingzhou/yipingate', u'һƷ�ô���', None, 0, exits)

exits = [
	Exit('west', 'lingzhou/yipindayuan', False),
]
yipinjieyin=Room('lingzhou/yipinjieyin', u'������', None, 0, exits)

exits = [
	Exit('east', 'lingzhou/yipindayuan', False),
]
yipinzhang=Room('lingzhou/yipinzhang', u'һƷ���ʷ�', None, 0, exits)

