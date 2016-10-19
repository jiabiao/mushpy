# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('southdown', 'wudang/xilang', False),
]
cangjingge=Room('wudang/cangjingge', u'藏经阁', None, 0, exits)

exits = [
	Exit('north', 'wudang/caolianfang', False),
]
caolian1=Room('wudang/caolian1', u'南间操练房', None, 0, exits)

exits = [
	Exit('south', 'wudang/caolianfang', False),
]
caolian2=Room('wudang/caolian2', u'北间操练房', None, 0, exits)

exits = [
	Exit('east', 'wudang/caolianfang', False),
]
caolian3=Room('wudang/caolian3', u'西间操练房', None, 0, exits)

exits = [
	Exit('west', 'wudang/caolian3', False),
	Exit('eastdown', 'wudang/xilang', False),
	Exit('south', 'wudang/caolian1', False),
	Exit('north', 'wudang/caolian2', False),
]
caolianfang=Room('wudang/caolianfang', u'操练房', None, 0, exits)

exits = [
	Exit('south', 'wudang/huixianqiao', False),
	Exit('northdown', 'wudang/hutouyan', False),
]
chaotiangong=Room('wudang/chaotiangong', u'朝天宫', 'wudang', 0, exits)

exits = [
	Exit('north', 'wudang/donglang2', False),
]
chashi=Room('wudang/chashi', u'茶室', None, 0, exits)

exits = [
	Exit('west', 'wudang/sanqingdian', False),
	Exit('east', 'wudang/donglang2', False),
]
donglang1=Room('wudang/donglang1', u'东厢走廊', None, 0, exits)

exits = [
	Exit('west', 'wudang/donglang1', False),
	Exit('south', 'wudang/chashi', False),
	Exit('east', 'wudang/liangongfang', False),
]
donglang2=Room('wudang/donglang2', u'东厢走廊', None, 0, exits)

exits = [
	Exit('southup', 'wudang/santiangate', False),
	Exit('northdown', 'wudang/toutiangate', False),
]
ertiangate=Room('wudang/ertiangate', u'二天门', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/taizipo', False),
]
fuzhenguan=Room('wudang/fuzhenguan', u'复真观五层楼', 'wudang', 0, exits)

exits = [
	Exit('northdown', 'wudang/nanyangong', False),
]
gaotai=Room('wudang/gaotai', u'南岩宫高台', 'wudang', 0, exits)

exits = [
	Exit('eastdown', 'wudang/tyroad1', False),
	Exit('south', 'wudang/sanqingdian', False),
	Exit('east', 'wudang/shanlu2', False),
	Exit('northdown', 'wudang/zixiaogate', False),
]
guangchang=Room('wudang/guangchang', u'武当广场', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/tyroad13', False),
	Exit('east', 'wudang/gyroad2', False),
]
gyroad1=Room('wudang/gyroad1', u'果园小路', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/gyroad1', False),
]
gyroad2=Room('wudang/gyroad2', u'果园', 'wudang', 0, exits)

exits = [
	Exit('southdown', 'wudang/shanlu1', False),
	Exit('northdown', 'wudang/wdbl', False),
]
haohanpo=Room('wudang/haohanpo', u'好汉坡', 'wudang', 0, exits)

exits = [
	Exit('north', 'wudang/wdroad6', False),
]
house=Room('wudang/house', u'小土屋', None, 0, exits)

exits = [
	Exit('south', 'wudang/xiaolu1', False),
	Exit('north', 'wudang/sanqingdian', False),
]
houyuan=Room('wudang/houyuan', u'后院', None, 0, exits)

exits = [
	Exit('south', 'wudang/toutiangate', False),
	Exit('north', 'wudang/chaotiangong', False),
]
huixianqiao=Room('wudang/huixianqiao', u'会仙桥', 'wudang', 0, exits)

exits = [
	Exit('southup', 'wudang/chaotiangong', False),
	Exit('northdown', 'wudang/wulaofeng', False),
]
hutouyan=Room('wudang/hutouyan', u'虎头岩', 'wudang', 0, exits)

exits = [
	Exit('eastdown', 'wudang/slxl2', False),
	Exit('westup', 'wudang/slxl3', False),
]
jiejianyan=Room('wudang/jiejianyan', u'解剑岩', 'wudang', 0, exits)

exits = [
	Exit('north', 'wudang/zijincheng', False),
]
jindian=Room('wudang/jindian', u'金殿', None, 0, exits)

exits = [
	Exit('west', 'wudang/shierliantai', False),
	Exit('south', 'wudang/zijincheng', False),
	Exit('northdown', 'wudang/santiangate', False),
]
jinding=Room('wudang/jinding', u'金顶', 'wudang', 0, exits)

exits = [
	Exit('east', 'wudang/lameigt', False),
]
langmei=Room('wudang/langmei', u'榔梅园', 'wudang', 0, exits)

exits = [
	Exit('southup', 'wudang/wuyaling', False),
	Exit('northup', 'wudang/taiziyan', False),
	Exit('westup', 'wudang/nanyanfeng', False),
]
langmeiyuan=Room('wudang/langmeiyuan', u'榔梅园', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/donglang2', False),
]
liangongfang=Room('wudang/liangongfang', u'练功房', None, 0, exits)

exits = [
	Exit('west', 'wudang/shanlu1', False),
]
mozhenjing=Room('wudang/mozhenjing', u'磨针井', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/nanyan2', False),
	Exit('south', 'wudang/nanyan3', False),
	Exit('north', 'wudang/nanyan4', False),
	Exit('east', 'wudang/nanyan1', False),
	Exit('up', 'wudang/nanyangong', False),
]
nanyan0=Room('wudang/nanyan0', u'南岩宫地下室', None, 0, exits)

exits = [
	Exit('southeast', 'wudang/nanyan0', False),
	Exit('west', 'wudang/nanyan3', False),
	Exit('northwest', 'wudang/nanyan4', False),
	Exit('south', 'wudang/nanyan2', False),
	Exit('southwest', 'wudang/nanyan2', False),
	Exit('northeast', 'wudang/nanyan3', False),
	Exit('north', 'wudang/nanyan4', False),
	Exit('east', 'wudang/nanyan1', False),
]
nanyan1=Room('wudang/nanyan1', u'南岩迷宫', None, 0, exits)

exits = [
	Exit('southeast', 'wudang/nanyan1', False),
	Exit('west', 'wudang/nanyan3', False),
	Exit('northwest', 'wudang/nanyan4', False),
	Exit('south', 'wudang/nanyan2', False),
	Exit('southwest', 'wudang/nanyan0', False),
	Exit('northeast', 'wudang/nanyan3', False),
	Exit('north', 'wudang/nanyan4', False),
	Exit('east', 'wudang/nanyan1', False),
]
nanyan2=Room('wudang/nanyan2', u'南岩迷宫', None, 0, exits)

exits = [
	Exit('southeast', 'wudang/nanyan1', False),
	Exit('west', 'wudang/nanyan3', False),
	Exit('northwest', 'wudang/nanyan4', False),
	Exit('south', 'wudang/nanyan2', False),
	Exit('southwest', 'wudang/nanyan2', False),
	Exit('northeast', 'wudang/nanyan0', False),
	Exit('north', 'wudang/nanyan4', False),
	Exit('east', 'wudang/nanyan1', False),
]
nanyan3=Room('wudang/nanyan3', u'南岩迷宫', None, 0, exits)

exits = [
	Exit('southeast', 'wudang/nanyan1', False),
	Exit('west', 'wudang/nanyan3', False),
	Exit('northwest', 'wudang/nanyan0', False),
	Exit('south', 'wudang/nanyan2', False),
	Exit('southwest', 'wudang/nanyan2', False),
	Exit('northeast', 'wudang/nanyan3', False),
	Exit('north', 'wudang/nanyan4', False),
	Exit('east', 'wudang/nanyan1', False),
]
nanyan4=Room('wudang/nanyan4', u'南岩迷宫', None, 0, exits)

exits = [
	Exit('southdown', 'wudang/shizhu', False),
	Exit('west', 'wudang/sheshenya', False),
	Exit('eastdown', 'wudang/langmeiyuan', False),
]
nanyanfeng=Room('wudang/nanyanfeng', u'南岩峰', 'wudang', 0, exits)

exits = [
	Exit('out', 'wudang/shizhu', False),
	Exit('southup', 'wudang/gaotai', False),
]
nanyangong=Room('wudang/nanyangong', u'南岩宫', None, 0, exits)

exits = [
	Exit('southeast', 'wudang/wdroad9', False),
	Exit('southwest', 'emei/wdroad', False),
	Exit('east', 'wudang/wdroad8', False),
]
sanbuguan=Room('wudang/sanbuguan', u'三不管', 'wudang', 0, exits)

exits = [
	Exit('southup', 'wudang/wulaofeng', False),
	Exit('northdown', 'wudang/wuyaling', False),
]
sanlaofeng=Room('wudang/sanlaofeng', u'三老峰', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/xilang', False),
	Exit('south', 'wudang/houyuan', False),
	Exit('east', 'wudang/donglang1', False),
	Exit('north', 'wudang/guangchang', False),
]
sanqingdian=Room('wudang/sanqingdian', u'三清殿', None, 0, exits)

exits = [
	Exit('southup', 'wudang/jinding', False),
	Exit('northdown', 'wudang/ertiangate', False),
]
santiangate=Room('wudang/santiangate', u'三天门', 'wudang', 0, exits)

exits = [
	Exit('southup', 'wudang/taizipo', False),
	Exit('northup', 'wudang/haohanpo', False),
	Exit('east', 'wudang/mozhenjing', False),
]
shanlu1=Room('wudang/shanlu1', u'山路', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/guangchang', False),
	Exit('east', 'wudang/shanlu3', False),
]
shanlu2=Room('wudang/shanlu2', u'山路', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/shanlu2', False),
	Exit('southup', 'wudang/shanlu4', False),
]
shanlu3=Room('wudang/shanlu3', u'山路', 'wudang', 0, exits)

exits = [
	Exit('southup', 'wudang/taiziyan', False),
	Exit('northdown', 'wudang/shanlu3', False),
]
shanlu4=Room('wudang/shanlu4', u'山路', 'wudang', 0, exits)

exits = [
	Exit('east', 'wudang/nanyanfeng', False),
]
sheshenya=Room('wudang/sheshenya', u'舍身崖', 'wudang', 0, exits)

exits = [
	Exit('southup', 'wudang/shijie2', False),
	Exit('northdown', 'wudang/shiliang', False),
]
shibapan=Room('wudang/shibapan', u'十八盘', 'wudang', 0, exits)

exits = [
	Exit('east', 'wudang/jinding', False),
]
shierliantai=Room('wudang/shierliantai', u'十二莲台', 'wudang', 0, exits)

exits = [
	Exit('southup', 'wudang/yuzhengong', False),
	Exit('northdown', 'wudang/xuanyuegate', False),
]
shijie1=Room('wudang/shijie1', u'石阶', 'wudang', 0, exits)

exits = [
	Exit('southup', 'wudang/zixiaogate', False),
	Exit('northdown', 'wudang/shibapan', False),
]
shijie2=Room('wudang/shijie2', u'石阶', 'wudang', 0, exits)

exits = [
	Exit('southup', 'wudang/shibapan', False),
	Exit('northup', 'wudang/taizipo', False),
	Exit('east', 'wudang/shop', False),
]
shiliang=Room('wudang/shiliang', u'石梁', 'wudang', 0, exits)

exits = [
	Exit('northup', 'wudang/nanyanfeng', False),
	Exit('enter', 'wudang/nanyangong', False),
]
shizhu=Room('wudang/shizhu', u'石柱', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/shiliang', False),
]
shop=Room('wudang/shop', u'小吃店', None, 0, exits)

exits = [
	Exit('west', 'wudang/slxl2', False),
	Exit('east', 'wudang/wdroad10', False),
]
slxl1=Room('wudang/slxl1', u'松林小路', 'wudang', 0, exits)

exits = [
	Exit('south', 'wudang/songlin1', False),
	Exit('north', 'wudang/songlin2', False),
	Exit('east', 'wudang/slxl1', False),
	Exit('westup', 'wudang/jiejianyan', False),
]
slxl2=Room('wudang/slxl2', u'松林小路', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/xuanyuegate', False),
	Exit('eastdown', 'wudang/jiejianyan', False),
]
slxl3=Room('wudang/slxl3', u'松林小路', 'wudang', 0, exits)

exits = [
	Exit('south', 'wudang/songlin3', False),
	Exit('north', 'wudang/slxl2', False),
]
songlin1=Room('wudang/songlin1', u'松林', 'wudang', 0, exits)

exits = [
	Exit('south', 'wudang/slxl2', False),
	Exit('north', 'wudang/songlin4', False),
]
songlin2=Room('wudang/songlin2', u'松林', 'wudang', 0, exits)

exits = [
	Exit('north', 'wudang/songlin1', False),
]
songlin3=Room('wudang/songlin3', u'松林', 'wudang', 0, exits)

exits = [
	Exit('south', 'wudang/songlin2', False),
]
songlin4=Room('wudang/songlin4', u'松林', 'wudang', 0, exits)

exits = [
	Exit('southdown', 'wudang/shiliang', False),
	Exit('east', 'wudang/fuzhenguan', False),
	Exit('northdown', 'wudang/shanlu1', False),
]
taizipo=Room('wudang/taizipo', u'太子坡', 'wudang', 0, exits)

exits = [
	Exit('southdown', 'wudang/langmeiyuan', False),
	Exit('northdown', 'wudang/shanlu4', False),
]
taiziyan=Room('wudang/taiziyan', u'太子岩', 'wudang', 0, exits)

exits = [
	Exit('southup', 'wudang/ertiangate', False),
	Exit('north', 'wudang/huixianqiao', False),
]
toutiangate=Room('wudang/toutiangate', u'头天门', 'wudang', 0, exits)

exits = [
	Exit('south', 'wudang/tufeiwo2', False),
	Exit('northdown', 'wudang/wdroad10', False),
]
tufeiwo1=Room('wudang/tufeiwo1', u'林中小路', 'wudang', 0, exits)

exits = [
	Exit('north', 'wudang/tufeiwo1', False),
	Exit('east', 'wudang/tufeiwo3', False),
]
tufeiwo2=Room('wudang/tufeiwo2', u'林中小路', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/tufeiwo2', False),
]
tufeiwo3=Room('wudang/tufeiwo3', u'林中小路', 'wudang', 0, exits)

exits = [
	Exit('south', 'wudang/tyroad10', False),
]
tygate1=Room('wudang/tygate1', u'桃园篱笆', 'wudang', 0, exits)

exits = [
	Exit('north', 'wudang/tyroad10', False),
]
tygate2=Room('wudang/tygate2', u'桃园木门', 'wudang', 0, exits)

exits = [
	Exit('south', 'wudang/tyroad8', False),
]
tynroad=Room('wudang/tynroad', u'桃园小路', 'wudang', 0, exits)

exits = [
	Exit('east', 'wudang/tyroad2', False),
	Exit('westup', 'wudang/guangchang', False),
]
tyroad1=Room('wudang/tyroad1', u'石阶', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/tyroad9', False),
	Exit('south', 'wudang/tygate2', False),
	Exit('north', 'wudang/tygate1', False),
	Exit('east', 'wudang/tyroad11', False),
]
tyroad10=Room('wudang/tyroad10', u'桃园小路', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/tyroad10', False),
	Exit('east', 'wudang/tyroad12', False),
]
tyroad11=Room('wudang/tyroad11', u'桃园小路', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/tyroad11', False),
	Exit('east', 'wudang/tyroad13', False),
]
tyroad12=Room('wudang/tyroad12', u'桃园小路', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/tyroad12', False),
	Exit('east', 'wudang/gyroad1', False),
]
tyroad13=Room('wudang/tyroad13', u'桃园', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/tyroad1', False),
	Exit('east', 'wudang/tyroad3', False),
]
tyroad2=Room('wudang/tyroad2', u'石阶', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/tyroad2', False),
	Exit('eastdown', 'wudang/tyroad4', False),
]
tyroad3=Room('wudang/tyroad3', u'石阶', 'wudang', 0, exits)

exits = [
	Exit('southdown', 'wudang/tyroad5', False),
	Exit('westup', 'wudang/tyroad3', False),
]
tyroad4=Room('wudang/tyroad4', u'崎岖山路', 'wudang', 0, exits)

exits = [
	Exit('eastdown', 'wudang/tyroad6', False),
	Exit('northup', 'wudang/tyroad4', False),
]
tyroad5=Room('wudang/tyroad5', u'崎岖山路', 'wudang', 0, exits)

exits = [
	Exit('southdown', 'wudang/tyroad7', False),
	Exit('westup', 'wudang/tyroad5', False),
]
tyroad6=Room('wudang/tyroad6', u'崎岖山路', 'wudang', 0, exits)

exits = [
	Exit('eastdown', 'wudang/tyroad8', False),
	Exit('northup', 'wudang/tyroad6', False),
]
tyroad7=Room('wudang/tyroad7', u'崎岖山路', 'wudang', 0, exits)

exits = [
	Exit('south', 'wudang/tysroad', False),
	Exit('north', 'wudang/tynroad', False),
	Exit('east', 'wudang/tyroad9', False),
	Exit('westup', 'wudang/tyroad7', False),
]
tyroad8=Room('wudang/tyroad8', u'桃园小路', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/tyroad8', False),
	Exit('east', 'wudang/tyroad10', False),
]
tyroad9=Room('wudang/tyroad9', u'桃园小路', 'wudang', 0, exits)

exits = [
	Exit('north', 'wudang/tyroad8', False),
]
tysroad=Room('wudang/tysroad', u'桃园小路', 'wudang', 0, exits)

exits = [
	Exit('southup', 'wudang/haohanpo', False),
	Exit('northdown', 'wudang/yuzhengong', False),
]
wdbl=Room('wudang/wdbl', u'武当柏林', 'wudang', 0, exits)

exits = [
	Exit('south', 'wudang/wdroad2', False),
	Exit('north', 'city/nanmen', False),
]
wdroad1=Room('wudang/wdroad1', u'青石大道', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/slxl1', False),
	Exit('southup', 'wudang/tufeiwo1', False),
	Exit('north', 'wudang/wdroad9', False),
]
wdroad10=Room('wudang/wdroad10', u'黄土路', 'wudang', 0, exits)

exits = [
	Exit('southeast', 'guiyun/yixing', False),
	Exit('south', 'wudang/wdroad3', False),
	Exit('north', 'wudang/wdroad1', False),
]
wdroad2=Room('wudang/wdroad2', u'青石大道', 'wudang', 0, exits)

exits = [
	Exit('south', 'wudang/wdroad4', False),
	Exit('north', 'wudang/wdroad2', False),
]
wdroad3=Room('wudang/wdroad3', u'青石大道', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/wdroad5', False),
	Exit('southup', 'henshan/hsroad1', False),
	Exit('north', 'wudang/wdroad3', False),
	Exit('east', 'xiaoyao/shulin3', False),
]
wdroad4=Room('wudang/wdroad4', u'青石大道', 'wudang', 0, exits)

exits = [
	Exit('northwest', 'wudang/wdroad6', False),
	Exit('east', 'wudang/wdroad4', False),
	Exit('north', 'xiangyang/caodi6', False),
]
wdroad5=Room('wudang/wdroad5', u'青石大道', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/wdroad7', False),
	Exit('southeast', 'wudang/wdroad5', False),
	Exit('south', 'wudang/house', False),
]
wdroad6=Room('wudang/wdroad6', u'小路', 'wudang', 0, exits)

exits = [
	Exit('southwest', 'wudang/wdroad8', False),
	Exit('east', 'wudang/wdroad6', False),
]
wdroad7=Room('wudang/wdroad7', u'小路', 'wudang', 0, exits)

exits = [
	Exit('west', 'wudang/sanbuguan', False),
	Exit('northeast', 'wudang/wdroad7', False),
]
wdroad8=Room('wudang/wdroad8', u'小路', 'wudang', 0, exits)

exits = [
	Exit('southeast', 'henshan/hsroad8', False),
	Exit('northwest', 'wudang/sanbuguan', False),
	Exit('south', 'wudang/wdroad10', False),
]
wdroad9=Room('wudang/wdroad9', u'黄土路', 'wudang', 0, exits)

exits = [
	Exit('southup', 'wudang/hutouyan', False),
	Exit('northdown', 'wudang/sanlaofeng', False),
]
wulaofeng=Room('wudang/wulaofeng', u'五老峰', 'wudang', 0, exits)

exits = [
	Exit('southup', 'wudang/sanlaofeng', False),
	Exit('northdown', 'wudang/langmeiyuan', False),
]
wuyaling=Room('wudang/wuyaling', u'乌鸦岭', 'wudang', 0, exits)

exits = [
	Exit('south', 'wudang/xiaolu2', False),
	Exit('north', 'wudang/houyuan', False),
]
xiaolu1=Room('wudang/xiaolu1', u'林间小径', 'wudang', 0, exits)

exits = [
	Exit('south', 'wudang/xiaoyuan', True),
	Exit('north', 'wudang/xiaolu1', False),
]
xiaolu2=Room('wudang/xiaolu2', u'林间小径', 'wudang', 0, exits)

exits = [
	Exit('north', 'wudang/xiaolu2', True),
]
xiaoyuan=Room('wudang/xiaoyuan', u'后山小院', None, 0, exits)

exits = [
	Exit('northup', 'wudang/cangjingge', False),
	Exit('east', 'wudang/sanqingdian', False),
	Exit('westup', 'wudang/caolianfang', False),
]
xilang=Room('wudang/xilang', u'西厢走廊', None, 0, exits)

exits = [
]
xiuxishi=Room('wudang/xiuxishi', u'休息室', None, 0, exits)

exits = [
	Exit('southup', 'wudang/shijie1', False),
	Exit('east', 'wudang/slxl3', False),
]
xuanyuegate=Room('wudang/xuanyuegate', u'玄岳门', 'wudang', 0, exits)

exits = [
	Exit('southup', 'wudang/wdbl', False),
	Exit('northdown', 'wudang/shijie1', False),
]
yuzhengong=Room('wudang/yuzhengong', u'遇真宫', 'wudang', 0, exits)

exits = [
	Exit('south', 'wudang/jindian', False),
	Exit('north', 'wudang/jinding', False),
]
zijincheng=Room('wudang/zijincheng', u'紫金城', 'wudang', 0, exits)

exits = [
	Exit('southup', 'wudang/guangchang', False),
	Exit('northdown', 'wudang/shijie2', False),
]
zixiaogate=Room('wudang/zixiaogate', u'紫霄宫大门', 'wudang', 0, exits)

