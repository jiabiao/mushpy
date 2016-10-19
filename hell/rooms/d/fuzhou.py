# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('northup', 'fuzhou/pingshan', False),
	Exit('south', 'fuzhou/dongjiekou', False),
]
beidajie=Room('fuzhou/beidajie', u'�����', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'fuzhou/xidajie', False),
	Exit('enter', 'fuzhou/biaojudy', False),
]
biaoju=Room('fuzhou/biaoju', u'�����ھ�', None, 0, exits)

exits = [
	Exit('out', 'fuzhou/biaoju', False),
	Exit('north', 'fuzhou/biaojuzt', False),
]
biaojudy=Room('fuzhou/biaojudy', u'�ھִ�Ժ', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'fuzhou/biaojuzt', False),
]
biaojuhy=Room('fuzhou/biaojuhy', u'�ھֺ�Ժ', 'fuzhou', 0, exits)

exits = [
	Exit('east', 'fuzhou/biaojuzt', False),
]
biaojunz=Room('fuzhou/biaojunz', u'��լ', None, 0, exits)

exits = [
	Exit('west', 'fuzhou/biaojunz', False),
	Exit('south', 'fuzhou/biaojudy', False),
	Exit('north', 'fuzhou/biaojuhy', False),
]
biaojuzt=Room('fuzhou/biaojuzt', u'����', None, 0, exits)

exits = [
	Exit('west', 'fuzhou/dongjiekou', False),
	Exit('southup', 'fuzhou/yushan', False),
	Exit('east', 'fuzhou/dongxiaojie', False),
	Exit('north', 'fuzhou/rongcheng', False),
]
dongdajie=Room('fuzhou/dongdajie', u'�����', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/xidajie', False),
	Exit('south', 'fuzhou/nandajie', False),
	Exit('east', 'fuzhou/dongdajie', False),
	Exit('north', 'fuzhou/beidajie', False),
]
dongjiekou=Room('fuzhou/dongjiekou', u'���ֿ�', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/dongxiaojie', False),
	Exit('east', 'fuzhou/shulin', False),
]
dongmen=Room('fuzhou/dongmen', u'���ݶ���', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/dongdajie', False),
	Exit('east', 'fuzhou/dongmen', False),
]
dongxiaojie=Room('fuzhou/dongxiaojie', u'��С��', 'fuzhou', 0, exits)

exits = [
	Exit('southdown', 'fuzhou/fzroad2', False),
	Exit('west', 'fuzhou/kedian', False),
	Exit('north', 'fuzhou/fzroad1', False),
]
erbapu=Room('fuzhou/erbapu', u'إ����', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'fuzhou/erbapu', False),
	Exit('northdown', 'quanzhou/qzroad4', False),
]
fzroad1=Room('fuzhou/fzroad1', u'��ϼ��', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'fuzhou/fzroad9', False),
]
fzroad10=Room('fuzhou/fzroad10', u'����', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/fzroad9', False),
	Exit('east', 'fuzhou/ximen', False),
]
fzroad11=Room('fuzhou/fzroad11', u'���д��', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/wuyishan1', False),
	Exit('southup', 'fuzhou/fzroad3', False),
	Exit('northup', 'fuzhou/erbapu', False),
]
fzroad2=Room('fuzhou/fzroad2', u'����ɽ��', 'fuzhou', 0, exits)

exits = [
	Exit('southdown', 'fuzhou/yanping', False),
	Exit('northdown', 'fuzhou/fzroad2', False),
]
fzroad3=Room('fuzhou/fzroad3', u'����ŵ�', 'fuzhou', 0, exits)

exits = [
	Exit('southwest', 'fuzhou/fzroad5', False),
	Exit('northeast', 'fuzhou/yanping', False),
]
fzroad4=Room('fuzhou/fzroad4', u'���ӹŵ�', 'fuzhou', 0, exits)

exits = [
	Exit('northeast', 'fuzhou/fzroad4', False),
	Exit('westup', 'fuzhou/fzroad6', False),
]
fzroad5=Room('fuzhou/fzroad5', u'���ӹŵ�', 'fuzhou', 0, exits)

exits = [
	Exit('eastdown', 'fuzhou/fzroad5', False),
	Exit('westdown', 'fuzhou/fzroad7', False),
]
fzroad6=Room('fuzhou/fzroad6', u'���ӹŵ�', 'fuzhou', 0, exits)

exits = [
	Exit('northwest', 'henshan/hsroad2', False),
	Exit('eastup', 'fuzhou/fzroad6', False),
]
fzroad7=Room('fuzhou/fzroad7', u'���ӹŵ�', 'fuzhou', 0, exits)

exits = [
	Exit('southeast', 'fuzhou/fzroad9', False),
	Exit('northwest', 'fuzhou/yanping', False),
]
fzroad8=Room('fuzhou/fzroad8', u'����', 'fuzhou', 0, exits)

exits = [
	Exit('northwest', 'fuzhou/fzroad8', False),
	Exit('east', 'fuzhou/fzroad11', False),
	Exit('north', 'fuzhou/fzroad10', False),
]
fzroad9=Room('fuzhou/fzroad9', u'���д��', 'fuzhou', 0, exits)

exits = [
	Exit('westdown', 'fuzhou/shulin', False),
	Exit('north', 'fuzhou/yongquan', False),
]
gushan=Room('fuzhou/gushan', u'��ɽ', 'fuzhou', 0, exits)

exits = [
	Exit('down', 'fuzhou/well', False),
]
houyuan=Room('fuzhou/houyuan', u'��լ��Ժ', None, 0, exits)

exits = [
	Exit('east', 'fuzhou/erbapu', False),
]
kedian=Room('fuzhou/kedian', u'�͵�', None, 0, exits)

exits = [
	Exit('south', 'fuzhou/xiangyang', False),
]
laozhai=Room('fuzhou/laozhai', u'������լ', None, 0, exits)

exits = [
	Exit('down', 'fuzhou/mishi', False),
]
liang=Room('fuzhou/liang', u'���ҷ���', None, 0, exits)

exits = [
	Exit('south', 'fuzhou/rongcheng', False),
]
majiu=Room('fuzhou/majiu', u'���', 'fuzhou', 0, exits)

exits = [
	Exit('out', 'fuzhou/well', False),
]
midao=Room('fuzhou/midao', u'�ܵ�', None, 0, exits)

exits = [
	Exit('out', 'fuzhou/midao', False),
]
mishi=Room('fuzhou/mishi', u'����', None, 0, exits)

exits = [
	Exit('west', 'fuzhou/yamen', False),
	Exit('south', 'fuzhou/nanmendou', False),
	Exit('east', 'fuzhou/weizhongwei', False),
	Exit('north', 'fuzhou/dongjiekou', False),
]
nandajie=Room('fuzhou/nandajie', u'�ϴ��', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'fuzhou/zhongzhou', False),
	Exit('north', 'fuzhou/nanmendou', False),
]
nanmen=Room('fuzhou/nanmen', u'��������', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/shiqiao', False),
	Exit('south', 'fuzhou/nanmen', False),
	Exit('east', 'fuzhou/xiaochang', False),
	Exit('north', 'fuzhou/nandajie', False),
]
nanmendou=Room('fuzhou/nanmendou', u'���Ŷ�', 'fuzhou', 0, exits)

exits = [
	Exit('southdown', 'fuzhou/beidajie', False),
]
pingshan=Room('fuzhou/pingshan', u'������ɽ', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'quanzhou/beimen', False),
	Exit('north', 'fuzhou/zhongzhou', False),
]
puxian=Room('fuzhou/puxian', u'����ƽԭ', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'fuzhou/dongdajie', False),
	Exit('up', 'fuzhou/rongcheng2', False),
	Exit('north', 'fuzhou/majiu', False),
]
rongcheng=Room('fuzhou/rongcheng', u'�ų���', None, 0, exits)

exits = [
	Exit('down', 'fuzhou/rongcheng', False),
]
rongcheng2=Room('fuzhou/rongcheng2', u'�ų����¥', None, 0, exits)

exits = [
	Exit('west', 'fuzhou/xiangyang', False),
	Exit('east', 'fuzhou/nanmendou', False),
]
shiqiao=Room('fuzhou/shiqiao', u'ʯ��', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/dongmen', False),
	Exit('eastup', 'fuzhou/gushan', False),
	Exit('north', 'fuzhou/wuxiang', False),
]
shulin=Room('fuzhou/shulin', u'����', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/nandajie', False),
]
weizhongwei=Room('fuzhou/weizhongwei', u'ζ��ζ', None, 0, exits)

exits = [
	Exit('up', 'fuzhou/houyuan', False),
	Exit('down', 'fuzhou/well1', False),
]
well=Room('fuzhou/well', u'����', None, 0, exits)

exits = [
	Exit('up', 'fuzhou/well', False),
]
well1=Room('fuzhou/well1', u'����', None, 0, exits)

exits = [
	Exit('northdown', 'fuzhou/xidajie', False),
]
wushan=Room('fuzhou/wushan', u'������ɽ', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'fuzhou/shulin', False),
]
wuxiang=Room('fuzhou/wuxiang', u'������', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/wuyishan2', False),
	Exit('east', 'fuzhou/fzroad2', False),
]
wuyishan1=Room('fuzhou/wuyishan1', u'����ɽ', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/wuyishan5', False),
	Exit('south', 'fuzhou/wuyishan7', False),
	Exit('northup', 'fuzhou/wuyishan6', False),
	Exit('east', 'fuzhou/wuyishan1', False),
]
wuyishan2=Room('fuzhou/wuyishan2', u'����Ϫ', 'fuzhou', 0, exits)

exits = [
	Exit('southdown', 'fuzhou/wuyishan5', False),
]
wuyishan3=Room('fuzhou/wuyishan3', u'���η�', 'fuzhou', 0, exits)

exits = [
	Exit('southeast', 'fuzhou/wuyishan5', False),
]
wuyishan4=Room('fuzhou/wuyishan4', u'������', 'fuzhou', 0, exits)

exits = [
	Exit('northwest', 'fuzhou/wuyishan4', False),
	Exit('northup', 'fuzhou/wuyishan3', False),
	Exit('east', 'fuzhou/wuyishan2', False),
]
wuyishan5=Room('fuzhou/wuyishan5', u'����Ϫ', 'fuzhou', 0, exits)

exits = [
	Exit('southdown', 'fuzhou/wuyishan2', False),
]
wuyishan6=Room('fuzhou/wuyishan6', u'������', 'fuzhou', 0, exits)

exits = [
	Exit('north', 'fuzhou/wuyishan2', False),
]
wuyishan7=Room('fuzhou/wuyishan7', u'��Ů��', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/zahuopu', False),
	Exit('north', 'fuzhou/laozhai', False),
	Exit('east', 'fuzhou/shiqiao', False),
]
xiangyang=Room('fuzhou/xiangyang', u'������', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/nanmendou', False),
]
xiaochang=Room('fuzhou/xiaochang', u'У��', 'fuzhou', 0, exits)

exits = [
	Exit('north', 'fuzhou/ximendajie', False),
]
xichansi=Room('fuzhou/xichansi', u'������', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/ximendajie', False),
	Exit('southup', 'fuzhou/wushan', False),
	Exit('east', 'fuzhou/dongjiekou', False),
	Exit('north', 'fuzhou/biaoju', False),
]
xidajie=Room('fuzhou/xidajie', u'�����', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'fuzhou/ximendajie', False),
]
xihu=Room('fuzhou/xihu', u'����', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/fzroad11', False),
	Exit('east', 'fuzhou/ximendajie', False),
]
ximen=Room('fuzhou/ximen', u'��������', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/ximen', False),
	Exit('south', 'fuzhou/xichansi', False),
	Exit('north', 'fuzhou/xihu', False),
	Exit('east', 'fuzhou/xidajie', False),
]
ximendajie=Room('fuzhou/ximendajie', u'���Ŵ��', 'fuzhou', 0, exits)

exits = [
	Exit('east', 'fuzhou/nandajie', False),
]
yamen=Room('fuzhou/yamen', u'�ᶽ����', None, 0, exits)

exits = [
	Exit('southeast', 'fuzhou/fzroad8', False),
	Exit('northup', 'fuzhou/fzroad3', False),
	Exit('southwest', 'fuzhou/fzroad4', False),
]
yanping=Room('fuzhou/yanping', u'��ƽ��', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'fuzhou/gushan', False),
]
yongquan=Room('fuzhou/yongquan', u'ӿȪ��', 'fuzhou', 0, exits)

exits = [
	Exit('northdown', 'fuzhou/dongdajie', False),
]
yushan=Room('fuzhou/yushan', u'������ɽ', 'fuzhou', 0, exits)

exits = [
	Exit('east', 'fuzhou/xiangyang', False),
]
zahuopu=Room('fuzhou/zahuopu', u'�ӻ���', None, 0, exits)

exits = [
	Exit('south', 'fuzhou/puxian', False),
	Exit('north', 'fuzhou/nanmen', False),
]
zhongzhou=Room('fuzhou/zhongzhou', u'������', 'fuzhou', 0, exits)

