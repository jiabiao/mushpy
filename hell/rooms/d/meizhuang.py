# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'meizhuang/zoulang3', False),
]
chufang=Room('meizhuang/chufang', u'厨房', None, 0, exits)

exits = [
	Exit('south', 'meizhuang/tianjing', False),
	Exit('north', 'meizhuang/keting', False),
]
dating=Room('meizhuang/dating', u'四雅清风', None, 0, exits)

exits = [
	Exit('out', 'meizhuang/keting', False),
	Exit('west', 'meizhuang/didao2', False),
	Exit('south', 'meizhuang/didao1', False),
	Exit('east', 'meizhuang/didao1', False),
	Exit('north', 'meizhuang/didao2', False),
]
didao1=Room('meizhuang/didao1', u'梅庄密道', None, 0, exits)

exits = [
	Exit('west', 'meizhuang/didao2', False),
	Exit('south', 'meizhuang/didao1', False),
	Exit('east', 'meizhuang/didao1', False),
	Exit('north', 'meizhuang/didao3', False),
]
didao2=Room('meizhuang/didao2', u'梅庄密道', None, 0, exits)

exits = [
	Exit('south', 'meizhuang/didao2', False),
]
didao3=Room('meizhuang/didao3', u'梅庄密道', None, 0, exits)

exits = [
	Exit('up', 'meizhuang/didao3', False),
	Exit('north', 'meizhuang/didao5', False),
]
didao4=Room('meizhuang/didao4', u'甬道', None, 0, exits)

exits = [
	Exit('west', 'meizhuang/didao5', False),
	Exit('south', 'meizhuang/didao4', False),
	Exit('east', 'meizhuang/didao4', False),
	Exit('north', 'meizhuang/didao6', False),
]
didao5=Room('meizhuang/didao5', u'甬道', None, 0, exits)

exits = [
	Exit('west', 'meizhuang/didao4', False),
	Exit('south', 'meizhuang/didao7', False),
	Exit('north', 'meizhuang/didao5', False),
	Exit('east', 'meizhuang/didao6', False),
]
didao6=Room('meizhuang/didao6', u'梅庄密道', None, 0, exits)

exits = [
	Exit('west', 'meizhuang/didao6', False),
	Exit('north', 'meizhuang/laofang', False),
]
didao7=Room('meizhuang/didao7', u'梅庄密道', None, 0, exits)

exits = [
	Exit('down', 'meizhuang/mishi', False),
]
dingduan=Room('meizhuang/dingduan', u'书架顶部', None, 0, exits)

exits = [
	Exit('south', 'meizhuang/xiaolu', False),
]
gate=Room('meizhuang/gate', u'梅庄大门', 'meizhuang', 0, exits)

exits = [
	Exit('west', 'meizhuang/zoulang1', False),
]
huashi=Room('meizhuang/huashi', u'画室', None, 0, exits)

exits = [
	Exit('west', 'quanzhou/nanhu1', False),
	Exit('north', 'meizhuang/xiaolu', False),
]
hupan=Room('meizhuang/hupan', u'南湖湖畔', None, 0, exits)

exits = [
	Exit('south', 'meizhuang/dating', False),
	Exit('north', 'meizhuang/senlin1', False),
]
keting=Room('meizhuang/keting', u'迎客亭', None, 0, exits)

exits = [
	Exit('south', 'meizhuang/didao7', False),
]
laofang=Room('meizhuang/laofang', u'牢房', None, 0, exits)

exits = [
	Exit('out', 'meizhuang/hupan', False),
	Exit('south', 'meizhuang/didao5', False),
]
lingmu=Room('meizhuang/lingmu', u'古皇陵', None, 0, exits)

exits = [
	Exit('out', 'meizhuang/neitang', False),
]
mishi=Room('meizhuang/mishi', u'密室', None, 0, exits)

exits = [
	Exit('west', 'meizhuang/xiaoyuan', False),
]
mishi2=Room('meizhuang/mishi2', u'柳园', 'meizhuang', 0, exits)

exits = [
	Exit('east', 'meizhuang/senlin1', False),
]
neitang=Room('meizhuang/neitang', u'偏房', None, 0, exits)

exits = [
	Exit('south', 'meizhuang/senlin1', False),
	Exit('north', 'meizhuang/zoulang1', False),
]
neiyuan=Room('meizhuang/neiyuan', u'内院', 'meizhuang', 0, exits)

exits = [
	Exit('eastup', 'meizhuang/xiaodao', False),
	Exit('north', 'meizhuang/senlin1', False),
]
qhpo=Room('meizhuang/qhpo', u'奇槐坡', 'meizhuang', 0, exits)

exits = [
	Exit('east', 'meizhuang/zoulang2', False),
]
qishi=Room('meizhuang/qishi', u'棋室', None, 0, exits)

exits = [
	Exit('west', 'meizhuang/neitang', False),
	Exit('south', 'meizhuang/keting', False),
	Exit('east', 'meizhuang/senlin2', False),
	Exit('north', 'meizhuang/neiyuan', False),
]
senlin1=Room('meizhuang/senlin1', u'百木园', 'meizhuang', 0, exits)

exits = [
	Exit('west', 'meizhuang/senlin3', False),
	Exit('south', 'meizhuang/senlin9', False),
	Exit('east', 'meizhuang/senlin6', False),
	Exit('north', 'meizhuang/senlin7', False),
]
senlin10=Room('meizhuang/senlin10', u'百木园', 'meizhuang', 0, exits)

exits = [
	Exit('west', 'meizhuang/senlin2', False),
	Exit('south', 'meizhuang/senlin3', False),
	Exit('east', 'meizhuang/senlin2', False),
	Exit('north', 'meizhuang/senlin3', False),
]
senlin2=Room('meizhuang/senlin2', u'百木园', 'meizhuang', 0, exits)

exits = [
	Exit('west', 'meizhuang/senlin3', False),
	Exit('south', 'meizhuang/senlin4', False),
	Exit('east', 'meizhuang/senlin1', False),
	Exit('north', 'meizhuang/senlin2', False),
]
senlin3=Room('meizhuang/senlin3', u'百木园', 'meizhuang', 0, exits)

exits = [
	Exit('west', 'meizhuang/senlin5', False),
	Exit('south', 'meizhuang/senlin4', False),
	Exit('east', 'meizhuang/senlin2', False),
	Exit('north', 'meizhuang/senlin3', False),
]
senlin4=Room('meizhuang/senlin4', u'百木园', 'meizhuang', 0, exits)

exits = [
	Exit('west', 'meizhuang/senlin2', False),
	Exit('southeast', 'meizhuang/senlin4', False),
	Exit('northwest', 'meizhuang/senlin4', False),
	Exit('south', 'meizhuang/senlin5', False),
	Exit('southwest', 'meizhuang/senlin6', False),
	Exit('north', 'meizhuang/senlin3', False),
	Exit('east', 'meizhuang/senlin2', False),
	Exit('northeast', 'meizhuang/senlin2', False),
]
senlin5=Room('meizhuang/senlin5', u'百木园', 'meizhuang', 0, exits)

exits = [
	Exit('west', 'meizhuang/senlin3', False),
	Exit('south', 'meizhuang/senlin7', False),
	Exit('east', 'meizhuang/senlin8', False),
	Exit('north', 'meizhuang/senlin4', False),
]
senlin6=Room('meizhuang/senlin6', u'百木园', 'meizhuang', 0, exits)

exits = [
	Exit('west', 'meizhuang/senlin3', False),
	Exit('south', 'meizhuang/senlin6', False),
	Exit('north', 'meizhuang/senlin2', False),
	Exit('east', 'meizhuang/senlin4', False),
]
senlin7=Room('meizhuang/senlin7', u'百木园', 'meizhuang', 0, exits)

exits = [
	Exit('west', 'meizhuang/senlin5', False),
	Exit('south', 'meizhuang/qhpo', False),
	Exit('east', 'meizhuang/senlin2', False),
	Exit('north', 'meizhuang/senlin7', False),
]
senlin8=Room('meizhuang/senlin8', u'百木园', 'meizhuang', 0, exits)

exits = [
	Exit('west', 'meizhuang/senlin7', False),
	Exit('south', 'meizhuang/senlin2', False),
	Exit('east', 'meizhuang/senlin3', False),
	Exit('north', 'meizhuang/senlin5', False),
]
senlin9=Room('meizhuang/senlin9', u'百木园', 'meizhuang', 0, exits)

exits = [
	Exit('eastdown', 'hangzhou/gushan', False),
	Exit('north', 'meizhuang/xiaolu', False),
]
shijie=Room('meizhuang/shijie', u'孤山石级', None, 0, exits)

exits = [
	Exit('east', 'meizhuang/zoulang1', False),
]
shushi=Room('meizhuang/shushi', u'书室', 'meizhuang', 0, exits)

exits = [
	Exit('north', 'meizhuang/dating', False),
]
tianjing=Room('meizhuang/tianjing', u'大天井', 'meizhuang', 0, exits)

exits = [
	Exit('westdown', 'meizhuang/qhpo', False),
	Exit('north', 'meizhuang/xiaoyuan', False),
]
xiaodao=Room('meizhuang/xiaodao', u'小路', 'meizhuang', 0, exits)

exits = [
	Exit('south', 'meizhuang/shijie', False),
	Exit('north', 'meizhuang/gate', False),
]
xiaolu=Room('meizhuang/xiaolu', u'蜿蜒小径', 'meizhuang', 0, exits)

exits = [
	Exit('out', 'meizhuang/xiaoyuan', False),
]
xiaowu=Room('meizhuang/xiaowu', u'小屋', 'meizhuang', 0, exits)

exits = [
	Exit('south', 'meizhuang/xiaodao', False),
	Exit('enter', 'meizhuang/xiaowu', False),
]
xiaoyuan=Room('meizhuang/xiaoyuan', u'琴音小院', 'meizhuang', 0, exits)

exits = [
	Exit('west', 'meizhuang/zoulang2', False),
]
xiuxishi=Room('meizhuang/xiuxishi', u'休息室', None, 0, exits)

exits = [
	Exit('west', 'meizhuang/shushi', False),
	Exit('south', 'meizhuang/neiyuan', False),
	Exit('north', 'meizhuang/zoulang2', False),
	Exit('east', 'meizhuang/huashi', False),
]
zoulang1=Room('meizhuang/zoulang1', u'走廊', None, 0, exits)

exits = [
	Exit('west', 'meizhuang/qishi', False),
	Exit('south', 'meizhuang/zoulang1', False),
	Exit('north', 'meizhuang/zoulang3', False),
	Exit('east', 'meizhuang/xiuxishi', False),
]
zoulang2=Room('meizhuang/zoulang2', u'走廊', None, 0, exits)

exits = [
	Exit('south', 'meizhuang/zoulang2', False),
	Exit('north', 'meizhuang/chufang', False),
]
zoulang3=Room('meizhuang/zoulang3', u'走廊', None, 0, exits)

