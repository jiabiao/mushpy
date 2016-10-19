# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('west', 'changan/fufeng1', False),
	Exit('east', 'changan/baihu2', False),
]
baihu1=Room('changan/baihu1', u'白虎街', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/baihu1', False),
	Exit('south', 'changan/bridge1', False),
	Exit('east', 'changan/baihu3', False),
	Exit('north', 'changan/beian_dadao', False),
]
baihu2=Room('changan/baihu2', u'白虎街', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/baihu2', False),
	Exit('east', 'changan/fengxu1', False),
	Exit('north', 'changan/guozijian', False),
]
baihu3=Room('changan/baihu3', u'白虎街', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/qixiang4', False),
]
bank=Room('changan/bank', u'四海钱庄', None, 0, exits)

exits = [
	Exit('west', 'changan/piandian', False),
	Exit('east', 'changan/fangzhangshi', False),
	Exit('north', 'changan/baoxiangsi', False),
]
baodian=Room('changan/baodian', u'大雄宝殿', None, 0, exits)

exits = [
	Exit('south', 'changan/baodian', False),
	Exit('north', 'changan/qinglong1', False),
]
baoxiangsi=Room('changan/baoxiangsi', u'宝象寺', None, 0, exits)

exits = [
	Exit('north', 'changan/yongtai_nankou', False),
]
baozipu=Room('changan/baozipu', u'包子铺', None, 0, exits)

exits = [
	Exit('out', 'changan/kzsleep', False),
]
bed=Room('changan/bed', u'床上', None, 0, exits)

exits = [
	Exit('south', 'changan/beian_daokou', False),
	Exit('north', 'changan/tulu1', False),
]
bei_chengmen=Room('changan/bei_chengmen', u'长安北城门', '1', 0, exits)

exits = [
	Exit('south', 'changan/baihu2', False),
	Exit('north', 'changan/beian_daokou', False),
]
beian_dadao=Room('changan/beian_dadao', u'北安大道', 'changan', 0, exits)

exits = [
	Exit('southeast', 'changan/bingying1', False),
	Exit('west', 'changan/qixiang3', False),
	Exit('south', 'changan/beian_dadao', False),
	Exit('southwest', 'changan/bingying2', False),
	Exit('east', 'changan/qixiang4', False),
	Exit('north', 'changan/bei_chengmen', False),
]
beian_daokou=Room('changan/beian_daokou', u'北安道口', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/biaoju_dayuan', False),
	Exit('north', 'changan/qixiang5', False),
]
biaoju_damen=Room('changan/biaoju_damen', u'河洛镖局', None, 0, exits)

exits = [
	Exit('north', 'changan/biaoju_dayuan', False),
]
biaoju_dating=Room('changan/biaoju_dating', u'河洛镖局大厅', None, 0, exits)

exits = [
	Exit('south', 'changan/biaoju_dating', False),
	Exit('north', 'changan/biaoju_damen', False),
]
biaoju_dayuan=Room('changan/biaoju_dayuan', u'河洛镖局大院', 'changan', 0, exits)

exits = [
	Exit('northwest', 'changan/beian_daokou', False),
]
bingying1=Room('changan/bingying1', u'兵营', 'changan', 0, exits)

exits = [
	Exit('northeast', 'changan/beian_daokou', False),
]
bingying2=Room('changan/bingying2', u'兵营', 'changan', 0, exits)

exits = [
	Exit('northwest', 'changan/xian_daokou', False),
]
bingying3=Room('changan/bingying3', u'兵营', 'changan', 0, exits)

exits = [
	Exit('southwest', 'changan/nanan_daokou', False),
]
bingying4=Room('changan/bingying4', u'兵营', 'changan', 0, exits)

exits = [
	Exit('southeast', 'changan/nanan_daokou', False),
]
bingying5=Room('changan/bingying5', u'兵营', 'changan', 0, exits)

exits = [
	Exit('northeast', 'changan/dongan_daokou', False),
]
bingying6=Room('changan/bingying6', u'兵营', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/huanggong', False),
	Exit('north', 'changan/baihu2', False),
]
bridge1=Room('changan/bridge1', u'金水桥', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/qinglong2', False),
	Exit('north', 'changan/huanggong', False),
]
bridge2=Room('changan/bridge2', u'金水桥', 'changan', 0, exits)

exits = [
	Exit('north', 'changan/qixiang3', False),
]
dangpu=Room('changan/dangpu', u'萧记当铺', None, 0, exits)

exits = [
	Exit('west', 'changan/dongan_daokou', False),
	Exit('east', 'changan/road4', False),
]
dong_chengmen=Room('changan/dong_chengmen', u'长安东城门', '1', 0, exits)

exits = [
	Exit('west', 'changan/fengxu3', False),
	Exit('east', 'changan/dongan_daokou', False),
]
dongan_dadao=Room('changan/dongan_dadao', u'东安大道', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/dongan_dadao', False),
	Exit('south', 'changan/liande_dadao4', False),
	Exit('southwest', 'changan/bingying6', False),
	Exit('east', 'changan/dong_chengmen', False),
	Exit('north', 'changan/liande_dadao3', False),
]
dongan_daokou=Room('changan/dongan_daokou', u'东安道口', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/qixiang3', False),
]
duchang=Room('changan/duchang', u'赌场', None, 0, exits)

exits = [
	Exit('west', 'changan/baodian', False),
]
fangzhangshi=Room('changan/fangzhangshi', u'方丈室', None, 0, exits)

exits = [
	Exit('west', 'changan/baihu3', False),
	Exit('south', 'changan/fengxu2', False),
]
fengxu1=Room('changan/fengxu1', u'冯诩道', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/fengxu3', False),
	Exit('north', 'changan/fengxu1', False),
]
fengxu2=Room('changan/fengxu2', u'冯诩道', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/fengxu4', False),
	Exit('east', 'changan/dongan_dadao', False),
	Exit('north', 'changan/fengxu2', False),
]
fengxu3=Room('changan/fengxu3', u'冯诩道', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/fengxu5', False),
	Exit('east', 'changan/lingyange', False),
	Exit('north', 'changan/fengxu3', False),
]
fengxu4=Room('changan/fengxu4', u'冯诩道', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/qinglong3', False),
	Exit('east', 'changan/xunbufang', False),
	Exit('north', 'changan/fengxu4', False),
]
fengxu5=Room('changan/fengxu5', u'冯诩道', 'changan', 0, exits)

exits = [
	Exit('north', 'changan/qixiang2', False),
]
fruit_shop=Room('changan/fruit_shop', u'水果店', None, 0, exits)

exits = [
	Exit('west', 'changan/huanggong', False),
]
fudian1=Room('changan/fudian1', u'右翼殿', None, 0, exits)

exits = [
	Exit('east', 'changan/huanggong', False),
]
fudian2=Room('changan/fudian2', u'左翼殿', None, 0, exits)

exits = [
	Exit('south', 'changan/fufeng2', False),
	Exit('east', 'changan/baihu1', False),
]
fufeng1=Room('changan/fufeng1', u'扶风道', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/fufeng3', False),
	Exit('north', 'changan/fufeng1', False),
]
fufeng2=Room('changan/fufeng2', u'扶风道', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/xian_dadao', False),
	Exit('south', 'changan/fufeng4', False),
	Exit('north', 'changan/fufeng2', False),
]
fufeng3=Room('changan/fufeng3', u'扶风道', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/fufeng5', False),
	Exit('north', 'changan/fufeng3', False),
]
fufeng4=Room('changan/fufeng4', u'扶风道', 'changan', 0, exits)

exits = [
	Exit('east', 'changan/qinglong1', False),
	Exit('north', 'changan/fufeng4', False),
]
fufeng5=Room('changan/fufeng5', u'扶风道', 'changan', 0, exits)

exits = [
	Exit('north', 'changan/gongbu', False),
]
gongbu_shi=Room('changan/gongbu_shi', u'工部石厂', None, 0, exits)

exits = [
	Exit('south', 'changan/gongbu', False),
]
gongbu_tong=Room('changan/gongbu_tong', u'工部铜厂', None, 0, exits)

exits = [
	Exit('west', 'changan/nanan_dadao', False),
	Exit('south', 'changan/gongbu_shi', False),
	Exit('north', 'changan/gongbu_tong', False),
]
gongbu=Room('changan/gongbu', u'工部', None, 0, exits)

exits = [
	Exit('south', 'changan/baihu3', False),
]
guozijian=Room('changan/guozijian', u'国子监', None, 0, exits)

exits = [
	Exit('west', 'changan/road2', False),
	Exit('south', 'xiangyang/caodi3', False),
	Exit('east', 'changan/road1', False),
]
hanguguan=Room('changan/hanguguan', u'函谷关', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/huarui3', False),
]
huadian=Room('changan/huadian', u'花店', None, 0, exits)

exits = [
	Exit('west', 'changan/fudian2', False),
	Exit('south', 'changan/bridge2', False),
	Exit('east', 'changan/fudian1', False),
	Exit('north', 'changan/bridge1', False),
]
huanggong=Room('changan/huanggong', u'皇宫大殿', None, 0, exits)

exits = [
	Exit('west', 'changan/yongtai_nankou', False),
	Exit('south', 'changan/minju1', False),
	Exit('north', 'changan/majiu', False),
	Exit('east', 'changan/huarui2', False),
]
huarui1=Room('changan/huarui1', u'华瑞街', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/huarui1', False),
	Exit('south', 'changan/minju2', False),
	Exit('east', 'changan/huarui3', False),
	Exit('north', 'changan/mianguan', False),
]
huarui2=Room('changan/huarui2', u'华瑞街', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/huarui2', False),
	Exit('south', 'changan/minju3', False),
	Exit('east', 'changan/nanan_daokou', False),
	Exit('north', 'changan/huadian', False),
]
huarui3=Room('changan/huarui3', u'华瑞街', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/nanan_daokou', False),
	Exit('south', 'changan/minju4', False),
	Exit('east', 'changan/huarui5', False),
	Exit('north', 'changan/xiaojinghu', False),
]
huarui4=Room('changan/huarui4', u'华瑞街', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/huarui4', False),
	Exit('south', 'changan/minju5', False),
	Exit('north', 'changan/zahuopu', False),
	Exit('east', 'changan/huarui6', False),
]
huarui5=Room('changan/huarui5', u'华瑞街', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/huarui5', False),
	Exit('south', 'changan/minju6', False),
	Exit('east', 'changan/liande_nankou', False),
	Exit('north', 'changan/tuchangguan', False),
]
huarui6=Room('changan/huarui6', u'华瑞街', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/yongtai_dadao3', False),
]
huiwenge=Room('changan/huiwenge', u'汇文阁', None, 0, exits)

exits = [
	Exit('west', 'changan/yongtai_dadao1', False),
]
huozhan=Room('changan/huozhan', u'货栈', None, 0, exits)

exits = [
	Exit('south', 'changan/qixiang1', False),
	Exit('up', 'changan/jiulou2', False),
]
jiulou=Room('changan/jiulou', u'望星楼', None, 0, exits)

exits = [
	Exit('down', 'changan/jiulou', False),
]
jiulou2=Room('changan/jiulou2', u'望星楼二楼', None, 0, exits)

exits = [
	Exit('up', 'changan/kzsleep', False),
	Exit('north', 'changan/qixiang1', False),
]
kezhan=Room('changan/kezhan', u'悦宾客栈', None, 0, exits)

exits = [
	Exit('down', 'changan/kezhan', False),
]
kzsleep=Room('changan/kzsleep', u'客店睡房', None, 0, exits)

exits = [
	Exit('north', 'changan/xunbufang', False),
]
laofang=Room('changan/laofang', u'牢房', None, 0, exits)

exits = [
	Exit('west', 'changan/qixiang6', False),
	Exit('south', 'changan/liande_dadao1', False),
	Exit('north', 'changan/xiyuan', False),
]
liande_beikou=Room('changan/liande_beikou', u'连德北口', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/liande_dadao2', False),
	Exit('north', 'changan/liande_beikou', False),
]
liande_dadao1=Room('changan/liande_dadao1', u'连德大道', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/liande_dadao3', False),
	Exit('north', 'changan/liande_dadao1', False),
]
liande_dadao2=Room('changan/liande_dadao2', u'连德大道', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/dongan_daokou', False),
	Exit('north', 'changan/liande_dadao2', False),
]
liande_dadao3=Room('changan/liande_dadao3', u'连德大道', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/liande_dadao5', False),
	Exit('north', 'changan/dongan_daokou', False),
]
liande_dadao4=Room('changan/liande_dadao4', u'连德大道', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/liande_nankou', False),
	Exit('east', 'changan/xiaojia_qianyuan', False),
	Exit('north', 'changan/liande_dadao4', False),
]
liande_dadao5=Room('changan/liande_dadao5', u'连德大道', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/huarui6', False),
	Exit('south', 'changan/xiaojiuguan', False),
	Exit('north', 'changan/liande_dadao5', False),
]
liande_nankou=Room('changan/liande_nankou', u'连德南口', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/fengxu4', False),
]
lingyange=Room('changan/lingyange', u'凌烟阁', None, 0, exits)

exits = [
	Exit('south', 'changan/huarui1', False),
]
majiu=Room('changan/majiu', u'马厩', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/huarui2', False),
]
mianguan=Room('changan/mianguan', u'面馆', None, 0, exits)

exits = [
	Exit('west', 'changan/yongtai_dadao4', False),
]
miao=Room('changan/miao', u'城隍庙', None, 0, exits)

exits = [
	Exit('north', 'changan/huarui1', False),
]
minju1=Room('changan/minju1', u'民居', None, 0, exits)

exits = [
	Exit('north', 'changan/huarui2', False),
]
minju2=Room('changan/minju2', u'民居', None, 0, exits)

exits = [
	Exit('north', 'changan/huarui3', False),
]
minju3=Room('changan/minju3', u'民居', None, 0, exits)

exits = [
	Exit('north', 'changan/huarui4', False),
]
minju4=Room('changan/minju4', u'民居', None, 0, exits)

exits = [
	Exit('north', 'changan/huarui5', False),
]
minju5=Room('changan/minju5', u'民居', None, 0, exits)

exits = [
	Exit('north', 'changan/huarui6', False),
]
minju6=Room('changan/minju6', u'民居', None, 0, exits)

exits = [
	Exit('southwest', 'quanzhen/guandao1', False),
	Exit('north', 'changan/nanan_daokou', False),
]
nan_chengmen=Room('changan/nan_chengmen', u'长安南城门', '1', 0, exits)

exits = [
	Exit('south', 'changan/nanan_daokou', False),
	Exit('east', 'changan/gongbu', False),
	Exit('north', 'changan/qinglong2', False),
]
nanan_dadao=Room('changan/nanan_dadao', u'南安大道', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/huarui3', False),
	Exit('northwest', 'changan/bingying5', False),
	Exit('south', 'changan/nan_chengmen', False),
	Exit('northeast', 'changan/bingying4', False),
	Exit('east', 'changan/huarui4', False),
	Exit('north', 'changan/nanan_dadao', False),
]
nanan_daokou=Room('changan/nanan_daokou', u'南安道口', 'changan', 0, exits)

exits = [
	Exit('east', 'changan/baodian', False),
]
piandian=Room('changan/piandian', u'偏殿', None, 0, exits)

exits = [
]
prison=Room('changan/prison', u'大牢', None, 0, exits)

exits = [
	Exit('west', 'changan/fufeng5', False),
	Exit('south', 'changan/baoxiangsi', False),
	Exit('east', 'changan/qinglong2', False),
]
qinglong1=Room('changan/qinglong1', u'青龙街', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/qinglong1', False),
	Exit('south', 'changan/nanan_dadao', False),
	Exit('east', 'changan/qinglong3', False),
	Exit('north', 'changan/bridge2', False),
]
qinglong2=Room('changan/qinglong2', u'青龙街', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/qinglong2', False),
	Exit('south', 'changan/yamen', False),
	Exit('east', 'changan/fengxu5', False),
]
qinglong3=Room('changan/qinglong3', u'青龙街', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/yongtai_beikou', False),
	Exit('south', 'changan/kezhan', False),
	Exit('east', 'changan/qixiang2', False),
	Exit('north', 'changan/jiulou', False),
]
qixiang1=Room('changan/qixiang1', u'麒祥街', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/qixiang1', False),
	Exit('south', 'changan/fruit_shop', False),
	Exit('east', 'changan/qixiang3', False),
	Exit('north', 'changan/tea_shop', False),
]
qixiang2=Room('changan/qixiang2', u'麒祥街', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/qixiang2', False),
	Exit('south', 'changan/dangpu', False),
	Exit('east', 'changan/beian_daokou', False),
	Exit('north', 'changan/duchang', False),
]
qixiang3=Room('changan/qixiang3', u'麒祥街', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/beian_daokou', False),
	Exit('south', 'changan/qunyulou', False),
	Exit('east', 'changan/qixiang5', False),
	Exit('north', 'changan/bank', False),
]
qixiang4=Room('changan/qixiang4', u'麒祥街', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/qixiang4', False),
	Exit('south', 'changan/biaoju_damen', False),
	Exit('east', 'changan/qixiang6', False),
	Exit('north', 'changan/shoushi_dian', False),
]
qixiang5=Room('changan/qixiang5', u'麒祥街', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/qixiang5', False),
	Exit('south', 'changan/weapon_shop', False),
	Exit('east', 'changan/liande_beikou', False),
	Exit('north', 'changan/yaopu', False),
]
qixiang6=Room('changan/qixiang6', u'麒祥街', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/qunyulou1', False),
	Exit('north', 'changan/qixiang4', False),
]
qunyulou=Room('changan/qunyulou', u'群玉楼', None, 0, exits)

exits = [
	Exit('up', 'changan/qunyulou2', False),
	Exit('north', 'changan/qunyulou', False),
]
qunyulou1=Room('changan/qunyulou1', u'群玉楼大厅', None, 0, exits)

exits = [
	Exit('west', 'changan/qunyuys3', False),
	Exit('south', 'changan/qunyuys2', False),
	Exit('up', 'changan/qunyulou3', False),
	Exit('east', 'changan/qunyuys4', False),
	Exit('north', 'changan/qunyuys1', False),
	Exit('down', 'changan/qunyulou1', False),
]
qunyulou2=Room('changan/qunyulou2', u'群玉楼二楼', None, 0, exits)

exits = [
	Exit('west', 'changan/qunyuys7', False),
	Exit('south', 'changan/qunyuys6', False),
	Exit('east', 'changan/qunyuys8', False),
	Exit('north', 'changan/qunyuys5', False),
	Exit('down', 'changan/qunyulou2', False),
]
qunyulou3=Room('changan/qunyulou3', u'群玉楼三楼', None, 0, exits)

exits = [
	Exit('south', 'changan/qunyuys8', False),
]
qunyums=Room('changan/qunyums', u'群玉楼密室', None, 0, exits)

exits = [
	Exit('south', 'changan/qunyulou2', False),
]
qunyuys1=Room('changan/qunyuys1', u'群玉楼雅室', None, 0, exits)

exits = [
	Exit('north', 'changan/qunyulou2', False),
]
qunyuys2=Room('changan/qunyuys2', u'群玉楼雅室', None, 0, exits)

exits = [
	Exit('east', 'changan/qunyulou2', False),
]
qunyuys3=Room('changan/qunyuys3', u'群玉楼雅室', None, 0, exits)

exits = [
	Exit('west', 'changan/qunyulou2', False),
]
qunyuys4=Room('changan/qunyuys4', u'群玉楼雅室', None, 0, exits)

exits = [
	Exit('south', 'changan/qunyulou3', False),
]
qunyuys5=Room('changan/qunyuys5', u'群玉楼雅室', None, 0, exits)

exits = [
	Exit('north', 'changan/qunyulou3', False),
]
qunyuys6=Room('changan/qunyuys6', u'群玉楼雅室', None, 0, exits)

exits = [
	Exit('east', 'changan/qunyulou3', False),
]
qunyuys7=Room('changan/qunyuys7', u'群玉楼雅室', None, 0, exits)

exits = [
	Exit('west', 'changan/qunyulou3', False),
]
qunyuys8=Room('changan/qunyuys8', u'群玉楼雅室', None, 0, exits)

exits = [
	Exit('west', 'changan/hanguguan', False),
	Exit('east', 'city/ximenroad', False),
]
road1=Room('changan/road1', u'关洛道', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/zhongnan', False),
	Exit('east', 'changan/hanguguan', False),
	Exit('north', 'village/hsroad1', False),
]
road2=Room('changan/road2', u'大官道', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/road4', False),
	Exit('east', 'changan/zhongnan', False),
]
road3=Room('changan/road3', u'大官道', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/dong_chengmen', False),
	Exit('east', 'changan/road3', False),
]
road4=Room('changan/road4', u'大官道', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/qixiang5', False),
]
shoushi_dian=Room('changan/shoushi_dian', u'首饰店', None, 0, exits)

exits = [
	Exit('south', 'changan/qixiang2', False),
]
tea_shop=Room('changan/tea_shop', u'茶馆', None, 0, exits)

exits = [
	Exit('south', 'changan/huarui6', False),
]
tuchangguan=Room('changan/tuchangguan', u'土娼馆', None, 0, exits)

exits = [
	Exit('south', 'changan/bei_chengmen', False),
	Exit('northeast', 'changan/tulu2', False),
]
tulu1=Room('changan/tulu1', u'土路', 'changan', 0, exits)

exits = [
	Exit('northup', 'changan/tulu3', False),
	Exit('southwest', 'changan/tulu1', False),
]
tulu2=Room('changan/tulu2', u'土路', 'changan', 0, exits)

exits = [
	Exit('southdown', 'changan/tulu2', False),
	Exit('northeast', 'changan/tulu4', False),
]
tulu3=Room('changan/tulu3', u'土路', 'changan', 0, exits)

exits = [
	Exit('southwest', 'changan/tulu3', False),
	Exit('northdown', 'huanghe/yongdeng', False),
]
tulu4=Room('changan/tulu4', u'土路', 'changan', 0, exits)

exits = [
	Exit('north', 'changan/qixiang6', False),
]
weapon_shop=Room('changan/weapon_shop', u'兵器店', None, 0, exits)

exits = [
	Exit('west', 'xingxiu/xxroad1', False),
	Exit('east', 'changan/xian_daokou', False),
]
xi_chengmen=Room('changan/xi_chengmen', u'长安西城门', 'changan', 0, exits)

exits = [
	Exit('west', 'changan/xian_daokou', False),
	Exit('east', 'changan/fufeng3', False),
]
xian_dadao=Room('changan/xian_dadao', u'西安大道', 'changan', 0, exits)

exits = [
	Exit('southeast', 'changan/bingying3', False),
	Exit('west', 'changan/xi_chengmen', False),
	Exit('south', 'changan/yongtai_dadao4', False),
	Exit('east', 'changan/xian_dadao', False),
	Exit('north', 'changan/yongtai_dadao3', False),
]
xian_daokou=Room('changan/xian_daokou', u'西安道口', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/xiaojiadt', False),
]
xiaojia_pianting=Room('changan/xiaojia_pianting', u'偏厅', None, 0, exits)

exits = [
	Exit('west', 'changan/liande_dadao5', False),
	Exit('east', 'changan/xiaojiadt', False),
]
xiaojia_qianyuan=Room('changan/xiaojia_qianyuan', u'萧家前院', 'changan', 0, exits)

exits = [
	Exit('north', 'changan/xiaojiadt', False),
]
xiaojia_sleep=Room('changan/xiaojia_sleep', u'卧室', None, 0, exits)

exits = [
	Exit('west', 'changan/xiaojia_qianyuan', False),
	Exit('south', 'changan/xiaojia_sleep', False),
	Exit('north', 'changan/xiaojia_pianting', False),
]
xiaojiadt=Room('changan/xiaojiadt', u'萧家大厅', None, 0, exits)

exits = [
	Exit('south', 'changan/huarui4', False),
]
xiaojinghu=Room('changan/xiaojinghu', u'小镜湖', 'changan', 0, exits)

exits = [
	Exit('north', 'changan/liande_nankou', False),
]
xiaojiuguan=Room('changan/xiaojiuguan', u'小酒馆', None, 0, exits)

exits = [
	Exit('south', 'changan/liande_beikou', False),
]
xiyuan=Room('changan/xiyuan', u'戏院', None, 0, exits)

exits = [
	Exit('west', 'changan/fengxu5', False),
]
xunbufang=Room('changan/xunbufang', u'巡捕房', None, 0, exits)

exits = [
	Exit('north', 'changan/yamen', False),
]
yamen_datang=Room('changan/yamen_datang', u'长安府大堂', None, 0, exits)

exits = [
	Exit('south', 'changan/yamen_datang', False),
	Exit('north', 'changan/qinglong3', False),
]
yamen=Room('changan/yamen', u'衙门大门', None, 0, exits)

exits = [
	Exit('south', 'changan/qixiang6', False),
]
yaopu=Room('changan/yaopu', u'回春堂药铺', None, 0, exits)

exits = [
	Exit('south', 'changan/yongtai_dadao1', False),
	Exit('north', 'changan/zhubaohang', False),
	Exit('east', 'changan/qixiang1', False),
]
yongtai_beikou=Room('changan/yongtai_beikou', u'永泰北口', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/yongtai_dadao2', False),
	Exit('east', 'changan/huozhan', False),
	Exit('north', 'changan/yongtai_beikou', False),
]
yongtai_dadao1=Room('changan/yongtai_dadao1', u'永泰大道', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/yongtai_dadao3', False),
	Exit('east', 'pk/entry', False),
	Exit('north', 'changan/yongtai_dadao1', False),
]
yongtai_dadao2=Room('changan/yongtai_dadao2', u'永泰大道', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/xian_daokou', False),
	Exit('east', 'changan/huiwenge', False),
	Exit('north', 'changan/yongtai_dadao2', False),
]
yongtai_dadao3=Room('changan/yongtai_dadao3', u'永泰大道', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/yongtai_dadao5', False),
	Exit('east', 'changan/miao', False),
	Exit('north', 'changan/xian_daokou', False),
]
yongtai_dadao4=Room('changan/yongtai_dadao4', u'永泰大道', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/yongtai_nankou', False),
	Exit('north', 'changan/yongtai_dadao4', False),
]
yongtai_dadao5=Room('changan/yongtai_dadao5', u'永泰大道', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/baozipu', False),
	Exit('north', 'changan/yongtai_dadao5', False),
	Exit('east', 'changan/huarui1', False),
]
yongtai_nankou=Room('changan/yongtai_nankou', u'永泰南口', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/huarui5', False),
]
zahuopu=Room('changan/zahuopu', u'杂货铺', None, 0, exits)

exits = [
	Exit('west', 'changan/road3', False),
	Exit('east', 'changan/road2', False),
]
zhongnan=Room('changan/zhongnan', u'终南山口', 'changan', 0, exits)

exits = [
	Exit('south', 'changan/yongtai_beikou', False),
]
zhubaohang=Room('changan/zhubaohang', u'珠宝行', None, 0, exits)

