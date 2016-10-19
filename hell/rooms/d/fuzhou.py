# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('northup', 'fuzhou/pingshan', False),
	Exit('south', 'fuzhou/dongjiekou', False),
]
beidajie=Room('fuzhou/beidajie', u'北大街', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'fuzhou/xidajie', False),
	Exit('enter', 'fuzhou/biaojudy', False),
]
biaoju=Room('fuzhou/biaoju', u'福威镖局', None, 0, exits)

exits = [
	Exit('out', 'fuzhou/biaoju', False),
	Exit('north', 'fuzhou/biaojuzt', False),
]
biaojudy=Room('fuzhou/biaojudy', u'镖局大院', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'fuzhou/biaojuzt', False),
]
biaojuhy=Room('fuzhou/biaojuhy', u'镖局后院', 'fuzhou', 0, exits)

exits = [
	Exit('east', 'fuzhou/biaojuzt', False),
]
biaojunz=Room('fuzhou/biaojunz', u'内宅', None, 0, exits)

exits = [
	Exit('west', 'fuzhou/biaojunz', False),
	Exit('south', 'fuzhou/biaojudy', False),
	Exit('north', 'fuzhou/biaojuhy', False),
]
biaojuzt=Room('fuzhou/biaojuzt', u'正厅', None, 0, exits)

exits = [
	Exit('west', 'fuzhou/dongjiekou', False),
	Exit('southup', 'fuzhou/yushan', False),
	Exit('east', 'fuzhou/dongxiaojie', False),
	Exit('north', 'fuzhou/rongcheng', False),
]
dongdajie=Room('fuzhou/dongdajie', u'东大街', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/xidajie', False),
	Exit('south', 'fuzhou/nandajie', False),
	Exit('east', 'fuzhou/dongdajie', False),
	Exit('north', 'fuzhou/beidajie', False),
]
dongjiekou=Room('fuzhou/dongjiekou', u'东街口', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/dongxiaojie', False),
	Exit('east', 'fuzhou/shulin', False),
]
dongmen=Room('fuzhou/dongmen', u'福州东门', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/dongdajie', False),
	Exit('east', 'fuzhou/dongmen', False),
]
dongxiaojie=Room('fuzhou/dongxiaojie', u'东小街', 'fuzhou', 0, exits)

exits = [
	Exit('southdown', 'fuzhou/fzroad2', False),
	Exit('west', 'fuzhou/kedian', False),
	Exit('north', 'fuzhou/fzroad1', False),
]
erbapu=Room('fuzhou/erbapu', u'廿八铺', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'fuzhou/erbapu', False),
	Exit('northdown', 'quanzhou/qzroad4', False),
]
fzroad1=Room('fuzhou/fzroad1', u'仙霞岭', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'fuzhou/fzroad9', False),
]
fzroad10=Room('fuzhou/fzroad10', u'酒肆', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/fzroad9', False),
	Exit('east', 'fuzhou/ximen', False),
]
fzroad11=Room('fuzhou/fzroad11', u'闽中大道', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/wuyishan1', False),
	Exit('southup', 'fuzhou/fzroad3', False),
	Exit('northup', 'fuzhou/erbapu', False),
]
fzroad2=Room('fuzhou/fzroad2', u'武夷山道', 'fuzhou', 0, exits)

exits = [
	Exit('southdown', 'fuzhou/yanping', False),
	Exit('northdown', 'fuzhou/fzroad2', False),
]
fzroad3=Room('fuzhou/fzroad3', u'闽浙古道', 'fuzhou', 0, exits)

exits = [
	Exit('southwest', 'fuzhou/fzroad5', False),
	Exit('northeast', 'fuzhou/yanping', False),
]
fzroad4=Room('fuzhou/fzroad4', u'闽赣古道', 'fuzhou', 0, exits)

exits = [
	Exit('northeast', 'fuzhou/fzroad4', False),
	Exit('westup', 'fuzhou/fzroad6', False),
]
fzroad5=Room('fuzhou/fzroad5', u'闽赣古道', 'fuzhou', 0, exits)

exits = [
	Exit('eastdown', 'fuzhou/fzroad5', False),
	Exit('westdown', 'fuzhou/fzroad7', False),
]
fzroad6=Room('fuzhou/fzroad6', u'闽赣古道', 'fuzhou', 0, exits)

exits = [
	Exit('northwest', 'henshan/hsroad2', False),
	Exit('eastup', 'fuzhou/fzroad6', False),
]
fzroad7=Room('fuzhou/fzroad7', u'闽赣古道', 'fuzhou', 0, exits)

exits = [
	Exit('southeast', 'fuzhou/fzroad9', False),
	Exit('northwest', 'fuzhou/yanping', False),
]
fzroad8=Room('fuzhou/fzroad8', u'闽江', 'fuzhou', 0, exits)

exits = [
	Exit('northwest', 'fuzhou/fzroad8', False),
	Exit('east', 'fuzhou/fzroad11', False),
	Exit('north', 'fuzhou/fzroad10', False),
]
fzroad9=Room('fuzhou/fzroad9', u'闽中大道', 'fuzhou', 0, exits)

exits = [
	Exit('westdown', 'fuzhou/shulin', False),
	Exit('north', 'fuzhou/yongquan', False),
]
gushan=Room('fuzhou/gushan', u'鼓山', 'fuzhou', 0, exits)

exits = [
	Exit('down', 'fuzhou/well', False),
]
houyuan=Room('fuzhou/houyuan', u'老宅后院', None, 0, exits)

exits = [
	Exit('east', 'fuzhou/erbapu', False),
]
kedian=Room('fuzhou/kedian', u'客店', None, 0, exits)

exits = [
	Exit('south', 'fuzhou/xiangyang', False),
]
laozhai=Room('fuzhou/laozhai', u'向阳老宅', None, 0, exits)

exits = [
	Exit('down', 'fuzhou/mishi', False),
]
liang=Room('fuzhou/liang', u'密室房梁', None, 0, exits)

exits = [
	Exit('south', 'fuzhou/rongcheng', False),
]
majiu=Room('fuzhou/majiu', u'马厩', 'fuzhou', 0, exits)

exits = [
	Exit('out', 'fuzhou/well', False),
]
midao=Room('fuzhou/midao', u'密道', None, 0, exits)

exits = [
	Exit('out', 'fuzhou/midao', False),
]
mishi=Room('fuzhou/mishi', u'密室', None, 0, exits)

exits = [
	Exit('west', 'fuzhou/yamen', False),
	Exit('south', 'fuzhou/nanmendou', False),
	Exit('east', 'fuzhou/weizhongwei', False),
	Exit('north', 'fuzhou/dongjiekou', False),
]
nandajie=Room('fuzhou/nandajie', u'南大街', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'fuzhou/zhongzhou', False),
	Exit('north', 'fuzhou/nanmendou', False),
]
nanmen=Room('fuzhou/nanmen', u'福州南门', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/shiqiao', False),
	Exit('south', 'fuzhou/nanmen', False),
	Exit('east', 'fuzhou/xiaochang', False),
	Exit('north', 'fuzhou/nandajie', False),
]
nanmendou=Room('fuzhou/nanmendou', u'南门兜', 'fuzhou', 0, exits)

exits = [
	Exit('southdown', 'fuzhou/beidajie', False),
]
pingshan=Room('fuzhou/pingshan', u'福州屏山', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'quanzhou/beimen', False),
	Exit('north', 'fuzhou/zhongzhou', False),
]
puxian=Room('fuzhou/puxian', u'莆仙平原', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'fuzhou/dongdajie', False),
	Exit('up', 'fuzhou/rongcheng2', False),
	Exit('north', 'fuzhou/majiu', False),
]
rongcheng=Room('fuzhou/rongcheng', u'榕城驿', None, 0, exits)

exits = [
	Exit('down', 'fuzhou/rongcheng', False),
]
rongcheng2=Room('fuzhou/rongcheng2', u'榕城驿二楼', None, 0, exits)

exits = [
	Exit('west', 'fuzhou/xiangyang', False),
	Exit('east', 'fuzhou/nanmendou', False),
]
shiqiao=Room('fuzhou/shiqiao', u'石桥', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/dongmen', False),
	Exit('eastup', 'fuzhou/gushan', False),
	Exit('north', 'fuzhou/wuxiang', False),
]
shulin=Room('fuzhou/shulin', u'树林', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/nandajie', False),
]
weizhongwei=Room('fuzhou/weizhongwei', u'味中味', None, 0, exits)

exits = [
	Exit('up', 'fuzhou/houyuan', False),
	Exit('down', 'fuzhou/well1', False),
]
well=Room('fuzhou/well', u'井中', None, 0, exits)

exits = [
	Exit('up', 'fuzhou/well', False),
]
well1=Room('fuzhou/well1', u'井底', None, 0, exits)

exits = [
	Exit('northdown', 'fuzhou/xidajie', False),
]
wushan=Room('fuzhou/wushan', u'福州乌山', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'fuzhou/shulin', False),
]
wuxiang=Room('fuzhou/wuxiang', u'无相庵', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/wuyishan2', False),
	Exit('east', 'fuzhou/fzroad2', False),
]
wuyishan1=Room('fuzhou/wuyishan1', u'武夷山', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/wuyishan5', False),
	Exit('south', 'fuzhou/wuyishan7', False),
	Exit('northup', 'fuzhou/wuyishan6', False),
	Exit('east', 'fuzhou/wuyishan1', False),
]
wuyishan2=Room('fuzhou/wuyishan2', u'九曲溪', 'fuzhou', 0, exits)

exits = [
	Exit('southdown', 'fuzhou/wuyishan5', False),
]
wuyishan3=Room('fuzhou/wuyishan3', u'天游峰', 'fuzhou', 0, exits)

exits = [
	Exit('southeast', 'fuzhou/wuyishan5', False),
]
wuyishan4=Room('fuzhou/wuyishan4', u'天心岩', 'fuzhou', 0, exits)

exits = [
	Exit('northwest', 'fuzhou/wuyishan4', False),
	Exit('northup', 'fuzhou/wuyishan3', False),
	Exit('east', 'fuzhou/wuyishan2', False),
]
wuyishan5=Room('fuzhou/wuyishan5', u'九曲溪', 'fuzhou', 0, exits)

exits = [
	Exit('southdown', 'fuzhou/wuyishan2', False),
]
wuyishan6=Room('fuzhou/wuyishan6', u'大王峰', 'fuzhou', 0, exits)

exits = [
	Exit('north', 'fuzhou/wuyishan2', False),
]
wuyishan7=Room('fuzhou/wuyishan7', u'玉女峰', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/zahuopu', False),
	Exit('north', 'fuzhou/laozhai', False),
	Exit('east', 'fuzhou/shiqiao', False),
]
xiangyang=Room('fuzhou/xiangyang', u'向阳巷', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/nanmendou', False),
]
xiaochang=Room('fuzhou/xiaochang', u'校场', 'fuzhou', 0, exits)

exits = [
	Exit('north', 'fuzhou/ximendajie', False),
]
xichansi=Room('fuzhou/xichansi', u'西禅寺', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/ximendajie', False),
	Exit('southup', 'fuzhou/wushan', False),
	Exit('east', 'fuzhou/dongjiekou', False),
	Exit('north', 'fuzhou/biaoju', False),
]
xidajie=Room('fuzhou/xidajie', u'西大街', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'fuzhou/ximendajie', False),
]
xihu=Room('fuzhou/xihu', u'西湖', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/fzroad11', False),
	Exit('east', 'fuzhou/ximendajie', False),
]
ximen=Room('fuzhou/ximen', u'福州西门', 'fuzhou', 0, exits)

exits = [
	Exit('west', 'fuzhou/ximen', False),
	Exit('south', 'fuzhou/xichansi', False),
	Exit('north', 'fuzhou/xihu', False),
	Exit('east', 'fuzhou/xidajie', False),
]
ximendajie=Room('fuzhou/ximendajie', u'西门大街', 'fuzhou', 0, exits)

exits = [
	Exit('east', 'fuzhou/nandajie', False),
]
yamen=Room('fuzhou/yamen', u'提督衙门', None, 0, exits)

exits = [
	Exit('southeast', 'fuzhou/fzroad8', False),
	Exit('northup', 'fuzhou/fzroad3', False),
	Exit('southwest', 'fuzhou/fzroad4', False),
]
yanping=Room('fuzhou/yanping', u'延平府', 'fuzhou', 0, exits)

exits = [
	Exit('south', 'fuzhou/gushan', False),
]
yongquan=Room('fuzhou/yongquan', u'涌泉寺', 'fuzhou', 0, exits)

exits = [
	Exit('northdown', 'fuzhou/dongdajie', False),
]
yushan=Room('fuzhou/yushan', u'福州于山', 'fuzhou', 0, exits)

exits = [
	Exit('east', 'fuzhou/xiangyang', False),
]
zahuopu=Room('fuzhou/zahuopu', u'杂货铺', None, 0, exits)

exits = [
	Exit('south', 'fuzhou/puxian', False),
	Exit('north', 'fuzhou/nanmen', False),
]
zhongzhou=Room('fuzhou/zhongzhou', u'中洲桥', 'fuzhou', 0, exits)

