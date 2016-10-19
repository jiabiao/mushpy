# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('southdown', 'taishan/daizong', False),
	Exit('northup', 'taishan/yitian', False),
]
baihe=Room('taishan/baihe', u'白鹤泉', 'taishan', 0, exits)

exits = [
	Exit('westup', 'taishan/bixia', False),
]
baozang=Room('taishan/baozang', u'宝藏岭', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/zhangren', False),
]
beitian=Room('taishan/beitian', u'北天门', 'taishan', 0, exits)

exits = [
	Exit('west', 'taishan/weipin', False),
	Exit('eastdown', 'taishan/baozang', False),
]
bixia=Room('taishan/bixia', u'碧霞祠', 'taishan', 0, exits)

exits = [
	Exit('west', 'huanghe/huanghe5', False),
	Exit('south', 'taishan/taishanjiao', False),
	Exit('northup', 'taishan/baihe', False),
]
daizong=Room('taishan/daizong', u'岱宗坊', 'taishan', 0, exits)

exits = [
	Exit('west', 'taishan/tanhai', False),
]
dongtian=Room('taishan/dongtian', u'东天门', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/yitian', False),
	Exit('eastup', 'taishan/shijin', False),
]
doumo=Room('taishan/doumo', u'斗母宫', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/huima', False),
	Exit('northup', 'taishan/wudafu', False),
]
ertian=Room('taishan/ertian', u'二天门', 'taishan', 0, exits)

exits = [
	Exit('down', 'taishan/yuhuang', False),
]
fengchan=Room('taishan/fengchan', u'封禅台', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/shijin', False),
	Exit('northup', 'taishan/ertian', False),
]
huima=Room('taishan/huima', u'回马岭', 'taishan', 0, exits)

exits = [
	Exit('west', 'taishan/taishanjiao', False),
	Exit('up', 'taishan/kedian2', False),
]
kedian=Room('taishan/kedian', u'客栈', None, 0, exits)

exits = [
	Exit('down', 'taishan/kedian', False),
]
kedian2=Room('taishan/kedian2', u'客店二楼', None, 0, exits)

exits = [
	Exit('northup', 'taishan/shixin', False),
	Exit('westup', 'taishan/tianjie', False),
]
lianhua=Room('taishan/lianhua', u'莲花峰', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/wudafu', False),
	Exit('northup', 'taishan/shengxian', False),
]
longmen=Room('taishan/longmen', u'龙门', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/shengxian', False),
	Exit('west', 'taishan/yueguan', False),
	Exit('northup', 'taishan/yuhuang', False),
	Exit('eastup', 'taishan/tianjie', False),
]
nantian=Room('taishan/nantian', u'南天门', 'taishan', 0, exits)

exits = [
	Exit('eastup', 'taishan/tanhai', False),
	Exit('westup', 'taishan/yuhuang', False),
]
riguan=Room('taishan/riguan', u'日观峰', None, 0, exits)

exits = [
	Exit('southdown', 'taishan/longmen', False),
	Exit('northup', 'taishan/nantian', False),
]
shengxian=Room('taishan/shengxian', u'升仙坊', 'taishan', 0, exits)

exits = [
	Exit('northup', 'taishan/huima', False),
	Exit('westdown', 'taishan/doumo', False),
]
shijin=Room('taishan/shijin', u'石经峪', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/lianhua', False),
]
shixin=Room('taishan/shixin', u'试心石', 'taishan', 0, exits)

exits = [
	Exit('south', 'taishan/yidao3', False),
	Exit('east', 'taishan/kedian', False),
	Exit('north', 'taishan/daizong', False),
]
taishanjiao=Room('taishan/taishanjiao', u'泰山脚下', 'taishan', 0, exits)

exits = [
	Exit('east', 'taishan/dongtian', False),
	Exit('westdown', 'taishan/riguan', False),
]
tanhai=Room('taishan/tanhai', u'探海石', 'taishan', 0, exits)

exits = [
	Exit('eastdown', 'taishan/lianhua', False),
	Exit('eastup', 'taishan/weipin', False),
	Exit('westdown', 'taishan/nantian', False),
]
tianjie=Room('taishan/tianjie', u'天街', 'taishan', 0, exits)

exits = [
	Exit('east', 'taishan/bixia', False),
	Exit('westdown', 'taishan/tianjie', False),
]
weipin=Room('taishan/weipin', u'围屏山', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/ertian', False),
	Exit('northup', 'taishan/longmen', False),
]
wudafu=Room('taishan/wudafu', u'五大夫松', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/yueguan', False),
]
xitian=Room('taishan/xitian', u'西天门', 'taishan', 0, exits)

exits = [
	Exit('west', 'city/dongmen', False),
	Exit('east', 'taishan/yidao1', False),
]
yidao=Room('taishan/yidao', u'大驿道', 'taishan', 0, exits)

exits = [
	Exit('southeast', 'quanzhou/qzroad1', False),
	Exit('west', 'taishan/yidao', False),
	Exit('northeast', 'taishan/yidao2', False),
]
yidao1=Room('taishan/yidao1', u'大驿道', 'taishan', 0, exits)

exits = [
	Exit('southwest', 'taishan/yidao1', False),
	Exit('north', 'taishan/yidao3', False),
]
yidao2=Room('taishan/yidao2', u'大驿道', 'taishan', 0, exits)

exits = [
	Exit('south', 'taishan/yidao2', False),
	Exit('north', 'taishan/taishanjiao', False),
]
yidao3=Room('taishan/yidao3', u'大驿道', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/baihe', False),
	Exit('northup', 'taishan/doumo', False),
]
yitian=Room('taishan/yitian', u'一天门', 'taishan', 0, exits)

exits = [
	Exit('northup', 'taishan/xitian', False),
	Exit('east', 'taishan/nantian', False),
]
yueguan=Room('taishan/yueguan', u'月观峰', 'taishan', 0, exits)

exits = [
	Exit('southdown', 'taishan/nantian', False),
	Exit('west', 'taishan/zhangren', False),
	Exit('eastdown', 'taishan/riguan', False),
	Exit('up', 'taishan/fengchan', False),
]
yuhuang=Room('taishan/yuhuang', u'玉皇顶', 'taishan', 0, exits)

exits = [
	Exit('northup', 'taishan/beitian', False),
	Exit('east', 'taishan/yuhuang', False),
]
zhangren=Room('taishan/zhangren', u'丈人峰', 'taishan', 0, exits)

