# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'suzhou/erxianting', False),
]
bailianchi=Room('suzhou/bailianchi', u'������', 'suzhou', 0, exits)

exits = [
	Exit('northwest', 'suzhou/xidajie1', False),
	Exit('south', 'suzhou/nandajie1', False),
	Exit('north', 'suzhou/canlangting', False),
	Exit('northeast', 'suzhou/dongdajie1', False),
]
baodaiqiao=Room('suzhou/baodaiqiao', u'������', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/majiu', False),
	Exit('south', 'suzhou/canlangting', False),
	Exit('southwest', 'suzhou/xiyuan', False),
	Exit('north', 'suzhou/beidajie2', False),
	Exit('east', 'suzhou/kedian', False),
]
beidajie1=Room('suzhou/beidajie1', u'�����', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/zijinan', False),
	Exit('south', 'suzhou/beidajie1', False),
	Exit('north', 'suzhou/beimen', False),
	Exit('east', 'suzhou/jiudian', False),
]
beidajie2=Room('suzhou/beidajie2', u'�����', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/beidajie2', False),
	Exit('north', 'suzhou/road1', False),
]
beimen=Room('suzhou/beimen', u'����', 'suzhou', 0, exits)

exits = [
	Exit('north', 'suzhou/xidajie1', False),
]
bingying=Room('suzhou/bingying', u'��Ӫ', 'suzhou', 0, exits)

exits = [
	Exit('southeast', 'suzhou/dongdajie1', False),
	Exit('south', 'suzhou/baodaiqiao', False),
	Exit('southwest', 'suzhou/xidajie1', False),
	Exit('north', 'suzhou/beidajie1', False),
]
canlangting=Room('suzhou/canlangting', u'����ͤ', 'suzhou', 0, exits)

exits = [
	Exit('southwest', 'suzhou/nandajie1', False),
]
chaguan=Room('suzhou/chaguan', u'���', None, 0, exits)

exits = [
	Exit('northeast', 'suzhou/gumujiaohe', False),
]
chitang=Room('suzhou/chitang', u'����', 'suzhou', 0, exits)

exits = [
	Exit('north', 'suzhou/dongdajie1', False),
]
dangpu=Room('suzhou/dangpu', u'���ͼ�', None, 0, exits)

exits = [
	Exit('north', 'suzhou/dongdajie2', False),
]
datiepu=Room('suzhou/datiepu', u'������', 'suzhou', 0, exits)

exits = [
	Exit('northwest', 'suzhou/canlangting', False),
	Exit('south', 'suzhou/dangpu', False),
	Exit('southwest', 'suzhou/baodaiqiao', False),
	Exit('north', 'suzhou/hutong1', False),
	Exit('east', 'suzhou/dongdajie2', False),
]
dongdajie1=Room('suzhou/dongdajie1', u'�����', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/dongdajie1', False),
	Exit('northwest', 'suzhou/hutong3', False),
	Exit('south', 'suzhou/datiepu', False),
	Exit('north', 'suzhou/yaopu', False),
	Exit('east', 'suzhou/dongmen', False),
]
dongdajie2=Room('suzhou/dongdajie2', u'�����', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/dongdajie2', False),
	Exit('east', 'quanzhou/qzroad2', False),
]
dongmen=Room('suzhou/dongmen', u'����', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/qianrenshi', False),
	Exit('north', 'suzhou/bailianchi', False),
]
erxianting=Room('suzhou/erxianting', u'����ͤ', 'suzhou', 0, exits)

exits = [
	Exit('north', 'suzhou/tielingguan', False),
	Exit('enter', 'suzhou/hanshidian', False),
]
fengqiao=Room('suzhou/fengqiao', u'����', 'suzhou', 0, exits)

exits = [
	Exit('southwest', 'suzhou/chitang', False),
	Exit('east', 'suzhou/hehuating', False),
]
gumujiaohe=Room('suzhou/gumujiaohe', u'��ľ��ڭ', 'suzhou', 0, exits)

exits = [
	Exit('eastdown', 'suzhou/wanjing', False),
]
hanhanquan=Room('suzhou/hanhanquan', u'����Ȫ', 'suzhou', 0, exits)

exits = [
	Exit('southeast', 'suzhou/road4', False),
	Exit('enter', 'suzhou/zhengdian', False),
]
hanshansi=Room('suzhou/hanshansi', u'��ɽ��', None, 0, exits)

exits = [
	Exit('west', 'suzhou/zhengdian', False),
	Exit('out', 'suzhou/fengqiao', False),
]
hanshidian=Room('suzhou/hanshidian', u'��ʰ��', None, 0, exits)

exits = [
	Exit('west', 'suzhou/gumujiaohe', False),
	Exit('east', 'suzhou/liuyuan', False),
]
hehuating=Room('suzhou/hehuating', u'�ɻ���', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/toumenshan', False),
	Exit('northeast', 'suzhou/road1', False),
]
huqiu=Room('suzhou/huqiu', u'����ɽ', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/leitai', False),
	Exit('south', 'suzhou/dongdajie1', False),
	Exit('northeast', 'suzhou/hutong2', False),
]
hutong1=Room('suzhou/hutong1', u'��ͬ', 'suzhou', 0, exits)

exits = [
	Exit('southwest', 'suzhou/hutong1', False),
	Exit('east', 'suzhou/hutong3', False),
]
hutong2=Room('suzhou/hutong2', u'��ͬ', 'suzhou', 0, exits)

exits = [
	Exit('southeast', 'suzhou/dongdajie2', False),
	Exit('west', 'suzhou/hutong2', False),
]
hutong3=Room('suzhou/hutong3', u'��ͬ', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/beidajie2', False),
]
jiudian=Room('suzhou/jiudian', u'����¥', 'suzhou', 0, exits)

exits = [
	Exit('east', 'suzhou/nandajie1', False),
]
jubaozhai=Room('suzhou/jubaozhai', u'�۱�ի', None, 0, exits)

exits = [
	Exit('west', 'suzhou/beidajie1', False),
	Exit('up', 'suzhou/kedian2', False),
]
kedian=Room('suzhou/kedian', u'�͵�', None, 0, exits)

exits = [
	Exit('enter', 'suzhou/kedian3', False),
	Exit('down', 'suzhou/kedian', False),
]
kedian2=Room('suzhou/kedian2', u'�͵��¥', None, 0, exits)

exits = [
	Exit('out', 'suzhou/kedian2', False),
]
kedian3=Room('suzhou/kedian3', u'�͵��¥', None, 0, exits)

exits = [
	Exit('east', 'suzhou/hutong1', False),
]
leitai=Room('suzhou/leitai', u'��̨ǰ�㳡', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/hehuating', False),
	Exit('east', 'suzhou/nandajie2', False),
]
liuyuan=Room('suzhou/liuyuan', u'��԰', 'suzhou', 0, exits)

exits = [
	Exit('north', 'suzhou/wenmeige', False),
]
lixuetang=Room('suzhou/lixuetang', u'��ѩ��', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/xiyuan', False),
	Exit('east', 'suzhou/beidajie1', False),
]
majiu=Room('suzhou/majiu', u'���', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/jubaozhai', False),
	Exit('south', 'suzhou/nandajie2', False),
	Exit('southwest', 'suzhou/shuyuan', False),
	Exit('northeast', 'suzhou/chaguan', False),
	Exit('north', 'suzhou/baodaiqiao', False),
	Exit('east', 'suzhou/shizilin', False),
]
nandajie1=Room('suzhou/nandajie1', u'�ϴ��', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/liuyuan', False),
	Exit('south', 'suzhou/nanmen', False),
	Exit('north', 'suzhou/nandajie1', False),
	Exit('east', 'suzhou/tingyu', False),
]
nandajie2=Room('suzhou/nandajie2', u'�ϴ��', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/road5', False),
	Exit('north', 'suzhou/nandajie2', False),
]
nanmen=Room('suzhou/nanmen', u'����', 'suzhou', 0, exits)

exits = [
	Exit('northwest', 'suzhou/zhishuang', False),
	Exit('north', 'suzhou/shijianshi', False),
	Exit('east', 'suzhou/erxianting', False),
]
qianrenshi=Room('suzhou/qianrenshi', u'ǧ��ʯ', 'suzhou', 0, exits)

exits = [
	Exit('northwest', 'guiyun/shanlu2', False),
	Exit('south', 'suzhou/beimen', False),
	Exit('southwest', 'suzhou/huqiu', False),
]
road1=Room('suzhou/road1', u'��ʯ�ٵ�', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/road3', False),
	Exit('east', 'suzhou/ximen', False),
]
road2=Room('suzhou/road2', u'��ʯ�ٵ�', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/road4', False),
	Exit('east', 'suzhou/road2', False),
]
road3=Room('suzhou/road3', u'��ʯ�ٵ�', 'suzhou', 0, exits)

exits = [
	Exit('northwest', 'suzhou/hanshansi', False),
	Exit('east', 'suzhou/road3', False),
]
road4=Room('suzhou/road4', u'��ʯ�ٵ�', 'suzhou', 0, exits)

exits = [
	Exit('southwest', 'yanziwu/hupan', False),
	Exit('east', 'item/road1', False),
	Exit('north', 'suzhou/nanmen', False),
]
road5=Room('suzhou/road5', u'��ʯ�ٵ�', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/qianrenshi', False),
	Exit('north', 'suzhou/zhenshi', False),
	Exit('northeast', 'suzhou/zhenniang', False),
	Exit('down', 'suzhou/wanjing', False),
]
shijianshi=Room('suzhou/shijianshi', u'�Խ�ʯ', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/nandajie1', False),
	Exit('northeast', 'suzhou/zhipoxuan', False),
	Exit('east', 'suzhou/yanyutang', False),
]
shizilin=Room('suzhou/shizilin', u'ʨ����', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/xidajie2', False),
]
shuchang=Room('suzhou/shuchang', u'�鳡', 'suzhou', 0, exits)

exits = [
	Exit('northeast', 'suzhou/nandajie1', False),
]
shuyuan=Room('suzhou/shuyuan', u'��Ժ', None, 0, exits)

exits = [
	Exit('south', 'suzhou/zhenniang', False),
]
sunwuting=Room('suzhou/sunwuting', u'����ͤ', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/fengqiao', False),
]
tielingguan=Room('suzhou/tielingguan', u'�����', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/nandajie2', False),
]
tingyu=Room('suzhou/tingyu', u'������', None, 0, exits)

exits = [
	Exit('west', 'suzhou/wanjing', False),
	Exit('north', 'suzhou/huqiu', False),
]
toumenshan=Room('suzhou/toumenshan', u'ͷ��ɽ', 'suzhou', 0, exits)

exits = [
	Exit('north', 'suzhou/hanhanquan', False),
	Exit('east', 'suzhou/toumenshan', False),
	Exit('up', 'suzhou/shijianshi', False),
]
wanjing=Room('suzhou/wanjing', u'��ɽׯ', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/zhenquting', False),
	Exit('south', 'suzhou/lixuetang', False),
]
wenmeige=Room('suzhou/wenmeige', u'��÷��', 'suzhou', 0, exits)

exits = [
	Exit('southeast', 'suzhou/baodaiqiao', False),
	Exit('west', 'suzhou/xidajie2', False),
	Exit('northwest', 'suzhou/yunhematou', False),
	Exit('south', 'suzhou/bingying', False),
	Exit('northeast', 'suzhou/canlangting', False),
	Exit('north', 'suzhou/yamen', False),
]
xidajie1=Room('suzhou/xidajie1', u'�����', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/ximen', False),
	Exit('south', 'suzhou/xuanmiao', False),
	Exit('north', 'suzhou/shuchang', False),
	Exit('east', 'suzhou/xidajie1', False),
]
xidajie2=Room('suzhou/xidajie2', u'�����', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/road2', False),
	Exit('east', 'suzhou/xidajie2', False),
]
ximen=Room('suzhou/ximen', u'����', 'suzhou', 0, exits)

exits = [
	Exit('north', 'suzhou/majiu', False),
	Exit('northeast', 'suzhou/beidajie1', False),
]
xiyuan=Room('suzhou/xiyuan', u'Ϸ԰��', None, 0, exits)

exits = [
	Exit('north', 'suzhou/xidajie2', False),
]
xuanmiao=Room('suzhou/xuanmiao', u'�����', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/xidajie1', False),
]
yamen=Room('suzhou/yamen', u'���ݸ���', 'suzhou', 0, exits)

exits = [
	Exit('southeast', 'suzhou/zhenquting', False),
	Exit('west', 'suzhou/shizilin', False),
]
yanyutang=Room('suzhou/yanyutang', u'������', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/dongdajie2', False),
]
yaopu=Room('suzhou/yaopu', u'������', 'suzhou', 0, exits)

exits = [
	Exit('southeast', 'suzhou/xidajie1', False),
]
yunhematou=Room('suzhou/yunhematou', u'�˺���ͷ', 'suzhou', 0, exits)

exits = [
	Exit('out', 'suzhou/hanshansi', False),
	Exit('east', 'suzhou/hanshidian', False),
]
zhengdian=Room('suzhou/zhengdian', u'����', None, 0, exits)

exits = [
	Exit('southwest', 'suzhou/shijianshi', False),
	Exit('north', 'suzhou/sunwuting', False),
]
zhenniang=Room('suzhou/zhenniang', u'����Ĺ', 'suzhou', 0, exits)

exits = [
	Exit('northwest', 'suzhou/yanyutang', False),
	Exit('east', 'suzhou/wenmeige', False),
]
zhenquting=Room('suzhou/zhenquting', u'��Ȥͤ', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/shijianshi', False),
]
zhenshi=Room('suzhou/zhenshi', u'��ʯ', 'suzhou', 0, exits)

exits = [
	Exit('southwest', 'suzhou/shizilin', False),
]
zhipoxuan=Room('suzhou/zhipoxuan', u'Ҿ��ָ����', 'suzhou', 0, exits)

exits = [
	Exit('southeast', 'suzhou/qianrenshi', False),
]
zhishuang=Room('suzhou/zhishuang', u'��ˬ��', 'suzhou', 0, exits)

exits = [
	Exit('east', 'suzhou/beidajie2', False),
]
zijinan=Room('suzhou/zijinan', u'�Ͻ���', 'suzhou', 1, exits)

