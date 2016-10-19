# coding=gbk

from mushpy import trigger,async,TriggerFlags,TimerTask
from sys import world
import hell

_room = None
_config = None
noPot = False


NAME = "master"

@async("xue_master_job")
def entry(config):
	global _room,_config
	if _room == None:
		_config = config
		room_id = config["room"]
		_room = hell.rooms.manager.get_room(room_id)
	yield hell.rooms.walker.runto(_room)	
	world.send("cha")	
	yield TimerTask(0,0,1)
	world.send("cha 2")	
	yield TimerTask(0,0,1)
	yield hell.core.status.yun_dispel()
	world.send("c")

mission = hell.core.missionfactory.register_mission(NAME, entry)


@async()
def learn():
	if hell.core.status.nei1() < 1000:
		yield hell.core.status.yun_recover()
	yield TimerTask(0,0,1)
	skill = hell.core.skills.min_skill(_config["skills"])
	master = _config["master"]
	world.send("xue %s %s 300\nyun regenerate\nhp\nc" % (master, skill))	

@trigger('^你的潜能不够学习这么多次了。',name='xue_master1', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def zhuxi2(*args):	
	global noPot
	noPot = True




@trigger('^这项技能你的程度已经不输你师父了。',name='xue_master2', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def lian1(*args):
	skill = hell.core.skills.min_skill(_config["skills"])
	_config["skills"].remove(skill)



@trigger('^你要向谁求婚',name='xue_master4', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def zhuxi4(*args):
	global noPot
	
	if noPot:
		noPot = False
		mission.end()
		return
	learn().begin()



