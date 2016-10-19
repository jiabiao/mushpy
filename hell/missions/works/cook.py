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
	world.send(u"ask chu 工作\ncook")

mission = hell.core.missionfactory.register_mission(NAME, entry)



@trigger('^你隐隐约约的发现炒菜居然和武功有一些相通之处，真是奇妙。$',name='cook_1', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def work(*args):

	if hell.core.status.qn() < _config["max_qn"]:
		world.send(u"ask chu 工作\ncook")
	else:
		qn_mission_name = _config["qn_mission"]
		qn_mission_config = _config["qn_mission_config"]
		hell.missions.missionDispatcher.add_temp_mission(qn_mission_name,qn_mission_config)
		mission.end()





