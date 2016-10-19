# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('west', 'guanwai/caoguduo', False),
	Exit('north', 'guanwai/xiaoyuan', False),
	Exit('east', 'guanwai/milin1', False),
]
baihe=Room('guanwai/baihe', u'白河', 'guanwai', 0, exits)

exits = [
	Exit('eastdown', 'guanwai/tianchi1', False),
	Exit('southwest', 'guanwai/yuzhu', False),
	Exit('north', 'guanwai/luming', False),
]
baiyun=Room('guanwai/baiyun', u'白云峰', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/xiaoxiang', False),
	Exit('south', 'guanwai/jishi', False),
]
beicheng=Room('guanwai/beicheng', u'北城', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/chuanchang', False),
	Exit('east', 'guanwai/damenkan', False),
]
bingmian=Room('guanwai/bingmian', u'冰面', 'guanwai', 0, exits)

exits = [
	Exit('northwest', 'guanwai/mantianxing', False),
	Exit('east', 'guanwai/baihe', False),
]
caoguduo=Room('guanwai/caoguduo', u'谷草垛', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/xuedi3', False),
	Exit('east', 'guanwai/bingmian', False),
]
chuanchang=Room('guanwai/chuanchang', u'船厂', 'guanwai', 0, exits)

exits = [
	Exit('east', 'guanwai/shizilu', False),
]
chufang=Room('guanwai/chufang', u'厨房', None, 0, exits)

exits = [
	Exit('northwest', 'guanwai/pubu', False),
	Exit('southwest', 'guanwai/longmen', False),
]
damen=Room('guanwai/damen', u'达门', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/bingmian', False),
	Exit('southeast', 'guanwai/ermenkan', False),
]
damenkan=Room('guanwai/damenkan', u'大门坎子', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/jishi', False),
	Exit('south', 'guanwai/tuyaoguan', False),
	Exit('northeast', 'guanwai/huandi1', False),
	Exit('east', 'guanwai/xuedi1', False),
]
dongcheng=Room('guanwai/dongcheng', u'东城', 'guanwai', 0, exits)

exits = [
	Exit('northwest', 'guanwai/damenkan', False),
	Exit('east', 'guanwai/mantianxing', False),
]
ermenkan=Room('guanwai/ermenkan', u'二门坎子', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/famu1', False),
	Exit('southup', 'guanwai/luming', False),
]
famu=Room('guanwai/famu', u'伐木场', 'guanwai', 0, exits)

exits = [
	Exit('east', 'guanwai/famu', False),
]
famu1=Room('guanwai/famu1', u'伐木场', 'guanwai', 0, exits)

exits = [
	Exit('westdown', 'guanwai/milin3', False),
	Exit('east', 'guanwai/xiaotianchi', False),
]
heifengkou=Room('guanwai/heifengkou', u'黑风口', None, 0, exits)

exits = [
	Exit('west', 'guanwai/jingxiu', False),
	Exit('south', 'guanwai/xiaowu', False),
	Exit('east', 'guanwai/liangong', False),
	Exit('north', 'guanwai/shizilu', False),
]
houyuan=Room('guanwai/houyuan', u'后院', None, 0, exits)

exits = [
	Exit('westdown', 'guanwai/tianchi1', False),
	Exit('north', 'guanwai/tianhuo', False),
]
huagai=Room('guanwai/huagai', u'华盖峰', 'guanwai', 0, exits)

exits = [
	Exit('southwest', 'guanwai/dongcheng', False),
	Exit('northeast', 'guanwai/huandi2', False),
]
huandi1=Room('guanwai/huandi1', u'荒路', 'guanwai', 0, exits)

exits = [
	Exit('southwest', 'guanwai/huandi1', False),
	Exit('enter', 'guanwai/shanshenmiao', False),
]
huandi2=Room('guanwai/huandi2', u'荒路', 'guanwai', 0, exits)

exits = [
	Exit('east', 'guanwai/houyuan', False),
]
jingxiu=Room('guanwai/jingxiu', u'静修室', None, 0, exits)

exits = [
	Exit('west', 'guanwai/kedian', False),
	Exit('south', 'guanwai/nancheng', False),
	Exit('east', 'guanwai/dongcheng', False),
	Exit('north', 'guanwai/beicheng', False),
]
jishi=Room('guanwai/jishi', u'集市', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/majiu', False),
	Exit('up', 'guanwai/kedian2', False),
	Exit('east', 'guanwai/jishi', False),
]
kedian=Room('guanwai/kedian', u'客店', None, 0, exits)

exits = [
	Exit('down', 'guanwai/kedian', False),
]
kedian2=Room('guanwai/kedian2', u'客店二楼', None, 0, exits)

exits = [
	Exit('northwest', 'guanwai/shanhaiguan', False),
	Exit('southwest', 'beijing/road3', False),
]
laolongtou=Room('guanwai/laolongtou', u'老龙头', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/houyuan', False),
	Exit('south', 'guanwai/liangongs', False),
	Exit('east', 'guanwai/liangonge', False),
]
liangong=Room('guanwai/liangong', u'练功房', None, 0, exits)

exits = [
	Exit('west', 'guanwai/liangong', False),
]
liangonge=Room('guanwai/liangonge', u'东练功房', None, 0, exits)

exits = [
	Exit('north', 'guanwai/liangong', False),
]
liangongs=Room('guanwai/liangongs', u'南练功房', None, 0, exits)

exits = [
	Exit('southdown', 'guanwai/tianchi1', False),
	Exit('west', 'guanwai/luming', False),
	Exit('east', 'guanwai/tianhuo', False),
	Exit('northeast', 'guanwai/damen', False),
]
longmen=Room('guanwai/longmen', u'龙门峰', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/baiyun', False),
	Exit('northdown', 'guanwai/famu', False),
	Exit('east', 'guanwai/longmen', False),
]
luming=Room('guanwai/luming', u'鹿鸣峰', 'guanwai', 0, exits)

exits = [
	Exit('east', 'guanwai/kedian', False),
]
majiu=Room('guanwai/majiu', u'马厩', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/ermenkan', False),
	Exit('southeast', 'guanwai/caoguduo', False),
]
mantianxing=Room('guanwai/mantianxing', u'满天星', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/baihe', False),
	Exit('eastup', 'guanwai/milin2', False),
]
milin1=Room('guanwai/milin1', u'密林', 'guanwai', 0, exits)

exits = [
	Exit('southup', 'guanwai/milin3', False),
	Exit('westdown', 'guanwai/milin1', False),
]
milin2=Room('guanwai/milin2', u'密林', 'guanwai', 0, exits)

exits = [
	Exit('eastup', 'guanwai/heifengkou', False),
	Exit('northdown', 'guanwai/milin2', False),
]
milin3=Room('guanwai/milin3', u'密林', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/road8', False),
	Exit('north', 'guanwai/nancheng', False),
]
muqiao=Room('guanwai/muqiao', u'木桥', 'guanwai', 0, exits)

exits = [
	Exit('southeast', 'guanwai/tulu', False),
	Exit('west', 'guanwai/rouguan', False),
	Exit('south', 'guanwai/muqiao', False),
	Exit('north', 'guanwai/jishi', False),
]
nancheng=Room('guanwai/nancheng', u'南城', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/road3', False),
	Exit('northeast', 'guanwai/road4', False),
]
ningyuan=Room('guanwai/ningyuan', u'宁远', 'guanwai', 0, exits)

exits = [
	Exit('southeast', 'guanwai/damen', False),
	Exit('westdown', 'guanwai/xiaotianchi', False),
]
pubu=Room('guanwai/pubu', u'长白瀑布', 'guanwai', 0, exits)

exits = [
	Exit('southwest', 'guanwai/shanhaiguan', False),
	Exit('northeast', 'guanwai/road2', False),
]
road1=Room('guanwai/road1', u'官道', 'guanwai', 0, exits)

exits = [
	Exit('southwest', 'guanwai/road1', False),
	Exit('northeast', 'guanwai/road3', False),
]
road2=Room('guanwai/road2', u'官道', 'guanwai', 0, exits)

exits = [
	Exit('southwest', 'guanwai/road2', False),
	Exit('north', 'guanwai/ningyuan', False),
]
road3=Room('guanwai/road3', u'官道', 'guanwai', 0, exits)

exits = [
	Exit('southwest', 'guanwai/ningyuan', False),
	Exit('northeast', 'guanwai/road5', False),
]
road4=Room('guanwai/road4', u'大道', 'guanwai', 0, exits)

exits = [
	Exit('southwest', 'guanwai/road4', False),
	Exit('north', 'guanwai/road6', False),
]
road5=Room('guanwai/road5', u'大道', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/road5', False),
	Exit('north', 'guanwai/road7', False),
]
road6=Room('guanwai/road6', u'大道', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/road6', False),
	Exit('north', 'guanwai/road8', False),
]
road7=Room('guanwai/road7', u'大道', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/road7', False),
	Exit('north', 'guanwai/muqiao', False),
]
road8=Room('guanwai/road8', u'大道', 'guanwai', 0, exits)

exits = [
	Exit('east', 'guanwai/nancheng', False),
]
rouguan=Room('guanwai/rouguan', u'香肉馆', None, 0, exits)

exits = [
	Exit('southeast', 'guanwai/laolongtou', False),
	Exit('northeast', 'guanwai/road1', False),
]
shanhaiguan=Room('guanwai/shanhaiguan', u'山海关', 'guanwai', 0, exits)

exits = [
	Exit('out', 'guanwai/huandi2', False),
]
shanshenmiao=Room('guanwai/shanshenmiao', u'山神庙', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/tulu', False),
]
shichang=Room('guanwai/shichang', u'采石场', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/chufang', False),
	Exit('south', 'guanwai/houyuan', False),
	Exit('east', 'guanwai/taxue', False),
]
shizilu=Room('guanwai/shizilu', u'石路', None, 0, exits)

exits = [
]
songhuajiang=Room('guanwai/songhuajiang', u'松花江面', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/shizilu', False),
]
taxue=Room('guanwai/taxue', u'踏雪院', None, 0, exits)

exits = [
	Exit('eastup', 'guanwai/huagai', False),
	Exit('northup', 'guanwai/longmen', False),
	Exit('south', 'guanwai/tianchi2', False),
	Exit('westup', 'guanwai/baiyun', False),
]
tianchi1=Room('guanwai/tianchi1', u'白头山天池', 'guanwai', 0, exits)

exits = [
	Exit('north', 'guanwai/tianchi1', False),
]
tianchi2=Room('guanwai/tianchi2', u'白头山天池', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/longmen', False),
	Exit('south', 'guanwai/huagai', False),
]
tianhuo=Room('guanwai/tianhuo', u'天豁峰', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/yuzhu', False),
]
tiyun=Room('guanwai/tiyun', u'梯云峰', 'guanwai', 0, exits)

exits = [
	Exit('northwest', 'guanwai/nancheng', False),
	Exit('east', 'guanwai/shichang', False),
]
tulu=Room('guanwai/tulu', u'土路', 'guanwai', 0, exits)

exits = [
	Exit('north', 'guanwai/xiaoxiang', False),
]
tuwu=Room('guanwai/tuwu', u'小土屋', 'guanwai', 0, exits)

exits = [
	Exit('north', 'guanwai/dongcheng', False),
]
tuyaoguan=Room('guanwai/tuyaoguan', u'土窑馆', None, 0, exits)

exits = [
	Exit('west', 'guanwai/heifengkou', False),
	Exit('eastup', 'guanwai/pubu', False),
]
xiaotianchi=Room('guanwai/xiaotianchi', u'小天池', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/xiaoyuan', False),
	Exit('north', 'guanwai/houyuan', False),
]
xiaowu=Room('guanwai/xiaowu', u'小茅屋', None, 0, exits)

exits = [
	Exit('south', 'guanwai/tuwu', False),
	Exit('east', 'guanwai/beicheng', False),
]
xiaoxiang=Room('guanwai/xiaoxiang', u'小巷', 'guanwai', 0, exits)

exits = [
	Exit('south', 'guanwai/baihe', False),
	Exit('north', 'guanwai/xiaowu', False),
]
xiaoyuan=Room('guanwai/xiaoyuan', u'小院子', None, 0, exits)

exits = [
]
xiuxishi=Room('guanwai/xiuxishi', u'休息室', None, 0, exits)

exits = [
	Exit('west', 'guanwai/dongcheng', False),
	Exit('northeast', 'guanwai/xuedi2', False),
]
xuedi1=Room('guanwai/xuedi1', u'雪地', 'guanwai', 0, exits)

exits = [
	Exit('southwest', 'guanwai/xuedi1', False),
	Exit('east', 'guanwai/xuedi3', False),
]
xuedi2=Room('guanwai/xuedi2', u'雪地', 'guanwai', 0, exits)

exits = [
	Exit('west', 'guanwai/xuedi2', False),
	Exit('north', 'guanwai/chuanchang', False),
]
xuedi3=Room('guanwai/xuedi3', u'雪地', 'guanwai', 0, exits)

exits = [
	Exit('northeast', 'guanwai/baiyun', False),
	Exit('north', 'guanwai/tiyun', False),
]
yuzhu=Room('guanwai/yuzhu', u'玉柱峰', 'guanwai', 0, exits)

