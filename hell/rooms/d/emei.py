# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('southeast', 'emei/qingyinge', False),
	Exit('west', 'emei/gudelin2', False),
	Exit('northup', 'emei/wannianan', False),
	Exit('east', 'emei/gudelin1', False),
]
bailongdong=Room('emei/bailongdong', u'白龙洞', 'emei', 0, exits)

exits = [
	Exit('southeast', 'emei/lengsl2', False),
	Exit('southwest', 'emei/bashisipan2', False),
	Exit('northdown', 'emei/leidongping', False),
]
bashisipan1=Room('emei/bashisipan1', u'八十四盘', 'emei', 0, exits)

exits = [
	Exit('southup', 'emei/bashisipan3', False),
	Exit('east', 'emei/lengsl3', False),
	Exit('northeast', 'emei/bashisipan1', False),
]
bashisipan2=Room('emei/bashisipan2', u'八十四盘', 'emei', 0, exits)

exits = [
	Exit('southeast', 'emei/jieyindian', False),
	Exit('northeast', 'emei/lengsl4', False),
	Exit('northdown', 'emei/bashisipan2', False),
]
bashisipan3=Room('emei/bashisipan3', u'八十四盘', 'emei', 0, exits)

exits = [
	Exit('west', 'emei/bgsxq', False),
	Exit('southwest', 'emei/milin1', False),
	Exit('east', 'emei/bgsgate', False),
	Exit('enter', 'emei/dxdian', False),
]
bgs=Room('emei/bgs', u'报国寺', 'emei', 0, exits)

exits = [
	Exit('east', 'emei/dxdian', False),
]
bgschanfang=Room('emei/bgschanfang', u'保国寺禅房', None, 0, exits)

exits = [
	Exit('west', 'emei/bgs', False),
	Exit('northdown', 'emei/qsjie2', False),
]
bgsgate=Room('emei/bgsgate', u'报国寺山门', 'emei', 0, exits)

exits = [
	Exit('east', 'emei/bgs', False),
]
bgsxq=Room('emei/bgsxq', u'报国寺西墙', 'emei', 0, exits)

exits = [
	Exit('down', 'emei/chuwujian', False),
]
cangjingge=Room('emei/cangjingge', u'藏经阁', None, 0, exits)

exits = [
	Exit('south', 'emei/dxdian', False),
]
cangjinglou=Room('emei/cangjinglou', u'藏经楼', None, 0, exits)

exits = [
	Exit('west', 'emei/majiu1', False),
	Exit('east', 'emei/qsjie2', False),
]
caopeng=Room('emei/caopeng', u'草棚', 'emei', 0, exits)

exits = [
	Exit('eastdown', 'emei/guiyunge', False),
	Exit('westup', 'emei/shenshuian', False),
]
chunyangdian=Room('emei/chunyangdian', u'纯阳殿', 'emei', 0, exits)

exits = [
	Exit('north', 'emei/hcazhaitang', False),
	Exit('up', 'emei/cangjingge', False),
]
chuwujian=Room('emei/chuwujian', u'储物间', None, 0, exits)

exits = [
	Exit('east', 'emei/duguangtai', False),
	Exit('enter', 'emei/woyunan', False),
]
dgtsheshenya=Room('emei/dgtsheshenya', u'睹光台舍身崖', 'emei', 0, exits)

exits = [
	Exit('west', 'emei/dgtsheshenya', False),
	Exit('north', 'emei/huacangan', False),
]
duguangtai=Room('emei/duguangtai', u'睹光台', 'emei', 0, exits)

exits = [
	Exit('out', 'emei/bgs', False),
	Exit('west', 'emei/bgschanfang', False),
	Exit('north', 'emei/cangjinglou', False),
]
dxdian=Room('emei/dxdian', u'大雄殿', None, 0, exits)

exits = [
	Exit('east', 'emei/milin1', False),
	Exit('westup', 'emei/milin2', False),
]
fhs=Room('emei/fhs', u'伏虎寺', 'emei', 0, exits)

exits = [
	Exit('west', 'emei/lingwenge', False),
]
fsachanfang=Room('emei/fsachanfang', u'禅房', None, 0, exits)

exits = [
	Exit('southdown', 'emei/fsazhaitang', True),
]
fsaxiuxishi=Room('emei/fsaxiuxishi', u'福寿庵休息室', None, 0, exits)

exits = [
	Exit('northup', 'emei/fsaxiuxishi', True),
	Exit('east', 'emei/lingwenge', False),
]
fsazhaitang=Room('emei/fsazhaitang', u'福寿庵斋堂', None, 0, exits)

exits = [
	Exit('north', 'emei/shenshuian', False),
	Exit('enter', 'emei/lingwenge', False),
]
fushouan=Room('emei/fushouan', u'福寿庵', 'emei', 0, exits)

exits = [
	Exit('eastdown', 'emei/jietuopo', False),
	Exit('westup', 'emei/guiyunge', False),
]
guanyintang=Room('emei/guanyintang', u'观音堂', 'emei', 0, exits)

exits = [
	Exit('southeast', 'emei/gudelin2', False),
	Exit('northwest', 'emei/gudelin2', False),
	Exit('south', 'emei/bailongdong', False),
	Exit('southwest', 'emei/gudelin2', False),
	Exit('northeast', 'emei/gudelin2', False),
]
gudelin1=Room('emei/gudelin1', u'古德林', 'emei', 0, exits)

exits = [
	Exit('southeast', 'emei/gudelin1', False),
	Exit('northwest', 'emei/gudelin1', False),
	Exit('south', 'emei/bailongdong', False),
	Exit('southwest', 'emei/gudelin1', False),
	Exit('northeast', 'emei/gudelin1', False),
]
gudelin2=Room('emei/gudelin2', u'古德林', 'emei', 0, exits)

exits = [
	Exit('southup', 'emei/yunufeng', False),
	Exit('eastdown', 'emei/guanyintang', False),
	Exit('westup', 'emei/chunyangdian', False),
]
guiyunge=Room('emei/guiyunge', u'归云阁', 'emei', 0, exits)

exits = [
	Exit('south', 'emei/hcaxiuxishi', False),
	Exit('north', 'emei/hcawest2', False),
]
hcachanfang=Room('emei/hcachanfang', u'华藏庵禅房', None, 0, exits)

exits = [
	Exit('south', 'emei/hcahoudian', False),
	Exit('northdown', 'emei/hcaguangchang', False),
]
hcadadian=Room('emei/hcadadian', u'大雄宝殿', None, 0, exits)

exits = [
	Exit('west', 'emei/hcazhengdian', False),
]
hcaeast=Room('emei/hcaeast', u'华藏庵侧殿', None, 0, exits)

exits = [
	Exit('west', 'emei/hcaguangchang', False),
	Exit('south', 'emei/hcaeast2', False),
]
hcaeast1=Room('emei/hcaeast1', u'华藏庵东廊', 'emei', 0, exits)

exits = [
	Exit('south', 'emei/hcazhaitang', False),
	Exit('north', 'emei/hcaeast1', False),
]
hcaeast2=Room('emei/hcaeast2', u'华藏庵东廊', 'emei', 0, exits)

exits = [
	Exit('west', 'emei/hcawest1', False),
	Exit('southup', 'emei/hcadadian', False),
	Exit('east', 'emei/hcaeast1', False),
	Exit('north', 'emei/hcazhengdian', False),
]
hcaguangchang=Room('emei/hcaguangchang', u'华藏庵广场', 'emei', 0, exits)

exits = [
	Exit('north', 'emei/hcadadian', False),
]
hcahoudian=Room('emei/hcahoudian', u'华藏庵后殿', None, 0, exits)

exits = [
	Exit('east', 'emei/hcazhengdian', False),
]
hcawest=Room('emei/hcawest', u'华藏庵侧殿', None, 0, exits)

exits = [
	Exit('south', 'emei/hcawest2', False),
	Exit('east', 'emei/hcaguangchang', False),
]
hcawest1=Room('emei/hcawest1', u'华藏庵西廊', 'emei', 0, exits)

exits = [
	Exit('south', 'emei/hcachanfang', False),
	Exit('north', 'emei/hcawest1', False),
]
hcawest2=Room('emei/hcawest2', u'华藏庵西廊', 'emei', 0, exits)

exits = [
	Exit('north', 'emei/hcachanfang', False),
]
hcaxiuxishi=Room('emei/hcaxiuxishi', u'华藏庵休息室', None, 0, exits)

exits = [
	Exit('south', 'emei/chuwujian', False),
	Exit('north', 'emei/hcaeast2', False),
]
hcazhaitang=Room('emei/hcazhaitang', u'华藏庵斋堂', None, 0, exits)

exits = [
	Exit('west', 'emei/hcawest', False),
	Exit('out', 'emei/huacangan', False),
	Exit('south', 'emei/hcaguangchang', False),
	Exit('east', 'emei/hcaeast', False),
]
hcazhengdian=Room('emei/hcazhengdian', u'华藏庵正殿', None, 0, exits)

exits = [
	Exit('south', 'emei/heilong2', False),
	Exit('northeast', 'emei/qingyinge', False),
]
heilong1=Room('emei/heilong1', u'黑龙江栈道', 'emei', 0, exits)

exits = [
	Exit('south', 'emei/qianfoan', False),
	Exit('north', 'emei/heilong1', False),
]
heilong2=Room('emei/heilong2', u'黑龙江栈道', 'emei', 0, exits)

exits = [
	Exit('northwest', 'emei/woyunan', False),
	Exit('south', 'emei/duguangtai', False),
	Exit('north', 'emei/jinding', False),
	Exit('enter', 'emei/hcazhengdian', False),
]
huacangan=Room('emei/huacangan', u'华藏庵', 'emei', 0, exits)

exits = [
	Exit('south', 'emei/majiu2', False),
	Exit('northeast', 'emei/shierpan4', False),
	Exit('westup', 'emei/lianhuashi', False),
]
huayanding=Room('emei/huayanding', u'华严顶', 'emei', 0, exits)

exits = [
	Exit('eastdown', 'emei/milin2', False),
	Exit('westup', 'emei/guanyintang', False),
]
jietuopo=Room('emei/jietuopo', u'解脱坡', 'emei', 0, exits)

exits = [
	Exit('northwest', 'emei/bashisipan3', False),
	Exit('westup', 'emei/wanxingan', False),
]
jieyindian=Room('emei/jieyindian', u'接引殿', 'emei', 0, exits)

exits = [
	Exit('south', 'emei/huacangan', False),
	Exit('southwest', 'emei/woyunan', False),
	Exit('northdown', 'emei/wanxingan', False),
]
jinding=Room('emei/jinding', u'金顶', 'emei', 0, exits)

exits = [
	Exit('west', 'emei/jldongnei', False),
	Exit('out', 'emei/jldongkou', False),
	Exit('south', 'emei/jldongnei', False),
	Exit('east', 'emei/jldongnei', False),
	Exit('north', 'emei/jldongnei', False),
]
jiulaodong=Room('emei/jiulaodong', u'九老洞', None, 0, exits)

exits = [
	Exit('northwest', 'emei/lianhuashi', False),
	Exit('northeast', 'emei/jsjdg4', False),
	Exit('enter', 'emei/jiulaodong', False),
]
jldongkou=Room('emei/jldongkou', u'九老洞口', 'emei', 0, exits)

exits = [
	Exit('out', 'emei/jiulaodong', False),
]
jldongnei=Room('emei/jldongnei', u'九老洞', None, 0, exits)

exits = [
	Exit('northeast', 'emei/qianfoan', False),
	Exit('westup', 'emei/jsjdg2', False),
]
jsjdg1=Room('emei/jsjdg1', u'九十九道拐', 'emei', 0, exits)

exits = [
	Exit('eastdown', 'emei/jsjdg1', False),
	Exit('southwest', 'emei/jsjdg3', False),
]
jsjdg2=Room('emei/jsjdg2', u'九十九道拐', 'emei', 0, exits)

exits = [
	Exit('northeast', 'emei/jsjdg2', False),
	Exit('westup', 'emei/jsjdg4', False),
]
jsjdg3=Room('emei/jsjdg3', u'九十九道拐', 'emei', 0, exits)

exits = [
	Exit('eastdown', 'emei/jsjdg3', False),
	Exit('southwest', 'emei/jldongkou', False),
]
jsjdg4=Room('emei/jsjdg4', u'九十九道拐', 'emei', 0, exits)

exits = [
	Exit('southup', 'emei/bashisipan1', False),
	Exit('east', 'emei/lengsl1', False),
	Exit('northdown', 'emei/lingyunti', False),
]
leidongping=Room('emei/leidongping', u'雷洞坪', 'emei', 0, exits)

exits = [
	Exit('west', 'emei/leidongping', False),
	Exit('southup', 'emei/lengsl2', False),
	Exit('northdown', 'emei/lingyunti', False),
]
lengsl1=Room('emei/lengsl1', u'冷杉林', None, 0, exits)

exits = [
	Exit('southwest', 'emei/lengsl3', False),
	Exit('northdown', 'emei/lengsl1', False),
	Exit('east', 'emei/bashisipan1', False),
]
lengsl2=Room('emei/lengsl2', u'冷杉林', None, 0, exits)

exits = [
	Exit('west', 'emei/bashisipan2', False),
	Exit('southup', 'emei/lengsl4', False),
	Exit('northeast', 'emei/lengsl2', False),
]
lengsl3=Room('emei/lengsl3', u'冷杉林', None, 0, exits)

exits = [
	Exit('southeast', 'emei/jieyindian', False),
	Exit('southwest', 'emei/bashisipan3', False),
	Exit('northdown', 'emei/lengsl3', False),
]
lengsl4=Room('emei/lengsl4', u'冷杉林', None, 0, exits)

exits = [
	Exit('southeast', 'emei/jldongkou', False),
	Exit('eastdown', 'emei/huayanding', False),
	Exit('westup', 'emei/ztpo1', False),
]
lianhuashi=Room('emei/lianhuashi', u'莲花石', 'emei', 0, exits)

exits = [
	Exit('west', 'emei/fsazhaitang', False),
	Exit('out', 'emei/fushouan', False),
	Exit('east', 'emei/fsachanfang', False),
]
lingwenge=Room('emei/lingwenge', u'灵文阁', None, 0, exits)

exits = [
	Exit('southup', 'emei/leidongping', False),
	Exit('northdown', 'emei/xixiangchi', False),
]
lingyunti=Room('emei/lingyunti', u'凌云梯', 'emei', 0, exits)

exits = [
	Exit('east', 'emei/caopeng', False),
]
majiu1=Room('emei/majiu1', u'马厩', 'emei', 0, exits)

exits = [
	Exit('south', 'emei/huayanding', False),
]
majiu2=Room('emei/majiu2', u'马厩', 'emei', 0, exits)

exits = [
	Exit('west', 'emei/fhs', False),
	Exit('northeast', 'emei/bgs', False),
]
milin1=Room('emei/milin1', u'密林', 'emei', 0, exits)

exits = [
	Exit('eastdown', 'emei/fhs', False),
	Exit('westup', 'emei/jietuopo', False),
]
milin2=Room('emei/milin2', u'密林', 'emei', 0, exits)

exits = [
	Exit('west', 'emei/qfadadian', False),
]
qfachanfang=Room('emei/qfachanfang', u'禅房', None, 0, exits)

exits = [
	Exit('out', 'emei/qianfoan', False),
	Exit('east', 'emei/qfachanfang', False),
]
qfadadian=Room('emei/qfadadian', u'千佛庵大殿', None, 0, exits)

exits = [
	Exit('southwest', 'emei/jsjdg1', False),
	Exit('north', 'emei/heilong2', False),
	Exit('enter', 'emei/qfadadian', False),
]
qianfoan=Room('emei/qianfoan', u'千佛庵', 'emei', 0, exits)

exits = [
	Exit('south', 'emei/xiaoshulin4', False),
]
qinggong=Room('emei/qinggong', u'峨嵋寝宫', None, 0, exits)

exits = [
	Exit('southeast', 'emei/zhongfengsi', False),
	Exit('northwest', 'emei/bailongdong', False),
	Exit('southwest', 'emei/heilong1', False),
]
qingyinge=Room('emei/qingyinge', u'清音阁', 'emei', 0, exits)

exits = [
	Exit('west', 'city3/road1', False),
	Exit('southwest', 'emei/qsjie2', False),
	Exit('north', 'emei/xiaolu2', False),
]
qsjie1=Room('emei/qsjie1', u'青石阶', 'emei', 0, exits)

exits = [
	Exit('west', 'emei/caopeng', False),
	Exit('southup', 'emei/bgsgate', False),
	Exit('southwest', 'dali/road1', False),
	Exit('northeast', 'emei/qsjie1', False),
]
qsjie2=Room('emei/qsjie2', u'青石阶', 'emei', 0, exits)

exits = [
	Exit('south', 'emei/fushouan', False),
	Exit('eastdown', 'emei/chunyangdian', False),
	Exit('westup', 'emei/zhongfengsi', False),
]
shenshuian=Room('emei/shenshuian', u'神水庵', 'emei', 0, exits)

exits = [
	Exit('eastdown', 'emei/wannianan', False),
	Exit('southwest', 'emei/shierpan2', False),
]
shierpan1=Room('emei/shierpan1', u'十二盘', 'emei', 0, exits)

exits = [
	Exit('northeast', 'emei/shierpan1', False),
	Exit('westup', 'emei/shierpan3', False),
]
shierpan2=Room('emei/shierpan2', u'十二盘', 'emei', 0, exits)

exits = [
	Exit('eastdown', 'emei/shierpan2', False),
	Exit('southwest', 'emei/shierpan4', False),
]
shierpan3=Room('emei/shierpan3', u'十二盘', 'emei', 0, exits)

exits = [
	Exit('southwest', 'emei/huayanding', False),
	Exit('northeast', 'emei/shierpan3', False),
]
shierpan4=Room('emei/shierpan4', u'十二盘', 'emei', 0, exits)

exits = [
	Exit('east', 'emei/st8', False),
]
ssyb=Room('emei/ssyb', u'舍身崖壁', 'emei', 0, exits)

exits = [
]
st0=Room('emei/st0', u'深潭', None, 0, exits)

exits = [
]
st1=Room('emei/st1', u'深潭', None, 0, exits)

exits = [
]
st2=Room('emei/st2', u'深潭', None, 0, exits)

exits = [
]
st3=Room('emei/st3', u'深潭', None, 0, exits)

exits = [
]
st4=Room('emei/st4', u'深潭', None, 0, exits)

exits = [
]
st5=Room('emei/st5', u'深潭', None, 0, exits)

exits = [
]
st6=Room('emei/st6', u'深潭', None, 0, exits)

exits = [
]
st7=Room('emei/st7', u'深潭', None, 0, exits)

exits = [
]
st8=Room('emei/st8', u'深潭', None, 0, exits)

exits = [
	Exit('southdown', 'emei/bailongdong', False),
	Exit('enter', 'emei/wnadian', False),
	Exit('westup', 'emei/shierpan1', False),
]
wannianan=Room('emei/wannianan', u'万年庵', 'emei', 0, exits)

exits = [
	Exit('southup', 'emei/jinding', False),
	Exit('eastdown', 'emei/jieyindian', False),
]
wanxingan=Room('emei/wanxingan', u'万行庵', 'emei', 0, exits)

exits = [
	Exit('southwest', 'emei/xiaolu1', False),
	Exit('northeast', 'wudang/sanbuguan', False),
]
wdroad=Room('emei/wdroad', u'大道', 'wudang', 0, exits)

exits = [
	Exit('west', 'emei/wnadian', False),
]
wnachanfang=Room('emei/wnachanfang', u'禅房', None, 0, exits)

exits = [
	Exit('out', 'emei/wannianan', False),
	Exit('east', 'emei/wnachanfang', False),
]
wnadian=Room('emei/wnadian', u'万年庵砖殿', None, 0, exits)

exits = [
	Exit('southeast', 'emei/huacangan', False),
	Exit('out', 'emei/dgtsheshenya', False),
	Exit('northeast', 'emei/jinding', False),
]
woyunan=Room('emei/woyunan', u'卧云庵', 'emei', 0, exits)

exits = [
	Exit('west', 'emei/xiaolu2', False),
	Exit('northeast', 'emei/wdroad', False),
]
xiaolu1=Room('emei/xiaolu1', u'小路', 'emei', 0, exits)

exits = [
	Exit('south', 'emei/qsjie1', False),
	Exit('east', 'emei/xiaolu1', False),
]
xiaolu2=Room('emei/xiaolu2', u'小路', 'emei', 0, exits)

exits = [
	Exit('south', 'emei/xiaoshulin2', False),
]
xiaoshulin1=Room('emei/xiaoshulin1', u'小树林', 'emei', 0, exits)

exits = [
	Exit('south', 'emei/xiaoshulin3', False),
	Exit('north', 'emei/xiaoshulin1', False),
]
xiaoshulin2=Room('emei/xiaoshulin2', u'小树林', 'emei', 0, exits)

exits = [
	Exit('southeast', 'emei/xiaoshulin4', False),
	Exit('north', 'emei/xiaoshulin2', False),
]
xiaoshulin3=Room('emei/xiaoshulin3', u'小树林', 'emei', 0, exits)

exits = [
	Exit('northwest', 'emei/xiaoshulin3', False),
	Exit('north', 'emei/qinggong', False),
]
xiaoshulin4=Room('emei/xiaoshulin4', u'小树林', 'emei', 0, exits)

exits = [
	Exit('southup', 'emei/lingyunti', False),
	Exit('eastdown', 'emei/ztpo2', False),
]
xixiangchi=Room('emei/xixiangchi', u'洗象池', 'emei', 0, exits)

exits = [
	Exit('northdown', 'emei/guiyunge', False),
]
yunufeng=Room('emei/yunufeng', u'玉女峰', 'emei', 0, exits)

exits = [
	Exit('northwest', 'emei/qingyinge', False),
	Exit('eastdown', 'emei/shenshuian', False),
]
zhongfengsi=Room('emei/zhongfengsi', u'中峰寺', 'emei', 0, exits)

exits = [
	Exit('eastdown', 'emei/lianhuashi', False),
	Exit('westup', 'emei/ztpo2', False),
]
ztpo1=Room('emei/ztpo1', u'钻天坡', 'emei', 0, exits)

exits = [
	Exit('eastdown', 'emei/ztpo1', False),
	Exit('westup', 'emei/xixiangchi', False),
]
ztpo2=Room('emei/ztpo2', u'钻天坡', 'emei', 0, exits)

