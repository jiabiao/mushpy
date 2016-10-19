# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('southeast', 'city3/northroad1', False),
]
bingqidian=Room('city3/bingqidian', u'兵器铺', None, 0, exits)

exits = [
	Exit('south', 'city3/path2', False),
]
caotang=Room('city3/caotang', u'杜甫草堂', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/jiudian', False),
]
chufang=Room('city3/chufang', u'酒楼厨房', None, 0, exits)

exits = [
	Exit('west', 'city3/eastroad2', False),
	Exit('east', 'city3/fuheqiaoe', False),
]
eastgate=Room('city3/eastgate', u'东门', 'chengdu', 0, exits)

exits = [
	Exit('northwest', 'city3/northroad3', False),
	Exit('south', 'city3/eastroad2', False),
	Exit('northeast', 'city3/jiudian', False),
]
eastroad1=Room('city3/eastroad1', u'东大街', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/shuduroad1', False),
	Exit('south', 'city3/eastroad3', False),
	Exit('north', 'city3/eastroad1', False),
	Exit('east', 'city3/eastgate', False),
]
eastroad2=Room('city3/eastroad2', u'东大街', 'chengdu', 0, exits)

exits = [
	Exit('southeast', 'city3/wangjianglou', False),
	Exit('southwest', 'city3/southroad1', False),
	Exit('north', 'city3/eastroad2', False),
]
eastroad3=Room('city3/eastroad3', u'东大街', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/eastgate', False),
	Exit('east', 'city3/road2', False),
]
fuheqiaoe=Room('city3/fuheqiaoe', u'府河桥', 'chengdu', 0, exits)

exits = [
	Exit('south', 'city3/northgate', False),
	Exit('north', 'qingcheng/qcroad1', False),
]
fuheqiaon=Room('city3/fuheqiaon', u'府河桥', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/shuduroad2', False),
	Exit('south', 'city3/tiduroad', False),
	Exit('north', 'city3/tidugate', False),
	Exit('east', 'city3/shuduroad1', False),
]
guangchang=Room('city3/guangchang', u'广场', 'chengdu', 0, exits)

exits = [
	Exit('southwest', 'city3/eastroad1', False),
	Exit('east', 'city3/chufang', False),
]
jiudian=Room('city3/jiudian', u'蓉城酒楼', None, 0, exits)

exits = [
	Exit('northwest', 'city3/southroad1', False),
	Exit('east', 'city3/majiu', False),
	Exit('up', 'city3/kedian2', False),
]
kedian=Room('city3/kedian', u'锦城驿', None, 0, exits)

exits = [
	Exit('down', 'city3/kedian', False),
]
kedian2=Room('city3/kedian2', u'客店二楼', None, 0, exits)

exits = [
	Exit('northup', 'city3/wuhouci', False),
	Exit('south', 'city3/wuhoucigate', False),
]
liubeidian=Room('city3/liubeidian', u'刘备殿', None, 0, exits)

exits = [
	Exit('west', 'city3/kedian', False),
]
majiu=Room('city3/majiu', u'马厩', 'city3', 0, exits)

exits = [
	Exit('south', 'xuedao/sroad1', False),
	Exit('north', 'city3/southgate', False),
]
nanheqiaos=Room('city3/nanheqiaos', u'南河桥', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/path1', False),
	Exit('east', 'city3/westgate', False),
]
nanheqiaow=Room('city3/nanheqiaow', u'南河桥', 'chengdu', 0, exits)

exits = [
	Exit('south', 'city3/northroad2', False),
	Exit('north', 'city3/fuheqiaon', False),
]
northgate=Room('city3/northgate', u'北城门', 'chengdu', 0, exits)

exits = [
	Exit('northwest', 'city3/bingqidian', False),
	Exit('southwest', 'city3/westroad3', False),
	Exit('east', 'city3/northroad2', False),
]
northroad1=Room('city3/northroad1', u'北大街', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/northroad1', False),
	Exit('south', 'city3/tanggate', False),
	Exit('north', 'city3/northgate', False),
	Exit('east', 'city3/northroad3', False),
]
northroad2=Room('city3/northroad2', u'北大街', 'chengdu', 0, exits)

exits = [
	Exit('southeast', 'city3/eastroad1', False),
	Exit('west', 'city3/northroad2', False),
	Exit('northeast', 'city3/wuguan', False),
]
northroad3=Room('city3/northroad3', u'北大街', 'chengdu', 0, exits)

exits = [
	Exit('east', 'city3/nanheqiaow', False),
	Exit('north', 'city3/path2', False),
]
path1=Room('city3/path1', u'浣花溪', 'chengdu', 0, exits)

exits = [
	Exit('south', 'city3/path1', False),
	Exit('north', 'city3/caotang', False),
]
path2=Room('city3/path2', u'浣花溪', 'chengdu', 0, exits)

exits = [
	Exit('down', 'city3/wuguan', False),
]
practice=Room('city3/practice', u'武馆操练房', None, 0, exits)

exits = [
	Exit('northeast', 'city3/westroad1', False),
]
qingyanggong=Room('city3/qingyanggong', u'青羊宫', None, 0, exits)

exits = [
	Exit('northwest', 'city3/road2', False),
	Exit('east', 'emei/qsjie1', False),
]
road1=Room('city3/road1', u'青石大道', 'emei', 0, exits)

exits = [
	Exit('west', 'city3/fuheqiaoe', False),
	Exit('southeast', 'city3/road1', False),
]
road2=Room('city3/road2', u'青石大道', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/guangchang', False),
	Exit('east', 'city3/eastroad2', False),
]
shuduroad1=Room('city3/shuduroad1', u'蜀都道', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/westroad2', False),
	Exit('east', 'city3/guangchang', False),
]
shuduroad2=Room('city3/shuduroad2', u'蜀都道', 'chengdu', 0, exits)

exits = [
	Exit('south', 'city3/nanheqiaos', False),
	Exit('north', 'city3/southroad2', False),
]
southgate=Room('city3/southgate', u'南城门', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/southroad2', False),
	Exit('southeast', 'city3/kedian', False),
	Exit('northeast', 'city3/eastroad3', False),
]
southroad1=Room('city3/southroad1', u'南大街', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/southroad3', False),
	Exit('south', 'city3/southgate', False),
	Exit('east', 'city3/southroad1', False),
	Exit('north', 'city3/tiduroad', False),
]
southroad2=Room('city3/southroad2', u'南大街', 'chengdu', 0, exits)

exits = [
	Exit('northwest', 'city3/westroad1', False),
	Exit('southwest', 'city3/wuhoucigate', False),
	Exit('east', 'city3/southroad2', False),
]
southroad3=Room('city3/southroad3', u'南大街', 'chengdu', 0, exits)

exits = [
	Exit('north', 'city3/northroad2', False),
]
tanggate=Room('city3/tanggate', u'唐门大门', 'chengdu', 0, exits)

exits = [
	Exit('south', 'city3/tidugate', False),
]
tidufu=Room('city3/tidufu', u'提督府', None, 0, exits)

exits = [
	Exit('south', 'city3/guangchang', False),
	Exit('north', 'city3/tidufu', False),
]
tidugate=Room('city3/tidugate', u'提督府门', 'chengdu', 0, exits)

exits = [
	Exit('south', 'city3/southroad2', False),
	Exit('north', 'city3/guangchang', False),
]
tiduroad=Room('city3/tiduroad', u'提督街', 'chengdu', 0, exits)

exits = [
	Exit('northwest', 'city3/eastroad3', False),
]
wangjianglou=Room('city3/wangjianglou', u'望江楼', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/nanheqiaow', False),
	Exit('east', 'city3/westroad2', False),
]
westgate=Room('city3/westgate', u'西门', 'chengdu', 0, exits)

exits = [
	Exit('southeast', 'city3/southroad3', False),
	Exit('southwest', 'city3/qingyanggong', False),
	Exit('north', 'city3/westroad2', False),
]
westroad1=Room('city3/westroad1', u'西大街', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/westgate', False),
	Exit('south', 'city3/westroad1', False),
	Exit('north', 'city3/westroad3', False),
	Exit('east', 'city3/shuduroad2', False),
]
westroad2=Room('city3/westroad2', u'西大街', 'chengdu', 0, exits)

exits = [
	Exit('northwest', 'city3/yaodian', False),
	Exit('south', 'city3/westroad2', False),
	Exit('northeast', 'city3/northroad1', False),
]
westroad3=Room('city3/westroad3', u'西大街', 'chengdu', 0, exits)

exits = [
	Exit('west', 'city3/wuguanxiao', False),
	Exit('south', 'city3/wuguanlong', False),
	Exit('southwest', 'city3/northroad3', False),
	Exit('up', 'city3/practice', False),
	Exit('north', 'city3/wuguanliu', False),
	Exit('east', 'city3/wuguanchen', False),
	Exit('down', 'city3/wuxiuxi', False),
]
wuguan=Room('city3/wuguan', u'金牛武馆', None, 0, exits)

exits = [
	Exit('west', 'city3/wuguan', False),
]
wuguanchen=Room('city3/wuguanchen', u'金牛武馆一部', None, 0, exits)

exits = [
	Exit('south', 'city3/wuguan', False),
]
wuguanliu=Room('city3/wuguanliu', u'金牛武馆四部', None, 0, exits)

exits = [
	Exit('north', 'city3/wuguan', False),
]
wuguanlong=Room('city3/wuguanlong', u'金牛武馆二部', None, 0, exits)

exits = [
	Exit('east', 'city3/wuguan', False),
]
wuguanxiao=Room('city3/wuguanxiao', u'金牛武馆三部', None, 0, exits)

exits = [
	Exit('southdown', 'city3/liubeidian', False),
]
wuhouci=Room('city3/wuhouci', u'诸葛亮殿', None, 0, exits)

exits = [
	Exit('north', 'city3/liubeidian', False),
	Exit('northeast', 'city3/southroad3', False),
]
wuhoucigate=Room('city3/wuhoucigate', u'武侯祠大门', 'chengdu', 0, exits)

exits = [
	Exit('up', 'city3/wuguan', False),
]
wuxiuxi=Room('city3/wuxiuxi', u'金牛武馆地下室', None, 0, exits)

exits = [
	Exit('southeast', 'city3/westroad3', False),
]
yaodian=Room('city3/yaodian', u'济世堂药店', None, 0, exits)

