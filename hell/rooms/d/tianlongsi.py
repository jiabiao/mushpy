# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'tianlongsi/munitang', False),
	Exit('north', 'tianlongsi/doushuai', False),
]
banruotai=Room('tianlongsi/banruotai', u'����̨', None, 0, exits)

exits = [
	Exit('north', 'tianlongsi/ta1', False),
]
baodian=Room('tianlongsi/baodian', u'��ʥ����', 'tianlongsi', 0, exits)

exits = [
	Exit('south', 'tianlongsi/sanwugong', False),
	Exit('east', 'tianlongsi/wuwujing', False),
]
cibeiyuan=Room('tianlongsi/cibeiyuan', u'�ȱ�Ժ', None, 0, exits)

exits = [
	Exit('south', 'tianlongsi/dadao2', False),
	Exit('northeast', 'emei/qsjie2', False),
]
dadao1=Room('tianlongsi/dadao1', u'��ʯ���', 'tianlongsi', 0, exits)

exits = [
	Exit('west', 'tianlongsi/dadao3', False),
	Exit('north', 'tianlongsi/dadao1', False),
]
dadao2=Room('tianlongsi/dadao2', u'��ʯ���', 'tianlongsi', 0, exits)

exits = [
	Exit('west', 'tianlongsi/dadao4', False),
	Exit('east', 'tianlongsi/dadao2', False),
]
dadao3=Room('tianlongsi/dadao3', u'��ʯ���', 'tianlongsi', 0, exits)

exits = [
	Exit('south', 'tianlongsi/damen', False),
	Exit('east', 'tianlongsi/dadao3', False),
]
dadao4=Room('tianlongsi/dadao4', u'��ʯ���', 'tianlongsi', 0, exits)

exits = [
	Exit('south', 'tianlongsi/talin', False),
	Exit('north', 'dali/hongsheng', False),
]
damen=Room('tianlongsi/damen', u'����', 'tianlongsi', 0, exits)

exits = [
	Exit('southwest', 'tianlongsi/doushuai', False),
	Exit('north', 'tianlongsi/yuhuayuan', False),
]
doumugong=Room('tianlongsi/doumugong', u'��ĸ��', None, 0, exits)

exits = [
	Exit('northwest', 'tianlongsi/sanwugong', False),
	Exit('south', 'tianlongsi/banruotai', False),
	Exit('northeast', 'tianlongsi/doumugong', False),
	Exit('north', 'tianlongsi/qingxinge', False),
]
doushuai=Room('tianlongsi/doushuai', u'���ʴ�ʿԺ', None, 0, exits)

exits = [
	Exit('west', 'tianlongsi/wulege', False),
	Exit('south', 'tianlongsi/yaotai', False),
	Exit('east', 'tianlongsi/wuchangge', False),
]
huangtianmen=Room('tianlongsi/huangtianmen', u'������', 'tianlongsi', 0, exits)

exits = [
	Exit('north', 'tianlongsi/banruotai', False),
]
munitang=Room('tianlongsi/munitang', u'Ĳ����', None, 0, exits)

exits = [
	Exit('south', 'tianlongsi/doushuai', False),
	Exit('north', 'tianlongsi/wuwujing', False),
]
qingxinge=Room('tianlongsi/qingxinge', u'���ĸ�', None, 0, exits)

exits = [
	Exit('south', 'tianlongsi/wuchangge', False),
	Exit('north', 'tianlongsi/wuwoge', False),
]
ruihemen=Room('tianlongsi/ruihemen', u'�����', 'tianlongsi', 0, exits)

exits = [
	Exit('southeast', 'tianlongsi/doushuai', False),
	Exit('north', 'tianlongsi/cibeiyuan', False),
]
sanwugong=Room('tianlongsi/sanwugong', u'���޹�', None, 0, exits)

exits = [
	Exit('west', 'tianlongsi/wujingge', False),
	Exit('south', 'tianlongsi/baodian', False),
	Exit('north', 'tianlongsi/talin', False),
	Exit('east', 'tianlongsi/wuwoge', False),
]
ta1=Room('tianlongsi/ta1', u'������', 'tianlongsi', 0, exits)

exits = [
	Exit('west', 'tianlongsi/talin', False),
]
ta2=Room('tianlongsi/ta2', u'������', 'tianlongsi', 0, exits)

exits = [
	Exit('east', 'tianlongsi/talin', False),
]
ta3=Room('tianlongsi/ta3', u'������', 'tianlongsi', 0, exits)

exits = [
	Exit('down', 'tianlongsi/ta1', False),
]
tading=Room('tianlongsi/tading', u'����', 'tianlongsi', 0, exits)

exits = [
	Exit('west', 'tianlongsi/ta3', False),
	Exit('south', 'tianlongsi/ta1', False),
	Exit('north', 'tianlongsi/damen', False),
	Exit('east', 'tianlongsi/ta2', False),
]
talin=Room('tianlongsi/talin', u'����', 'tianlongsi', 0, exits)

exits = [
	Exit('west', 'tianlongsi/huangtianmen', False),
	Exit('north', 'tianlongsi/ruihemen', False),
]
wuchangge=Room('tianlongsi/wuchangge', u'�޳���', None, 0, exits)

exits = [
	Exit('south', 'tianlongsi/xianghemen', False),
	Exit('east', 'tianlongsi/ta1', False),
]
wujingge=Room('tianlongsi/wujingge', u'�޾���', None, 0, exits)

exits = [
	Exit('east', 'tianlongsi/huangtianmen', False),
	Exit('north', 'tianlongsi/xianghemen', False),
]
wulege=Room('tianlongsi/wulege', u'���ָ�', None, 0, exits)

exits = [
	Exit('west', 'tianlongsi/ta1', False),
	Exit('south', 'tianlongsi/ruihemen', False),
]
wuwoge=Room('tianlongsi/wuwoge', u'���Ҹ�', None, 0, exits)

exits = [
	Exit('west', 'tianlongsi/cibeiyuan', False),
	Exit('south', 'tianlongsi/qingxinge', False),
	Exit('east', 'tianlongsi/yuhuayuan', False),
	Exit('north', 'tianlongsi/yaotai', False),
]
wuwujing=Room('tianlongsi/wuwujing', u'���޾�', 'tianlongsi', 0, exits)

exits = [
	Exit('south', 'tianlongsi/wulege', False),
	Exit('north', 'tianlongsi/wujingge', False),
]
xianghemen=Room('tianlongsi/xianghemen', u'�����', 'tianlongsi', 0, exits)

exits = [
	Exit('south', 'tianlongsi/wuwujing', False),
	Exit('north', 'tianlongsi/huangtianmen', False),
]
yaotai=Room('tianlongsi/yaotai', u'�嶼��̨', 'tianlongsi', 0, exits)

exits = [
	Exit('west', 'tianlongsi/wuwujing', False),
	Exit('south', 'tianlongsi/doumugong', False),
]
yuhuayuan=Room('tianlongsi/yuhuayuan', u'�껨Ժ', None, 0, exits)

