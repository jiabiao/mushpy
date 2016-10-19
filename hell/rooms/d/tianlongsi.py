# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'tianlongsi/munitang', False),
	Exit('north', 'tianlongsi/doushuai', False),
]
banruotai=Room('tianlongsi/banruotai', u'般若台', None, 0, exits)

exits = [
	Exit('north', 'tianlongsi/ta1', False),
]
baodian=Room('tianlongsi/baodian', u'崇圣宝殿', 'tianlongsi', 0, exits)

exits = [
	Exit('south', 'tianlongsi/sanwugong', False),
	Exit('east', 'tianlongsi/wuwujing', False),
]
cibeiyuan=Room('tianlongsi/cibeiyuan', u'慈悲院', None, 0, exits)

exits = [
	Exit('south', 'tianlongsi/dadao2', False),
	Exit('northeast', 'emei/qsjie2', False),
]
dadao1=Room('tianlongsi/dadao1', u'青石大道', 'tianlongsi', 0, exits)

exits = [
	Exit('west', 'tianlongsi/dadao3', False),
	Exit('north', 'tianlongsi/dadao1', False),
]
dadao2=Room('tianlongsi/dadao2', u'青石大道', 'tianlongsi', 0, exits)

exits = [
	Exit('west', 'tianlongsi/dadao4', False),
	Exit('east', 'tianlongsi/dadao2', False),
]
dadao3=Room('tianlongsi/dadao3', u'青石大道', 'tianlongsi', 0, exits)

exits = [
	Exit('south', 'tianlongsi/damen', False),
	Exit('east', 'tianlongsi/dadao3', False),
]
dadao4=Room('tianlongsi/dadao4', u'青石大道', 'tianlongsi', 0, exits)

exits = [
	Exit('south', 'tianlongsi/talin', False),
	Exit('north', 'dali/hongsheng', False),
]
damen=Room('tianlongsi/damen', u'大门', 'tianlongsi', 0, exits)

exits = [
	Exit('southwest', 'tianlongsi/doushuai', False),
	Exit('north', 'tianlongsi/yuhuayuan', False),
]
doumugong=Room('tianlongsi/doumugong', u'斗母宫', None, 0, exits)

exits = [
	Exit('northwest', 'tianlongsi/sanwugong', False),
	Exit('south', 'tianlongsi/banruotai', False),
	Exit('northeast', 'tianlongsi/doumugong', False),
	Exit('north', 'tianlongsi/qingxinge', False),
]
doushuai=Room('tianlongsi/doushuai', u'兜率大士院', None, 0, exits)

exits = [
	Exit('west', 'tianlongsi/wulege', False),
	Exit('south', 'tianlongsi/yaotai', False),
	Exit('east', 'tianlongsi/wuchangge', False),
]
huangtianmen=Room('tianlongsi/huangtianmen', u'晃天门', 'tianlongsi', 0, exits)

exits = [
	Exit('north', 'tianlongsi/banruotai', False),
]
munitang=Room('tianlongsi/munitang', u'牟尼堂', None, 0, exits)

exits = [
	Exit('south', 'tianlongsi/doushuai', False),
	Exit('north', 'tianlongsi/wuwujing', False),
]
qingxinge=Room('tianlongsi/qingxinge', u'清心阁', None, 0, exits)

exits = [
	Exit('south', 'tianlongsi/wuchangge', False),
	Exit('north', 'tianlongsi/wuwoge', False),
]
ruihemen=Room('tianlongsi/ruihemen', u'瑞鹤门', 'tianlongsi', 0, exits)

exits = [
	Exit('southeast', 'tianlongsi/doushuai', False),
	Exit('north', 'tianlongsi/cibeiyuan', False),
]
sanwugong=Room('tianlongsi/sanwugong', u'三无宫', None, 0, exits)

exits = [
	Exit('west', 'tianlongsi/wujingge', False),
	Exit('south', 'tianlongsi/baodian', False),
	Exit('north', 'tianlongsi/talin', False),
	Exit('east', 'tianlongsi/wuwoge', False),
]
ta1=Room('tianlongsi/ta1', u'舍利塔', 'tianlongsi', 0, exits)

exits = [
	Exit('west', 'tianlongsi/talin', False),
]
ta2=Room('tianlongsi/ta2', u'舍利塔', 'tianlongsi', 0, exits)

exits = [
	Exit('east', 'tianlongsi/talin', False),
]
ta3=Room('tianlongsi/ta3', u'舍利塔', 'tianlongsi', 0, exits)

exits = [
	Exit('down', 'tianlongsi/ta1', False),
]
tading=Room('tianlongsi/tading', u'塔顶', 'tianlongsi', 0, exits)

exits = [
	Exit('west', 'tianlongsi/ta3', False),
	Exit('south', 'tianlongsi/ta1', False),
	Exit('north', 'tianlongsi/damen', False),
	Exit('east', 'tianlongsi/ta2', False),
]
talin=Room('tianlongsi/talin', u'塔林', 'tianlongsi', 0, exits)

exits = [
	Exit('west', 'tianlongsi/huangtianmen', False),
	Exit('north', 'tianlongsi/ruihemen', False),
]
wuchangge=Room('tianlongsi/wuchangge', u'无常阁', None, 0, exits)

exits = [
	Exit('south', 'tianlongsi/xianghemen', False),
	Exit('east', 'tianlongsi/ta1', False),
]
wujingge=Room('tianlongsi/wujingge', u'无净阁', None, 0, exits)

exits = [
	Exit('east', 'tianlongsi/huangtianmen', False),
	Exit('north', 'tianlongsi/xianghemen', False),
]
wulege=Room('tianlongsi/wulege', u'无乐阁', None, 0, exits)

exits = [
	Exit('west', 'tianlongsi/ta1', False),
	Exit('south', 'tianlongsi/ruihemen', False),
]
wuwoge=Room('tianlongsi/wuwoge', u'无我阁', None, 0, exits)

exits = [
	Exit('west', 'tianlongsi/cibeiyuan', False),
	Exit('south', 'tianlongsi/qingxinge', False),
	Exit('east', 'tianlongsi/yuhuayuan', False),
	Exit('north', 'tianlongsi/yaotai', False),
]
wuwujing=Room('tianlongsi/wuwujing', u'无无境', 'tianlongsi', 0, exits)

exits = [
	Exit('south', 'tianlongsi/wulege', False),
	Exit('north', 'tianlongsi/wujingge', False),
]
xianghemen=Room('tianlongsi/xianghemen', u'翔鹤门', 'tianlongsi', 0, exits)

exits = [
	Exit('south', 'tianlongsi/wuwujing', False),
	Exit('north', 'tianlongsi/huangtianmen', False),
]
yaotai=Room('tianlongsi/yaotai', u'清都瑶台', 'tianlongsi', 0, exits)

exits = [
	Exit('west', 'tianlongsi/wuwujing', False),
	Exit('south', 'tianlongsi/doumugong', False),
]
yuhuayuan=Room('tianlongsi/yuhuayuan', u'雨花院', None, 0, exits)

