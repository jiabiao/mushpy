# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('southdown', 'taishan/daizong', False),
	Exit('northup', 'taishan/yitian', False),
]
baihe=Room('taishan/baihe', u'�׺�Ȫ', 'taishan', 0, exits)

exits = [
	Exit('westup', 'taishan/bixia', False),
]
baozang=Room('taishan/baozang', u'������', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/zhangren', False),
]
beitian=Room('taishan/beitian', u'������', 'taishan', 0, exits)

exits = [
	Exit('west', 'taishan/weipin', False),
	Exit('eastdown', 'taishan/baozang', False),
]
bixia=Room('taishan/bixia', u'��ϼ��', 'taishan', 0, exits)

exits = [
	Exit('west', 'huanghe/huanghe5', False),
	Exit('south', 'taishan/taishanjiao', False),
	Exit('northup', 'taishan/baihe', False),
]
daizong=Room('taishan/daizong', u'��ڷ�', 'taishan', 0, exits)

exits = [
	Exit('west', 'taishan/tanhai', False),
]
dongtian=Room('taishan/dongtian', u'������', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/yitian', False),
	Exit('eastup', 'taishan/shijin', False),
]
doumo=Room('taishan/doumo', u'��ĸ��', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/huima', False),
	Exit('northup', 'taishan/wudafu', False),
]
ertian=Room('taishan/ertian', u'������', 'taishan', 0, exits)

exits = [
	Exit('down', 'taishan/yuhuang', False),
]
fengchan=Room('taishan/fengchan', u'����̨', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/shijin', False),
	Exit('northup', 'taishan/ertian', False),
]
huima=Room('taishan/huima', u'������', 'taishan', 0, exits)

exits = [
	Exit('west', 'taishan/taishanjiao', False),
	Exit('up', 'taishan/kedian2', False),
]
kedian=Room('taishan/kedian', u'��ջ', None, 0, exits)

exits = [
	Exit('down', 'taishan/kedian', False),
]
kedian2=Room('taishan/kedian2', u'�͵��¥', None, 0, exits)

exits = [
	Exit('northup', 'taishan/shixin', False),
	Exit('westup', 'taishan/tianjie', False),
]
lianhua=Room('taishan/lianhua', u'������', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/wudafu', False),
	Exit('northup', 'taishan/shengxian', False),
]
longmen=Room('taishan/longmen', u'����', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/shengxian', False),
	Exit('west', 'taishan/yueguan', False),
	Exit('northup', 'taishan/yuhuang', False),
	Exit('eastup', 'taishan/tianjie', False),
]
nantian=Room('taishan/nantian', u'������', 'taishan', 0, exits)

exits = [
	Exit('eastup', 'taishan/tanhai', False),
	Exit('westup', 'taishan/yuhuang', False),
]
riguan=Room('taishan/riguan', u'�չ۷�', None, 0, exits)

exits = [
	Exit('southdown', 'taishan/longmen', False),
	Exit('northup', 'taishan/nantian', False),
]
shengxian=Room('taishan/shengxian', u'���ɷ�', 'taishan', 0, exits)

exits = [
	Exit('northup', 'taishan/huima', False),
	Exit('westdown', 'taishan/doumo', False),
]
shijin=Room('taishan/shijin', u'ʯ����', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/lianhua', False),
]
shixin=Room('taishan/shixin', u'����ʯ', 'taishan', 0, exits)

exits = [
	Exit('south', 'taishan/yidao3', False),
	Exit('east', 'taishan/kedian', False),
	Exit('north', 'taishan/daizong', False),
]
taishanjiao=Room('taishan/taishanjiao', u'̩ɽ����', 'taishan', 0, exits)

exits = [
	Exit('east', 'taishan/dongtian', False),
	Exit('westdown', 'taishan/riguan', False),
]
tanhai=Room('taishan/tanhai', u'̽��ʯ', 'taishan', 0, exits)

exits = [
	Exit('eastdown', 'taishan/lianhua', False),
	Exit('eastup', 'taishan/weipin', False),
	Exit('westdown', 'taishan/nantian', False),
]
tianjie=Room('taishan/tianjie', u'���', 'taishan', 0, exits)

exits = [
	Exit('east', 'taishan/bixia', False),
	Exit('westdown', 'taishan/tianjie', False),
]
weipin=Room('taishan/weipin', u'Χ��ɽ', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/ertian', False),
	Exit('northup', 'taishan/longmen', False),
]
wudafu=Room('taishan/wudafu', u'������', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/yueguan', False),
]
xitian=Room('taishan/xitian', u'������', 'taishan', 0, exits)

exits = [
	Exit('west', 'city/dongmen', False),
	Exit('east', 'taishan/yidao1', False),
]
yidao=Room('taishan/yidao', u'�����', 'taishan', 0, exits)

exits = [
	Exit('southeast', 'quanzhou/qzroad1', False),
	Exit('west', 'taishan/yidao', False),
	Exit('northeast', 'taishan/yidao2', False),
]
yidao1=Room('taishan/yidao1', u'�����', 'taishan', 0, exits)

exits = [
	Exit('southwest', 'taishan/yidao1', False),
	Exit('north', 'taishan/yidao3', False),
]
yidao2=Room('taishan/yidao2', u'�����', 'taishan', 0, exits)

exits = [
	Exit('south', 'taishan/yidao2', False),
	Exit('north', 'taishan/taishanjiao', False),
]
yidao3=Room('taishan/yidao3', u'�����', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/baihe', False),
	Exit('northup', 'taishan/doumo', False),
]
yitian=Room('taishan/yitian', u'һ����', 'taishan', 0, exits)

exits = [
	Exit('northup', 'taishan/xitian', False),
	Exit('east', 'taishan/nantian', False),
]
yueguan=Room('taishan/yueguan', u'�¹۷�', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/nantian', False),
	Exit('west', 'taishan/zhangren', False),
	Exit('eastdown', 'taishan/riguan', False),
	Exit('up', 'taishan/fengchan', False),
]
yuhuang=Room('taishan/yuhuang', u'��ʶ�', 'taishan', 0, exits)

exits = [
	Exit('northup', 'taishan/beitian', False),
	Exit('east', 'taishan/yuhuang', False),
]
zhangren=Room('taishan/zhangren', u'���˷�', 'taishan', 0, exits)

