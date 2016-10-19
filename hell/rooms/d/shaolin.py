# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'shaolin/rukou', False),
	Exit('north', 'shaolin/jianyu1', True),
]
andao1=Room('shaolin/andao1', u'暗道', None, 0, exits)

exits = [
	Exit('up', 'shaolin/gulou1', False),
]
andao2=Room('shaolin/andao2', u'暗道', None, 0, exits)

exits = [
	Exit('up', 'shaolin/zhonglou1', False),
	Exit('enter', 'shaolin/bagua0', False),
]
andao3=Room('shaolin/andao3', u'暗道', None, 0, exits)

exits = [
	Exit('up', 'shaolin/andao3', False),
]
bagua=Room('shaolin/bagua', u'八卦阵阵心', None, 0, exits)

exits = [
	Exit('离', 'shaolin/bagua5', False),
	Exit('巽', 'shaolin/bagua6', False),
	Exit('兑', 'shaolin/bagua3', False),
	Exit('乾', 'shaolin/bagua7', False),
	Exit('坎', 'shaolin/bagua2', False),
	Exit('艮', 'shaolin/bagua4', False),
	Exit('坤', 'shaolin/bagua0', False),
	Exit('震', 'shaolin/bagua1', False),
]
bagua0=Room('shaolin/bagua0', u'八卦阵', None, 0, exits)

exits = [
	Exit('离', 'shaolin/bagua5', False),
	Exit('巽', 'shaolin/bagua6', False),
	Exit('兑', 'shaolin/bagua3', False),
	Exit('乾', 'shaolin/bagua7', False),
	Exit('坎', 'shaolin/bagua2', False),
	Exit('艮', 'shaolin/bagua4', False),
	Exit('坤', 'shaolin/bagua0', False),
	Exit('震', 'shaolin/bagua1', False),
]
bagua1=Room('shaolin/bagua1', u'八卦阵', None, 0, exits)

exits = [
	Exit('离', 'shaolin/bagua5', False),
	Exit('巽', 'shaolin/bagua6', False),
	Exit('兑', 'shaolin/bagua3', False),
	Exit('乾', 'shaolin/bagua7', False),
	Exit('坎', 'shaolin/bagua2', False),
	Exit('艮', 'shaolin/bagua4', False),
	Exit('坤', 'shaolin/bagua0', False),
	Exit('震', 'shaolin/bagua1', False),
]
bagua2=Room('shaolin/bagua2', u'八卦阵', None, 0, exits)

exits = [
	Exit('离', 'shaolin/bagua5', False),
	Exit('巽', 'shaolin/bagua6', False),
	Exit('兑', 'shaolin/bagua3', False),
	Exit('乾', 'shaolin/bagua7', False),
	Exit('坎', 'shaolin/bagua2', False),
	Exit('艮', 'shaolin/bagua4', False),
	Exit('坤', 'shaolin/bagua0', False),
	Exit('震', 'shaolin/bagua1', False),
]
bagua3=Room('shaolin/bagua3', u'八卦阵', None, 0, exits)

exits = [
	Exit('离', 'shaolin/bagua5', False),
	Exit('巽', 'shaolin/bagua6', False),
	Exit('兑', 'shaolin/bagua3', False),
	Exit('乾', 'shaolin/bagua7', False),
	Exit('坎', 'shaolin/bagua2', False),
	Exit('艮', 'shaolin/bagua4', False),
	Exit('坤', 'shaolin/bagua0', False),
	Exit('震', 'shaolin/bagua1', False),
]
bagua4=Room('shaolin/bagua4', u'八卦阵', None, 0, exits)

exits = [
	Exit('离', 'shaolin/bagua5', False),
	Exit('巽', 'shaolin/bagua6', False),
	Exit('兑', 'shaolin/bagua3', False),
	Exit('乾', 'shaolin/bagua7', False),
	Exit('坎', 'shaolin/bagua2', False),
	Exit('艮', 'shaolin/bagua4', False),
	Exit('坤', 'shaolin/bagua0', False),
	Exit('震', 'shaolin/bagua1', False),
]
bagua5=Room('shaolin/bagua5', u'八卦阵', None, 0, exits)

exits = [
	Exit('离', 'shaolin/bagua5', False),
	Exit('巽', 'shaolin/bagua6', False),
	Exit('兑', 'shaolin/bagua3', False),
	Exit('乾', 'shaolin/bagua7', False),
	Exit('坎', 'shaolin/bagua2', False),
	Exit('艮', 'shaolin/bagua4', False),
	Exit('坤', 'shaolin/bagua0', False),
	Exit('震', 'shaolin/bagua1', False),
]
bagua6=Room('shaolin/bagua6', u'八卦阵', None, 0, exits)

exits = [
	Exit('离', 'shaolin/bagua5', False),
	Exit('巽', 'shaolin/bagua6', False),
	Exit('兑', 'shaolin/bagua3', False),
	Exit('乾', 'shaolin/bagua7', False),
	Exit('坎', 'shaolin/bagua2', False),
	Exit('艮', 'shaolin/bagua4', False),
	Exit('坤', 'shaolin/bagua0', False),
	Exit('震', 'shaolin/bagua1', False),
]
bagua7=Room('shaolin/bagua7', u'八卦阵', None, 0, exits)

exits = [
	Exit('south', 'shaolin/qfdian', True),
	Exit('southwest', 'shaolin/bamboo2', False)
]
bamboo1=Room('shaolin/bamboo1', u'竹林', 'shaolin', 0, exits)

exits = [
	Exit('south', 'shaolin/bamboo11', False)
]
bamboo10=Room('shaolin/bamboo10', u'竹林', 'shaolin', 0, exits)

exits = [
	Exit('west', 'shaolin/bamboo12', False)
]
bamboo11=Room('shaolin/bamboo11', u'竹林', 'shaolin', 0, exits)

exits = [
	Exit('north', 'shaolin/bamboo13', False),
]
bamboo12=Room('shaolin/bamboo12', u'竹林', 'shaolin', 0, exits)

exits = [
	Exit('northwest', 'shaolin/bamboo14', False),
]
bamboo13=Room('shaolin/bamboo13', u'竹林', 'shaolin', 0, exits)

exits = [
	Exit('north', 'shaolin/damodong', False),
]
bamboo14=Room('shaolin/bamboo14', u'竹林', 'shaolin', 0, exits)

exits = [
	Exit('southwest', 'shaolin/bamboo3', False),
]
bamboo2=Room('shaolin/bamboo2', u'竹林', 'shaolin', 0, exits)

exits = [
	Exit('north', 'shaolin/bamboo4', False),
]
bamboo3=Room('shaolin/bamboo3', u'竹林', 'shaolin', 0, exits)

exits = [
	Exit('north', 'shaolin/bamboo5', False),
]
bamboo4=Room('shaolin/bamboo4', u'竹林', 'shaolin', 0, exits)

exits = [
	Exit('north', 'shaolin/bamboo6', False),
]
bamboo5=Room('shaolin/bamboo5', u'竹林', 'shaolin', 0, exits)

exits = [
	Exit('north', 'shaolin/bamboo7', False),
]
bamboo6=Room('shaolin/bamboo6', u'竹林', 'shaolin', 0, exits)

exits = [
	Exit('south', 'shaolin/bamboo8', False)
]
bamboo7=Room('shaolin/bamboo7', u'竹林', 'shaolin', 0, exits)

exits = [
	Exit('east', 'shaolin/bamboo9', False),
]
bamboo8=Room('shaolin/bamboo8', u'竹林', 'shaolin', 0, exits)

exits = [
	Exit('east', 'shaolin/bamboo10', False),
]
bamboo9=Room('shaolin/bamboo9', u'竹林', 'shaolin', 0, exits)

exits = [
	Exit('south', 'shaolin/zoulang1', False),
	Exit('north', 'shaolin/banruo2', False),
]
banruo1=Room('shaolin/banruo1', u'般若堂一部', None, 0, exits)

exits = [
	Exit('south', 'shaolin/banruo1', False),
	Exit('north', 'shaolin/banruo3', False),
]
banruo2=Room('shaolin/banruo2', u'般若堂二部', None, 0, exits)

exits = [
	Exit('south', 'shaolin/banruo2', False),
	Exit('north', 'shaolin/banruo4', False),
]
banruo3=Room('shaolin/banruo3', u'般若堂三部', None, 0, exits)

exits = [
	Exit('south', 'shaolin/banruo3', False),
	Exit('north', 'shaolin/banruo5', False),
]
banruo4=Room('shaolin/banruo4', u'般若堂四部', None, 0, exits)

exits = [
	Exit('south', 'shaolin/banruo4', False),
	Exit('north', 'shaolin/banruo6', False),
	Exit('east', 'shaolin/wuchang1', False),
]
banruo5=Room('shaolin/banruo5', u'般若堂五部', None, 0, exits)

exits = [
	Exit('south', 'shaolin/banruo5', False),
	Exit('north', 'shaolin/banruo7', False),
]
banruo6=Room('shaolin/banruo6', u'般若堂六部', None, 0, exits)

exits = [
	Exit('south', 'shaolin/banruo6', False),
	Exit('north', 'shaolin/banruo8', False),
]
banruo7=Room('shaolin/banruo7', u'般若堂七部', None, 0, exits)

exits = [
	Exit('south', 'shaolin/banruo7', False),
	Exit('north', 'shaolin/banruo9', False),
]
banruo8=Room('shaolin/banruo8', u'般若堂八部', None, 0, exits)

exits = [
	Exit('northup', 'shaolin/zoulang5', False),
	Exit('south', 'shaolin/banruo8', False),
]
banruo9=Room('shaolin/banruo9', u'般若堂九部', None, 0, exits)

exits = [
	Exit('west', 'shaolin/taijie', False),
]
beilin1=Room('shaolin/beilin1', u'东碑林', 'shaolin', 0, exits)

exits = [
	Exit('east', 'shaolin/taijie', False),
]
beilin2=Room('shaolin/beilin2', u'西碑林', 'shaolin', 0, exits)

exits = [
]
beilin3=Room('shaolin/beilin3', u'地下室', None, 0, exits)

exits = [
	Exit('west', 'shaolin/guangchang5', False),
]
bydian=Room('shaolin/bydian', u'白衣殿', None, 0, exits)

exits = [
	Exit('south', 'shaolin/fanting1', False),
]
chufang=Room('shaolin/chufang', u'厨房', None, 0, exits)

exits = [
	Exit('southwest', 'shaolin/houshan', False),
]
chufang2=Room('shaolin/chufang2', u'厨房', None, 0, exits)

exits = [
	Exit('up', 'shaolin/cjlou1', False),
	Exit('east', 'shaolin/zhulin5', False),
]
cjlou=Room('shaolin/cjlou', u'藏经阁一楼', None, 0, exits)

exits = [
	Exit('down', 'shaolin/cjlou', False),
]
cjlou1=Room('shaolin/cjlou1', u'藏经阁二楼', None, 0, exits)

exits = [
	Exit('out', 'shaolin/bamboo1', False),
]
damodong=Room('shaolin/damodong', u'达摩洞', None, 0, exits)

exits = [
	Exit('southdown', 'shaolin/wuchang3', False),
	Exit('up', 'shaolin/dmyuan2', False),
	Exit('northdown', 'shaolin/guangchang5', False),
]
dmyuan=Room('shaolin/dmyuan', u'达摩院', None, 0, exits)

exits = [
	Exit('down', 'shaolin/dmyuan', False),
]
dmyuan2=Room('shaolin/dmyuan2', u'达摩院二楼', None, 0, exits)

exits = [
]
duchuan=Room('shaolin/duchuan', u'渡船', 'shaolin', 0, exits)

exits = [
	Exit('southdown', 'shaolin/guangchang2', False),
]
dxbdian=Room('shaolin/dxbdian', u'大雄宝殿', None, 0, exits)

exits = [
	Exit('east', 'shaolin/guangchang5', False),
]
dzdian=Room('shaolin/dzdian', u'地藏殿', None, 0, exits)

exits = [
	Exit('south', 'shaolin/wuqiku', False),
	Exit('north', 'shaolin/yaopinku', False),
]
fangjuku=Room('shaolin/fangjuku', u'防具库', None, 0, exits)

exits = [
	Exit('north', 'shaolin/fanting1', False),
	Exit('east', 'shaolin/guangchang3', False),
]
fanting=Room('shaolin/fanting', u'斋厅', None, 0, exits)

exits = [
	Exit('south', 'shaolin/fanting', False),
	Exit('north', 'shaolin/chufang', False),
]
fanting1=Room('shaolin/fanting1', u'斋厅', None, 0, exits)

exits = [
	Exit('out', 'shaolin/qyping', False),
]
fumoquan=Room('shaolin/fumoquan', u'金刚伏魔圈', None, 0, exits)

exits = [
	Exit('west', 'shaolin/zoulang6', False),
	Exit('south', 'shaolin/wuchang', False),
	Exit('east', 'shaolin/zoulang7', False),
	Exit('north', 'shaolin/wuchang3', False),
	Exit('up', 'shaolin/fzlou1', False),
]
fzlou=Room('shaolin/fzlou', u'方丈楼', None, 0, exits)

exits = [
	Exit('north', 'shaolin/fzlou2', False),
	Exit('down', 'shaolin/fzlou', False),
]
fzlou1=Room('shaolin/fzlou1', u'茶室', None, 0, exits)

exits = [
	Exit('south', 'shaolin/fzlou1', False),
]
fzlou2=Room('shaolin/fzlou2', u'方丈室', None, 0, exits)

exits = [
	Exit('west', 'shaolin/guangchang1w', False),
	Exit('south', 'shaolin/shijie11', False),
	Exit('east', 'shaolin/guangchang1e', False),
]
guangchang1=Room('shaolin/guangchang1', u'广场', 'shaolin', 0, exits)

exits = [
	Exit('southdown', 'shaolin/shijie11', False),
	Exit('west', 'shaolin/guangchang1', False),
	Exit('east', 'shaolin/shulin1', False),
]
guangchang1e=Room('shaolin/guangchang1e', u'广场', 'shaolin', 0, exits)

exits = [
	Exit('southdown', 'shaolin/shijie11', False),
	Exit('west', 'shaolin/shulin1', False),
	Exit('east', 'shaolin/guangchang1', False),
]
guangchang1w=Room('shaolin/guangchang1w', u'广场', 'shaolin', 0, exits)

exits = [
	Exit('west', 'shaolin/gulou', False),
	Exit('south', 'shaolin/twdian', False),
	Exit('east', 'shaolin/zhonglou', False),
	Exit('up', 'shaolin/dxbdian', False),
	Exit('north', 'shaolin/guangchang3', False),
]
guangchang2=Room('shaolin/guangchang2', u'广场', 'shaolin', 0, exits)

exits = [
	Exit('west', 'shaolin/fanting', False),
	Exit('south', 'shaolin/guangchang2', False),
	Exit('up', 'shaolin/jlyuan', False),
	Exit('north', 'shaolin/guangchang4', False),
]
guangchang3=Room('shaolin/guangchang3', u'勤修场', 'shaolin', 0, exits)

exits = [
	Exit('south', 'shaolin/guangchang3', False),
	Exit('up', 'shaolin/putiyuan', False),
	Exit('north', 'shaolin/houdian', False),
]
guangchang4=Room('shaolin/guangchang4', u'精进场', 'shaolin', 0, exits)

exits = [
	Exit('west', 'shaolin/dzdian', False),
	Exit('southup', 'shaolin/dmyuan', False),
	Exit('northup', 'shaolin/qfdian', False),
	Exit('southwest', 'shaolin/wuchang3', False),
	Exit('east', 'shaolin/bydian', False),
]
guangchang5=Room('shaolin/guangchang5', u'广场', 'shaolin', 0, exits)

exits = [
	Exit('east', 'shaolin/guangchang2', False),
	Exit('enter', 'shaolin/gulou1', False),
]
gulou=Room('shaolin/gulou', u'鼓楼小院', 'shaolin', 0, exits)

exits = [
	Exit('out', 'shaolin/gulou', False),
	Exit('up', 'shaolin/gulou2', False),
]
gulou1=Room('shaolin/gulou1', u'鼓楼一层', None, 0, exits)

exits = [
	Exit('up', 'shaolin/gulou3', False),
	Exit('down', 'shaolin/gulou1', False),
]
gulou2=Room('shaolin/gulou2', u'鼓楼二层', None, 0, exits)

exits = [
	Exit('up', 'shaolin/gulou4', False),
	Exit('down', 'shaolin/gulou2', False),
]
gulou3=Room('shaolin/gulou3', u'鼓楼三层', None, 0, exits)

exits = [
	Exit('up', 'shaolin/gulou5', False),
	Exit('down', 'shaolin/gulou3', False),
]
gulou4=Room('shaolin/gulou4', u'鼓楼四层', None, 0, exits)

exits = [
	Exit('up', 'shaolin/gulou6', False),
	Exit('down', 'shaolin/gulou4', False),
]
gulou5=Room('shaolin/gulou5', u'鼓楼五层', None, 0, exits)

exits = [
	Exit('up', 'shaolin/gulou7', False),
	Exit('down', 'shaolin/gulou5', False),
]
gulou6=Room('shaolin/gulou6', u'鼓楼六层', None, 0, exits)

exits = [
	Exit('down', 'shaolin/gulou6', False),
]
gulou7=Room('shaolin/gulou7', u'鼓楼七层', None, 0, exits)

exits = [
	Exit('south', 'shaolin/yidao2', False),
]
hanshui1=Room('shaolin/hanshui1', u'汉水南岸', 'nanyang', 0, exits)

exits = [
	Exit('north', 'shaolin/nanyang', False),
]
hanshui2=Room('shaolin/hanshui2', u'汉水北岸', 'nanyang', 0, exits)

exits = [
]
hanshuim=Room('shaolin/hanshuim', u'汉水', 'nanyang', 0, exits)

exits = [
]
hantan1=Room('shaolin/hantan1', u'万古寒潭', None, 0, exits)

exits = [
]
hantan2=Room('shaolin/hantan2', u'万古寒潭', None, 0, exits)

exits = [
]
hantan3=Room('shaolin/hantan3', u'万古寒潭', None, 0, exits)

exits = [
	Exit('west', 'shaolin/zoulang2', False),
	Exit('south', 'shaolin/guangchang4', False),
	Exit('north', 'shaolin/wuchang', False),
	Exit('east', 'shaolin/zoulang3', False),
]
houdian=Room('shaolin/houdian', u'后殿', None, 0, exits)

exits = [
	Exit('northwest', 'shaolin/zhushe', False),
	Exit('northeast', 'shaolin/chufang2', False),
	Exit('north', 'shaolin/xiaowu', False),
	Exit('east', 'shaolin/xiaojing2', False),
]
houshan=Room('shaolin/houshan', u'小院', 'shaolin', 0, exits)

exits = [
	Exit('west', 'shaolin/wuchang3', False),
	Exit('south', 'shaolin/zoulang7', False),
	Exit('north', 'shaolin/hsyuan2', False),
	Exit('east', 'shaolin/zhulin1', False),
]
hsyuan1=Room('shaolin/hsyuan1', u'和尚院一部', None, 0, exits)

exits = [
	Exit('south', 'shaolin/hsyuan1', False),
	Exit('north', 'shaolin/hsyuan3', False),
	Exit('east', 'shaolin/zhulin2', False),
]
hsyuan2=Room('shaolin/hsyuan2', u'和尚院二部', None, 0, exits)

exits = [
	Exit('south', 'shaolin/hsyuan2', False),
	Exit('east', 'shaolin/zhulin3', False),
]
hsyuan3=Room('shaolin/hsyuan3', u'和尚院三部', None, 0, exits)

exits = [
	Exit('west', 'shaolin/zhulin4', False),
	Exit('south', 'shaolin/zoulang6', False),
	Exit('north', 'shaolin/hsyuan5', False),
	Exit('east', 'shaolin/wuchang3', False),
]
hsyuan4=Room('shaolin/hsyuan4', u'和尚院四部', None, 0, exits)

exits = [
	Exit('west', 'shaolin/zhulin5', False),
	Exit('south', 'shaolin/hsyuan4', False),
	Exit('north', 'shaolin/hsyuan6', False),
]
hsyuan5=Room('shaolin/hsyuan5', u'和尚院五部', None, 0, exits)

exits = [
	Exit('west', 'shaolin/zhulin6', False),
	Exit('south', 'shaolin/hsyuan5', False),
]
hsyuan6=Room('shaolin/hsyuan6', u'和尚院六部', None, 0, exits)

exits = [
	Exit('south', 'shaolin/jianyu1', False),
]
jianyu=Room('shaolin/jianyu', u'监狱', None, 0, exits)

exits = [
	Exit('north', 'shaolin/jianyu', False),
]
jianyu1=Room('shaolin/jianyu1', u'监狱', None, 0, exits)

exits = [
	Exit('northup', 'shaolin/qyping', False),
	Exit('southdown', 'shaolin/shulin14', False),
]
jiebei=Room('shaolin/jiebei', u'界碑', 'shaolin', 0, exits)

exits = [
	Exit('up', 'shaolin/jiulou2', False),
	Exit('east', 'shaolin/nanyang', False),
]
jiulou1=Room('shaolin/jiulou1', u'迎宾楼', None, 1, exits)

exits = [
	Exit('down', 'shaolin/jiulou1', False),
]
jiulou2=Room('shaolin/jiulou2', u'迎宾楼二楼', None, 0, exits)

exits = [
	Exit('southdown', 'shaolin/guangchang3', False),
]
jlyuan=Room('shaolin/jlyuan', u'戒律院', None, 1, exits)

exits = [
	Exit('west', 'shaolin/nanyang', False),
	Exit('up', 'shaolin/kedian2', False),
	Exit('east', 'shaolin/majiu1', False),
]
kedian1=Room('shaolin/kedian1', u'悦来客栈', None, 0, exits)

exits = [
	Exit('down', 'shaolin/kedian1', False),
]
kedian2=Room('shaolin/kedian2', u'客店二楼', None, 0, exits)

exits = [
	Exit('south', 'shaolin/zoulang4', False),
	Exit('north', 'shaolin/luohan2', False),
]
luohan1=Room('shaolin/luohan1', u'罗汉堂一部', None, 0, exits)

exits = [
	Exit('south', 'shaolin/luohan1', False),
	Exit('north', 'shaolin/luohan3', False),
]
luohan2=Room('shaolin/luohan2', u'罗汉堂二部', None, 0, exits)

exits = [
	Exit('south', 'shaolin/luohan2', False),
	Exit('north', 'shaolin/luohan4', False),
]
luohan3=Room('shaolin/luohan3', u'罗汉堂三部', None, 0, exits)

exits = [
	Exit('south', 'shaolin/luohan3', False),
	Exit('north', 'shaolin/luohan5', False),
]
luohan4=Room('shaolin/luohan4', u'罗汉堂四部', None, 0, exits)

exits = [
	Exit('west', 'shaolin/wuchang2', False),
	Exit('south', 'shaolin/luohan4', False),
	Exit('north', 'shaolin/luohan6', False),
]
luohan5=Room('shaolin/luohan5', u'罗汉堂五部', None, 0, exits)

exits = [
	Exit('south', 'shaolin/luohan5', False),
	Exit('north', 'shaolin/luohan7', False),
]
luohan6=Room('shaolin/luohan6', u'罗汉堂六部', None, 0, exits)

exits = [
	Exit('south', 'shaolin/luohan6', False),
	Exit('north', 'shaolin/luohan8', False),
]
luohan7=Room('shaolin/luohan7', u'罗汉堂七部', None, 0, exits)

exits = [
	Exit('south', 'shaolin/luohan7', False),
	Exit('north', 'shaolin/luohan9', False),
]
luohan8=Room('shaolin/luohan8', u'罗汉堂八部', None, 0, exits)

exits = [
	Exit('northup', 'shaolin/zoulang8', False),
	Exit('south', 'shaolin/luohan8', False),
]
luohan9=Room('shaolin/luohan9', u'罗汉堂九部', None, 0, exits)

exits = [
	Exit('west', 'shaolin/kedian1', False),
]
majiu1=Room('shaolin/majiu1', u'马厩', 'nanyang', 0, exits)

exits = [
	Exit('north', 'songshan/taishique', False),
]
maowu=Room('shaolin/maowu', u'茅屋', None, 0, exits)

exits = [
	Exit('west', 'shaolin/jiulou1', False),
	Exit('south', 'shaolin/hanshui2', False),
	Exit('east', 'shaolin/kedian1', False),
	Exit('north', 'shaolin/yidao3', False),
]
nanyang=Room('shaolin/nanyang', u'南阳城', 'nanyang', 0, exits)

exits = [
	Exit('southdown', 'shaolin/guangchang4', False),
]
putiyuan=Room('shaolin/putiyuan', u'菩提院', None, 0, exits)

exits = [
	Exit('southdown', 'shaolin/guangchang5', False),
	Exit('north', 'shaolin/bamboo1', True),
]
qfdian=Room('shaolin/qfdian', u'千佛殿', None, 0, exits)

exits = [
	Exit('southdown', 'shaolin/shulin14', False),
	Exit('enter', 'shaolin/fumoquan', False),
]
qyping=Room('shaolin/qyping', u'青云坪', 'shaolin', 0, exits)

exits = [
	Exit('south', 'shaolin/wuxing0', False),
	Exit('north', 'shaolin/andao1', False),
]
rukou=Room('shaolin/rukou', u'五行洞入口', None, 0, exits)

exits = [
	Exit('west', 'songshan/taishique', False),
	Exit('south', 'shaolin/yidao3', False),
	Exit('north', 'beijing/road10', False),
]
ruzhou=Room('shaolin/ruzhou', u'汝州城', 'ruzhou', 0, exits)

exits = [
	Exit('west', 'shaolin/shijie7', False),
	Exit('eastup', 'shaolin/shijie8', False),
]
shanmen=Room('shaolin/shanmen', u'少林寺', 'shaolin', 0, exits)

exits = [
	Exit('west', 'shaolin/xiaojing1', False),
	Exit('northup', 'shaolin/shijie2', False),
	Exit('east', 'songshan/taishique', False),
]
shijie1=Room('shaolin/shijie1', u'石阶', 'shaolin', 0, exits)

exits = [
	Exit('southdown', 'shaolin/shijie9', False),
	Exit('northup', 'shaolin/shijie11', False),
]
shijie10=Room('shaolin/shijie10', u'石阶', 'shaolin', 0, exits)

exits = [
	Exit('southdown', 'shaolin/shijie10', False),
	Exit('north', 'shaolin/guangchang1', False),
]
shijie11=Room('shaolin/shijie11', u'石阶', 'shaolin', 0, exits)

exits = [
	Exit('southdown', 'shaolin/shijie1', False),
	Exit('northup', 'shaolin/shijie3', False),
]
shijie2=Room('shaolin/shijie2', u'石阶', 'shaolin', 0, exits)

exits = [
	Exit('southdown', 'shaolin/shijie2', False),
	Exit('westup', 'shaolin/shijie4', False),
]
shijie3=Room('shaolin/shijie3', u'石阶', 'shaolin', 0, exits)

exits = [
	Exit('eastdown', 'shaolin/shijie3', False),
	Exit('northup', 'shaolin/shijie5', False),
]
shijie4=Room('shaolin/shijie4', u'石阶', 'shaolin', 0, exits)

exits = [
	Exit('southdown', 'shaolin/shijie4', False),
	Exit('northup', 'shaolin/shijie6', False),
]
shijie5=Room('shaolin/shijie5', u'石阶', 'shaolin', 0, exits)

exits = [
	Exit('southdown', 'shaolin/shijie5', False),
	Exit('northup', 'shaolin/shijie7', False),
]
shijie6=Room('shaolin/shijie6', u'石阶', 'shaolin', 0, exits)

exits = [
	Exit('southdown', 'shaolin/shijie6', False),
	Exit('east', 'shaolin/shanmen', False),
]
shijie7=Room('shaolin/shijie7', u'石阶', 'shaolin', 0, exits)

exits = [
	Exit('northup', 'shaolin/shijie9', False),
	Exit('westdown', 'shaolin/shanmen', False),
]
shijie8=Room('shaolin/shijie8', u'石阶', 'shaolin', 0, exits)

exits = [
	Exit('southdown', 'shaolin/shijie8', False),
	Exit('northup', 'shaolin/shijie10', False),
]
shijie9=Room('shaolin/shijie9', u'石阶', 'shaolin', 0, exits)

exits = [
	Exit('west', 'shaolin/guangchang1e', False),
	Exit('south', 'shaolin/shulin2', False),
]
shulin1=Room('shaolin/shulin1', u'松树林', 'shaolin', 0, exits)

exits = [
]
shulin10=Room('shaolin/shulin10', u'松树林', 'shaolin', 0, exits)

exits = [
]
shulin11=Room('shaolin/shulin11', u'松树林', 'shaolin', 0, exits)

exits = [
]
shulin12=Room('shaolin/shulin12', u'松树林', 'shaolin', 0, exits)

exits = [
]
shulin13=Room('shaolin/shulin13', u'松树林', 'shaolin', 0, exits)

exits = [
	
	Exit('south', 'shaolin/qyping', False),	
	Exit('west', 'shaolin/shulin8', False),
]
shulin14=Room('shaolin/shulin14', u'松树林', 'shaolin', 0, exits)

exits = [
	Exit('west', 'shaolin/shulin1', False),	
	Exit('east', 'shaolin/shulin3', False),
]
shulin2=Room('shaolin/shulin2', u'松树林', 'shaolin', 0, exits)

exits = [	
	Exit('south', 'shaolin/shulin4', False),	
	Exit('east', 'shaolin/shulin2', False),
]
shulin3=Room('shaolin/shulin3', u'松树林', 'shaolin', 0, exits)

exits = [
	Exit('north', 'shaolin/shulin3', False),
	Exit('east', 'shaolin/shulin5', False),
]
shulin4=Room('shaolin/shulin4', u'松树林', 'shaolin', 0, exits)

exits = [	
	Exit('south', 'shaolin/shulin4', False),
	Exit('north', 'shaolin/shulin6', False),
]
shulin5=Room('shaolin/shulin5', u'松树林', 'shaolin', 0, exits)

exits = [
	Exit('north', 'shaolin/shulin7', False),
	Exit('east', 'shaolin/shulin5', False),
]
shulin6=Room('shaolin/shulin6', u'松树林', 'shaolin', 0, exits)

exits = [
	Exit('north', 'shaolin/shulin6', False),
	Exit('east', 'shaolin/shulin8', False),
]
shulin7=Room('shaolin/shulin7', u'松树林', 'shaolin', 0, exits)

exits = [
	Exit('west', 'shaolin/shulin14', False),
	Exit('east', 'shaolin/shulin7', False),
]
shulin8=Room('shaolin/shulin8', u'松树林', 'shaolin', 0, exits)

exits = [
]
shulin9=Room('shaolin/shulin9', u'松树林', 'shaolin', 0, exits)

exits = [
	Exit('west', 'shaolin/smdian2', False),
	Exit('north', 'shaolin/taijie', False),
	Exit('east', 'shaolin/smdian1', False),
]
smdian=Room('shaolin/smdian', u'山门殿', None, 0, exits)

exits = [
	Exit('west', 'shaolin/smdian', False),
]
smdian1=Room('shaolin/smdian1', u'东侧殿', None, 0, exits)

exits = [
	Exit('east', 'shaolin/smdian', False),
]
smdian2=Room('shaolin/smdian2', u'西侧殿', None, 0, exits)

exits = [
	Exit('west', 'shaolin/beilin2', False),
	Exit('northup', 'shaolin/twdian', False),
	Exit('south', 'shaolin/smdian', False),
	Exit('east', 'shaolin/beilin1', False),
]
taijie=Room('shaolin/taijie', u'台阶', 'shaolin', 0, exits)

exits = [
	Exit('southdown', 'shaolin/taijie', False),
	Exit('west', 'shaolin/twdian2', False),
	Exit('north', 'shaolin/guangchang2', False),
	Exit('east', 'shaolin/twdian1', False),
]
twdian=Room('shaolin/twdian', u'天王殿', None, 0, exits)

exits = [
	Exit('west', 'shaolin/twdian', False),
]
twdian1=Room('shaolin/twdian1', u'东侧殿', None, 0, exits)

exits = [
	Exit('east', 'shaolin/twdian', False),
]
twdian2=Room('shaolin/twdian2', u'西侧殿', None, 0, exits)

exits = [
	Exit('south', 'shaolin/xiaowu', False),
]
woshi=Room('shaolin/woshi', u'卧室', None, 0, exits)

exits = [
	Exit('west', 'shaolin/wuchang1', False),
	Exit('south', 'shaolin/houdian', False),
	Exit('north', 'shaolin/fzlou', False),
	Exit('east', 'shaolin/wuchang2', False),
]
wuchang=Room('shaolin/wuchang', u'练武场', 'shaolin', 0, exits)

exits = [
	Exit('west', 'shaolin/banruo5', False),
	Exit('south', 'shaolin/zoulang2', False),
	Exit('north', 'shaolin/zoulang6', False),
	Exit('east', 'shaolin/wuchang', False),
]
wuchang1=Room('shaolin/wuchang1', u'练武场', 'shaolin', 0, exits)

exits = [
	Exit('west', 'shaolin/wuchang', False),
	Exit('south', 'shaolin/zoulang3', False),
	Exit('north', 'shaolin/zoulang7', False),
	Exit('east', 'shaolin/luohan5', False),
]
wuchang2=Room('shaolin/wuchang2', u'练武场', 'shaolin', 0, exits)

exits = [
	Exit('west', 'shaolin/hsyuan4', False),
	Exit('south', 'shaolin/fzlou', False),
	Exit('up', 'shaolin/dmyuan', False),
	Exit('north', 'shaolin/guangchang5', False),
	Exit('east', 'shaolin/hsyuan1', False),
]
wuchang3=Room('shaolin/wuchang3', u'练武场', 'shaolin', 0, exits)

exits = [
	Exit('west', 'shaolin/zhulin2', True),
	Exit('north', 'shaolin/fangjuku', False),
]
wuqiku=Room('shaolin/wuqiku', u'武器库', None, 0, exits)

exits = [
	Exit('west', 'shaolin/wuxing1', False),
	Exit('south', 'shaolin/wuxing3', False),
	Exit('north', 'shaolin/wuxing2', False),
	Exit('east', 'shaolin/wuxing4', False),
]
wuxing0=Room('shaolin/wuxing0', u'五行洞', None, 0, exits)

exits = [
	Exit('west', 'shaolin/wuxing4', False),
	Exit('south', 'shaolin/wuxing3', False),
	Exit('north', 'shaolin/wuxing2', False),
	Exit('east', 'shaolin/wuxing0', False),
]
wuxing1=Room('shaolin/wuxing1', u'五行洞', None, 0, exits)

exits = [
	Exit('west', 'shaolin/wuxing0', False),
	Exit('south', 'shaolin/wuxing4', False),
	Exit('north', 'shaolin/wuxing3', False),
	Exit('east', 'shaolin/wuxing1', False),
]
wuxing2=Room('shaolin/wuxing2', u'五行洞', None, 0, exits)

exits = [
	Exit('west', 'shaolin/wuxing0', False),
	Exit('south', 'shaolin/wuxing2', False),
	Exit('north', 'shaolin/wuxing4', False),
	Exit('east', 'shaolin/wuxing1', False),
]
wuxing3=Room('shaolin/wuxing3', u'五行洞', None, 0, exits)

exits = [
	Exit('west', 'shaolin/wuxing0', False),
	Exit('south', 'shaolin/wuxing3', False),
	Exit('north', 'shaolin/wuxing2', False),
	Exit('east', 'shaolin/wuxing1', False),
]
wuxing4=Room('shaolin/wuxing4', u'五行洞', None, 0, exits)

exits = [
	Exit('northup', 'shaolin/xiaojing2', False),
	Exit('east', 'shaolin/shijie1', False),
]
xiaojing1=Room('shaolin/xiaojing1', u'山坡', 'shaolin', 0, exits)

exits = [
	Exit('southdown', 'shaolin/xiaojing1', False),
	Exit('west', 'shaolin/houshan', False),
]
xiaojing2=Room('shaolin/xiaojing2', u'田埂边', 'shaolin', 0, exits)

exits = [
	Exit('south', 'shaolin/houshan', False),
	Exit('north', 'shaolin/woshi', False),
]
xiaowu=Room('shaolin/xiaowu', u'小土屋', None, 0, exits)

exits = [
	Exit('south', 'shaolin/fangjuku', False),
]
yaopinku=Room('shaolin/yaopinku', u'药品库', None, 0, exits)

exits = [
	Exit('south', 'city/beimen', False),
	Exit('north', 'shaolin/yidao1', False),
]
yidao=Room('shaolin/yidao', u'大驿道', 'nanyang', 0, exits)

exits = [
	Exit('south', 'shaolin/yidao', False),
	Exit('north', 'shaolin/yidao2', False),
]
yidao1=Room('shaolin/yidao1', u'大驿道', 'nanyang', 0, exits)

exits = [
	Exit('south', 'shaolin/yidao1', False),
	Exit('east', 'room/xiaoyuan', False),
	Exit('north', 'shaolin/hanshui1', False),
]
yidao2=Room('shaolin/yidao2', u'大驿道', 'nanyang', 0, exits)

exits = [
	Exit('south', 'shaolin/nanyang', False),
	Exit('north', 'shaolin/ruzhou', False),
]
yidao3=Room('shaolin/yidao3', u'大驿道', 'nanyang', 0, exits)

exits = [
	Exit('west', 'shaolin/guangchang2', False),
	Exit('enter', 'shaolin/zhonglou1', False),
]
zhonglou=Room('shaolin/zhonglou', u'钟楼小院', 'shaolin', 0, exits)

exits = [
	Exit('out', 'shaolin/zhonglou', False),
	Exit('up', 'shaolin/zhonglou2', False),
]
zhonglou1=Room('shaolin/zhonglou1', u'钟楼一层', None, 0, exits)

exits = [
	Exit('up', 'shaolin/zhonglou3', False),
	Exit('down', 'shaolin/zhonglou1', False),
]
zhonglou2=Room('shaolin/zhonglou2', u'钟楼二层', None, 0, exits)

exits = [
	Exit('up', 'shaolin/zhonglou4', False),
	Exit('down', 'shaolin/zhonglou2', False),
]
zhonglou3=Room('shaolin/zhonglou3', u'钟楼三层', None, 0, exits)

exits = [
	Exit('up', 'shaolin/zhonglou5', False),
	Exit('down', 'shaolin/zhonglou3', False),
]
zhonglou4=Room('shaolin/zhonglou4', u'钟楼四层', None, 0, exits)

exits = [
	Exit('up', 'shaolin/zhonglou6', False),
	Exit('down', 'shaolin/zhonglou4', False),
]
zhonglou5=Room('shaolin/zhonglou5', u'钟楼五层', None, 0, exits)

exits = [
	Exit('up', 'shaolin/zhonglou7', False),
	Exit('down', 'shaolin/zhonglou5', False),
]
zhonglou6=Room('shaolin/zhonglou6', u'钟楼六层', None, 0, exits)

exits = [
	Exit('down', 'shaolin/zhonglou6', False),
]
zhonglou7=Room('shaolin/zhonglou7', u'钟楼七层', None, 0, exits)

exits = [
	Exit('west', 'shaolin/hsyuan1', False),
	Exit('south', 'shaolin/zoulang8', False),
	Exit('north', 'shaolin/zhulin2', False),
]
zhulin1=Room('shaolin/zhulin1', u'竹林小道', 'shaolin', 0, exits)

exits = [
	Exit('west', 'shaolin/hsyuan2', False),
	Exit('south', 'shaolin/zhulin1', False),
	Exit('north', 'shaolin/zhulin3', False),
	Exit('east', 'shaolin/wuqiku', True),
]
zhulin2=Room('shaolin/zhulin2', u'竹林小道', 'shaolin', 0, exits)

exits = [
	Exit('west', 'shaolin/hsyuan3', False),
	Exit('south', 'shaolin/zhulin2', False),
]
zhulin3=Room('shaolin/zhulin3', u'竹林小道', 'shaolin', 0, exits)

exits = [
	Exit('south', 'shaolin/zoulang5', False),
	Exit('north', 'shaolin/zhulin5', False),
	Exit('east', 'shaolin/hsyuan4', False),
]
zhulin4=Room('shaolin/zhulin4', u'竹林小道', 'shaolin', 0, exits)

exits = [
	Exit('west', 'shaolin/cjlou', False),
	Exit('south', 'shaolin/zhulin4', False),
	Exit('north', 'shaolin/zhulin6', False),
	Exit('east', 'shaolin/hsyuan5', False),
]
zhulin5=Room('shaolin/zhulin5', u'竹林小道', 'shaolin', 0, exits)

exits = [
	Exit('south', 'shaolin/zhulin5', False),
	Exit('east', 'shaolin/hsyuan6', False),
]
zhulin6=Room('shaolin/zhulin6', u'竹林小道', 'shaolin', 0, exits)

exits = [
	Exit('southeast', 'shaolin/houshan', False),
]
zhushe=Room('shaolin/zhushe', u'猪舍', None, 0, exits)

exits = [
	Exit('north', 'shaolin/banruo1', False),
	Exit('east', 'shaolin/zoulang2', False),
]
zoulang1=Room('shaolin/zoulang1', u'走廊', None, 0, exits)

exits = [
	Exit('west', 'shaolin/zoulang1', False),
	Exit('north', 'shaolin/wuchang1', False),
	Exit('east', 'shaolin/houdian', False),
]
zoulang2=Room('shaolin/zoulang2', u'走廊', None, 0, exits)

exits = [
	Exit('west', 'shaolin/houdian', False),
	Exit('north', 'shaolin/wuchang2', False),
	Exit('east', 'shaolin/zoulang4', False),
]
zoulang3=Room('shaolin/zoulang3', u'走廊', None, 0, exits)

exits = [
	Exit('west', 'shaolin/zoulang3', False),
	Exit('north', 'shaolin/luohan1', False),
]
zoulang4=Room('shaolin/zoulang4', u'走廊', None, 0, exits)

exits = [
	Exit('southdown', 'shaolin/banruo9', False),
	Exit('north', 'shaolin/zhulin4', False),
	Exit('east', 'shaolin/zoulang6', False),
]
zoulang5=Room('shaolin/zoulang5', u'走廊', None, 0, exits)

exits = [
	Exit('west', 'shaolin/zoulang5', False),
	Exit('south', 'shaolin/wuchang1', False),
	Exit('north', 'shaolin/hsyuan4', False),
	Exit('east', 'shaolin/fzlou', False),
]
zoulang6=Room('shaolin/zoulang6', u'走廊', None, 0, exits)

exits = [
	Exit('west', 'shaolin/fzlou', False),
	Exit('south', 'shaolin/wuchang2', False),
	Exit('north', 'shaolin/hsyuan1', False),
	Exit('east', 'shaolin/zoulang8', False),
]
zoulang7=Room('shaolin/zoulang7', u'走廊', None, 0, exits)

exits = [
	Exit('southdown', 'shaolin/luohan9', False),
	Exit('west', 'shaolin/zoulang7', False),
	Exit('north', 'shaolin/zhulin1', False),
]
zoulang8=Room('shaolin/zoulang8', u'走廊', None, 0, exits)

