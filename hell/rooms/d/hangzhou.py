# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('southwest', 'hangzhou/pinghuqiuyue', False),
	Exit('east', 'hangzhou/duanqiao', False),
]
baiti=Room('hangzhou/baiti', u'白堤', 'hangzhou', 0, exits)

exits = [
	Exit('southdown', 'hangzhou/road8', False),
	Exit('northup', 'hangzhou/baoshuta', False),
]
baoshishan=Room('hangzhou/baoshishan', u'宝石山', 'hangzhou', 0, exits)

exits = [
	Exit('southdown', 'hangzhou/baoshishan', False),
]
baoshuta=Room('hangzhou/baoshuta', u'保淑塔', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/longjing', False),
]
chashi=Room('hangzhou/chashi', u'茶室', None, 0, exits)

exits = [
	Exit('westdown', 'hangzhou/qinglindong', False),
]
cuiweiting=Room('hangzhou/cuiweiting', u'翠微亭', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/guozhuang', False),
	Exit('south', 'hangzhou/dadao2', False),
	Exit('north', 'hangzhou/road5', False),
]
dadao1=Room('hangzhou/dadao1', u'沿湖大道', 'hangzhou', 0, exits)

exits = [
	Exit('southwest', 'hangzhou/dalu1', False),
	Exit('north', 'hangzhou/dadao1', False),
]
dadao2=Room('hangzhou/dadao2', u'沿湖大道', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/liuzhuang', False),
	Exit('south', 'hangzhou/road19', False),
	Exit('north', 'hangzhou/dalu1', False),
]
dadao3=Room('hangzhou/dadao3', u'沿湖大道', 'hangzhou', 0, exits)

exits = [
	Exit('south', 'hangzhou/dadao3', False),
	Exit('northeast', 'hangzhou/dadao2', False),
]
dalu1=Room('hangzhou/dalu1', u'大路', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/baiti', False),
	Exit('northeast', 'hangzhou/road9', False),
]
duanqiao=Room('hangzhou/duanqiao', u'断桥', 'hangzhou', 0, exits)

exits = [
	Exit('south', 'hangzhou/tianwangdian', False),
	Exit('enter', 'hangzhou/dxbaodian2', False),
]
dxbaodian1=Room('hangzhou/dxbaodian1', u'大雄宝殿', 'hangzhou', 0, exits)

exits = [
	Exit('out', 'hangzhou/dxbaodian1', False),
]
dxbaodian2=Room('hangzhou/dxbaodian2', u'大雄宝殿', 'hangzhou', 0, exits)

exits = [
	Exit('southup', 'hangzhou/shanlu2', False),
	Exit('northdown', 'hangzhou/shanlu1', False),
]
fajingsi=Room('hangzhou/fajingsi', u'法镜寺', 'hangzhou', 0, exits)

exits = [
	Exit('southup', 'hangzhou/shanlu3', False),
	Exit('northdown', 'hangzhou/shanlu2', False),
]
fajinsi=Room('hangzhou/fajinsi', u'法净寺', 'hangzhou', 0, exits)

exits = [
	Exit('southeast', 'hangzhou/pinghuqiuyue', False),
	Exit('southwest', 'hangzhou/gushan', False),
]
fangheting=Room('hangzhou/fangheting', u'放鹤亭', 'hangzhou', 0, exits)

exits = [
	Exit('eastdown', 'hangzhou/shanlu4', False),
	Exit('northdown', 'hangzhou/shanlu3', False),
]
faxisi=Room('hangzhou/faxisi', u'法喜寺', 'hangzhou', 0, exits)

exits = [
	Exit('eastup', 'hangzhou/qinglindong', False),
	Exit('north', 'hangzhou/road1', False),
	Exit('westup', 'hangzhou/longhongdong', False),
]
feilaifeng=Room('hangzhou/feilaifeng', u'飞来峰', 'hangzhou', 0, exits)

exits = [
	Exit('east', 'hangzhou/dadao1', False),
]
guozhuang=Room('hangzhou/guozhuang', u'郭庄', None, 0, exits)

exits = [
	Exit('northwest', 'hangzhou/xilingqiao', False),
	Exit('southup', 'hangzhou/gushanpingtai', False),
	Exit('northeast', 'hangzhou/fangheting', False),
	Exit('east', 'hangzhou/pinghuqiuyue', False),
	Exit('westup', 'meizhuang/shijie', False),
]
gushan=Room('hangzhou/gushan', u'孤山', 'hangzhou', 0, exits)

exits = [
	Exit('northdown', 'hangzhou/gushan', False),
]
gushanpingtai=Room('hangzhou/gushanpingtai', u'孤山平台', 'hangzhou', 0, exits)

exits = [
	Exit('southwest', 'hangzhou/road3', False),
	Exit('north', 'hangzhou/road4', False),
]
hongchunqiao=Room('hangzhou/hongchunqiao', u'洪春桥', 'hangzhou', 0, exits)

exits = [
	Exit('east', 'hangzhou/suti6', False),
]
huagang=Room('hangzhou/huagang', u'花港观鱼', 'hangzhou', 0, exits)

exits = [
	Exit('south', 'hangzhou/shanlu8', False),
]
huanglongdong=Room('hangzhou/huanglongdong', u'黄龙洞', None, 0, exits)

exits = [
	Exit('southdown', 'hangzhou/maojiabu', False),
	Exit('northdown', 'hangzhou/road3', False),
]
huangniling=Room('hangzhou/huangniling', u'黄泥岭', 'hangzhou', 0, exits)

exits = [
	Exit('east', 'hangzhou/road17', False),
]
hupaoquan=Room('hangzhou/hupaoquan', u'虎跑泉', 'hangzhou', 0, exits)

exits = [
	Exit('out', 'hangzhou/jingcisi', False),
]
jingci=Room('hangzhou/jingci', u'净慈寺', None, 0, exits)

exits = [
	Exit('north', 'hangzhou/road16', False),
	Exit('enter', 'hangzhou/jingci', False),
]
jingcisi=Room('hangzhou/jingcisi', u'净慈寺', None, 0, exits)

exits = [
	Exit('west', 'hangzhou/road10', False),
	Exit('up', 'hangzhou/loveroom', False),
]
jiulou=Room('hangzhou/jiulou', u'楼外楼', None, 0, exits)

exits = [
	Exit('northeast', 'hangzhou/liulangqiao', False),
	Exit('east', 'hangzhou/qingbomen', False),
]
jujingyuan=Room('hangzhou/jujingyuan', u'聚景园', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/road13', False),
	Exit('up', 'hangzhou/kedian2', False),
	Exit('east', 'hangzhou/majiu', False),
]
kedian=Room('hangzhou/kedian', u'天外天客店', None, 0, exits)

exits = [
	Exit('enter', 'hangzhou/kedian3', False),
	Exit('down', 'hangzhou/kedian', False),
]
kedian2=Room('hangzhou/kedian2', u'天外天客店二楼', None, 0, exits)

exits = [
	Exit('out', 'hangzhou/kedian2', False),
]
kedian3=Room('hangzhou/kedian3', u'天外天客店二楼', None, 0, exits)

exits = [
	Exit('west', 'hangzhou/road17', False),
	Exit('east', 'hangzhou/kslu2', False),
]
kslu=Room('hangzhou/kslu', u'碎石路', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/kslu', False),
	Exit('east', 'hangzhou/kuangshan', False),
]
kslu2=Room('hangzhou/kslu2', u'碎石路', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/kslu2', False),
]
kuangshan=Room('hangzhou/kuangshan', u'铜矿山', 'hangzhou', 0, exits)

exits = [
	Exit('south', 'hangzhou/road1', False),
	Exit('enter', 'hangzhou/tianwangdian', False),
]
lingyinsi=Room('hangzhou/lingyinsi', u'灵隐寺', 'hangzhou', 0, exits)

exits = [
	Exit('out', 'hangzhou/liuheta', False),
	Exit('up', 'hangzhou/liuhe2', False),
]
liuhe1=Room('hangzhou/liuhe1', u'六和塔', None, 0, exits)

exits = [
	Exit('up', 'hangzhou/liuhe3', False),
	Exit('down', 'hangzhou/liuhe1', False),
]
liuhe2=Room('hangzhou/liuhe2', u'六和塔', None, 0, exits)

exits = [
	Exit('up', 'hangzhou/liuhe4', False),
	Exit('down', 'hangzhou/liuhe2', False),
]
liuhe3=Room('hangzhou/liuhe3', u'六和塔', None, 0, exits)

exits = [
	Exit('up', 'hangzhou/liuhe5', False),
	Exit('down', 'hangzhou/liuhe3', False),
]
liuhe4=Room('hangzhou/liuhe4', u'六和塔', None, 0, exits)

exits = [
	Exit('up', 'hangzhou/liuhe6', False),
	Exit('down', 'hangzhou/liuhe4', False),
]
liuhe5=Room('hangzhou/liuhe5', u'六和塔', None, 0, exits)

exits = [
	Exit('up', 'hangzhou/liuhe7', False),
	Exit('down', 'hangzhou/liuhe5', False),
]
liuhe6=Room('hangzhou/liuhe6', u'六和塔', None, 0, exits)

exits = [
	Exit('up', 'hangzhou/liuhe8', False),
	Exit('down', 'hangzhou/liuhe6', False),
]
liuhe7=Room('hangzhou/liuhe7', u'六和塔', None, 0, exits)

exits = [
	Exit('up', 'hangzhou/liuhe9', False),
	Exit('down', 'hangzhou/liuhe7', False),
]
liuhe8=Room('hangzhou/liuhe8', u'六和塔', None, 0, exits)

exits = [
	Exit('up', 'hangzhou/liuhea', False),
	Exit('down', 'hangzhou/liuhe8', False),
]
liuhe9=Room('hangzhou/liuhe9', u'六和塔', None, 0, exits)

exits = [
	Exit('up', 'hangzhou/liuheb', False),
	Exit('down', 'hangzhou/liuhe9', False),
]
liuhea=Room('hangzhou/liuhea', u'六和塔', None, 0, exits)

exits = [
	Exit('up', 'hangzhou/liuhec', False),
	Exit('down', 'hangzhou/liuhea', False),
]
liuheb=Room('hangzhou/liuheb', u'六和塔', None, 0, exits)

exits = [
	Exit('up', 'hangzhou/liuhed', False),
	Exit('down', 'hangzhou/liuheb', False),
]
liuhec=Room('hangzhou/liuhec', u'六和塔', None, 0, exits)

exits = [
	Exit('down', 'hangzhou/liuhec', False),
]
liuhed=Room('hangzhou/liuhed', u'六和塔', None, 0, exits)

exits = [
	Exit('eastdown', 'hangzhou/qiantang', False),
	Exit('enter', 'hangzhou/liuhe1', False),
]
liuheta=Room('hangzhou/liuheta', u'六和塔底', None, 0, exits)

exits = [
	Exit('southwest', 'hangzhou/jujingyuan', False),
]
liulangqiao=Room('hangzhou/liulangqiao', u'柳浪桥', 'hangzhou', 0, exits)

exits = [
	Exit('south', 'hangzhou/liuzhuang1', False),
	Exit('north', 'hangzhou/liuzhuang2', False),
	Exit('east', 'hangzhou/dadao3', False),
]
liuzhuang=Room('hangzhou/liuzhuang', u'刘庄', None, 0, exits)

exits = [
	Exit('north', 'hangzhou/liuzhuang', False),
]
liuzhuang1=Room('hangzhou/liuzhuang1', u'刘庄侧院', None, 0, exits)

exits = [
	Exit('south', 'hangzhou/liuzhuang', False),
]
liuzhuang2=Room('hangzhou/liuzhuang2', u'刘庄侧院', None, 0, exits)

exits = [
	Exit('northwest', 'hangzhou/shexudong', False),
	Exit('eastdown', 'hangzhou/feilaifeng', False),
]
longhongdong=Room('hangzhou/longhongdong', u'龙泓洞', 'hangzhou', 0, exits)

exits = [
	Exit('south', 'hangzhou/shanlu5', False),
	Exit('east', 'hangzhou/chashi', False),
]
longjing=Room('hangzhou/longjing', u'龙井', 'hangzhou', 0, exits)

exits = [
	Exit('down', 'hangzhou/jiulou', False),
]
loveroom=Room('hangzhou/loveroom', u'相约轩', None, 0, exits)

exits = [
	Exit('west', 'hangzhou/kedian', False),
]
majiu=Room('hangzhou/majiu', u'马厩', 'hangzhou', 0, exits)

exits = [
	Exit('eastdown', 'hangzhou/shiwudong', False),
	Exit('westup', 'hangzhou/shuiledong', False),
]
manjuelong=Room('hangzhou/manjuelong', u'满觉陇', None, 0, exits)

exits = [
	Exit('northup', 'hangzhou/huangniling', False),
	Exit('southwest', 'hangzhou/tulu1', False),
]
maojiabu=Room('hangzhou/maojiabu', u'茅家埠', 'hangzhou', 0, exits)

exits = [
	Exit('east', 'hangzhou/road10', False),
]
marryroom=Room('hangzhou/marryroom', u'红娘庄', None, 0, exits)

exits = [
	Exit('west', 'hangzhou/gushan', False),
	Exit('northwest', 'hangzhou/fangheting', False),
	Exit('northeast', 'hangzhou/baiti', False),
]
pinghuqiuyue=Room('hangzhou/pinghuqiuyue', u'平湖秋月', 'hangzhou', 0, exits)

exits = [
	Exit('north', 'hangzhou/road17', False),
	Exit('westup', 'hangzhou/liuheta', False),
]
qiantang=Room('hangzhou/qiantang', u'钱塘江畔', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/jujingyuan', False),
	Exit('east', 'hangzhou/road14', False),
]
qingbomen=Room('hangzhou/qingbomen', u'清波门', 'hangzhou', 0, exits)

exits = [
	Exit('eastup', 'hangzhou/cuiweiting', False),
	Exit('westdown', 'hangzhou/feilaifeng', False),
]
qinglindong=Room('hangzhou/qinglindong', u'清林洞', 'hangzhou', 0, exits)

exits = [
	Exit('east', 'hangzhou/suti2', False),
	Exit('enter', 'hangzhou/quyuanfenghe', False),
]
quyuanbei=Room('hangzhou/quyuanbei', u'曲院风荷', 'hangzhou', 0, exits)

exits = [
	Exit('out', 'hangzhou/quyuanbei', False),
]
quyuanfenghe=Room('hangzhou/quyuanfenghe', u'曲院风荷', 'hangzhou', 0, exits)

exits = [
	Exit('northwest', 'quanzhou/jxnanmen', False),
	Exit('south', 'hangzhou/feilaifeng', False),
	Exit('north', 'hangzhou/lingyinsi', False),
	Exit('northeast', 'hangzhou/road2', False),
]
road1=Room('hangzhou/road1', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/marryroom', False),
	Exit('south', 'hangzhou/road11', False),
	Exit('east', 'hangzhou/jiulou', False),
	Exit('north', 'hangzhou/road9', False),
]
road10=Room('hangzhou/road10', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('south', 'hangzhou/road12', False),
	Exit('east', 'hangzhou/tiejiangpu', False),
	Exit('north', 'hangzhou/road10', False),
]
road11=Room('hangzhou/road11', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('south', 'hangzhou/road13', False),
	Exit('east', 'hangzhou/shuyuan', False),
	Exit('north', 'hangzhou/road11', False),
]
road12=Room('hangzhou/road12', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('southwest', 'hangzhou/road14', False),
	Exit('east', 'hangzhou/kedian', False),
	Exit('north', 'hangzhou/road12', False),
]
road13=Room('hangzhou/road13', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/qingbomen', False),
	Exit('southwest', 'hangzhou/road15', False),
	Exit('east', 'hangzhou/yaodian', False),
	Exit('northeast', 'hangzhou/road13', False),
]
road14=Room('hangzhou/road14', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/road16', False),
	Exit('southwest', 'hangzhou/yuhuangsj', False),
	Exit('northeast', 'hangzhou/road14', False),
]
road15=Room('hangzhou/road15', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/road20', False),
	Exit('south', 'hangzhou/jingcisi', False),
	Exit('northup', 'hangzhou/xizhaoshan', False),
	Exit('east', 'hangzhou/road15', False),
]
road16=Room('hangzhou/road16', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/hupaoquan', False),
	Exit('south', 'hangzhou/qiantang', False),
	Exit('east', 'hangzhou/kslu', False),
	Exit('north', 'hangzhou/road18', False),
]
road17=Room('hangzhou/road17', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/shiwudong', False),
	Exit('south', 'hangzhou/road17', False),
	Exit('east', 'hangzhou/yuhuangshan', False),
	Exit('northeast', 'hangzhou/road19', False),
]
road18=Room('hangzhou/road18', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('southwest', 'hangzhou/road18', False),
	Exit('east', 'hangzhou/road20', False),
	Exit('north', 'hangzhou/dadao3', False),
]
road19=Room('hangzhou/road19', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('southup', 'hangzhou/shanlu1', False),
	Exit('southwest', 'hangzhou/road1', False),
	Exit('northeast', 'hangzhou/road3', False),
]
road2=Room('hangzhou/road2', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/road19', False),
	Exit('east', 'hangzhou/road16', False),
	Exit('north', 'hangzhou/suti7', False),
]
road20=Room('hangzhou/road20', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('southup', 'hangzhou/huangniling', False),
	Exit('southwest', 'hangzhou/road2', False),
	Exit('northeast', 'hangzhou/hongchunqiao', False),
]
road3=Room('hangzhou/road3', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('south', 'hangzhou/hongchunqiao', False),
	Exit('northeast', 'hangzhou/road5', False),
]
road4=Room('hangzhou/road4', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('south', 'hangzhou/dadao1', False),
	Exit('southwest', 'hangzhou/road4', False),
	Exit('east', 'hangzhou/road6', False),
	Exit('westup', 'hangzhou/yuquan', False),
]
road5=Room('hangzhou/road5', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/road5', False),
	Exit('south', 'hangzhou/suti1', False),
	Exit('east', 'hangzhou/road7', False),
	Exit('north', 'hangzhou/yuelang', False),
]
road6=Room('hangzhou/road6', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/road6', False),
	Exit('south', 'hangzhou/xilingqiao', False),
	Exit('north', 'hangzhou/shanlu8', False),
	Exit('northeast', 'hangzhou/road8', False),
]
road7=Room('hangzhou/road7', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('northup', 'hangzhou/baoshishan', False),
	Exit('southwest', 'hangzhou/road7', False),
	Exit('east', 'hangzhou/road9', False),
]
road8=Room('hangzhou/road8', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/road8', False),
	Exit('south', 'hangzhou/road10', False),
	Exit('southwest', 'hangzhou/duanqiao', False),
]
road9=Room('hangzhou/road9', u'青石大道', 'hangzhou', 0, exits)

exits = [
	Exit('southup', 'hangzhou/fajingsi', False),
	Exit('northdown', 'hangzhou/road2', False),
]
shanlu1=Room('hangzhou/shanlu1', u'山路', 'hangzhou', 0, exits)

exits = [
	Exit('southup', 'hangzhou/fajinsi', False),
	Exit('northdown', 'hangzhou/fajingsi', False),
]
shanlu2=Room('hangzhou/shanlu2', u'山路', 'hangzhou', 0, exits)

exits = [
	Exit('southup', 'hangzhou/faxisi', False),
	Exit('northdown', 'hangzhou/fajinsi', False),
]
shanlu3=Room('hangzhou/shanlu3', u'山路', 'hangzhou', 0, exits)

exits = [
	Exit('eastdown', 'hangzhou/shanlu5', False),
	Exit('westup', 'hangzhou/faxisi', False),
]
shanlu4=Room('hangzhou/shanlu4', u'山路', 'hangzhou', 0, exits)

exits = [
	Exit('east', 'hangzhou/yanxiadong', False),
	Exit('north', 'hangzhou/longjing', False),
	Exit('northeast', 'hangzhou/tulu1', False),
	Exit('westup', 'hangzhou/shanlu4', False),
]
shanlu5=Room('hangzhou/shanlu5', u'山路', 'hangzhou', 0, exits)

exits = [
	Exit('eastup', 'hangzhou/yuhuangsd', False),
	Exit('westdown', 'hangzhou/yuhuangshan', False),
]
shanlu6=Room('hangzhou/shanlu6', u'山路', 'hangzhou', 0, exits)

exits = [
	Exit('eastdown', 'hangzhou/yuhuangsj', False),
	Exit('westup', 'hangzhou/yuhuangsd', False),
]
shanlu7=Room('hangzhou/shanlu7', u'山路', 'hangzhou', 0, exits)

exits = [
	Exit('south', 'hangzhou/road7', False),
	Exit('north', 'hangzhou/huanglongdong', False),
]
shanlu8=Room('hangzhou/shanlu8', u'山路', 'hangzhou', 0, exits)

exits = [
	Exit('southeast', 'hangzhou/longhongdong', False),
]
shexudong=Room('hangzhou/shexudong', u'射旭洞', 'hangzhou', 0, exits)

exits = [
	Exit('east', 'hangzhou/road18', False),
	Exit('westup', 'hangzhou/manjuelong', False),
]
shiwudong=Room('hangzhou/shiwudong', u'石屋洞', None, 0, exits)

exits = [
	Exit('eastdown', 'hangzhou/manjuelong', False),
	Exit('westup', 'hangzhou/yanxiadong', False),
]
shuiledong=Room('hangzhou/shuiledong', u'水乐洞', None, 0, exits)

exits = [
	Exit('west', 'hangzhou/road12', False),
]
shuyuan=Room('hangzhou/shuyuan', u'凤池书院', None, 0, exits)

exits = [
	Exit('south', 'hangzhou/suti2', False),
	Exit('north', 'hangzhou/road6', False),
]
suti1=Room('hangzhou/suti1', u'苏堤', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/quyuanbei', False),
	Exit('south', 'hangzhou/suti3', False),
	Exit('north', 'hangzhou/suti1', False),
]
suti2=Room('hangzhou/suti2', u'苏堤', 'hangzhou', 0, exits)

exits = [
	Exit('south', 'hangzhou/suti4', False),
	Exit('north', 'hangzhou/suti2', False),
]
suti3=Room('hangzhou/suti3', u'苏堤', 'hangzhou', 0, exits)

exits = [
	Exit('south', 'hangzhou/suti5', False),
	Exit('north', 'hangzhou/suti3', False),
]
suti4=Room('hangzhou/suti4', u'苏堤', 'hangzhou', 0, exits)

exits = [
	Exit('south', 'hangzhou/suti6', False),
	Exit('north', 'hangzhou/suti4', False),
]
suti5=Room('hangzhou/suti5', u'苏堤', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/huagang', False),
	Exit('south', 'hangzhou/suti7', False),
	Exit('north', 'hangzhou/suti5', False),
]
suti6=Room('hangzhou/suti6', u'苏堤', 'hangzhou', 0, exits)

exits = [
	Exit('south', 'hangzhou/road20', False),
	Exit('north', 'hangzhou/suti6', False),
]
suti7=Room('hangzhou/suti7', u'苏堤', 'hangzhou', 0, exits)

exits = [
	Exit('out', 'hangzhou/lingyinsi', False),
	Exit('north', 'hangzhou/dxbaodian1', False),
]
tianwangdian=Room('hangzhou/tianwangdian', u'天王殿', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/road11', False),
]
tiejiangpu=Room('hangzhou/tiejiangpu', u'铁匠铺', None, 0, exits)

exits = [
	Exit('southwest', 'hangzhou/shanlu5', False),
	Exit('northeast', 'hangzhou/maojiabu', False),
]
tulu1=Room('hangzhou/tulu1', u'土路', 'hangzhou', 0, exits)

exits = [
	Exit('southeast', 'hangzhou/gushan', False),
	Exit('north', 'hangzhou/road7', False),
]
xilingqiao=Room('hangzhou/xilingqiao', u'西泠桥', 'hangzhou', 0, exits)

exits = [
	Exit('southdown', 'hangzhou/road16', False),
]
xizhaoshan=Room('hangzhou/xizhaoshan', u'夕照山', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/shanlu5', False),
	Exit('eastdown', 'hangzhou/shuiledong', False),
]
yanxiadong=Room('hangzhou/yanxiadong', u'烟霞洞', None, 0, exits)

exits = [
	Exit('west', 'hangzhou/road14', False),
]
yaodian=Room('hangzhou/yaodian', u'胡庆余堂', None, 1, exits)

exits = [
	Exit('south', 'hangzhou/yuelang', False),
]
yuefen=Room('hangzhou/yuefen', u'岳坟', 'hangzhou', 0, exits)

exits = [
	Exit('south', 'hangzhou/road6', False),
	Exit('north', 'hangzhou/yuefen', False),
]
yuelang=Room('hangzhou/yuelang', u'岳廊', None, 0, exits)

exits = [
	Exit('eastdown', 'hangzhou/shanlu7', False),
	Exit('westdown', 'hangzhou/shanlu6', False),
]
yuhuangsd=Room('hangzhou/yuhuangsd', u'玉皇山顶', 'hangzhou', 0, exits)

exits = [
	Exit('west', 'hangzhou/road18', False),
	Exit('eastup', 'hangzhou/shanlu6', False),
]
yuhuangshan=Room('hangzhou/yuhuangshan', u'玉皇山', 'hangzhou', 0, exits)

exits = [
	Exit('northeast', 'hangzhou/road15', False),
	Exit('westup', 'hangzhou/shanlu7', False),
]
yuhuangsj=Room('hangzhou/yuhuangsj', u'玉皇山脚', 'hangzhou', 0, exits)

exits = [
	Exit('eastdown', 'hangzhou/road5', False),
]
yuquan=Room('hangzhou/yuquan', u'玉泉', 'hangzhou', 0, exits)

