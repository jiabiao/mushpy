# coding=gbk

from mushpy import trigger,async,TriggerFlags,TimerTask,timer,TimerFlags
from sys import world
import hell

_room = None
_config = None
noPot = False


NAME = "yanjiu"

@async("lian_job")
def entry(config):
	global _room,_config
	if _room == None:
		_config = config
		room_id = config["room"]
		_room = hell.rooms.manager.get_room(room_id)
	yield hell.rooms.walker.runto(_room)
	world.send("cha\ncha 2\nyun dispel")
	yield TimerTask(0,0,3)
	world.send("c")

mission = hell.core.missionfactory.register_mission(NAME, entry)


@async()
def yanjiu():
	if hell.core.status.nei1() < 1500:
		yield hell.core.status.yun_recover()
	yield TimerTask(0,0,1)
	skill = hell.core.skills.min_skill(_config["skills"])
	world.send("yanjiu %s 300\nyun regenerate\nc" % (skill))	


@trigger('^你要向谁求婚',name='yanjiu1', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def yanjiu1(*args):
	global noPot

	if noPot:
		noPot = False
		mission.end()
		return
	yanjiu().begin()

	# if hell.core.status.dan_count() == 0:
	# 	get_dan().begin()
	# 	return
	





# @async("yanjiu_get_dan")
# def get_dan():
# 	yield TimerTask(0,0,20)
# 	world.send("halt\nej")
# 	yield hell.rooms.walker.runto(hell.rooms.city.kedian)
# 	world.send("ask shizhe 护心丹")
# 	yield TimerTask(0,0,1)	
# 	yield hell.rooms.walker.runto(_room)
# 	world.send("c")



@trigger('^你的潜能不够研究这么多次了。',name='yanjiu2', flags=TriggerFlags.KeepEval_Re_Replace, group=NAME)
def zhuxi2(*args):
	global noPot
	noPot = True

