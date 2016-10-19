# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'suzhou/erxianting', False),
]
bailianchi=Room('suzhou/bailianchi', u'白莲池', 'suzhou', 0, exits)

exits = [
	Exit('northwest', 'suzhou/xidajie1', False),
	Exit('south', 'suzhou/nandajie1', False),
	Exit('north', 'suzhou/canlangting', False),
	Exit('northeast', 'suzhou/dongdajie1', False),
]
baodaiqiao=Room('suzhou/baodaiqiao', u'宝带桥', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/majiu', False),
	Exit('south', 'suzhou/canlangting', False),
	Exit('southwest', 'suzhou/xiyuan', False),
	Exit('north', 'suzhou/beidajie2', False),
	Exit('east', 'suzhou/kedian', False),
]
beidajie1=Room('suzhou/beidajie1', u'北大街', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/zijinan', False),
	Exit('south', 'suzhou/beidajie1', False),
	Exit('north', 'suzhou/beimen', False),
	Exit('east', 'suzhou/jiudian', False),
]
beidajie2=Room('suzhou/beidajie2', u'北大街', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/beidajie2', False),
	Exit('north', 'suzhou/road1', False),
]
beimen=Room('suzhou/beimen', u'北门', 'suzhou', 0, exits)

exits = [
	Exit('north', 'suzhou/xidajie1', False),
]
bingying=Room('suzhou/bingying', u'兵营', 'suzhou', 0, exits)

exits = [
	Exit('southeast', 'suzhou/dongdajie1', False),
	Exit('south', 'suzhou/baodaiqiao', False),
	Exit('southwest', 'suzhou/xidajie1', False),
	Exit('north', 'suzhou/beidajie1', False),
]
canlangting=Room('suzhou/canlangting', u'沧浪亭', 'suzhou', 0, exits)

exits = [
	Exit('southwest', 'suzhou/nandajie1', False),
]
chaguan=Room('suzhou/chaguan', u'茶馆', None, 0, exits)

exits = [
	Exit('northeast', 'suzhou/gumujiaohe', False),
]
chitang=Room('suzhou/chitang', u'池塘', 'suzhou', 0, exits)

exits = [
	Exit('north', 'suzhou/dongdajie1', False),
]
dangpu=Room('suzhou/dangpu', u'宝和记', None, 0, exits)

exits = [
	Exit('north', 'suzhou/dongdajie2', False),
]
datiepu=Room('suzhou/datiepu', u'打铁铺', 'suzhou', 0, exits)

exits = [
	Exit('northwest', 'suzhou/canlangting', False),
	Exit('south', 'suzhou/dangpu', False),
	Exit('southwest', 'suzhou/baodaiqiao', False),
	Exit('north', 'suzhou/hutong1', False),
	Exit('east', 'suzhou/dongdajie2', False),
]
dongdajie1=Room('suzhou/dongdajie1', u'东大街', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/dongdajie1', False),
	Exit('northwest', 'suzhou/hutong3', False),
	Exit('south', 'suzhou/datiepu', False),
	Exit('north', 'suzhou/yaopu', False),
	Exit('east', 'suzhou/dongmen', False),
]
dongdajie2=Room('suzhou/dongdajie2', u'东大街', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/dongdajie2', False),
	Exit('east', 'quanzhou/qzroad2', False),
]
dongmen=Room('suzhou/dongmen', u'东门', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/qianrenshi', False),
	Exit('north', 'suzhou/bailianchi', False),
]
erxianting=Room('suzhou/erxianting', u'二仙亭', 'suzhou', 0, exits)

exits = [
	Exit('north', 'suzhou/tielingguan', False),
	Exit('enter', 'suzhou/hanshidian', False),
]
fengqiao=Room('suzhou/fengqiao', u'枫桥', 'suzhou', 0, exits)

exits = [
	Exit('southwest', 'suzhou/chitang', False),
	Exit('east', 'suzhou/hehuating', False),
]
gumujiaohe=Room('suzhou/gumujiaohe', u'古木交诃', 'suzhou', 0, exits)

exits = [
	Exit('eastdown', 'suzhou/wanjing', False),
]
hanhanquan=Room('suzhou/hanhanquan', u'憨憨泉', 'suzhou', 0, exits)

exits = [
	Exit('southeast', 'suzhou/road4', False),
	Exit('enter', 'suzhou/zhengdian', False),
]
hanshansi=Room('suzhou/hanshansi', u'寒山寺', None, 0, exits)

exits = [
	Exit('west', 'suzhou/zhengdian', False),
	Exit('out', 'suzhou/fengqiao', False),
]
hanshidian=Room('suzhou/hanshidian', u'寒拾殿', None, 0, exits)

exits = [
	Exit('west', 'suzhou/gumujiaohe', False),
	Exit('east', 'suzhou/liuyuan', False),
]
hehuating=Room('suzhou/hehuating', u'荷花厅', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/toumenshan', False),
	Exit('northeast', 'suzhou/road1', False),
]
huqiu=Room('suzhou/huqiu', u'虎丘山', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/leitai', False),
	Exit('south', 'suzhou/dongdajie1', False),
	Exit('northeast', 'suzhou/hutong2', False),
]
hutong1=Room('suzhou/hutong1', u'胡同', 'suzhou', 0, exits)

exits = [
	Exit('southwest', 'suzhou/hutong1', False),
	Exit('east', 'suzhou/hutong3', False),
]
hutong2=Room('suzhou/hutong2', u'胡同', 'suzhou', 0, exits)

exits = [
	Exit('southeast', 'suzhou/dongdajie2', False),
	Exit('west', 'suzhou/hutong2', False),
]
hutong3=Room('suzhou/hutong3', u'胡同', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/beidajie2', False),
]
jiudian=Room('suzhou/jiudian', u'春在楼', 'suzhou', 0, exits)

exits = [
	Exit('east', 'suzhou/nandajie1', False),
]
jubaozhai=Room('suzhou/jubaozhai', u'聚宝斋', None, 0, exits)

exits = [
	Exit('west', 'suzhou/beidajie1', False),
	Exit('up', 'suzhou/kedian2', False),
]
kedian=Room('suzhou/kedian', u'客店', None, 0, exits)

exits = [
	Exit('enter', 'suzhou/kedian3', False),
	Exit('down', 'suzhou/kedian', False),
]
kedian2=Room('suzhou/kedian2', u'客店二楼', None, 0, exits)

exits = [
	Exit('out', 'suzhou/kedian2', False),
]
kedian3=Room('suzhou/kedian3', u'客店二楼', None, 0, exits)

exits = [
	Exit('east', 'suzhou/hutong1', False),
]
leitai=Room('suzhou/leitai', u'擂台前广场', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/hehuating', False),
	Exit('east', 'suzhou/nandajie2', False),
]
liuyuan=Room('suzhou/liuyuan', u'留园', 'suzhou', 0, exits)

exits = [
	Exit('north', 'suzhou/wenmeige', False),
]
lixuetang=Room('suzhou/lixuetang', u'立雪堂', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/xiyuan', False),
	Exit('east', 'suzhou/beidajie1', False),
]
majiu=Room('suzhou/majiu', u'马厩', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/jubaozhai', False),
	Exit('south', 'suzhou/nandajie2', False),
	Exit('southwest', 'suzhou/shuyuan', False),
	Exit('northeast', 'suzhou/chaguan', False),
	Exit('north', 'suzhou/baodaiqiao', False),
	Exit('east', 'suzhou/shizilin', False),
]
nandajie1=Room('suzhou/nandajie1', u'南大街', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/liuyuan', False),
	Exit('south', 'suzhou/nanmen', False),
	Exit('north', 'suzhou/nandajie1', False),
	Exit('east', 'suzhou/tingyu', False),
]
nandajie2=Room('suzhou/nandajie2', u'南大街', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/road5', False),
	Exit('north', 'suzhou/nandajie2', False),
]
nanmen=Room('suzhou/nanmen', u'南门', 'suzhou', 0, exits)

exits = [
	Exit('northwest', 'suzhou/zhishuang', False),
	Exit('north', 'suzhou/shijianshi', False),
	Exit('east', 'suzhou/erxianting', False),
]
qianrenshi=Room('suzhou/qianrenshi', u'千人石', 'suzhou', 0, exits)

exits = [
	Exit('northwest', 'guiyun/shanlu2', False),
	Exit('south', 'suzhou/beimen', False),
	Exit('southwest', 'suzhou/huqiu', False),
]
road1=Room('suzhou/road1', u'青石官道', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/road3', False),
	Exit('east', 'suzhou/ximen', False),
]
road2=Room('suzhou/road2', u'青石官道', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/road4', False),
	Exit('east', 'suzhou/road2', False),
]
road3=Room('suzhou/road3', u'青石官道', 'suzhou', 0, exits)

exits = [
	Exit('northwest', 'suzhou/hanshansi', False),
	Exit('east', 'suzhou/road3', False),
]
road4=Room('suzhou/road4', u'青石官道', 'suzhou', 0, exits)

exits = [
	Exit('southwest', 'yanziwu/hupan', False),
	Exit('east', 'item/road1', False),
	Exit('north', 'suzhou/nanmen', False),
]
road5=Room('suzhou/road5', u'青石官道', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/qianrenshi', False),
	Exit('north', 'suzhou/zhenshi', False),
	Exit('northeast', 'suzhou/zhenniang', False),
	Exit('down', 'suzhou/wanjing', False),
]
shijianshi=Room('suzhou/shijianshi', u'试剑石', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/nandajie1', False),
	Exit('northeast', 'suzhou/zhipoxuan', False),
	Exit('east', 'suzhou/yanyutang', False),
]
shizilin=Room('suzhou/shizilin', u'狮子林', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/xidajie2', False),
]
shuchang=Room('suzhou/shuchang', u'书场', 'suzhou', 0, exits)

exits = [
	Exit('northeast', 'suzhou/nandajie1', False),
]
shuyuan=Room('suzhou/shuyuan', u'书院', None, 0, exits)

exits = [
	Exit('south', 'suzhou/zhenniang', False),
]
sunwuting=Room('suzhou/sunwuting', u'孙武亭', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/fengqiao', False),
]
tielingguan=Room('suzhou/tielingguan', u'铁岭关', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/nandajie2', False),
]
tingyu=Room('suzhou/tingyu', u'听雨轩', None, 0, exits)

exits = [
	Exit('west', 'suzhou/wanjing', False),
	Exit('north', 'suzhou/huqiu', False),
]
toumenshan=Room('suzhou/toumenshan', u'头门山', 'suzhou', 0, exits)

exits = [
	Exit('north', 'suzhou/hanhanquan', False),
	Exit('east', 'suzhou/toumenshan', False),
	Exit('up', 'suzhou/shijianshi', False),
]
wanjing=Room('suzhou/wanjing', u'万景山庄', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/zhenquting', False),
	Exit('south', 'suzhou/lixuetang', False),
]
wenmeige=Room('suzhou/wenmeige', u'问梅阁', 'suzhou', 0, exits)

exits = [
	Exit('southeast', 'suzhou/baodaiqiao', False),
	Exit('west', 'suzhou/xidajie2', False),
	Exit('northwest', 'suzhou/yunhematou', False),
	Exit('south', 'suzhou/bingying', False),
	Exit('northeast', 'suzhou/canlangting', False),
	Exit('north', 'suzhou/yamen', False),
]
xidajie1=Room('suzhou/xidajie1', u'西大街', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/ximen', False),
	Exit('south', 'suzhou/xuanmiao', False),
	Exit('north', 'suzhou/shuchang', False),
	Exit('east', 'suzhou/xidajie1', False),
]
xidajie2=Room('suzhou/xidajie2', u'西大街', 'suzhou', 0, exits)

exits = [
	Exit('west', 'suzhou/road2', False),
	Exit('east', 'suzhou/xidajie2', False),
]
ximen=Room('suzhou/ximen', u'西门', 'suzhou', 0, exits)

exits = [
	Exit('north', 'suzhou/majiu', False),
	Exit('northeast', 'suzhou/beidajie1', False),
]
xiyuan=Room('suzhou/xiyuan', u'戏园子', None, 0, exits)

exits = [
	Exit('north', 'suzhou/xidajie2', False),
]
xuanmiao=Room('suzhou/xuanmiao', u'玄妙观', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/xidajie1', False),
]
yamen=Room('suzhou/yamen', u'苏州府衙', 'suzhou', 0, exits)

exits = [
	Exit('southeast', 'suzhou/zhenquting', False),
	Exit('west', 'suzhou/shizilin', False),
]
yanyutang=Room('suzhou/yanyutang', u'燕誉堂', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/dongdajie2', False),
]
yaopu=Room('suzhou/yaopu', u'立春堂', 'suzhou', 0, exits)

exits = [
	Exit('southeast', 'suzhou/xidajie1', False),
]
yunhematou=Room('suzhou/yunhematou', u'运河码头', 'suzhou', 0, exits)

exits = [
	Exit('out', 'suzhou/hanshansi', False),
	Exit('east', 'suzhou/hanshidian', False),
]
zhengdian=Room('suzhou/zhengdian', u'正殿', None, 0, exits)

exits = [
	Exit('southwest', 'suzhou/shijianshi', False),
	Exit('north', 'suzhou/sunwuting', False),
]
zhenniang=Room('suzhou/zhenniang', u'真娘墓', 'suzhou', 0, exits)

exits = [
	Exit('northwest', 'suzhou/yanyutang', False),
	Exit('east', 'suzhou/wenmeige', False),
]
zhenquting=Room('suzhou/zhenquting', u'真趣亭', 'suzhou', 0, exits)

exits = [
	Exit('south', 'suzhou/shijianshi', False),
]
zhenshi=Room('suzhou/zhenshi', u'枕石', 'suzhou', 0, exits)

exits = [
	Exit('southwest', 'suzhou/shizilin', False),
]
zhipoxuan=Room('suzhou/zhipoxuan', u'揖峰指柏轩', 'suzhou', 0, exits)

exits = [
	Exit('southeast', 'suzhou/qianrenshi', False),
]
zhishuang=Room('suzhou/zhishuang', u'致爽阁', 'suzhou', 0, exits)

exits = [
	Exit('east', 'suzhou/beidajie2', False),
]
zijinan=Room('suzhou/zijinan', u'紫金庵', 'suzhou', 1, exits)

