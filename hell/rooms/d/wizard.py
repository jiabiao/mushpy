# coding=gbk
from _objects import Room,Exit

exits = [
	Exit('southeast', 'city/wumiao', True),
	Exit('up', 'wizard/wizard_room', False),
]
guest_room=Room('wizard/guest_room', u'��ʦ�����', None, 0, exits)

exits = [
	Exit('down', 'wizard/guest_room', False),
]
wizard_room=Room('wizard/wizard_room', u'��ʦ��Ϣ��', None, 1, exits)

