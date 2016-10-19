# coding=gbk

from _objects import Room,Exit

exits = [
	Exit('east', 'xiakedao/neiting', False),
]
chashi=Room('xiakedao/chashi', u'茶室', None, 0, exits)

exits = [
]
dahai=Room('xiakedao/dahai', u'大海', 'xiakedao', 0, exits)

exits = [
	Exit('west', 'xiakedao/wuqiku', False),
	Exit('east', 'xiakedao/shufang', False),
	Exit('north', 'xiakedao/shidong5', False),
]
dating=Room('xiakedao/dating', u'大厅', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/shidong1', False),
	Exit('enter', 'xiakedao/yingbin', False),
]
dongmen=Room('xiakedao/dongmen', u'洞门', None, 0, exits)

exits = [
]
duchuan=Room('xiakedao/duchuan', u'小舟', 'xiakedao', 0, exits)

exits = [
]
gudi=Room('xiakedao/gudi', u'谷底', 'xiakedao', 0, exits)

exits = [
	Exit('west', 'xiakedao/zhuwu', False),
	Exit('north', 'xiakedao/xkroad4', False),
]
haibin=Room('xiakedao/haibin', u'南海之滨', 'nanhai', 0, exits)

exits = [
	Exit('east', 'xiakedao/xkroad4', False),
]
haigang=Room('xiakedao/haigang', u'渔港', 'nanhai', 0, exits)

exits = [
	Exit('south', 'xiakedao/lin1', False),
]
haitan=Room('xiakedao/haitan', u'海滩', 'xiakedao', 0, exits)

exits = [
	Exit('west', 'xiakedao/lin1', False),
	Exit('south', 'xiakedao/lin2', False),
	Exit('north', 'xiakedao/haitan', False),
	Exit('east', 'xiakedao/lin1', False),
]
lin1=Room('xiakedao/lin1', u'树林', 'xiakedao', 0, exits)

exits = [
	Exit('southeast', 'xiakedao/lin2', False),
	Exit('west', 'xiakedao/lin1', False),
	Exit('south', 'xiakedao/lin2', False),
	Exit('northeast', 'xiakedao/lin2', False),
	Exit('north', 'xiakedao/lin2', False),
	Exit('east', 'xiakedao/lin3', False),
]
lin2=Room('xiakedao/lin2', u'树林', 'xiakedao', 0, exits)

exits = [
	Exit('southeast', 'xiakedao/lin4', False),
	Exit('west', 'xiakedao/lin2', False),
	Exit('south', 'xiakedao/lin3', False),
	Exit('northeast', 'xiakedao/lin3', False),
	Exit('north', 'xiakedao/lin3', False),
	Exit('east', 'xiakedao/lin3', False),
]
lin3=Room('xiakedao/lin3', u'树林', 'xiakedao', 0, exits)

exits = [
	Exit('southeast', 'xiakedao/lin4', False),
	Exit('west', 'xiakedao/lin5', False),
	Exit('northwest', 'xiakedao/lin3', False),
	Exit('south', 'xiakedao/lin4', False),
	Exit('north', 'xiakedao/lin4', False),
	Exit('east', 'xiakedao/lin4', False),
]
lin4=Room('xiakedao/lin4', u'树林', 'xiakedao', 0, exits)

exits = [
	Exit('southeast', 'xiakedao/lin5', False),
	Exit('west', 'xiakedao/lin5', False),
	Exit('northwest', 'xiakedao/lin6', False),
	Exit('south', 'xiakedao/lin5', False),
	Exit('north', 'xiakedao/lin5', False),
	Exit('east', 'xiakedao/lin4', False),
]
lin5=Room('xiakedao/lin5', u'树林', 'xiakedao', 0, exits)

exits = [
	Exit('southeast', 'xiakedao/lin5', False),
	Exit('west', 'xiakedao/lin6', False),
	Exit('northwest', 'xiakedao/lin6', False),
	Exit('south', 'xiakedao/lin6', False),
	Exit('north', 'xiakedao/lin6', False),
	Exit('east', 'xiakedao/lin7', False),
]
lin6=Room('xiakedao/lin6', u'树林', 'xiakedao', 0, exits)

exits = [
	Exit('southeast', 'xiakedao/lin7', False),
	Exit('west', 'xiakedao/lin6', False),
	Exit('northwest', 'xiakedao/lin7', False),
	Exit('south', 'xiakedao/lin8', False),
	Exit('north', 'xiakedao/lin7', False),
	Exit('east', 'xiakedao/lin7', False),
]
lin7=Room('xiakedao/lin7', u'树林', 'xiakedao', 0, exits)

exits = [
	Exit('south', 'xiakedao/shanmen', False),
	Exit('north', 'xiakedao/lin7', False),
]
lin8=Room('xiakedao/lin8', u'树林', 'xiakedao', 0, exits)

exits = [
	Exit('west', 'xiakedao/midao1', False),
	Exit('south', 'xiakedao/midao1', False),
	Exit('east', 'xiakedao/midao2', False),
	Exit('north', 'xiakedao/midao1', False),
]
midao1=Room('xiakedao/midao1', u'秘密通道', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/midao1', False),
	Exit('south', 'xiakedao/midao3', False),
	Exit('north', 'xiakedao/midao2', False),
	Exit('east', 'xiakedao/midao2', False),
]
midao2=Room('xiakedao/midao2', u'秘密通道', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/midao4', False),
	Exit('south', 'xiakedao/midao3', False),
	Exit('east', 'xiakedao/midao3', False),
	Exit('north', 'xiakedao/midao2', False),
]
midao3=Room('xiakedao/midao3', u'秘密通道', None, 0, exits)

exits = [
	Exit('east', 'xiakedao/midao3', False),
]
midao4=Room('xiakedao/midao4', u'密道', None, 0, exits)

exits = [
	Exit('out', 'xiakedao/neiting', False),
	Exit('east', 'xiakedao/midao4', False),
]
midao5=Room('xiakedao/midao5', u'秘密通道', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/midao7', False),
]
midao6=Room('xiakedao/midao6', u'石洞', None, 0, exits)

exits = [
	Exit('out', 'xiakedao/dating', False),
	Exit('northup', 'xiakedao/midao8', False),
	Exit('east', 'xiakedao/midao6', False),
]
midao7=Room('xiakedao/midao7', u'秘密通道', None, 0, exits)

exits = [
	Exit('southdown', 'xiakedao/midao7', False),
]
midao8=Room('xiakedao/midao8', u'密道', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/chashi', False),
	Exit('east', 'xiakedao/shibi', False),
	Exit('north', 'xiakedao/xiuxis2', False),
	Exit('enter', 'xiakedao/shihole1', False),
]
neiting=Room('xiakedao/neiting', u'内厅', None, 0, exits)

exits = [
	Exit('northdown', 'xiakedao/road4', False),
]
pubu=Room('xiakedao/pubu', u'瀑布', 'xiakedao', 0, exits)

exits = [
	Exit('southup', 'xiakedao/road2', False),
	Exit('northdown', 'xiakedao/shanmen', False),
]
road1=Room('xiakedao/road1', u'山路', 'xiakedao', 0, exits)

exits = [
	Exit('southup', 'xiakedao/road3', False),
	Exit('northdown', 'xiakedao/road1', False),
]
road2=Room('xiakedao/road2', u'山路', 'xiakedao', 0, exits)

exits = [
	Exit('southup', 'xiakedao/road4', False),
	Exit('northdown', 'xiakedao/road2', False),
]
road3=Room('xiakedao/road3', u'山路', 'xiakedao', 0, exits)

exits = [
	Exit('southup', 'xiakedao/pubu', False),
	Exit('northdown', 'xiakedao/road3', False),
]
road4=Room('xiakedao/road4', u'山路', 'xiakedao', 0, exits)

exits = [
	Exit('southup', 'xiakedao/road6', False),
	Exit('north', 'xiakedao/shidong8', False),
]
road5=Room('xiakedao/road5', u'山路', 'xiakedao', 0, exits)

exits = [
	Exit('southup', 'xiakedao/road7', False),
	Exit('northdown', 'xiakedao/road5', False),
]
road6=Room('xiakedao/road6', u'山路', 'xiakedao', 0, exits)

exits = [
	Exit('southup', 'xiakedao/road8', False),
	Exit('northdown', 'xiakedao/road6', False),
]
road7=Room('xiakedao/road7', u'夹鳖石', 'xiakedao', 0, exits)

exits = [
	Exit('southup', 'xiakedao/wangyun', False),
	Exit('northdown', 'xiakedao/road7', False),
]
road8=Room('xiakedao/road8', u'一线天', 'xiakedao', 0, exits)

exits = [
	Exit('southup', 'xiakedao/road1', False),
	Exit('north', 'xiakedao/lin8', False),
]
shanmen=Room('xiakedao/shanmen', u'山门', 'xiakedao', 0, exits)

exits = [
	Exit('out', 'xiakedao/shimen', False),
	Exit('west', 'xiakedao/neiting', False),
	Exit('east', 'xiakedao/wuchang', False),
]
shibi=Room('xiakedao/shibi', u'石壁', None, 0, exits)

exits = [
	Exit('south', 'xiakedao/shidong6', False),
	Exit('north', 'xiakedao/yongdao2', False),
	Exit('east', 'xiakedao/dongmen', False),
]
shidong1=Room('xiakedao/shidong1', u'石洞', None, 0, exits)

exits = [
	Exit('out', 'xiakedao/dating', False),
	Exit('east', 'xiakedao/shidong9', False),
]
shidong10=Room('xiakedao/shidong10', u'石洞', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/shidong2', False),
	Exit('south', 'xiakedao/shidong2', False),
	Exit('north', 'xiakedao/yingbin', False),
	Exit('east', 'xiakedao/shidong3', False),
]
shidong2=Room('xiakedao/shidong2', u'石洞', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/shidong3', False),
	Exit('south', 'xiakedao/shidong4', False),
	Exit('north', 'xiakedao/yingbin', False),
	Exit('east', 'xiakedao/shidong3', False),
]
shidong3=Room('xiakedao/shidong3', u'石洞', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/shidong5', False),
	Exit('south', 'xiakedao/shidong4', False),
	Exit('north', 'xiakedao/yingbin', False),
	Exit('east', 'xiakedao/shidong4', False),
]
shidong4=Room('xiakedao/shidong4', u'石洞', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/shidong5', False),
	Exit('south', 'xiakedao/dating', False),
	Exit('north', 'xiakedao/yingbin', False),
	Exit('east', 'xiakedao/shidong5', False),
]
shidong5=Room('xiakedao/shidong5', u'石洞', None, 0, exits)

exits = [
	Exit('south', 'xiakedao/shidong7', False),
	Exit('north', 'xiakedao/shidong1', False),
]
shidong6=Room('xiakedao/shidong6', u'石洞', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/shidong8', False),
	Exit('north', 'xiakedao/shidong6', False),
]
shidong7=Room('xiakedao/shidong7', u'石洞', None, 0, exits)

exits = [
	Exit('south', 'xiakedao/road5', False),
	Exit('east', 'xiakedao/shidong7', False),
]
shidong8=Room('xiakedao/shidong8', u'石洞', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/shidong10', False),
	Exit('east', 'xiakedao/yadi', False),
]
shidong9=Room('xiakedao/shidong9', u'石洞', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/shiroom04', False),
	Exit('out', 'xiakedao/neiting', False),
	Exit('south', 'xiakedao/shiroom02', False),
	Exit('east', 'xiakedao/shiroom03', False),
	Exit('north', 'xiakedao/shiroom01', False),
	Exit('enter', 'xiakedao/shihole2', False),
]
shihole1=Room('xiakedao/shihole1', u'石洞', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/shiroom08', False),
	Exit('out', 'xiakedao/shihole1', False),
	Exit('south', 'xiakedao/shiroom06', False),
	Exit('east', 'xiakedao/shiroom07', False),
	Exit('north', 'xiakedao/shiroom05', False),
	Exit('enter', 'xiakedao/shihole3', False),
]
shihole2=Room('xiakedao/shihole2', u'石洞', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/shiroom12', False),
	Exit('out', 'xiakedao/shihole2', False),
	Exit('south', 'xiakedao/shiroom10', False),
	Exit('east', 'xiakedao/shiroom11', False),
	Exit('north', 'xiakedao/shiroom09', False),
	Exit('enter', 'xiakedao/shihole4', False),
]
shihole3=Room('xiakedao/shihole3', u'石洞', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/shiroom16', False),
	Exit('out', 'xiakedao/shihole3', False),
	Exit('south', 'xiakedao/shiroom14', False),
	Exit('east', 'xiakedao/shiroom15', False),
	Exit('north', 'xiakedao/shiroom13', False),
	Exit('enter', 'xiakedao/shihole5', False),
]
shihole4=Room('xiakedao/shihole4', u'石洞', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/shiroom20', False),
	Exit('out', 'xiakedao/shihole4', False),
	Exit('south', 'xiakedao/shiroom18', False),
	Exit('east', 'xiakedao/shiroom19', False),
	Exit('north', 'xiakedao/shiroom17', False),
	Exit('enter', 'xiakedao/shihole6', False),
]
shihole5=Room('xiakedao/shihole5', u'石洞', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/shiroom24', False),
	Exit('out', 'xiakedao/shihole5', False),
	Exit('south', 'xiakedao/shiroom22', False),
	Exit('east', 'xiakedao/shiroom23', False),
	Exit('north', 'xiakedao/shiroom21', False),
]
shihole6=Room('xiakedao/shihole6', u'石洞', None, 0, exits)

exits = [
	Exit('north', 'xiakedao/yongdao3', False),
	Exit('enter', 'xiakedao/shibi', False),
]
shimen=Room('xiakedao/shimen', u'石门', None, 0, exits)

exits = [
	Exit('south', 'xiakedao/shihole1', False),
]
shiroom01=Room('xiakedao/shiroom01', u'石室', None, 0, exits)

exits = [
	Exit('north', 'xiakedao/shihole1', False),
]
shiroom02=Room('xiakedao/shiroom02', u'石室', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/shihole1', False),
]
shiroom03=Room('xiakedao/shiroom03', u'石室', None, 0, exits)

exits = [
	Exit('east', 'xiakedao/shihole1', False),
]
shiroom04=Room('xiakedao/shiroom04', u'石室', None, 0, exits)

exits = [
	Exit('south', 'xiakedao/shihole2', False),
]
shiroom05=Room('xiakedao/shiroom05', u'石室', None, 0, exits)

exits = [
	Exit('north', 'xiakedao/shihole2', False),
]
shiroom06=Room('xiakedao/shiroom06', u'石室', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/shihole2', False),
]
shiroom07=Room('xiakedao/shiroom07', u'石室', None, 0, exits)

exits = [
	Exit('east', 'xiakedao/shihole2', False),
]
shiroom08=Room('xiakedao/shiroom08', u'石室', None, 0, exits)

exits = [
	Exit('south', 'xiakedao/shihole3', False),
]
shiroom09=Room('xiakedao/shiroom09', u'石室', None, 0, exits)

exits = [
	Exit('north', 'xiakedao/shihole3', False),
]
shiroom10=Room('xiakedao/shiroom10', u'石室', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/shihole3', False),
]
shiroom11=Room('xiakedao/shiroom11', u'石室', None, 0, exits)

exits = [
	Exit('east', 'xiakedao/shihole3', False),
]
shiroom12=Room('xiakedao/shiroom12', u'石室', None, 0, exits)

exits = [
	Exit('south', 'xiakedao/shihole4', False),
]
shiroom13=Room('xiakedao/shiroom13', u'石室', None, 0, exits)

exits = [
	Exit('north', 'xiakedao/shihole4', False),
]
shiroom14=Room('xiakedao/shiroom14', u'石室', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/shihole4', False),
]
shiroom15=Room('xiakedao/shiroom15', u'石室', None, 0, exits)

exits = [
	Exit('east', 'xiakedao/shihole4', False),
]
shiroom16=Room('xiakedao/shiroom16', u'石室', None, 0, exits)

exits = [
	Exit('south', 'xiakedao/shihole5', False),
]
shiroom17=Room('xiakedao/shiroom17', u'石室', None, 0, exits)

exits = [
	Exit('north', 'xiakedao/shihole5', False),
]
shiroom18=Room('xiakedao/shiroom18', u'石室', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/shihole5', False),
]
shiroom19=Room('xiakedao/shiroom19', u'石室', None, 0, exits)

exits = [
	Exit('east', 'xiakedao/shihole5', False),
]
shiroom20=Room('xiakedao/shiroom20', u'石室', None, 0, exits)

exits = [
	Exit('south', 'xiakedao/shihole6', False),
]
shiroom21=Room('xiakedao/shiroom21', u'石室', None, 0, exits)

exits = [
	Exit('north', 'xiakedao/shihole6', False),
]
shiroom22=Room('xiakedao/shiroom22', u'石室', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/shihole6', False),
]
shiroom23=Room('xiakedao/shiroom23', u'石室', None, 0, exits)

exits = [
	Exit('east', 'xiakedao/shihole6', False),
]
shiroom24=Room('xiakedao/shiroom24', u'石室', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/dating', False),
]
shufang=Room('xiakedao/shufang', u'书房', None, 0, exits)

exits = [
	Exit('northdown', 'xiakedao/road8', False),
]
wangyun=Room('xiakedao/wangyun', u'望云台', 'xiakedao', 0, exits)

exits = [
	Exit('west', 'xiakedao/shibi', False),
]
wuchang=Room('xiakedao/wuchang', u'武场', None, 0, exits)

exits = [
	Exit('east', 'xiakedao/dating', False),
]
wuqiku=Room('xiakedao/wuqiku', u'武器库', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/yingbin', False),
]
xiaodian=Room('xiakedao/xiaodian', u'小吃店', None, 0, exits)

exits = [
	Exit('east', 'xiakedao/yingbin', False),
]
xiuxis=Room('xiakedao/xiuxis', u'休息室', None, 0, exits)

exits = [
	Exit('south', 'xiakedao/neiting', False),
]
xiuxis2=Room('xiakedao/xiuxis2', u'休息室', None, 0, exits)

exits = [
	Exit('south', 'xiakedao/xkroad2', False),
	Exit('northup', 'henshan/hsroad9', False),
]
xkroad1=Room('xiakedao/xkroad1', u'南岭山口', 'xiakedao', 0, exits)

exits = [
	Exit('south', 'xiakedao/xkroad3', False),
	Exit('north', 'xiakedao/xkroad1', False),
]
xkroad2=Room('xiakedao/xkroad2', u'佛山', 'xiakedao', 0, exits)

exits = [
	Exit('south', 'xiakedao/xkroad4', False),
	Exit('north', 'foshan/southgate', False),
]
xkroad3=Room('xiakedao/xkroad3', u'平原小路', 'nanhai', 0, exits)

exits = [
	Exit('west', 'xiakedao/haigang', False),
	Exit('south', 'xiakedao/haibin', False),
	Exit('east', 'xiakedao/xkroad5', False),
	Exit('north', 'xiakedao/xkroad3', False),
]
xkroad4=Room('xiakedao/xkroad4', u'南海渔村', 'nanhai', 0, exits)

exits = [
	Exit('west', 'xiakedao/xkroad4', False),
	Exit('north', 'xiakedao/xkroad6', False),
]
xkroad5=Room('xiakedao/xkroad5', u'渔村晒网场', 'nanhai', 0, exits)

exits = [
	Exit('south', 'xiakedao/xkroad5', False),
]
xkroad6=Room('xiakedao/xkroad6', u'渔村小屋', None, 0, exits)

exits = [
]
yadi=Room('xiakedao/yadi', u'崖底', None, 0, exits)

exits = [
	Exit('out', 'xiakedao/dongmen', False),
	Exit('west', 'xiakedao/xiuxis', False),
	Exit('south', 'xiakedao/shidong2', False),
	Exit('east', 'xiakedao/xiaodian', False),
]
yingbin=Room('xiakedao/yingbin', u'迎宾馆', None, 0, exits)

exits = [
	Exit('south', 'xiakedao/yongdao2', False),
	Exit('north', 'xiakedao/pubu', False),
]
yongdao1=Room('xiakedao/yongdao1', u'甬道', None, 0, exits)

exits = [
	Exit('south', 'xiakedao/shidong1', False),
	Exit('north', 'xiakedao/yongdao1', False),
]
yongdao2=Room('xiakedao/yongdao2', u'甬道', None, 0, exits)

exits = [
	Exit('south', 'xiakedao/shimen', False),
	Exit('north', 'xiakedao/dating', False),
]
yongdao3=Room('xiakedao/yongdao3', u'甬道', None, 0, exits)

exits = [
	Exit('west', 'xiakedao/zhuwu2', False),
	Exit('east', 'xiakedao/haibin', False),
]
zhuwu=Room('xiakedao/zhuwu', u'竹屋', 'nanhai', 0, exits)

exits = [
	Exit('east', 'xiakedao/zhuwu', False),
]
zhuwu2=Room('xiakedao/zhuwu2', u'竹屋', None, 0, exits)

