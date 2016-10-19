# coding=gbk

from mushpy import trigger,async,TriggerFlags,TimerTask,timer,TimerFlags
from sys import world
import hell

_room = None
_config = None
noPot = False

NAME = "jiqu"

@async("jiqu_job")
def entry(config):
	global _room,_config
	if _room == None:
		_config = config
		room_id = config["room"]
		_room = hell.rooms.manager.get_room(room_id)
	yield hell.rooms.walker.runto(_room)
	world.send("jiqu")	
	world.doafter(10,"c")
mission = hell.core.missionfactory.register_mission(NAME, entry)


@trigger('^你要向谁求婚',name='jiqu1', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def jiqu1(*args):
	global noPot

	if noPot:
		noPot = False
		mission.end()
		return
	world.doafter(30,"c")







@trigger('^你现在积累的实战体会还太少。|^你将实战中获得的体会心得充分的消化吸收了。',name='jiqu2', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def jiqu2(*args):
	global noPot
	noPot = True

