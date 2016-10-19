# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'foshan/street1', False),
]
beidimiao=Room('foshan/beidimiao', u'北帝庙', None, 0, exits)

exits = [
	Exit('north', 'foshan/street5', False),
]
dangpu=Room('foshan/dangpu', u'英雄典当', None, 0, exits)

exits = [
	Exit('west', 'foshan/street5', False),
	Exit('east', 'foshan/road8', False),
]
eastgate=Room('foshan/eastgate', u'东门', 'foshan', 0, exits)

exits = [
	Exit('north', 'foshan/street2', False),
]
huiguan=Room('foshan/huiguan', u'英雄会馆', None, 1, exits)

exits = [
	Exit('north', 'foshan/yingxionglou', False),
]
majiu=Room('foshan/majiu', u'马厩', 'foshan', 0, exits)

exits = [
	Exit('south', 'foshan/northgate', False),
	Exit('northup', 'henshan/hsroad9', False),
]
nanling=Room('foshan/nanling', u'南岭山口', 'foshan', 0, exits)

exits = [
	Exit('south', 'foshan/street3', False),
	Exit('north', 'foshan/nanling', False),
]
northgate=Room('foshan/northgate', u'北门', 'foshan', 0, exits)

exits = [
	Exit('northwest', 'dali/road5', False),
	Exit('east', 'foshan/road2', False),
]
road1=Room('foshan/road1', u'小道', 'foshan', 0, exits)

exits = [
	Exit('west', 'foshan/road9', False),
	Exit('southeast', 'foshan/road12', False),
	Exit('northeast', 'foshan/road11', False),
]
road10=Room('foshan/road10', u'林间道', 'foshan', 0, exits)

exits = [
	Exit('southwest', 'foshan/road10', False),
	Exit('northeast', 'foshan/road13', False),
]
road11=Room('foshan/road11', u'林间道', 'foshan', 0, exits)

exits = [
	Exit('northwest', 'foshan/road10', False),
]
road12=Room('foshan/road12', u'林间道', 'foshan', 0, exits)

exits = [
	Exit('southwest', 'foshan/road11', False),
	Exit('northeast', 'foshan/road14', False),
]
road13=Room('foshan/road13', u'林间道', 'foshan', 0, exits)

exits = [
	Exit('southwest', 'foshan/road13', False),
	Exit('east', 'quanzhou/westbridge', False),
]
road14=Room('foshan/road14', u'林间道', 'foshan', 0, exits)

exits = [
	Exit('west', 'foshan/road1', False),
	Exit('east', 'foshan/road3', False),
]
road2=Room('foshan/road2', u'小道', 'foshan', 0, exits)

exits = [
	Exit('west', 'foshan/road2', False),
	Exit('northeast', 'foshan/road4', False),
]
road3=Room('foshan/road3', u'小道', 'foshan', 0, exits)

exits = [
	Exit('southeast', 'foshan/road5', False),
	Exit('southwest', 'foshan/road3', False),
]
road4=Room('foshan/road4', u'小道', 'foshan', 0, exits)

exits = [
	Exit('northwest', 'foshan/road4', False),
	Exit('east', 'foshan/road6', False),
]
road5=Room('foshan/road5', u'小道', 'foshan', 0, exits)

exits = [
	Exit('west', 'foshan/road5', False),
	Exit('east', 'foshan/road7', False),
]
road6=Room('foshan/road6', u'小道', 'foshan', 0, exits)

exits = [
	Exit('west', 'foshan/road6', False),
	Exit('east', 'foshan/westgate', False),
]
road7=Room('foshan/road7', u'小道', 'foshan', 0, exits)

exits = [
	Exit('west', 'foshan/eastgate', False),
	Exit('east', 'foshan/road9', False),
]
road8=Room('foshan/road8', u'林间道', 'foshan', 0, exits)

exits = [
	Exit('west', 'foshan/road8', False),
	Exit('east', 'foshan/road10', False),
]
road9=Room('foshan/road9', u'林间道', 'foshan', 0, exits)

exits = [
	Exit('south', 'xiakedao/xkroad3', False),
	Exit('north', 'foshan/street3', False),
]
southgate=Room('foshan/southgate', u'南门', 'foshan', 0, exits)

exits = [
	Exit('west', 'foshan/westgate', False),
	Exit('east', 'foshan/street2', False),
	Exit('north', 'foshan/beidimiao', False),
]
street1=Room('foshan/street1', u'西镇街', 'foshan', 0, exits)

exits = [
	Exit('west', 'foshan/street1', False),
	Exit('south', 'foshan/huiguan', False),
	Exit('east', 'foshan/street3', False),
]
street2=Room('foshan/street2', u'西镇街', 'foshan', 0, exits)

exits = [
	Exit('west', 'foshan/street2', False),
	Exit('south', 'foshan/southgate', False),
	Exit('east', 'foshan/street4', False),
	Exit('north', 'foshan/northgate', False),
]
street3=Room('foshan/street3', u'大镇街', 'foshan', 0, exits)

exits = [
	Exit('west', 'foshan/street3', False),
	Exit('south', 'foshan/yingxionglou', False),
	Exit('east', 'foshan/street5', False),
	Exit('north', 'foshan/youtiaopu', False),
]
street4=Room('foshan/street4', u'东镇街', 'foshan', 0, exits)

exits = [
	Exit('west', 'foshan/street4', False),
	Exit('south', 'foshan/dangpu', False),
	Exit('east', 'foshan/eastgate', False),
]
street5=Room('foshan/street5', u'东镇街', 'foshan', 0, exits)

exits = [
	Exit('west', 'foshan/road7', False),
	Exit('east', 'foshan/street1', False),
]
westgate=Room('foshan/westgate', u'西门', 'foshan', 0, exits)

exits = [
	Exit('south', 'foshan/majiu', False),
	Exit('up', 'foshan/yingxionglou2', False),
	Exit('north', 'foshan/street4', False),
]
yingxionglou=Room('foshan/yingxionglou', u'英雄楼', None, 0, exits)

exits = [
	Exit('down', 'foshan/yingxionglou', False),
]
yingxionglou2=Room('foshan/yingxionglou2', u'英雄楼', None, 0, exits)

exits = [
	Exit('south', 'foshan/street4', False),
]
youtiaopu=Room('foshan/youtiaopu', u'油条铺', 'foshan', 0, exits)

