# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('west', 'changan/yongtai_dadao2', False),
	Exit('north', 'pk/ready', False),
]
entry=Room('pk/entry', u'���˳����', None, 0, exits)

exits = [
	Exit('south', 'pk/entry', False),
]
ready=Room('pk/ready', u'���˳���Ϣ��', None, 0, exits)

exits = [
	Exit('south', 'pk/turen4', False),
	Exit('southwest', 'pk/turen3', False),
	Exit('east', 'pk/turen2', False),
]
turen1=Room('pk/turen1', u'���˳�', None, 0, exits)

exits = [
	Exit('west', 'pk/turen9', False),
	Exit('southwest', 'pk/turen12', False),
	Exit('north', 'pk/turen6', False),
]
turen10=Room('pk/turen10', u'���˳�', None, 0, exits)

exits = [
	Exit('northwest', 'pk/turen7', False),
	Exit('north', 'pk/turen8', False),
	Exit('east', 'pk/turen12', False),
]
turen11=Room('pk/turen11', u'���˳�', None, 0, exits)

exits = [
	Exit('west', 'pk/turen11', False),
	Exit('north', 'pk/turen9', False),
	Exit('northeast', 'pk/turen10', False),
]
turen12=Room('pk/turen12', u'¾�˳�', None, 0, exits)

exits = [
	Exit('west', 'pk/turen1', False),
	Exit('southeast', 'pk/turen6', False),
	Exit('south', 'pk/turen5', False),
]
turen2=Room('pk/turen2', u'���˳�', None, 0, exits)

exits = [
	Exit('south', 'pk/turen7', False),
	Exit('northeast', 'pk/turen1', False),
	Exit('east', 'pk/turen4', False),
]
turen3=Room('pk/turen3', u'���˳�', None, 0, exits)

exits = [
	Exit('west', 'pk/turen3', False),
	Exit('south', 'pk/turen8', False),
	Exit('north', 'pk/turen1', False),
	Exit('east', 'pk/turen5', False),
]
turen4=Room('pk/turen4', u'��ʬ��', None, 0, exits)

exits = [
	Exit('west', 'pk/turen4', False),
	Exit('south', 'pk/turen9', False),
	Exit('north', 'pk/turen2', False),
	Exit('east', 'pk/turen6', False),
]
turen5=Room('pk/turen5', u'�Ѫ��', None, 0, exits)

exits = [
	Exit('west', 'pk/turen5', False),
	Exit('northwest', 'pk/turen2', False),
	Exit('south', 'pk/turen10', False),
]
turen6=Room('pk/turen6', u'���˳�', None, 0, exits)

exits = [
	Exit('southeast', 'pk/turen11', False),
	Exit('north', 'pk/turen3', False),
	Exit('east', 'pk/turen8', False),
]
turen7=Room('pk/turen7', u'ɥ����', None, 0, exits)

exits = [
	Exit('west', 'pk/turen7', False),
	Exit('south', 'pk/turen11', False),
	Exit('north', 'pk/turen4', False),
	Exit('east', 'pk/turen9', False),
]
turen8=Room('pk/turen8', u'������', None, 0, exits)

exits = [
	Exit('west', 'pk/turen8', False),
	Exit('south', 'pk/turen12', False),
	Exit('north', 'pk/turen5', False),
	Exit('east', 'pk/turen10', False),
]
turen9=Room('pk/turen9', u'������', None, 0, exits)

