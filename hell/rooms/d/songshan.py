# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('southdown', 'songshan/junjigate', False),
]
chanyuan=Room('songshan/chanyuan', u'������Ժ', None, 0, exits)

exits = [
	Exit('southdown', 'songshan/shandao5', False),
	Exit('northup', 'songshan/shandao6', False),
]
chaotian=Room('songshan/chaotian', u'������', 'songshan', 0, exits)

exits = [
	Exit('south', 'songshan/tianzhongge', False),
	Exit('north', 'songshan/dadian', False),
]
chongsheng=Room('songshan/chongsheng', u'��ʥ��', None, 0, exits)

exits = [
	Exit('south', 'songshan/chongsheng', False),
	Exit('northup', 'songshan/shandao1', False),
]
dadian=Room('songshan/dadian', u'�������', None, 0, exits)

exits = [
	Exit('southdown', 'songshan/shandao4', False),
	Exit('west', 'songshan/yuetai', False),
	Exit('northup', 'songshan/tayuan', False),
	Exit('northeast', 'songshan/shandao5', False),
]
fawangsi=Room('songshan/fawangsi', u'������', None, 0, exits)

exits = [
	Exit('eastdown', 'songshan/junjigate', False),
]
fengchantai=Room('songshan/fengchantai', u'����̨', 'songshan', 0, exits)

exits = [
	Exit('southdown', 'songshan/shandao6', False),
	Exit('northup', 'songshan/chanyuan', False),
	Exit('westup', 'songshan/fengchantai', False),
]
junjigate=Room('songshan/junjigate', u'������Ժɽ��', None, 0, exits)

exits = [
	Exit('southwest', 'songshan/shandao1', False),
	Exit('up', 'songshan/tieliang', False),
]
luyanpubu=Room('songshan/luyanpubu', u'«���ٲ�', 'songshan', 0, exits)

exits = [
	Exit('east', 'songshan/qimushi', False),
]
qimuque=Room('songshan/qimuque', u'��ĸ��', None, 0, exits)

exits = [
	Exit('west', 'songshan/qimuque', False),
	Exit('southeast', 'songshan/shandao1', False),
	Exit('northup', 'songshan/shandao2', False),
]
qimushi=Room('songshan/qimushi', u'��ĸʯ', 'songshan', 0, exits)

exits = [
	Exit('southdown', 'songshan/dadian', False),
	Exit('northwest', 'songshan/qimushi', False),
	Exit('northeast', 'songshan/luyanpubu', False),
]
shandao1=Room('songshan/shandao1', u'ɽ��', 'songshan', 0, exits)

exits = [
	Exit('southdown', 'songshan/qimushi', False),
	Exit('northup', 'songshan/shuyuan', False),
]
shandao2=Room('songshan/shandao2', u'ɽ��', 'songshan', 0, exits)

exits = [
	Exit('southeast', 'songshan/shuyuan', False),
	Exit('northup', 'songshan/songyuesi', False),
]
shandao3=Room('songshan/shandao3', u'ɽ��', 'songshan', 0, exits)

exits = [
	Exit('southeast', 'songshan/songyuesi', False),
	Exit('northup', 'songshan/fawangsi', False),
]
shandao4=Room('songshan/shandao4', u'ɽ��', 'songshan', 0, exits)

exits = [
	Exit('southdown', 'songshan/tieliang', False),
	Exit('northup', 'songshan/chaotian', False),
	Exit('southwest', 'songshan/fawangsi', False),
]
shandao5=Room('songshan/shandao5', u'ɽ���', 'songshan', 0, exits)

exits = [
	Exit('southdown', 'songshan/chaotian', False),
	Exit('northup', 'songshan/junjigate', False),
]
shandao6=Room('songshan/shandao6', u'ɽ��', 'songshan', 0, exits)

exits = [
	Exit('southdown', 'songshan/shandao2', False),
	Exit('northwest', 'songshan/shandao3', False),
]
shuyuan=Room('songshan/shuyuan', u'������Ժ', None, 0, exits)

exits = [
	Exit('southdown', 'songshan/shandao3', False),
	Exit('west', 'songshan/songyueta', False),
	Exit('northwest', 'songshan/shandao4', False),
]
songyuesi=Room('songshan/songyuesi', u'������', None, 0, exits)

exits = [
	Exit('east', 'songshan/songyuesi', False),
]
songyueta=Room('songshan/songyueta', u'��������', 'songshan', 0, exits)

exits = [
	Exit('west', 'shaolin/shijie1', False),
	Exit('south', 'shaolin/maowu', False),
	Exit('east', 'shaolin/ruzhou', False),
	Exit('north', 'songshan/tianzhongge', False),
]
taishique=Room('songshan/taishique', u'̫����', 'songshan', 0, exits)

exits = [
	Exit('southdown', 'songshan/fawangsi', False),
]
tayuan=Room('songshan/tayuan', u'��Ժ', 'songshan', 0, exits)

exits = [
	Exit('south', 'songshan/taishique', False),
	Exit('north', 'songshan/chongsheng', False),
]
tianzhongge=Room('songshan/tianzhongge', u'���и�', 'songshan', 0, exits)

exits = [
	Exit('northup', 'songshan/shandao5', False),
	Exit('down', 'songshan/luyanpubu', False),
]
tieliang=Room('songshan/tieliang', u'����Ͽ', 'songshan', 0, exits)

exits = [
	Exit('east', 'songshan/fawangsi', False),
]
yuetai=Room('songshan/yuetai', u'��̨', 'songshan', 0, exits)

