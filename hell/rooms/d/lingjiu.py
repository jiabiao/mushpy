# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'lingjiu/men3', False),
]
biguan=Room('lingjiu/biguan', u'闭关室', None, 0, exits)

exits = [
	Exit('south', 'lingjiu/changl10', False),
]
caifeng=Room('lingjiu/caifeng', u'潇湘馆', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/changl5', False),
	Exit('east', 'lingjiu/huayuan', False),
]
changl1=Room('lingjiu/changl1', u'画廊', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/changl13', False),
	Exit('south', 'lingjiu/changl3', False),
	Exit('north', 'lingjiu/caifeng', False),
	Exit('east', 'lingjiu/changl14', False),
]
changl10=Room('lingjiu/changl10', u'画廊', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/men1', False),
	Exit('east', 'lingjiu/changl9', False),
]
changl11=Room('lingjiu/changl11', u'画廊', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/changl9', False),
	Exit('east', 'lingjiu/men2', False),
]
changl12=Room('lingjiu/changl12', u'画廊', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/xuanbing', False),
	Exit('east', 'lingjiu/changl10', False),
]
changl13=Room('lingjiu/changl13', u'画廊', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/changl10', False),
	Exit('east', 'lingjiu/daban', False),
]
changl14=Room('lingjiu/changl14', u'画廊', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/changl7', False),
	Exit('south', 'lingjiu/dating', False),
	Exit('north', 'lingjiu/huayuan', False),
	Exit('east', 'lingjiu/changl8', False),
]
changl15=Room('lingjiu/changl15', u'画廊', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/huayuan', False),
	Exit('east', 'lingjiu/changl3', False),
]
changl2=Room('lingjiu/changl2', u'画廊', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/changl2', False),
	Exit('south', 'lingjiu/changl4', False),
	Exit('north', 'lingjiu/changl10', False),
	Exit('east', 'lingjiu/restroom', False),
]
changl3=Room('lingjiu/changl3', u'画廊', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/changl8', False),
	Exit('east', 'lingjiu/liangong', False),
	Exit('north', 'lingjiu/changl3', False),
]
changl4=Room('lingjiu/changl4', u'画廊', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/wuqiku', False),
	Exit('south', 'lingjiu/changl6', False),
	Exit('north', 'lingjiu/changl9', False),
	Exit('east', 'lingjiu/changl1', False),
]
changl5=Room('lingjiu/changl5', u'画廊', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/chufang', False),
	Exit('east', 'lingjiu/changl7', False),
	Exit('north', 'lingjiu/changl5', False),
]
changl6=Room('lingjiu/changl6', u'画廊', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/changl6', False),
	Exit('east', 'lingjiu/changl15', False),
]
changl7=Room('lingjiu/changl7', u'画廊', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/changl15', False),
	Exit('east', 'lingjiu/changl4', False),
]
changl8=Room('lingjiu/changl8', u'画廊', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/changl11', False),
	Exit('south', 'lingjiu/changl5', False),
	Exit('east', 'lingjiu/changl12', False),
]
changl9=Room('lingjiu/changl9', u'画廊', None, 0, exits)

exits = [
	Exit('east', 'lingjiu/changl6', False),
]
chufang=Room('lingjiu/chufang', u'藕香榭', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/changl14', False),
]
daban=Room('lingjiu/daban', u'缀锦阁', None, 0, exits)

exits = [
	Exit('westdown', 'lingjiu/xianchou', False),
	Exit('north', 'lingjiu/dadao2', False),
]
dadao1=Room('lingjiu/dadao1', u'青石大道', 'lingjiu', 0, exits)

exits = [
	Exit('south', 'lingjiu/dadao1', False),
	Exit('north', 'lingjiu/damen', False),
]
dadao2=Room('lingjiu/dadao2', u'青石大道', 'lingjiu', 0, exits)

exits = [
	Exit('south', 'lingjiu/dadao2', False),
	Exit('north', 'lingjiu/dating', False),
]
damen=Room('lingjiu/damen', u'独尊厅大门', 'lingjiu', 0, exits)

exits = [
	Exit('south', 'lingjiu/damen', False),
	Exit('north', 'lingjiu/changl15', False),
]
dating=Room('lingjiu/dating', u'独尊厅', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/changl1', False),
	Exit('south', 'lingjiu/changl15', False),
	Exit('east', 'lingjiu/changl2', False),
	Exit('north', 'lingjiu/xiaodao1', False),
]
huayuan=Room('lingjiu/huayuan', u'花园', 'lingjiu', 0, exits)

exits = [
	Exit('southdown', 'lingjiu/yan', False),
]
jian=Room('lingjiu/jian', u'百丈涧', 'lingjiu', 0, exits)

exits = [
	Exit('west', 'lingjiu/changl4', False),
	Exit('up', 'lingjiu/liangong2', False),
]
liangong=Room('lingjiu/liangong', u'戏凤阁', None, 0, exits)

exits = [
	Exit('up', 'lingjiu/liangong3', False),
	Exit('down', 'lingjiu/liangong', False),
]
liangong2=Room('lingjiu/liangong2', u'戏凤阁二楼', None, 0, exits)

exits = [
	Exit('down', 'lingjiu/liangong2', False),
]
liangong3=Room('lingjiu/liangong3', u'戏凤阁三楼', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/qiushi', False),
	Exit('east', 'lingjiu/changl11', False),
]
men1=Room('lingjiu/men1', u'囚室大门', 'lingjiu', 0, exits)

exits = [
	Exit('west', 'lingjiu/changl12', False),
	Exit('east', 'lingjiu/shufang', False),
]
men2=Room('lingjiu/men2', u'书房大门', 'lingjiu', 0, exits)

exits = [
	Exit('south', 'lingjiu/xiaodao2', False),
	Exit('north', 'lingjiu/biguan', False),
]
men3=Room('lingjiu/men3', u'闭关室大门', 'lingjiu', 0, exits)

exits = [
	Exit('northdown', 'lingjiu/midao2', False),
	Exit('up', 'lingjiu/huayuan', False),
]
midao1=Room('lingjiu/midao1', u'密道', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/midao14', False),
	Exit('south', 'lingjiu/midao13', False),
	Exit('east', 'lingjiu/midao13', False),
	Exit('north', 'lingjiu/midao11', False),
]
midao10=Room('lingjiu/midao10', u'密道', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/mishi', False),
	Exit('south', 'lingjiu/midao13', False),
	Exit('east', 'lingjiu/midao14', False),
	Exit('north', 'lingjiu/midao12', False),
]
midao11=Room('lingjiu/midao11', u'密道', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/mishi1', False),
	Exit('south', 'lingjiu/midao13', False),
	Exit('east', 'lingjiu/midao14', False),
	Exit('north', 'lingjiu/midao14', False),
]
midao12=Room('lingjiu/midao12', u'密道', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/midao5', False),
	Exit('south', 'lingjiu/midao13', False),
	Exit('east', 'lingjiu/midao13', False),
	Exit('north', 'lingjiu/midao13', False),
]
midao13=Room('lingjiu/midao13', u'密道', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/midao14', False),
	Exit('south', 'lingjiu/midao14', False),
	Exit('east', 'lingjiu/midao5', False),
	Exit('north', 'lingjiu/midao14', False),
]
midao14=Room('lingjiu/midao14', u'密道', None, 0, exits)

exits = [
	Exit('southup', 'lingjiu/midao1', False),
	Exit('northdown', 'lingjiu/midao3', False),
]
midao2=Room('lingjiu/midao2', u'密道', None, 0, exits)

exits = [
	Exit('southup', 'lingjiu/midao2', False),
	Exit('eastdown', 'lingjiu/midao4', False),
]
midao3=Room('lingjiu/midao3', u'密道', None, 0, exits)

exits = [
	Exit('north', 'lingjiu/midao5', False),
	Exit('westup', 'lingjiu/midao3', False),
]
midao4=Room('lingjiu/midao4', u'密道', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/midao14', False),
	Exit('south', 'lingjiu/midao5', False),
	Exit('east', 'lingjiu/midao13', False),
	Exit('north', 'lingjiu/midao6', False),
]
midao5=Room('lingjiu/midao5', u'密道', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/midao14', False),
	Exit('south', 'lingjiu/midao5', False),
	Exit('east', 'lingjiu/midao13', False),
	Exit('north', 'lingjiu/midao7', False),
]
midao6=Room('lingjiu/midao6', u'密道', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/midao14', False),
	Exit('south', 'lingjiu/midao13', False),
	Exit('east', 'lingjiu/midao13', False),
	Exit('north', 'lingjiu/midao8', False),
]
midao7=Room('lingjiu/midao7', u'密道', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/midao14', False),
	Exit('south', 'lingjiu/midao13', False),
	Exit('east', 'lingjiu/midao13', False),
	Exit('north', 'lingjiu/midao9', False),
]
midao8=Room('lingjiu/midao8', u'密道', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/midao14', False),
	Exit('south', 'lingjiu/midao13', False),
	Exit('east', 'lingjiu/midao10', False),
	Exit('north', 'lingjiu/midao14', False),
]
midao9=Room('lingjiu/midao9', u'密道', None, 0, exits)

exits = [
	Exit('up', 'lingjiu/huayuan', False),
]
mishi=Room('lingjiu/mishi', u'密室', None, 0, exits)

exits = [
	Exit('south', 'lingjiu/midao13', False),
	Exit('up', 'lingjiu/huayuan', False),
	Exit('east', 'lingjiu/midao14', False),
	Exit('north', 'lingjiu/midao14', False),
]
mishi1=Room('lingjiu/mishi1', u'密室', None, 0, exits)

exits = [
	Exit('east', 'lingjiu/men1', False),
]
qiushi=Room('lingjiu/qiushi', u'囚室', None, 0, exits)

exits = [
	Exit('west', 'lingjiu/changl3', False),
]
restroom=Room('lingjiu/restroom', u'憩凤阁', None, 0, exits)

exits = [
	Exit('southdown', 'xingxiu/tianroad2', False),
	Exit('westup', 'lingjiu/ya', False),
]
shanjiao=Room('lingjiu/shanjiao', u'缥缈峰山脚', 'lingjiu', 0, exits)

exits = [
	Exit('west', 'lingjiu/men2', False),
]
shufang=Room('lingjiu/shufang', u'沁芳轩', None, 0, exits)

exits = [
	Exit('east', 'lingjiu/changl5', False),
]
wuqiku=Room('lingjiu/wuqiku', u'蓼风轩', None, 0, exits)

exits = [
	Exit('southdown', 'lingjiu/jian', False),
	Exit('eastup', 'lingjiu/dadao1', False),
]
xianchou=Room('lingjiu/xianchou', u'仙愁门', 'lingjiu', 0, exits)

exits = [
	Exit('south', 'lingjiu/huayuan', False),
	Exit('north', 'lingjiu/xiaodao2', False),
]
xiaodao1=Room('lingjiu/xiaodao1', u'小道', 'lingjiu', 0, exits)

exits = [
	Exit('south', 'lingjiu/xiaodao1', False),
	Exit('north', 'lingjiu/men3', False),
]
xiaodao2=Room('lingjiu/xiaodao2', u'小道', 'lingjiu', 0, exits)

exits = [
	Exit('east', 'lingjiu/changl13', False),
]
xuanbing=Room('lingjiu/xuanbing', u'玄冰室', None, 0, exits)

exits = [
	Exit('eastdown', 'lingjiu/shanjiao', False),
	Exit('westup', 'lingjiu/yan', False),
]
ya=Room('lingjiu/ya', u'断魂崖', 'lingjiu', 0, exits)

exits = [
	Exit('eastdown', 'lingjiu/ya', False),
	Exit('northup', 'lingjiu/jian', False),
]
yan=Room('lingjiu/yan', u'失足岩', 'lingjiu', 0, exits)

