# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('west', 'yanziwu/huayuan', False),
	Exit('east', 'yanziwu/tingxiang', False),
]
biheqiao=Room('yanziwu/biheqiao', u'�̺���', 'yanziwu', 0, exits)

exits = [
	Exit('northdown', 'yanziwu/muti', False),
	Exit('east', 'yanziwu/pindi', False),
]
bozhou=Room('yanziwu/bozhou', u'������', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/qiushuan', False),
	Exit('south', 'yanziwu/shuwu', False),
	Exit('north', 'yanziwu/yimen', False),
	Exit('east', 'yanziwu/zuijing', False),
]
canheju=Room('yanziwu/canheju', u'�κϾ�', None, 0, exits)

exits = [
	Exit('west', 'yanziwu/lixiang', False),
	Exit('south', 'yanziwu/huayuan', False),
	Exit('north', 'yanziwu/shijian', False),
	Exit('east', 'yanziwu/huizhen', False),
]
changlang=Room('yanziwu/changlang', u'����', None, 0, exits)

exits = [
	Exit('south', 'yanziwu/lixiang', False),
	Exit('north', 'yanziwu/cuixia', False),
]
chuantang=Room('yanziwu/chuantang', u'����', None, 0, exits)

exits = [
	Exit('north', 'yanziwu/xiaoting', False),
]
chufang=Room('yanziwu/chufang', u'����', None, 0, exits)

exits = [
	Exit('west', 'yanziwu/xiaoting', False),
	Exit('south', 'yanziwu/chuantang', False),
	Exit('east', 'yanziwu/zhulin1', False),
]
cuixia=Room('yanziwu/cuixia', u'��ϼ��', None, 0, exits)

exits = [
	Exit('west', 'yanziwu/yimen', False),
	Exit('east', 'yanziwu/huayuan', False),
]
dannuo=Room('yanziwu/dannuo', u'�Ŵ��', None, 0, exits)

exits = [
]
hu=Room('yanziwu/hu', u'������', 'yanziwu', 0, exits)

exits = [
	Exit('out', 'yanziwu/lanyue', False),
]
huanshi=Room('yanziwu/huanshi', u'��ʩˮ��', None, 0, exits)

exits = [
	Exit('west', 'yanziwu/dannuo', False),
	Exit('south', 'yanziwu/jiashan', False),
	Exit('east', 'yanziwu/biheqiao', False),
	Exit('north', 'yanziwu/changlang', False),
]
huayuan=Room('yanziwu/huayuan', u'��԰', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/changlang', False),
]
huizhen=Room('yanziwu/huizhen', u'����԰', 'yanziwu', 0, exits)

exits = [
	Exit('northeast', 'suzhou/road5', False),
]
hupan=Room('yanziwu/hupan', u'̫������', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/zuijing', False),
	Exit('north', 'yanziwu/huayuan', False),
	Exit('east', 'yanziwu/shuiyun', False),
]
jiashan=Room('yanziwu/jiashan', u'��ɽ', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/shijian', False),
	Exit('east', 'yanziwu/kuxiu2', False),
]
kuxiu=Room('yanziwu/kuxiu', u'���޳�', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/kuxiu', False),
]
kuxiu2=Room('yanziwu/kuxiu2', u'���޳�', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/shuwu', False),
]
lanyue=Room('yanziwu/lanyue', u'���¾�', None, 0, exits)

exits = [
	Exit('west', 'yanziwu/longfeng', False),
	Exit('east', 'yanziwu/changlang', False),
	Exit('north', 'yanziwu/chuantang', False),
]
lixiang=Room('yanziwu/lixiang', u'����Է', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/pindi', False),
	Exit('south', 'yanziwu/yimen', False),
	Exit('east', 'yanziwu/lixiang', False),
]
longfeng=Room('yanziwu/longfeng', u'������', None, 0, exits)

exits = [
	Exit('southup', 'yanziwu/bozhou', False),
	Exit('eastup', 'yanziwu/qinyun', False),
]
muti=Room('yanziwu/muti', u'ľ��', 'yanziwu', 0, exits)

exits = [
]
muzhuang=Room('yanziwu/muzhuang', u'ľ׮', 'yanziwu', 0, exits)

exits = [
	Exit('north', 'yanziwu/qinyun', False),
]
neitang=Room('yanziwu/neitang', u'����', None, 0, exits)

exits = [
	Exit('west', 'yanziwu/bozhou', False),
	Exit('east', 'yanziwu/longfeng', False),
]
pindi=Room('yanziwu/pindi', u'Ʒ��ͥ', None, 0, exits)

exits = [
	Exit('up', 'yanziwu/qinfang2', False),
	Exit('east', 'yanziwu/yimen', False),
]
qinfang1=Room('yanziwu/qinfang1', u'�߷���', None, 0, exits)

exits = [
	Exit('down', 'yanziwu/qinfang1', False),
]
qinfang2=Room('yanziwu/qinfang2', u'�߷������', None, 0, exits)

exits = [
	Exit('south', 'yanziwu/zhulin3', False),
]
qingzong=Room('yanziwu/qingzong', u'��ڣ', 'yanziwu', 0, exits)

exits = [
	Exit('south', 'yanziwu/neitang', False),
	Exit('east', 'yanziwu/xiaoting', False),
	Exit('westdown', 'yanziwu/muti', False),
]
qinyun=Room('yanziwu/qinyun', u'����С��', None, 0, exits)

exits = [
	Exit('east', 'yanziwu/canheju', False),
]
qiushuan=Room('yanziwu/qiushuan', u'��ˬի', None, 0, exits)

exits = [
	Exit('north', 'yanziwu/shuwu', False),
]
shangyu=Room('yanziwu/shangyu', u'����̨', 'yanziwu', 0, exits)

exits = [
	Exit('south', 'yanziwu/changlang', False),
	Exit('east', 'yanziwu/kuxiu', False),
]
shijian=Room('yanziwu/shijian', u'�Խ�̨', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/jiashan', False),
]
shuiyun=Room('yanziwu/shuiyun', u'ˮ����', 'yanziwu', 0, exits)

exits = [
	Exit('south', 'yanziwu/shangyu', False),
	Exit('north', 'yanziwu/canheju', False),
	Exit('east', 'yanziwu/lanyue', False),
]
shuwu=Room('yanziwu/shuwu', u'��ī����', None, 0, exits)

exits = [
]
taihu=Room('yanziwu/taihu', u'̫��', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/biheqiao', False),
]
tingxiang=Room('yanziwu/tingxiang', u'����ˮ�', None, 0, exits)

exits = [
	Exit('south', 'yanziwu/xiaoqiao', False),
]
tingyu=Room('yanziwu/tingyu', u'�����', None, 0, exits)

exits = [
	Exit('west', 'yanziwu/xiaoqiao', False),
	Exit('south', 'yanziwu/xiaoting', False),
]
xiaojing=Room('yanziwu/xiaojing', u'С��', 'yanziwu', 0, exits)

exits = [
	Exit('east', 'yanziwu/xiaojing', False),
	Exit('north', 'yanziwu/tingyu', False),
]
xiaoqiao=Room('yanziwu/xiaoqiao', u'������', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/qinyun', False),
	Exit('south', 'yanziwu/chufang', False),
	Exit('north', 'yanziwu/xiaojing', False),
	Exit('east', 'yanziwu/cuixia', False),
]
xiaoting=Room('yanziwu/xiaoting', u'������', None, 0, exits)

exits = [
]
xiaozhou=Room('yanziwu/xiaozhou', u'С��', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/qinfang1', False),
	Exit('south', 'yanziwu/canheju', False),
	Exit('north', 'yanziwu/longfeng', False),
	Exit('east', 'yanziwu/dannuo', False),
]
yimen=Room('yanziwu/yimen', u'����', None, 0, exits)

exits = [
	Exit('west', 'yanziwu/cuixia', False),
	Exit('south', 'yanziwu/zhulin4', False),
	Exit('north', 'yanziwu/zhulin4', False),
	Exit('east', 'yanziwu/zhulin2', False),
]
zhulin1=Room('yanziwu/zhulin1', u'����', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/zhulin1', False),
	Exit('south', 'yanziwu/zhulin2', False),
	Exit('north', 'yanziwu/zhulin3', False),
	Exit('east', 'yanziwu/zhulin1', False),
]
zhulin2=Room('yanziwu/zhulin2', u'����', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/zhulin4', False),
	Exit('south', 'yanziwu/zhulin2', False),
	Exit('north', 'yanziwu/qingzong', False),
	Exit('east', 'yanziwu/zhulin3', False),
]
zhulin3=Room('yanziwu/zhulin3', u'����', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/zhulin4', False),
	Exit('south', 'yanziwu/zhulin1', False),
	Exit('north', 'yanziwu/zhulin1', False),
	Exit('east', 'yanziwu/zhulin3', False),
]
zhulin4=Room('yanziwu/zhulin4', u'����', 'yanziwu', 0, exits)

exits = [
	Exit('west', 'yanziwu/canheju', False),
	Exit('east', 'yanziwu/jiashan', False),
]
zuijing=Room('yanziwu/zuijing', u'׺��¥', None, 0, exits)

exits = [
	Exit('down', 'yanziwu/zuijing', False),
]
zuijing2=Room('yanziwu/zuijing2', u'׺��¥����', None, 0, exits)

