# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('eastup', 'huashan/pingxinshi', False),
	Exit('northdown', 'huashan/qianchi', False),
]
baichi=Room('huashan/baichi', u'百尺峡', 'xx', 0, exits)

exits = [
	Exit('west', 'huashan/square', False),
]
bingqifang=Room('huashan/bingqifang', u'兵器房', None, 0, exits)

exits = [
	Exit('west', 'huashan/garden', False),
	Exit('south', 'huashan/qunxianguan', False),
	Exit('east', 'huashan/buwei3', False),
	Exit('north', 'huashan/buwei2', False),
]
buwei1=Room('huashan/buwei1', u'有所不为轩', None, 0, exits)

exits = [
	Exit('south', 'huashan/buwei1', False),
]
buwei2=Room('huashan/buwei2', u'寝室', None, 0, exits)

exits = [
	Exit('west', 'huashan/buwei1', False),
]
buwei3=Room('huashan/buwei3', u'偏厅', None, 0, exits)

exits = [
	Exit('northup', 'huashan/yuntai', False),
	Exit('eastdown', 'huashan/shangtianti', False),
	Exit('westup', 'huashan/sheshen', False),
]
canglong=Room('huashan/canglong', u'苍龙岭', 'xx', 0, exits)

exits = [
	Exit('west', 'huashan/jushi', False),
	Exit('south', 'huashan/garden', False),
	Exit('north', 'huashan/songlin1', False),
]
changlang=Room('huashan/changlang', u'长廊', None, 0, exits)

exits = [
	Exit('southeast', 'huashan/square', False),
	Exit('northeast', 'huashan/chaopath2', False),
]
chaopath1=Room('huashan/chaopath1', u'朝阳峰小路', 'xx', 0, exits)

exits = [
	Exit('eastup', 'huashan/chaoyang', False),
	Exit('southwest', 'huashan/chaopath1', False),
	Exit('westup', 'huashan/ziqitai', False),
]
chaopath2=Room('huashan/chaopath2', u'朝阳峰小路', 'xx', 0, exits)

exits = [
	Exit('westdown', 'huashan/chaopath2', False),
]
chaoyang=Room('huashan/chaoyang', u'朝阳峰', 'xx', 0, exits)

exits = [
	Exit('eastdown', 'huashan/lianpath2', False),
	Exit('westup', 'huashan/lianhua', False),
]
chengxiang=Room('huashan/chengxiang', u'沉香劈山处', 'xx', 0, exits)

exits = [
	Exit('east', 'huashan/garden', False),
]
chufang=Room('huashan/chufang', u'厨房', None, 1, exits)

exits = [
	Exit('east', 'huashan/road1', False),
]
doctorroom=Room('huashan/doctorroom', u'郎中家', 'huashan', 0, exits)

exits = [
	Exit('west', 'huashan/chufang', False),
	Exit('south', 'huashan/shufang', False),
	Exit('southwest', 'huashan/houyuan', False),
	Exit('north', 'huashan/changlang', False),
	Exit('east', 'huashan/buwei1', False),
]
garden=Room('huashan/garden', u'花园', 'xx', 0, exits)

exits = [
	Exit('west', 'huashan/jiashan', False),
	Exit('east', 'huashan/xuanya', False),
	Exit('northeast', 'huashan/garden', False),
]
houyuan=Room('huashan/houyuan', u'后院', 'xx', 0, exits)

exits = [
	Exit('eastup', 'huashan/qianchi', False),
	Exit('westdown', 'huashan/qingke', False),
]
huixinshi=Room('huashan/huixinshi', u'回心石', 'xx', 0, exits)

exits = [
	Exit('southup', 'huashan/shangtianti', False),
	Exit('northdown', 'huashan/laojun', False),
]
husun=Room('huashan/husun', u'猢狲愁', 'xx', 0, exits)

exits = [
	Exit('east', 'huashan/houyuan', False),
]
jiashan=Room('huashan/jiashan', u'假山小池', 'xx', 0, exits)

exits = [
	Exit('southup', 'huashan/zhenyue', False),
	Exit('northdown', 'huashan/shangtianti', False),
]
jinsuo=Room('huashan/jinsuo', u'金锁关', 'huashan', 0, exits)

exits = [
	Exit('east', 'huashan/changlang', False),
]
jushi=Room('huashan/jushi', u'居室', None, 0, exits)

exits = [
	Exit('southwest', 'village/hsroad2', False),
	Exit('east', 'huashan/jzroad2', False),
]
jzroad1=Room('huashan/jzroad1', u'松树林', 'huashan', 0, exits)

exits = [
	Exit('west', 'huashan/jzroad1', False),
	Exit('east', 'huashan/jzroad3', False),
]
jzroad2=Room('huashan/jzroad2', u'松树林', 'huashan', 0, exits)

exits = [
	Exit('west', 'huashan/jzroad2', False),
	Exit('eastup', 'huashan/jzroad4', False),
]
jzroad3=Room('huashan/jzroad3', u'中条山脚', 'huashan', 0, exits)

exits = [
	Exit('southup', 'huashan/jzroad5', False),
	Exit('westdown', 'huashan/jzroad3', False),
]
jzroad4=Room('huashan/jzroad4', u'中条山森林', 'huashan', 0, exits)

exits = [
	Exit('northdown', 'huashan/jzroad4', False),
]
jzroad5=Room('huashan/jzroad5', u'中条山密林', None, 0, exits)

exits = [
	Exit('westup', 'huashan/jzroad7', False),
	Exit('enter', 'huashan/jzroad5', False),
]
jzroad6=Room('huashan/jzroad6', u'树林外', None, 0, exits)

exits = [
	Exit('southup', 'huashan/shangu', False),
	Exit('eastdown', 'huashan/jzroad6', False),
]
jzroad7=Room('huashan/jzroad7', u'峭壁', 'xx', 0, exits)

exits = [
	Exit('east', 'huashan/songlin4', False),
]
kuihua_1=Room('huashan/kuihua_1', u'山崖', None, 0, exits)

exits = [
]
kuihua_2=Room('huashan/kuihua_2', u'山崖', 'huashan', 0, exits)

exits = [
	Exit('southup', 'huashan/husun', False),
	Exit('westdown', 'huashan/pingxinshi', False),
]
laojun=Room('huashan/laojun', u'老君沟', 'xx', 0, exits)

exits = [
	Exit('eastdown', 'huashan/chengxiang', False),
]
lianhua=Room('huashan/lianhua', u'莲花峰', 'huashan', 0, exits)

exits = [
	Exit('northeast', 'huashan/zhenyue', False),
	Exit('westup', 'huashan/lianpath2', False),
]
lianpath1=Room('huashan/lianpath1', u'莲花峰小路', 'xx', 0, exits)

exits = [
	Exit('eastdown', 'huashan/lianpath1', False),
	Exit('westup', 'huashan/chengxiang', False),
]
lianpath2=Room('huashan/lianpath2', u'莲花峰小路', 'xx', 0, exits)

exits = [
	Exit('northdown', 'huashan/zhandao', False),
]
luoyan=Room('huashan/luoyan', u'落雁峰', 'huashan', 0, exits)

exits = [
	Exit('west', 'huashan/xiaowu', False),
]
neishi=Room('huashan/neishi', u'内室', None, 0, exits)

exits = [
	Exit('southeast', 'huashan/shaluo', False),
	Exit('west', 'village/eexit', False),
	Exit('north', 'huashan/yuquan', False),
]
path1=Room('huashan/path1', u'华山脚下', 'xx', 0, exits)

exits = [
	Exit('east', 'huashan/xiaowu', False),
	Exit('north', 'huashan/shangu', False),
]
pingdi=Room('huashan/pingdi', u'山间平地', 'xx', 0, exits)

exits = [
	Exit('eastup', 'huashan/laojun', False),
	Exit('westdown', 'huashan/baichi', False),
]
pingxinshi=Room('huashan/pingxinshi', u'平心石', 'xx', 0, exits)

exits = [
	Exit('southup', 'huashan/baichi', False),
	Exit('westdown', 'huashan/huixinshi', False),
]
qianchi=Room('huashan/qianchi', u'千尺幢', 'xx', 0, exits)

exits = [
	Exit('eastup', 'huashan/huixinshi', False),
	Exit('northdown', 'huashan/yunmen', False),
]
qingke=Room('huashan/qingke', u'青柯坪', 'xx', 0, exits)

exits = [
	Exit('south', 'huashan/square', False),
	Exit('north', 'huashan/buwei1', False),
]
qunxianguan=Room('huashan/qunxianguan', u'群仙观', None, 0, exits)

exits = [
	Exit('out', 'huashan/sgyhole1', False),
	Exit('southup', 'huashan/zhandao', False),
]
sgyhole=Room('huashan/sgyhole', u'山洞', None, 0, exits)

exits = [
	Exit('out', 'huashan/siguoya', False),
]
sgyhole1=Room('huashan/sgyhole1', u'山洞', None, 0, exits)

exits = [
	Exit('southup', 'huashan/yunmen', False),
	Exit('northwest', 'huashan/path1', False),
	Exit('northeast', 'huashan/shanhongpb', False),
]
shaluo=Room('huashan/shaluo', u'莎萝坪', 'xx', 0, exits)

exits = [
	Exit('out', 'huashan/shanhongpb', False),
]
shandong=Room('huashan/shandong', u'山洞', None, 0, exits)

exits = [
	Exit('southup', 'huashan/jinsuo', False),
	Exit('northdown', 'huashan/husun', False),
	Exit('westup', 'huashan/canglong', False),
]
shangtianti=Room('huashan/shangtianti', u'上天梯', 'huashan', 0, exits)

exits = [
	Exit('south', 'huashan/pingdi', False),
	Exit('northdown', 'huashan/jzroad7', False),
]
shangu=Room('huashan/shangu', u'山谷', 'xx', 0, exits)

exits = [
	Exit('southwest', 'huashan/shaluo', False),
]
shanhongpb=Room('huashan/shanhongpb', u'山洪瀑布', 'huashan', 0, exits)

exits = [
	Exit('eastdown', 'huashan/canglong', False),
]
sheshen=Room('huashan/sheshen', u'舍身崖', 'xx', 0, exits)

exits = [
	Exit('east', 'huashan/square', False),
]
shop=Room('huashan/shop', u'山顶小店', None, 0, exits)

exits = [
	Exit('north', 'huashan/garden', False),
]
shufang=Room('huashan/shufang', u'华山书房', None, 0, exits)

exits = [
	Exit('northdown', 'huashan/yunupath2', False),
	Exit('enter', 'huashan/sgyhole1', False),
]
siguoya=Room('huashan/siguoya', u'思过崖', 'huashan', 0, exits)

exits = [
	Exit('west', 'huashan/songlin1', False),
	Exit('south', 'huashan/changlang', False),
	Exit('east', 'huashan/songlin2', False),
	Exit('north', 'huashan/songlin2', False),
]
songlin1=Room('huashan/songlin1', u'松树林', 'huashan', 0, exits)

exits = [
	Exit('west', 'huashan/songlin3', False),
	Exit('south', 'huashan/songlin3', False),
	Exit('east', 'huashan/songlin4', False),
	Exit('north', 'huashan/songlin3', False),
]
songlin2=Room('huashan/songlin2', u'松树林', 'huashan', 0, exits)

exits = [
	Exit('west', 'huashan/songlin3', False),
	Exit('south', 'huashan/songlin3', False),
	Exit('east', 'huashan/songlin3', False),
	Exit('north', 'huashan/songlin4', False),
]
songlin3=Room('huashan/songlin3', u'松树林', 'huashan', 0, exits)

exits = [
	Exit('west', 'huashan/songlin2', False),
	Exit('south', 'huashan/songlin1', False),
	Exit('east', 'huashan/songlin3', False),
	Exit('north', 'huashan/songlin1', False),
]
songlin4=Room('huashan/songlin4', u'松树林', 'huashan', 0, exits)

exits = [
	Exit('west', 'huashan/shop', False),
	Exit('northwest', 'huashan/chaopath1', False),
	Exit('south', 'huashan/yunu', False),
	Exit('east', 'huashan/bingqifang', False),
	Exit('north', 'huashan/qunxianguan', False),
	Exit('northeast', 'huashan/wuchang1', False),
]
square=Room('huashan/square', u'广场', 'huashan', 0, exits)

exits = [
	Exit('southwest', 'huashan/square', False),
	Exit('east', 'huashan/wuchang3', False),
	Exit('north', 'huashan/wuchang2', False),
]
wuchang1=Room('huashan/wuchang1', u'南练武场', 'huashan', 0, exits)

exits = [
	Exit('south', 'huashan/wuchang1', False),
]
wuchang2=Room('huashan/wuchang2', u'北练武场', 'huashan', 0, exits)

exits = [
	Exit('west', 'huashan/wuchang1', False),
]
wuchang3=Room('huashan/wuchang3', u'东练武场', 'huashan', 0, exits)

exits = [
	Exit('southwest', 'huashan/yunu', False),
	Exit('northeast', 'huashan/xiaolu2', False),
]
xiaolu1=Room('huashan/xiaolu1', u'小山路', 'xx', 0, exits)

exits = [
	Exit('southwest', 'huashan/xiaolu1', False),
]
xiaolu2=Room('huashan/xiaolu2', u'小山路', 'huashan', 0, exits)

exits = [
	Exit('west', 'huashan/pingdi', False),
	Exit('east', 'huashan/neishi', False),
]
xiaowu=Room('huashan/xiaowu', u'林间小屋', None, 0, exits)

exits = [
]
xiuxishi=Room('huashan/xiuxishi', u'华山小筑', None, 0, exits)

exits = [
	Exit('west', 'huashan/houyuan', False),
]
xuanya=Room('huashan/xuanya', u'悬崖', 'xx', 0, exits)

exits = [
	Exit('southup', 'huashan/qingke', False),
	Exit('northdown', 'huashan/shaluo', False),
]
yunmen=Room('huashan/yunmen', u'云门', 'xx', 0, exits)

exits = [
	Exit('southdown', 'huashan/canglong', False),
]
yuntai=Room('huashan/yuntai', u'云台峰', 'huashan', 0, exits)

exits = [
	Exit('southdown', 'huashan/yunupath1', False),
	Exit('west', 'huashan/yunuci', False),
	Exit('northeast', 'huashan/xiaolu1', False),
	Exit('north', 'huashan/square', False),
	Exit('westdown', 'huashan/zhenyue', False),
]
yunu=Room('huashan/yunu', u'玉女峰', 'xx', 0, exits)

exits = [
	Exit('east', 'huashan/yunu', False),
]
yunuci=Room('huashan/yunuci', u'玉女祠', 'huashan', 0, exits)

exits = [
	Exit('southup', 'huashan/yunupath2', False),
	Exit('northup', 'huashan/yunu', False),
]
yunupath1=Room('huashan/yunupath1', u'玉女峰山路', 'xx', 0, exits)

exits = [
	Exit('southup', 'huashan/siguoya', False),
	Exit('northdown', 'huashan/yunupath1', False),
]
yunupath2=Room('huashan/yunupath2', u'玉女峰山路', 'xx', 0, exits)

exits = [
	Exit('south', 'huashan/path1', False),
]
yuquan=Room('huashan/yuquan', u'玉泉院', None, 0, exits)

exits = [
	Exit('southup', 'huashan/luoyan', False),
	Exit('northdown', 'huashan/sgyhole', False),
]
zhandao=Room('huashan/zhandao', u'长空栈道', 'huashan', 0, exits)

exits = [
	Exit('eastup', 'huashan/yunu', False),
	Exit('southwest', 'huashan/lianpath1', False),
	Exit('northdown', 'huashan/jinsuo', False),
]
zhenyue=Room('huashan/zhenyue', u'镇岳宫', 'huashan', 0, exits)

exits = [
	Exit('eastdown', 'huashan/chaopath2', False),
]
ziqitai=Room('huashan/ziqitai', u'紫气台', 'xx', 0, exits)

