# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('south', 'mingjiao/qiandian', False),
	Exit('enter', 'mingjiao/neishi', False),
]
dadian=Room('mingjiao/dadian', u'���̴��', None, 0, exits)

exits = [
	Exit('north', 'mingjiao/mjfengmen1', False),
]
daoshe=Room('mingjiao/daoshe', u'��������', None, 0, exits)

exits = [
	Exit('south', 'mingjiao/shanjiao', False),
	Exit('north', 'mingjiao/youjing', False),
]
donglu=Room('mingjiao/donglu', u'����ɽ´', 'mingjiao', 0, exits)

exits = [
	Exit('west', 'mingjiao/qiandian', False),
]
eastdian=Room('mingjiao/eastdian', u'���̶����', None, 0, exits)

exits = [
	Exit('east', 'mingjiao/square', False),
]
fangtang=Room('mingjiao/fangtang', u'���̷���', None, 0, exits)

exits = [
	Exit('south', 'mingjiao/mjfengmen1', False),
]
foshe=Room('mingjiao/foshe', u'�������', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/gebitan2', False),
	Exit('south', 'mingjiao/gebitan1', False),
	Exit('north', 'mingjiao/gebitan1', False),
	Exit('east', 'mingjiao/westroad2', False),
]
gebitan1=Room('mingjiao/gebitan1', u'���̲', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/gebitan3', False),
	Exit('south', 'mingjiao/gebitan2', False),
	Exit('north', 'mingjiao/gebitan2', False),
	Exit('east', 'mingjiao/gebitan1', False),
]
gebitan2=Room('mingjiao/gebitan2', u'���̲', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/gebitan3', False),
	Exit('south', 'mingjiao/gebitan3', False),
	Exit('north', 'mingjiao/gebitan4', False),
	Exit('east', 'mingjiao/gebitan2', False),
]
gebitan3=Room('mingjiao/gebitan3', u'���̲', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/gebitan4', False),
	Exit('south', 'mingjiao/gebitan3', False),
	Exit('north', 'mingjiao/gebitan5', False),
	Exit('east', 'mingjiao/gebitan4', False),
]
gebitan4=Room('mingjiao/gebitan4', u'���̲', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/shanjiao', False),
	Exit('south', 'mingjiao/gebitan4', False),
	Exit('north', 'mingjiao/gebitan5', False),
	Exit('east', 'mingjiao/gebitan5', False),
]
gebitan5=Room('mingjiao/gebitan5', u'���̲', None, 0, exits)

exits = [
]
gudi1=Room('mingjiao/gudi1', u'���عȵ�', 'mingjiao', 0, exits)

exits = [
]
gudi2=Room('mingjiao/gudi2', u'���عȵ�', 'mingjiao', 0, exits)

exits = [
	Exit('west', 'mingjiao/gudi5', False),
	Exit('south', 'mingjiao/gudi4', False),
]
gudi3=Room('mingjiao/gudi3', u'�����ɾ�', 'mingjiao', 0, exits)

exits = [
	Exit('north', 'mingjiao/gudi3', False),
]
gudi4=Room('mingjiao/gudi4', u'�����ɾ�', 'mingjiao', 0, exits)

exits = [
	Exit('east', 'mingjiao/gudi3', False),
]
gudi5=Room('mingjiao/gudi5', u'�����ɾ�', 'mingjiao', 0, exits)

exits = [
	Exit('out', 'mingjiao/hsqmen', False),
	Exit('north', 'mingjiao/hsqdating', False),
]
hsqchanglang=Room('mingjiao/hsqchanglang', u'��ˮ�쳤��', 'mingjiao', 0, exits)

exits = [
	Exit('south', 'mingjiao/hsqchanglang', False),
]
hsqdating=Room('mingjiao/hsqdating', u'��ˮ�����', None, 0, exits)

exits = [
	Exit('south', 'mingjiao/tohsq7', False),
	Exit('enter', 'mingjiao/hsqchanglang', False),
]
hsqmen=Room('mingjiao/hsqmen', u'��ˮ�����', 'mingjiao', 0, exits)

exits = [
	Exit('west', 'mingjiao/hsqtan1', False),
	Exit('south', 'mingjiao/hsqtan1', False),
	Exit('north', 'mingjiao/hsqtan2', False),
	Exit('east', 'mingjiao/hsqtan1', False),
]
hsqtan1=Room('mingjiao/hsqtan1', u'��̶', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/hsqtan2', False),
	Exit('south', 'mingjiao/hsqtan1', False),
	Exit('north', 'mingjiao/hsqtan2', False),
	Exit('east', 'mingjiao/hsqtan3', False),
]
hsqtan2=Room('mingjiao/hsqtan2', u'��̶', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/hsqtan2', False),
	Exit('south', 'mingjiao/hsqtan4', False),
	Exit('north', 'mingjiao/hsqtan3', False),
	Exit('east', 'mingjiao/hsqtan3', False),
]
hsqtan3=Room('mingjiao/hsqtan3', u'��̶', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/hsqtan4', False),
	Exit('south', 'mingjiao/hsqtan4', False),
	Exit('north', 'mingjiao/hsqtan3', False),
	Exit('east', 'mingjiao/hsqtan5', False),
]
hsqtan4=Room('mingjiao/hsqtan4', u'��̶', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/hsqtan4', False),
	Exit('south', 'mingjiao/hsqtan5', False),
	Exit('north', 'mingjiao/hsqtan5', False),
	Exit('east', 'mingjiao/hsqtan6', False),
]
hsqtan5=Room('mingjiao/hsqtan5', u'��̶', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/hsqtan5', False),
	Exit('up', 'mingjiao/hsqmen', False),
]
hsqtan6=Room('mingjiao/hsqtan6', u'��̶', None, 0, exits)

exits = [
	Exit('out', 'mingjiao/htqmen', False),
]
htqdating=Room('mingjiao/htqdating', u'���������', None, 0, exits)

exits = [
	Exit('south', 'mingjiao/tohtq7', False),
	Exit('enter', 'mingjiao/htqdating', False),
]
htqmen=Room('mingjiao/htqmen', u'��������', 'mingjiao', 0, exits)

exits = [
	Exit('west', 'mingjiao/huangtulu2', False),
	Exit('east', 'mingjiao/shanlu2', False),
]
huangtulu1=Room('mingjiao/huangtulu1', u'����С·', 'mingjiao', 0, exits)

exits = [
	Exit('east', 'mingjiao/huangtulu1', False),
	Exit('enter', 'mingjiao/shandong', False),
]
huangtulu2=Room('mingjiao/huangtulu2', u'����С·', 'mingjiao', 0, exits)

exits = [
	Exit('out', 'mingjiao/lhqyuan', False),
]
huroom=Room('mingjiao/huroom', u'ҽ��', 'mingjiao', 0, exits)

exits = [
	Exit('down', 'mingjiao/jmqshenmu', False),
]
jmqdating=Room('mingjiao/jmqdating', u'��ľ�����', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/jmqjiguan', False),
	Exit('south', 'mingjiao/jmqjiguan', False),
	Exit('north', 'mingjiao/jmqjiguan', False),
	Exit('east', 'mingjiao/jmqjiguan', False),
]
jmqjiguan=Room('mingjiao/jmqjiguan', u'��ľ�����', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/tojmq3', False),
	Exit('enter', 'mingjiao/jmqshulin1', False),
]
jmqmen=Room('mingjiao/jmqmen', u'��ľ�����', 'mingjiao', 0, exits)

exits = [
	Exit('east', 'mingjiao/jmqshulin6', False),
]
jmqshenmu=Room('mingjiao/jmqshenmu', u'��ľ����ľ', 'mingjiao', 0, exits)

exits = [
	Exit('out', 'mingjiao/jmqmen', False),
	Exit('west', 'mingjiao/jmqshulin1', False),
	Exit('south', 'mingjiao/jmqshulin1', False),
	Exit('north', 'mingjiao/jmqshulin2', False),
	Exit('east', 'mingjiao/jmqshulin1', False),
]
jmqshulin1=Room('mingjiao/jmqshulin1', u'��ľ������', 'mingjiao', 0, exits)

exits = [
	Exit('west', 'mingjiao/jmqshulin2', False),
	Exit('south', 'mingjiao/jmqshulin2', False),
	Exit('north', 'mingjiao/jmqshulin3', False),
	Exit('east', 'mingjiao/jmqshulin2', False),
]
jmqshulin2=Room('mingjiao/jmqshulin2', u'��ľ������', 'mingjiao', 0, exits)

exits = [
	Exit('west', 'mingjiao/jmqshulin3', False),
	Exit('south', 'mingjiao/jmqshulin3', False),
	Exit('north', 'mingjiao/jmqshulin3', False),
	Exit('east', 'mingjiao/jmqshulin4', False),
]
jmqshulin3=Room('mingjiao/jmqshulin3', u'��ľ������', 'mingjiao', 0, exits)

exits = [
	Exit('west', 'mingjiao/jmqshulin4', False),
	Exit('south', 'mingjiao/jmqshulin4', False),
	Exit('north', 'mingjiao/jmqshulin5', False),
	Exit('east', 'mingjiao/jmqshulin4', False),
]
jmqshulin4=Room('mingjiao/jmqshulin4', u'��ľ������', 'mingjiao', 0, exits)

exits = [
	Exit('west', 'mingjiao/jmqshulin6', False),
	Exit('south', 'mingjiao/jmqshulin5', False),
	Exit('north', 'mingjiao/jmqshulin5', False),
	Exit('east', 'mingjiao/jmqshulin5', False),
]
jmqshulin5=Room('mingjiao/jmqshulin5', u'��ľ������', 'mingjiao', 0, exits)

exits = [
	Exit('west', 'mingjiao/jmqjiguan', False),
	Exit('south', 'mingjiao/jmqshulin6', False),
	Exit('north', 'mingjiao/jmqshulin6', False),
	Exit('east', 'mingjiao/jmqshulin6', False),
]
jmqshulin6=Room('mingjiao/jmqshulin6', u'��ľ������', 'mingjiao', 0, exits)

exits = [
	Exit('west', 'mingjiao/lhqyuan', False),
]
lhqdating=Room('mingjiao/lhqdating', u'�һ������', None, 0, exits)

exits = [
	Exit('southdown', 'mingjiao/lhqyuan', False),
	Exit('northup', 'mingjiao/zhandao1', False),
]
lhqhoumen=Room('mingjiao/lhqhoumen', u'�һ������', 'mingjiao', 0, exits)

exits = [
	Exit('east', 'mingjiao/lhqyuan', False),
]
lhqlwch=Room('mingjiao/lhqlwch', u'���䳡', 'mingjiao', 0, exits)

exits = [
	Exit('southdown', 'mingjiao/lhqpaifang', False),
	Exit('enter', 'mingjiao/lhqyuan', False),
]
lhqmen=Room('mingjiao/lhqmen', u'�һ������', 'mingjiao', 0, exits)

exits = [
	Exit('southdown', 'mingjiao/shanlu4', False),
	Exit('northwest', 'mingjiao/tojmq1', False),
	Exit('northup', 'mingjiao/lhqmen', False),
	Exit('northeast', 'mingjiao/torjq1', False),
]
lhqpaifang=Room('mingjiao/lhqpaifang', u'�һ����Ʒ�', 'mingjiao', 0, exits)

exits = [
	Exit('out', 'mingjiao/lhqmen', False),
	Exit('west', 'mingjiao/lhqlwch', False),
	Exit('northup', 'mingjiao/lhqhoumen', False),
	Exit('east', 'mingjiao/lhqdating', False),
	Exit('enter', 'mingjiao/huroom', False),
]
lhqyuan=Room('mingjiao/lhqyuan', u'��Ժ', 'mingjiao', 0, exits)

exits = [
	Exit('north', 'mingjiao/westroad2', False),
]
miaorenbuluo=Room('mingjiao/miaorenbuluo', u'���˲���', None, 0, exits)

exits = [
	Exit('north', 'mingjiao/midao1', True),
]
midao0=Room('mingjiao/midao0', u'��', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/midao4', True),
	Exit('south', 'mingjiao/midao0', True),
	Exit('east', 'mingjiao/midao2', True),
	Exit('north', 'mingjiao/midao5', True),
]
midao1=Room('mingjiao/midao1', u'ʯ��', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/midao9', True),
	Exit('south', 'mingjiao/midao6', True),
	Exit('east', 'mingjiao/midao11', True),
	Exit('north', 'mingjiao/midao2', True),
]
midao10=Room('mingjiao/midao10', u'ʯ��', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/midao10', True),
	Exit('south', 'mingjiao/midao7', True),
	Exit('east', 'mingjiao/midao12', True),
	Exit('north', 'mingjiao/midao3', True),
]
midao11=Room('mingjiao/midao11', u'ʯ��', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/midao11', True),
	Exit('south', 'mingjiao/midao8', True),
	Exit('east', 'mingjiao/midao9', True),
	Exit('north', 'mingjiao/midao4', True),
]
midao12=Room('mingjiao/midao12', u'ʯ��', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/midao1', True),
	Exit('south', 'mingjiao/midao10', True),
	Exit('east', 'mingjiao/midao3', True),
	Exit('north', 'mingjiao/midao6', True),
]
midao2=Room('mingjiao/midao2', u'ʯ��', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/midao2', True),
	Exit('south', 'mingjiao/midao11', True),
	Exit('east', 'mingjiao/midao4', True),
	Exit('north', 'mingjiao/midao7', True),
]
midao3=Room('mingjiao/midao3', u'ʯ��', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/midao3', True),
	Exit('south', 'mingjiao/midao12', True),
	Exit('east', 'mingjiao/midao1', True),
	Exit('north', 'mingjiao/midao8', True),
]
midao4=Room('mingjiao/midao4', u'ʯ��', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/midao8', True),
	Exit('south', 'mingjiao/midao1', True),
	Exit('east', 'mingjiao/midao6', True),
	Exit('north', 'mingjiao/midao9', True),
]
midao5=Room('mingjiao/midao5', u'ʯ��', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/midao5', True),
	Exit('south', 'mingjiao/midao2', True),
	Exit('east', 'mingjiao/midao7', True),
	Exit('north', 'mingjiao/midao10', True),
]
midao6=Room('mingjiao/midao6', u'ʯ��', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/midao6', True),
	Exit('south', 'mingjiao/midao3', True),
	Exit('east', 'mingjiao/midao8', True),
	Exit('north', 'mingjiao/midao11', True),
]
midao7=Room('mingjiao/midao7', u'ʯ��', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/midao7', True),
	Exit('south', 'mingjiao/midao4', True),
	Exit('east', 'mingjiao/midao5', True),
	Exit('north', 'mingjiao/midao12', True),
]
midao8=Room('mingjiao/midao8', u'ʯ��', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/midao12', True),
	Exit('south', 'mingjiao/midao5', True),
	Exit('east', 'mingjiao/midao10', True),
	Exit('north', 'mingjiao/mishi', True),
]
midao9=Room('mingjiao/midao9', u'ʯ��', None, 0, exits)

exits = [
	Exit('south', 'mingjiao/midao9', True),
	Exit('up', 'mingjiao/neishi', False),
]
mishi=Room('mingjiao/mishi', u'ʯ��', None, 0, exits)

exits = [
	Exit('southwest', 'mingjiao/mjsimen1', False),
	Exit('northeast', 'mingjiao/mjdimen1', False),
]
mjdimen=Room('mingjiao/mjdimen', u'�ݵ�', 'mingjiao', 0, exits)

exits = [
	Exit('southwest', 'mingjiao/mjdimen', False),
	Exit('enter', 'mingjiao/nushe', False),
]
mjdimen1=Room('mingjiao/mjdimen1', u'�ſ�', 'mingjiao', 0, exits)

exits = [
	Exit('southeast', 'mingjiao/mjfengmen1', False),
	Exit('northwest', 'mingjiao/mjsimen1', False),
]
mjfengmen=Room('mingjiao/mjfengmen', u'����', 'mingjiao', 0, exits)

exits = [
	Exit('northwest', 'mingjiao/mjfengmen', False),
	Exit('south', 'mingjiao/daoshe', False),
	Exit('north', 'mingjiao/foshe', False),
]
mjfengmen1=Room('mingjiao/mjfengmen1', u'����', 'mingjiao', 0, exits)

exits = [
	Exit('southwest', 'mingjiao/mjleimen1', False),
	Exit('northeast', 'mingjiao/mjsimen1', False),
]
mjleimen=Room('mingjiao/mjleimen', u'��ʯ��', 'mingjiao', 0, exits)

exits = [
	Exit('northeast', 'mingjiao/mjleimen', False),
	Exit('enter', 'mingjiao/sushe', False),
]
mjleimen1=Room('mingjiao/mjleimen1', u'�ſ�', 'mingjiao', 0, exits)

exits = [
	Exit('south', 'mingjiao/mjsimen1', False),
	Exit('north', 'mingjiao/tomen2', False),
]
mjsimen=Room('mingjiao/mjsimen', u'��ʯ��', 'mingjiao', 0, exits)

exits = [
	Exit('southeast', 'mingjiao/mjfengmen', False),
	Exit('northwest', 'mingjiao/mjtianmen', False),
	Exit('southwest', 'mingjiao/mjleimen', False),
	Exit('northeast', 'mingjiao/mjdimen', False),
	Exit('north', 'mingjiao/mjsimen', False),
]
mjsimen1=Room('mingjiao/mjsimen1', u'�㳡', 'mingjiao', 0, exits)

exits = [
	Exit('southeast', 'mingjiao/mjsimen1', False),
	Exit('northwest', 'mingjiao/mjtianmen1', False),
]
mjtianmen=Room('mingjiao/mjtianmen', u'������', 'mingjiao', 0, exits)

exits = [
	Exit('southeast', 'mingjiao/mjtianmen', False),
	Exit('enter', 'mingjiao/nanshe', False),
]
mjtianmen1=Room('mingjiao/mjtianmen1', u'�ſ�', 'mingjiao', 0, exits)

exits = [
	Exit('out', 'mingjiao/mjtianmen1', False),
]
nanshe=Room('mingjiao/nanshe', u'��������', None, 0, exits)

exits = [
	Exit('out', 'mingjiao/dadian', False),
]
neishi=Room('mingjiao/neishi', u'��������', None, 1, exits)

exits = [
	Exit('out', 'mingjiao/mjdimen1', False),
]
nushe=Room('mingjiao/nushe', u'����Ů��', None, 0, exits)

exits = [
	Exit('southdown', 'mingjiao/square', False),
	Exit('west', 'mingjiao/westdian', False),
	Exit('north', 'mingjiao/dadian', False),
	Exit('east', 'mingjiao/eastdian', False),
]
qiandian=Room('mingjiao/qiandian', u'����ǰ��', None, 0, exits)

exits = [
	Exit('south', 'mingjiao/rjqyuan', False),
]
rjqdating=Room('mingjiao/rjqdating', u'��������', None, 0, exits)

exits = [
	Exit('north', 'mingjiao/rjqmishi', False),
]
rjqjiguan=Room('mingjiao/rjqjiguan', u'�ܵ�', None, 0, exits)

exits = [
	Exit('north', 'mingjiao/rjqyuan', False),
]
rjqlwch=Room('mingjiao/rjqlwch', u'���䳡', None, 0, exits)

exits = [
	Exit('east', 'mingjiao/torjq3', False),
	Exit('enter', 'mingjiao/rjqyuan', False),
]
rjqmen=Room('mingjiao/rjqmen', u'����', 'mingjiao', 0, exits)

exits = [
	Exit('east', 'mingjiao/rjqyuan', False),
	Exit('up', 'mingjiao/rjqmenlou2', False),
]
rjqmenlou1=Room('mingjiao/rjqmenlou1', u'��¥һ��', None, 0, exits)

exits = [
	Exit('up', 'mingjiao/rjqmenlou3', False),
	Exit('down', 'mingjiao/rjqmenlou1', False),
]
rjqmenlou2=Room('mingjiao/rjqmenlou2', u'��¥����', None, 0, exits)

exits = [
	Exit('down', 'mingjiao/rjqmenlou2', False),
]
rjqmenlou3=Room('mingjiao/rjqmenlou3', u'��¥����', None, 0, exits)

exits = [
	Exit('north', 'mingjiao/rjqjiguan', False),
]
rjqmidao=Room('mingjiao/rjqmidao', u'�ܵ�', None, 0, exits)

exits = [
	Exit('south', 'mingjiao/rjqjiguan', False),
	Exit('down', 'mingjiao/rjqmenlou1', False),
]
rjqmishi=Room('mingjiao/rjqmishi', u'����', None, 0, exits)

exits = [
	Exit('out', 'mingjiao/rjqmen', False),
	Exit('west', 'mingjiao/rjqmenlou1', False),
	Exit('south', 'mingjiao/rjqlwch', False),
	Exit('north', 'mingjiao/rjqdating', False),
]
rjqyuan=Room('mingjiao/rjqyuan', u'��Ժ', 'mingjiao', 0, exits)

exits = [
	Exit('out', 'mingjiao/huangtulu2', False),
]
shandong=Room('mingjiao/shandong', u'�����ܶ�', 'mingjiao', 0, exits)

exits = [
	Exit('west', 'mingjiao/tomen2', False),
	Exit('north', 'mingjiao/donglu', False),
	Exit('east', 'mingjiao/gebitan5', False),
]
shanjiao=Room('mingjiao/shanjiao', u'����ɽ��', 'mingjiao', 0, exits)

exits = [
	Exit('eastdown', 'mingjiao/shanmen', False),
	Exit('westup', 'mingjiao/shanlu2', False),
]
shanlu1=Room('mingjiao/shanlu1', u'��ʯ��', 'mingjiao', 0, exits)

exits = [
	Exit('west', 'mingjiao/huangtulu1', False),
	Exit('northup', 'mingjiao/shanlu3', False),
	Exit('eastdown', 'mingjiao/shanlu1', False),
]
shanlu2=Room('mingjiao/shanlu2', u'��ʯ��', 'mingjiao', 0, exits)

exits = [
	Exit('southdown', 'mingjiao/shanlu2', False),
	Exit('northup', 'mingjiao/shanlu4', False),
	Exit('up', 'mingjiao/xuantianshi', False),
]
shanlu3=Room('mingjiao/shanlu3', u'������', 'mingjiao', 0, exits)

exits = [
	Exit('southdown', 'mingjiao/shanlu3', False),
	Exit('northup', 'mingjiao/lhqpaifang', False),
]
shanlu4=Room('mingjiao/shanlu4', u'��ʯ��', 'mingjiao', 0, exits)

exits = [
	Exit('east', 'mingjiao/tomen1', False),
	Exit('westup', 'mingjiao/shanlu1', False),
]
shanmen=Room('mingjiao/shanmen', u'����ɽ��', 'mingjiao', 0, exits)

exits = [
	Exit('west', 'mingjiao/fangtang', False),
	Exit('south', 'mingjiao/tianweitang', False),
	Exit('northup', 'mingjiao/qiandian', False),
	Exit('east', 'mingjiao/xingtang', False),
]
square=Room('mingjiao/square', u'��Ժ', 'mingjiao', 0, exits)

exits = [
	Exit('out', 'mingjiao/mjleimen1', False),
]
sushe=Room('mingjiao/sushe', u'��������', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/tianweitang', False),
]
tianshitang=Room('mingjiao/tianshitang', u'������', None, 0, exits)

exits = [
	Exit('southdown', 'mingjiao/zhandao2', False),
	Exit('west', 'mingjiao/ziweitang', False),
	Exit('north', 'mingjiao/square', False),
	Exit('east', 'mingjiao/tianshitang', False),
]
tianweitang=Room('mingjiao/tianweitang', u'��΢��', None, 0, exits)

exits = [
	Exit('southeast', 'mingjiao/torjq3', False),
	Exit('northwest', 'mingjiao/tohsq2', False),
]
tohsq1=Room('mingjiao/tohsq1', u'ɽ·', 'mingjiao', 0, exits)

exits = [
	Exit('southeast', 'mingjiao/tohsq1', False),
	Exit('northwest', 'mingjiao/tohsq3', False),
	Exit('north', 'mingjiao/tohsq4', False),
]
tohsq2=Room('mingjiao/tohsq2', u'ɽ·', 'mingjiao', 0, exits)

exits = [
	Exit('southeast', 'mingjiao/tohsq2', False),
]
tohsq3=Room('mingjiao/tohsq3', u'ɽ·', 'mingjiao', 0, exits)

exits = [
	Exit('south', 'mingjiao/tohsq2', False),
	Exit('north', 'mingjiao/tohsq5', False),
]
tohsq4=Room('mingjiao/tohsq4', u'ɽ·', 'mingjiao', 0, exits)

exits = [
	Exit('south', 'mingjiao/tohsq4', False),
	Exit('north', 'mingjiao/tohsq6', False),
]
tohsq5=Room('mingjiao/tohsq5', u'ɽ·', 'mingjiao', 0, exits)

exits = [
	Exit('south', 'mingjiao/tohsq5', False),
	Exit('north', 'mingjiao/tohsq7', False),
]
tohsq6=Room('mingjiao/tohsq6', u'ɽ·', 'mingjiao', 0, exits)

exits = [
	Exit('south', 'mingjiao/tohsq6', False),
	Exit('north', 'mingjiao/hsqmen', False),
]
tohsq7=Room('mingjiao/tohsq7', u'ɽ·', 'mingjiao', 0, exits)

exits = [
	Exit('southwest', 'mingjiao/tojmq3', False),
	Exit('northeast', 'mingjiao/tohtq2', False),
]
tohtq1=Room('mingjiao/tohtq1', u'ɽ·', 'mingjiao', 0, exits)

exits = [
	Exit('southwest', 'mingjiao/tohtq1', False),
	Exit('northdown', 'mingjiao/tohtq3', False),
]
tohtq2=Room('mingjiao/tohtq2', u'ɽ·', 'mingjiao', 0, exits)

exits = [
	Exit('southup', 'mingjiao/tohtq2', False),
	Exit('enter', 'mingjiao/tohtq4', False),
]
tohtq3=Room('mingjiao/tohtq3', u'ɽ·', 'mingjiao', 0, exits)

exits = [
	Exit('out', 'mingjiao/tohtq3', False),
	Exit('north', 'mingjiao/tohtq5', False),
]
tohtq4=Room('mingjiao/tohtq4', u'ɽ��', 'mingjiao', 0, exits)

exits = [
	Exit('south', 'mingjiao/tohtq4', False),
	Exit('east', 'mingjiao/tohtq6', False),
]
tohtq5=Room('mingjiao/tohtq5', u'ɽ��', 'mingjiao', 0, exits)

exits = [
	Exit('west', 'mingjiao/tohtq5', False),
	Exit('north', 'mingjiao/htqmen', False),
]
tohtq6=Room('mingjiao/tohtq6', u'ɽ��', 'mingjiao', 0, exits)

exits = [
	Exit('west', 'mingjiao/tohtq5', False),
	Exit('north', 'mingjiao/tohtq7', False),
]
tohtq7=Room('mingjiao/tohtq7', u'ɽ��', 'mingjiao', 0, exits)

exits = [
	Exit('southeast', 'mingjiao/lhqpaifang', False),
	Exit('northwest', 'mingjiao/tojmq2', False),
]
tojmq1=Room('mingjiao/tojmq1', u'��ʯ���', 'mingjiao', 0, exits)

exits = [
	Exit('southeast', 'mingjiao/tojmq1', False),
	Exit('northwest', 'mingjiao/tojmq3', False),
]
tojmq2=Room('mingjiao/tojmq2', u'��ʯ���', 'mingjiao', 0, exits)

exits = [
	Exit('southeast', 'mingjiao/tojmq2', False),
	Exit('northeast', 'mingjiao/tohtq1', False),
	Exit('east', 'mingjiao/jmqmen', False),
]
tojmq3=Room('mingjiao/tojmq3', u'��ʯ���', 'mingjiao', 0, exits)

exits = [
	Exit('west', 'mingjiao/shanmen', False),
	Exit('east', 'mingjiao/tomen2', False),
]
tomen1=Room('mingjiao/tomen1', u'��ʯ��', 'mingjiao', 0, exits)

exits = [
	Exit('west', 'mingjiao/tomen1', False),
	Exit('south', 'mingjiao/mjsimen', False),
	Exit('east', 'mingjiao/shanjiao', False),
]
tomen2=Room('mingjiao/tomen2', u'��ʯ��', 'mingjiao', 0, exits)

exits = [
	Exit('southwest', 'mingjiao/lhqpaifang', False),
	Exit('northeast', 'mingjiao/torjq2', False),
]
torjq1=Room('mingjiao/torjq1', u'��ʯ���', 'mingjiao', 0, exits)

exits = [
	Exit('southwest', 'mingjiao/torjq1', False),
	Exit('northeast', 'mingjiao/torjq3', False),
]
torjq2=Room('mingjiao/torjq2', u'��ʯ���', 'mingjiao', 0, exits)

exits = [
	Exit('west', 'mingjiao/rjqmen', False),
	Exit('northwest', 'mingjiao/tohsq1', False),
	Exit('southwest', 'mingjiao/torjq2', False),
]
torjq3=Room('mingjiao/torjq3', u'��ʯ���', 'mingjiao', 0, exits)

exits = [
	Exit('east', 'mingjiao/qiandian', False),
]
westdian=Room('mingjiao/westdian', u'���������', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/westroad2', False),
	Exit('east', 'xingxiu/silk2', False),
]
westroad1=Room('mingjiao/westroad1', u'ɽ·', 'mingjiao', 0, exits)

exits = [
	Exit('west', 'mingjiao/gebitan1', False),
	Exit('south', 'mingjiao/miaorenbuluo', False),
	Exit('east', 'mingjiao/westroad1', False),
]
westroad2=Room('mingjiao/westroad2', u'��ɽ', None, 0, exits)

exits = [
	Exit('west', 'mingjiao/square', False),
]
xingtang=Room('mingjiao/xingtang', u'����', None, 1, exits)

exits = [
	Exit('down', 'mingjiao/shanlu3', False),
]
xuantianshi=Room('mingjiao/xuantianshi', u'����ʯ', 'mingjiao', 0, exits)

exits = [
	Exit('south', 'mingjiao/donglu', False),
]
youjing=Room('mingjiao/youjing', u'�����ľ�', 'mingjiao', 0, exits)

exits = [
	Exit('southdown', 'mingjiao/lhqhoumen', False),
	Exit('northup', 'mingjiao/zhandao2', False),
]
zhandao1=Room('mingjiao/zhandao1', u'ջ��', 'mingjiao', 0, exits)

exits = [
	Exit('southdown', 'mingjiao/zhandao1', False),
	Exit('northup', 'mingjiao/tianweitang', False),
]
zhandao2=Room('mingjiao/zhandao2', u'ջ��', 'mingjiao', 0, exits)

exits = [
	Exit('east', 'mingjiao/tianweitang', False),
]
ziweitang=Room('mingjiao/ziweitang', u'��΢��', None, 0, exits)

