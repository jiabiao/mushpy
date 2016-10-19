# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'hengshan/square', False),
]
baiyunan=Room('hengshan/baiyunan', u'白云庵', None, 0, exits)

exits = [
	Exit('southdown', 'hengshan/beiyuemiao', False),
	Exit('northup', 'hengshan/shandao1', False),
	Exit('eastup', 'hengshan/yuyang', False),
	Exit('westup', 'hengshan/huixiantai', False),
]
beiyuedian=Room('hengshan/beiyuedian', u'北岳殿', None, 0, exits)

exits = [
	Exit('southdown', 'hengshan/guolaoling', False),
	Exit('west', 'hengshan/jijiaoshi', False),
	Exit('northup', 'hengshan/beiyuedian', False),
	Exit('east', 'hengshan/kutianjing', False),
]
beiyuemiao=Room('hengshan/beiyuemiao', u'北岳庙', None, 0, exits)

exits = [
	Exit('down', 'hengshan/cuipinggu2', False),
	Exit('westup', 'hengshan/cuiping2', False),
]
cuiping1=Room('hengshan/cuiping1', u'翠屏山道', 'hengshan', 0, exits)

exits = [
	Exit('eastdown', 'hengshan/cuiping1', False),
	Exit('eastup', 'hengshan/xuankong1', False),
]
cuiping2=Room('hengshan/cuiping2', u'翠屏山道', 'hengshan', 0, exits)

exits = [
	Exit('southeast', 'hengshan/cuipinggu2', False),
	Exit('northwest', 'hengshan/jinlongxia', False),
]
cuipinggu1=Room('hengshan/cuipinggu1', u'翠屏谷', 'hengshan', 0, exits)

exits = [
	Exit('northwest', 'hengshan/cuipinggu1', False),
	Exit('up', 'hengshan/cuiping1', False),
]
cuipinggu2=Room('hengshan/cuipinggu2', u'翠屏谷', 'hengshan', 0, exits)

exits = [
	Exit('west', 'hengshan/yunge', False),
	Exit('northeast', 'hengshan/hufengkou', False),
]
daziling=Room('hengshan/daziling', u'大字岭', 'hengshan', 0, exits)

exits = [
	Exit('northup', 'hengshan/beiyuemiao', False),
	Exit('southwest', 'hengshan/hufengkou', False),
	Exit('westdown', 'hengshan/tongyuangu', False),
]
guolaoling=Room('hengshan/guolaoling', u'果老岭', 'hengshan', 0, exits)

exits = [
	Exit('west', 'hengshan/xuangengsong', False),
	Exit('southwest', 'hengshan/daziling', False),
	Exit('northeast', 'hengshan/guolaoling', False),
]
hufengkou=Room('hengshan/hufengkou', u'虎风口', 'hengshan', 0, exits)

exits = [
	Exit('eastdown', 'hengshan/beiyuedian', False),
]
huixiantai=Room('hengshan/huixiantai', u'会仙台', None, 0, exits)

exits = [
	Exit('east', 'hengshan/beiyuemiao', False),
]
jijiaoshi=Room('hengshan/jijiaoshi', u'鸡叫石', 'hengshan', 0, exits)

exits = [
	Exit('southeast', 'hengshan/cuipinggu1', False),
	Exit('northeast', 'beijing/road6', False),
]
jinlongxia=Room('hengshan/jinlongxia', u'金龙峡', 'hengshan', 0, exits)

exits = [
	Exit('west', 'hengshan/beiyuemiao', False),
]
kutianjing=Room('hengshan/kutianjing', u'苦甜井', 'hengshan', 0, exits)

exits = [
	Exit('down', 'hengshan/xuankong1', False),
]
sanjiaodian=Room('hengshan/sanjiaodian', u'三教殿', None, 0, exits)

exits = [
	Exit('southdown', 'hengshan/beiyuedian', False),
	Exit('northup', 'hengshan/shandao2', False),
]
shandao1=Room('hengshan/shandao1', u'见性峰山道', None, 0, exits)

exits = [
	Exit('southdown', 'hengshan/beiyuedian', False),
	Exit('eastup', 'hengshan/square', False),
]
shandao2=Room('hengshan/shandao2', u'见性峰山道', None, 0, exits)

exits = [
	Exit('north', 'hengshan/baiyunan', False),
	Exit('westdown', 'hengshan/shandao2', False),
]
square=Room('hengshan/square', u'见性峰广场', 'hengshan', 0, exits)

exits = [
	Exit('eastup', 'hengshan/guolaoling', False),
]
tongyuangu=Room('hengshan/tongyuangu', u'通元谷', 'hengshan', 0, exits)

exits = [
	Exit('east', 'hengshan/hufengkou', False),
]
xuangengsong=Room('hengshan/xuangengsong', u'悬根松', 'hengshan', 0, exits)

exits = [
	Exit('south', 'hengshan/zhanqiao', False),
	Exit('westdown', 'hengshan/cuiping2', False),
	Exit('up', 'hengshan/sanjiaodian', False),
]
xuankong1=Room('hengshan/xuankong1', u'悬空寺北楼', None, 0, exits)

exits = [
	Exit('southup', 'hengshan/zhandao', False),
	Exit('north', 'hengshan/zhanqiao', False),
]
xuankong2=Room('hengshan/xuankong2', u'悬空寺南楼', None, 0, exits)

exits = [
	Exit('northdown', 'hengshan/zhandao', False),
	Exit('east', 'hengshan/daziling', False),
]
yunge=Room('hengshan/yunge', u'云阁虹桥', 'hengshan', 0, exits)

exits = [
	Exit('westdown', 'hengshan/beiyuedian', False),
]
yuyang=Room('hengshan/yuyang', u'玉羊游云', 'hengshan', 0, exits)

exits = [
	Exit('southup', 'hengshan/yunge', False),
	Exit('northdown', 'hengshan/xuankong2', False),
]
zhandao=Room('hengshan/zhandao', u'梯式栈道', 'hengshan', 0, exits)

exits = [
	Exit('south', 'hengshan/xuankong2', False),
	Exit('north', 'hengshan/xuankong1', False),
]
zhanqiao=Room('hengshan/zhanqiao', u'悬空栈桥', 'hengshan', 0, exits)

