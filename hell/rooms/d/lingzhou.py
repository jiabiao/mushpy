# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('west', 'lingzhou/xiaolu2', False),
]
baxian=Room('lingzhou/baxian', u'八仙道观', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/center', False),
	Exit('north', 'lingzhou/gonggate', False),
]
beidajie=Room('lingzhou/beidajie', u'北大街', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/caifang', True),
	Exit('east', 'lingzhou/xiaolu3', False),
]
biangate=Room('lingzhou/biangate', u'边门', None, 0, exits)

exits = [
	Exit('west', 'lingzhou/malan', False),
	Exit('south', 'lingzhou/xiaoxiaochang', False),
	Exit('east', 'lingzhou/xidajie', False),
	Exit('north', 'lingzhou/yinfang', False),
]
biaoqiyin=Room('lingzhou/biaoqiyin', u'骠骑营', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/xidajie', False),
	Exit('south', 'lingzhou/nandajie', False),
	Exit('east', 'lingzhou/dongdajie', False),
	Exit('north', 'lingzhou/beidajie', False),
]
center=Room('lingzhou/center', u'城中心', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/nandajie', False),
	Exit('up', 'lingzhou/chema2', False),
	Exit('east', 'lingzhou/majiu', False),
]
chema=Room('lingzhou/chema', u'车马店', None, 0, exits)

exits = [
	Exit('down', 'lingzhou/chema', False),
]
chema2=Room('lingzhou/chema2', u'车马店二楼', None, 0, exits)

exits = [
	Exit('south', 'lingzhou/wangling', False),
	Exit('north', 'lingzhou/deling', False),
]
chiling=Room('lingzhou/chiling', u'赤陵', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/luorilin1', False),
	Exit('northeast', 'lingzhou/luorilin2', False),
	Exit('north', 'lingzhou/xiaolu1', False),
]
dalu=Room('lingzhou/dalu', u'林中大路', 'lingzhou', 0, exits)

exits = [
	Exit('north', 'lingzhou/xidajie', False),
]
daodian=Room('lingzhou/daodian', u'刀店', None, 0, exits)

exits = [
	Exit('out', 'lingzhou/kongdi', False),
]
dawu=Room('lingzhou/dawu', u'林中大屋', None, 0, exits)

exits = [
	Exit('south', 'lingzhou/chiling', False),
	Exit('north', 'lingzhou/gongling', False),
]
deling=Room('lingzhou/deling', u'德陵', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/center', False),
	Exit('south', 'lingzhou/jiangjungate', False),
	Exit('east', 'lingzhou/dongmen', False),
	Exit('north', 'lingzhou/yamen', False),
]
dongdajie=Room('lingzhou/dongdajie', u'东大街', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/dongdajie', False),
	Exit('northeast', 'lingzhou/luorilin1', False),
]
dongmen=Room('lingzhou/dongmen', u'灵州东门', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/beidajie', False),
	Exit('north', 'lingzhou/gongsquare', True),
]
gonggate=Room('lingzhou/gonggate', u'皇宫大门', None, 0, exits)

exits = [
	Exit('south', 'lingzhou/deling', False),
]
gongling=Room('lingzhou/gongling', u'恭陵', 'lingzhou', 0, exits)

exits = [
	Exit('southwest', 'lingzhou/xiaoba', False),
	Exit('north', 'lingzhou/nanmen', False),
]
huangyangtan=Room('lingzhou/huangyangtan', u'黄羊滩', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/jiangjunyuan', True),
	Exit('north', 'lingzhou/dongdajie', False),
]
jiangjungate=Room('lingzhou/jiangjungate', u'大将军府', None, 0, exits)

exits = [
	Exit('south', 'lingzhou/neizai', False),
	Exit('north', 'lingzhou/jiangjungate', True),
	Exit('east', 'lingzhou/xiaoyuan', False),
]
jiangjunyuan=Room('lingzhou/jiangjunyuan', u'将军府大院', None, 0, exits)

exits = [
	Exit('east', 'lingzhou/nandajie', False),
]
jiuguan=Room('lingzhou/jiuguan', u'酒馆', 'lingzhou', 0, exits)

exits = [
	Exit('northwest', 'lingzhou/qingxinquan', False),
	Exit('southwest', 'lingzhou/tulu', False),
	Exit('enter', 'lingzhou/dawu', False),
]
kongdi=Room('lingzhou/kongdi', u'林中空地', 'lingzhou', 0, exits)

exits = [
	Exit('southwest', 'lingzhou/dongmen', False),
	Exit('north', 'lingzhou/dalu', False),
]
luorilin1=Room('lingzhou/luorilin1', u'落日林', 'lingzhou', 0, exits)

exits = [
	Exit('southwest', 'lingzhou/dalu', False),
	Exit('north', 'lingzhou/tulu', False),
]
luorilin2=Room('lingzhou/luorilin2', u'落日林', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/chema', False),
]
majiu=Room('lingzhou/majiu', u'马厩', 'lingzhou', 0, exits)

exits = [
	Exit('east', 'lingzhou/biaoqiyin', False),
]
malan=Room('lingzhou/malan', u'马栏', 'lingzhou', 0, exits)

exits = [
	Exit('southwest', 'lingzhou/xuanhebao', False),
	Exit('northeast', 'lingzhou/qingtongxia', False),
]
mingshazhou=Room('lingzhou/mingshazhou', u'鸣沙洲', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/jiuguan', False),
	Exit('south', 'lingzhou/nanmen', False),
	Exit('east', 'lingzhou/chema', False),
	Exit('north', 'lingzhou/center', False),
]
nandajie=Room('lingzhou/nandajie', u'南大街', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/huangyangtan', False),
	Exit('north', 'lingzhou/nandajie', False),
]
nanmen=Room('lingzhou/nanmen', u'灵州南门', 'lingzhou', 0, exits)

exits = [
	Exit('north', 'lingzhou/jiangjunyuan', False),
]
neizai=Room('lingzhou/neizai', u'将军府内宅', None, 0, exits)

exits = [
	Exit('southwest', 'lingzhou/mingshazhou', False),
	Exit('northeast', 'lingzhou/xiaoba', False),
]
qingtongxia=Room('lingzhou/qingtongxia', u'青铜峡', 'lingzhou', 0, exits)

exits = [
	Exit('southeast', 'lingzhou/kongdi', False),
	Exit('northdown', 'lingzhou/wangling', False),
]
qingxinquan=Room('lingzhou/qingxinquan', u'清新泉', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/luorilin2', False),
	Exit('northeast', 'lingzhou/kongdi', False),
]
tulu=Room('lingzhou/tulu', u'林中土路', 'lingzhou', 0, exits)

exits = [
	Exit('southup', 'lingzhou/qingxinquan', False),
	Exit('north', 'lingzhou/chiling', False),
]
wangling=Room('lingzhou/wangling', u'西夏王陵', 'lingzhou', 0, exits)

exits = [
	Exit('southwest', 'lingzhou/qingtongxia', False),
	Exit('northeast', 'lingzhou/huangyangtan', False),
]
xiaoba=Room('lingzhou/xiaoba', u'小坝', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/dalu', False),
	Exit('north', 'lingzhou/xiaolu2', False),
]
xiaolu1=Room('lingzhou/xiaolu1', u'林中小路', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/xiaolu3', False),
	Exit('south', 'lingzhou/xiaolu1', False),
	Exit('east', 'lingzhou/baxian', False),
]
xiaolu2=Room('lingzhou/xiaolu2', u'林中小路', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/biangate', False),
	Exit('east', 'lingzhou/xiaolu2', False),
]
xiaolu3=Room('lingzhou/xiaolu3', u'林中小路', 'lingzhou', 0, exits)

exits = [
	Exit('north', 'lingzhou/biaoqiyin', False),
]
xiaoxiaochang=Room('lingzhou/xiaoxiaochang', u'小校场', 'lingzhou', 0, exits)

exits = [
	Exit('west', 'lingzhou/jiangjunyuan', False),
]
xiaoyuan=Room('lingzhou/xiaoyuan', u'将军府小院', None, 0, exits)

exits = [
	Exit('west', 'lingzhou/biaoqiyin', False),
	Exit('south', 'lingzhou/daodian', False),
	Exit('east', 'lingzhou/center', False),
	Exit('north', 'lingzhou/yipingate', False),
]
xidajie=Room('lingzhou/xidajie', u'西大街', 'lingzhou', 0, exits)

exits = [
	Exit('northeast', 'lingzhou/mingshazhou', False),
]
xuanhebao=Room('lingzhou/xuanhebao', u'宣和堡', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/dongdajie', False),
]
yamen=Room('lingzhou/yamen', u'衙门', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/biaoqiyin', False),
]
yinfang=Room('lingzhou/yinfang', u'营房', 'lingzhou', 0, exits)

exits = [
	Exit('south', 'lingzhou/yipindayuan', False),
]
yipindating=Room('lingzhou/yipindating', u'一品堂大厅', None, 0, exits)

exits = [
	Exit('west', 'lingzhou/yipinzhang', False),
	Exit('south', 'lingzhou/yipingate', False),
	Exit('east', 'lingzhou/yipinjieyin', False),
	Exit('north', 'lingzhou/yipindating', False),
]
yipindayuan=Room('lingzhou/yipindayuan', u'一品堂大院', None, 0, exits)

exits = [
	Exit('south', 'lingzhou/xidajie', False),
	Exit('north', 'lingzhou/yipindayuan', True),
]
yipingate=Room('lingzhou/yipingate', u'一品堂大门', None, 0, exits)

exits = [
	Exit('west', 'lingzhou/yipindayuan', False),
]
yipinjieyin=Room('lingzhou/yipinjieyin', u'接引堂', None, 0, exits)

exits = [
	Exit('east', 'lingzhou/yipindayuan', False),
]
yipinzhang=Room('lingzhou/yipinzhang', u'一品堂帐房', None, 0, exits)

