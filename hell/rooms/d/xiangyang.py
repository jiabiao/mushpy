# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'xiangyang/anfupailou', False),
]
anfugate=Room('xiangyang/anfugate', u'安抚使衙门', 'xiangyang', 0, exits)

exits = [
	Exit('south', 'xiangyang/guangchang', False),
	Exit('north', 'xiangyang/anfugate', False),
]
anfupailou=Room('xiangyang/anfupailou', u'安抚府牌楼', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/eastroad1', False),
]
biaoju=Room('xiangyang/biaoju', u'福威镖局', None, 0, exits)

exits = [
	Exit('east', 'xiangyang/northjie', False),
]
bingying1=Room('xiangyang/bingying1', u'兵营', None, 0, exits)

exits = [
	Exit('south', 'xiangyang/eastjie3', False),
]
bingying2=Room('xiangyang/bingying2', u'兵营', None, 0, exits)

exits = [
	Exit('east', 'xiangyang/southjie3', False),
]
bingying3=Room('xiangyang/bingying3', u'兵营', None, 0, exits)

exits = [
	Exit('south', 'xiangyang/westjie3', False),
]
bingying4=Room('xiangyang/bingying4', u'兵营', None, 0, exits)

exits = [
	Exit('west', 'xiangyang/northgate2', False),
]
caodi1=Room('xiangyang/caodi1', u'草地', 'xiangyang', 0, exits)

exits = [
	Exit('east', 'xiangyang/northgate2', False),
]
caodi2=Room('xiangyang/caodi2', u'草地', 'xiangyang', 0, exits)

exits = [
	Exit('south', 'xiangyang/northgate2', False),
	Exit('north', 'changan/hanguguan', False),
]
caodi3=Room('xiangyang/caodi3', u'草地', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/southgate2', False),
	Exit('east', 'xiangyang/huapu', False),
]
caodi4=Room('xiangyang/caodi4', u'草地', 'xiangyang', 0, exits)

exits = [
	Exit('east', 'xiangyang/southgate2', False),
]
caodi5=Room('xiangyang/caodi5', u'草地', 'xiangyang', 0, exits)

exits = [
	Exit('south', 'wudang/wdroad5', False),
	Exit('north', 'xiangyang/southgate2', False),
]
caodi6=Room('xiangyang/caodi6', u'草地', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/northjie', False),
]
chaguan=Room('xiangyang/chaguan', u'茶馆', None, 0, exits)

exits = [
	Exit('north', 'xiangyang/westjie3', False),
]
dajiaochang=Room('xiangyang/dajiaochang', u'大校场', 'xiangyang', 0, exits)

exits = [
	Exit('north', 'xiangyang/westjie1', False),
]
dangpu=Room('xiangyang/dangpu', u'当铺', None, 0, exits)

exits = [
	Exit('west', 'xiangyang/northroad1', False),
	Exit('north', 'xiangyang/northjie', False),
	Exit('east', 'xiangyang/northroad2', False),
]
dingzi=Room('xiangyang/dingzi', u'丁字街口', 'xiangyang', 0, exits)

exits = [
	Exit('east', 'xiangyang/southjie2', False),
]
duchang=Room('xiangyang/duchang', u'赌场', None, 0, exits)

exits = [
	Exit('west', 'xiangyang/eastjie3', False),
	Exit('southup', 'xiangyang/walle1', False),
	Exit('northup', 'xiangyang/walle2', False),
	Exit('east', 'xiangyang/eastgate2', False),
]
eastgate1=Room('xiangyang/eastgate1', u'青龙内门', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/eastgate1', False),
]
eastgate2=Room('xiangyang/eastgate2', u'青龙外门', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/guangchang', False),
	Exit('south', 'xiangyang/yaopu', False),
	Exit('north', 'xiangyang/jiangjungate', False),
	Exit('east', 'xiangyang/eastjie2', False),
]
eastjie1=Room('xiangyang/eastjie1', u'东大街', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/eastjie1', False),
	Exit('south', 'xiangyang/jiedao', False),
	Exit('north', 'xiangyang/eastroad1', False),
	Exit('east', 'xiangyang/eastjie3', False),
]
eastjie2=Room('xiangyang/eastjie2', u'东大街', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/eastjie2', False),
	Exit('south', 'xiangyang/mujiang', False),
	Exit('north', 'xiangyang/bingying2', False),
	Exit('east', 'xiangyang/eastgate1', False),
]
eastjie3=Room('xiangyang/eastjie3', u'东大街', 'xiangyang', 0, exits)

exits = [
	Exit('south', 'xiangyang/eastjie2', False),
	Exit('north', 'xiangyang/eastroad2', False),
	Exit('east', 'xiangyang/biaoju', False),
]
eastroad1=Room('xiangyang/eastroad1', u'东内大街', 'xiangyang', 0, exits)

exits = [
	Exit('south', 'xiangyang/eastroad1', False),
	Exit('north', 'xiangyang/jiekou2', False),
	Exit('east', 'xiangyang/zhonglie', False),
]
eastroad2=Room('xiangyang/eastroad2', u'东内大街', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/westjie1', False),
	Exit('south', 'xiangyang/southjie1', False),
	Exit('north', 'xiangyang/anfupailou', False),
	Exit('east', 'xiangyang/eastjie1', False),
]
guangchang=Room('xiangyang/guangchang', u'中央广场', 'xiangyang', 0, exits)

exits = [
	Exit('south', 'xiangyang/westjie1', False),
	Exit('north', 'xiangyang/guofuyuan', False),
]
guofugate=Room('xiangyang/guofugate', u'郭府大门', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/guofukefang', False),
	Exit('south', 'xiangyang/guofuting', False),
	Exit('north', 'xiangyang/guofushufang', False),
	Exit('east', 'xiangyang/guofuwoshi', False),
]
guofuhuayuan=Room('xiangyang/guofuhuayuan', u'郭府后花园', None, 0, exits)

exits = [
	Exit('east', 'xiangyang/guofuhuayuan', False),
]
guofukefang=Room('xiangyang/guofukefang', u'客房', None, 0, exits)

exits = [
	Exit('south', 'xiangyang/guofuhuayuan', False),
]
guofushufang=Room('xiangyang/guofushufang', u'书房', None, 0, exits)

exits = [
	Exit('south', 'xiangyang/guofuyuan', False),
	Exit('north', 'xiangyang/guofuhuayuan', False),
]
guofuting=Room('xiangyang/guofuting', u'郭府客厅', None, 0, exits)

exits = [
	Exit('west', 'xiangyang/guofuhuayuan', False),
]
guofuwoshi=Room('xiangyang/guofuwoshi', u'卧室', None, 0, exits)

exits = [
	Exit('south', 'xiangyang/guofugate', False),
	Exit('north', 'xiangyang/guofuting', False),
]
guofuyuan=Room('xiangyang/guofuyuan', u'郭府大院', 'xiangyang', 0, exits)

exits = [
	Exit('north', 'xiangyang/maoshe', False),
]
huafang=Room('xiangyang/huafang', u'花房', None, 0, exits)

exits = [
	Exit('west', 'xiangyang/caodi4', False),
	Exit('south', 'xiangyang/huapu2', False),
	Exit('north', 'xiangyang/xibian', False),
	Exit('east', 'xiangyang/maoshe', False),
]
huapu=Room('xiangyang/huapu', u'花圃', 'xiangyang', 0, exits)

exits = [
	Exit('north', 'xiangyang/huapu', False),
]
huapu2=Room('xiangyang/huapu2', u'花圃', 'xiangyang', 0, exits)

exits = [
	Exit('east', 'xiangyang/jiekou1', False),
]
hutong1=Room('xiangyang/hutong1', u'胡同', 'xiangyang', 0, exits)

exits = [
	Exit('south', 'xiangyang/jiekou1', False),
]
hutong2=Room('xiangyang/hutong2', u'胡同', 'xiangyang', 0, exits)

exits = [
	Exit('south', 'xiangyang/eastjie1', False),
	Exit('north', 'xiangyang/jiangjunyuan', False),
]
jiangjungate=Room('xiangyang/jiangjungate', u'将军府大门', 'xiangyang', 0, exits)

exits = [
	Exit('south', 'xiangyang/jiangjunyuan', False),
]
jiangjuntang=Room('xiangyang/jiangjuntang', u'将军府大堂', None, 0, exits)

exits = [
	Exit('south', 'xiangyang/jiangjungate', False),
	Exit('north', 'xiangyang/jiangjuntang', False),
]
jiangjunyuan=Room('xiangyang/jiangjunyuan', u'将军府大院', None, 0, exits)

exits = [
	Exit('west', 'xiangyang/minju2', False),
	Exit('north', 'xiangyang/eastjie2', False),
	Exit('east', 'xiangyang/minju1', False),
]
jiedao=Room('xiangyang/jiedao', u'街道', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/hutong1', False),
	Exit('south', 'xiangyang/westroad2', False),
	Exit('north', 'xiangyang/hutong2', False),
	Exit('east', 'xiangyang/northroad1', False),
]
jiekou1=Room('xiangyang/jiekou1', u'大街口', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/northroad2', False),
	Exit('south', 'xiangyang/eastroad2', False),
	Exit('north', 'xiangyang/xiaorong2', False),
	Exit('east', 'xiangyang/xiaorong1', False),
]
jiekou2=Room('xiangyang/jiekou2', u'大街口', 'xiangyang', 0, exits)

exits = [
	Exit('north', 'xiangyang/juyihuayuan', False),
]
juyichufang=Room('xiangyang/juyichufang', u'厨房', None, 0, exits)

exits = [
	Exit('west', 'xiangyang/juyihuayuan', False),
]
juyifemale=Room('xiangyang/juyifemale', u'女客房', None, 0, exits)

exits = [
	Exit('southeast', 'xiangyang/juyiwupin', False),
	Exit('west', 'xiangyang/juyimale', False),
	Exit('south', 'xiangyang/juyichufang', False),
	Exit('north', 'xiangyang/juyilang', False),
	Exit('east', 'xiangyang/juyifemale', False),
]
juyihuayuan=Room('xiangyang/juyihuayuan', u'花园', 'xiangyang', 0, exits)

exits = [
	Exit('south', 'xiangyang/juyihuayuan', False),
	Exit('north', 'xiangyang/juyiyuan', False),
]
juyilang=Room('xiangyang/juyilang', u'水上走廊', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/juyiyuan', False),
]
juyilianwu1=Room('xiangyang/juyilianwu1', u'练功场', 'xiangyang', 0, exits)

exits = [
	Exit('east', 'xiangyang/juyiyuan', False),
]
juyilianwu2=Room('xiangyang/juyilianwu2', u'练功场', 'xiangyang', 0, exits)

exits = [
	Exit('east', 'xiangyang/juyihuayuan', False),
]
juyimale=Room('xiangyang/juyimale', u'男客房', None, 0, exits)

exits = [
	Exit('northwest', 'xiangyang/juyihuayuan', False),
]
juyiwupin=Room('xiangyang/juyiwupin', u'物品房', None, 0, exits)

exits = [
	Exit('west', 'xiangyang/juyilianwu2', False),
	Exit('south', 'xiangyang/juyilang', False),
	Exit('north', 'xiangyang/westjie2', False),
	Exit('east', 'xiangyang/juyilianwu1', False),
]
juyiyuan=Room('xiangyang/juyiyuan', u'大院', 'xiangyang', 0, exits)

exits = [
	Exit('east', 'xiangyang/westroad1', False),
]
kedian=Room('xiangyang/kedian', u'襄阳客栈', None, 0, exits)

exits = [
	Exit('south', 'xiangyang/maoshe', True),
]
liwu=Room('xiangyang/liwu', u'里屋', None, 0, exits)

exits = [
	Exit('south', 'xiangyang/northroad2', False),
]
majiu=Room('xiangyang/majiu', u'马厩', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/huapu', False),
	Exit('south', 'xiangyang/huafang', False),
	Exit('north', 'xiangyang/liwu', True),
]
maoshe=Room('xiangyang/maoshe', u'茅舍', None, 0, exits)

exits = [
	Exit('west', 'xiangyang/jiedao', False),
]
minju1=Room('xiangyang/minju1', u'民居', None, 0, exits)

exits = [
	Exit('east', 'xiangyang/jiedao', False),
]
minju2=Room('xiangyang/minju2', u'民居', None, 0, exits)

exits = [
	Exit('north', 'xiangyang/eastjie3', False),
]
mujiang=Room('xiangyang/mujiang', u'木匠铺', None, 0, exits)

exits = [
	Exit('west', 'xiangyang/southjie2', False),
]
nixianglou=Room('xiangyang/nixianglou', u'觅香楼', None, 0, exits)

exits = [
	Exit('south', 'xiangyang/northjie', False),
	Exit('eastup', 'xiangyang/walln1', False),
	Exit('north', 'xiangyang/northgate2', False),
	Exit('westup', 'xiangyang/walln2', False),
]
northgate1=Room('xiangyang/northgate1', u'玄武内门', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/caodi2', False),
	Exit('south', 'xiangyang/northgate1', False),
	Exit('east', 'xiangyang/caodi1', False),
	Exit('north', 'xiangyang/caodi3', False),
]
northgate2=Room('xiangyang/northgate2', u'玄武外门', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/bingying1', False),
	Exit('south', 'xiangyang/dingzi', False),
	Exit('north', 'xiangyang/northgate1', False),
	Exit('east', 'xiangyang/chaguan', False),
]
northjie=Room('xiangyang/northjie', u'北大街', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/jiekou1', False),
	Exit('north', 'xiangyang/xinluofang', False),
	Exit('east', 'xiangyang/dingzi', False),
]
northroad1=Room('xiangyang/northroad1', u'北内大街', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/dingzi', False),
	Exit('north', 'xiangyang/majiu', False),
	Exit('east', 'xiangyang/jiekou2', False),
]
northroad2=Room('xiangyang/northroad2', u'北内大街', 'xiangyang', 0, exits)

exits = [
	Exit('east', 'xiangyang/southjie1', False),
]
qianzhuang=Room('xiangyang/qianzhuang', u'钱庄', None, 0, exits)

exits = [
	Exit('east', 'xiangyang/westroad2', False),
]
shudian=Room('xiangyang/shudian', u'书店', None, 0, exits)

exits = [
	Exit('south', 'xiangyang/southgate2', False),
	Exit('eastup', 'xiangyang/walls2', False),
	Exit('north', 'xiangyang/southjie3', False),
	Exit('westup', 'xiangyang/walls1', False),
]
southgate1=Room('xiangyang/southgate1', u'朱雀内门', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/caodi5', False),
	Exit('south', 'xiangyang/caodi6', False),
	Exit('north', 'xiangyang/southgate1', False),
	Exit('east', 'xiangyang/caodi4', False),
]
southgate2=Room('xiangyang/southgate2', u'朱雀外门', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/qianzhuang', False),
	Exit('south', 'xiangyang/southjie2', False),
	Exit('north', 'xiangyang/guangchang', False),
	Exit('east', 'xiangyang/xuetang', False),
]
southjie1=Room('xiangyang/southjie1', u'南大街', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/duchang', False),
	Exit('south', 'xiangyang/southjie3', False),
	Exit('north', 'xiangyang/southjie1', False),
	Exit('east', 'xiangyang/nixianglou', False),
]
southjie2=Room('xiangyang/southjie2', u'南大街', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/bingying3', False),
	Exit('south', 'xiangyang/southgate1', False),
	Exit('north', 'xiangyang/southjie2', False),
	Exit('east', 'xiangyang/tiejiangpu', False),
]
southjie3=Room('xiangyang/southjie3', u'南大街', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/southjie3', False),
]
tiejiangpu=Room('xiangyang/tiejiangpu', u'兵器铺', None, 0, exits)

exits = [
	Exit('southup', 'xiangyang/walle3', False),
	Exit('northdown', 'xiangyang/eastgate1', False),
]
walle1=Room('xiangyang/walle1', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('southdown', 'xiangyang/eastgate1', False),
	Exit('northup', 'xiangyang/walle4', False),
]
walle2=Room('xiangyang/walle2', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('southup', 'xiangyang/walle5', False),
	Exit('northdown', 'xiangyang/walle1', False),
]
walle3=Room('xiangyang/walle3', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('southdown', 'xiangyang/walle2', False),
	Exit('northup', 'xiangyang/walle6', False),
]
walle4=Room('xiangyang/walle4', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('southup', 'xiangyang/walle7', False),
	Exit('northdown', 'xiangyang/walle3', False),
]
walle5=Room('xiangyang/walle5', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('southdown', 'xiangyang/walle4', False),
	Exit('northup', 'xiangyang/walle8', False),
]
walle6=Room('xiangyang/walle6', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('southwest', 'xiangyang/walls8', False),
	Exit('northdown', 'xiangyang/walle5', False),
]
walle7=Room('xiangyang/walle7', u'东城头', 'xiangyang', 0, exits)

exits = [
	Exit('southdown', 'xiangyang/walle6', False),
	Exit('northwest', 'xiangyang/walln7', False),
]
walle8=Room('xiangyang/walle8', u'东城头', 'xiangyang', 0, exits)

exits = [
	Exit('eastup', 'xiangyang/walln3', False),
	Exit('westdown', 'xiangyang/northgate1', False),
]
walln1=Room('xiangyang/walln1', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('eastdown', 'xiangyang/northgate1', False),
	Exit('westup', 'xiangyang/walln4', False),
]
walln2=Room('xiangyang/walln2', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('eastup', 'xiangyang/walln5', False),
	Exit('westdown', 'xiangyang/walln1', False),
]
walln3=Room('xiangyang/walln3', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('eastdown', 'xiangyang/walln2', False),
	Exit('westup', 'xiangyang/walln6', False),
]
walln4=Room('xiangyang/walln4', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('eastup', 'xiangyang/walln7', False),
	Exit('westdown', 'xiangyang/walln3', False),
]
walln5=Room('xiangyang/walln5', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('eastdown', 'xiangyang/walln4', False),
	Exit('westup', 'xiangyang/walln8', False),
]
walln6=Room('xiangyang/walln6', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('southeast', 'xiangyang/walle8', False),
	Exit('westdown', 'xiangyang/walln5', False),
]
walln7=Room('xiangyang/walln7', u'北城头', 'xiangyang', 0, exits)

exits = [
	Exit('eastdown', 'xiangyang/walln6', False),
	Exit('southwest', 'xiangyang/wallw7', False),
]
walln8=Room('xiangyang/walln8', u'北城头', 'xiangyang', 0, exits)

exits = [
	Exit('eastdown', 'xiangyang/southgate1', False),
	Exit('westup', 'xiangyang/walls3', False),
]
walls1=Room('xiangyang/walls1', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('eastup', 'xiangyang/walls4', False),
	Exit('westdown', 'xiangyang/southgate1', False),
]
walls2=Room('xiangyang/walls2', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('eastdown', 'xiangyang/walls1', False),
	Exit('westup', 'xiangyang/walls5', False),
]
walls3=Room('xiangyang/walls3', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('eastup', 'xiangyang/walls6', False),
	Exit('westdown', 'xiangyang/walls2', False),
]
walls4=Room('xiangyang/walls4', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('eastdown', 'xiangyang/walls3', False),
	Exit('westup', 'xiangyang/walls7', False),
]
walls5=Room('xiangyang/walls5', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('eastup', 'xiangyang/walls8', False),
	Exit('westdown', 'xiangyang/walls4', False),
]
walls6=Room('xiangyang/walls6', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('northwest', 'xiangyang/wallw8', False),
	Exit('eastdown', 'xiangyang/walls5', False),
]
walls7=Room('xiangyang/walls7', u'南城头', 'xiangyang', 0, exits)

exits = [
	Exit('westdown', 'xiangyang/walls6', False),
	Exit('northeast', 'xiangyang/walle7', False),
]
walls8=Room('xiangyang/walls8', u'南城头', 'xiangyang', 0, exits)

exits = [
	Exit('southdown', 'xiangyang/westgate1', False),
	Exit('northup', 'xiangyang/wallw3', False),
]
wallw1=Room('xiangyang/wallw1', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('southup', 'xiangyang/wallw4', False),
	Exit('northdown', 'xiangyang/westgate1', False),
]
wallw2=Room('xiangyang/wallw2', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('southdown', 'xiangyang/wallw1', False),
	Exit('northup', 'xiangyang/wallw5', False),
]
wallw3=Room('xiangyang/wallw3', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('southup', 'xiangyang/wallw6', False),
	Exit('northdown', 'xiangyang/wallw2', False),
]
wallw4=Room('xiangyang/wallw4', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('southdown', 'xiangyang/wallw3', False),
	Exit('northup', 'xiangyang/wallw7', False),
]
wallw5=Room('xiangyang/wallw5', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('southup', 'xiangyang/wallw8', False),
	Exit('northdown', 'xiangyang/wallw4', False),
]
wallw6=Room('xiangyang/wallw6', u'石阶', 'xiangyang', 0, exits)

exits = [
	Exit('southdown', 'xiangyang/wallw5', False),
	Exit('northeast', 'xiangyang/walln8', False),
]
wallw7=Room('xiangyang/wallw7', u'西城头', 'xiangyang', 0, exits)

exits = [
	Exit('southeast', 'xiangyang/walls7', False),
	Exit('northdown', 'xiangyang/wallw6', False),
]
wallw8=Room('xiangyang/wallw8', u'西城头', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/westgate2', False),
	Exit('southup', 'xiangyang/wallw2', False),
	Exit('northup', 'xiangyang/wallw1', False),
	Exit('east', 'xiangyang/westjie3', False),
]
westgate1=Room('xiangyang/westgate1', u'白虎内门', 'xiangyang', 0, exits)

exits = [
	Exit('east', 'xiangyang/westgate1', False),
]
westgate2=Room('xiangyang/westgate2', u'白虎外门', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/westjie2', False),
	Exit('south', 'xiangyang/dangpu', False),
	Exit('north', 'xiangyang/guofugate', False),
	Exit('east', 'xiangyang/guangchang', False),
]
westjie1=Room('xiangyang/westjie1', u'西大街', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/westjie3', False),
	Exit('south', 'xiangyang/juyiyuan', False),
	Exit('north', 'xiangyang/westroad1', False),
	Exit('east', 'xiangyang/westjie1', False),
]
westjie2=Room('xiangyang/westjie2', u'西大街', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/westgate1', False),
	Exit('south', 'xiangyang/dajiaochang', False),
	Exit('north', 'xiangyang/bingying4', False),
	Exit('east', 'xiangyang/westjie2', False),
]
westjie3=Room('xiangyang/westjie3', u'西大街', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/kedian', False),
	Exit('south', 'xiangyang/westjie2', False),
	Exit('north', 'xiangyang/westroad2', False),
]
westroad1=Room('xiangyang/westroad1', u'西内大街', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/shudian', False),
	Exit('south', 'xiangyang/westroad1', False),
	Exit('north', 'xiangyang/jiekou1', False),
]
westroad2=Room('xiangyang/westroad2', u'西内大街', 'xiangyang', 0, exits)

exits = [
	Exit('west', 'xiangyang/jiekou2', False),
]
xiaorong1=Room('xiangyang/xiaorong1', u'胡同', 'xiangyang', 0, exits)

exits = [
	Exit('south', 'xiangyang/jiekou2', False),
]
xiaorong2=Room('xiangyang/xiaorong2', u'胡同', 'xiangyang', 0, exits)

exits = [
	Exit('south', 'xiangyang/huapu', False),
]
xibian=Room('xiangyang/xibian', u'溪边', 'xiangyang', 0, exits)

exits = [
	Exit('south', 'xiangyang/northroad1', False),
]
xinluofang=Room('xiangyang/xinluofang', u'新罗坊', None, 0, exits)

exits = [
	Exit('west', 'xiangyang/southjie1', False),
]
xuetang=Room('xiangyang/xuetang', u'学堂', None, 0, exits)

exits = [
	Exit('north', 'xiangyang/eastjie1', False),
]
yaopu=Room('xiangyang/yaopu', u'药铺', None, 0, exits)

exits = [
	Exit('west', 'xiangyang/eastroad2', False),
]
zhonglie=Room('xiangyang/zhonglie', u'忠烈祠', None, 0, exits)

