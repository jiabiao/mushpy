# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('southeast', 'dali/yixibu', False),
	Exit('north', 'dali/lushui', False),
	Exit('westup', 'dali/gaolishan1', False),
]
atoubu=Room('dali/atoubu', u'��ͷ��', 'dali', 0, exits)

exits = [
	Exit('eastup', 'dali/lushuieast', False),
	Exit('south', 'dali/lushui', False),
	Exit('north', 'dali/zhenxiong', False),
]
badidian=Room('dali/badidian', u'�͵ĵ�', 'dali', 0, exits)

exits = [
	Exit('north', 'dali/dahejieeast', False),
]
baiyiminju=Room('dali/baiyiminju', u'�������', None, 0, exits)

exits = [
	Exit('south', 'dali/dahejieeast', False),
]
baiyiziguan=Room('dali/baiyiziguan', u'�����ֹ�', None, 0, exits)

exits = [
	Exit('northup', 'dali/shanjian', False),
	Exit('east', 'dali/buxiongbu', False),
]
banshan=Room('dali/banshan', u'��ɽ����', 'dali', 0, exits)

exits = [
	Exit('eastdown', 'dali/yanan2', False),
	Exit('westdown', 'dali/qingxi', False),
]
bijishan=Room('dali/bijishan', u'�̼�ɽ��', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/yixibu', False),
]
biluoshan=Room('dali/biluoshan', u'����ɽ��', 'dali', 0, exits)

exits = [
	Exit('eastdown', 'dali/shanlu2', False),
	Exit('westdown', 'dali/lushuieast', False),
]
biluoxueshan=Room('dali/biluoxueshan', u'����ѩɽ', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/chahua1', False),
]
bingqiku=Room('dali/bingqiku', u'������', None, 0, exits)

exits = [
	Exit('west', 'dali/majiu', False),
	Exit('north', 'dali/dahejiewest', False),
]
bingying=Room('dali/bingying', u'��Ӫ', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/banshan', False),
	Exit('south', 'dali/xingyunhu', False),
	Exit('north', 'dali/nongtian5', False),
	Exit('east', 'dali/yangcanfang', False),
]
buxiongbu=Room('dali/buxiongbu', u'���۲�', 'dali', 0, exits)

exits = [
	Exit('southwest', 'dali/xiaguan', False),
	Exit('east', 'dali/hongsheng', False),
	Exit('north', 'dali/shilin', False),
]
cangshan=Room('dali/cangshan', u'��ɽ', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/heshang', False),
	Exit('northeast', 'dali/cangshanzhong', False),
]
cangshanlu1=Room('dali/cangshanlu1', u'��ɽɽ·', 'dali', 0, exits)

exits = [
	Exit('southeast', 'dali/xiaguan', False),
	Exit('southwest', 'dali/cangshanlu1', False),
	Exit('north', 'dali/jianchuan', False),
]
cangshanzhong=Room('dali/cangshanzhong', u'��ɽ�в�', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/wumeng', False),
]
caopo=Room('dali/caopo', u'�������', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/shizilukou', False),
	Exit('east', 'dali/taiheju', False),
	Exit('north', 'dali/taihejiekou', False),
]
center=Room('dali/center', u'���Ĺ㳡', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/tingyuan', False),
	Exit('south', 'dali/xiuxishi', False),
	Exit('east', 'dali/chahua2', False),
	Exit('north', 'dali/bingqiku', False),
]
chahua1=Room('dali/chahua1', u'�軨԰��', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/chahua7', False),
]
chahua10=Room('dali/chahua10', u'�軨Է', None, 0, exits)

exits = [
	Exit('southeast', 'dali/chahua4', False),
	Exit('west', 'dali/chahua1', False),
	Exit('northeast', 'dali/chahua3', False),
]
chahua2=Room('dali/chahua2', u'�軨԰', 'dali', 0, exits)

exits = [
	Exit('southeast', 'dali/chahua5', False),
	Exit('southwest', 'dali/chahua2', False),
	Exit('north', 'dali/chahua6', False),
]
chahua3=Room('dali/chahua3', u'�軨԰', 'dali', 0, exits)

exits = [
	Exit('northwest', 'dali/chahua2', False),
	Exit('northeast', 'dali/chahua5', False),
]
chahua4=Room('dali/chahua4', u'�軨԰', 'dali', 0, exits)

exits = [
	Exit('northwest', 'dali/chahua3', False),
	Exit('southwest', 'dali/chahua4', False),
]
chahua5=Room('dali/chahua5', u'�軨԰', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/chahua3', False),
	Exit('north', 'dali/chahua7', False),
]
chahua6=Room('dali/chahua6', u'�軨԰', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/chahua8', False),
	Exit('northup', 'dali/chahua9', False),
	Exit('south', 'dali/chahua6', False),
	Exit('east', 'dali/chahua10', False),
]
chahua7=Room('dali/chahua7', u'�軨԰', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/yongdao2', False),
	Exit('east', 'dali/chahua7', False),
]
chahua8=Room('dali/chahua8', u'�軨԰����', 'dali', 0, exits)

exits = [
	Exit('southdown', 'dali/chahua7', False),
]
chahua9=Room('dali/chahua9', u'�軨԰', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/northgate', False),
	Exit('eastup', 'dali/chahuashan2', False),
]
chahuashan1=Room('dali/chahuashan1', u'�軨ɽ', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/chahuashan4', False),
	Exit('westdown', 'dali/chahuashan1', False),
	Exit('east', 'dali/chahuashan5', False),
	Exit('north', 'dali/chahuashan3', False),
]
chahuashan2=Room('dali/chahuashan2', u'�軨ɽ', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/chahuashan2', False),
]
chahuashan3=Room('dali/chahuashan3', u'�軨ɽ', 'dali', 0, exits)

exits = [
	Exit('north', 'dali/chahuashan2', False),
]
chahuashan4=Room('dali/chahuashan4', u'�軨ɽ', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/chahuashan2', False),
	Exit('eastdown', 'dali/chahuashan6', False),
]
chahuashan5=Room('dali/chahuashan5', u'�軨ɽ', 'dali', 0, exits)

exits = [
	Exit('southeast', 'dali/dadieshui', False),
	Exit('westup', 'dali/chahuashan5', False),
]
chahuashan6=Room('dali/chahuashan6', u'�軨ɽ��', 'dali', 0, exits)

exits = [
	Exit('southdown', 'dali/shilin', False),
	Exit('west', 'dali/shilin1', False),
	Exit('northeast', 'dali/shilin2', False),
	Exit('enter', 'dali/hole', False),
]
changhu=Room('dali/changhu', u'����', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/tingyuan', False),
	Exit('north', 'dali/tingfang', False),
]
changlang=Room('dali/changlang', u'����', 'dali', 0, exits)

exits = [
	Exit('east', 'dali/tingfang', False),
]
chufang=Room('dali/chufang', u'����', None, 0, exits)

exits = [
	Exit('southdown', 'dali/qingxi', False),
	Exit('northwest', 'dali/chahuashan6', False),
	Exit('eastdown', 'dali/xiaojing', False),
]
dadieshui=Room('dali/dadieshui', u'���ˮ�ٲ�', 'dali', 0, exits)

exits = [
	Exit('southup', 'dali/wunong', False),
]
daduhe=Room('dali/daduhe', u'��ɺӱ�', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/shizilukou', False),
	Exit('south', 'dali/baiyiminju', False),
	Exit('north', 'dali/baiyiziguan', False),
]
dahejieeast=Room('dali/dahejieeast', u'��ͽ�', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/bingying', False),
	Exit('north', 'dali/tusifu', False),
	Exit('east', 'dali/shizilukou', False),
]
dahejiewest=Room('dali/dahejiewest', u'��ͽ�', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/nongtian4', False),
	Exit('up', 'dali/dalangan2', False),
]
dalangan1=Room('dali/dalangan1', u'������', 'dali', 0, exits)

exits = [
	Exit('down', 'dali/dalangan1', False),
]
dalangan2=Room('dali/dalangan2', u'�����в�', None, 0, exits)

exits = [
	Exit('northwest', 'dali/ershuiqiao', False),
	Exit('south', 'dali/northgate', False),
	Exit('north', 'dali/taihecheng', False),
]
dalinorth=Room('dali/dalinorth', u'����Ǳ�', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/dianchi', False),
	Exit('north', 'dali/heisenlin', False),
]
dasenlin=Room('dali/dasenlin', u'��ɭ��', 'dali', 0, exits)

exits = [
	Exit('out', 'dali/gudao', False),
	Exit('north', 'dali/louti', False),
]
dating=Room('dali/dating', u'����', None, 0, exits)

exits = [
	Exit('south', 'dali/taihecheng', False),
	Exit('north', 'dali/road3', False),
]
dehuabei=Room('dali/dehuabei', u'��گ�»���', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/yanchi1', False),
	Exit('north', 'dali/dasenlin', False),
]
dianchi=Room('dali/dianchi', u'���', 'dali', 0, exits)

exits = [
	Exit('southeast', 'dali/dalinorth', False),
	Exit('north', 'dali/xiaguan', False),
]
ershuiqiao=Room('dali/ershuiqiao', u'��ˮ��', 'dali', 0, exits)

exits = [
	Exit('southeast', 'dali/feilihueast', False),
	Exit('east', 'dali/luwang', False),
	Exit('north', 'dali/xizhou', False),
]
feilihu=Room('dali/feilihu', u'��������', 'dali', 0, exits)

exits = [
	Exit('northwest', 'dali/feilihu', False),
	Exit('south', 'dali/longkou', False),
	Exit('southwest', 'dali/hexi', False),
]
feilihueast=Room('dali/feilihueast', u'��������', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/huanggs', False),
	Exit('south', 'dali/hexi', False),
]
feilihusouth=Room('dali/feilihusouth', u'�������ϰ�', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/gaolishan2', False),
	Exit('eastdown', 'dali/atoubu', False),
]
gaolishan1=Room('dali/gaolishan1', u'����ɽ����', 'dali', 0, exits)

exits = [
	Exit('east', 'dali/gaolishan1', False),
]
gaolishan2=Room('dali/gaolishan2', u'����ɽ����', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/taiheeast', False),
]
garments=Room('dali/garments', u'Ѧ�ǳ�����', None, 0, exits)

exits = [
	Exit('south', 'dali/zhenxiong', False),
	Exit('northup', 'dali/shanlin', False),
	Exit('east', 'dali/minadian', False),
]
gelucheng=Room('dali/gelucheng', u'��³��', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/yujie', False),
	Exit('north', 'dali/qiandian', False),
]
gongmen=Room('dali/gongmen', u'����', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/shanlu6', False),
	Exit('east', 'dali/luyuxi', False),
	Exit('enter', 'dali/dating', False),
]
gudao=Room('dali/gudao', u'�ŵ�', 'dali', 0, exits)

exits = [
	Exit('out', 'dali/zoulang3', False),
]
guibingshi1=Room('dali/guibingshi1', u'�����', None, 0, exits)

exits = [
	Exit('out', 'dali/zoulang4', False),
]
guibingshi2=Room('dali/guibingshi2', u'�����', None, 0, exits)

exits = [
	Exit('south', 'dali/shanlin', False),
	Exit('east', 'dali/heshang', False),
]
hebian=Room('dali/hebian', u'�ӱ�', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/shulinwai', False),
	Exit('southwest', 'dali/xiaodao2', False),
	Exit('north', 'dali/xiaodao1', False),
]
heilongling=Room('dali/heilongling', u'������', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/dasenlin', False),
]
heisenlin=Room('dali/heisenlin', u'��ɭ��', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/hebian', False),
	Exit('east', 'dali/cangshanlu1', False),
]
heshang=Room('dali/heshang', u'����', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/yujia', False),
	Exit('south', 'dali/zhulin2', False),
	Exit('north', 'dali/feilihusouth', False),
	Exit('northeast', 'dali/feilihueast', False),
]
hexi=Room('dali/hexi', u'������', 'dali', 0, exits)

exits = [
	Exit('out', 'dali/changhu', False),
]
hole=Room('dali/hole', u'֥�ƶ�', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/cangshan', False),
	Exit('south', 'tianlongsi/damen', False),
	Exit('enter', 'dali/hongsheng1', False),
]
hongsheng=Room('dali/hongsheng', u'��ʥ����', None, 0, exits)

exits = [
	Exit('out', 'dali/hongsheng', False),
	Exit('up', 'dali/hongsheng2', False),
]
hongsheng1=Room('dali/hongsheng1', u'����', None, 0, exits)

exits = [
	Exit('up', 'dali/hongsheng3', False),
	Exit('down', 'dali/hongsheng1', False),
]
hongsheng2=Room('dali/hongsheng2', u'��ʥ����', None, 0, exits)

exits = [
	Exit('up', 'dali/hongsheng4', False),
	Exit('down', 'dali/hongsheng2', False),
]
hongsheng3=Room('dali/hongsheng3', u'��ʥ����', None, 0, exits)

exits = [
	Exit('down', 'dali/hongsheng3', False),
]
hongsheng4=Room('dali/hongsheng4', u'��ʥ����', None, 0, exits)

exits = [
	Exit('west', 'dali/yushanfang', False),
	Exit('south', 'dali/yuhuayuan', False),
	Exit('east', 'dali/piandian', False),
	Exit('north', 'dali/zhengdian', False),
]
hualang=Room('dali/hualang', u'����', 'dali', 0, exits)

exits = [
	Exit('east', 'dali/feilihusouth', False),
]
huanggs=Room('dali/huanggs', u'�ƹ����ٲ�', 'dali', 0, exits)

exits = [
	Exit('east', 'dali/xiaodao1', False),
	Exit('north', 'dali/yuxuguanqian', False),
]
hudiequan=Room('dali/hudiequan', u'����Ȫ', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/cangshanzhong', False),
	Exit('north', 'dali/jianchuankou', False),
]
jianchuan=Room('dali/jianchuan', u'������', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/jianchuan', False),
	Exit('north', 'dali/shanlu1', False),
]
jianchuankou=Room('dali/jianchuankou', u'����ɽ��', 'dali', 0, exits)

exits = [
	Exit('out', 'dali/jinzhihe', False),
	Exit('up', 'dali/jingzhuang2', False),
]
jingzhuang1=Room('dali/jingzhuang1', u'��һ��', 'dali', 0, exits)

exits = [
	Exit('up', 'dali/jingzhuang3', False),
	Exit('down', 'dali/jingzhuang1', False),
]
jingzhuang2=Room('dali/jingzhuang2', u'�ڶ���', 'dali', 0, exits)

exits = [
	Exit('up', 'dali/jingzhuang4', False),
	Exit('down', 'dali/jingzhuang2', False),
]
jingzhuang3=Room('dali/jingzhuang3', u'������', 'dali', 0, exits)

exits = [
	Exit('up', 'dali/jingzhuang5', False),
	Exit('down', 'dali/jingzhuang3', False),
]
jingzhuang4=Room('dali/jingzhuang4', u'���Ĳ�', 'dali', 0, exits)

exits = [
	Exit('up', 'dali/jingzhuang6', False),
	Exit('down', 'dali/jingzhuang4', False),
]
jingzhuang5=Room('dali/jingzhuang5', u'�����', 'dali', 0, exits)

exits = [
	Exit('up', 'dali/jingzhuang7', False),
	Exit('down', 'dali/jingzhuang5', False),
]
jingzhuang6=Room('dali/jingzhuang6', u'������', 'dali', 0, exits)

exits = [
	Exit('down', 'dali/jingzhuang6', False),
]
jingzhuang7=Room('dali/jingzhuang7', u'���߲�', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/xiaojing', False),
	Exit('north', 'dali/jingzhuang1', False),
	Exit('east', 'dali/yanchi1', False),
]
jinzhihe=Room('dali/jinzhihe', u'��֭����', 'dali', 0, exits)

exits = [
	Exit('out', 'dali/wuyiminju3', False),
]
jisidawu1=Room('dali/jisidawu1', u'�������', None, 0, exits)

exits = [
	Exit('west', 'dali/xizhou', False),
	Exit('up', 'dali/kedian2', False),
]
kedian=Room('dali/kedian', u'�͵�', None, 0, exits)

exits = [
	Exit('down', 'dali/kedian', False),
]
kedian2=Room('dali/kedian2', u'�͵��¥', None, 0, exits)

exits = [
	Exit('out', 'dali/zoulang2', False),
]
kefang=Room('dali/kefang', u'�ͷ�', None, 0, exits)

exits = [
	Exit('up', 'dali/langan2', False),
	Exit('north', 'dali/nongtian2', False),
]
langan1=Room('dali/langan1', u'����', 'dali', 0, exits)

exits = [
	Exit('down', 'dali/langan1', False),
]
langan2=Room('dali/langan2', u'�����в�', None, 0, exits)

exits = [
	Exit('west', 'dali/nongtian5', False),
	Exit('up', 'dali/langan4', False),
]
langan3=Room('dali/langan3', u'����', 'dali', 0, exits)

exits = [
	Exit('down', 'dali/langan3', False),
]
langan4=Room('dali/langan4', u'�����в�', None, 0, exits)

exits = [
	Exit('southeast', 'dali/yongdao1', False),
	Exit('north', 'dali/liangong2', False),
]
liangong=Room('dali/liangong', u'���䳡', None, 0, exits)

exits = [
	Exit('south', 'dali/liangong', False),
	Exit('north', 'dali/liangong3', False),
]
liangong2=Room('dali/liangong2', u'���䳡', None, 0, exits)

exits = [
	Exit('south', 'dali/liangong2', False),
]
liangong3=Room('dali/liangong3', u'���䳡', None, 0, exits)

exits = [
	Exit('north', 'dali/feilihueast', False),
]
longkou=Room('dali/longkou', u'���ڳ�', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/dating', False),
	Exit('up', 'dali/zoulang1', False),
]
louti=Room('dali/louti', u'¥��', None, 0, exits)

exits = [
	Exit('northwest', 'dali/yanchi3', False),
	Exit('southwest', 'dali/yanan1', False),
	Exit('east', 'dali/nongtian2', False),
]
luojiadian=Room('dali/luojiadian', u'��٤��', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/atoubu', False),
	Exit('north', 'dali/badidian', False),
]
lushui=Room('dali/lushui', u'��ˮ�ذ�', 'dali', 0, exits)

exits = [
	Exit('eastup', 'dali/biluoxueshan', False),
	Exit('westdown', 'dali/badidian', False),
]
lushuieast=Room('dali/lushuieast', u'����ˮ�ӹ�', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/feilihu', False),
	Exit('south', 'dali/shuitian', False),
	Exit('north', 'dali/zhulou3', False),
	Exit('east', 'dali/yulin', False),
]
luwang=Room('dali/luwang', u'³����', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/gudao', False),
	Exit('east', 'dali/shuangheqiao', False),
]
luyuxi=Room('dali/luyuxi', u'����Ϫ�ذ�', 'dali', 0, exits)

exits = [
	Exit('east', 'dali/bingying', False),
]
majiu=Room('dali/majiu', u'���', 'dali', 0, exits)

exits = [
	Exit('southup', 'dali/shanjian', False),
	Exit('northeast', 'dali/yangzong', False),
]
milin=Room('dali/milin', u'����', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/gelucheng', False),
	Exit('southwest', 'dali/zhenxiong', False),
]
minadian=Room('dali/minadian', u'���ɵ�', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/yongdao2', False),
]
neitang=Room('dali/neitang', u'����', None, 0, exits)

exits = [
	Exit('out', 'dali/nianhuasi', False),
]
nianhua1=Room('dali/nianhua1', u'�黨�º�Ժ', 'dali', 0, exits)

exits = [
	Exit('southdown', 'dali/shanlu2', False),
	Exit('enter', 'dali/nianhua1', False),
]
nianhuasi=Room('dali/nianhuasi', u'�黨��', 'dali', 0, exits)

exits = [
	Exit('north', 'dali/wuding', False),
]
nongtian1=Room('dali/nongtian1', u'ũ��', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/luojiadian', False),
	Exit('south', 'dali/langan1', False),
	Exit('east', 'dali/nongtian3', False),
]
nongtian2=Room('dali/nongtian2', u'ũ��', 'dali', 0, exits)

exits = [
	Exit('southeast', 'dali/shanlu7', False),
	Exit('west', 'dali/nongtian2', False),
]
nongtian3=Room('dali/nongtian3', u'ũ��', 'dali', 0, exits)

exits = [
	Exit('southwest', 'dali/yangzong', False),
	Exit('east', 'dali/dalangan1', False),
]
nongtian4=Room('dali/nongtian4', u'ũ��', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/buxiongbu', False),
	Exit('east', 'dali/langan3', False),
]
nongtian5=Room('dali/nongtian5', u'ũ��', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/shanlu3', False),
	Exit('south', 'dali/paifang', False),
	Exit('east', 'dali/chahuashan1', False),
	Exit('north', 'dali/dalinorth', False),
]
northgate=Room('dali/northgate', u'������', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/yujie', False),
	Exit('south', 'dali/taihejiekou', False),
	Exit('north', 'dali/northgate', False),
	Exit('east', 'dali/wangfulu', False),
]
paifang=Room('dali/paifang', u'�Ʒ�', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/hualang', False),
]
piandian=Room('dali/piandian', u'ƫ��', None, 0, exits)

exits = [
	Exit('south', 'dali/gongmen', False),
	Exit('north', 'dali/yuhuayuan', False),
]
qiandian=Room('dali/qiandian', u'ǰ��', None, 0, exits)

exits = [
	Exit('east', 'dali/sheguta', False),
]
qingchi=Room('dali/qingchi', u'���', 'dali', 0, exits)

exits = [
	Exit('southdown', 'dali/xiaodao1', False),
	Exit('eastup', 'dali/bijishan', False),
	Exit('northup', 'dali/dadieshui', False),
]
qingxi=Room('dali/qingxi', u'��Ϫ��̶', 'dali', 0, exits)

exits = [
	Exit('east', 'dali/wuding', False),
]
qingzhulin=Room('dali/qingzhulin', u'������', 'dali', 0, exits)

exits = [
	Exit('southwest', 'dali/road2', False),
	Exit('northeast', 'emei/qsjie2', False),
]
road1=Room('dali/road1', u'�ٵ�', 'dali', 0, exits)

exits = [
	Exit('southwest', 'dali/road3', False),
	Exit('northeast', 'dali/road1', False),
]
road2=Room('dali/road2', u'�ٵ�', 'dali', 0, exits)

exits = [
	Exit('northwest', 'wanjiegu/riverside2', False),
	Exit('south', 'dali/dehuabei', False),
	Exit('northeast', 'dali/road2', False),
]
road3=Room('dali/road3', u'�ٵ�', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/tianweijing', False),
	Exit('north', 'dali/shuangheqiao', False),
]
road4=Room('dali/road4', u'��·', 'dali', 0, exits)

exits = [
	Exit('southeast', 'foshan/road1', False),
	Exit('northwest', 'dali/shuangheqiao', False),
]
road5=Room('dali/road5', u'����·', 'dali', 0, exits)

exits = [
	Exit('northdown', 'dali/yangzong', False),
]
sanglin=Room('dali/sanglin', u'ɣ��', 'dali', 0, exits)

exits = [
	Exit('southdown', 'dali/banshan', False),
	Exit('northdown', 'dali/milin', False),
]
shanjian=Room('dali/shanjian', u'����ɽ��', 'dali', 0, exits)

exits = [
	Exit('southdown', 'dali/gelucheng', False),
	Exit('north', 'dali/hebian', False),
]
shanlin=Room('dali/shanlin', u'ɽ��', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/jianchuankou', False),
	Exit('northup', 'dali/wunong', False),
]
shanlu1=Room('dali/shanlu1', u'����ɽ·', 'dali', 0, exits)

exits = [
	Exit('northup', 'dali/nianhuasi', False),
	Exit('south', 'dali/shanlu4', False),
	Exit('east', 'dali/shanlu3', False),
	Exit('westup', 'dali/biluoxueshan', False),
]
shanlu2=Room('dali/shanlu2', u'ɽ·', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/shanlu2', False),
	Exit('east', 'dali/northgate', False),
]
shanlu3=Room('dali/shanlu3', u'ɽ·', 'dali', 0, exits)

exits = [
	Exit('southwest', 'dali/shanlu5', False),
	Exit('north', 'dali/shanlu2', False),
]
shanlu4=Room('dali/shanlu4', u'ɽ·', 'dali', 0, exits)

exits = [
	Exit('southeast', 'dali/shanlu6', False),
	Exit('northeast', 'dali/shanlu4', False),
]
shanlu5=Room('dali/shanlu5', u'ɽ·', 'dali', 0, exits)

exits = [
	Exit('northwest', 'dali/shanlu5', False),
	Exit('east', 'dali/gudao', False),
]
shanlu6=Room('dali/shanlu6', u'ɽ·', 'dali', 0, exits)

exits = [
	Exit('northwest', 'dali/nongtian3', False),
	Exit('eastup', 'dali/shanlu8', False),
]
shanlu7=Room('dali/shanlu7', u'ɽ·', 'dali', 0, exits)

exits = [
	Exit('eastdown', 'dali/yangzong', False),
	Exit('westdown', 'dali/shanlu7', False),
]
shanlu8=Room('dali/shanlu8', u'ɽ·', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/qingchi', False),
	Exit('east', 'dali/taihejiekou', False),
]
sheguta=Room('dali/sheguta', u'�߹���', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/wfdating', False),
	Exit('east', 'dali/tingyuan', False),
]
shijing=Room('dali/shijing', u'ʯ��', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/cangshan', False),
	Exit('northup', 'dali/changhu', False),
]
shilin=Room('dali/shilin', u'·��ʯ��', 'dali', 0, exits)

exits = [
	Exit('east', 'dali/changhu', False),
]
shilin1=Room('dali/shilin1', u'������ʯ��', 'dali', 0, exits)

exits = [
	Exit('southwest', 'dali/changhu', False),
]
shilin2=Room('dali/shilin2', u'��Ħ��ʯ��', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/dahejiewest', False),
	Exit('south', 'dali/southgate', False),
	Exit('east', 'dali/dahejieeast', False),
	Exit('north', 'dali/center', False),
]
shizilukou=Room('dali/shizilukou', u'ʮ��·��', 'dali', 0, exits)

exits = [
	Exit('southeast', 'dali/road5', False),
	Exit('west', 'dali/luyuxi', False),
	Exit('south', 'dali/road4', False),
	Exit('north', 'dali/southgate', False),
]
shuangheqiao=Room('dali/shuangheqiao', u'˫����', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/tingfang', False),
]
shufang=Room('dali/shufang', u'�鷿', None, 0, exits)

exits = [
	Exit('north', 'dali/luwang', False),
]
shuitian=Room('dali/shuitian', u'ˮ��', 'dali', 0, exits)

exits = [
	Exit('north', 'dali/heilongling', False),
]
shulinwai=Room('dali/shulinwai', u'������', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/zonglichu', False),
]
sikong=Room('dali/sikong', u'˾����', None, 0, exits)

exits = [
	Exit('west', 'dali/zonglichu', False),
]
sima=Room('dali/sima', u'˾����', None, 0, exits)

exits = [
	Exit('east', 'dali/zonglichu', False),
]
situ=Room('dali/situ', u'˾ͽ��', None, 0, exits)

exits = [
	Exit('south', 'dali/shuangheqiao', False),
	Exit('east', 'dali/xiaodao2', False),
	Exit('north', 'dali/shizilukou', False),
]
southgate=Room('dali/southgate', u'�ϳ���', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/taiheeast', False),
]
stoneshop=Room('dali/stoneshop', u'ʯ��', None, 0, exits)

exits = [
	Exit('south', 'dali/dalinorth', False),
	Exit('north', 'dali/dehuabei', False),
]
taihecheng=Room('dali/taihecheng', u'̫�ͳ�', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/taihejiekou', False),
	Exit('south', 'dali/yaoshop', False),
	Exit('north', 'dali/garments', False),
	Exit('east', 'dali/stoneshop', False),
]
taiheeast=Room('dali/taiheeast', u'̫�Ͷ���', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/sheguta', False),
	Exit('south', 'dali/center', False),
	Exit('east', 'dali/taiheeast', False),
	Exit('north', 'dali/paifang', False),
]
taihejiekou=Room('dali/taihejiekou', u'̫�ͽֿ�', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/center', False),
	Exit('up', 'dali/taiheju2', False),
]
taiheju=Room('dali/taiheju', u'̫�;�', None, 0, exits)

exits = [
	Exit('down', 'dali/taiheju', False),
]
taiheju2=Room('dali/taiheju2', u'̫�;Ӷ�¥', None, 0, exits)

exits = [
	Exit('south', 'dali/xizhou', False),
	Exit('north', 'dali/road4', False),
]
tianweijing=Room('dali/tianweijing', u'������', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/chufang', False),
	Exit('south', 'dali/changlang', False),
	Exit('east', 'dali/shufang', False),
	Exit('north', 'dali/yongdao1', False),
]
tingfang=Room('dali/tingfang', u'����', None, 0, exits)

exits = [
	Exit('west', 'dali/shijing', False),
	Exit('north', 'dali/changlang', False),
	Exit('east', 'dali/chahua1', False),
]
tingyuan=Room('dali/tingyuan', u'ͥԺ', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/zhenxiong', False),
]
titian1=Room('dali/titian1', u'����', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/dahejiewest', False),
	Exit('enter', 'dali/tusimentang', False),
]
tusifu=Room('dali/tusifu', u'��˾��', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/tusimentang', False),
]
tusihouting=Room('dali/tusihouting', u'����', None, 0, exits)

exits = [
	Exit('out', 'dali/tusifu', False),
	Exit('up', 'dali/tusiyishi', False),
	Exit('north', 'dali/tusihouting', False),
]
tusimentang=Room('dali/tusimentang', u'����', None, 0, exits)

exits = [
	Exit('down', 'dali/tusimentang', False),
]
tusiyishi=Room('dali/tusiyishi', u'������', None, 0, exits)

exits = [
	Exit('south', 'dali/wangfulu', False),
	Exit('enter', 'dali/wfdating', False),
]
wangfugate=Room('dali/wangfugate', u'��������', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/paifang', False),
	Exit('north', 'dali/wangfugate', False),
]
wangfulu=Room('dali/wangfulu', u'����·', 'dali', 0, exits)

exits = [
	Exit('out', 'dali/wangfugate', False),
	Exit('west', 'dali/zhangfang', False),
	Exit('north', 'dali/zonglichu', False),
	Exit('east', 'dali/shijing', False),
]
wfdating=Room('dali/wfdating', u'������������', None, 0, exits)

exits = [
	Exit('west', 'dali/qingzhulin', False),
	Exit('south', 'dali/nongtian1', False),
	Exit('northeast', 'dali/zhulin', False),
	Exit('north', 'dali/zhulou1', False),
]
wuding=Room('dali/wuding', u'�䶨��', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/wunong', False),
	Exit('south', 'dali/wuyiminju2', False),
	Exit('north', 'dali/wuyiminju1', False),
	Exit('east', 'dali/caopo', False),
]
wumeng=Room('dali/wumeng', u'���ɴ���', 'dali', 0, exits)

exits = [
	Exit('southdown', 'dali/shanlu1', False),
	Exit('east', 'dali/wumeng', False),
	Exit('northdown', 'dali/daduhe', False),
]
wunong=Room('dali/wunong', u'��Ū��', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/wumeng', False),
]
wuyiminju1=Room('dali/wuyiminju1', u'�������', None, 0, exits)

exits = [
	Exit('north', 'dali/wumeng', False),
]
wuyiminju2=Room('dali/wuyiminju2', u'�������', None, 0, exits)

exits = [
	Exit('east', 'dali/zhenxiong', False),
	Exit('enter', 'dali/jisidawu1', False),
]
wuyiminju3=Room('dali/wuyiminju3', u'�������', None, 0, exits)

exits = [
	Exit('north', 'dali/yixibu', False),
]
wuyiminju4=Room('dali/wuyiminju4', u'�������', None, 0, exits)

exits = [
	Exit('northwest', 'dali/cangshanzhong', False),
	Exit('south', 'dali/ershuiqiao', False),
	Exit('northeast', 'dali/cangshan', False),
]
xiaguan=Room('dali/xiaguan', u'�¹س�', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/hudiequan', False),
	Exit('south', 'dali/heilongling', False),
	Exit('northup', 'dali/qingxi', False),
]
xiaodao1=Room('dali/xiaodao1', u'����С��', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/southgate', False),
	Exit('northeast', 'dali/heilongling', False),
]
xiaodao2=Room('dali/xiaodao2', u'�ּ�С��', 'dali', 0, exits)

exits = [
	Exit('east', 'dali/jinzhihe', False),
	Exit('westup', 'dali/dadieshui', False),
]
xiaojing=Room('dali/xiaojing', u'ɽ��С��', 'dali', 0, exits)

exits = [
	Exit('eastup', 'dali/yuxiashan', False),
	Exit('north', 'dali/buxiongbu', False),
]
xingyunhu=Room('dali/xingyunhu', u'���ƺ���', 'dali', 0, exits)

exits = [
	Exit('north', 'dali/chahua1', False),
]
xiuxishi=Room('dali/xiuxishi', u'�᷿', None, 0, exits)

exits = [
	Exit('south', 'dali/feilihu', False),
	Exit('southwest', 'dali/zhulin', False),
	Exit('east', 'dali/kedian', False),
	Exit('north', 'dali/tianweijing', False),
]
xizhou=Room('dali/xizhou', u'ϲ�ݳ�', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/yanan2', False),
	Exit('northeast', 'dali/luojiadian', False),
]
yanan1=Room('dali/yanan1', u'����ذ�', 'dali', 0, exits)

exits = [
	Exit('east', 'dali/yanan1', False),
	Exit('westup', 'dali/bijishan', False),
]
yanan2=Room('dali/yanan2', u'�س�С·', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/jinzhihe', False),
	Exit('eastup', 'dali/yanchi2', False),
	Exit('north', 'dali/dianchi', False),
]
yanchi1=Room('dali/yanchi1', u'�سص̰�', 'dali', 0, exits)

exits = [
	Exit('east', 'dali/yanchi3', False),
	Exit('westdown', 'dali/yanchi1', False),
]
yanchi2=Room('dali/yanchi2', u'�سص̰�', 'dali', 0, exits)

exits = [
	Exit('southeast', 'dali/luojiadian', False),
	Exit('west', 'dali/yanchi2', False),
]
yanchi3=Room('dali/yanchi3', u'�سص̰�', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/buxiongbu', False),
]
yangcanfang=Room('dali/yangcanfang', u'���Ϸ�', None, 0, exits)

exits = [
	Exit('southup', 'dali/sanglin', False),
	Exit('southwest', 'dali/milin', False),
	Exit('northeast', 'dali/nongtian4', False),
	Exit('westup', 'dali/shanlu8', False),
]
yangzong=Room('dali/yangzong', u'������', 'dali', 0, exits)

exits = [
	Exit('north', 'dali/taiheeast', False),
]
yaoshop=Room('dali/yaoshop', u'ҩ��', None, 0, exits)

exits = [
	Exit('northwest', 'dali/atoubu', False),
	Exit('south', 'dali/wuyiminju4', False),
	Exit('east', 'dali/biluoshan', False),
]
yixibu=Room('dali/yixibu', u'��Ϫ��', 'dali', 0, exits)

exits = [
	Exit('northwest', 'dali/liangong', False),
	Exit('south', 'dali/tingfang', False),
	Exit('northeast', 'dali/yongdao2', False),
]
yongdao1=Room('dali/yongdao1', u'��', 'dali', 0, exits)

exits = [
	Exit('southwest', 'dali/yongdao1', False),
	Exit('east', 'dali/chahua8', False),
	Exit('north', 'dali/neitang', False),
]
yongdao2=Room('dali/yongdao2', u'��', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/qiandian', False),
	Exit('north', 'dali/hualang', False),
]
yuhuayuan=Room('dali/yuhuayuan', u'����԰', 'dali', 0, exits)

exits = [
	Exit('east', 'dali/hexi', False),
]
yujia=Room('dali/yujia', u'���', 'dali', 0, exits)

exits = [
	Exit('north', 'dali/gongmen', False),
	Exit('east', 'dali/paifang', False),
]
yujie=Room('dali/yujie', u'����', 'dali', 0, exits)

exits = [
	Exit('west', 'dali/luwang', False),
]
yulin=Room('dali/yulin', u'��������', 'dali', 0, exits)

exits = [
	Exit('east', 'dali/hualang', False),
]
yushanfang=Room('dali/yushanfang', u'���ŷ�', None, 0, exits)

exits = [
	Exit('westdown', 'dali/xingyunhu', False),
]
yuxiashan=Room('dali/yuxiashan', u'��ϼɽ', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/yuxuguanqian', False),
]
yuxuguan=Room('dali/yuxuguan', u'�����', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/hudiequan', False),
	Exit('north', 'dali/yuxuguan', False),
]
yuxuguanqian=Room('dali/yuxuguanqian', u'�����ǰ', 'dali', 0, exits)

exits = [
	Exit('east', 'dali/wfdating', False),
]
zhangfang=Room('dali/zhangfang', u'�ʷ�', None, 0, exits)

exits = [
	Exit('south', 'dali/hualang', False),
]
zhengdian=Room('dali/zhengdian', u'����', None, 0, exits)

exits = [
	Exit('west', 'dali/wuyiminju3', False),
	Exit('south', 'dali/badidian', False),
	Exit('east', 'dali/titian1', False),
	Exit('northeast', 'dali/minadian', False),
	Exit('north', 'dali/gelucheng', False),
]
zhenxiong=Room('dali/zhenxiong', u'����', 'dali', 0, exits)

exits = [
	Exit('southwest', 'dali/wuding', False),
	Exit('northeast', 'dali/xizhou', False),
]
zhulin=Room('dali/zhulin', u'����С·', 'dali', 0, exits)

exits = [
	Exit('north', 'dali/hexi', False),
]
zhulin2=Room('dali/zhulin2', u'�����', 'dali', 0, exits)

exits = [
	Exit('south', 'dali/wuding', False),
	Exit('up', 'dali/zhulou2', False),
]
zhulou1=Room('dali/zhulou1', u'��¥��', 'dali', 0, exits)

exits = [
	Exit('down', 'dali/zhulou1', False),
]
zhulou2=Room('dali/zhulou2', u'��¥', None, 0, exits)

exits = [
	Exit('south', 'dali/luwang', False),
	Exit('up', 'dali/zhulou4', False),
]
zhulou3=Room('dali/zhulou3', u'����¥', None, 0, exits)

exits = [
	Exit('up', 'dali/zhulou5', False),
	Exit('down', 'dali/zhulou3', False),
]
zhulou4=Room('dali/zhulou4', u'������', None, 0, exits)

exits = [
	Exit('down', 'dali/zhulou4', False),
]
zhulou5=Room('dali/zhulou5', u'������', None, 0, exits)

exits = [
	Exit('west', 'dali/situ', False),
	Exit('south', 'dali/wfdating', False),
	Exit('east', 'dali/sima', False),
	Exit('north', 'dali/sikong', False),
]
zonglichu=Room('dali/zonglichu', u'��������', None, 0, exits)

exits = [
	Exit('west', 'dali/zoulang2', False),
	Exit('east', 'dali/zoulang3', False),
	Exit('down', 'dali/louti', False),
]
zoulang1=Room('dali/zoulang1', u'����', None, 0, exits)

exits = [
	Exit('east', 'dali/zoulang1', False),
	Exit('enter', 'dali/kefang', False),
]
zoulang2=Room('dali/zoulang2', u'����', None, 0, exits)

exits = [
	Exit('west', 'dali/zoulang1', False),
	Exit('east', 'dali/zoulang4', False),
	Exit('enter', 'dali/guibingshi1', False),
]
zoulang3=Room('dali/zoulang3', u'����', None, 0, exits)

exits = [
	Exit('west', 'dali/zoulang3', False),
	Exit('enter', 'dali/guibingshi2', False),
]
zoulang4=Room('dali/zoulang4', u'����', None, 0, exits)

