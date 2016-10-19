# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('west', 'city/qianzhuang', False),
	Exit('south', 'city/guangchang', False),
	Exit('north', 'city/beidajie2', False),
	Exit('east', 'city/kedian', False),
]
beidajie1=Room('city/beidajie1', u'北大街', 'city', 0, exits)

exits = [
	Exit('west', 'city/wumiao', False),
	Exit('south', 'city/beidajie1', False),
	Exit('north', 'city/beimen', False),
	Exit('east', 'city/zuixianlou', False),
]
beidajie2=Room('city/beidajie2', u'北大街', 'city', 0, exits)

exits = [
	Exit('west', 'huanghe/caodi1', False),
	Exit('south', 'city/beidajie2', False),
	Exit('east', 'city/postofficer', False),
	Exit('north', 'shaolin/yidao', False),
]
beimen=Room('city/beimen', u'北门', 'city', 0, exits)

exits = [
	Exit('north', 'city/bingyin', True),
]
bingqiku=Room('city/bingqiku', u'兵器库', None, 0, exits)

exits = [
	Exit('south', 'city/bingqiku', True),
	Exit('north', 'city/bingyindamen', False),
]
bingyin=Room('city/bingyin', u'兵营', None, 0, exits)

exits = [
	Exit('south', 'city/bingyin', False),
	Exit('north', 'city/xidajie1', False),
]
bingyindamen=Room('city/bingyindamen', u'兵营大门', None, 0, exits)

exits = [
	Exit('up', 'city/chaguan', False),
]
bocai=Room('city/bocai', u'地下博彩屋', None, 0, exits)

exits = [
	Exit('south', 'city/xidajie2', False),
	Exit('north', 'city/dayuan', False),
]
caizhu=Room('city/caizhu', u'财主大门', None, 0, exits)

exits = [
]
cangku=Room('city/cangku', u'仓库', None, 0, exits)

exits = [
	Exit('east', 'city/nandajie2', False),
	Exit('down', 'city/bocai', False),
]
chaguan=Room('city/chaguan', u'春来茶馆', None, 0, exits)

exits = [
	Exit('east', 'city/road1', False),
]
damo=Room('city/damo', u'大漠', None, 0, exits)

exits = [
	Exit('west', 'city/nandajie1', False),
	Exit('down', 'city/xsmidao', False),
]
dangpu=Room('city/dangpu', u'当铺', None, 0, exits)

exits = [
	Exit('north', 'city/dongdajie2', False),
]
datiepu=Room('city/datiepu', u'打铁铺', None, 0, exits)

exits = [
	Exit('east', 'city/duchang', False),
]
daxiao=Room('city/daxiao', u'赌场', None, 1, exits)

exits = [
	Exit('south', 'city/caizhu', False),
	Exit('north', 'city/houyuan', False),
]
dayuan=Room('city/dayuan', u'财主大院', None, 0, exits)

exits = [
	Exit('west', 'city/guangchang', False),
	Exit('south', 'city/zahuopu', False),
	Exit('north', 'city/shuyuan', False),
	Exit('east', 'city/dongdajie2', False),
]
dongdajie1=Room('city/dongdajie1', u'东大街', 'city', 0, exits)

exits = [
	Exit('west', 'city/dongdajie1', False),
	Exit('south', 'city/datiepu', False),
	Exit('north', 'city/yaopu', False),
	Exit('east', 'city/dongmen', False),
]
dongdajie2=Room('city/dongdajie2', u'东大街', 'city', 0, exits)

exits = [
	Exit('west', 'city/dongdajie2', False),
	Exit('south', 'city/jiaowai1', False),
	Exit('north', 'city/ml1', False),
	Exit('east', 'taishan/yidao', False),
]
dongmen=Room('city/dongmen', u'东门', 'city', 0, exits)

exits = [
	Exit('west', 'city/ymzhengting', False),
]
dongting=Room('city/dongting', u'东厅', None, 0, exits)

exits = [
	Exit('west', 'city/houyuan', False),
]
dongxiang=Room('city/dongxiang', u'财主东厢', None, 0, exits)

exits = [
	Exit('west', 'city/daxiao', False),
	Exit('east', 'city/nandajie1', False),
	Exit('up', 'city/duchang2', False),
]
duchang=Room('city/duchang', u'赌场', None, 0, exits)

exits = [
	Exit('west', 'city/wproom', False),
	Exit('south', 'city/sproom', False),
	Exit('north', 'city/nproom', False),
	Exit('east', 'city/eproom', False),
	Exit('down', 'city/duchang', False),
]
duchang2=Room('city/duchang2', u'赌场', None, 0, exits)

exits = [
]
duchuan=Room('city/duchuan', u'渡船', None, 0, exits)

exits = [
	Exit('west', 'city/duchang2', False),
]
eproom=Room('city/eproom', u'拱猪房', None, 1, exits)

exits = [
	Exit('south', 'city/zxlpath', False),
]
furong=Room('city/furong', u'芙蓉宴厅', None, 0, exits)

exits = [
	Exit('up', 'city/garments2', False),
	Exit('down', 'city/zahuopu', False),
]
garments=Room('city/garments', u'成衣店', None, 0, exits)

exits = [
	Exit('down', 'city/garments', False),
]
garments2=Room('city/garments2', u'成衣店阁楼', None, 0, exits)

exits = [
	Exit('out', 'city/pomiao', True),
	Exit('east', 'city/gbxiaowu', False),
]
gbandao=Room('city/gbandao', u'暗道', None, 0, exits)

exits = [
	Exit('out', 'city/ml7', False),
	Exit('west', 'city/gbandao', False),
	Exit('east', 'gaibang/undertre', False),
]
gbxiaowu=Room('city/gbxiaowu', u'林间小屋', None, 0, exits)

exits = [
	Exit('west', 'city/xidajie1', False),
	Exit('south', 'city/nandajie1', False),
	Exit('up', 'city/shiji', False),
	Exit('north', 'city/beidajie1', False),
	Exit('east', 'city/dongdajie1', False),
]
guangchang=Room('city/guangchang', u'泥潭广场', 'city', 0, exits)

exits = [
	Exit('west', 'city/level_up', False),
]
guest=Room('city/guest', u'东客房', None, 0, exits)

exits = [
	Exit('west', 'city/xixiang', False),
	Exit('south', 'city/dayuan', False),
]
houyuan=Room('city/houyuan', u'财主后院', None, 0, exits)

exits = [
	Exit('east', 'city/xiaohuayuan', False),
]
huafang=Room('city/huafang', u'花房', None, 0, exits)

exits = [
	Exit('south', 'city/jiaowai2', False),
	Exit('north', 'city/dongmen', False),
]
jiaowai1=Room('city/jiaowai1', u'草地', 'city', 0, exits)

exits = [
	Exit('west', 'city/jiaowai11', False),
	Exit('north', 'city/jiaowai12', False),
	Exit('east', 'city/jiaowai9', False),
]
jiaowai10=Room('city/jiaowai10', u'密林', None, 0, exits)

exits = [
	Exit('north', 'city/jiaowai13', False),
	Exit('east', 'city/jiaowai10', False),
]
jiaowai11=Room('city/jiaowai11', u'密林', None, 0, exits)

exits = [
	Exit('west', 'city/jiaowai13', False),
	Exit('south', 'city/jiaowai10', False),
]
jiaowai12=Room('city/jiaowai12', u'密林', None, 0, exits)

exits = [
	Exit('south', 'city/jiaowai11', False),
	Exit('east', 'city/jiaowai12', False),
]
jiaowai13=Room('city/jiaowai13', u'密林', None, 0, exits)

exits = [
	Exit('south', 'city/jiaowai3', False),
	Exit('north', 'city/jiaowai1', False),
]
jiaowai2=Room('city/jiaowai2', u'树林', 'yangzhou', 0, exits)

exits = [
	Exit('south', 'city/jiaowai4', False),
	Exit('north', 'city/jiaowai2', False),
]
jiaowai3=Room('city/jiaowai3', u'树林', 'yangzhou', 0, exits)

exits = [
	Exit('southeast', 'guiyun/shulin1', False),
	Exit('west', 'city/jiaowai5', False),
	Exit('north', 'city/jiaowai3', False),
]
jiaowai4=Room('city/jiaowai4', u'密林', None, 0, exits)

exits = [
	Exit('west', 'city/jiaowai6', False),
	Exit('east', 'city/jiaowai4', False),
]
jiaowai5=Room('city/jiaowai5', u'密林', None, 0, exits)

exits = [
	Exit('west', 'city/jiaowai7', False),
	Exit('east', 'city/jiaowai5', False),
]
jiaowai6=Room('city/jiaowai6', u'树林', 'yangzhou', 0, exits)

exits = [
	Exit('west', 'city/nanmen', False),
	Exit('east', 'city/jiaowai6', False),
]
jiaowai7=Room('city/jiaowai7', u'草地', 'city', 0, exits)

exits = [
	Exit('west', 'city/jiaowai9', False),
	Exit('east', 'city/nanmen', False),
]
jiaowai8=Room('city/jiaowai8', u'草地', 'yangzhou', 0, exits)

exits = [
	Exit('west', 'city/jiaowai10', False),
	Exit('east', 'city/jiaowai8', False),
]
jiaowai9=Room('city/jiaowai9', u'密林', None, 0, exits)

exits = [
	Exit('west', 'city/beidajie1', False),
	Exit('south', 'city/liaotian', False),
	Exit('up', 'city/kedian2', False),
]
kedian=Room('city/kedian', u'宝昌客栈', None, 0, exits)

exits = [
	Exit('enter', 'city/kedian3', False),
	Exit('down', 'city/kedian', False),
]
kedian2=Room('city/kedian2', u'客店二楼', None, 0, exits)

exits = [
	Exit('out', 'city/kedian2', False),
]
kedian3=Room('city/kedian3', u'客房', None, 0, exits)

exits = [
	Exit('southdown', 'city/wudao3', False),
	Exit('eastdown', 'city/wudao1', False),
	Exit('northdown', 'city/wudao4', False),
	Exit('westdown', 'city/wudao2', False),
]
leitai=Room('city/leitai', u'擂台', 'city', 0, exits)

exits = [
	Exit('east', 'city/guest', False),
	Exit('down', 'city/shiji', False),
]
level_up=Room('city/level_up', u'树屋', None, 0, exits)

exits = [
	Exit('out', 'city/xiaohuayuan', False),
	Exit('north', 'city/kedian', False),
]
liaotian=Room('city/liaotian', u'客店茶房', None, 0, exits)

exits = [
	Exit('south', 'city/lichunyuan', False),
]
library=Room('city/library', u'图书馆', None, 0, exits)

exits = [
	Exit('west', 'city/nandajie2', False),
	Exit('up', 'city/lichunyuan2', False),
]
lichunyuan=Room('city/lichunyuan', u'丽春院', None, 0, exits)

exits = [
	Exit('down', 'city/lichunyuan', False),
]
lichunyuan2=Room('city/lichunyuan2', u'丽春院二楼', None, 1, exits)

exits = [
	Exit('west', 'city/zuixianlou', False),
	Exit('east', 'city/menpai_jieyin', False),
]
majiu=Room('city/majiu', u'马厩', 'city', 0, exits)

exits = [
	Exit('west', 'city/zxlpath', False),
]
meigui=Room('city/meigui', u'玫瑰宴厅', None, 0, exits)

exits = [
	Exit('west', 'city/majiu', False),
]
menpai_jieyin=Room('city/menpai_jieyin', u'门派办事处', None, 0, exits)

exits = [
	Exit('south', 'city/dongmen', False),
	Exit('east', 'city/ml2', False),
]
ml1=Room('city/ml1', u'青竹林', 'city', 0, exits)

exits = [
	Exit('south', 'city/dongmen', False),
	Exit('north', 'city/ml3', False),
]
ml2=Room('city/ml2', u'青竹林', 'city', 0, exits)

exits = [
	Exit('west', 'city/ml4', False),
	Exit('south', 'city/dongmen', False),
]
ml3=Room('city/ml3', u'青竹林', 'city', 0, exits)

exits = [
	Exit('south', 'city/dongmen', False),
	Exit('north', 'city/ml5', False),
]
ml4=Room('city/ml4', u'青竹林', 'city', 0, exits)

exits = [
	Exit('south', 'city/dongmen', False),
	Exit('east', 'city/ml6', False),
]
ml5=Room('city/ml5', u'青竹林', 'city', 0, exits)

exits = [
	Exit('west', 'city/ml7', False),
	Exit('south', 'city/dongmen', False),
]
ml6=Room('city/ml6', u'青竹林', 'city', 0, exits)

exits = [
	Exit('south', 'city/dongmen', False),
	Exit('north', 'city/pomiao', False),
	Exit('enter', 'city/gbxiaowu', False),
]
ml7=Room('city/ml7', u'青竹林', 'city', 0, exits)

exits = [
	Exit('north', 'city/zxlpath', False),
]
mudan=Room('city/mudan', u'牡丹宴厅', None, 0, exits)

exits = [
	Exit('west', 'city/duchang', False),
	Exit('south', 'city/nandajie2', False),
	Exit('north', 'city/guangchang', False),
	Exit('east', 'city/dangpu', False),
]
nandajie1=Room('city/nandajie1', u'南大街', 'city', 0, exits)

exits = [
	Exit('west', 'city/chaguan', False),
	Exit('south', 'city/nanmen', False),
	Exit('north', 'city/nandajie1', False),
	Exit('east', 'city/lichunyuan', False),
]
nandajie2=Room('city/nandajie2', u'南大街', 'city', 0, exits)

exits = [
	Exit('west', 'city/jiaowai8', False),
	Exit('south', 'wudang/wdroad1', False),
	Exit('east', 'city/jiaowai7', False),
	Exit('north', 'city/nandajie2', False),
]
nanmen=Room('city/nanmen', u'南门', 'city', 0, exits)

exits = [
	Exit('south', 'city/ymzhengting', False),
]
neizhai=Room('city/neizhai', u'内宅', None, 0, exits)

exits = [
	Exit('south', 'city/duchang2', False),
]
nproom=Room('city/nproom', u'拱猪房', None, 1, exits)

exits = [
	Exit('west', 'gaibang/shoushe', False),
	Exit('south', 'city/ml4', False),
	Exit('east', 'gaibang/sheyuan', False),
	Exit('enter', 'city/gbandao', True),
]
pomiao=Room('city/pomiao', u'土地庙', None, 0, exits)

exits = [
	Exit('west', 'city/beimen', False),
]
postofficer=Room('city/postofficer', u'扬州驿站', None, 0, exits)

exits = [
	Exit('east', 'city/beidajie1', False),
]
qianzhuang=Room('city/qianzhuang', u'钱庄', None, 0, exits)

exits = [
	Exit('west', 'city/road10', False),
]
quanzhou=Room('city/quanzhou', u'泉州港口', None, 0, exits)

exits = [
	Exit('west', 'city/road7', False),
]
shenlong=Room('city/shenlong', u'神龙教', None, 0, exits)

exits = [
	Exit('up', 'city/level_up', False),
	Exit('down', 'city/guangchang', False),
]
shiji=Room('city/shiji', u'市集', None, 0, exits)

exits = [
	Exit('south', 'city/dongdajie1', False),
	Exit('up', 'city/shuyuan2', False),
]
shuyuan=Room('city/shuyuan', u'书院', None, 0, exits)

exits = [
	Exit('down', 'city/shuyuan', False),
]
shuyuan2=Room('city/shuyuan2', u'书院书库', None, 0, exits)

exits = [
	Exit('north', 'city/duchang2', False),
]
sproom=Room('city/sproom', u'拱猪房', None, 1, exits)

exits = [
	Exit('east', 'city/road2', False),
]
tianshan=Room('city/tianshan', u'天山', None, 0, exits)

exits = [
]
underlt=Room('city/underlt', u'', None, 0, exits)

exits = [
	Exit('east', 'city/duchang2', False),
]
wproom=Room('city/wproom', u'拱猪房', None, 1, exits)

exits = [
	Exit('northwest', 'city/wudao4', False),
	Exit('southwest', 'city/wudao3', False),
	Exit('leitai', 'city/leitai', False),
]
wudao1=Room('city/wudao1', u'武道场', 'city', 0, exits)

exits = [
	Exit('southeast', 'city/wudao3', False),
	Exit('leitai', 'city/leitai', False),
	Exit('northeast', 'city/wudao4', False),
]
wudao2=Room('city/wudao2', u'武道场', 'city', 0, exits)

exits = [
	Exit('northwest', 'city/wudao2', False),
	Exit('leitai', 'city/leitai', False),
	Exit('northeast', 'city/wudao1', False),
]
wudao3=Room('city/wudao3', u'武道场', 'city', 0, exits)

exits = [
	Exit('southeast', 'city/wudao1', False),
	Exit('southwest', 'city/wudao2', False),
	Exit('leitai', 'city/leitai', False),
	Exit('north', 'city/ximenroad', False),
]
wudao4=Room('city/wudao4', u'武道场', 'city', 0, exits)

exits = [
	Exit('north', 'city/xidajie2', False),
]
wuguan=Room('city/wuguan', u'扬州武馆', None, 0, exits)

exits = [
	Exit('northwest', 'wizard/guest_room', True),
	Exit('up', 'city/wumiao2', False),
	Exit('east', 'city/beidajie2', False),
]
wumiao=Room('city/wumiao', u'武庙', None, 1, exits)

exits = [
	Exit('down', 'city/wumiao', False),
]
wumiao2=Room('city/wumiao2', u'武庙二楼', None, 0, exits)

exits = [
	Exit('west', 'city/huafang', False),
	Exit('enter', 'city/liaotian', False),
]
xiaohuayuan=Room('city/xiaohuayuan', u'小花园', None, 0, exits)

exits = [
	Exit('west', 'city/xidajie2', False),
	Exit('south', 'city/bingyindamen', False),
	Exit('north', 'city/yamen', False),
	Exit('east', 'city/guangchang', False),
]
xidajie1=Room('city/xidajie1', u'西大街', 'city', 0, exits)

exits = [
	Exit('west', 'city/ximen', False),
	Exit('south', 'city/wuguan', False),
	Exit('north', 'city/caizhu', False),
	Exit('east', 'city/xidajie1', False),
]
xidajie2=Room('city/xidajie2', u'西大街', 'city', 0, exits)

exits = [
	Exit('west', 'city/ximenroad', False),
	Exit('east', 'city/xidajie2', False),
]
ximen=Room('city/ximen', u'西门', 'city', 0, exits)

exits = [
	Exit('west', 'changan/road1', False),
	Exit('south', 'city/wudao4', False),
	Exit('east', 'city/ximen', False),
]
ximenroad=Room('city/ximenroad', u'西门大道', 'city', 0, exits)

exits = [
	Exit('east', 'city/ymzhengting', False),
]
xiting=Room('city/xiting', u'西厅', None, 0, exits)

exits = [
	Exit('east', 'city/houyuan', False),
]
xixiang=Room('city/xixiang', u'财主西厢', None, 0, exits)

exits = [
	Exit('west', 'city/xsmidao1', False),
	Exit('up', 'city/dangpu', False),
]
xsmidao=Room('city/xsmidao', u'雪山寺密道', None, 0, exits)

exits = [
	Exit('west', 'city/xsmidao2', False),
	Exit('east', 'city/xsmidao', False),
]
xsmidao1=Room('city/xsmidao1', u'雪山寺密道', None, 0, exits)

exits = [
	Exit('northwest', 'city/xsmidao3', False),
	Exit('east', 'city/xsmidao1', False),
]
xsmidao2=Room('city/xsmidao2', u'雪山寺密道', None, 0, exits)

exits = [
	Exit('southeast', 'city/xsmidao2', False),
	Exit('northwest', 'city/xsmidao4', False),
]
xsmidao3=Room('city/xsmidao3', u'雪山寺密道', None, 0, exits)

exits = [
	Exit('west', 'city/xsmidao5', False),
	Exit('southeast', 'city/xsmidao3', False),
]
xsmidao4=Room('city/xsmidao4', u'雪山寺密道', None, 0, exits)

exits = [
	Exit('up', 'xueshan/mishi', False),
	Exit('east', 'city/xsmidao4', False),
]
xsmidao5=Room('city/xsmidao5', u'雪山寺密道', None, 0, exits)

exits = [
	Exit('south', 'city/xidajie1', False),
	Exit('north', 'city/ymzhengting', False),
]
yamen=Room('city/yamen', u'衙门大门', None, 0, exits)

exits = [
	Exit('south', 'city/dongdajie2', False),
	Exit('north', 'city/yaopu_neishi', False),
]
yaopu=Room('city/yaopu', u'药铺', None, 0, exits)

exits = [
	Exit('west', 'city/yaopu_neishi2', False),
	Exit('south', 'city/yaopu', False),
	Exit('north', 'city/yaopu_neishi3', False),
	Exit('east', 'city/yaopu_neishi1', False),
]
yaopu_neishi=Room('city/yaopu_neishi', u'中央药材室', None, 0, exits)

exits = [
	Exit('west', 'city/yaopu_neishi', False),
]
yaopu_neishi1=Room('city/yaopu_neishi1', u'东药室', None, 0, exits)

exits = [
	Exit('east', 'city/yaopu_neishi', False),
]
yaopu_neishi2=Room('city/yaopu_neishi2', u'西药室', None, 0, exits)

exits = [
	Exit('south', 'city/yaopu_neishi', False),
]
yaopu_neishi3=Room('city/yaopu_neishi3', u'北药室', None, 0, exits)

exits = [
	Exit('west', 'city/xiting', False),
	Exit('south', 'city/yamen', False),
	Exit('north', 'city/neizhai', False),
	Exit('east', 'city/dongting', False),
]
ymzhengting=Room('city/ymzhengting', u'衙门正厅', None, 0, exits)

exits = [
	Exit('north', 'city/zahuopu', False),
]
zahuo_neishi=Room('city/zahuo_neishi', u'杂货铺内室', None, 0, exits)

exits = [
	Exit('south', 'city/zahuo_neishi', False),
	Exit('up', 'city/garments', False),
	Exit('north', 'city/dongdajie1', False),
]
zahuopu=Room('city/zahuopu', u'杂货铺', None, 0, exits)

exits = [
	Exit('up', 'city/kedian', False),
]
zhujuan=Room('city/zhujuan', u'猪圈', None, 0, exits)

exits = [
	Exit('west', 'city/beidajie2', False),
	Exit('east', 'city/majiu', False),
	Exit('up', 'city/zuixianlou2', False),
]
zuixianlou=Room('city/zuixianlou', u'醉仙楼', None, 0, exits)

exits = [
	Exit('east', 'city/zxlpath', False),
	Exit('down', 'city/zuixianlou', False),
]
zuixianlou2=Room('city/zuixianlou2', u'醉仙楼二楼', None, 0, exits)

exits = [
	Exit('down', 'city/zuixianlou2', False),
]
zuixianlou3=Room('city/zuixianlou3', u'醉仙楼三楼', None, 0, exits)

exits = [
	Exit('west', 'city/zuixianlou2', False),
	Exit('south', 'city/mudan', False),
	Exit('north', 'city/furong', False),
	Exit('east', 'city/meigui', False),
]
zxlpath=Room('city/zxlpath', u'醉仙楼大堂', None, 1, exits)

