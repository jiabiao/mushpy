# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('southwest', 'huanghe/shixiazi', False),
	Exit('northeast', 'huanghe/yinpanshui', False),
]
bingcao=Room('huanghe/bingcao', u'冰草湾', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/caodi2', False),
	Exit('east', 'city/beimen', False),
]
caodi1=Room('huanghe/caodi1', u'草地', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/shulin1', False),
	Exit('east', 'huanghe/caodi1', False),
]
caodi2=Room('huanghe/caodi2', u'草地', 'huanghe', 0, exits)

exits = [
	Exit('southwest', 'huanghe/gulang', False),
	Exit('north', 'huanghe/wuqiao', False),
]
dacaigou=Room('huanghe/dacaigou', u'打柴沟', 'huanghe', 0, exits)

exits = [
]
duchuan=Room('huanghe/duchuan', u'渡船', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/xiayiting', False),
	Exit('east', 'huanghe/huanghegate', False),
]
guangchang=Room('huanghe/guangchang', u'广场', 'huanghe', 0, exits)

exits = [
	Exit('southeast', 'huanghe/shimen', False),
	Exit('southwest', 'huanghe/yinpanshui', False),
]
guchangcheng=Room('huanghe/guchangcheng', u'古长城', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/xiaojiaqiao', False),
	Exit('south', 'huanghe/yongdeng', False),
	Exit('northeast', 'huanghe/dacaigou', False),
	Exit('east', 'huanghe/yaocaidian', False),
	Exit('north', 'huanghe/xueguan', False),
]
gulang=Room('huanghe/gulang', u'古浪', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/qingcheng', False),
	Exit('southwest', 'huanghe/huangtu', False),
	Exit('east', 'huanghe/huanghe_1', False),
]
hetao=Room('huanghe/hetao', u'河套', 'huanghe', 0, exits)

exits = [
	Exit('south', 'huanghe/jingyuan', False),
	Exit('north', 'huanghe/shimen', False),
]
hongshanxia=Room('huanghe/hongshanxia', u'红山峡', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/huanghegate', False),
	Exit('south', 'huanghe/tiandi4', False),
	Exit('east', 'huanghe/huanghe2', False),
	Exit('north', 'huanghe/weifen', False),
]
huanghe1=Room('huanghe/huanghe1', u'黄河岸边', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/huanghe1', False),
	Exit('east', 'huanghe/huanghe3', False),
]
huanghe2=Room('huanghe/huanghe2', u'黄河岸边', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/huanghe2', False),
	Exit('east', 'huanghe/huanghe4', False),
]
huanghe3=Room('huanghe/huanghe3', u'黄河岸边', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/huanghe3', False),
	Exit('northeast', 'huanghe/huanghe5', False),
]
huanghe4=Room('huanghe/huanghe4', u'黄河岸边', 'huanghe', 0, exits)

exits = [
	Exit('southwest', 'huanghe/huanghe4', False),
	Exit('northeast', 'huanghe/huanghe6', False),
	Exit('east', 'taishan/daizong', False),
]
huanghe5=Room('huanghe/huanghe5', u'黄河岸边', 'huanghe', 0, exits)

exits = [
	Exit('southwest', 'huanghe/huanghe5', False),
	Exit('northeast', 'huanghe/huanghe7', False),
]
huanghe6=Room('huanghe/huanghe6', u'黄河岸边', 'huanghe', 0, exits)

exits = [
	Exit('southwest', 'huanghe/huanghe6', False),
	Exit('northeast', 'huanghe/huanghe8', False),
]
huanghe7=Room('huanghe/huanghe7', u'黄河岸边', 'huanghe', 0, exits)

exits = [
	Exit('southwest', 'huanghe/huanghe7', False),
]
huanghe8=Room('huanghe/huanghe8', u'黄河入海口', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/hetao', False),
	Exit('south', 'huanghe/weifen', False),
]
huanghe_1=Room('huanghe/huanghe_1', u'黄河', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/huanghe_3', False),
	Exit('northeast', 'huanghe/huangtu', False),
]
huanghe_2=Room('huanghe/huanghe_2', u'黄河', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/yongdeng', False),
	Exit('east', 'huanghe/huanghe_2', False),
]
huanghe_3=Room('huanghe/huanghe_3', u'黄河', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/guangchang', False),
	Exit('east', 'huanghe/huanghe1', False),
]
huanghegate=Room('huanghe/huanghegate', u'黄河帮寨门', 'huanghe', 0, exits)

exits = [
	Exit('southwest', 'huanghe/huanghe_2', False),
	Exit('northeast', 'huanghe/hetao', False),
]
huangtu=Room('huanghe/huangtu', u'黄土高原', 'huanghe', 0, exits)

exits = [
	Exit('south', 'huanghe/shamo', False),
	Exit('north', 'huanghe/hongshanxia', False),
]
jingyuan=Room('huanghe/jingyuan', u'靖远', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/majiu', False),
	Exit('up', 'huanghe/kedian2', False),
	Exit('east', 'huanghe/yongdeng', False),
]
kedian=Room('huanghe/kedian', u'客店', None, 0, exits)

exits = [
	Exit('enter', 'huanghe/kedian3', False),
	Exit('down', 'huanghe/kedian', False),
]
kedian2=Room('huanghe/kedian2', u'客店二楼', None, 0, exits)

exits = [
	Exit('out', 'huanghe/kedian2', False),
]
kedian3=Room('huanghe/kedian3', u'客店二楼', None, 0, exits)

exits = [
	Exit('eastdown', 'village/wexit', False),
	Exit('northdown', 'huanghe/yongdeng', False),
]
liupanshan=Room('huanghe/liupanshan', u'六盘山', 'huanghe', 0, exits)

exits = [
	Exit('east', 'huanghe/kedian', False),
]
majiu=Room('huanghe/majiu', u'马厩', 'huanghe', 0, exits)

exits = [
	Exit('east', 'huanghe/hetao', False),
	Exit('north', 'huanghe/shamo', False),
]
qingcheng=Room('huanghe/qingcheng', u'青城', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/shamo', False),
	Exit('south', 'huanghe/shamo1', False),
	Exit('east', 'huanghe/shamo', False),
	Exit('north', 'huanghe/shamo', False),
]
shamo=Room('huanghe/shamo', u'沙漠', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/shamo1', False),
	Exit('south', 'huanghe/shamo1', False),
	Exit('east', 'huanghe/shamo1', False),
	Exit('north', 'huanghe/shamo1', False),
	Exit('enter', 'huanghe/shidong', False),
]
shamo1=Room('huanghe/shamo1', u'沙漠', 'huanghe', 0, exits)

exits = [
	Exit('out', 'huanghe/shamo1', False),
]
shidong=Room('huanghe/shidong', u'石洞', None, 0, exits)

exits = [
	Exit('northwest', 'huanghe/yinpanshui', False),
	Exit('south', 'huanghe/hongshanxia', False),
	Exit('north', 'huanghe/wufosi', False),
]
shimen=Room('huanghe/shimen', u'石门', 'huanghe', 0, exits)

exits = [
	Exit('southwest', 'huanghe/tumenzi', False),
	Exit('northeast', 'huanghe/bingcao', False),
]
shixiazi=Room('huanghe/shixiazi', u'石峡子', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/shulin2', False),
	Exit('north', 'huanghe/shulin3', False),
	Exit('east', 'huanghe/caodi2', False),
]
shulin1=Room('huanghe/shulin1', u'树林', 'huanghe', 0, exits)

exits = [
	Exit('north', 'huanghe/shulin4', False),
	Exit('east', 'huanghe/shulin1', False),
]
shulin2=Room('huanghe/shulin2', u'树林', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/shulin4', False),
	Exit('south', 'huanghe/shulin1', False),
	Exit('north', 'huanghe/tiandi1', False),
]
shulin3=Room('huanghe/shulin3', u'树林', 'huanghe', 0, exits)

exits = [
	Exit('northwest', 'huanghe/shulin5', False),
	Exit('south', 'huanghe/shulin2', False),
	Exit('east', 'huanghe/shulin3', False),
]
shulin4=Room('huanghe/shulin4', u'树林', 'huanghe', 0, exits)

exits = [
	Exit('southeast', 'huanghe/shulin4', False),
	Exit('west', 'huanghe/shulin6', False),
	Exit('northeast', 'huanghe/tiandi2', False),
]
shulin5=Room('huanghe/shulin5', u'树林', 'huanghe', 0, exits)

exits = [
	Exit('east', 'huanghe/shulin5', False),
]
shulin6=Room('huanghe/shulin6', u'树林', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/tiandi2', False),
	Exit('south', 'huanghe/shulin3', False),
	Exit('east', 'huanghe/tiandi3', False),
]
tiandi1=Room('huanghe/tiandi1', u'田地', 'huanghe', 0, exits)

exits = [
	Exit('southwest', 'huanghe/shulin5', False),
	Exit('east', 'huanghe/tiandi1', False),
]
tiandi2=Room('huanghe/tiandi2', u'田地', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/tiandi1', False),
	Exit('northeast', 'huanghe/tiandi4', False),
]
tiandi3=Room('huanghe/tiandi3', u'田地', 'huanghe', 0, exits)

exits = [
	Exit('southwest', 'huanghe/tiandi3', False),
	Exit('north', 'huanghe/huanghe1', False),
]
tiandi4=Room('huanghe/tiandi4', u'田地', 'huanghe', 0, exits)

exits = [
	Exit('south', 'huanghe/wuwei', False),
	Exit('northeast', 'huanghe/shixiazi', False),
]
tumenzi=Room('huanghe/tumenzi', u'土门子', 'huanghe', 0, exits)

exits = [
	Exit('south', 'huanghe/huanghe1', False),
	Exit('southwest', 'heimuya/road5', False),
	Exit('northeast', 'heimuya/dukou2', False),
	Exit('north', 'huanghe/huanghe_1', False),
]
weifen=Room('huanghe/weifen', u'渭汾流域', 'huanghe', 0, exits)

exits = [
	Exit('south', 'huanghe/shimen', False),
]
wufosi=Room('huanghe/wufosi', u'五佛寺', None, 0, exits)

exits = [
	Exit('northwest', 'huanghe/wuwei', False),
	Exit('south', 'huanghe/dacaigou', False),
]
wuqiao=Room('huanghe/wuqiao', u'乌鞘岭', 'huanghe', 0, exits)

exits = [
	Exit('southeast', 'huanghe/wuqiao', False),
	Exit('north', 'huanghe/tumenzi', False),
]
wuwei=Room('huanghe/wuwei', u'武威', 'huanghe', 0, exits)

exits = [
	Exit('east', 'huanghe/gulang', False),
]
xiaojiaqiao=Room('huanghe/xiaojiaqiao', u'萧家桥', 'huanghe', 0, exits)

exits = [
	Exit('east', 'huanghe/guangchang', False),
]
xiayiting=Room('huanghe/xiayiting', u'侠义厅', 'huanghe', 0, exits)

exits = [
	Exit('south', 'huanghe/gulang', False),
]
xueguan=Room('huanghe/xueguan', u'学馆', None, 0, exits)

exits = [
	Exit('west', 'huanghe/gulang', False),
]
yaocaidian=Room('huanghe/yaocaidian', u'皮货药材店', None, 0, exits)

exits = [
	Exit('southwest', 'huanghe/bingcao', False),
	Exit('northeast', 'huanghe/guchangcheng', False),
]
yinpanshui=Room('huanghe/yinpanshui', u'营盘水', 'huanghe', 0, exits)

exits = [
	Exit('west', 'huanghe/kedian', False),
	Exit('southup', 'changan/tulu4', False),
	Exit('east', 'huanghe/huanghe_3', False),
	Exit('north', 'huanghe/gulang', False),
]
yongdeng=Room('huanghe/yongdeng', u'永登', 'huanghe', 0, exits)

