# coding=gbk
from sys import world  
from mushpy import trigger,async,TriggerFlags
import hell

_room = None
_config = None
NAME = "cook"

@async("cook_job")
def entry(config):	
	global _room
	global _config

	if _room == None:
		_config = config
		room_id = config["room"]
		_room = hell.rooms.manager.get_room(room_id)

	yield hell.rooms.walker.runto(_room)
	world.send(u"ask chu ����\ncook")

mission = hell.core.missionfactory.register_mission(NAME, entry)



@trigger('^������ԼԼ�ķ��ֳ��˾�Ȼ���书��һЩ��֮ͨ�����������$',name='cook_1', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def work(*args):

	if hell.core.status.qn() < _config["max_qn"]:
		world.send(u"ask chu ����\ncook")
	else:
		qn_mission_name = _config["qn_mission"]
		qn_mission_config = _config["qn_mission_config"]
		hell.missions.missionDispatcher.add_temp_mission(qn_mission_name,qn_mission_config)
		mission.end()





