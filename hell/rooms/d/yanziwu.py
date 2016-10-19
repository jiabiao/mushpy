# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('west', 'yanziwu/huayuan', False),
	Exit('east', 'yanziwu/tingxiang', False),
]
biheqiao=Room('yanziwu/biheqiao', u'碧荷桥', 'yanziwu', 0, exits)

exits = [
	Exit('northdown', 'yanziwu/muti', False),
	Exit('east', 'yanziwu/pindi', False),
]
bozhou=Room('yanziwu/bozhou', u'泊舟坞', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/qiushuan', False),
	Exit('south', 'yanziwu/shuwu', False),
	Exit('north', 'yanziwu/yimen', False),
	Exit('east', 'yanziwu/zuijing', False),
]
canheju=Room('yanziwu/canheju', u'参合居', None, 0, exits)

exits = [
	Exit('west', 'yanziwu/lixiang', False),
	Exit('south', 'yanziwu/huayuan', False),
	Exit('north', 'yanziwu/shijian', False),
	Exit('east', 'yanziwu/huizhen', False),
]
changlang=Room('yanziwu/changlang', u'长廊', None, 0, exits)

exits = [
	Exit('south', 'yanziwu/lixiang', False),
	Exit('north', 'yanziwu/cuixia', False),
]
chuantang=Room('yanziwu/chuantang', u'穿堂', None, 0, exits)

exits = [
	Exit('north', 'yanziwu/xiaoting', False),
]
chufang=Room('yanziwu/chufang', u'厨房', None, 0, exits)

exits = [
	Exit('west', 'yanziwu/xiaoting', False),
	Exit('south', 'yanziwu/chuantang', False),
	Exit('east', 'yanziwu/zhulin1', False),
]
cuixia=Room('yanziwu/cuixia', u'翠霞堂', None, 0, exits)

exits = [
	Exit('west', 'yanziwu/yimen', False),
	Exit('east', 'yanziwu/huayuan', False),
]
dannuo=Room('yanziwu/dannuo', u'啖糯厅', None, 0, exits)

exits = [
]
hu=Room('yanziwu/hu', u'百曲湖', 'yanziwu', 0, exits)

exits = [
	Exit('out', 'yanziwu/lanyue', False),
]
huanshi=Room('yanziwu/huanshi', u'还施水阁', None, 0, exits)

exits = [
	Exit('west', 'yanziwu/dannuo', False),
	Exit('south', 'yanziwu/jiashan', False),
	Exit('east', 'yanziwu/biheqiao', False),
	Exit('north', 'yanziwu/changlang', False),
]
huayuan=Room('yanziwu/huayuan', u'花园', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/changlang', False),
]
huizhen=Room('yanziwu/huizhen', u'汇珍园', 'yanziwu', 0, exits)

exits = [
	Exit('northeast', 'suzhou/road5', False),
]
hupan=Room('yanziwu/hupan', u'太湖湖畔', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/zuijing', False),
	Exit('north', 'yanziwu/huayuan', False),
	Exit('east', 'yanziwu/shuiyun', False),
]
jiashan=Room('yanziwu/jiashan', u'假山', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/shijian', False),
	Exit('east', 'yanziwu/kuxiu2', False),
]
kuxiu=Room('yanziwu/kuxiu', u'苦修场', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/kuxiu', False),
]
kuxiu2=Room('yanziwu/kuxiu2', u'苦修场', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/shuwu', False),
]
lanyue=Room('yanziwu/lanyue', u'揽月居', None, 0, exits)

exits = [
	Exit('west', 'yanziwu/longfeng', False),
	Exit('east', 'yanziwu/changlang', False),
	Exit('north', 'yanziwu/chuantang', False),
]
lixiang=Room('yanziwu/lixiang', u'梨香苑', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/pindi', False),
	Exit('south', 'yanziwu/yimen', False),
	Exit('east', 'yanziwu/lixiang', False),
]
longfeng=Room('yanziwu/longfeng', u'龙凤厅', None, 0, exits)

exits = [
	Exit('southup', 'yanziwu/bozhou', False),
	Exit('eastup', 'yanziwu/qinyun', False),
]
muti=Room('yanziwu/muti', u'木梯', 'yanziwu', 0, exits)

exits = [
]
muzhuang=Room('yanziwu/muzhuang', u'木桩', 'yanziwu', 0, exits)

exits = [
	Exit('north', 'yanziwu/qinyun', False),
]
neitang=Room('yanziwu/neitang', u'内堂', None, 0, exits)

exits = [
	Exit('west', 'yanziwu/bozhou', False),
	Exit('east', 'yanziwu/longfeng', False),
]
pindi=Room('yanziwu/pindi', u'品笛庭', None, 0, exits)

exits = [
	Exit('up', 'yanziwu/qinfang2', False),
	Exit('east', 'yanziwu/yimen', False),
]
qinfang1=Room('yanziwu/qinfang1', u'沁芳阁', None, 0, exits)

exits = [
	Exit('down', 'yanziwu/qinfang1', False),
]
qinfang2=Room('yanziwu/qinfang2', u'沁芳阁二层', None, 0, exits)

exits = [
	Exit('south', 'yanziwu/zhulin3', False),
]
qingzong=Room('yanziwu/qingzong', u'青冢', 'yanziwu', 0, exits)

exits = [
	Exit('south', 'yanziwu/neitang', False),
	Exit('east', 'yanziwu/xiaoting', False),
	Exit('westdown', 'yanziwu/muti', False),
]
qinyun=Room('yanziwu/qinyun', u'琴韵小筑', None, 0, exits)

exits = [
	Exit('east', 'yanziwu/canheju', False),
]
qiushuan=Room('yanziwu/qiushuan', u'秋爽斋', None, 0, exits)

exits = [
	Exit('north', 'yanziwu/shuwu', False),
]
shangyu=Room('yanziwu/shangyu', u'赏鱼台', 'yanziwu', 0, exits)

exits = [
	Exit('south', 'yanziwu/changlang', False),
	Exit('east', 'yanziwu/kuxiu', False),
]
shijian=Room('yanziwu/shijian', u'试剑台', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/jiashan', False),
]
shuiyun=Room('yanziwu/shuiyun', u'水云轩', 'yanziwu', 0, exits)

exits = [
	Exit('south', 'yanziwu/shangyu', False),
	Exit('north', 'yanziwu/canheju', False),
	Exit('east', 'yanziwu/lanyue', False),
]
shuwu=Room('yanziwu/shuwu', u'翰墨书屋', None, 0, exits)

exits = [
]
taihu=Room('yanziwu/taihu', u'太湖', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/biheqiao', False),
]
tingxiang=Room('yanziwu/tingxiang', u'听香水榭', None, 0, exits)

exits = [
	Exit('south', 'yanziwu/xiaoqiao', False),
]
tingyu=Room('yanziwu/tingyu', u'听雨居', None, 0, exits)

exits = [
	Exit('west', 'yanziwu/xiaoqiao', False),
	Exit('south', 'yanziwu/xiaoting', False),
]
xiaojing=Room('yanziwu/xiaojing', u'小径', 'yanziwu', 0, exits)

exits = [
	Exit('east', 'yanziwu/xiaojing', False),
	Exit('north', 'yanziwu/tingyu', False),
]
xiaoqiao=Room('yanziwu/xiaoqiao', u'紫菱桥', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/qinyun', False),
	Exit('south', 'yanziwu/chufang', False),
	Exit('north', 'yanziwu/xiaojing', False),
	Exit('east', 'yanziwu/cuixia', False),
]
xiaoting=Room('yanziwu/xiaoting', u'晓寒厅', None, 0, exits)

exits = [
]
xiaozhou=Room('yanziwu/xiaozhou', u'小舟', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/qinfang1', False),
	Exit('south', 'yanziwu/canheju', False),
	Exit('north', 'yanziwu/longfeng', False),
	Exit('east', 'yanziwu/dannuo', False),
]
yimen=Room('yanziwu/yimen', u'仪门', None, 0, exits)

exits = [
	Exit('west', 'yanziwu/cuixia', False),
	Exit('south', 'yanziwu/zhulin4', False),
	Exit('north', 'yanziwu/zhulin4', False),
	Exit('east', 'yanziwu/zhulin2', False),
]
zhulin1=Room('yanziwu/zhulin1', u'竹林', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/zhulin1', False),
	Exit('south', 'yanziwu/zhulin2', False),
	Exit('north', 'yanziwu/zhulin3', False),
	Exit('east', 'yanziwu/zhulin1', False),
]
zhulin2=Room('yanziwu/zhulin2', u'竹林', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/zhulin4', False),
	Exit('south', 'yanziwu/zhulin2', False),
	Exit('north', 'yanziwu/qingzong', False),
	Exit('east', 'yanziwu/zhulin3', False),
]
zhulin3=Room('yanziwu/zhulin3', u'竹林', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/zhulin4', False),
	Exit('south', 'yanziwu/zhulin1', False),
	Exit('north', 'yanziwu/zhulin1', False),
	Exit('east', 'yanziwu/zhulin3', False),
]
zhulin4=Room('yanziwu/zhulin4', u'竹林', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/canheju', False),
	Exit('east', 'yanziwu/jiashan', False),
]
zuijing=Room('yanziwu/zuijing', u'缀锦楼', None, 0, exits)

exits = [
	Exit('down', 'yanziwu/zuijing', False),
]
zuijing2=Room('yanziwu/zuijing2', u'缀锦楼二层', None, 0, exits)

