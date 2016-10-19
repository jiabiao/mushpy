# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('southdown', 'henshan/shanlu4', False),
	Exit('northup', 'henshan/shanlu5', False),
]
banshan=Room('henshan/banshan', u'��ɽͤ', 'henshan', 0, exits)

exits = [
	Exit('northup', 'henshan/shanlu1', False),
	Exit('south', 'henshan/houdian', False),
]
beimen=Room('henshan/beimen', u'������', 'henshan', 0, exits)

exits = [
	Exit('south', 'henshan/shuzhuangtai', False),
	Exit('east', 'henshan/shanlu14', False),
]
cangjingdian=Room('henshan/cangjingdian', u'�ؾ���', None, 0, exits)

exits = [
	Exit('north', 'henshan/hengyang', False),
]
chaguan=Room('henshan/chaguan', u'�������', None, 0, exits)

exits = [
	Exit('west', 'henshan/hsroad6', False),
]
chating=Room('henshan/chating', u'��ͤ', 'henshan', 0, exits)

exits = [
	Exit('southdown', 'henshan/shanlu2', False),
	Exit('eastdown', 'henshan/shanlu11', False),
	Exit('northdown', 'henshan/shanlu3', False),
]
chidifeng=Room('henshan/chidifeng', u'��۷�', 'henshan', 0, exits)

exits = [
	Exit('south', 'henshan/yushulou', False),
	Exit('north', 'henshan/houdian', False),
]
dadian=Room('henshan/dadian', u'���', None, 0, exits)

exits = [
	Exit('northdown', 'henshan/nantian', False),
]
denggaotai=Room('henshan/denggaotai', u'�Ǹ�̨', 'henshan', 0, exits)

exits = [
	Exit('southdown', 'henshan/shanjian', False),
	Exit('eastup', 'henshan/shanlu10', False),
]
fangguangsi=Room('henshan/fangguangsi', u'������', 'henshan', 0, exits)

exits = [
	Exit('southdown', 'henshan/shanlu9', False),
	Exit('northdown', 'henshan/shanlu8', False),
	Exit('westup', 'henshan/sansheng', False),
]
fuyansi=Room('henshan/fuyansi', u'������', 'henshan', 0, exits)

exits = [
	Exit('up', 'henshan/shanjian', False),
]
heishatan=Room('henshan/heishatan', u'��ɳ̶', 'henshan', 0, exits)

exits = [
	Exit('west', 'henshan/hengyang1', False),
	Exit('south', 'henshan/chaguan', False),
	Exit('north', 'henshan/lingxingmen', False),
	Exit('east', 'henshan/hsroad3', False),
]
hengyang=Room('henshan/hengyang', u'������', 'hengyang', 0, exits)

exits = [
	Exit('west', 'henshan/hsroad4', False),
	Exit('south', 'henshan/shop', False),
	Exit('southwest', 'henshan/majiu', False),
	Exit('north', 'henshan/liufugate', False),
	Exit('east', 'henshan/hengyang', False),
]
hengyang1=Room('henshan/hengyang1', u'��������', 'hengyang', 0, exits)

exits = [
	Exit('south', 'henshan/dadian', False),
	Exit('north', 'henshan/beimen', False),
]
houdian=Room('henshan/houdian', u'���', None, 0, exits)

exits = [
	Exit('southeast', 'henshan/hsroad2', False),
	Exit('northdown', 'wudang/wdroad4', False),
]
hsroad1=Room('henshan/hsroad1', u'��·', 'hengyang', 0, exits)

exits = [
	Exit('southeast', 'fuzhou/fzroad7', False),
	Exit('northwest', 'henshan/hsroad1', False),
	Exit('southwest', 'henshan/hsroad3', False),
]
hsroad2=Room('henshan/hsroad2', u'��·', 'hengyang', 0, exits)

exits = [
	Exit('west', 'henshan/hengyang', False),
	Exit('northeast', 'henshan/hsroad2', False),
]
hsroad3=Room('henshan/hsroad3', u'��·', 'hengyang', 0, exits)

exits = [
	Exit('west', 'henshan/hsroad5', False),
	Exit('east', 'henshan/hengyang1', False),
]
hsroad4=Room('henshan/hsroad4', u'����·', 'hengyang', 0, exits)

exits = [
	Exit('west', 'motianya/mtroad1', False),
	Exit('southup', 'henshan/hsroad9', False),
	Exit('north', 'henshan/hsroad6', False),
	Exit('east', 'henshan/hsroad4', False),
]
hsroad5=Room('henshan/hsroad5', u'�ּ���', 'hengyang', 0, exits)

exits = [
	Exit('south', 'henshan/hsroad5', False),
	Exit('north', 'henshan/hsroad7', False),
	Exit('east', 'henshan/chating', False),
]
hsroad6=Room('henshan/hsroad6', u'�ּ���', 'hengyang', 0, exits)

exits = [
	Exit('south', 'henshan/hsroad6', False),
	Exit('north', 'henshan/hsroad8', False),
]
hsroad7=Room('henshan/hsroad7', u'�ּ���', 'hengyang', 0, exits)

exits = [
	Exit('northwest', 'wudang/wdroad9', False),
	Exit('south', 'henshan/hsroad7', False),
]
hsroad8=Room('henshan/hsroad8', u'�ּ��', 'hengyang', 0, exits)

exits = [
	Exit('southdown', 'foshan/nanling', False),
	Exit('northdown', 'henshan/hsroad5', False),
]
hsroad9=Room('henshan/hsroad9', u'����ɽ��', 'hengyang', 0, exits)

exits = [
	Exit('down', 'henshan/shop', False),
]
huiyan=Room('henshan/huiyan', u'����¥', None, 0, exits)

exits = [
	Exit('south', 'henshan/yubeiting', False),
	Exit('north', 'henshan/yushulou', False),
]
jiayingmen=Room('henshan/jiayingmen', u'��Ӧ��', 'henshan', 0, exits)

exits = [
	Exit('northdown', 'henshan/sansheng', False),
]
jigaoming=Room('henshan/jigaoming', u'������̨', 'henshan', 0, exits)

exits = [
	Exit('south', 'henshan/lingxingmen', False),
	Exit('north', 'henshan/zhengchuan', False),
	Exit('east', 'henshan/zhongting', False),
]
kuixingge=Room('henshan/kuixingge', u'���Ǹ�', 'henshan', 0, exits)

exits = [
	Exit('south', 'henshan/hengyang', False),
	Exit('north', 'henshan/kuixingge', False),
]
lingxingmen=Room('henshan/lingxingmen', u'������', 'henshan', 0, exits)

exits = [
	Exit('west', 'henshan/liufuwest', False),
	Exit('south', 'henshan/liufudayuan', False),
	Exit('east', 'henshan/liufueast', False),
]
liufudating=Room('henshan/liufudating', u'��������', None, 0, exits)

exits = [
	Exit('south', 'henshan/liufugate', False),
	Exit('north', 'henshan/liufudating', False),
]
liufudayuan=Room('henshan/liufudayuan', u'������Ժ', None, 0, exits)

exits = [
	Exit('west', 'henshan/liufudating', False),
]
liufueast=Room('henshan/liufueast', u'�������᷿', None, 0, exits)

exits = [
	Exit('south', 'henshan/hengyang1', False),
]
liufugate=Room('henshan/liufugate', u'��������', 'hengyang', 0, exits)

exits = [
	Exit('east', 'henshan/liufudating', False),
]
liufuwest=Room('henshan/liufuwest', u'�������᷿', None, 0, exits)

exits = [
	Exit('westdown', 'henshan/nantian', False),
]
liuyunping=Room('henshan/liuyunping', u'����ƺ', 'henshan', 0, exits)

exits = [
	Exit('northeast', 'henshan/hengyang1', False),
]
majiu=Room('henshan/majiu', u'���', 'henshan', 0, exits)

exits = [
	Exit('southdown', 'henshan/shanlu8', False),
	Exit('northup', 'henshan/shanlu6', False),
	Exit('westup', 'henshan/shanlu7', False),
]
mojingtai=Room('henshan/mojingtai', u'ĥ��̨', 'henshan', 0, exits)

exits = [
	Exit('northdown', 'henshan/shanlu9', False),
]
nantaisi=Room('henshan/nantaisi', u'��̨��', 'henshan', 0, exits)

exits = [
	Exit('northwest', 'henshan/shanlu14', False),
	Exit('southup', 'henshan/denggaotai', False),
	Exit('eastup', 'henshan/liuyunping', False),
	Exit('southwest', 'henshan/shanlu13', False),
	Exit('northeast', 'henshan/shiziyan', False),
]
nantian=Room('henshan/nantian', u'������', 'henshan', 0, exits)

exits = [
	Exit('southup', 'henshan/jigaoming', False),
	Exit('eastdown', 'henshan/fuyansi', False),
]
sansheng=Room('henshan/sansheng', u'������', 'henshan', 0, exits)

exits = [
	Exit('northup', 'henshan/fangguangsi', False),
	Exit('down', 'henshan/heishatan', False),
]
shanjian=Room('henshan/shanjian', u'ɽ��', 'henshan', 0, exits)

exits = [
	Exit('southdown', 'henshan/beimen', False),
	Exit('northwest', 'henshan/shanlu2', False),
]
shanlu1=Room('henshan/shanlu1', u'ɽ·', 'henshan', 0, exits)

exits = [
	Exit('eastup', 'henshan/tianzhu', False),
	Exit('westdown', 'henshan/fangguangsi', False),
]
shanlu10=Room('henshan/shanlu10', u'ɽ·', 'henshan', 0, exits)

exits = [
	Exit('east', 'henshan/shanlu12', False),
	Exit('westup', 'henshan/chidifeng', False),
]
shanlu11=Room('henshan/shanlu11', u'ɽ·', 'henshan', 0, exits)

exits = [
	Exit('west', 'henshan/shanlu11', False),
	Exit('eastup', 'henshan/shuiliandong', False),
]
shanlu12=Room('henshan/shanlu12', u'ɽ·', 'henshan', 0, exits)

exits = [
	Exit('southeast', 'henshan/shanlu5', False),
	Exit('northeast', 'henshan/nantian', False),
]
shanlu13=Room('henshan/shanlu13', u'ɽ·', 'henshan', 0, exits)

exits = [
	Exit('southeast', 'henshan/nantian', False),
	Exit('west', 'henshan/cangjingdian', False),
]
shanlu14=Room('henshan/shanlu14', u'ɽ·', 'henshan', 0, exits)

exits = [
	Exit('southeast', 'henshan/shanlu1', False),
	Exit('northup', 'henshan/chidifeng', False),
]
shanlu2=Room('henshan/shanlu2', u'ɽ·', 'henshan', 0, exits)

exits = [
	Exit('northwest', 'henshan/shanlu4', False),
	Exit('southup', 'henshan/chidifeng', False),
]
shanlu3=Room('henshan/shanlu3', u'ɽ·', 'henshan', 0, exits)

exits = [
	Exit('southeast', 'henshan/shanlu3', False),
	Exit('northup', 'henshan/banshan', False),
]
shanlu4=Room('henshan/shanlu4', u'ɽ·', 'henshan', 0, exits)

exits = [
	Exit('southdown', 'henshan/banshan', False),
	Exit('west', 'henshan/shanlu6', False),
	Exit('northwest', 'henshan/shanlu13', False),
]
shanlu5=Room('henshan/shanlu5', u'ɽ·', 'henshan', 0, exits)

exits = [
	Exit('southdown', 'henshan/mojingtai', False),
	Exit('east', 'henshan/shanlu5', False),
]
shanlu6=Room('henshan/shanlu6', u'ɽ·', 'henshan', 0, exits)

exits = [
	Exit('eastdown', 'henshan/mojingtai', False),
	Exit('westup', 'henshan/tianzhu', False),
]
shanlu7=Room('henshan/shanlu7', u'ɽ·', 'henshan', 0, exits)

exits = [
	Exit('southup', 'henshan/fuyansi', False),
	Exit('northup', 'henshan/mojingtai', False),
]
shanlu8=Room('henshan/shanlu8', u'ɽ·', 'henshan', 0, exits)

exits = [
	Exit('southup', 'henshan/nantaisi', False),
	Exit('northup', 'henshan/fuyansi', False),
]
shanlu9=Room('henshan/shanlu9', u'ɽ·', 'henshan', 0, exits)

exits = [
	Exit('northup', 'henshan/wangritai', False),
	Exit('southwest', 'henshan/nantian', False),
]
shiziyan=Room('henshan/shiziyan', u'ʨ����', 'henshan', 0, exits)

exits = [
	Exit('up', 'henshan/huiyan', False),
	Exit('north', 'henshan/hengyang1', False),
]
shop=Room('henshan/shop', u'С��', None, 0, exits)

exits = [
	Exit('westdown', 'henshan/shanlu12', False),
]
shuiliandong=Room('henshan/shuiliandong', u'ˮ����', 'henshan', 0, exits)

exits = [
	Exit('north', 'henshan/cangjingdian', False),
]
shuzhuangtai=Room('henshan/shuzhuangtai', u'��ױ̨', 'henshan', 0, exits)

exits = [
	Exit('eastdown', 'henshan/shanlu7', False),
	Exit('westdown', 'henshan/shanlu10', False),
]
tianzhu=Room('henshan/tianzhu', u'������', None, 0, exits)

exits = [
	Exit('southdown', 'henshan/shiziyan', False),
	Exit('northup', 'henshan/zhurongdian', False),
]
wangritai=Room('henshan/wangritai', u'����̨', 'henshan', 0, exits)

exits = [
	Exit('southup', 'henshan/zhurongdian', False),
]
wangyuetai=Room('henshan/wangyuetai', u'����̨', 'henshan', 0, exits)

exits = [
	Exit('south', 'henshan/zhengchuan', False),
	Exit('north', 'henshan/jiayingmen', False),
]
yubeiting=Room('henshan/yubeiting', u'����ͤ', None, 0, exits)

exits = [
	Exit('south', 'henshan/jiayingmen', False),
	Exit('north', 'henshan/dadian', False),
]
yushulou=Room('henshan/yushulou', u'����¥', None, 0, exits)

exits = [
	Exit('south', 'henshan/kuixingge', False),
	Exit('north', 'henshan/yubeiting', False),
]
zhengchuan=Room('henshan/zhengchuan', u'������', 'henshan', 0, exits)

exits = [
	Exit('west', 'henshan/kuixingge', False),
]
zhongting=Room('henshan/zhongting', u'��ͤ', None, 0, exits)

exits = [
	Exit('southdown', 'henshan/wangritai', False),
	Exit('northdown', 'henshan/wangyuetai', False),
	Exit('westup', 'henshan/zhurongfeng', False),
]
zhurongdian=Room('henshan/zhurongdian', u'ף�ڵ�', None, 0, exits)

exits = [
	Exit('eastdown', 'henshan/zhurongdian', False),
]
zhurongfeng=Room('henshan/zhurongfeng', u'ף�ڷ�', None, 0, exits)

