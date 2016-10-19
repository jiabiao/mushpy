# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('southdown', 'quanzhen/cuipinggu', False),
	Exit('northup', 'quanzhen/baishulin3', False),
	Exit('east', 'quanzhen/baishulin2', False),
]
baishulin1=Room('quanzhen/baishulin1', u'������', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/baishulin1', False),
	Exit('northup', 'quanzhen/baishulin4', False),
]
baishulin2=Room('quanzhen/baishulin2', u'������', 'quanzhen', 0, exits)

exits = [
	Exit('southdown', 'quanzhen/baishulin1', False),
	Exit('northup', 'quanzhen/cuipingfeng', False),
	Exit('east', 'quanzhen/baishulin4', False),
]
baishulin3=Room('quanzhen/baishulin3', u'������', 'quanzhen', 0, exits)

exits = [
	Exit('southdown', 'quanzhen/baishulin2', False),
	Exit('west', 'quanzhen/baishulin3', False),
]
baishulin4=Room('quanzhen/baishulin4', u'������', 'quanzhen', 0, exits)

exits = [
	Exit('southdown', 'quanzhen/shijie5', False),
]
banshanting=Room('quanzhen/banshanting', u'��ɽͤ', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/minju1', False),
	Exit('south', 'quanzhen/zhongxin', False),
	Exit('north', 'quanzhen/jiulou1', False),
]
beijie=Room('quanzhen/beijie', u'����', 'wugong', 0, exits)

exits = [
	Exit('west', 'quanzhen/huizhentang', False),
	Exit('south', 'quanzhen/datang2', False),
	Exit('north', 'quanzhen/shiweishi', False),
	Exit('east', 'quanzhen/guozhendian', False),
]
cetang=Room('quanzhen/cetang', u'����', None, 0, exits)

exits = [
	Exit('east', 'quanzhen/chanfang2', False),
]
chanfang1=Room('quanzhen/chanfang1', u'����', None, 0, exits)

exits = [
	Exit('west', 'quanzhen/chanfang1', False),
	Exit('south', 'quanzhen/liangong', False),
	Exit('east', 'quanzhen/chanfang3', False),
]
chanfang2=Room('quanzhen/chanfang2', u'����', None, 0, exits)

exits = [
	Exit('west', 'quanzhen/chanfang2', False),
	Exit('east', 'quanzhen/xiaohuayuan2', False),
]
chanfang3=Room('quanzhen/chanfang3', u'����', None, 0, exits)

exits = [
	Exit('west', 'quanzhen/shantang', False),
]
chufang=Room('quanzhen/chufang', u'����', None, 0, exits)

exits = [
	Exit('southdown', 'quanzhen/baishulin3', False),
]
cuipingfeng=Room('quanzhen/cuipingfeng', u'�����嶥', 'quanzhen', 0, exits)

exits = [
	Exit('southdown', 'quanzhen/shanlu3', False),
	Exit('northup', 'quanzhen/baishulin1', False),
]
cuipinggu=Room('quanzhen/cuipinggu', u'������', 'quanzhen', 0, exits)

exits = [
	Exit('northup', 'quanzhen/cundaota2', False),
	Exit('south', 'quanzhen/guozhendian', False),
]
cundaota1=Room('quanzhen/cundaota1', u'�����һ��', None, 0, exits)

exits = [
	Exit('southdown', 'quanzhen/cundaota1', False),
	Exit('northup', 'quanzhen/cundaota3', False),
]
cundaota2=Room('quanzhen/cundaota2', u'���������', None, 0, exits)

exits = [
	Exit('southdown', 'quanzhen/cundaota2', False),
	Exit('northup', 'quanzhen/cundaota4', False),
]
cundaota3=Room('quanzhen/cundaota3', u'���������', None, 0, exits)

exits = [
	Exit('southdown', 'quanzhen/cundaota3', False),
]
cundaota4=Room('quanzhen/cundaota4', u'�������', None, 0, exits)

exits = [
	Exit('south', 'quanzhen/guchang', False),
]
cunzhangjia=Room('quanzhen/cunzhangjia', u'�峤��', None, 0, exits)

exits = [
	Exit('westdown', 'quanzhen/jiaobei', False),
]
damen=Room('quanzhen/damen', u'ȫ��̴���', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/damen', False),
	Exit('south', 'quanzhen/xianzhentang', False),
	Exit('north', 'quanzhen/huizhentang', False),
	Exit('east', 'quanzhen/datang2', False),
]
datang1=Room('quanzhen/datang1', u'����һ��', None, 0, exits)

exits = [
	Exit('west', 'quanzhen/datang1', False),
	Exit('south', 'quanzhen/piandian', False),
	Exit('north', 'quanzhen/cetang', False),
	Exit('east', 'quanzhen/datang3', False),
]
datang2=Room('quanzhen/datang2', u'���ö���', None, 0, exits)

exits = [
	Exit('west', 'quanzhen/datang2', False),
	Exit('south', 'quanzhen/nairongdian', False),
	Exit('north', 'quanzhen/guozhendian', False),
	Exit('east', 'quanzhen/laojundian', False),
]
datang3=Room('quanzhen/datang3', u'��������', None, 0, exits)

exits = [
	Exit('north', 'quanzhen/jingxiushi', False),
]
diziju=Room('quanzhen/diziju', u'���Ӿ�', None, 0, exits)

exits = [
	Exit('west', 'quanzhen/zhongxin', False),
	Exit('south', 'quanzhen/fu_damen', False),
	Exit('north', 'quanzhen/kedian1', False),
	Exit('east', 'quanzhen/dongmen', False),
]
dongjie=Room('quanzhen/dongjie', u'����', 'wugong', 0, exits)

exits = [
	Exit('west', 'quanzhen/dongjie', False),
	Exit('east', 'quanzhen/guandao2', False),
]
dongmen=Room('quanzhen/dongmen', u'����', 'wugong', 0, exits)

exits = [
	Exit('southdown', 'quanzhen/shijie7', False),
	Exit('north', 'quanzhen/yuzhengong', False),
]
fangzhenqiao=Room('quanzhen/fangzhenqiao', u'������', 'quanzhen', 0, exits)

exits = [
	Exit('northwest', 'quanzhen/nanjie', False),
	Exit('east', 'quanzhen/fu_xiaoyuan', False),
]
fu_cemen=Room('quanzhen/fu_cemen', u'���Ҳ���', None, 0, exits)

exits = [
	Exit('west', 'quanzhen/fu_datang', False),
	Exit('north', 'quanzhen/fu_huating', False),
]
fu_ceting=Room('quanzhen/fu_ceting', u'����', None, 0, exits)

exits = [
	Exit('south', 'quanzhen/fu_xiaoyuan', False),
	Exit('north', 'quanzhen/dongjie', False),
]
fu_damen=Room('quanzhen/fu_damen', u'���Ҵ���', 'wugong', 0, exits)

exits = [
	Exit('west', 'quanzhen/fu_zhangfang', False),
	Exit('south', 'quanzhen/fu_houyuan', False),
	Exit('north', 'quanzhen/fu_xiaoyuan', False),
	Exit('east', 'quanzhen/fu_ceting', False),
]
fu_datang=Room('quanzhen/fu_datang', u'���Ҵ���', None, 0, exits)

exits = [
	Exit('southeast', 'quanzhen/houhuayuan', False),
	Exit('south', 'quanzhen/fu_woshi', False),
	Exit('north', 'quanzhen/fu_datang', False),
]
fu_houyuan=Room('quanzhen/fu_houyuan', u'��Ժ', 'wugong', 0, exits)

exits = [
	Exit('west', 'quanzhen/fu_xiaoyuan', False),
	Exit('south', 'quanzhen/fu_ceting', False),
]
fu_huating=Room('quanzhen/fu_huating', u'����', 'wugong', 0, exits)

exits = [
	Exit('southeast', 'quanzhen/fu_mishi', False),
]
fu_midao=Room('quanzhen/fu_midao', u'�ܵ�', None, 0, exits)

exits = [
	Exit('northwest', 'quanzhen/fu_midao', False),
	Exit('up', 'quanzhen/fu_woshi', False),
]
fu_mishi=Room('quanzhen/fu_mishi', u'����', None, 0, exits)

exits = [
	Exit('north', 'quanzhen/fu_houyuan', False),
]
fu_woshi=Room('quanzhen/fu_woshi', u'����', None, 0, exits)

exits = [
	Exit('west', 'quanzhen/fu_cemen', False),
	Exit('south', 'quanzhen/fu_datang', False),
	Exit('east', 'quanzhen/fu_huating', False),
	Exit('north', 'quanzhen/fu_damen', False),
]
fu_xiaoyuan=Room('quanzhen/fu_xiaoyuan', u'����СԺ', 'wugong', 0, exits)

exits = [
	Exit('east', 'quanzhen/fu_datang', False),
]
fu_zhangfang=Room('quanzhen/fu_zhangfang', u'�ʷ�', None, 0, exits)

exits = [
	Exit('west', 'quanzhen/guandao2', False),
	Exit('northeast', 'changan/nan_chengmen', False),
]
guandao1=Room('quanzhen/guandao1', u'�ٵ�', 'wugong', 0, exits)

exits = [
	Exit('west', 'quanzhen/dongmen', False),
	Exit('east', 'quanzhen/guandao1', False),
]
guandao2=Room('quanzhen/guandao2', u'�ٵ�', 'wugong', 0, exits)

exits = [
	Exit('north', 'quanzhen/piandian', False),
]
guangning=Room('quanzhen/guangning', u'������', None, 0, exits)

exits = [
	Exit('north', 'quanzhen/houhuayuan', False),
]
guanjinglou=Room('quanzhen/guanjinglou', u'�۾�¥', 'quanzhen', 0, exits)

exits = [
	Exit('north', 'quanzhen/shijie9', False),
]
guanritai=Room('quanzhen/guanritai', u'����̨', 'quanzhen', 0, exits)

exits = [
	Exit('southeast', 'quanzhen/xiaocun', False),
	Exit('northwest', 'quanzhen/minju3', False),
	Exit('southwest', 'quanzhen/minju4', False),
	Exit('north', 'quanzhen/cunzhangjia', False),
]
guchang=Room('quanzhen/guchang', u'ɹ�ȳ�', 'wugong', 0, exits)

exits = [
	Exit('west', 'quanzhen/cetang', False),
	Exit('south', 'quanzhen/datang3', False),
	Exit('north', 'quanzhen/cundaota1', False),
]
guozhendian=Room('quanzhen/guozhendian', u'�����', None, 0, exits)

exits = [
	Exit('northwest', 'quanzhen/fu_houyuan', False),
	Exit('south', 'quanzhen/guanjinglou', False),
	Exit('east', 'quanzhen/houhuayuan1', False),
]
houhuayuan=Room('quanzhen/houhuayuan', u'��԰', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/houhuayuan', False),
]
houhuayuan1=Room('quanzhen/houhuayuan1', u'��԰', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/jingxiushi', False),
	Exit('northeast', 'quanzhen/xiaolu1', False),
]
houshan=Room('quanzhen/houshan', u'��ɽ', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/laojundian', False),
	Exit('east', 'quanzhen/houtang2', False),
]
houtang1=Room('quanzhen/houtang1', u'����һ��', None, 0, exits)

exits = [
	Exit('west', 'quanzhen/houtang1', False),
	Exit('south', 'quanzhen/wuchang1', False),
	Exit('north', 'quanzhen/liangong', False),
	Exit('east', 'quanzhen/houtang3', False),
]
houtang2=Room('quanzhen/houtang2', u'���ö���', None, 0, exits)

exits = [
	Exit('west', 'quanzhen/houtang2', False),
	Exit('northeast', 'quanzhen/xiaohuayuan1', False),
	Exit('east', 'quanzhen/jingxiushi', False),
]
houtang3=Room('quanzhen/houtang3', u'��������', None, 0, exits)

exits = [
	Exit('south', 'quanzhen/datang1', False),
	Exit('north', 'quanzhen/wanwutang', False),
	Exit('east', 'quanzhen/cetang', False),
]
huizhentang=Room('quanzhen/huizhentang', u'������', None, 0, exits)

exits = [
	Exit('west', 'quanzhen/shijianyan', False),
	Exit('eastup', 'quanzhen/damen', False),
	Exit('northup', 'quanzhen/shijie6', False),
]
jiaobei=Room('quanzhen/jiaobei', u'�̱�', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/houtang3', False),
	Exit('south', 'quanzhen/diziju', False),
	Exit('east', 'quanzhen/houshan', False),
]
jingxiushi=Room('quanzhen/jingxiushi', u'������', None, 0, exits)

exits = [
	Exit('south', 'quanzhen/beijie', False),
	Exit('up', 'quanzhen/jiulou2', False),
]
jiulou1=Room('quanzhen/jiulou1', u'��¥', None, 0, exits)

exits = [
	Exit('down', 'quanzhen/jiulou1', False),
]
jiulou2=Room('quanzhen/jiulou2', u'��¥��¥', None, 0, exits)

exits = [
	Exit('south', 'quanzhen/dongjie', False),
	Exit('up', 'quanzhen/kedian2', False),
	Exit('north', 'quanzhen/majiu', False),
]
kedian1=Room('quanzhen/kedian1', u'�͵�', None, 0, exits)

exits = [
	Exit('down', 'quanzhen/kedian1', False),
]
kedian2=Room('quanzhen/kedian2', u'�͵��¥', None, 1, exits)

exits = [
	Exit('west', 'quanzhen/datang3', False),
	Exit('south', 'quanzhen/tongtiandian', False),
	Exit('north', 'quanzhen/yuanshidian', False),
	Exit('east', 'quanzhen/houtang1', False),
]
laojundian=Room('quanzhen/laojundian', u'�Ͼ���', None, 0, exits)

exits = [
	Exit('south', 'quanzhen/houtang2', False),
	Exit('north', 'quanzhen/chanfang2', False),
]
liangong=Room('quanzhen/liangong', u'������', None, 0, exits)

exits = [
	Exit('south', 'quanzhen/kedian1', False),
]
majiu=Room('quanzhen/majiu', u'���', 'wugong', 0, exits)

exits = [
	Exit('east', 'quanzhen/beijie', False),
]
minju1=Room('quanzhen/minju1', u'���', None, 0, exits)

exits = [
	Exit('south', 'quanzhen/xijie', False),
]
minju2=Room('quanzhen/minju2', u'���', None, 0, exits)

exits = [
	Exit('southeast', 'quanzhen/guchang', False),
]
minju3=Room('quanzhen/minju3', u'���', None, 0, exits)

exits = [
	Exit('northeast', 'quanzhen/guchang', False),
]
minju4=Room('quanzhen/minju4', u'���', None, 0, exits)

exits = [
	Exit('eastup', 'city/guangchang', False),
	Exit('up', 'quanzhen/diziju', False),
]
mishi=Room('quanzhen/mishi', u'����', None, 0, exits)

exits = [
	Exit('west', 'quanzhen/piandian', False),
	Exit('south', 'quanzhen/qingjing', False),
	Exit('north', 'quanzhen/datang3', False),
]
nairongdian=Room('quanzhen/nairongdian', u'���ݵ�', None, 0, exits)

exits = [
	Exit('southeast', 'quanzhen/fu_cemen', False),
	Exit('north', 'quanzhen/zhongxin', False),
]
nanjie=Room('quanzhen/nanjie', u'�Ͻ�', 'wugong', 0, exits)

exits = [
	Exit('west', 'quanzhen/xianzhentang', False),
	Exit('south', 'quanzhen/guangning', False),
	Exit('north', 'quanzhen/datang2', False),
	Exit('east', 'quanzhen/nairongdian', False),
]
piandian=Room('quanzhen/piandian', u'ƫ��', None, 0, exits)

exits = [
	Exit('north', 'quanzhen/nairongdian', False),
]
qingjing=Room('quanzhen/qingjing', u'�徻��', None, 0, exits)

exits = [
	Exit('north', 'quanzhen/xianzhentang', False),
]
rongwutang=Room('quanzhen/rongwutang', u'������', None, 0, exits)

exits = [
	Exit('out', 'quanzhen/xiaolu12', False),
]
shandong=Room('quanzhen/shandong', u'��ɽɽ��', None, 0, exits)

exits = [
	Exit('westdown', 'quanzhen/shanlu4', False),
	Exit('north', 'gumu/shanlu13', False),
]
shanjiao=Room('quanzhen/shanjiao', u'����ɽ��', 'quanzhen', 0, exits)

exits = [
	Exit('northup', 'quanzhen/xiaocun', False),
	Exit('eastup', 'quanzhen/shanlu2', False),
	Exit('southwest', 'quanzhen/ximen', False),
]
shanlu1=Room('quanzhen/shanlu1', u'ɽ·', 'wugong', 0, exits)

exits = [
	Exit('southeast', 'quanzhen/shanlu4', False),
	Exit('westdown', 'quanzhen/shanlu1', False),
	Exit('northeast', 'quanzhen/shanlu3', False),
]
shanlu2=Room('quanzhen/shanlu2', u'ɽ·', 'quanzhen', 0, exits)

exits = [
	Exit('northup', 'quanzhen/cuipinggu', False),
	Exit('southwest', 'quanzhen/shanlu2', False),
]
shanlu3=Room('quanzhen/shanlu3', u'ɽ·', 'quanzhen', 0, exits)

exits = [
	Exit('northwest', 'quanzhen/shanlu2', False),
	Exit('eastup', 'quanzhen/shanjiao', False),
]
shanlu4=Room('quanzhen/shanlu4', u'ɽ·', 'wugong', 0, exits)

exits = [
	Exit('northwest', 'quanzhen/wuchang2', False),
	Exit('east', 'quanzhen/chufang', False),
	Exit('north', 'quanzhen/xiuxishi', False),
]
shantang=Room('quanzhen/shantang', u'����', None, 0, exits)

exits = [
	Exit('southup', 'quanzhen/shijie8', False),
	Exit('east', 'quanzhen/jiaobei', False),
	Exit('northdown', 'quanzhen/shijie4', False),
]
shijianyan=Room('quanzhen/shijianyan', u'�Խ���', 'quanzhen', 0, exits)

exits = [
	Exit('southdown', 'gumu/daxiaochang', False),
	Exit('northup', 'quanzhen/shijie2', False),
]
shijie1=Room('quanzhen/shijie1', u'ʯ��', 'quanzhen', 0, exits)

exits = [
	Exit('southdown', 'quanzhen/shijie1', False),
	Exit('southeast', 'quanzhen/shijie3', False),
]
shijie2=Room('quanzhen/shijie2', u'ʯ��', 'quanzhen', 0, exits)

exits = [
	Exit('northwest', 'quanzhen/shijie2', False),
	Exit('eastup', 'quanzhen/shijie4', False),
]
shijie3=Room('quanzhen/shijie3', u'ʯ��', 'quanzhen', 0, exits)

exits = [
	Exit('southup', 'quanzhen/shijianyan', False),
	Exit('northup', 'quanzhen/shijie5', False),
	Exit('westdown', 'quanzhen/shijie3', False),
]
shijie4=Room('quanzhen/shijie4', u'ʯ��', 'quanzhen', 0, exits)

exits = [
	Exit('southdown', 'quanzhen/shijie4', False),
	Exit('northup', 'quanzhen/banshanting', False),
]
shijie5=Room('quanzhen/shijie5', u'ʯ��', 'quanzhen', 0, exits)

exits = [
	Exit('southdown', 'quanzhen/jiaobei', False),
	Exit('northup', 'quanzhen/shijie7', False),
]
shijie6=Room('quanzhen/shijie6', u'ʯ��', 'quanzhen', 0, exits)

exits = [
	Exit('southdown', 'quanzhen/shijie6', False),
	Exit('northup', 'quanzhen/fangzhenqiao', False),
]
shijie7=Room('quanzhen/shijie7', u'ʯ��', 'quanzhen', 0, exits)

exits = [
	Exit('southup', 'quanzhen/shijie9', False),
	Exit('northdown', 'quanzhen/shijianyan', False),
]
shijie8=Room('quanzhen/shijie8', u'ʯ��', 'quanzhen', 0, exits)

exits = [
	Exit('south', 'quanzhen/guanritai', False),
	Exit('northdown', 'quanzhen/shijie8', False),
]
shijie9=Room('quanzhen/shijie9', u'ʯ��', 'quanzhen', 0, exits)

exits = [
	Exit('south', 'quanzhen/cetang', False),
]
shiweishi=Room('quanzhen/shiweishi', u'��Ϊ��', None, 0, exits)

exits = [
	Exit('north', 'quanzhen/laojundian', False),
]
tongtiandian=Room('quanzhen/tongtiandian', u'ͨ���', None, 0, exits)

exits = [
	Exit('south', 'quanzhen/huizhentang', False),
]
wanwutang=Room('quanzhen/wanwutang', u'������', None, 0, exits)

exits = [
	Exit('southeast', 'quanzhen/xiuxishi', False),
	Exit('south', 'quanzhen/wuchang2', False),
	Exit('north', 'quanzhen/houtang2', False),
]
wuchang1=Room('quanzhen/wuchang1', u'�䳡', 'quanzhen', 0, exits)

exits = [
	Exit('southeast', 'quanzhen/shantang', False),
	Exit('south', 'quanzhen/wuchang3', False),
	Exit('east', 'quanzhen/xiuxishi', False),
	Exit('north', 'quanzhen/wuchang1', False),
]
wuchang2=Room('quanzhen/wuchang2', u'�䳡', 'quanzhen', 0, exits)

exits = [
	Exit('north', 'quanzhen/wuchang2', False),
]
wuchang3=Room('quanzhen/wuchang3', u'�䳡', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/yaojishi', False),
	Exit('south', 'quanzhen/rongwutang', False),
	Exit('north', 'quanzhen/datang1', False),
	Exit('east', 'quanzhen/piandian', False),
]
xianzhentang=Room('quanzhen/xianzhentang', u'������', None, 0, exits)

exits = [
	Exit('southdown', 'quanzhen/shanlu1', False),
	Exit('northwest', 'quanzhen/guchang', False),
]
xiaocun=Room('quanzhen/xiaocun', u'С��ׯ', 'wugong', 0, exits)

exits = [
	Exit('southwest', 'quanzhen/houtang3', False),
	Exit('northeast', 'quanzhen/xiaohuayuan2', False),
]
xiaohuayuan1=Room('quanzhen/xiaohuayuan1', u'С��԰', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/chanfang3', False),
	Exit('southwest', 'quanzhen/xiaohuayuan1', False),
	Exit('east', 'quanzhen/xiaohuayuan3', False),
]
xiaohuayuan2=Room('quanzhen/xiaohuayuan2', u'С��԰', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/xiaohuayuan2', False),
]
xiaohuayuan3=Room('quanzhen/xiaohuayuan3', u'С��԰', 'quanzhen', 0, exits)

exits = [
	Exit('southwest', 'quanzhen/houshan', False),
	Exit('northeast', 'quanzhen/xiaolu2', False),
]
xiaolu1=Room('quanzhen/xiaolu1', u'��ɽС·', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/xiaolu9', False),
	Exit('south', 'quanzhen/xiaolu12', False),
	Exit('north', 'quanzhen/xiaolu10', False),
	Exit('east', 'quanzhen/xiaolu11', False),
]
xiaolu10=Room('quanzhen/xiaolu10', u'��ɽС·', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/xiaolu10', False),
	Exit('south', 'quanzhen/xiaolu11', False),
	Exit('north', 'quanzhen/xiaolu11', False),
	Exit('east', 'quanzhen/xiaolu11', False),
]
xiaolu11=Room('quanzhen/xiaolu11', u'��ɽС·', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/xiaolu12', False),
	Exit('south', 'quanzhen/xiaolu12', False),
	Exit('north', 'quanzhen/xiaolu10', False),
	Exit('east', 'quanzhen/xiaolu12', False),
	Exit('enter', 'quanzhen/shandong', False),
]
xiaolu12=Room('quanzhen/xiaolu12', u'��ɽС·', 'quanzhen', 0, exits)

exits = [
	Exit('southwest', 'quanzhen/xiaolu1', False),
	Exit('east', 'quanzhen/xiaolu3', False),
]
xiaolu2=Room('quanzhen/xiaolu2', u'��ɽС·', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/xiaolu2', False),
	Exit('south', 'quanzhen/xiaolu7', False),
	Exit('north', 'quanzhen/xiaolu5', False),
	Exit('east', 'quanzhen/xiaolu4', False),
]
xiaolu3=Room('quanzhen/xiaolu3', u'��ɽС·', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/xiaolu3', False),
	Exit('south', 'quanzhen/xiaolu8', False),
	Exit('north', 'quanzhen/xiaolu4', False),
	Exit('east', 'quanzhen/xiaolu4', False),
]
xiaolu4=Room('quanzhen/xiaolu4', u'��ɽС·', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/xiaolu5', False),
	Exit('south', 'quanzhen/xiaolu3', False),
	Exit('north', 'quanzhen/xiaolu6', False),
	Exit('east', 'quanzhen/xiaolu9', False),
]
xiaolu5=Room('quanzhen/xiaolu5', u'��ɽС·', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/xiaolu6', False),
	Exit('south', 'quanzhen/xiaolu5', False),
	Exit('north', 'quanzhen/xiaolu6', False),
	Exit('east', 'quanzhen/xiaolu6', False),
]
xiaolu6=Room('quanzhen/xiaolu6', u'��ɽС·', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/xiaolu7', False),
	Exit('south', 'quanzhen/xiaolu7', False),
	Exit('north', 'quanzhen/xiaolu3', False),
	Exit('east', 'quanzhen/xiaolu8', False),
]
xiaolu7=Room('quanzhen/xiaolu7', u'��ɽС·', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/xiaolu7', False),
	Exit('south', 'quanzhen/xiaolu8', False),
	Exit('north', 'quanzhen/xiaolu4', False),
	Exit('east', 'quanzhen/xiaolu8', False),
]
xiaolu8=Room('quanzhen/xiaolu8', u'��ɽС·', 'quanzhen', 0, exits)

exits = [
	Exit('west', 'quanzhen/xiaolu5', False),
	Exit('south', 'quanzhen/xiaolu9', False),
	Exit('north', 'quanzhen/xiaolu9', False),
	Exit('east', 'quanzhen/xiaolu10', False),
]
xiaolu9=Room('quanzhen/xiaolu9', u'��ɽС·', 'quanzhen', 0, exits)

exits = [
	Exit('north', 'quanzhen/xijie', False),
]
xiaomiao=Room('quanzhen/xiaomiao', u'������', None, 0, exits)

exits = [
	Exit('west', 'quanzhen/ximen', False),
	Exit('south', 'quanzhen/xiaomiao', False),
	Exit('north', 'quanzhen/minju2', False),
	Exit('east', 'quanzhen/zhongxin', False),
]
xijie=Room('quanzhen/xijie', u'����', 'wugong', 0, exits)

exits = [
	Exit('northeast', 'quanzhen/shanlu1', False),
	Exit('east', 'quanzhen/xijie', False),
]
ximen=Room('quanzhen/ximen', u'����', 'wugong', 0, exits)

exits = [
	Exit('west', 'quanzhen/wuchang2', False),
	Exit('northwest', 'quanzhen/wuchang1', False),
	Exit('south', 'quanzhen/shantang', False),
]
xiuxishi=Room('quanzhen/xiuxishi', u'��Ϣ��', None, 0, exits)

exits = [
	Exit('east', 'quanzhen/xianzhentang', False),
]
yaojishi=Room('quanzhen/yaojishi', u'ҩ����', None, 0, exits)

exits = [
	Exit('south', 'quanzhen/laojundian', False),
]
yuanshidian=Room('quanzhen/yuanshidian', u'Ԫʼ��', None, 0, exits)

exits = [
	Exit('south', 'quanzhen/fangzhenqiao', False),
]
yuzhengong=Room('quanzhen/yuzhengong', u'���湬', None, 0, exits)

exits = [
	Exit('west', 'quanzhen/xijie', False),
	Exit('south', 'quanzhen/nanjie', False),
	Exit('north', 'quanzhen/beijie', False),
	Exit('east', 'quanzhen/dongjie', False),
]
zhongxin=Room('quanzhen/zhongxin', u'���Ĺ㳡', 'wugong', 0, exits)

