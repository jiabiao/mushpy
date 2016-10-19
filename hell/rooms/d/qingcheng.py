# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('northup', 'qingcheng/sanwanjiudao', False),
	Exit('westdown', 'qingcheng/zushidian', False),
]
chaoyangdong=Room('qingcheng/chaoyangdong', u'朝阳洞', 'qingcheng', 0, exits)

exits = [
	Exit('southdown', 'qingcheng/tianshidong', False),
	Exit('northup', 'qingcheng/zushidian', False),
]
gulongqiao=Room('qingcheng/gulongqiao', u'古龙桥', 'qingcheng', 0, exits)

exits = [
	Exit('eastdown', 'qingcheng/shangqing', False),
]
huyingting=Room('qingcheng/huyingting', u'呼应亭', 'qingcheng', 0, exits)

exits = [
	Exit('northwest', 'qingcheng/path1', False),
	Exit('south', 'qingcheng/xiaoqiao', False),
]
jianfugong=Room('qingcheng/jianfugong', u'建福宫', None, 0, exits)

exits = [
	Exit('west', 'qingcheng/shangqing', False),
]
maguchi=Room('qingcheng/maguchi', u'麻姑池', 'qingcheng', 0, exits)

exits = [
	Exit('southeast', 'qingcheng/jianfugong', False),
	Exit('westup', 'qingcheng/tianran', False),
]
path1=Room('qingcheng/path1', u'盘山磴道', 'qingcheng', 0, exits)

exits = [
	Exit('eastdown', 'qingcheng/tianran', False),
	Exit('westup', 'qingcheng/tianshidong', False),
]
path2=Room('qingcheng/path2', u'青城山路', 'qingcheng', 0, exits)

exits = [
	Exit('west', 'qingcheng/qcroad2', False),
	Exit('south', 'city3/fuheqiaon', False),
]
qcroad1=Room('qingcheng/qcroad1', u'青石大道', 'qingcheng', 0, exits)

exits = [
	Exit('east', 'qingcheng/qcroad1', False),
	Exit('north', 'qingcheng/qcroad3', False),
]
qcroad2=Room('qingcheng/qcroad2', u'青泥小道', 'qingcheng', 0, exits)

exits = [
	Exit('south', 'qingcheng/qcroad2', False),
	Exit('north', 'qingcheng/xiaoqiao', False),
]
qcroad3=Room('qingcheng/qcroad3', u'青石大道', 'qingcheng', 0, exits)

exits = [
	Exit('west', 'qingcheng/tianshidong', False),
	Exit('eastdown', 'qingcheng/tingquanting', False),
]
sandaoshi=Room('qingcheng/sandaoshi', u'三岛石', 'qingcheng', 0, exits)

exits = [
	Exit('south', 'qingcheng/tianshidong', False),
]
sanqingdian=Room('qingcheng/sanqingdian', u'三清殿', None, 0, exits)

exits = [
	Exit('southdown', 'qingcheng/chaoyangdong', False),
	Exit('eastup', 'qingcheng/shangqing', False),
]
sanwanjiudao=Room('qingcheng/sanwanjiudao', u'三弯九倒', 'qingcheng', 0, exits)

exits = [
	Exit('west', 'qingcheng/yuanyangjing', False),
	Exit('south', 'qingcheng/songfengguan', False),
	Exit('east', 'qingcheng/maguchi', False),
	Exit('westdown', 'qingcheng/sanwanjiudao', False),
	Exit('westup', 'qingcheng/huyingting', False),
]
shangqing=Room('qingcheng/shangqing', u'上清宫', 'qingcheng', 0, exits)

exits = [
	Exit('north', 'qingcheng/shangqing', False),
]
songfengguan=Room('qingcheng/songfengguan', u'松风观', None, 0, exits)

exits = [
	Exit('eastdown', 'qingcheng/path1', False),
	Exit('north', 'qingcheng/zhuhezhuang', False),
	Exit('westup', 'qingcheng/path2', False),
]
tianran=Room('qingcheng/tianran', u'天然图画', None, 0, exits)

exits = [
	Exit('west', 'qingcheng/yinxing', False),
	Exit('eastdown', 'qingcheng/path2', False),
	Exit('northup', 'qingcheng/gulongqiao', False),
	Exit('east', 'qingcheng/sandaoshi', False),
	Exit('north', 'qingcheng/sanqingdian', False),
]
tianshidong=Room('qingcheng/tianshidong', u'天师洞', None, 0, exits)

exits = [
	Exit('westup', 'qingcheng/sandaoshi', False),
]
tingquanting=Room('qingcheng/tingquanting', u'听泉亭', 'qingcheng', 0, exits)

exits = [
	Exit('south', 'qingcheng/qcroad3', False),
	Exit('north', 'qingcheng/jianfugong', False),
]
xiaoqiao=Room('qingcheng/xiaoqiao', u'小桥', 'qingcheng', 0, exits)

exits = [
	Exit('east', 'qingcheng/tianshidong', False),
]
yinxing=Room('qingcheng/yinxing', u'古银杏树', 'qingcheng', 0, exits)

exits = [
	Exit('east', 'qingcheng/shangqing', False),
]
yuanyangjing=Room('qingcheng/yuanyangjing', u'鸳鸯井', 'qingcheng', 0, exits)

exits = [
	Exit('south', 'qingcheng/tianran', False),
]
zhuhezhuang=Room('qingcheng/zhuhezhuang', u'驻鹤庄', None, 0, exits)

exits = [
	Exit('southdown', 'qingcheng/gulongqiao', False),
	Exit('eastup', 'qingcheng/chaoyangdong', False),
]
zushidian=Room('qingcheng/zushidian', u'祖师殿', None, 0, exits)

