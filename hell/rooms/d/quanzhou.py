# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'quanzhou/zhongxin', False),
	Exit('north', 'fuzhou/puxian', False),
]
beimen=Room('quanzhou/beimen', u'泉州北门', 'quanzhou', 0, exits)

exits = [
	Exit('west', 'quanzhou/qzroad4', False),
]
chating=Room('quanzhou/chating', u'茶亭', 'quanzhou', 0, exits)

exits = [
	Exit('south', 'quanzhou/dagou', False),
	Exit('eastup', 'quanzhou/riyuetang', False),
	Exit('north', 'quanzhou/jilong', False),
]
chiqian=Room('quanzhou/chiqian', u'赤嵌城', 'quanzhou', 0, exits)

exits = [
	Exit('north', 'quanzhou/chiqian', False),
]
dagou=Room('quanzhou/dagou', u'打狗港', 'quanzhou', 0, exits)

exits = [
]
dahai=Room('quanzhou/dahai', u'大海', 'taohua', 0, exits)

exits = [
	Exit('west', 'quanzhou/zhongxin', False),
]
haigang=Room('quanzhou/haigang', u'海港', 'quanzhou', 0, exits)

exits = [
	Exit('west', 'quanzhou/qzroad2', False),
	Exit('south', 'quanzhou/jxnanmen', False),
	Exit('east', 'quanzhou/nanhu', False),
]
jiaxing=Room('quanzhou/jiaxing', u'嘉兴城', 'jiaxing', 0, exits)

exits = [
	Exit('west', 'quanzhou/nanhu', False),
]
jiaxinggang=Room('quanzhou/jiaxinggang', u'嘉兴海港', 'quanzhou', 0, exits)

exits = [
	Exit('south', 'quanzhou/chiqian', False),
]
jilong=Room('quanzhou/jilong', u'鸡笼港', 'quanzhou', 0, exits)

exits = [
	Exit('southeast', 'hangzhou/road1', False),
	Exit('south', 'quanzhou/qzroad4', False),
	Exit('southwest', 'quanzhou/majiu2', False),
	Exit('east', 'quanzhou/tieqiang', False),
	Exit('north', 'quanzhou/jiaxing', False),
]
jxnanmen=Room('quanzhou/jxnanmen', u'嘉兴南门', 'jiaxing', 0, exits)

exits = [
	Exit('northwest', 'quanzhou/zhongxin', False),
]
majiu1=Room('quanzhou/majiu1', u'马厩', 'quanzhou', 0, exits)

exits = [
	Exit('northeast', 'quanzhou/jxnanmen', False),
]
majiu2=Room('quanzhou/majiu2', u'马厩', 'jiaxing', 0, exits)

exits = [
	Exit('southeast', 'quanzhou/nanhu1', False),
	Exit('west', 'quanzhou/jiaxing', False),
	Exit('south', 'quanzhou/tieqiang', False),
	Exit('east', 'quanzhou/jiaxinggang', False),
]
nanhu=Room('quanzhou/nanhu', u'嘉兴南湖', 'jiaxing', 0, exits)

exits = [
	Exit('northwest', 'quanzhou/nanhu', False),
	Exit('south', 'quanzhou/yanyu', False),
]
nanhu1=Room('quanzhou/nanhu1', u'嘉兴南湖', 'jiaxing', 0, exits)

exits = [
	Exit('north', 'quanzhou/zhongxin', False),
]
nanmen=Room('quanzhou/nanmen', u'泉州南门', 'quanzhou', 0, exits)

exits = [
]
penghu=Room('quanzhou/penghu', u'澎湖岛', 'quanzhou', 0, exits)

exits = [
	Exit('northwest', 'taishan/yidao1', False),
	Exit('south', 'quanzhou/qzroad2', False),
]
qzroad1=Room('quanzhou/qzroad1', u'山路', 'quanzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/dongmen', False),
	Exit('south', 'quanzhou/qzroad3', False),
	Exit('east', 'quanzhou/jiaxing', False),
	Exit('north', 'quanzhou/qzroad1', False),
]
qzroad2=Room('quanzhou/qzroad2', u'山路', 'quanzhou', 0, exits)

exits = [
	Exit('east', 'quanzhou/qzroad4', False),
	Exit('north', 'quanzhou/qzroad2', False),
]
qzroad3=Room('quanzhou/qzroad3', u'山路', 'quanzhou', 0, exits)

exits = [
	Exit('west', 'quanzhou/qzroad3', False),
	Exit('southup', 'fuzhou/fzroad1', False),
	Exit('east', 'quanzhou/chating', False),
	Exit('north', 'quanzhou/jxnanmen', False),
]
qzroad4=Room('quanzhou/qzroad4', u'山路', 'quanzhou', 0, exits)

exits = [
	Exit('westdown', 'quanzhou/chiqian', False),
]
riyuetang=Room('quanzhou/riyuetang', u'日月潭', 'quanzhou', 0, exits)

exits = [
	Exit('west', 'quanzhou/jxnanmen', False),
	Exit('north', 'quanzhou/nanhu', False),
]
tieqiang=Room('quanzhou/tieqiang', u'铁枪庙', 'jiaxing', 0, exits)

exits = [
	Exit('west', 'foshan/road14', False),
	Exit('east', 'quanzhou/ximen', False),
]
westbridge=Room('quanzhou/westbridge', u'西门吊桥', 'foshan', 0, exits)

exits = [
	Exit('west', 'quanzhou/zahuopu', False),
	Exit('north', 'quanzhou/laozhai', False),
	Exit('east', 'quanzhou/zhongxin', False),
]
xijie=Room('quanzhou/xijie', u'西街', 'quanzhou', 0, exits)

exits = [
	Exit('west', 'quanzhou/westbridge', False),
	Exit('east', 'quanzhou/zhongxin', False),
]
ximen=Room('quanzhou/ximen', u'泉州西门', 'quanzhou', 0, exits)

exits = [
	Exit('north', 'quanzhou/nanhu1', False),
	Exit('up', 'quanzhou/yanyu2', False),
]
yanyu=Room('quanzhou/yanyu', u'烟雨楼', None, 0, exits)

exits = [
	Exit('down', 'quanzhou/yanyu', False),
]
yanyu2=Room('quanzhou/yanyu2', u'烟雨楼二楼', None, 0, exits)

exits = [
	Exit('southeast', 'quanzhou/majiu1', False),
	Exit('west', 'quanzhou/ximen', False),
	Exit('south', 'quanzhou/nanmen', False),
	Exit('east', 'quanzhou/haigang', False),
	Exit('north', 'quanzhou/beimen', False),
]
zhongxin=Room('quanzhou/zhongxin', u'城中心', 'quanzhou', 0, exits)

